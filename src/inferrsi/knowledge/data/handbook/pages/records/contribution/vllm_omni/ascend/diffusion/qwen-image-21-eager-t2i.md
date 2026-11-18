<!-- handbook
{
  "id": "vllm_omni.ascend.diffusion.qwen_image_21_eager_t2i",
  "kind": "record",
  "aliases": [
    "package:vllm_omni.ascend.diffusion.qwen_image_21_eager_t2i"
  ],
  "tags": [
    "qwen_image_21",
    "text_to_image",
    "rope",
    "npu_rotary_mul",
    "vae",
    "counterexample",
    "quality_gate"
  ],
  "carry": [
    "unit-when-this-applies",
    "unit-limits-of-this-evidence"
  ]
}
-->

# Qwen-Image-2.1 eager text-to-image on one 910B1: reuse plus interleaved RoPE, 30% not met

> Recorded state `imported` · locally verified `false` · evidence level `upstream_reported` · [Source](../../../../../../../repo_packs/vllm_omni/knowledge/ascend/diffusion/qwen-image-21-eager-t2i.json)

The author reports: On one Ascend 910B1, conditioning reuse plus npu_rotary_mul interleaved RoPE cuts the eager BF16 1280×704 eight-step mean from 3111.5 ms to 2459.6 ms with identical RGBA. Opt-in VAE fastpath reaches 2425.5 ms and passes the quality gate without pixel identity. A 30% line at 2178 ms was not met.

`contribution` · `vllm_omni` · `ascend` · `diffusion.image_generation`

<a id="unit-when-this-applies"></a>
## When this applies

- **Hardware**
  - 1× Ascend 910B1, 64 GiB HBM
- **Software**
  - vLLM 0.31.0
  - vllm-omni branch amy/qwen-image-21-conditioning-reuse at 399cc01d1bc4542964d91aaa17fb43862a8cf3b3
- **Models**
  - Qwen-Image-2.1-Turbo
- **Conditions**
  - BF16, eager, TORCH_SDPA, CFG=1, 1280×704, checkpoint native 8 sigmas
  - Two warmup rounds, then three repeated prompts with seeds 42/43/44
  - Unoptimized baseline mean 3111.5 ms; 30% line is 2178 ms
  - QWEN21_NPU_ROPE defaults to fused; QWEN21_NPU_ROPE=eager restores the unflatten/stack path
  - QWEN21_VAE_FASTPATH, QWEN21_ATTN and QWEN21_CACHE_STEP_INPUTS stay off unless set

<a id="unit-what-the-source-reports"></a>
## What the source reports

- **Upstream reported.** Conditioning reuse only: mean 2654.3 ms, −14.7% vs 3111.5 ms, decoded RGBA identical. An earlier same-patch cohort on this host was 2658.2 ms (−14.6%).
- **Upstream reported.** Reuse plus npu_rotary_mul interleaved RoPE: mean 2459.6 ms, −21.0%, RGBA identical. Atlas A2 npu_apply_rotary_pos_emb has no interleave mode. The fp32 cos/sin table follows the current freqs object; decode slices a longer table to the target-token tail.
- **Upstream reported.** Reuse plus NPU RoPE plus QWEN21_VAE_FASTPATH=1: mean 2425.5 ms, −22.0%. Quality gate passed (SSIM≥0.99, PSNR≥35 dB) and pixels were not identical. A later rerun of the same stack was 2431.9 ms (−21.8%).
- **Upstream reported.** A timed first request on the RoPE plus VAE stack spent about 550 ms in prompt encode, 1.5 s in the eight-step denoise, and 190 ms in the VAE.
- **Counterexample.** Rejected without changing steps, resolution, or the sampler: eager RoPE cos/sin cache 2657.2 ms; expanded SDPA mask cache 2667.5 ms; npu_fusion_attention precise=2 at 2655.2 ms and precise=0 at 2623.7 ms; decode-only fusion 2631.7 ms; TASK_QUEUE_ENABLE=1 at 2654.4 ms and =2 at 2661.1 ms; enforce_eager=0 at 2718.8 ms; dropping the prompt-cache autograd guard at 2474.7 ms.
- **Counterexample.** Per-step mask/prompt tensor cache, and RoPE plus VAE fastpath plus fusion attention, failed with NPU out-of-memory during allocation or initialization.
- **Quality limit.** The 2425.5 ms stack is not pixel-identical. Do not describe it as the B300 384.16→266.60 ms five-group HTTP PASS.

<a id="unit-putting-the-idea-to-work"></a>
## Putting the idea to work

- Keep npu_rotary_mul interleaved RoPE as the NPU default for this complex-pair layout, with QWEN21_NPU_ROPE=eager as the fallback.
- Treat QWEN21_VAE_FASTPATH as opt-in until a pixel-identical VAE path exists.
- Do not enable npu_fusion_attention or per-step input caching on a 64 GiB 910B1 that is already near a 30 GiB allocator watermark.
- Budget the next hypothesis on the eight-step denoise, which remains the largest timed piece.

<a id="unit-how-to-check-it"></a>
## How to check it

- Repeat the three-seed warm cohort on a quiet 910B1 before quoting a new mean.
- Keep pixel identity and the SSIM/PSNR gate as separate columns.
- Re-time prompt encode, denoise, and VAE on a warm cache hit before claiming another stage win.

<a id="unit-limits-of-this-evidence"></a>
## Limits of this evidence

- Single 910B1 eager cohort. Not a four-card B300 HTTP result and not a 30% PASS.
- Three measured requests after warmup. No production tail claim.
- Later repeats were blocked when the allocator could not reserve a small extra block and the NPU runtime reported insufficient compute resources.
- Ascend 910B1 evidence does not transfer to CUDA, ROCm, or other Ascend SKUs.
- Imported from amy-why-3459's report; raw per-request timings, RGBA outputs and a frozen validator are not included. No NPU rerun was performed for this import; InferRSI acceptance remains INCONCLUSIVE.

<a id="unit-sources"></a>
## Sources

- **Url** — <https://github.com/vllm-project/vllm-omni/>
- **Type** — upstream_report
- **Commit** — 399cc01d1bc4542964d91aaa17fb43862a8cf3b3
- **Merge commit** — `null`
- **Status** — open
- **Accessed at** — 2026-10-12
- **Authors**
  - amy-why-3459
