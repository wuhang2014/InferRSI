"""Check the editable handbook and optionally refresh its Markdown table of contents."""

from __future__ import annotations

import argparse
import json
import posixpath
import re
import subprocess
from collections import defaultdict
from pathlib import Path, PurePosixPath
from urllib.parse import unquote

from inferrsi.knowledge.handbook import BOOK, MARKUP, Handbook, prose_lines

PROJECT = Path(__file__).resolve().parents[1]
CHAPTERS = {
    "paths": (
        "Reading paths",
        "Follow a question through a sequence of lessons and a worked check.",
    ),
    "foundations": (
        "Foundations",
        "Work through measurement boundaries, resource bounds and ownership.",
    ),
    "methods": ("Methods", "Choose a method by the decision or measurement you need to make."),
    "hardware": ("Hardware", "Start with the accelerator or host resource you are investigating."),
    "frameworks": (
        "Frameworks",
        "Follow a tensor, stream, operator or checkpoint through its framework.",
    ),
    "repositories": (
        "Inference engines",
        "Study an engine's request lifecycle, integration points and validation.",
    ),
    "records": (
        "Research records",
        "Browse by learning tier, source repository, backend and component.",
    ),
    "models": ("Model profiles", "Identify the components and research sources for a model."),
    "workflows": (
        "Workflows",
        "Trace the steps for planning, checking evidence and maintaining knowledge.",
    ),
    "library": (
        "Source library guide",
        "Consult the original library's routing and ownership guidance.",
    ),
}


def contents(book: Handbook) -> dict[str, str]:
    chapters = defaultdict(list)
    for page in book.by_path.values():
        chapters[PurePosixPath(page.path).parts[1]].append(page)
    output = {}
    home = [
        "# Handbook contents",
        "",
        "Choose a chapter, or start with a worked question. [Handbook introduction](../README.md)",
        "",
    ]

    def link(page):
        title = page.title.replace("[", r"\[").replace("]", r"\]")
        return f"[{title}](../{page.path})"

    def directory(pages, depth, indent, lines):
        groups = defaultdict(list)
        for page in pages:
            parts = PurePosixPath(page.path).parts
            if len(parts) == depth + 1:
                lines.append(indent + "- " + link(page))
            else:
                groups[parts[depth]].append(page)
        for folder, children in sorted(groups.items()):
            owners = [
                p
                for p in children
                if len(PurePosixPath(p.path).parts) == depth + 2
                and PurePosixPath(p.path).name in {"lesson.md", "overview.md"}
            ]
            owner = owners[0] if owners else None
            label = link(owner) if owner else folder.replace("-", " ").replace("_", " ")
            lines.append(indent + "- " + label)
            directory([p for p in children if p is not owner], depth + 1, indent + "  ", lines)

    for chapter in dict.fromkeys([*CHAPTERS, *sorted(chapters)]):
        if chapter not in chapters:
            continue
        title, description = CHAPTERS.get(chapter, (chapter.replace("-", " ").title(), ""))
        home.append(f"- [{title}]({chapter}.md) — {description}")
        lines = [f"# {title}", "", description, "", "[All chapters](README.md)", ""]
        directory(chapters[chapter], 2, "", lines)
        output[chapter + ".md"] = "\n".join(lines) + "\n"
    output["README.md"] = "\n".join(home) + "\n"
    return output


def check_migration(root: Path, book: Handbook, local_links: dict[str, set[Path]]) -> int:
    receipt = json.loads((root / "migration.json").read_text(encoding="utf-8"))
    revision = receipt["revision"]
    if receipt["schema"] != 1 or not re.fullmatch("[0-9a-f]{40}", revision):
        raise ValueError("Invalid source edition in migration.json")
    data = "src/inferrsi/knowledge/data"
    raw = subprocess.run(
        ["git", "-C", str(PROJECT), "ls-tree", "-rz", "--name-only", revision, "--", data],
        capture_output=True,
        check=True,
    ).stdout
    expected = {
        p.removeprefix(data + "/")
        for p in raw.decode().split("\0")
        if p and not p.startswith(data + "/handbook/")
    }
    seen = set()
    for role in ("converted", "catalog_aliases", "resources"):
        for path, ref in receipt[role].items():
            page, _ = book.resolve(ref)
            if page.id != ref or path in seen:
                raise ValueError(f"Invalid or repeated migration mapping: {path}")
            seen.add(path)
            source = (root.parent / path).resolve()
            if source not in local_links[page.path]:
                raise ValueError(f"Missing {role} source link on {page.path}: {path}")
            if role == "catalog_aliases":
                identity = json.loads(source.read_text(encoding="utf-8"))["id"]
                if book.resolve("package:" + identity)[0] is not page:
                    raise ValueError(f"Catalog alias points to a different page: {identity}")
    if expected != seen:
        raise ValueError(f"Migration differs from the source tree: {sorted(expected ^ seen)}")
    return len(seen)


def check(root: Path = BOOK, *, write_contents: bool = False) -> dict:
    book = Handbook(root)
    nav = root / "contents"
    expected = contents(book)
    if write_contents:
        nav.mkdir(exist_ok=True)
        for name, value in expected.items():
            path = nav / name
            if not path.exists() or path.read_text(encoding="utf-8") != value:
                path.write_text(value, encoding="utf-8", newline="\n")
    actual = {p.name: p.read_text(encoding="utf-8") for p in nav.glob("*.md")}
    if actual != expected:
        raise ValueError(
            "Contents differ. Run tools/check_handbook.py --write-contents "
            "and remove any obsolete chapter index."
        )
    local_links = defaultdict(set)
    for path in root.rglob("*.md"):
        name = path.relative_to(root).as_posix()
        for _, line in prose_lines(path.read_text(encoding="utf-8").splitlines()):
            for m in MARKUP.finditer(line):
                href = m["target"]
                if not href or re.match(r"[a-z][\w+.-]*:", href, re.I):
                    continue
                filename, _, key = unquote(href).partition("#")
                target = (path.parent / filename).resolve() if filename else path.resolve()
                if not target.is_relative_to(root.parent.resolve()) or not target.is_file():
                    raise ValueError(f"Missing local link in {name}: {href}")
                local_links[name].add(target)
                target_name = posixpath.normpath(posixpath.join(posixpath.dirname(name), filename))
                page = book.by_path.get(target_name if filename else name)
                if page and key and key not in page.sections:
                    raise ValueError(f"Missing section link in {name}: {href}")
    for page in book.by_path.values():
        list(book.edges(page))
        if page.kind == "path":
            book.compose([page.id])
    return {
        "source_files": check_migration(root, book, local_links),
        "pages": len(book.by_path),
        "sections": sum(len(p.sections) for p in book.by_path.values()),
        "paths": sum(p.kind == "path" for p in book.by_path.values()),
    }


if __name__ == "__main__":
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--write-contents", action="store_true")
    try:
        print(json.dumps(check(write_contents=parser.parse_args().write_contents), indent=2))
    except (OSError, ValueError, subprocess.CalledProcessError) as exc:
        parser.exit(1, f"{exc}\n")
