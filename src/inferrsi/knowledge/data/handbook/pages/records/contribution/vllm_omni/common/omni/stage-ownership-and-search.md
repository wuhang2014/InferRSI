<!-- handbook
{
  "id": "vllm_omni.common.omni.stage_ownership_and_search",
  "kind": "record",
  "aliases": [
    "package:vllm_omni.common.omni.stage_ownership_and_search"
  ],
  "tags": [
    "pipeline",
    "stage_config",
    "replica_affinity",
    "transport",
    "search_space"
  ],
  "carry": [
    "unit-when-this-applies",
    "unit-limits-of-this-evidence"
  ]
}
-->

# vLLM-Omni stage ownership and constrained execution search

> Recorded state `imported` · locally verified `false` · evidence level `guidance` · [Source](../../../../../../../repo_packs/vllm_omni/knowledge/common/omni/stage-ownership-and-search.json)

Trace pipeline contracts, replica affinity and transfer lifetimes before changing placement, parallelism, batching or execution modes.

`contribution` · `vllm_omni` · `common` · `omni.*`

<a id="unit-when-this-applies"></a>
## When this applies

- **Hardware** — `[]`
- **Software**
  - vllm-project/vllm-omni source snapshot 52194f24fa42e14d1c5e096f4bea4dc7f95cffa1
- **Conditions**
  - Choose one concrete model pipeline and record input/output, state, schedule unit, device and termination per stage.
  - Separate immutable model topology from resolved deployment configuration.

<a id="unit-putting-the-idea-to-work"></a>
## Putting the idea to work

- Classify each candidate as an existing setting, implementation change or research extension with feasibility and correctness constraints.
- Preserve request/segment identity, replica affinity and producer/consumer completion when changing stage placement or buffering.

<a id="unit-how-to-check-it"></a>
## How to check it

- Check config merge/registry and stage completion/abort behavior before exercising actual connectors and ranks.
- Hold workload and model semantics fixed for execution comparisons and validate real output quality before performance claims.

<a id="unit-limits-of-this-evidence"></a>
## Limits of this evidence

- Lower resolution, fewer diffusion steps, quantization and approximate caches require their own quality budgets.
- A schema field or accepted configuration is not proof of runtime support for every model/backend combination.
- This indexed abstract links to the complete English skill and source evidence; it is imported guidance, not a benchmark result.
- Accelerator execution, real-model quality and service performance remain unverified for this import. Qualify each target revision, model, backend and workload separately.

<a id="unit-sources"></a>
## Sources

- **Url** — <https://github.com/vllm-project/vllm-omni/blob/52194f24fa42e14d1c5e096f4bea4dc7f95cffa1/vllm_omni/config/stage_config.py#L229-L399>
- **Type** — source
- **Commit** — 52194f24fa42e14d1c5e096f4bea4dc7f95cffa1
- **Accessed at** — 2026-10-14

- **Url** — <https://github.com/vllm-project/vllm-omni/blob/52194f24fa42e14d1c5e096f4bea4dc7f95cffa1/vllm_omni/engine/stage_pool.py#L465-L509>
- **Type** — source
- **Commit** — 52194f24fa42e14d1c5e096f4bea4dc7f95cffa1
- **Accessed at** — 2026-10-14

- **Url** — <https://github.com/vllm-project/vllm-omni/blob/52194f24fa42e14d1c5e096f4bea4dc7f95cffa1/vllm_omni/distributed/omni_connectors/connectors/base.py#L12-L103>
- **Type** — source
- **Commit** — 52194f24fa42e14d1c5e096f4bea4dc7f95cffa1
- **Accessed at** — 2026-10-14

<a id="unit-available-translation"></a>
## Available translation

- **Zh-cn**
  - **Title** — vLLM-Omni 阶段所有权与受约束执行搜索
  - **Summary** — 调整部署、并行、批处理或执行模式前，先梳理流水线契约、副本亲和性与传输生命周期。

<a id="unit-companion-material"></a>
## Companion material

- [SKILL.md](../../../../../repositories/vllm-omni/sub-skills/omni-architecture/lesson.md)
