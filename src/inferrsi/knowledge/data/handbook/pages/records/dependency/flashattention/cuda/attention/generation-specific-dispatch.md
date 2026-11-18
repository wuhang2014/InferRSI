<!-- handbook
{
  "id": "flashattention.cuda.attention.generation_specific_dispatch",
  "kind": "record",
  "aliases": [
    "package:flashattention.cuda.attention.generation_specific_dispatch"
  ],
  "tags": [
    "attention",
    "flashattention",
    "hopper",
    "blackwell",
    "api_compatibility"
  ],
  "carry": [
    "unit-when-this-applies",
    "unit-limits-of-this-evidence"
  ]
}
-->

# FlashAttention generations have distinct hardware and API contracts

> Recorded state `imported` · locally verified `false` · evidence level `guidance` · [Source](../../../../../../../knowledge_packs/dependency/flashattention/cuda/attention/generation-specific-dispatch.json)

Select an attention generation using its actual GPU, dtype and interface requirements; package names and installation paths are not interchangeable.

`dependency` · `flashattention` · `cuda` · `attention.*`

<a id="unit-when-this-applies"></a>
## When this applies

- **Hardware**
  - FA2 CUDA: Ampere/Ada/Hopper; FA3: H100/H800; FA4 CuTeDSL targets Hopper/Blackwell in the inspected README
- **Software**
  - Dao-AILab/flash-attention at 1fc0221183e799363001394a12dd9e78e15f5dda; later revisions need reinspection
- **Conditions**
  - Qualify exact head dimensions, masks, variable lengths and dtypes on the selected implementation

<a id="unit-what-the-source-reports"></a>
## What the source reports

- **Upstream reported.** FA3 documents FP16/BF16 forward/backward and FP8 forward, with CUDA >=12.3 and an H100/H800 requirement.
- **Upstream reported.** FA3 is installed from hopper and imported through flash_attn_3; FA4 uses flash-attn-4 and flash_attn.cute. The source keeps generation-specific installation and capability sections.

<a id="unit-consequences-for-a-downstream-project"></a>
## Consequences for a downstream project

- vLLM and vLLM-Omni: audit optional imports and dispatch during dependency upgrades, especially where Hopper and Blackwell share a configuration.
- vllm-ascend: use a separately qualified NPU implementation; this CUDA card supplies no compatible kernel.

<a id="unit-putting-the-idea-to-work"></a>
## Putting the idea to work

- Treat downstream impact as an InferRSI transfer hypothesis, not an upstream compatibility or performance result.

<a id="unit-how-to-check-it"></a>
## How to check it

- Test supported and unsupported dtype/head-size/mask combinations against the same reference before benchmarking prefill or diffusion attention.
- Measure kernel and full pipeline latency independently; include compilation/import cost and record the exact selected generation.

<a id="unit-limits-of-this-evidence"></a>
## Limits of this evidence

- Different algorithms and FP8 can change numerical error; mathematical attention equivalence is not bitwise parity.
- ROCm has separate implementation requirements in the source and is outside this CUDA card.
- Point-in-time source extraction, not a historical commit-delta audit. No local accelerator or model-quality reproduction was run.

<a id="unit-sources"></a>
## Sources

- **Url** — <https://github.com/Dao-AILab/flash-attention/blob/1fc0221183e799363001394a12dd9e78e15f5dda/README.md>
- **Type** — technical_document
- **Commit** — 1fc0221183e799363001394a12dd9e78e15f5dda
- **Accessed at** — 2026-10-15
- **Content sha256** — 0dbaba56da1c8372d460956e2609bfb89acf8f3aadd65d132b1697d221069619
