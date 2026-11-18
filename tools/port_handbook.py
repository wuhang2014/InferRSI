"""Seed an empty handbook from the knowledge files in a committed Git tree.

The output is an editable edition. Re-import into a new directory to compare
editions without overwriting an editor's changes. Requires the dev/skills extra.
"""

from __future__ import annotations

import argparse
import io
import json
import posixpath
import re
import subprocess
import tarfile
import tempfile
from dataclasses import dataclass, field
from pathlib import Path, PurePosixPath
from urllib.parse import unquote

from inferrsi.knowledge.handbook import MARKUP, Page, prose_lines
from inferrsi.knowledge.skill_catalog import _frontmatter

PROJECT = Path(__file__).resolve().parents[1]
DATA = "src/inferrsi/knowledge/data"
REPOSITORY = "https://github.com/InferMatrixLab/InferRSI"
SOURCE_DIRS = ("skill_library", "repo_packs", "knowledge_packs", "research_profiles")
SOURCES = (*SOURCE_DIRS, "query_aliases.json")


def snapshot(revision: str):
    def git(*args: str) -> bytes:
        return subprocess.run(
            ["git", "--no-replace-objects", "-C", str(PROJECT), *args],
            capture_output=True,
            check=True,
        ).stdout

    revision = (
        git("rev-parse", "--verify", "--end-of-options", revision + "^{commit}").decode().strip()
    )
    names = git("ls-tree", "-r", "-z", "--name-only", revision).decode().split("\0")
    tree = {PurePosixPath(name) for name in names if name}
    archive = git("archive", "--format=tar", revision, "--", *(f"{DATA}/{s}" for s in SOURCES))
    with tarfile.open(fileobj=io.BytesIO(archive)) as tar:
        docs = {
            member.name.removeprefix(DATA + "/"): tar.extractfile(member).read().decode("utf-8")
            for member in tar
            if member.isfile()
        }
    return revision, tree, docs


def readable(key: str) -> str:
    return key.replace("_", " ").capitalize()


def bullets(value, indent: str = "") -> list[str]:
    """Keep structure and scope on nested facts, including empty and false values."""
    lines = []
    if isinstance(value, dict):
        for key, item in value.items():
            if isinstance(item, (dict, list)) and item:
                lines.append(f"{indent}- **{readable(key)}**")
                lines.extend(bullets(item, indent + "  "))
            else:
                lines.append(f"{indent}- **{readable(key)}** — {scalar(item)}")
    elif isinstance(value, list):
        for item in value:
            if isinstance(item, dict):
                lines.extend(bullets(item, indent))
                lines.append("")
            else:
                lines.append(f"{indent}- {scalar(item)}")
    else:
        lines.append(f"{indent}- {scalar(value)}")
    return lines


def scalar(value) -> str:
    if isinstance(value, str):
        return f"<{value}>" if value.startswith("https://") and " " not in value else value
    return f"`{json.dumps(value, ensure_ascii=False)}`"


def block(title: str, value) -> str:
    return "\n".join([f"## {title}", "", *bullets(value)]).rstrip()


CARD_FIELDS = {
    "applicability": "When this applies",
    "claims": "What the source reports",
    "downstream_impact": "Consequences for a downstream project",
    "recommendations": "Putting the idea to work",
    "validation_plan": "How to check it",
    "limitations": "Limits of this evidence",
    "sources": "Sources",
    "attribution": "Attribution",
    "translations": "Available translation",
}


def sections(text: str) -> str:
    """Give each source heading a persistent, linkable key at the time of import."""
    lines = text.splitlines()
    seen = set()
    for i, line in prose_lines(lines):
        lines[i] = line = line.rstrip()
        heading = re.fullmatch(r"#{2,6} (.+)", line)
        if heading:
            slug = re.sub(r"[^\w]+", "-", heading[1].casefold()).strip("-")[:80].rstrip("-")
            base = "unit-" + (slug or "section")
            key = base
            suffix = 2
            while key in seen:
                key = f"{base}-{suffix}"
                suffix += 1
            seen.add(key)
            lines[i] = f'<a id="{key}"></a>\n' + line
    return "\n".join(lines)


