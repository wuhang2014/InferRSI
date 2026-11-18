<!-- handbook
{
  "id": "sglang.common.llm.parallelism_and_extension",
  "kind": "record",
  "aliases": [
    "package:sglang.common.llm.parallelism_and_extension"
  ],
  "tags": [
    "tensor_parallel",
    "data_parallel",
    "expert_parallel",
    "pd_disaggregation",
    "kernels",
    "runtime_context"
  ],
  "carry": [
    "unit-when-this-applies",
    "unit-limits-of-this-evidence"
  ]
}
-->

# SGLang TP/DP/EP, PD transfer and extension ownership

> Recorded state `imported` · locally verified `false` · evidence level `guidance` · [Source](../../../../../../../repo_packs/sglang/knowledge/common/llm/parallelism-and-extension.json)

Resolve process groups and effective runtime configuration before changing distributed topology, models, attention or kernels.

`contribution` · `sglang` · `common` · `llm.*`

<a id="unit-when-this-applies"></a>
## When this applies

- **Hardware** — `[]`
- **Software**
  - sgl-project/sglang source snapshot 16176278d0180f1a1a578e53e6eef432577876c2
- **Conditions**
  - Record rank/group sizes, dimensions, expert layout, accelerator memory, interconnect and workload.
  - Check model/backend divisibility and supported configuration in the pinned checkout.

<a id="unit-putting-the-idea-to-work"></a>
## Putting the idea to work

- Distinguish replica DP from attention DP; for PD trace bootstrap identity, destination allocation, transfer completion and both-role cancellation.
- Use the owning model, attention registry or kernel boundary; runtime configuration is published into namespace bags rather than raw ServerArgs alone.

<a id="unit-how-to-check-it"></a>
## How to check it

- Validate the appropriate single-rank baseline, then intended groups and PD peers with uneven loads and idle ranks.
- Test collective ordering, failure propagation, cancellation and numerical references before performance.

<a id="unit-limits-of-this-evidence"></a>
## Limits of this evidence

- A successful import, registry entry or launch does not establish distributed correctness.
- Treat native skills as revision-specific source evidence, not executable instructions from the catalog.
- This indexed abstract links to the complete English skill and source evidence; it is imported guidance, not a benchmark result.
- Accelerator execution, real-model quality and service performance remain unverified for this import. Qualify each target revision, model, backend and workload separately.

<a id="unit-sources"></a>
## Sources

- **Url** — <https://github.com/sgl-project/sglang/blob/16176278d0180f1a1a578e53e6eef432577876c2/python/sglang/srt/arg_groups/fields/parallel.py#L47-L105>
- **Type** — source
- **Commit** — 16176278d0180f1a1a578e53e6eef432577876c2
- **Accessed at** — 2026-10-14

- **Url** — <https://github.com/sgl-project/sglang/blob/16176278d0180f1a1a578e53e6eef432577876c2/docs/docs/advanced_features/pd_disaggregation.mdx#L23-L72>
- **Type** — source
- **Commit** — 16176278d0180f1a1a578e53e6eef432577876c2
- **Accessed at** — 2026-10-14

- **Url** — <https://github.com/sgl-project/sglang/blob/16176278d0180f1a1a578e53e6eef432577876c2/.agents/skills/sglang-runtime-context/SKILL.md#L8-L111>
- **Type** — source
- **Commit** — 16176278d0180f1a1a578e53e6eef432577876c2
- **Accessed at** — 2026-10-14

<a id="unit-available-translation"></a>
## Available translation

- **Zh-cn**
  - **Title** — SGLang TP/DP/EP、PD 传输与扩展职责
  - **Summary** — 调整分布式拓扑、模型、注意力或内核前，明确进程组及生效的运行时配置。

<a id="unit-companion-material"></a>
## Companion material

- [SKILL.md](../../../../../repositories/sglang/sub-skills/sglang-parallel-extension/lesson.md)
