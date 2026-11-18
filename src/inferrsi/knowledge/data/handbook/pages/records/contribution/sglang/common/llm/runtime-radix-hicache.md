<!-- handbook
{
  "id": "sglang.common.llm.runtime_radix_hicache",
  "kind": "record",
  "aliases": [
    "package:sglang.common.llm.runtime_radix_hicache"
  ],
  "tags": [
    "scheduler",
    "radix_cache",
    "hicache",
    "kv_cache",
    "chunked_prefill",
    "speculation"
  ],
  "carry": [
    "unit-when-this-applies",
    "unit-limits-of-this-evidence"
  ]
}
-->

# SGLang scheduler, RadixCache and HiCache state ownership

> Recorded state `imported` · locally verified `false` · evidence level `guidance` · [Source](../../../../../../../repo_packs/sglang/knowledge/common/llm/runtime-radix-hicache.json)

Separate request state, physical KV slots, prefix-cache nodes and pending transfers when tuning chunked prefill, memory or speculation.

`contribution` · `sglang` · `common` · `llm.*`

<a id="unit-when-this-applies"></a>
## When this applies

- **Hardware** — `[]`
- **Software**
  - sgl-project/sglang source snapshot 16176278d0180f1a1a578e53e6eef432577876c2
- **Conditions**
  - Record prompt/output lengths, prefix reuse, arrivals, sampling, cache state and model state type.
  - Identify the selected plain RadixCache or UnifiedRadixCache and its allocator/component contracts.

<a id="unit-putting-the-idea-to-work"></a>
## Putting the idea to work

- Trace admission, forward and finish/abort, then locate queueing, compute or host/storage-transfer delay.
- Inspect declaration and compatibility/resolution hooks; include allocator/refcount cleanup when changing memory behavior.

<a id="unit-how-to-check-it"></a>
## How to check it

- Check hit/miss equivalence, partial prefixes, eviction, finish/abort cleanup and chunk boundaries.
- For speculation verify draft/target compatibility, accepted-token accounting and rejected-state cleanup.

<a id="unit-limits-of-this-evidence"></a>
## Limits of this evidence

- Full-attention assumptions do not automatically apply to SWA or Mamba components.
- Fewer OOMs do not prove request-state correctness or improved service throughput.
- This indexed abstract links to the complete English skill and source evidence; it is imported guidance, not a benchmark result.
- Accelerator execution, real-model quality and service performance remain unverified for this import. Qualify each target revision, model, backend and workload separately.

<a id="unit-sources"></a>
## Sources

- **Url** — <https://github.com/sgl-project/sglang/blob/16176278d0180f1a1a578e53e6eef432577876c2/python/sglang/srt/mem_cache/radix_cache.py#L552-L616>
- **Type** — source
- **Commit** — 16176278d0180f1a1a578e53e6eef432577876c2
- **Accessed at** — 2026-10-14

- **Url** — <https://github.com/sgl-project/sglang/blob/16176278d0180f1a1a578e53e6eef432577876c2/python/sglang/srt/mem_cache/unified_cache/components/README.md#L1-L121>
- **Type** — source
- **Commit** — 16176278d0180f1a1a578e53e6eef432577876c2
- **Accessed at** — 2026-10-14

- **Url** — <https://github.com/sgl-project/sglang/blob/16176278d0180f1a1a578e53e6eef432577876c2/python/sglang/srt/managers/scheduler.py#L3766-L3835>
- **Type** — source
- **Commit** — 16176278d0180f1a1a578e53e6eef432577876c2
- **Accessed at** — 2026-10-14

<a id="unit-available-translation"></a>
## Available translation

- **Zh-cn**
  - **Title** — SGLang 调度、RadixCache 与 HiCache 状态所有权
  - **Summary** — 调优分块预填充、内存或投机解码时，区分请求状态、物理 KV 槽、前缀节点和待完成传输。

<a id="unit-companion-material"></a>
## Companion material

- [SKILL.md](../../../../../repositories/sglang/sub-skills/sglang-runtime-memory/lesson.md)