def prepare_prose(body: str) -> str:
    """Keep a compiled source's subdocuments and citations readable in isolation."""
    lines = body.splitlines()
    definitions = {}
    nested = False
    for i, line in prose_lines(lines):
        definition = re.fullmatch(r"\[([^\]]+)\]:\s+(\S+)", line)
        if definition:
            label, url = definition.groups()
            definitions[label.casefold()] = url
            lines[i] = f"- [{label}]({url})"
        if line.startswith("# "):
            nested = True
        if nested and re.match(r"^#{1,5} ", line):
            lines[i] = "#" + line
    if definitions:
        reference = re.compile(
            r"(?P<code>(?P<tick>`+).*?(?P=tick))|"
            r"\[(?P<label>[^\[\]\n]+)\](?!\()"
            r"(?:\[(?P<id>[^\[\]\n]*)\])?"
        )

        def resolve(match):
            if match["code"]:
                return match[0]
            key = (match["id"] or match["label"]).casefold()
            if key in definitions:
                return f"[{match['label']}]({definitions[key]})"
            # Some source ledgers cite several keys within one pair of brackets.
            labels = [label.strip() for label in match["label"].split(",")]
            if len(labels) > 1 and all(label.casefold() in definitions for label in labels):
                return ", ".join(f"[{label}]({definitions[label.casefold()]})" for label in labels)
            return match[0]

        for i, line in prose_lines(lines):
            lines[i] = reference.sub(resolve, line)
    return "\n".join(lines)


def stable_links(pages: dict[str, str]) -> None:
    """Move links to source heading slugs onto the corresponding permanent anchors."""
    targets = {}
    for path, text in pages.items():
        page = Page.parse(path, text)
        anchors = {}
        for key, title in [("", page.title), *((s.key, s.title) for s in page.sections.values())]:
            label = re.sub(r"\[([^\]]*)\]\([^)]+\)", r"\1", title)
            base = re.sub(r"[^\w -]", "", label.lower()).replace(" ", "-")
            slug = base
            suffix = 1
            while slug in anchors:
                slug = f"{base}-{suffix}"
                suffix += 1
            anchors[slug] = key
        targets[path] = anchors
    for path, text in pages.items():

        def replace(match):
            href = match["target"] or ""
            name, _, fragment = href.partition("#")
            if not fragment:
                return match[0]
            target = posixpath.normpath(posixpath.join(posixpath.dirname(path), name))
            anchors = targets.get(target if name else path)
            if anchors is None:
                return match[0]
            key = anchors[unquote(fragment)]
            address = name + ("#" + key if key else "")
            return f"[{match['label']}]({address or posixpath.basename(path)})"

        lines = text.splitlines()
        for i, line in prose_lines(lines):
            lines[i] = MARKUP.sub(replace, line)
        pages[path] = "\n".join(lines) + "\n"


@dataclass
class Entry:
    path: str
    identity: str
    kind: str
    aliases: list[str] = field(default_factory=list)
    attachments: list[str] = field(default_factory=list)
    abstract: str = ""


