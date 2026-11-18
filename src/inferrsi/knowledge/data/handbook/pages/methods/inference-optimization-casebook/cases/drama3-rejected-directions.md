<!-- handbook
{
  "id": "case.drama3-rejected-directions",
  "kind": "case",
  "aliases": [
    "checkout:case.drama3-rejected-directions"
  ],
  "tags": [
    "negative-evidence",
    "service-regression",
    "quality-rejection",
    "harness-mismatch",
    "prefix-reuse",
    "memory-compression",
    "analysis-only"
  ],
  "carry": [
    "unit-when-this-applies",
    "unit-limits-of-this-evidence"
  ]
}
-->

# Drama3 B300: rejected directions and invalid controls

> Recorded state `historical_observation` · [Source](../../../../../skill_library/methods/inference-optimization-casebook/cases/drama3-rejected-directions.md) · [Scope and provenance](../../../../../skill_library/methods/inference-optimization-casebook/cases/drama3-rejected-directions.json) · [Parent reading](../lesson.md)

The [pinned diagnostic ledger](https://github.com/InferMatrixLab/InferRSI/blob/d51c941dc57807c1e16ea698cd9291f414110c45/evidence/drama3-b300-scale150/results/diagnostic-lessons.md)
and [acceptance issue #10](https://github.com/InferMatrixLab/InferRSI/issues/10)
own the observations and exact runtime/artifact pins. The campaign remains
INCONCLUSIVE and optimization is paused. A completed individual gate failure
does not supply missing concurrency/repetition evidence. No experiment is
reopened and no external raw trace is rehashed here.
Kind, origin, state and source identities belong to the
[typed source and scope record](../../../../../skill_library/methods/inference-optimization-casebook/cases/drama3-rejected-directions.json).

| Direction | Recorded observation and disposition | Suggested revisit condition and first check |
| --- | --- | --- |
| Fused tower projections / multi-step decode | Faster or correct in isolated checks but no full-service throughput gain; multi-step decode delayed admission. | Measure actual active batches, admission/drain and complete service latency, including sampling and codec. Kernel timing alone cannot select the runtime. |
| Async service / overlap | Early fixed-request controls passed while service WER failed in both arms. Later bounded dynamic replay identified shared ATen cuBLAS workspace interference: dedicated codec capture matched tested states, and fresh private-capture service WER passed while shared capture failed. The runtime added a dedicated-capture guard. | Preserve the required private/dedicated capture setup and unchanged controls. This specific reproducer does not establish one cause for every historical WER failure, or qualify arbitrary overlap/throughput; all-concurrency acceptance remains unmet. |
| Production prefix reuse | Extensive graph/state checks and both full quality groups passed, yet the complete C64 service continuation gate failed; default-off. | Retain final drain and all returned work. Investigate the actual schedule and GPU critical path before retrying; removed MoE rows and intake-only rates cannot replace the failed service score. |
| Initial prefix-reuse harness comparison | Compared different private padding histories; mismatch was confined to a private slot before later states were checked. Corrected identical-input controls reran it. | Reset complete physical input rows and run A/A before blaming production math. Do not reuse this superseded setup failure as evidence of model incompatibility. |
| Transparent VMM weight compression | Native correctness/lifetime checks passed, but the fixed three-body screen missed its frozen timing gate; no runtime promotion. | First measure the current bottleneck and physical traffic/compression where possible. Mapped flags and logical capacity do not prove a bandwidth benefit. |
| Producer scale-tile cache | Complete-body reductions missed the source gate; stopped without model/service promotion. | New shapes or a different resource regime may justify another bounded screen; do not subtract unrelated historical screens to infer a cause. |
| Fixed eight-lane FP8 SIMT proposal | Stopped at CPU/AOT cost analysis for that mapping, before a runtime benchmark. | Revisit only with a changed mapping or supported cost model; this is an analytical rejection, not an empirical GPU failure or universal ceiling. |

The last column is proposed diagnosis. Preserve native computation, precision
and frozen acceptance rules; none of these cases authorizes a lossy shortcut,
looser validator or a resumed hardware campaign.

<a id="unit-when-this-applies"></a>
## When this applies

- Drama3 standalone native-computation runtime on one B300
- Only each cited microbenchmark, fixed-state diagnostic or complete service trial

<a id="unit-limits-of-this-evidence"></a>
## Limits of this evidence

- Campaign remains INCONCLUSIVE and optimization is paused
- Individual completed gate failures do not complete the all-concurrency acceptance matrix
- Repository summary inspected; external raw traces and runtime artifacts not rerun or rehashed
- No root cause inferred from client accounting or cross-screen timing subtraction

<a id="unit-qualify-fused-tower-projections-and-longer-decode-groups-at-service-scope"></a>
## Qualify fused tower projections and longer decode groups at service scope

- **Outcome** — no_gain
- **Reason** — The recorded isolated checks could be correct or faster while full-service throughput did not improve. Multi-step decode also deferred new admissions.
- **Revisit when** — Check active batch sizes through admission and drain, then time the complete path with sampling and codec under the same service workload.
- **Keywords**
  - tower projection fusion
  - multi-step decode
  - throughput
  - delayed admission
  - codec
- **Scope** — regime_bound

<a id="unit-check-aten-cublas-workspace-sharing-when-codec-capture-changes-wer"></a>
## Check ATen cuBLAS workspace sharing when codec capture changes WER

- **Outcome** — caveat
- **Reason** — The fixed-request controls initially passed despite service WER failures in both arms. In a later bounded replay, private codec capture passed the tested service control while shared capture failed; the runtime guarded dedicated capture.
- **Revisit when** — Preserve the private/dedicated capture setup and matched controls. Establish WER and throughput for the proposed overlap and concurrency separately.
- **Keywords**
  - async service
  - codec graph capture
  - WER
  - shared ATen cuBLAS workspace
  - private capture
- **Scope** — regime_bound

<a id="unit-require-the-complete-c64-continuation-gate-for-production-prefix-reuse"></a>
## Require the complete C64 continuation gate for production prefix reuse

- **Outcome** — rejected
- **Reason** — The graph/state checks and both full quality groups passed, while the complete C64 continuation gate failed. The recorded production default stayed off.
- **Revisit when** — Keep all returned work and final drain in the replay. Inspect the actual schedule and GPU critical path before proposing another production setting.
- **Keywords**
  - prefix reuse
  - C64 continuation gate
  - default-off
  - final drain
  - full quality groups
- **Scope** — regime_bound

<a id="unit-reset-private-padding-rows-before-an-a-a-state-comparison"></a>
## Reset private padding rows before an A/A state comparison

- **Outcome** — caveat
- **Reason** — The initial prefix-reuse comparison paired distinct physical padding histories. The reported discrepancy was in a private slot, and an identical-input control superseded that setup.
- **Revisit when** — Recreate all physical input rows with identical histories and finish A/A before interpreting any later state mismatch.
- **Keywords**
  - prefix reuse control
  - private padding history
  - physical rows
  - identical-input
  - A/A
- **Scope** — local
- **Bounds** — Initial Drama3 prefix-reuse harness comparison, later replaced by matched-input controls.

<a id="unit-require-physical-traffic-and-a-timing-win-before-enabling-transparent-vmm-compre"></a>
## Require physical traffic and a timing win before enabling transparent VMM compression

- **Outcome** — no_gain
- **Reason** — VMM compression passed native correctness and lifetime checks, yet its fixed three-body screen missed the frozen timing gate. The runtime did not promote it.
- **Revisit when** — Confirm the workload is bandwidth-sensitive and measure physical bytes or effective compression together with the complete timed body.
- **Keywords**
  - transparent VMM
  - weight compression
  - physical traffic
  - native lifetime
  - three-body timing
- **Scope** — regime_bound

<a id="unit-measure-complete-kernels-before-retaining-a-producer-scale-tile-cache"></a>
## Measure complete kernels before retaining a producer scale-tile cache

- **Outcome** — no_gain
- **Reason** — The producer scale-tile cache did not meet its complete-body reduction gate. The screen stopped before model or service promotion.
- **Revisit when** — Run a bounded screen for a materially different shape or resource constraint. Include a matched complete kernel as the control.
- **Keywords**
  - producer scale tile cache
  - complete-body
  - source gate
  - kernel timing
  - resource regime
- **Scope** — regime_bound

<a id="unit-revisit-fp8-simt-only-with-an-improved-mapping-or-cost-case"></a>
## Revisit FP8 SIMT only with an improved mapping or cost case

- **Outcome** — rejected
- **Reason** — The fixed eight-lane mapping was stopped by CPU/AOT analysis before runtime evaluation. No accelerator timing supports a hardware-wide conclusion.
- **Revisit when** — Supply a different lane mapping or a supported cost model before deciding whether a native run is warranted.
- **Keywords**
  - FP8 SIMT
  - eight-lane mapping
  - CPU/AOT
  - cost analysis
  - runtime benchmark
- **Scope** — regime_bound

<a id="unit-source-files"></a>
## Source files

- [drama3-rejected-directions.json](../../../../../skill_library/methods/inference-optimization-casebook/cases/drama3-rejected-directions.json)
