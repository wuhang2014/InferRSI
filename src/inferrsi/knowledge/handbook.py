"""Read, search and compose the editable Markdown handbook. All reads are offline."""

from __future__ import annotations

import hashlib
import json
import posixpath
import re
from dataclasses import dataclass
from pathlib import Path
from urllib.parse import unquote

BOOK = Path(__file__).with_name("data") / "handbook"
_HEADER = re.compile(r"\A<!-- handbook\n(.+?)\n-->\n\n# ([^\n]+)\n", re.DOTALL)
_ANCHOR = re.compile(r'<a id="(unit-[\w-]+)"></a>')
_ID = re.compile(r"[\w][\w./:-]*")
_FENCE = re.compile(r"^ {0,3}(`{3,}|~{3,})(.*)$")
# The handbook uses inline Markdown links for relations. Skip inline code examples.
MARKUP = re.compile(
    r"(?P<code>(?P<tick>`+).*?(?P=tick))|\[(?P<label>[^\]\n]*)\]"
    r"\((?P<target>[^\s()]+)\)"
)
KINDS = ("path", "concept", "procedure", "case", "record", "reference", "guide", "profile")


def prose_lines(lines):
    """Yield (index, line) outside fenced code, including longer outer fences."""
    fence = ""
    for index, line in enumerate(lines):
        match = _FENCE.match(line)
        if fence:
            if match and match[1].startswith(fence) and not match[2].strip():
                fence = ""
        elif match:
            fence = match[1]
        else:
            yield index, line


@dataclass(frozen=True)
class Section:
    key: str
    title: str
    level: int
    start: int
    end: int


@dataclass
class Page:
    path: str
    id: str
    title: str
    kind: str
    aliases: list[str]
    tags: list[str]
    context: str
    text: str
    lines: list[str]
    sections: dict[str, Section]
    carry: list[str]

    @classmethod
    def parse(cls, path: str, text: str) -> Page:
        match = _HEADER.match(text)
        if not match:
            raise ValueError(f"Missing handbook header or title in {path}")
        meta = json.loads(match[1])
        if not isinstance(meta, dict) or meta.get("kind") not in KINDS:
            raise ValueError(f"Invalid handbook kind in {path}")
        identity = meta.get("id")
        aliases, tags = meta.get("aliases", []), meta.get("tags", [])
        for values in (aliases, tags):
            if not isinstance(values, list) or any(not isinstance(v, str) or not v for v in values):
                raise ValueError(f"Expected a list of strings in {path}")
        if any(not isinstance(v, str) or not _ID.fullmatch(v) for v in [identity, *aliases]):
            raise ValueError(f"Invalid handbook ID in {path}")
        lines = text[match.end() :].splitlines()
        context = next((line for line in lines if line.strip()), "")
        if not context.startswith("> "):
            context = ""
        starts = []
        seen = set()
        for i, line in prose_lines(lines):
            anchor = _ANCHOR.fullmatch(line)
            if anchor:
                heading = (
                    re.fullmatch(r"(#{2,6}) (.+)", lines[i + 1]) if i + 1 < len(lines) else None
                )
                if not heading or anchor[1] in seen:
                    raise ValueError(f"Duplicate or misplaced anchor {anchor[1]} in {path}")
                seen.add(anchor[1])
                starts.append((i, anchor[1], len(heading[1]), heading[2]))
        sections = {}
        for pos, (i, key, level, title) in enumerate(starts):
            end = next((j for j, _, depth, _ in starts[pos + 1 :] if depth <= level), len(lines))
            sections[key] = Section(key, title, level, i, end)
        carry = meta.get("carry", [])
        if not isinstance(carry, list) or any(
            not isinstance(k, str) or k not in sections for k in carry
        ):
            raise ValueError(f"Unknown context section in {path}")
        return cls(
            path,
            identity,
            match[2],
            meta["kind"],
            aliases,
            tags,
            context,
            text,
            lines,
            sections,
            carry,
        )

    def section_text(self, key: str) -> str:
        section = self.sections[key]
        return "\n".join(self.lines[section.start + 2 : section.end]).strip()

    def view(self, key: str) -> dict:
        title = self.sections[key].title if key else self.title
        body = self.section_text(key) if key else "\n".join(self.lines).strip()
        ref = self.id + ("#" + key if key else "")
        if key:
            selected = self.sections[key]
            bounds = []
            for context_key in self.carry:
                section = self.sections[context_key]
                if not selected.start <= section.start < selected.end:
                    bounds.append(
                        f"### {section.title} (whole page)\n\n" + self.section_text(context_key)
                    )
            body = "\n\n".join(filter(None, (self.context, body, *bounds)))
            material = f"{ref}\n{self.kind}\n{self.title}\n{title}\n{body}"
        else:
            material = self.text
        return {
            "ref": ref,
            "path": self.path,
            "kind": self.kind,
            "page": self.title,
            "title": title,
            "revision": "sha256:" + hashlib.sha256(material.encode()).hexdigest(),
            "body": body,
        }


