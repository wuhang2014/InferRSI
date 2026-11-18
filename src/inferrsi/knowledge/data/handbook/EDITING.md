# Editing and citing the handbook

## Change one teaching unit

Open the Markdown page under `pages/`. Change the explanation, example or
evidence limit in place. Search reads these files directly. Keep the page
ID and the section's `unit-…` anchor when changing a title. This keeps saved
citations, reading paths and incoming links usable. If you move a page, keep
its ID and update the relative Markdown links that point to the old location.

Place a new page in its subject directory. The first comment holds a JSON
object. Give the page an ID and a kind, then write its title and lesson.
The rendered page starts at the title. Here is a complete small example.

```markdown
<!-- handbook
{"id": "reading-a-timer", "kind": "concept", "tags": ["timing"]}
-->

# Reading a timer

<a id="unit-endpoint"></a>
## Which event stops the clock?

A client can time the return from submission or wait for the completed output.
Record which event ended the interval before comparing two readings.
```

Kinds are `concept`, `procedure`, `case`, `record`, `reference`, `guide`,
`profile` and `path`. Optional `aliases` give existing IDs an unambiguous
destination. An optional opening blockquote carries the source and evidence
state into every excerpt. The optional `carry` array holds section keys on
this page whose contents travel with an excerpt. Use it for the applicability
and limits of a bounded observation. Edit that context once at its owner.

Each explicit anchor immediately precedes a level 2–6 heading. A parent section
includes its nested headings through the next heading at its own or a higher
level with an explicit anchor. Text inside fenced code stays literal. Paths and
other pages can link directly to `filename.md#unit-endpoint`.

## Assemble a reading path

Create a page of kind `path`. Under the stable anchor `unit-readings`, put one
relative Markdown link on each numbered step. Point to a page, a section or
another path. A `unit-prerequisites` section links readers to assumed knowledge.
The reader follows the numbered steps in order and includes each selected
reference once. Prerequisites and explanatory links remain available through
`links`. See a complete editable example. [Measure a request](pages/paths/measure-a-request.md)

```bash
inferrsi knowledge handbook compose "conditional-bounds#unit-floor" "measurement-boundaries#unit-completion"
inferrsi knowledge handbook search "buffer lifetime" --under frameworks --limit 5
inferrsi knowledge handbook contents hardware
```

Each CLI result with `--json` includes structured data. A read or composed
unit carries its `ref`, page-relative body, handbook-relative `path`, and
`revision`. The text renderer rebases links against the handbook directory so
you can save a composed reading alongside the handbook README. You can pass
a page link printed by `contents` directly to `read`, including its section anchor.

## Cite and recover a revision

Record the handbook Git commit, the `ref` and the `revision` returned by
`read --json`. A page revision hashes its UTF-8 text with LF line endings.
A section revision hashes its identity, kind, page and section titles, and
the excerpt including its inherited context. Editing a different section
preserves the digest if the excerpt and its context stay the same.

```bash
inferrsi knowledge handbook read "measurement-boundaries#unit-completion" --json
inferrsi knowledge handbook read "measurement-boundaries#unit-completion" --revision <sha256-revision>
git log --follow -- src/inferrsi/knowledge/data/handbook/pages/foundations/measurement-boundaries.md
git show <handbook-commit>:src/inferrsi/knowledge/data/handbook/pages/foundations/measurement-boundaries.md
```

A mismatched digest reports the current revision. To resolve an old excerpt
with its contemporary links and resources, run the reader in a checkout or
installation of the recorded commit. Research pins, licenses, case outcomes
and verification states in the material describe the cited sources. The
handbook's own Git history records editorial changes.

## Update navigation or compare against a source edition

From a development installation, refresh the table of contents after a title
change, addition or move. Run the check alone to verify the committed contents,
local links, reading paths, aliases and coverage of the frozen import.

```bash
python tools/check_handbook.py --write-contents
python tools/check_handbook.py
```

The handbook is edited independently after import. Existing InferRSI runtime
records continue to use their established contribution workflow. To compare a
later version of those records, seed a fresh directory, review the diff and
bring the desired edits into their teaching units. The importer reads committed
blobs at the supplied revision. It requires the development or skills extra.

```bash
python tools/port_handbook.py --revision <source-commit> --output build/handbook-comparison
```

The migration receipt records which original paths became pages, which catalog
records became aliases, and where each supporting file is linked. Keep the
historical receipt with the edition it describes. Raw evidence, exact resource
bytes and third-party notices retain their original locations and revisions.
