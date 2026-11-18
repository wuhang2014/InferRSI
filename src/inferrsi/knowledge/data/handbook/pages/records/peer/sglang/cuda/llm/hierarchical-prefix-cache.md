<!-- handbook
{
  "id": "sglang.cuda.llm.hierarchical_prefix_cache",
  "kind": "record",
  "aliases": [
    "package:sglang.cuda.llm.hierarchical_prefix_cache"
  ],
  "tags": [
    "prefix_cache",
    "kv_cache",
    "hicache",
    "prefetch",
    "storage",
    "transfer_hypothesis"
  ],
  "carry": [
    "unit-when-this-applies",
    "unit-limits-of-this-evidence"
  ]
}
-->

# SGLang HiCache: reuse prefixes only when transfer beats recomputation

> Recorded state `imported` · locally verified `false` · evidence level `guidance` · [Source](../../../../../../../knowledge_packs/peer/sglang/cuda/llm/hierarchical-prefix-cache.json)

Move reusable prefix KV across device, host and storage tiers while accounting for sharing scope, layout conversion and prefetch policy.

`peer` · `sglang` · `cuda` · `llm.*`

<a id="unit-when-this-applies"></a>
## When this applies

- **Hardware**
  - GPU plus CPU memory and optional storage/network backend; CUDA transfer path is the scope of this candidate
- **Software**
  - sgl-project/sglang at f7ad4345b86d147a1c3095a3cebabca9a33ebaa1; later revisions need reinspection
- **Conditions**
  - Repeated prefixes or long contexts with measurable reuse
  - Model/cache identity and distributed-rank agreement must be maintained

<a id="unit-what-the-source-reports"></a>
## What the source reports

- **Upstream reported.** HiCache keeps L1 device and L2 host caches private to an inference instance; only appropriately configured L3 storage enables cross-instance reuse.
- **Upstream reported.** Page-oriented layouts, selective write-through and prefetch termination policies trade I/O overhead against useful cache hits. Multi-rank consensus constrains usable prefix lengths.

<a id="unit-consequences-for-a-downstream-project"></a>
## Consequences for a downstream project

- vLLM: candidate experiment for long-context or repeated-prefix serving; compare transfer cost with recomputation under the actual hit-rate distribution.
- vLLM-Omni: consider only stages with genuinely reusable prefix KV; diffusion residual caching is a different technique.
- vllm-ascend: the hierarchy is a design hypothesis, with NPU I/O and layout behavior requiring separate validation.

<a id="unit-putting-the-idea-to-work"></a>
## Putting the idea to work

- Treat downstream impact as an InferRSI transfer hypothesis, not an upstream compatibility or performance result.

<a id="unit-how-to-check-it"></a>
## How to check it

- Compare cold cache, warm device cache, host hits and storage hits with identical request order; report TTFT, throughput, transfer bytes and hit rates.
- Test cache keys for model/revision/adapter differences, eviction, partial prefetch and rank disagreement.

<a id="unit-limits-of-this-evidence"></a>
## Limits of this evidence

- No SGLang benchmark gain is imported as an InferRSI result.
- Larger private host caches do not create a shared distributed cache; low reuse or slow storage can regress latency.
- Point-in-time source extraction, not a historical commit-delta audit. No local accelerator or model-quality reproduction was run.

<a id="unit-sources"></a>
## Sources

- **Url** — <https://github.com/sgl-project/sglang/blob/f7ad4345b86d147a1c3095a3cebabca9a33ebaa1/docs/docs/advanced_features/hicache_design.mdx>
- **Type** — technical_document
- **Commit** — f7ad4345b86d147a1c3095a3cebabca9a33ebaa1
- **Accessed at** — 2026-10-15
- **Content sha256** — ea9e7896aeeba4f648c3484b382780ce735bba74e0a74dd5403bf7a0438305b5

- **Url** — <https://github.com/sgl-project/sglang/blob/f7ad4345b86d147a1c3095a3cebabca9a33ebaa1/docs/docs/advanced_features/hicache_best_practices.mdx>
- **Type** — technical_document
- **Commit** — f7ad4345b86d147a1c3095a3cebabca9a33ebaa1
- **Accessed at** — 2026-10-15
- **Content sha256** — 1b23cd3668a11a1dce0f8be6104afdc9c8b735d14b86c3c36387f303c2daf31b
