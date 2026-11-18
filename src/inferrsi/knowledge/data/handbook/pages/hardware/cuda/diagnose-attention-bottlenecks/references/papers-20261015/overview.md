<!-- handbook
{
  "id": "hardware/cuda/diagnose-attention-bottlenecks/references/papers-20261015/overview",
  "kind": "guide"
}
-->

# Pack D: Attention bottlenecks after IO reduction

> Recorded state `candidate` · empirical validation `not_run` · [Source](../../../../../../../skill_library/hardware/cuda/diagnose-attention-bottlenecks/references/papers-20261015/README.md) · [Scope and provenance](../../../../../../../skill_library/hardware/cuda/diagnose-attention-bottlenecks/metadata.json) · [Parent reading](../../lesson.md)

> Supplier delivery snapshot, 2026-10-15. Packaging checks and inventory below refer to the original pack, not to this relocated integration. Empirical validation remains not_run.



Status: **candidate**. Empirical validation: **not_run**. Read-only paper extraction completed 2026-10-15; no implementation, benchmark, hardware run, installation, or InferRSI change.

Approved corpus only: FlashAttention `2205.14135v2`, FlashAttention-2 `2307.08691v1`, FlashAttention-3 `2407.08608v2`. Their PDF version stamps were directly checked. This is a historical, version-specific extraction, not a statement about current libraries.

<a id="unit-result"></a>
## Result

The useful progression is a change in the limiting resource, not a ranking of three headline speedups:

1. Avoid materializing quadratic attention intermediates in device HBM, using online softmax and selective recomputation.
2. Once those transfers are reduced, inspect non-matmul operations, insufficient independent work, and inter-warp reduction traffic.
3. With asynchronous hardware, schedule data movement and independent iterations around the remaining dependencies, while accounting for register and shared-memory pressure.
4. Faster low-precision matmul shifts more weight onto softmax, data layout and numerical error. A faster arithmetic format does not establish faster or acceptable attention.

<a id="unit-deliverables-and-why-these-boundaries"></a>
## Deliverables and why these boundaries

- One [operational skill](../../lesson.md), because all three papers inform the same decision: identify the currently exposed attention bottleneck before choosing the next intervention. Three version-named skills would duplicate its trigger and evidence gate.
- [Mechanism notes](../mechanisms.md), with objective, assumptions, variables, mechanism, benefit/cost, evidence, limits, and proposed rule for each mechanism.
- [Exact source readsets and pins](../sources.md), including prior-coverage reconciliation and what was not read.
- Three decision cases: [IO reduction can plateau](cases/io-reduction-can-plateau.md), [partitioning after fusion](cases/partitioning-after-fusion.md), and [overlap and FP8 counter-signals](cases/overlap-and-fp8-counter-signals.md). They retain different failure tests and are not three independent local experiments.
- One [knowledge note](knowledge/attention-cost-model-boundaries.md) separating transferable cost reasoning from hardware primitives and metric denominators.
- [Integration proposals](INTEGRATION_NOTES.md) for the existing two matrices only; [unread next-gate leads](NEXT_GATE_LEADS.md) are segregated.

`F` marks paper facts, including author-reported results and stated limitations. `P` marks our proposed operating procedure or inference. No `P` has been validated. Device HBM, SMEM/SRAM and registers stay in the **Accelerator** domain; these papers add no host-RAM, SSD or network evidence.
