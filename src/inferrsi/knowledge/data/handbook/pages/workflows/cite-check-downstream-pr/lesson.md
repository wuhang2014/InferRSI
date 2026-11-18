<!-- handbook
{
  "id": "cite-check-downstream-pr",
  "kind": "procedure",
  "aliases": [
    "checkout:cite-check-downstream-pr",
    "inferrsi.common.skills.cite_check_downstream_pr",
    "package:inferrsi.common.skills.cite_check_downstream_pr"
  ],
  "tags": [
    "review",
    "downstream",
    "citation",
    "evidence",
    "verdict"
  ]
}
-->

# Cite-check a downstream PR

> Recorded state `candidate` · empirical validation `not_run` · [Source](../../../../skill_library/workflows/cite-check-downstream-pr/SKILL.md) · [Scope and provenance](../../../../skill_library/workflows/cite-check-downstream-pr/metadata.json) · [Catalog record](../../../../repo_packs/inferrsi/knowledge/common/skills/cite-check-downstream-pr.json) · [Catalog revision](../../../../repo_packs/inferrsi/knowledge/_provenance.json) · [Parent reading](../../library/overview.md)

Review a downstream PR description for correct acceptance issue links, SHA pins, and artifact citations.

Use when reviewing external PRs that claim performance or quality improvements tied to RSI acceptance work.

<a id="unit-checklist"></a>
## Checklist

- [ ] Links an acceptance issue URL (not only a chat thread)
- [ ] States **baseline SHA** and **candidate SHA** matching that issue
- [ ] Points to `evidence/<campaign-id>/results/` (or equivalent published mirror)
- [ ] Does **not** invent new thresholds or restate bars differently
- [ ] Marks summaries **unverified** if artifacts are missing, stale, or off-SHA
- [ ] Uses verdict vocabulary only: `PASS` / `FAIL` / `INCONCLUSIVE`

<a id="unit-red-flags"></a>
## Red flags

- “X% faster” without artifact path
- Branch names instead of full SHAs
- Microbench-only support for e2e latency claims

<a id="unit-reference"></a>
## Reference

[docs/contributing.md#evidence-and-claims](https://github.com/InferMatrixLab/InferRSI/blob/b2f60f913a949f9073686a23476f752e11d709a4/docs/contributing.md#evidence-and-claims)

<a id="unit-when-this-applies"></a>
## When this applies

- **Scope** — Review of a downstream PR description that cites RSI acceptance work for a performance or quality improvement
- **Prerequisites** — The PR description, the acceptance issue it cites, and the evidence paths it names; reviewing is read-only and needs no local run
- **Input contract** — One PR description plus the cited acceptance issue and its evidence tree; the reviewer reads claims and citations, not the candidate code
- **Produced artifact** — A per-checklist review result that either accepts the citation or marks the summary unverified, using only PASS/FAIL/INCONCLUSIVE vocabulary
- **Failure modes**
  - No acceptance issue URL, only a chat thread
  - Branch names instead of full baseline and candidate SHAs
  - Microbenchmark evidence offered for an end-to-end latency claim
  - A threshold restated or invented relative to the acceptance issue
  - Evidence path absent, stale or on a different SHA than the cited candidate
- **Refusal point** — Refuses to restate a performance or quality claim whose artifacts are missing, stale or off-SHA; reports the summary as unverified instead

<a id="unit-putting-the-idea-to-work"></a>
## Putting the idea to work

- Read the cited acceptance issue before the PR description so an invented threshold is visible immediately.
- Resolve every listed evidence path and compare its SHA with the candidate SHA the PR names.
- Report an unverifiable claim as unverified rather than repeating its number.

<a id="unit-limits-of-this-evidence"></a>
## Limits of this evidence

- Checklist-only procedure; it validates citation discipline, not the measurement behind an artifact.
- A passing review does not establish that the campaign evidence itself is correct.

<a id="unit-source-files"></a>
## Source files

- [metadata.json](../../../../skill_library/workflows/cite-check-downstream-pr/metadata.json)
