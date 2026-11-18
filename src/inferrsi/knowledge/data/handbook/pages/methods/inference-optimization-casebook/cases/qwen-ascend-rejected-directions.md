<!-- handbook
{
  "id": "case.qwen-ascend-rejected-directions",
  "kind": "case",
  "aliases": [
    "checkout:case.qwen-ascend-rejected-directions"
  ],
  "tags": [
    "negative-evidence",
    "resource-failure",
    "OOM",
    "no-demonstrated-gain",
    "RoPE",
    "fusion-attention",
    "task-queue"
  ],
  "carry": [
    "unit-when-this-applies",
    "unit-limits-of-this-evidence"
  ]
}
-->

# Qwen Ascend: reported rejected directions

> Recorded state `author_reported` · [Source](../../../../../skill_library/methods/inference-optimization-casebook/cases/qwen-ascend-rejected-directions.md) · [Scope and provenance](../../../../../skill_library/methods/inference-optimization-casebook/cases/qwen-ascend-rejected-directions.json) · [Parent reading](../lesson.md)

These observations come from the [pinned Ascend guide](https://github.com/InferMatrixLab/InferRSI/blob/d51c941dc57807c1e16ea698cd9291f414110c45/docs/qwen-image-2.1-turbo-ascend.md),
which attributes them to amy-why-3459 at the upstream head recorded in the
typed record below.
They apply to its one-910B1, BF16, eager, 1280x704, native eight-sigma cohort.
They are author-reported, `locally_verified=false`, with InferRSI acceptance
INCONCLUSIVE. No raw timings, images or frozen validator were imported.
Kind, origin, state and source identities belong to the
[typed source and scope record](../../../../../skill_library/methods/inference-optimization-casebook/cases/qwen-ascend-rejected-directions.json).

| Direction | Recorded observation and disposition | Suggested revisit condition and first check |
| --- | --- | --- |
| Cache eager RoPE cos/sin or expanded SDPA masks | Pixel-identical, but discarded as slower in the source trials. | Profile current recomputation and retained-tensor costs; qualify a matched timing cohort before attributing a regression. |
| Cache per-step masks and prompt tensors | NPU OOM. | First inventory live tensor lifetimes and allocator headroom. A different residency policy or workload may change feasibility; the report does not establish a universal memory limit. |
| Fusion attention, including precise=2/0 and mask-free steps | No gain or a gain below the source keep criterion. | Check exact mask, dtype, shapes and device support; run operator quality then complete pipeline timing. Do not reuse the source keep threshold as a repository default. |
| TASK_QUEUE_ENABLE=1/2 or enforce_eager=0 | No gain or slower than the source eager configuration. | Inspect the actual execution path and scheduling overhead under the new stack; repeat with unchanged workload and warmups. |
| RoPE + VAE fastpath + fusion attention | Initialization OOM for this triple stack. | Inventory initialization residency before attempting a new combination. |
| Separate kept RoPE + VAE stack on a later busy host | Later requests failed resource reservation; this is a different stack/host cohort from the triple-stack initialization failure. | Qualify current headroom and outside contention before retrying; do not attribute this resource blockage to fusion attention. |

Revisit checks are new diagnostic suggestions, not reproduced causes or a
performance claim. Pixel identity and a looser quality gate remain separate.
The independently reported 910B3 cohort and CUDA results are different scopes;
neither automatically overturns nor confirms a 910B1 observation.

<a id="unit-when-this-applies"></a>
## When this applies

- Author-reported single Ascend 910B1 Qwen-Image-2.1-Turbo cohort
- BF16, eager, TORCH_SDPA, CFG=1, 1280x704, native eight sigmas

<a id="unit-limits-of-this-evidence"></a>
## Limits of this evidence

- Imported author report; locally_verified=false
- Raw request timings, RGBA outputs and frozen validator are absent from this import
- InferRSI acceptance remains INCONCLUSIVE; the source 30 percent target was not met
- No cross-device or HTTP-serving qualification

<a id="unit-check-eager-rope-table-and-expanded-sdpa-mask-retention-against-recomputation"></a>
## Check eager RoPE table and expanded SDPA mask retention against recomputation

- **Outcome** — no_gain
- **Reason** — The source trials produced identical pixels with retained cos/sin or expanded masks, but those alternatives were slower and were discarded.
- **Revisit when** — On the target shapes, measure the work avoided and the lifetime and cost of the retained tensors in a paired end-to-end run.
- **Keywords**
  - eager RoPE
  - cos sin precompute
  - SDPA mask
  - pixel identical
  - retention cost
- **Scope** — regime_bound

<a id="unit-budget-live-npu-memory-before-retaining-per-step-masks-and-prompt-tensors"></a>
## Budget live NPU memory before retaining per-step masks and prompt tensors

- **Outcome** — rejected
- **Reason** — That cache configuration exhausted device memory on the reported run. Its feasibility depends on what stays resident alongside the cached tensors.
- **Revisit when** — Inspect tensor lifetimes, allocator headroom and peak residency. Retry a paired test when the request shape or residency policy materially changes.
- **Keywords**
  - cache per-step masks
  - prompt tensors
  - NPU OOM
  - device memory
  - allocator headroom
- **Scope** — local

<a id="unit-qualify-fusion-attention-with-the-actual-mask-dtype-and-shape"></a>
## Qualify fusion attention with the actual mask, dtype and shape

- **Outcome** — no_gain
- **Reason** — The recorded fusion-attention runs, including precise=2 and precise=0 and steps without masks, showed either no gain or a gain below the source experiment’s keep criterion.
- **Revisit when** — Verify dispatch and numerical behavior for the present mask and tensor layout. Follow operator checks with a matched pipeline timing.
- **Keywords**
  - fusion attention
  - precise=2
  - precise=0
  - mask-free
  - Ascend
- **Scope** — regime_bound

<a id="unit-recheck-queueing-and-graph-mode-under-the-target-stack"></a>
## Recheck queueing and graph mode under the target stack

- **Outcome** — no_gain
- **Reason** — TASK_QUEUE_ENABLE=1/2 and enforce_eager=0 failed to improve the recorded eager configuration; some variants were slower.
- **Revisit when** — Confirm the execution route and scheduling overhead after a runtime change, with a fixed workload and equal warmups across arms.
- **Keywords**
  - TASK_QUEUE_ENABLE
  - enforce_eager
  - host dispatch
  - task queue
  - eager execution
- **Scope** — regime_bound

<a id="unit-check-initialization-residency-before-combining-rope-vae-and-attention-fast-path"></a>
## Check initialization residency before combining RoPE, VAE and attention fast paths

- **Outcome** — rejected
- **Reason** — The run with RoPE, the VAE fastpath and fusion attention ran out of memory during initialization. This identifies a failure phase for that particular combination.
- **Revisit when** — Measure what each component reserves during initialization before assembling another multi-path configuration.
- **Keywords**
  - RoPE VAE fusion attention
  - triple stack
  - initialization OOM
  - startup memory
- **Scope** — local
- **Bounds** — Triple-stack initialization, separate from later two-path requests on a busy host.

<a id="unit-qualify-host-headroom-for-the-later-rope-and-vae-reservation-failure"></a>
## Qualify host headroom for the later RoPE and VAE reservation failure

- **Outcome** — inconclusive
- **Reason** — A later run of the kept two-path stack on a busy host encountered resource-reservation failures. Fusion attention was not part of that stack.
- **Revisit when** — Check available device resources and contention on the target host before judging repeatability or timing.
- **Keywords**
  - kept RoPE VAE fastpath
  - busy host
  - resource reservation
  - outside contention
- **Scope** — local
- **Bounds** — Later resource-reservation failure for the separate RoPE plus VAE stack.

<a id="unit-source-files"></a>
## Source files

- [qwen-ascend-rejected-directions.json](../../../../../skill_library/methods/inference-optimization-casebook/cases/qwen-ascend-rejected-directions.json)
