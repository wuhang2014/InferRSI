<!-- handbook
{
  "id": "triton.common.kernel.bandwidth_fusion_resource_limits",
  "kind": "record",
  "aliases": [
    "package:triton.common.kernel.bandwidth_fusion_resource_limits"
  ],
  "tags": [
    "fusion",
    "softmax",
    "bandwidth",
    "register_pressure",
    "numerical_parity"
  ],
  "carry": [
    "unit-when-this-applies",
    "unit-limits-of-this-evidence"
  ]
}
-->

# Triton fusion trades memory traffic for register and shared-memory pressure

> Recorded state `imported` · locally verified `false` · evidence level `guidance` · [Source](../../../../../../../knowledge_packs/dependency/triton/common/kernel/bandwidth-fusion-resource-limits.json)

Fuse a bandwidth-bound reduction when its working set fits on chip; choose launch geometry using the compiled resource footprint.

`dependency` · `triton` · `common` · `kernel.*`

<a id="unit-when-this-applies"></a>
## When this applies

- **Hardware**
  - The tutorial includes CUDA and HIP target-specific occupancy calculations; each device still needs qualification
- **Software**
  - triton-lang/triton at 4eda6cc91e86553a2517d1c764ea2967985553ad; later revisions need reinspection
- **Conditions**
  - Rows fit the kernel resource envelope; the input stride and masked padded width are accounted for

<a id="unit-what-the-source-reports"></a>
## What the source reports

- **Upstream reported.** The fused softmax tutorial avoids intermediate global-memory passes and masks power-of-two padding.
- **Upstream reported.** Its launch calculation uses compiled register/shared-memory usage and distinguishes HIP occupancy. tl.exp is approximate.

<a id="unit-consequences-for-a-downstream-project"></a>
## Consequences for a downstream project

- vLLM and vLLM-Omni: use profiler evidence to nominate elementwise/reduction chains for fusion; retain eager dtype/rounding contracts.
- vllm-ascend: this CUDA/HIP tutorial is design input, not proof that its kernel runs on an NPU backend.

<a id="unit-putting-the-idea-to-work"></a>
## Putting the idea to work

- Treat downstream impact as an InferRSI transfer hypothesis, not an upstream compatibility or performance result.

<a id="unit-how-to-check-it"></a>
## How to check it

- Test irregular widths, row strides and numerical extremes against the original operation sequence.
- Sweep widths and measure traffic, occupancy/spills and latency before checking end-to-end effects.

<a id="unit-limits-of-this-evidence"></a>
## Limits of this evidence

- Tutorial speedups are tied to its reference implementations and shapes; they are not predictions for current torch.compile or a service.
- Fusion can regress when register pressure, padding or shared-memory demand reduces occupancy.
- Point-in-time source extraction, not a historical commit-delta audit. No local accelerator or model-quality reproduction was run.

<a id="unit-sources"></a>
## Sources

- **Url** — <https://github.com/triton-lang/triton/blob/4eda6cc91e86553a2517d1c764ea2967985553ad/python/tutorials/02-fused-softmax.py>
- **Type** — source_code
- **Commit** — 4eda6cc91e86553a2517d1c764ea2967985553ad
- **Accessed at** — 2026-10-15
- **Content sha256** — 4dbf82027df6149efaec19569e5b10b4c7600f53d4041dedc315a86c75b9141e
