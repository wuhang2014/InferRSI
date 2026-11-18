"""CLI for the side-by-side teaching edition of the knowledge corpus."""

import json
import re
import sys

from ...knowledge.handbook import BOOK, KINDS, Handbook, markdown


def _emit(text: str) -> None:
    """Keep scientific symbols intact when stdout is a Windows pipe or file."""
    if not sys.stdout.isatty() and hasattr(sys.stdout, "buffer"):
        sys.stdout.flush()
        sys.stdout.buffer.write((text + "\n").encode("utf-8"))
    else:
        print(text)


def add_commands(knowledge_actions):
    parser = knowledge_actions.add_parser("handbook", help="Browse and compose teaching material")
    actions = parser.add_subparsers(dest="handbook_action", required=True)
    contents = actions.add_parser("contents", help="Browse chapters or one chapter's sections")
    contents.add_argument("chapter", nargs="?", default="")
    search = actions.add_parser("search", help="Find a page or an individual section")
    search.add_argument("query")
    search.add_argument("--kind", choices=KINDS)
    search.add_argument("--under", default="", help="Restrict to a chapter, e.g. hardware/ascend")
    search.add_argument("--limit", type=int, default=10)
    read = actions.add_parser("read", help="Read a page or a page#unit reference")
    read.add_argument("ref")
    read.add_argument("--revision", help="Require the specified content digest")
    links = actions.add_parser("links", help="Show typed links and backlinks")
    links.add_argument("ref")
    compose = actions.add_parser("compose", help="Assemble pages, sections or a reading path")
    compose.add_argument("refs", nargs="+")
    for command in (search, read, links, compose):
        command.add_argument("--json", action="store_true")


def run(args) -> int:
    action = args.handbook_action
    if action == "contents":
        if args.chapter and not re.fullmatch("[a-z0-9-]+", args.chapter):
            raise ValueError("Use the chapter name from the table of contents")
        path = BOOK / "contents" / ((args.chapter or "README") + ".md")
        if not path.is_file():
            raise ValueError(f"Unknown handbook chapter: {args.chapter}")
        _emit(path.read_text(encoding="utf-8").rstrip())
        return 0
    book = Handbook()
    if action == "search":
        value = book.search(args.query, kind=args.kind, under=args.under, limit=args.limit)
    elif action == "links":
        value = book.links(args.ref)
    elif action == "compose":
        value = book.compose(args.refs)
    else:
        value = book.read(args.ref, args.revision)
    if args.json:
        _emit(json.dumps(value, indent=2))
    elif action == "search":
        for item in value:
            title = item["title"]
            if item["page"] != title:
                title = f"{item['page']} · {title}"
            _emit(f"{item['ref']}\t{title}")
    elif action == "links":
        for direction in ("outgoing", "incoming"):
            for edge in value[direction]:
                _emit(f"{direction}\t{edge['relation']}\t{edge['ref']}")
    else:
        _emit(markdown(value if action == "compose" else [value]))
    return 0
