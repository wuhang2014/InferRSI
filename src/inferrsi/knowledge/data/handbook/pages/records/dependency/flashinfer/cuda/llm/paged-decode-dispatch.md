<!-- handbook
{
  "id": "flashinfer.cuda.llm.paged_decode_dispatch",
  "kind": "record",
  "aliases": [
    "package:flashinfer.cuda.llm.paged_decode_dispatch"
  ],
  "tags": [
    "attention",
    "paged_kv",
    "cuda_graph",
    "dispatch",
    "dependency_drift"
  ],
  "carry": [
    "unit-when-this-applies",
    "unit-limits-of-this-evidence"
  ]
}
-->

# FlashInfer paged decode: freeze backend selection and graph buffers

> Recorded state `imported` · locally verified `false` · evidence level `guidance` · [Source](../../../../../../../knowledge_packs/dependency/flashinfer/cuda/llm/paged-decode-dispatch.json)

Paged attention separates planning from execution; auto dispatch and CUDA graph buffer ownership are part of the reproducibility boundary.

`dependency` · `flashinfer` · `cuda` · `llm.*`

<a id="unit-when-this-applies"></a>
## When this applies

- **Hardware**
  - NVIDIA CUDA; the inspected auto-cuDNN dispatch specifically distinguishes SM100/SM103 and frontend versions
- **Software**
  - flashinfer-ai/flashinfer at 3637083a3a3d08538cce60937cd876b17779c6f0; later revisions need reinspection
- **Conditions**
  - Paged KV decode with known head dimensions, dtype, page layout and batch shape
  - Caller-owned graph buffers must remain valid across planning and replay

<a id="unit-what-the-source-reports"></a>
## What the source reports

- **Upstream reported.** BatchDecodeWithPagedKVCacheWrapper exposes resolved_backend after planning. Auto selection depends on architecture, kernel availability, shapes and optional cuDNN/CuTe dependencies.
- **Upstream reported.** The inspected cuDNN path accepts a narrower feature set than the whole library; it excludes RoPE, soft-cap and FP8/NVFP4 KV. Captured block tables and backend choice cannot change arbitrarily between re-plans.

<a id="unit-consequences-for-a-downstream-project"></a>
## Consequences for a downstream project

- vLLM: record the resolved attention backend and dependency tuple when comparing upgrades; an unchanged backend=auto argument does not freeze the implementation.
- vLLM-Omni: transfer the dispatch/buffer-ownership checks only to adapters actually calling these APIs; this LLM decode card does not establish diffusion attention support.
- vllm-ascend: the CUDA kernels are not portable; only the explicit-dispatch and lifetime checks are candidate review practices.

<a id="unit-putting-the-idea-to-work"></a>
## Putting the idea to work

- Treat downstream impact as an InferRSI transfer hypothesis, not an upstream compatibility or performance result.

<a id="unit-how-to-check-it"></a>
## How to check it

- Compare numerical outputs with a reference over supported dtype/head/layout/masking combinations and require a defined fallback for unsupported inputs.
- Measure cold planning/JIT, warm run, graph capture and replay separately; vary batch and sequence shapes and test caller-owned buffer reuse.

<a id="unit-limits-of-this-evidence"></a>
## Limits of this evidence

- The library GPU table is not an operator-by-operator support matrix.
- No downstream dependency bump or universal speedup is recommended from this snapshot.
- Point-in-time source extraction, not a historical commit-delta audit. No local accelerator or model-quality reproduction was run.

<a id="unit-sources"></a>
## Sources

- **Url** — <https://github.com/flashinfer-ai/flashinfer/blob/3637083a3a3d08538cce60937cd876b17779c6f0/README.md>
- **Type** — technical_document
- **Commit** — 3637083a3a3d08538cce60937cd876b17779c6f0
- **Accessed at** — 2026-10-15
- **Content sha256** — 472bc506d8a67ca7d8048650b9fc8f17d75f5adbaa016b505b76bbb48a8b4fbc

- **Url** — <https://github.com/flashinfer-ai/flashinfer/blob/3637083a3a3d08538cce60937cd876b17779c6f0/flashinfer/decode.py>
- **Type** — source_code
- **Commit** — 3637083a3a3d08538cce60937cd876b17779c6f0
- **Accessed at** — 2026-10-15
- **Content sha256** — 85411257e706ffdcb4334d2a8d721268fe236145ac855e4b32bef9109a7bf780
