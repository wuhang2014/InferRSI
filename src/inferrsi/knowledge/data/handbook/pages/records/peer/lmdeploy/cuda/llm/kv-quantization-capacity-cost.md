<!-- handbook
{
  "id": "lmdeploy.cuda.llm.kv_quantization_capacity_cost",
  "kind": "record",
  "aliases": [
    "package:lmdeploy.cuda.llm.kv_quantization_capacity_cost"
  ],
  "tags": [
    "kv_quantization",
    "turboquant",
    "capacity",
    "latency_regression",
    "quality",
    "transfer_hypothesis"
  ],
  "carry": [
    "unit-when-this-applies",
    "unit-limits-of-this-evidence"
  ]
}
-->

# LMDeploy KV quantization: preserve capacity gains and latency counterexamples

> Recorded state `imported` · locally verified `false` · evidence level `upstream_reported` · [Source](../../../../../../../knowledge_packs/peer/lmdeploy/cuda/llm/kv-quantization-capacity-cost.json)

KV compression can increase cache capacity yet reduce throughput; distinguish engine-specific quantizers and validate long-context quality.

`peer` · `lmdeploy` · `cuda` · `llm.*`

<a id="unit-when-this-applies"></a>
## When this applies

- **Hardware**
  - INT4/INT8 source support spans NVIDIA Volta and later; the TurboQuant example is specifically H200
- **Software**
  - InternLM/lmdeploy at 822dddb8b3bc895eaf6cffb45a5514768e7ecb84; later revisions need reinspection
- **Conditions**
  - Record engine, quant_policy, attention architecture, head dimension and quantizer dependencies

<a id="unit-what-the-source-reports"></a>
## What the source reports

- **Upstream reported.** INT4/INT8 uses online per-head/per-token asymmetric quantization. The documented TurboQuant K4V2 path is PyTorch-engine-only, excludes MLA and speculative decoding, and requires power-of-two head dimensions.
- **Upstream reported.** Upstream unverified counterexample: H200, Qwen3-30B-A3B-Base, ShareGPT, concurrency 64, 5000 requests, quant_policy=42 versus 0 reports output throughput 2186.7 to 2027.0 tokens/s and mean E2E latency 5.888 to 6.348 seconds. Compression did not improve latency in this configuration.

<a id="unit-consequences-for-a-downstream-project"></a>
## Consequences for a downstream project

- vLLM and vllm-ascend: candidate capacity experiment under memory pressure; do not transplant LMDeploy quant_policy values into another engine.
- Compare achievable concurrency and quality as well as per-request latency; preserve regressions when ranking candidates.

<a id="unit-putting-the-idea-to-work"></a>
## Putting the idea to work

- Treat downstream impact as an InferRSI transfer hypothesis, not an upstream compatibility or performance result.

<a id="unit-how-to-check-it"></a>
## How to check it

- Measure actual KV bytes including scales/metadata, peak allocation and concurrency under equal total memory.
- Test long-context retrieval and generation quality, then serving throughput/latency with both ample-memory and constrained-memory workloads.

<a id="unit-limits-of-this-evidence"></a>
## Limits of this evidence

- Source quality slogans are not exactness guarantees. INT4/INT8 and TurboQuant are distinct techniques with different engine support.
- The reported table is not accompanied here by raw request samples or frozen validators; its numbers are neither locally reproduced nor a general gain claim.
- Point-in-time source extraction, not a historical commit-delta audit. No local accelerator or model-quality reproduction was run.

<a id="unit-sources"></a>
## Sources

- **Url** — <https://github.com/InternLM/lmdeploy/blob/822dddb8b3bc895eaf6cffb45a5514768e7ecb84/docs/en/quantization/kv_quant.md>
- **Type** — technical_document
- **Commit** — 822dddb8b3bc895eaf6cffb45a5514768e7ecb84
- **Accessed at** — 2026-10-15
- **Content sha256** — 58d41fe148d80b2b1ee4c8e3210a7ab6cf1d7f51943f1cb61690e6b1dde329e3
