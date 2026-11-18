<!-- handbook
{
  "id": "pytorch.cuda.compiler.cudagraph_shapes_and_lifetimes",
  "kind": "record",
  "aliases": [
    "package:pytorch.cuda.compiler.cudagraph_shapes_and_lifetimes"
  ],
  "tags": [
    "torch_compile",
    "inductor",
    "cuda_graph",
    "recompilation",
    "tensor_lifetime"
  ],
  "carry": [
    "unit-when-this-applies",
    "unit-limits-of-this-evidence"
  ]
}
-->

# Inductor CUDA graphs: distinguish compile guards, capture shapes and tensor lifetime

> Recorded state `imported` · locally verified `false` · evidence level `guidance` · [Source](../../../../../../../knowledge_packs/dependency/pytorch/cuda/compiler/cudagraph-shapes-and-lifetimes.json)

CUDA graph replay can reduce host launch overhead, but shape specialization, pointer stability and output lifetime remain independent constraints.

`dependency` · `pytorch` · `cuda` · `compiler.*`

<a id="unit-when-this-applies"></a>
## When this applies

- **Hardware**
  - CUDA devices supported by the pinned PyTorch/compiler stack
- **Software**
  - pytorch/pytorch at f15b476814ebc5eade36fb40512e379ebf79dd60; later revisions need reinspection
- **Conditions**
  - A torch.compile/Inductor path with launch overhead worth measuring
  - Representative shape distribution and input/output mutation behavior are known

<a id="unit-what-the-source-reports"></a>
## What the source reports

- **Upstream reported.** CUDA graphs replay fixed kernel arguments and addresses. CUDAGraph Trees manage shared pools subject to tensor-liveness and invocation constraints; eager-input mutation can cause capture to be skipped.
- **Upstream reported.** Shape or Python scalar guards can trigger recompilation. TORCH_LOGS=recompiles exposes causes; dynamic compilation and CUDA graph recording are not the same mechanism.

<a id="unit-consequences-for-a-downstream-project"></a>
## Consequences for a downstream project

- vLLM and vLLM-Omni: record compile/recompile/capture events separately from steady-state latency and include diverse request shapes in the evaluation.
- vllm-ascend: compiler diagnosis may transfer conceptually; CUDA graph memory and capture guarantees do not establish torch_npu behavior.

<a id="unit-putting-the-idea-to-work"></a>
## Putting the idea to work

- Treat downstream impact as an InferRSI transfer hypothesis, not an upstream compatibility or performance result.

<a id="unit-how-to-check-it"></a>
## How to check it

- Freeze a workload shape histogram and compare eager with compile-only and graph replay under identical inputs.
- Retain outputs across subsequent calls, exercise input mutation, and measure cold cost, graph-pool memory and recompilation counts.

<a id="unit-limits-of-this-evidence"></a>
## Limits of this evidence

- A single warm fixed-shape run cannot establish service improvement or dynamic-shape stability.
- Changing graph/compiler knobs may change memory use; no global mode is declared optimal.
- Point-in-time source extraction, not a historical commit-delta audit. No local accelerator or model-quality reproduction was run.

<a id="unit-sources"></a>
## Sources

- **Url** — <https://github.com/pytorch/pytorch/blob/f15b476814ebc5eade36fb40512e379ebf79dd60/docs/source/user_guide/torch_compiler/torch.compiler_cudagraph_trees.md>
- **Type** — technical_document
- **Commit** — f15b476814ebc5eade36fb40512e379ebf79dd60
- **Accessed at** — 2026-10-15
- **Content sha256** — 0dbfcef13ad6baea52c6e989eaf6561440c02a26a6ef667da850439d3a88c6a5

- **Url** — <https://github.com/pytorch/pytorch/blob/f15b476814ebc5eade36fb40512e379ebf79dd60/docs/source/user_guide/torch_compiler/compile/programming_model.recompilation.md>
- **Type** — technical_document
- **Commit** — f15b476814ebc5eade36fb40512e379ebf79dd60
- **Accessed at** — 2026-10-15
- **Content sha256** — 0240bbc4fc9ead047c5039d4bcab93e201c65bd7768c8995e09ee3eb654eaf59
