<!-- handbook
{
  "id": "transformers.common.llm.kv_cache_strategy_contracts",
  "kind": "record",
  "aliases": [
    "package:transformers.common.llm.kv_cache_strategy_contracts"
  ],
  "tags": [
    "kv_cache",
    "static_cache",
    "quantization",
    "offload",
    "torch_compile",
    "api_compatibility"
  ],
  "carry": [
    "unit-when-this-applies",
    "unit-limits-of-this-evidence"
  ]
}
-->

# Transformers cache strategies trade compilation, capacity and latency

> Recorded state `imported` · locally verified `false` · evidence level `guidance` · [Source](../../../../../../../knowledge_packs/dependency/transformers/common/llm/kv-cache-strategy-contracts.json)

Dynamic, static, offloaded and quantized KV caches have different contracts; select by workload and API support rather than a universal ranking.

`dependency` · `transformers` · `common` · `llm.*`

<a id="unit-when-this-applies"></a>
## When this applies

- **Hardware**
  - Device and quantization-backend support must be checked for the chosen model; this is API guidance
- **Software**
  - huggingface/transformers at 2126f65b0ab267e113e78a002447fc7094de83d5; later revisions need reinspection
- **Conditions**
  - Autoregressive generation with known length distribution, attention type and memory budget

<a id="unit-what-the-source-reports"></a>
## What the source reports

- **Upstream reported.** StaticCache reserves a maximum size and supports compilation, at the cost of reserved capacity and work on masked positions for shorter sequences.
- **Upstream reported.** The inspected table distinguishes sliding-layer, offloading and torch.compile support. Quantized cache can hurt latency on short contexts with sufficient GPU memory; offload adds transfer work.

<a id="unit-consequences-for-a-downstream-project"></a>
## Consequences for a downstream project

- vLLM and vLLM-Omni: audit model/cache adapters when Transformers changes; its generate cache_implementation flags do not configure vLLM paged KV managers.
- vllm-ascend: test supported cache backends independently and retain model-specific sliding/chunked-attention behavior.

<a id="unit-putting-the-idea-to-work"></a>
## Putting the idea to work

- Treat downstream impact as an InferRSI transfer hypothesis, not an upstream compatibility or performance result.

<a id="unit-how-to-check-it"></a>
## How to check it

- Test mixed prompt lengths, prefix reuse and sliding/chunked layers with separate per-request cache state.
- Measure memory, TTFT and decode latency along with long-context output quality and compile behavior.

<a id="unit-limits-of-this-evidence"></a>
## Limits of this evidence

- Memory reduction alone is not throughput evidence.
- This source documents Transformers interfaces; downstream serving-cache compatibility remains an unverified transfer hypothesis.
- Point-in-time source extraction, not a historical commit-delta audit. No local accelerator or model-quality reproduction was run.

<a id="unit-sources"></a>
## Sources

- **Url** — <https://github.com/huggingface/transformers/blob/2126f65b0ab267e113e78a002447fc7094de83d5/docs/source/en/kv_cache.md>
- **Type** — technical_document
- **Commit** — 2126f65b0ab267e113e78a002447fc7094de83d5
- **Accessed at** — 2026-10-15
- **Content sha256** — 70b4f34a7a10862ac48a697f998f65ecf446f423ab9adbd9d23137a259ba7dd0
