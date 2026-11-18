<!-- handbook
{
  "id": "vllm_omni.cuda.diffusion.minimax_h3_qk_norm_rope",
  "kind": "record",
  "aliases": [
    "package:vllm_omni.cuda.diffusion.minimax_h3_qk_norm_rope"
  ],
  "tags": [
    "minimax_h3",
    "operator_fusion",
    "rmsnorm",
    "rope",
    "packed_tokens"
  ],
  "carry": [
    "unit-when-this-applies",
    "unit-limits-of-this-evidence"
  ]
}
-->

# MiniMax-H3 guarded Q/K RMSNorm and packed RoPE fusion

> Recorded state `imported` · locally verified `false` · evidence level `upstream_reported` · [Source](../../../../../../../repo_packs/vllm_omni/knowledge/cuda/diffusion/minimax-h3-qk-norm-rope.json)

A merged CUDA fusion avoids normalized-Q/K and rotary intermediates for a specific packed BF16 geometry; reported denoise benefit is small and limited to a B300 workload.

`contribution` · `vllm_omni` · `cuda` · `diffusion.video_generation`

<a id="unit-when-this-applies"></a>
## When this applies

- **Hardware**
  - 4× NVIDIA B300 SXM6
- **Software**
  - Source revision 0d0d42fe7b4a07581cd45ac67bbe1a2f6194fcdd; merged as 596c16a550aa134faf7f3dcfa0f8adf513ccd9ce
  - CUDA/Triton BF16 fast path; head_dim=128, rotary_dim=96; TP1, Ulysses4, Ring1, TRTLLM_ATTN
- **Models**
  - MiniMax-H3
- **Conditions**
  - Packed [tokens, heads, head_dim] with compatible non-interleaved [cos|sin] frequencies
  - 1344×768, 243 frames, 50 configured steps, seed 0
  - One warmup followed by one measured request per revision

<a id="unit-what-the-source-reports"></a>
## What the source reports

- **Upstream reported.** Steady denoise latency fell from 109687 ms to 106205 ms, a reported 3.18% reduction. This is denoise timing, not client E2E or a statistical performance guarantee. Reported on Source accessed 2026-10-09.
- **Upstream reported.** Three CUDA unit cases tested sequence lengths 1, 257 and 1024. Author comment reports max absolute operator error 0.0625, mean absolute error 0.00072–0.00077; qualitative near-identical E2E video is reported without objective media metrics.
- **Source inspected.** The patch dispatches fusion only with HAS_TRITON, CUDA platform/tensors, BF16 and supported geometry; other valid inputs use the eager reference. It preserves a BF16 normalization materialization before RoPE but still tests tolerance rather than byte identity.

<a id="unit-putting-the-idea-to-work"></a>
## Putting the idea to work

- Treat the optimization as intended math-preserving with measured numerical tolerance, not universal bit-exactness.
- Verify selected geometry, RoPE convention and actual fast-path execution before attributing a gain.
- Reuse the existing guarded shared operator rather than copying a CUDA kernel into a platform-neutral model.

<a id="unit-how-to-check-it"></a>
## How to check it

- Run the target revision's tests/diffusion/layers/test_fused_qk_norm_rope.py with its registered GPU test markers.
- Compare native and fused operator/block/trajectory outputs including empty, ragged and strided Q/K cases.
- Run at least three unprofiled warm A/B requests on the target H200/B200 or other GPU; record client E2E, denoise, memory and same-seed video/audio metrics.
- Exercise unsupported dtype/geometry/platform fallbacks separately.

<a id="unit-limits-of-this-evidence"></a>
## Limits of this evidence

- The reported benchmark is B300, not H200/B200, ROCm or Ascend evidence.
- Only one measured request per arm was reported.
- No objective full-model quality metric appears in the reviewed report; imported status does not mean locally verified.

<a id="unit-sources"></a>
## Sources

- **Url** — <https://github.com/vllm-project/vllm-omni/>
- **Type** — upstream_report
- **Commit** — 0d0d42fe7b4a07581cd45ac67bbe1a2f6194fcdd
- **Merge commit** — 596c16a550aa134faf7f3dcfa0f8adf513ccd9ce
- **Status** — merged
- **Accessed at** — 2026-10-09
