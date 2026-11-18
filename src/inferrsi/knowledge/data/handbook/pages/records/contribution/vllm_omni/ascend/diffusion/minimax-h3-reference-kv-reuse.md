<!-- handbook
{
  "id": "vllm_omni.ascend.diffusion.minimax_h3_reference_kv_reuse",
  "kind": "record",
  "aliases": [
    "package:vllm_omni.ascend.diffusion.minimax_h3_reference_kv_reuse"
  ],
  "tags": [
    "minimax_h3",
    "ref2va",
    "kv_cache",
    "ulysses",
    "pinned_memory",
    "approximation",
    "counterexample"
  ],
  "carry": [
    "unit-when-this-applies",
    "unit-limits-of-this-evidence"
  ]
}
-->

# MiniMax-H3 reference KV reuse must balance ownership after Ulysses

> Recorded state `imported` · locally verified `false` · evidence level `upstream_reported` · [Source](../../../../../../../repo_packs/vllm_omni/knowledge/ascend/diffusion/minimax-h3-reference-kv-reuse.json)

A reference-KV reuse candidate fixes a slower pre-Ulysses prototype by caching full reference sequences per local head shard after All-to-All; reuse remains quality-sensitive and evidence is one-shot.

`contribution` · `vllm_omni` · `ascend` · `diffusion.video_generation`

<a id="unit-when-this-applies"></a>
## When this applies

- **Hardware**
  - 4× Ascend 910B3, 64 GiB HBM/device
- **Software**
  - Hardware environment vLLM 0.28.0, vllm-omni abbreviated validation commit 85d63868
  - Rebased source revision at import 6de9a18572ba3211fc33f47c8e5beaea8d895e98 targets vLLM 0.30 APIs; local rebase environment was incompatible
- **Models**
  - MiniMax-H3
- **Conditions**
  - USP4/Ring1, 1344×768, 5-second output, 24 FPS, 50 steps
  - Tier2, refresh interval 8, ring size 2, unquantized BF16 host cache
  - 4 images / 2-second reference video / 5-second reference video; one warmup then one measured request each

<a id="unit-what-the-source-reports"></a>
## What the source reports

- **Counterexample.** Pre-Ulysses prototype worsened E2E: 4 images 878321→913491 ms; 2s video 477610→675020 ms; 5s video 925693→1270051 ms. Sequence shards gave uneven reference ownership/H2D critical paths.
- **Upstream reported.** Post-Ulysses E2E: 739566 ms (4 images), 441096 ms (2s video), 846829 ms (5s video), reported reductions 15.80%, 7.65%, 8.52% against disabled baselines. Peak HBM rises slightly.
- **Source inspected.** Post-All-to-All cache keeps the full reference sequence for each rank's local head shard; pinned host storage is staged through a 2–3-slot device ring with ready/consumed events.
- **Quality limit.** Outputs were manually inspected with no obvious difference on tested prompts/seeds; no objective quality metric or repeated variance. INT8/FP8 host-cache modes have unit coverage but no Ascend E2E benchmark.

<a id="unit-putting-the-idea-to-work"></a>
## Putting the idea to work

- Treat periodic reference reuse as approximate unless timestep invariance is proven; BF16 storage alone does not make cached values exact.
- Audit token/head ownership before choosing cache placement. Balance H2D and cache synchronization across SP ranks.
- Separate unquantized reuse from INT8/FP8 host-cache quality/performance rows.

<a id="unit-how-to-check-it"></a>
## How to check it

- Use a dependency-compatible exact branch; do not mix the vLLM 0.28 hardware environment with rebased vLLM 0.30 APIs without revalidation.
- Run targeted reference-KV and parallel tests, including disabled, refresh, ring staging, fallback and SP boundary handling.
- Repeat each matched reference workload at least three times and capture per-rank H2D, memory, latency and balance.
- Compare trajectory/video/audio/temporal metrics, varied prompts/references and refresh policies before promotion.

<a id="unit-limits-of-this-evidence"></a>
## Limits of this evidence

- Unmerged candidate at import; hardware validation source differs from rebased Source revision.
- One-shot measurements after warmup cannot establish variance or production tail latency.
- Objective quality, host quantization E2E, remote reliability and cross-backend portability remain unverified.

<a id="unit-sources"></a>
## Sources

- **Url** — <https://github.com/vllm-project/vllm-omni/>
- **Type** — upstream_report
- **Commit** — 6de9a18572ba3211fc33f47c8e5beaea8d895e98
- **Merge commit** — `null`
- **Status** — open
- **Accessed at** — 2026-10-09
