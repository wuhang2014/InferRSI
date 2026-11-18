<!-- handbook
{
  "id": "vllm_omni.cuda.diffusion.minimax_h3_ref2va_teacache",
  "kind": "record",
  "aliases": [
    "package:vllm_omni.cuda.diffusion.minimax_h3_ref2va_teacache"
  ],
  "tags": [
    "minimax_h3",
    "ref2va",
    "teacache",
    "approximation",
    "quality",
    "request_isolation",
    "counterexample"
  ],
  "carry": [
    "unit-when-this-applies",
    "unit-limits-of-this-evidence"
  ]
}
-->

# MiniMax-H3 Ref2VA TeaCache needs task-specific calibration and step defaults

> Recorded state `imported` · locally verified `false` · evidence level `upstream_reported` · [Source](../../../../../../../repo_packs/vllm_omni/knowledge/cuda/diffusion/minimax-h3-ref2va-teacache.json)

A Ref2VA TeaCache candidate calibrates a conservative late-step budget; quality and speed depend on task/step policy, and some cases produce zero hits and no gain.

`contribution` · `vllm_omni` · `cuda` · `diffusion.video_generation`

<a id="unit-when-this-applies"></a>
## When this applies

- **Hardware**
  - 1× NVIDIA B300
- **Software**
  - Unmerged source revision at import f86bd6ad7bfc7e6eb04df0aaacd35ec68643d6a2
  - BF16, CUDNN_ATTN, task-specific TeaCache coefficients
- **Models**
  - MiniMax-H3 Ref2VA
- **Conditions**
  - 448×256, 107 output frames, 50 configured steps; fixed-seed comparison
  - Calibration uses 15 full-compute Ref2VA cases: 6 image, 6 image+audio, 3 video+audio
  - 35 initial full-compute denoise calls, then at most five cache hits; other step counts remain uncached

<a id="unit-what-the-source-reports"></a>
## What the source reports

- **Upstream reported.** Video+audio example: 5/49 cache hits; latency 244190→221240 ms, video SSIM 0.9795/PSNR 41.60 dB and audio PSNR 168.8 dB. This demonstrates a speed/quality tradeoff, not exact equivalence.
- **Counterexample.** Image-only example: 0/49 hits; 53340→53260 ms, SSIM 1.000 and sample-identical audio. No meaningful speed gain was observed.
- **Upstream reported.** Both video+audio runs peak at 140972 MiB; caching reduces compute and is not a weight-memory solution.
- **Review finding.** An omitted num_inference_steps initially resolved to 0 in cache refresh while the pipeline used 50, bypassing calibrated warmup. Author reports a fix at 0d9594f21 preserved in f86bd6ad7, with shared effective defaults and regressions.

<a id="unit-putting-the-idea-to-work"></a>
## Putting the idea to work

- Treat residual reuse as approximate; keep task-specific calibrated policies and explicit step fallback.
- Maintain separate hooks/request state for FL2VA and Ref2VA; do not copy residuals across tasks or concurrent requests.
- Record actual cache hits and effective step schedule, not just an enabled flag; validate custom thresholds across video and audio.

<a id="unit-how-to-check-it"></a>
## How to check it

- Use the exact source revision or verify target-source task support; the candidate was unmerged at import.
- Test explicit 50 steps, omitted steps, non-50 steps, task alternation and error/abort reset behavior.
- Same-seed A/B across multiple prompt/media types; measure video, temporal and audio metrics with an explicit acceptance threshold.
- Run at least three unprofiled warm repetitions and measure device/host memory separately from compute reduction.

<a id="unit-limits-of-this-evidence"></a>
## Limits of this evidence

- Unmerged candidate at import; no claim of main support or InferRSI reproduction.
- Reported quality results are a small same-seed sample set; full perception/temporal quality acceptance remains user-specific.
- TeaCache and Cache-DiT are separate mutually exclusive backend choices in the reviewed branch.

<a id="unit-sources"></a>
## Sources

- **Url** — <https://github.com/vllm-project/vllm-omni/>
- **Type** — upstream_report
- **Commit** — f86bd6ad7bfc7e6eb04df0aaacd35ec68643d6a2
- **Merge commit** — `null`
- **Status** — open_draft
- **Accessed at** — 2026-10-09
