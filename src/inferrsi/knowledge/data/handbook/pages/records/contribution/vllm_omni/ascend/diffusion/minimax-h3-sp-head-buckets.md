<!-- handbook
{
  "id": "vllm_omni.ascend.diffusion.minimax_h3_sp_head_buckets",
  "kind": "record",
  "aliases": [
    "package:vllm_omni.ascend.diffusion.minimax_h3_sp_head_buckets"
  ],
  "tags": [
    "minimax_h3",
    "ulysses",
    "communication_overlap",
    "head_buckets",
    "quality_gate"
  ],
  "carry": [
    "unit-when-this-applies",
    "unit-limits-of-this-evidence"
  ]
}
-->

# MiniMax-H3 SP head buckets reduce exposed All-to-All with quality still pending

> Recorded state `imported` · locally verified `false` · evidence level `upstream_reported` · [Source](../../../../../../../repo_packs/vllm_omni/knowledge/ascend/diffusion/minimax-h3-sp-head-buckets.json)

An open Ascend head-bucket pipeline overlaps projection/attention with communication; reported latency improves against the same-round chunk path, but full-model output equivalence remains unproven.

`contribution` · `vllm_omni` · `ascend` · `diffusion.video_generation`

<a id="unit-when-this-applies"></a>
## When this applies

- **Hardware**
  - 4× Ascend 910B
- **Software**
  - vLLM 0.29.0, CANN 9.0.0
  - Reported E2E source c36a9b6979a890c4ec9c3e8bf54000174134bea9; imported source revision f9e5d544d33428e17b818be3a01cb7d0956e4ead
- **Models**
  - MiniMax-H3 Ref2VA
- **Conditions**
  - SP4, 1344×768, 124 frames, 24 FPS, 8 steps, seed 3100, guidance 1, flow shift 12
  - Chunk size 64 MiB unchanged; head buckets 0→4
  - Each arm: 2 warmups + formal + profile + formal; only unprofiled formal requests underpin latency comparison

<a id="unit-what-the-source-reports"></a>
## What the source reports

- **Upstream reported.** Same-round chunk mean 88906±4 ms to head-split 85195±574 ms (sample SD, n=2 per arm), reported 4.174% client E2E reduction.
- **Upstream reported.** Diagnostic per-block exposed All-to-All falls 16.359→2.455 ms while compute kernels rise 145.323→147.346 ms; reported benefit is overlap/critical-path shortening, not faster compute kernels.
- **Quality limit.** Author self-review says cross-arm video hashes differ; operator/refactor equivalence checks do not establish full-model quality equivalence. E2E data precedes the current refactor.
- **Source version limit.** A previous-round baseline appears only as reference and must not be used as a matched control for the current 4.17% claim.

<a id="unit-putting-the-idea-to-work"></a>
## Putting the idea to work

- Compare against a matched same-revision control and report exposed communication separately from aggregate collective/kernel duration.
- Tune bucket count as a workload/topology experiment; stream ownership, workspace lifetime and collective ordering are part of correctness.
- Do not adopt a generic no-regression claim from an illustrative scheduling diagram.

<a id="unit-how-to-check-it"></a>
## How to check it

- Run current-head multi-rank parity with uneven buckets, padding, bias, RoPE and workspace reuse.
- Repeat current-head same-source HTTP A/B with at least three unprofiled warm samples and identical placement.
- Evaluate intermediate latents plus video/audio/temporal metrics across prompt/reference sets, using an explicit quality gate.
- Test collective failure/cancellation, memory growth and CLI-to-runtime bucket/chunk propagation.

<a id="unit-limits-of-this-evidence"></a>
## Limits of this evidence

- Unmerged candidate at import, not a main-supported feature declaration.
- Only two unprofiled formal samples per arm; current-head E2E and full-model quality need revalidation.
- Ascend910B/CANN evidence does not validate NVIDIA or ROCm transport.

<a id="unit-sources"></a>
## Sources

- **Url** — <https://github.com/vllm-project/vllm-omni/>
- **Type** — upstream_report
- **Commit** — f9e5d544d33428e17b818be3a01cb7d0956e4ead
- **Merge commit** — `null`
- **Status** — open
- **Accessed at** — 2026-10-09
