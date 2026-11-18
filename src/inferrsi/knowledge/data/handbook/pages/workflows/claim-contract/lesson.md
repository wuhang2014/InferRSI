<!-- handbook
{
  "id": "claim-contract",
  "kind": "procedure",
  "aliases": [
    "checkout:claim-contract",
    "inferrsi.common.skills.claim_contract",
    "package:inferrsi.common.skills.claim_contract"
  ],
  "tags": [
    "claim",
    "wording",
    "verdict",
    "evidence",
    "portable"
  ]
}
-->

# Claim contract (portable)

> Recorded state `candidate` · empirical validation `not_run` · [Source](../../../../skill_library/workflows/claim-contract/SKILL.md) · [Scope and provenance](../../../../skill_library/workflows/claim-contract/metadata.json) · [Catalog record](../../../../repo_packs/inferrsi/knowledge/common/skills/claim-contract.json) · [Catalog revision](../../../../repo_packs/inferrsi/knowledge/_provenance.json) · [Parent reading](../../library/overview.md)

Enforce ThinkFlowLab claim contract wording and verdict rules without embedding campaign-specific revision pins.

<a id="unit-public-claim-wording"></a>
## Public claim wording

Use: “on {repo}@{candidate} vs baseline@{baseline}, under {RunSpec}, we observed …”

Only after acceptance **`PASS`** with artifacts under `evidence/`.

<a id="unit-rules-not-numbers"></a>
## Rules (not numbers)

| Verdict | When |
| --- | --- |
| PASS | Pinned SHAs, artifact tree on candidate tip, gates satisfied |
| FAIL | Gates failed with complete evidence |
| INCONCLUSIVE | Cannot defend comparison (env, partial run, missing validator freeze) |

<a id="unit-what-not-to-do"></a>
## What not to do

- Do not bake baseline/candidate SHAs into shared repo templates, skills, or default CI env.
- Do not treat microbench alone as e2e campaign completion.
- Do not auto-transfer lessons across unverified repo × revision × backend × device × model × scenario tuples.

<a id="unit-sias"></a>
## SIAS

Respect plane boundaries: `harness/` orchestrates, `model/` defines quality, `infra/` supplies execution. Cross-plane deps belong in RunSpec.

<a id="unit-when-this-applies"></a>
## When this applies

- **Scope** — Wording and verdict rules for any public performance or quality claim produced from an RSI campaign
- **Prerequisites** — A completed campaign with pinned baseline and candidate SHAs and an evidence tree; the rules themselves carry no numeric threshold
- **Input contract** — A claim draft, the campaign RunSpec and its evidence tree under evidence/<campaign-id>/
- **Produced artifact** — A claim sentence in the pinned form, or a refusal when the campaign verdict is not PASS
- **Failure modes**
  - Claim asserted before the campaign reaches PASS with artifacts
  - Baseline or candidate SHA written into a shared template, skill or default CI environment
  - Microbenchmark result presented as end-to-end completion
  - A lesson transferred across an unverified repo x revision x backend x device x model x scenario tuple
- **Refusal point** — Refuses any public claim lacking a PASS verdict and artifacts under evidence/, and refuses numeric thresholds because thresholds belong to the campaign

<a id="unit-putting-the-idea-to-work"></a>
## Putting the idea to work

- Keep campaign SHAs in the acceptance issue; a shared template that carries them will be wrong for the next campaign.
- Write the verdict from the evidence tree before writing the claim sentence.
- Treat each repo x revision x backend x device x model x scenario tuple as an independent claim.

<a id="unit-limits-of-this-evidence"></a>
## Limits of this evidence

- States wording and verdict rules only; it selects no numeric gate and validates no measurement.
- SIAS plane boundaries constrain where a change belongs, not whether it is correct.

<a id="unit-source-files"></a>
## Source files

- [metadata.json](../../../../skill_library/workflows/claim-contract/metadata.json)
