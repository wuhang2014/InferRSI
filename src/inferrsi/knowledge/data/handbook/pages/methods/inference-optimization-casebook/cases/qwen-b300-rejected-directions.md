<!-- handbook
{
  "id": "case.qwen-b300-rejected-directions",
  "kind": "case",
  "aliases": [
    "checkout:case.qwen-b300-rejected-directions"
  ],
  "tags": [
    "negative-evidence",
    "quality-rejection",
    "no-demonstrated-gain",
    "confounded-run",
    "RoPE",
    "CUDA-Graph"
  ],
  "carry": [
    "unit-when-this-applies",
    "unit-limits-of-this-evidence"
  ]
}
-->

# Qwen B300: rejected directions to check before retrying

> Recorded state `historical_observation` · [Source](../../../../../skill_library/methods/inference-optimization-casebook/cases/qwen-b300-rejected-directions.md) · [Scope and provenance](../../../../../skill_library/methods/inference-optimization-casebook/cases/qwen-b300-rejected-directions.json) · [Parent reading](../lesson.md)

Scope: Qwen-Image-2.1-Turbo, four B300, BF16, native eight-step image generation.
The [pinned ledger](https://github.com/InferMatrixLab/InferRSI/blob/d51c941dc57807c1e16ea698cd9291f414110c45/docs/qwen-image-2.1-turbo-b300.md#optimization-ledger)
and [acceptance issue #3](https://github.com/InferMatrixLab/InferRSI/issues/3)
own the observations. The final campaign PASS belongs to its retained stack,
not these rejected alternatives. No source experiment is rerun here.
Kind, origin, state and source identities belong to the
[typed source and scope record](../../../../../skill_library/methods/inference-optimization-casebook/cases/qwen-b300-rejected-directions.json).

| Direction | Recorded observation and disposition | Suggested revisit condition and first check |
| --- | --- | --- |
| H3: initial Q/K RMSNorm + complex RoPE fusion | Operator tests passed; complete images failed; reverted. This is a quality rejection, not a kernel-speed result. | First match the actual reduction, complex FMA order and BF16 materialization; compare full native images after operator checks. H10/H13 show later, different implementations were retained, so the technique is not permanently excluded. |
| H1: packed Q/K/V 5D exchange | Quality passed but the exploratory trial was discarded. | Changed layouts/topology may justify another trial; measure staging/copies and the complete request against a matched control. Do not infer the cause from the one ledger timing. |
| H6/H7: graph projection/norm/RoPE or post-attention work | Removed for no material E2E gain; H7 records replay/copy costs. | A new capture boundary or buffer lifetime may change the tradeoff; include capture/replay, copies and full request cost. |
| H14/H16: broadcast decode scale/gate or skip empty concatenation | No demonstrated benefit; removed/reverted. | Confirm these operations are on the current critical path before repeating; retain a matched E2E control. |
| H17 and the noisy H13 attempt | Observed host load/concurrent diagnostics invalidate causal attribution. | Repeat on a qualified, uncontended host. Do not classify the numerical timing difference as a confirmed code regression. |
| H18: compiled launch API probe | Host enqueue improved in a diagnostic; no E2E integration was performed. | Treat it as an unintegrated lead; verify actual execution, correctness and complete service overhead before accepting it. |

The last column is a proposed diagnostic procedure, not an observed root cause
or permission to reopen the campaign. A new revision, workload or hardware
requires its own frozen controls and quality gate. Old helper hashes remain
bound to the original source revision.

<a id="unit-when-this-applies"></a>
## When this applies

- Qwen-Image-2.1-Turbo, four B300, BF16, native eight steps
- Only the source ledger's individual trials and controls

<a id="unit-limits-of-this-evidence"></a>
## Limits of this evidence

- The final campaign PASS does not qualify each rejected direction
- Exploratory trial timings are not additive gains or causal comparisons
- No experiment was rerun for this extraction

<a id="unit-require-full-image-parity-for-fused-q-k-rmsnorm-and-complex-rope"></a>
## Require full-image parity for fused Q/K RMSNorm and complex RoPE

- **Outcome** — rejected
- **Reason** — The H3 operator checks passed, yet its complete images failed and the change was reverted. The later kept H10/H13 implementations were different.
- **Revisit when** — Reproduce the reduction, complex FMA ordering and BF16 materialization, then check native full images after the operator comparisons.
- **Keywords**
  - H3
  - Q/K RMSNorm
  - complex RoPE
  - BF16 materialization
  - image quality
- **Scope** — regime_bound

<a id="unit-pair-a-packed-q-k-v-5d-layout-with-full-request-timing"></a>
## Pair a packed Q/K/V 5D layout with full request timing

- **Outcome** — rejected
- **Reason** — H1 passed quality but the exploratory exchange was discarded. The ledger’s standalone trial does not resolve the cost of layout staging or copies.
- **Revisit when** — For a changed topology or layout, keep the comparison matched and account for staging, transfers and request time separately.
- **Keywords**
  - H1
  - QKV
  - packed 5D exchange
  - layout staging
  - copies
- **Scope** — regime_bound

<a id="unit-measure-complete-graph-replay-before-promoting-projection-or-norm-rope-changes"></a>
## Measure complete graph replay before promoting projection or norm/RoPE changes

- **Outcome** — no_gain
- **Reason** — H6 and H7 were removed after failing to produce a material end-to-end gain. H7 includes capture/replay and copy costs that matter to the final decision.
- **Revisit when** — Test a materially different capture boundary or buffer lifetime against a paired full request. Account for capture, replay and copies.
- **Keywords**
  - H6
  - H7
  - graph replay
  - norm RoPE
  - capture boundary
  - post-attention
- **Scope** — regime_bound

<a id="unit-verify-critical-path-time-for-broadcast-scales-and-empty-concatenation-removal"></a>
## Verify critical-path time for broadcast scales and empty concatenation removal

- **Outcome** — no_gain
- **Reason** — The H14/H16 decode scale/gate broadcast and empty concatenation changes were removed or reverted because the trials did not demonstrate a benefit.
- **Revisit when** — Profile the intended configuration to see whether these operations are on its critical path, and retain the matched service control.
- **Keywords**
  - H14
  - H16
  - decode broadcast
  - scale gate
  - empty concat
  - critical path
- **Scope** — regime_bound

<a id="unit-treat-h17-and-the-noisy-h13-run-as-host-confounded-readings"></a>
## Treat H17 and the noisy H13 run as host-confounded readings

- **Outcome** — inconclusive
- **Reason** — Concurrent diagnostics and host load were observed during these attempts, so the timing difference does not isolate the code change.
- **Revisit when** — Repeat the same request on a qualified host without overlapping diagnostics.
- **Keywords**
  - H17
  - H13
  - host load
  - concurrent diagnostics
  - confounded timing
- **Scope** — local
- **Bounds** — The cited exploratory H17 run and noisy H13 attempt.

<a id="unit-carry-a-compiled-launch-api-probe-through-full-pipeline-integration-before-judgi"></a>
## Carry a compiled launch API probe through full-pipeline integration before judging gain

- **Outcome** — inconclusive
- **Reason** — H18 improved host enqueue in a diagnostic. It never went through the complete pipeline, so the resulting service overhead was not measured.
- **Revisit when** — Confirm actual dispatch and full-image correctness in the integrated candidate, then measure request time.
- **Keywords**
  - H18
  - compiled launch API
  - host enqueue
  - pipeline integration
  - dispatch
- **Scope** — regime_bound

<a id="unit-source-files"></a>
## Source files

- [qwen-b300-rejected-directions.json](../../../../../skill_library/methods/inference-optimization-casebook/cases/qwen-b300-rejected-directions.json)