class Handbook:
    def __init__(self, root: Path = BOOK):
        self.pages: dict[str, Page] = {}
        self.by_path: dict[str, Page] = {}
        for path in sorted((root / "pages").rglob("*.md")):
            page = Page.parse(path.relative_to(root).as_posix(), path.read_text(encoding="utf-8"))
            self.by_path[page.path] = page
            for name in [page.id, *page.aliases]:
                if name in self.pages:
                    raise ValueError(f"Duplicate handbook ID: {name}")
                self.pages[name] = page
        if not self.by_path:
            raise ValueError("Handbook has no pages")

    def resolve(self, ref: str) -> tuple[Page, str]:
        name, sep, key = ref.partition("#")
        # The Markdown contents link from contents/ into ../pages/. Resolve those
        # printed links through the same index as IDs, without opening arbitrary paths.
        page = self.pages.get(name) or self.by_path.get(name.removeprefix("../"))
        if page is None or (sep and key not in page.sections):
            raise ValueError(f"Unknown handbook reference: {ref}")
        return page, key

    def read(self, ref: str, revision: str | None = None) -> dict:
        page, key = self.resolve(ref)
        item = page.view(key)
        if revision is not None and item["revision"] != revision:
            raise ValueError(f"Revision mismatch for {ref}: current {item['revision']}")
        return item

    def _target(self, page: Page, href: str) -> str | None:
        path, _, anchor = unquote(href).partition("#")
        if re.match(r"[a-z][\w+.-]*:|/", path, re.I):
            return None
        target = posixpath.normpath(posixpath.join(posixpath.dirname(page.path), path))
        other = self.by_path.get(target) if path else page
        if other is None:
            if target.startswith("pages/") and path.endswith(".md"):
                raise ValueError(f"Broken handbook link in {page.path}: {href}")
            return None
        if anchor:
            if anchor not in other.sections:
                raise ValueError(f"Missing section in link from {page.path}: {href}")
            return f"{other.id}#{anchor}"
        return other.id

    def edges(self, page: Page):
        """Materialize relations from the same links a person follows in Markdown."""
        key = ""
        anchors = {s.start: s.key for s in page.sections.values()}
        for i, line in prose_lines(page.lines):
            if i in anchors:
                key = anchors[i]
                continue
            links = [m for m in MARKUP.finditer(line) if m["target"]]
            step = page.kind == "path" and key == "unit-readings" and re.match(r"^\d+\. ", line)
            if step and len(links) != 1:
                raise ValueError(f"Expected one handbook link per reading step in {page.path}")
            for match in links:
                target = self._target(page, match["target"])
                if step and not target:
                    raise ValueError(f"Reading step outside the handbook in {page.path}")
                if not target:
                    continue
                if step:
                    relation = "includes"
                elif key == "unit-prerequisites":
                    relation = "prerequisite"
                elif match["label"] == "Parent reading":
                    relation = "part-of"
                elif self.pages[target.partition("#")[0]].kind == "case":
                    relation = "example"
                else:
                    relation = "see-also"
                yield key, relation, target

    def links(self, ref: str) -> dict:
        page, key = self.resolve(ref)
        identity = page.id + ("#" + key if key else "")
        visible = set()
        context_targets = {
            self._target(page, match["target"])
            for match in MARKUP.finditer(page.context)
            if match["target"]
        }
        if key:
            ranges = [page.sections[k] for k in (key, *page.carry)]
            visible.update(
                s.key
                for s in page.sections.values()
                if any(r.start <= s.start < r.end for r in ranges)
            )
        outgoing, incoming = {}, {}
        for source in self.by_path.values():
            for section, relation, target in self.edges(source):
                if source is page and (
                    not key or section in visible or (not section and target in context_targets)
                ):
                    outgoing[relation, target] = None
                if target == identity or (not key and target.partition("#")[0] == identity):
                    incoming[relation, source.id + ("#" + section if section else "")] = None
        return {
            "ref": identity,
            "outgoing": [{"relation": r, "ref": t} for r, t in outgoing],
            "incoming": [{"relation": r, "ref": t} for r, t in incoming],
        }

    def compose(self, refs: list[str]) -> list[dict]:
        """Expand reading paths in order. Include each canonical reference once."""
        result = {}

        def visit(ref: str, active: tuple[str, ...]):
            page, key = self.resolve(ref)
            if key or page.kind != "path":
                item = page.view(key)
                result.setdefault(item["ref"], item)
                return
            if page.id in active:
                raise ValueError("Reading path cycle: " + " -> ".join((*active, page.id)))
            parts = [target for _, kind, target in self.edges(page) if kind == "includes"]
            if not parts:
                raise ValueError(f"Empty reading path: {page.id}")
            for target in parts:
                visit(target, (*active, page.id))

        for ref in refs:
            visit(ref, ())
        return list(result.values())

    def search(
        self, query: str, *, kind: str | None = None, under: str = "", limit: int = 10
    ) -> list[dict]:
        from .knowledge_find import Corpus, Document, expand

        if limit < 1:
            raise ValueError("limit must be positive")
        prefix = "pages/" + (under.strip("/") + "/" if under.strip("/") else "")
        if query.partition("#")[0] in self.pages:
            page, key = self.resolve(query)
            if (kind and page.kind != kind) or not page.path.startswith(prefix):
                return []
            return [self._hit(page, key)]
        terms, _ = expand(query)
        if not terms:
            return []
        entries, documents = [], []
        for page in self.by_path.values():
            if (kind and kind != page.kind) or not page.path.startswith(prefix):
                continue
            # Index each paragraph once. Reading a parent section also includes its children.
            boundaries = [("", -1)] + [(s.key, s.start) for s in page.sections.values()]
            for pos, (key, start) in enumerate(boundaries):
                end = boundaries[pos + 1][1] if pos + 1 < len(boundaries) else len(page.lines)
                first = start + 2 if key else 0
                body = "\n".join(line for line in page.lines[first:end] if line != page.context)
                # Search what a reader sees. Repeated paths in link destinations otherwise
                # cause attachment inventories to outrank observations on the same subject.
                body = MARKUP.sub(lambda m: m["label"] if m["target"] else m[0], body)
                title = page.sections[key].title if key else page.title
                fields = {"title": title, "body": body}
                if not key:
                    fields["tags"] = " ".join([page.id, *page.aliases, *page.tags])
                entries.append((page, key))
                documents.append(Document(page.id, page.kind, "", page.path, title, "", fields))
        corpus = Corpus(documents)
        ranked = []
        for i, (page, key) in enumerate(entries):
            score, _ = corpus.score(i, terms)
            if score > 0:
                ranked.append((-score, page.id, key))
        return [self._hit(self.pages[identity], key) for _, identity, key in sorted(ranked)[:limit]]

    @staticmethod
    def _hit(page: Page, key: str) -> dict:
        return {k: v for k, v in page.view(key).items() if k != "body"}


def markdown(items: list[dict]) -> str:
    """Render excerpts together. All relative links use the handbook root as their base."""
    result = []
    for item in items:
        path = item["path"]
        key = item["ref"].partition("#")[2]
        address = path + ("#" + key if key else "")
        lines = item["body"].splitlines()

        def rebase(match):
            href = match["target"]
            if not href or re.match(r"[a-z][\w+.-]*:|/", href, re.I):
                return match[0]
            name, marker, fragment = href.partition("#")
            target = posixpath.normpath(posixpath.join(posixpath.dirname(path), name))
            return f"[{match['label']}]({target if name else path}{marker}{fragment})"

        for i, line in prose_lines(lines):
            lines[i] = "" if _ANCHOR.fullmatch(line) else MARKUP.sub(rebase, line)
        result.append(
            f"# {item['title']}\n\n[{item['ref']}]({address}) · `{item['revision']}`"
            + "\n\n"
            + "\n".join(lines)
        )
    return "\n\n---\n\n".join(result)
