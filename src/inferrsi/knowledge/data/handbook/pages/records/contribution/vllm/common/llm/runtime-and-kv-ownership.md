<!-- handbook
{
  "id": "vllm.common.llm.runtime_and_kv_ownership",
  "kind": "record",
  "aliases": [
    "package:vllm.common.llm.runtime_and_kv_ownership"
  ],
  "tags": [
    "v1",
    "scheduler",
    "kv_cache",
    "prefix_cache",
    "speculation",
    "architecture"
  ],
  "carry": [
    "unit-when-this-applies",
    "unit-limits-of-this-evidence"
  ]
}
-->

# vLLM V1 scheduling, token budgets and KV ownership

> Recorded state `imported` · locally verified `false` · evidence level `guidance` · [Source](../../../../../../../repo_packs/vllm/knowledge/common/llm/runtime-and-kv-ownership.json)

Trace frontend, engine core, scheduler, runner and completion to identify the binding resource and preserve token/KV lifetime invariants.

`contribution` · `vllm` · `common` · `llm.*`

<a id="unit-when-this-applies"></a>
## When this applies

- **Hardware** — `[]`
- **Software**
  - vllm-project/vllm source snapshot 2521446ac8c92937b5a32b7dc2a84ef7fa8e99c5
- **Conditions**
  - Pin the target vLLM revision, effective serving configuration and request workload.
  - Identify scheduled-token budget, runner input capacity, admitted sequences, KV blocks and encoder/communication demand separately.

<a id="unit-putting-the-idea-to-work"></a>
## Putting the idea to work

- Trace one request and an abort/overlap path before selecting the smallest responsible owner.
- Include draft inputs in runner capacity and retain KV blocks until transfer/consumers complete; distinguish settings from experimental extension hooks.

<a id="unit-how-to-check-it"></a>
## How to check it

- Exercise context limits, preemption with in-flight output, cache hits/misses and pressure/eviction.
- Confirm effective serving defaults from resolution and match source assertions to the intended configuration.

<a id="unit-limits-of-this-evidence"></a>
## Limits of this evidence

- A custom scheduler or registered backend is not a stable compatibility or performance guarantee.
- Dataclass test defaults do not establish resolved serving defaults.
- This indexed abstract links to the complete English skill and source evidence; it is imported guidance, not a benchmark result.
- Accelerator execution, real-model quality and service performance remain unverified for this import. Qualify each target revision, model, backend and workload separately.

<a id="unit-sources"></a>
## Sources

- **Url** — <https://github.com/vllm-project/vllm/blob/2521446ac8c92937b5a32b7dc2a84ef7fa8e99c5/vllm/v1/core/sched/scheduler.py#L1403-L1415>
- **Type** — source
- **Commit** — 2521446ac8c92937b5a32b7dc2a84ef7fa8e99c5
- **Accessed at** — 2026-10-14

- **Url** — <https://github.com/vllm-project/vllm/blob/2521446ac8c92937b5a32b7dc2a84ef7fa8e99c5/vllm/v1/core/block_pool.py#L666-L795>
- **Type** — source
- **Commit** — 2521446ac8c92937b5a32b7dc2a84ef7fa8e99c5
- **Accessed at** — 2026-10-14

- **Url** — <https://github.com/vllm-project/vllm/blob/2521446ac8c92937b5a32b7dc2a84ef7fa8e99c5/vllm/config/scheduler.py#L238-L253>
- **Type** — source
- **Commit** — 2521446ac8c92937b5a32b7dc2a84ef7fa8e99c5
- **Accessed at** — 2026-10-14

<a id="unit-available-translation"></a>
## Available translation

- **Zh-cn**
  - **Title** — vLLM V1 调度、令牌预算与 KV 所有权
  - **Summary** — 沿前端、引擎核心、调度器、执行器和完成路径定位瓶颈，保持令牌预算及 KV 生命周期约束。

<a id="unit-companion-material"></a>
## Companion material

- [SKILL.md](../../../../../repositories/vllm/sub-skills/architecture-search-space/lesson.md)
