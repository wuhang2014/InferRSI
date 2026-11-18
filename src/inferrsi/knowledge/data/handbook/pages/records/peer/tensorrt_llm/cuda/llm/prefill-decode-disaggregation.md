<!-- handbook
{
  "id": "tensorrt_llm.cuda.llm.prefill_decode_disaggregation",
  "kind": "record",
  "aliases": [
    "package:tensorrt_llm.cuda.llm.prefill_decode_disaggregation"
  ],
  "tags": [
    "disaggregation",
    "prefill",
    "decode",
    "kv_transfer",
    "slo",
    "transfer_hypothesis"
  ],
  "carry": [
    "unit-when-this-applies",
    "unit-limits-of-this-evidence"
  ]
}
-->

# TensorRT-LLM disaggregation trades phase interference for KV transfer

> Recorded state `imported` · locally verified `false` · evidence level `guidance` · [Source](../../../../../../../knowledge_packs/peer/tensorrt_llm/cuda/llm/prefill-decode-disaggregation.json)

Separate prefill and decode resources when workload interference dominates the added transfer, queueing and layout-conversion costs.

`peer` · `tensorrt_llm` · `cuda` · `llm.*`

<a id="unit-when-this-applies"></a>
## When this applies

- **Hardware**
  - Separate NVIDIA GPU resources with a qualified KV transport such as RDMA or NVLink
- **Software**
  - NVIDIA/TensorRT-LLM at c9b18eefa731dc59b0091bdfff6d890aa9d1e98e; later revisions need reinspection
- **Conditions**
  - Serving workload has measured prefill/decode interference and compatible KV layouts

<a id="unit-what-the-source-reports"></a>
## What the source reports

- **Upstream reported.** Separate context and generation pools permit different resource and parallelism choices, while adding KV transfer between them.
- **Upstream reported.** The inspected design overlaps transfers with other requests and handles mapping between different parallel layouts; these are performance-critical operations.

<a id="unit-consequences-for-a-downstream-project"></a>
## Consequences for a downstream project

- vLLM: test disaggregated serving against colocated serving using the same total device budget and SLO workload.
- vLLM-Omni: stage disaggregation is a hypothesis, but a diffusion pipeline does not share the same autoregressive prefill/decode cost model.

<a id="unit-putting-the-idea-to-work"></a>
## Putting the idea to work

- Treat downstream impact as an InferRSI transfer hypothesis, not an upstream compatibility or performance result.

<a id="unit-how-to-check-it"></a>
## How to check it

- Freeze input/output-length and arrival distributions; report queue time, TTFT, TPOT, tail latency, goodput and total GPU/network resources.
- Include cache transfer bytes, layout conversion, backpressure, cancellation and failed-worker recovery.

<a id="unit-limits-of-this-evidence"></a>
## Limits of this evidence

- No numeric speedup or cost reduction is transferable from architecture alone.
- Short prompts, weak interconnects or imbalanced pools can make disaggregation slower.
- Point-in-time source extraction, not a historical commit-delta audit. No local accelerator or model-quality reproduction was run.

<a id="unit-sources"></a>
## Sources

- **Url** — <https://github.com/NVIDIA/TensorRT-LLM/blob/c9b18eefa731dc59b0091bdfff6d890aa9d1e98e/docs/source/features/disagg-serving.md>
- **Type** — technical_document
- **Commit** — c9b18eefa731dc59b0091bdfff6d890aa9d1e98e
- **Accessed at** — 2026-10-15
- **Content sha256** — 8b86780c4896ef07c597ec7ab0266fb491030f1d5cdc02adfe2db260973c39d8
