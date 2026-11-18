<!-- handbook
{
  "id": "draft-acceptance-issue",
  "kind": "procedure",
  "aliases": [
    "checkout:draft-acceptance-issue",
    "inferrsi.common.skills.draft_acceptance_issue",
    "package:inferrsi.common.skills.draft_acceptance_issue"
  ],
  "tags": [
    "acceptance",
    "issue",
    "runspec",
    "template",
    "campaign"
  ]
}
-->

# Draft acceptance issue

> Recorded state `candidate` · empirical validation `not_run` · [Source](../../../../skill_library/workflows/draft-acceptance-issue/SKILL.md) · [Scope and provenance](../../../../skill_library/workflows/draft-acceptance-issue/metadata.json) · [Catalog record](../../../../repo_packs/inferrsi/knowledge/common/skills/draft-acceptance-issue.json) · [Catalog revision](../../../../repo_packs/inferrsi/knowledge/_provenance.json) · [Parent reading](../../library/overview.md)

Draft a campaign acceptance issue with checklist, RunSpec, evidence paths, and placeholders for baseline/candidate SHAs.

Use when starting a new campaign in a ThinkFlowLab RSI-style repo.

<a id="unit-steps"></a>
## Steps

1. Pick `campaign_id` (naming: `{model-or-scenario} / {device}×{count}`).
2. Copy `evidence/_template/` → `evidence/<campaign_id>/` (empty tree with README stubs).
3. Open issue using `.github/ISSUE_TEMPLATE/campaign-acceptance.yml` or [docs/contributing.md#acceptance-checklist](https://github.com/InferMatrixLab/InferRSI/blob/b2f60f913a949f9073686a23476f752e11d709a4/docs/contributing.md#acceptance-checklist).
4. Fill **pinned baseline SHA** and **pinned candidate SHA** in the issue—use placeholders `<baseline-sha>` / `<candidate-sha>` until known.
5. Resolve criteria using the [acceptance-criteria procedure](../../methods/performance-ceiling-analysis/references/acceptance-criteria.md):
   use user-supplied criteria; otherwise use `performance-ceiling-analysis` to
   formulate targets. Preserve partial requirements, label derived fields and
   retain unresolved evidence gaps. List supported gates and their provenance in
   `plan/` before candidate search.
6. Set initial verdict `INCONCLUSIVE`.

<a id="unit-do-not"></a>
## Do not

- Commit campaign SHAs into `recipes/`, `benchmarks/`, skills, or workflow defaults.
- Claim `PASS` without `validator/` freeze and `results/` rationale.

<a id="unit-output"></a>
## Output

Issue body sections: campaign id, SHAs, RunSpec, criteria source and derivation (including evidence gaps and freeze authority), gates, evidence paths, verdict, downstream citation blurb.

<a id="unit-when-this-applies"></a>
## When this applies

- **Scope** — Opening a new acceptance campaign in an RSI-style repository, before any baseline or candidate run
- **Prerequisites** — A chosen campaign subject and an empty evidence/<campaign-id>/ tree copied from evidence/_template/; SHAs may still be placeholders
- **Input contract** — A campaign id of the form {model-or-scenario}/{device}x{count}, any user-supplied criteria or accepted plan, and available workload/baseline/calibration evidence for deriving missing targets
- **Produced artifact** — An acceptance issue body with campaign id, pinned baseline and candidate SHAs, RunSpec, criteria source and derivation including gaps and freeze authority, gates, evidence paths, initial verdict and a downstream citation blurb
- **Failure modes**
  - Gates written after the search loop has already run
  - Campaign SHAs committed into recipes/, benchmarks/, skills or workflow defaults
  - PASS claimed without a validator/ freeze and a results/ rationale
- **Refusal point** — Refuses to state a verdict other than INCONCLUSIVE while the validator freeze or results rationale is absent

<a id="unit-putting-the-idea-to-work"></a>
## Putting the idea to work

- Use user-supplied criteria; when absent, follow the performance-ceiling-analysis acceptance procedure to formulate targets, preserving partial requirements and identifying derived fields and evidence gaps.
- Write the gates in plan/ before any search loop; a gate chosen afterwards cannot reject the candidate honestly.
- Use the <baseline-sha> and <candidate-sha> placeholders until the campaign fixes them, and keep the real values in the issue.
- Set the initial verdict to INCONCLUSIVE so the absence of evidence is recorded rather than assumed away.

<a id="unit-limits-of-this-evidence"></a>
## Limits of this evidence

- Drafts an issue only; it freezes no gate and runs no measurement.
- The placeholder SHA convention depends on the campaign owner filling them in later.

<a id="unit-source-files"></a>
## Source files

- [metadata.json](../../../../skill_library/workflows/draft-acceptance-issue/metadata.json)
