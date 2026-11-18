<!-- handbook
{
  "id": "vllm_omni.cuda.diffusion.minimax_h3_adaln_schedule_cache",
  "kind": "record",
  "aliases": [
    "package:vllm_omni.cuda.diffusion.minimax_h3_adaln_schedule_cache"
  ],
  "tags": [
    "minimax_h3",
    "adaln",
    "schedule_cache",
    "memory",
    "offload",
    "counterexample"
  ],
  "carry": [
    "unit-when-this-applies",
    "unit-limits-of-this-evidence"
  ]
}
-->

# MiniMax-H3 exact AdaLN schedule cache: capacity benefit can exceed latency benefit

> Recorded state `imported` · locally verified `false` · evidence level `upstream_reported` · [Source](../../../../../../../repo_packs/vllm_omni/knowledge/cuda/diffusion/minimax-h3-adaln-schedule-cache.json)

A schedule-cache candidate precomputes finite-schedule AdaLN tables and can release projection weights; production-shape compiled measurements show capacity savings without a distinguishable speed gain.

`contribution` · `vllm_omni` · `cuda` · `diffusion.video_generation`

<a id="unit-when-this-applies"></a>
## When this applies

- **Hardware**
  - 2× NVIDIA H20 98 GB for TP2; one H20 for the separately reported layerwise run
- **Software**
  - Source/hardware revision 635215a96d3eaf6b5bac66020feae51b34daa5c9
  - Python 3.12, PyTorch 2.11.0+cu128, vLLM 0.26.0, FlashAttention
- **Models**
  - MiniMax-H3 FL2VA / T2VA
- **Conditions**
  - Small eager row: 448×256, 29 requested/39 aligned frames, 50 sigma points/49 forwards, seed 42, TP2/text-encoder TP2, flow shifts 12/3
  - Production regional-compile row: 1248×768, 209 frames, 50 steps, seed 2101, TP2
  - Single request in flight; schedule hits and cold misses measured separately

<a id="unit-what-the-source-reports"></a>
## What the source reports

- **Upstream reported.** Small eager row: five steady requests after warmup; wall mean 15285.8 ms disabled, 14987.9 ms cache retained, 15029.4 ms cache+weight-offload. These are roughly 1.95% and 1.68% reductions for that row.
- **Upstream reported.** Per TP rank, 12.144 GiB projection weights replaced by 0.885 GiB tables yields 11.259 GiB net device-memory reduction by accounting. First-build peak still includes coexisting weights and tables.
- **Counterexample.** Production compiled row: one measured steady sample per mode; retained cache changed client wall 1298497→1298456 ms, effectively no distinguishable speed benefit. Weight offload increased client wall to 1305133 ms (~0.51% slower) while lowering residency ~11.256 GiB/device.
- **Upstream reported.** Fixed steady outputs were reported byte-identical across the three modes. Schedule changes require restore/build/atomic replace/re-offload and can add substantial miss latency; cold-to-steady audio differences also exist in the disabled control.

<a id="unit-putting-the-idea-to-work"></a>
## Putting the idea to work

- Treat weight release as a capacity optimization with a latency/memory frontier, not an additional automatic speedup.
- Key exact schedules and all dependent configuration/adapter/device/dtype identities; bound cache size and preserve distributed ownership.
- Reserve memory for cold build and schedule replacement; a lower steady footprint cannot solve an unfit first-build phase.

<a id="unit-how-to-check-it"></a>
## How to check it

- Use the pinned source implementation or first verify an equivalent path exists in target source; it was open at import.
- A/B cache off, cache retained and cache+offload with fixed workload and compile state, at least three warm repeats.
- Measure cold miss, same-schedule hit and changed-schedule rebuild independently; capture NVML/device and allocator peaks.
- Compare steady output hashes plus decoded video/audio and test layerwise/HSDP/quantized ownership separately.

<a id="unit-limits-of-this-evidence"></a>
## Limits of this evidence

- Source candidate unmerged at import; target main support is not implied.
- Production-shape deltas are one-sample observations and sub-1% values do not establish statistically meaningful speed changes.
- H20 and specific versions/schedules only; H200/B200 or another backend needs new validation.

<a id="unit-sources"></a>
## Sources

- **Url** — <https://github.com/vllm-project/vllm-omni/>
- **Type** — upstream_report
- **Commit** — 635215a96d3eaf6b5bac66020feae51b34daa5c9
- **Merge commit** — `null`
- **Status** — open
- **Accessed at** — 2026-10-09
