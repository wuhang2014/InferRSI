<!-- handbook
{
  "id": "diffusers.cuda.diffusion.group_offload_transfer_overlap",
  "kind": "record",
  "aliases": [
    "package:diffusers.cuda.diffusion.group_offload_transfer_overlap"
  ],
  "tags": [
    "offload",
    "prefetch",
    "cpu_memory",
    "stream",
    "vae",
    "dependency_compatibility"
  ],
  "carry": [
    "unit-when-this-applies",
    "unit-limits-of-this-evidence"
  ]
}
-->

# Diffusers group offload exchanges VRAM for host memory and transfer scheduling

> Recorded state `imported` · locally verified `false` · evidence level `guidance` · [Source](../../../../../../../knowledge_packs/dependency/diffusers/cuda/diffusion/group-offload-transfer-overlap.json)

Group/leaf offload and asynchronous prefetch offer different memory-latency tradeoffs; hook compatibility and host allocation must be evaluated.

`dependency` · `diffusers` · `cuda` · `diffusion.*`

<a id="unit-when-this-applies"></a>
## When this applies

- **Hardware**
  - CUDA GPU with asynchronous transfer streams, sufficient CPU memory and measured host-device bandwidth
- **Software**
  - huggingface/diffusers at efe46a5b177af67c64b3666da8ddddac7ee12163; later revisions need reinspection
- **Conditions**
  - The model supports the relevant group-offload hooks and its forward device casts do not conflict with them

<a id="unit-what-the-source-reports"></a>
## What the source reports

- **Upstream reported.** Group offload moves internal module groups or leaves. CUDA streams can prefetch subsequent work while the current layer executes.
- **Upstream reported.** Pre-pinning can raise host memory substantially; low_cpu_mem_usage trades on-demand pinning for additional execution time. Block-level streaming requires num_blocks_per_group=1 in this documentation.

<a id="unit-consequences-for-a-downstream-project"></a>
## Consequences for a downstream project

- vLLM-Omni: check whether upstream offload hooks are used or replaced before copying configuration; track both host PSS and device peak.
- Keep loading, first real request, denoise and VAE timings separate when estimating overlap benefits.
- vllm-ascend: revalidate transfer/event semantics with its own backend; a CUDA stream recipe is not an NPU result.

<a id="unit-putting-the-idea-to-work"></a>
## Putting the idea to work

- Treat downstream impact as an InferRSI transfer hypothesis, not an upstream compatibility or performance result.

<a id="unit-how-to-check-it"></a>
## How to check it

- Compare resident, group-offload and streamed variants with fixed model/dtype/shape and report preparation, first request and warm requests.
- Exercise VAE tiling, cancellation and repeated requests; retain output parity and allocator/host-memory traces.

<a id="unit-limits-of-this-evidence"></a>
## Limits of this evidence

- The source warns about weight-dependent input device casting and a tiled-VAE warmup requirement; warmup belongs in preparation, not a substituted readiness response.
- Insufficient CPU RAM or transfer bandwidth can erase latency gains.
- Point-in-time source extraction, not a historical commit-delta audit. No local accelerator or model-quality reproduction was run.

<a id="unit-sources"></a>
## Sources

- **Url** — <https://github.com/huggingface/diffusers/blob/efe46a5b177af67c64b3666da8ddddac7ee12163/docs/source/en/optimization/memory.md>
- **Type** — technical_document
- **Commit** — efe46a5b177af67c64b3666da8ddddac7ee12163
- **Accessed at** — 2026-10-15
- **Content sha256** — fb390aac843bb8b53273f9584832b69299cacc7a805d07552598c017e7d1bae6
