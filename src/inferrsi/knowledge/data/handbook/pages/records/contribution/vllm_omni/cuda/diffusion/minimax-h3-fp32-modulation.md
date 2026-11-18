<!-- handbook
{
  "id": "vllm_omni.cuda.diffusion.minimax_h3_fp32_modulation",
  "kind": "record",
  "aliases": [
    "package:vllm_omni.cuda.diffusion.minimax_h3_fp32_modulation"
  ],
  "tags": [
    "minimax_h3",
    "operator_fusion",
    "modulation",
    "rounding",
    "platform_dispatch",
    "counterexample"
  ],
  "carry": [
    "unit-when-this-applies",
    "unit-limits-of-this-evidence"
  ]
}
-->

# MiniMax-H3 modulation fusion changes rounding and requires platform guards

> Recorded state `imported` · locally verified `false` · evidence level `upstream_reported` · [Source](../../../../../../../repo_packs/vllm_omni/knowledge/cuda/diffusion/minimax-h3-fp32-modulation.json)

Merged FP32-accumulating modulation fusion reduces launch count but removes intermediate BF16 rounding; its numerical drift and historical non-CUDA dispatch finding must remain visible.

`contribution` · `vllm_omni` · `cuda` · `diffusion.video_generation`

<a id="unit-when-this-applies"></a>
## When this applies

- **Hardware**
  - CUDA GPU SKU not stated in source benchmark; do not substitute H200/B200
- **Software**
  - Source revision 7d74126f0723d355d82b47e98f820394320e1a4a; merged 14f2c16fb28e1e0c8615372675f2757466260ad8
  - Triton modulation path, eager, USP4
- **Models**
  - MiniMax-H3 Ref2VA
- **Conditions**
  - 5-second output, 49 denoise iterations; both configurations warmed up
  - Report hardware/driver/runtime identity before reproduction

<a id="unit-what-the-source-reports"></a>
## What the source reports

- **Upstream reported.** Engine E2E fell from 136961 ms to 134707 ms (1.65%); a single DiT profile reports 1969→1234 CUDA kernels (37.33% fewer). Profiled wall time is diagnostic and not interchangeable with unprofiled engine E2E.
- **Upstream reported.** FP32 accumulation removes intermediate BF16 rounding. Reported output PSNR is 39.55 dB and SSIM 0.9750; the author explicitly says outputs are not bit-exact.
- **Review finding.** Review identified x.is_cpu-only gating, which could launch Triton on NPU/XPU/MUSA, and noted row-major contiguity assumptions. The fetched source patch still contains that historical guard; verify subsequent target-source fixes rather than inferring safe non-CUDA support.

<a id="unit-putting-the-idea-to-work"></a>
## Putting the idea to work

- Classify this as a numerically changed implementation and require an explicit quality tolerance.
- Preserve original BF16 materialization boundaries when designing an exact fusion; otherwise report the changed rounding.
- Gate fast paths by platform, device, dtype, shape and layout; retain backend-native norm/eager fallbacks.

<a id="unit-how-to-check-it"></a>
## How to check it

- Verify current source platform guards and contiguity contract before remote use.
- Compare operator outputs, trajectory drift and decoded video/audio against a same-seed reference and baseline self-run variance.
- Repeat unprofiled E2E measurements with exact device/runtime identity; retain profile evidence separately.
- Run fallback checks on each advertised backend; CPU tests alone do not validate CUDA/NPU numerical paths.

<a id="unit-limits-of-this-evidence"></a>
## Limits of this evidence

- Hardware SKU, repeat count and broader prompt coverage are not stated in the source report.
- Merged code is not proof of quality equivalence or safe support on every backend.
- Historical review findings may have changed later; source revision must be rechecked.

<a id="unit-sources"></a>
## Sources

- **Url** — <https://github.com/vllm-project/vllm-omni/>
- **Type** — upstream_report
- **Commit** — 7d74126f0723d355d82b47e98f820394320e1a4a
- **Merge commit** — 14f2c16fb28e1e0c8615372675f2757466260ad8
- **Status** — merged
- **Accessed at** — 2026-10-09