class Edition:
    def __init__(self, revision, tree, docs):
        self.revision, self.tree, self.docs = revision, tree, docs
        self.records = {
            p: row
            for p, text in docs.items()
            if p.endswith(".json") and isinstance(row := json.loads(text), dict)
        }
        self.entries: dict[str, Entry] = {}
        self.resources: dict[str, str] = {}
        self.aliases: dict[str, str] = {}
        registry = self.records["skill_library/skill-index.json"]["skills"]
        registered = {
            "skill_library/" + row["path"] + "/SKILL.md": name for name, row in registry.items()
        }
        self.cases = {
            posixpath.join(posixpath.dirname(p), row["content"]): p
            for p, row in self.records.items()
            if row.get("kind") == "case" and "content" in row
        }
        for path in docs:
            dest = self.destination(path)
            if dest is None:
                continue
            identity = dest.removeprefix("pages/").removesuffix(".md").lower()
            entry = Entry(dest, identity, "reference")
            record = self.records.get(path, {})
            if record.get("id"):
                entry.identity, entry.kind = record["id"], "record"
                entry.aliases = ["package:" + entry.identity]
            elif path.startswith("research_profiles/"):
                entry.identity, entry.kind = "model." + PurePosixPath(path).stem, "profile"
            elif path in self.cases:
                entry.identity, entry.kind = self.records[self.cases[path]]["id"], "case"
                entry.aliases = ["checkout:" + entry.identity]
            elif path.endswith("/SKILL.md"):
                entry.identity = registered.get(path, identity.removesuffix("/lesson"))
                entry.kind = "procedure"
                if path in registered:
                    entry.aliases = ["checkout:" + entry.identity]
            elif path.endswith("/README.md"):
                entry.kind = "guide"
            elif "/cases/" in path:
                entry.kind = "case"
            self.entries[path] = entry
        for path in sorted(docs.keys() - self.entries.keys()):
            record = self.records.get(path, {})
            if record.get("index_type") == "packaged-skill":
                source = record["skill_documents"]["original"].removeprefix("data/")
                entry = self.entries[source]
                entry.aliases.extend([record["id"], "package:" + record["id"]])
                entry.abstract = path
                self.aliases[path] = entry.identity
                continue
            owner = self.owner(path)
            self.resources[path] = self.entries[owner].identity
            self.entries[owner].attachments.append(path)

    def destination(self, path: str) -> str | None:
        p = PurePosixPath(path)
        record = self.records.get(path, {})
        if p.parts[0] == "research_profiles":
            return "pages/models/" + p.with_suffix(".md").name
        if p.parts[0] == "skill_library" and p.suffix == ".md":
            if re.search(r"(?:^|[-_])(license|notice)(?:-mit)?\.md$", p.name, re.I):
                return None
            dest = p.relative_to("skill_library")
            if p.name == "SKILL.md":
                dest = dest.with_name("lesson.md")
            if p.name == "README.md":
                dest = dest.with_name("overview.md")
            return "pages/" + ("library/" if len(dest.parts) == 1 else "") + dest.as_posix()
        if p.parts[0] in ("repo_packs", "knowledge_packs"):
            if record.get("index_type") == "packaged-skill" or not (
                record.get("id") or p.name == "README.md"
            ):
                return None
            if p.parts[0] == "repo_packs":
                dest = PurePosixPath("contribution", p.parts[1], *p.parts[3:])
            else:
                dest = p.relative_to("knowledge_packs")
            dest = (
                dest.with_name("overview.md") if p.name == "README.md" else dest.with_suffix(".md")
            )
            return "pages/records/" + dest.as_posix()
        return None

    def owner(self, path: str) -> str:
        companion = str(PurePosixPath(path).with_suffix(".md"))
        if path != companion and companion in self.entries:
            return companion
        for parent in PurePosixPath(path).parents:
            for filename in ("SKILL.md", "README.md"):
                candidate = (parent / filename).as_posix()
                if candidate != path and candidate in self.entries:
                    return candidate
        return "skill_library/README.md"

    @staticmethod
    def local_link(dest: str, target: str) -> str:
        return posixpath.relpath(target, posixpath.dirname("handbook/" + dest))

    def rewrite(self, text: str, source: str, dest: str) -> str:
        def replace(match):
            href = match["target"]
            if not href or re.match(r"[a-z][\w+.-]*:|[/#]", href, re.I):
                return match[0]
            name, sep, fragment = href.partition("#")
            target = posixpath.normpath(posixpath.join(posixpath.dirname(source), unquote(name)))
            repo_path = PurePosixPath(posixpath.normpath(DATA + "/" + target))
            # This retained navigation link predates the package's move into knowledge/.
            if repo_path.as_posix() == "src/docs/daily-learning-prompt.md":
                repo_path = PurePosixPath("docs/daily-learning-prompt.md")
            if target in self.entries:
                target = self.local_link(dest, "handbook/" + self.entries[target].path)
            elif target in self.aliases:
                original = self.records[target]["skill_documents"]["original"].removeprefix("data/")
                target = self.local_link(dest, "handbook/" + self.entries[original].path)
            elif target in self.docs:
                target = self.local_link(dest, target)
            elif any(p.is_relative_to(repo_path) for p in self.tree):
                mode = "blob" if repo_path in self.tree else "tree"
                target = f"{REPOSITORY}/{mode}/{self.revision}/{repo_path}"
            else:
                return f"{match['label']} (`{href}`, unavailable in the source tree)"
            return f"[{match['label']}]({target}{sep}{fragment})"

        lines = text.splitlines()
        for i, line in prose_lines(lines):
            lines[i] = MARKUP.sub(replace, line)
        return "\n".join(lines)

    def record_body(self, record: dict, entry: Entry) -> tuple[str, str]:
        if entry.kind == "profile":
            body = [
                block("Component roles", record["components"]),
                block(
                    "Discovery terms",
                    {
                        k: record[k]
                        for k in (
                            "aliases",
                            "tasks",
                            "modalities",
                            "input_modalities",
                            "output_modalities",
                            "mechanisms",
                        )
                    },
                ),
            ]
            title = record["model"]
        else:
            title = record["title"]
            body = [
                record["summary"],
                " · ".join(
                    f"`{record.get(k, 'contribution')}`"
                    for k in ("tier", "repo", "backend", "scenario")
                ),
            ]
        for key, label in CARD_FIELDS.items():
            if key == "claims" and record.get(key):
                claims = [
                    f"- **{readable(claim['kind'])}.** {claim['description']}"
                    + (f" Reported on {claim['reported_on']}." if claim.get("reported_on") else "")
                    for claim in record[key]
                ]
                body.append(f"## {label}\n\n" + "\n".join(claims))
            elif record.get(key):
                body.append(block(label, record[key]))
        targets = list(record.get("skill_documents", {}).values())
        targets.extend(v for k, v in record.items() if k.endswith("_resource"))
        if targets:
            links = []
            for target in dict.fromkeys(targets):
                source = target.removeprefix("data/")
                if source in self.entries:
                    target = "handbook/" + self.entries[source].path
                else:
                    target = source
                links.append(
                    f"- [{PurePosixPath(source).name}]({self.local_link(entry.path, target)})"
                )
            body.append("## Companion material\n\n" + "\n".join(links))
        return title, "\n\n".join(body)

    def render(self, path: str, entry: Entry) -> str:
        def link(label, target):
            return f"[{label}]({self.local_link(entry.path, target)})"

        owner = self.owner(path)
        scope_file = next(
            (
                str(folder / "metadata.json")
                for folder in PurePosixPath(path).parents
                if str(folder / "metadata.json") in self.records
            ),
            "",
        )
        if path in self.cases:
            scope_file = self.cases[path]
        scope = self.records.get(scope_file, {})
        front = {}
        if path in self.records:
            scope = self.records[path]
            title, body = self.record_body(scope, entry)
        else:
            body = self.docs[path].replace("\r\n", "\n").strip()
            if body.startswith("---\n"):
                front = _frontmatter(io.BytesIO(body.encode()))
                body = body.split("\n---\n", 1)[1].strip()
            heading = re.search(r"^# (.+)$", body, re.M)
            title = heading[1] if heading else PurePosixPath(path).stem.replace("-", " ").title()
            if heading:
                body = (body[: heading.start()] + body[heading.end() :]).strip()
            body = self.rewrite(prepare_prose(body), path, entry.path)
            if front.get("description"):
                body = front["description"].strip() + "\n\n" + body
            if entry.kind == "procedure" and scope_file == str(
                PurePosixPath(path).with_name("metadata.json")
            ):
                for key in ("applicability", "recommendations", "limitations"):
                    if scope.get(key):
                        body += "\n\n" + block(CARD_FIELDS[key], scope[key])
                if scope.get("references"):
                    related = []
                    for relative in scope["references"]:
                        target = posixpath.normpath(
                            posixpath.join(posixpath.dirname(path), relative)
                        )
                        if target in self.entries:
                            other = self.entries[target]
                            related.append("- " + link(other.identity, "handbook/" + other.path))
                        elif target in self.docs:
                            related.append("- " + link(relative, target))
                        else:
                            raise ValueError(
                                f"Missing declared reference in {scope_file}: {relative}"
                            )
                    body += "\n\n## Declared references\n\n" + "\n".join(related)
            if path in self.cases:
                for key in ("applicability", "limitations"):
                    if scope.get(key):
                        body += "\n\n" + block(CARD_FIELDS[key], scope[key])
                for item in scope.get("findings", []):
                    body += "\n\n" + block(
                        item["direction"], {k: v for k, v in item.items() if k != "direction"}
                    )
        about = []
        state = scope.get("state") or scope.get("status")
        if state:
            about.append(f"Recorded state `{state}`")
        validation = scope.get("empirical_validation")
        if validation:
            about.append(f"empirical validation `{validation}`")
        verification = scope.get("verification", {})
        if "locally_verified" in verification:
            about.append("locally verified `" + json.dumps(verification["locally_verified"]) + "`")
            if verification.get("evidence_level"):
                about.append(f"evidence level `{verification['evidence_level']}`")
        license_name = scope.get("license", front.get("license"))
        if license_name:
            about.append(f"license `{license_name}`")
        about.append(link("Source", path))
        if scope_file:
            about.append(link("Scope and provenance", scope_file))
        if entry.abstract:
            about.append(link("Catalog record", entry.abstract))
            about.append(link("Catalog revision", "repo_packs/inferrsi/knowledge/_provenance.json"))
        if owner != path and path.startswith("skill_library/") and owner in self.entries:
            about.append(link("Parent reading", "handbook/" + self.entries[owner].path))
        if entry.attachments:
            links = [
                link(posixpath.relpath(p, posixpath.dirname(path)), p) for p in entry.attachments
            ]
            body += "\n\n## Source files\n\n" + "\n".join("- " + item for item in links)
        meta = {"id": entry.identity, "kind": entry.kind}
        if entry.aliases:
            meta["aliases"] = entry.aliases
        if tags := scope.get("tags"):
            meta["tags"] = tags
        if path in self.cases or entry.kind in ("record", "profile"):
            meta["carry"] = [
                anchor
                for field, anchor in [
                    ("applicability", "unit-when-this-applies"),
                    ("limitations", "unit-limits-of-this-evidence"),
                ]
                if scope.get(field)
            ]
        header = json.dumps(meta, indent=2, ensure_ascii=False)
        return (
            f"<!-- handbook\n{header}\n-->\n\n# {title}\n\n> "
            + " · ".join(about)
            + ("\n\n" + sections(body).rstrip() + "\n")
        )

    def write(self, target: Path):
        if target.exists():
            raise FileExistsError(f"Choose a new directory for the handbook: {target}")
        pages = {entry.path: self.render(path, entry) for path, entry in self.entries.items()}
        if len(pages) != len(self.entries):
            raise ValueError("Handbook destinations collide")
        stable_links(pages)
        receipt = {
            "schema": 1,
            "repository": REPOSITORY,
            "revision": self.revision,
            "converted": {p: e.identity for p, e in self.entries.items()},
            "catalog_aliases": self.aliases,
            "resources": self.resources,
        }
        pages["migration.json"] = json.dumps(receipt, indent=2, sort_keys=True) + "\n"
        target.parent.mkdir(parents=True, exist_ok=True)
        with tempfile.TemporaryDirectory(dir=target.parent, prefix=".handbook-") as tmp:
            stage = Path(tmp) / "edition"
            for name, value in pages.items():
                output = stage / name
                output.parent.mkdir(parents=True, exist_ok=True)
                output.write_text(value, encoding="utf-8", newline="\n")
            stage.rename(target)


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--revision", required=True)
    parser.add_argument("--output", type=Path, required=True, help="New directory for this import")
    args = parser.parse_args()
    if args.output.exists():
        parser.error("choose a new output directory to preserve existing edits")
    Edition(*snapshot(args.revision)).write(args.output)


if __name__ == "__main__":
    main()
