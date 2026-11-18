<!-- handbook
{
  "id": "competitor-scan",
  "kind": "procedure",
  "aliases": [
    "checkout:competitor-scan",
    "inferrsi.common.skills.competitor_scan",
    "package:inferrsi.common.skills.competitor_scan"
  ],
  "tags": [
    "competitive-analysis",
    "positioning",
    "claim",
    "unverified"
  ]
}
-->

# Competitor scan (generic)

> Recorded state `candidate` · empirical validation `not_run` · [Source](../../../../skill_library/workflows/competitor-scan/SKILL.md) · [Scope and provenance](../../../../skill_library/workflows/competitor-scan/metadata.json) · [Catalog record](../../../../repo_packs/inferrsi/knowledge/common/skills/competitor-scan.json) · [Catalog revision](../../../../repo_packs/inferrsi/knowledge/_provenance.json) · [Parent reading](../../library/overview.md)

Structure a lightweight competitive scan without inventing benchmark numbers or campaign verdicts.

Use when positioning a new RSI repo—not to replace acceptance evidence.

<a id="unit-frame"></a>
## Frame

| Question | Answer (qualitative) |
| --- | --- |
| What do others optimize? | _throughput, latency, cost, quality, …_ |
| How do they publish proof? | _blogs, papers, dashboards, none_ |
| Claim contract? | _pinned revisions + reproducible artifacts? often missing_ |
| Our wedge | _smallest proof that unlocks the next bet_ |

<a id="unit-rules"></a>
## Rules

- No numeric comparisons unless sourced from **our** `evidence/.../results/` with `PASS`.
- Label third-party numbers **unverified** if not reproduced under our RunSpec.
- Use the [evidence and claim rules](https://github.com/InferMatrixLab/InferRSI/blob/b2f60f913a949f9073686a23476f752e11d709a4/docs/contributing.md#evidence-and-claims) when writing a comparison.

<a id="unit-deliverable"></a>
## Deliverable

Short markdown: problem, alternatives, differentiation (claim contract + SIAS), limits, open questions.

<a id="unit-when-this-applies"></a>
## When this applies

- **Scope** — Qualitative positioning of a new RSI repository against other projects before acceptance evidence exists
- **Prerequisites** — A selected repository and readable public material from the alternatives; no benchmark run is required
- **Input contract** — A target repository plus whatever the alternatives publish about what they optimize and how they prove it
- **Produced artifact** — A short Markdown note covering problem, alternatives, differentiation, limits and open questions
- **Failure modes**
  - Numeric comparison written without a PASS campaign in our own evidence tree
  - Third-party figure repeated as if reproduced under our RunSpec
  - Scan presented as a substitute for acceptance evidence
- **Refusal point** — Refuses any numeric comparison not sourced from our own evidence/<campaign-id>/results/ with a PASS verdict

<a id="unit-putting-the-idea-to-work"></a>
## Putting the idea to work

- Answer the four framing questions qualitatively first; the absence of a published claim contract is itself a finding.
- Label every third-party number unverified unless it was reproduced under our RunSpec.
- Close the note with open questions rather than a conclusion the evidence cannot support.

<a id="unit-limits-of-this-evidence"></a>
## Limits of this evidence

- Produces positioning material only; it establishes no performance or quality result.
- Third-party claim contracts are read from public material and may be incomplete.

<a id="unit-source-files"></a>
## Source files

- [metadata.json](../../../../skill_library/workflows/competitor-scan/metadata.json)
