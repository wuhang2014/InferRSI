<!-- handbook
{
  "id": "strata.common.llm.architecture_search_space",
  "kind": "record",
  "aliases": [
    "package:strata.common.llm.architecture_search_space"
  ],
  "tags": [
    "architecture",
    "expert_cache",
    "kv_cache",
    "speculation",
    "search_space"
  ],
  "carry": [
    "unit-when-this-applies",
    "unit-limits-of-this-evidence"
  ]
}
-->

# Strata family contracts and constrained inference search

> Recorded state `imported` · locally verified `false` · evidence level `guidance` · [Source](../../../../../../../repo_packs/strata/knowledge/common/llm/architecture-search-space.json)

Separate model-family geometry, expert residency, KV/state and speculative verification before selecting settings or implementation changes.

`contribution` · `strata` · `common` · `llm.*`

<a id="unit-when-this-applies"></a>
## When this applies

- **Hardware** — `[]`
- **Software**
  - Niko1221/Strata source snapshot 296b59d2f73c8f04a805df29c2fa97655adace78
- **Conditions**
  - Identify the selected model family, numerical contract, hardware topology and workload.
  - Inspect effective startup settings and family-specific implementation before treating a documented option as supported.

<a id="unit-putting-the-idea-to-work"></a>
## Putting the idea to work

- Classify a candidate as an existing setting, algorithm replacement or new capability; model dimensions are kernel contracts, not tuning knobs.
- Budget weights, expert residency, KV/state, MTP, prompt workspace and batch slots together; preserve accepted-prefix state and transfer lifetimes.

<a id="unit-how-to-check-it"></a>
## How to check it

- Check family dispatch, shape/dtype invariants and memory feasibility before running the changed backend.
- Compare operator/state parity, real-model quality and matched service workloads before ranking candidates.

<a id="unit-limits-of-this-evidence"></a>
## Limits of this evidence

- Do not transfer Flash-Next dimensions or backend assumptions to Qwen3.6.
- Approximate expert skipping and numerical changes require a separate quality contract.
- This indexed abstract links to the complete English skill and source evidence; it is imported guidance, not a benchmark result.
- Accelerator execution, real-model quality and service performance remain unverified for this import. Qualify each target revision, model, backend and workload separately.

<a id="unit-sources"></a>
## Sources

- **Url** — <https://github.com/Niko1221/Strata/blob/296b59d2f73c8f04a805df29c2fa97655adace78/include/strata/core/geometry.hpp#L20-L76>
- **Type** — source
- **Commit** — 296b59d2f73c8f04a805df29c2fa97655adace78
- **Accessed at** — 2026-10-14

- **Url** — <https://github.com/Niko1221/Strata/blob/296b59d2f73c8f04a805df29c2fa97655adace78/include/strata/core/expert_cache.hpp#L37-L134>
- **Type** — source
- **Commit** — 296b59d2f73c8f04a805df29c2fa97655adace78
- **Accessed at** — 2026-10-14

- **Url** — <https://github.com/Niko1221/Strata/blob/296b59d2f73c8f04a805df29c2fa97655adace78/include/strata/core/verify.hpp#L1-L21>
- **Type** — source
- **Commit** — 296b59d2f73c8f04a805df29c2fa97655adace78
- **Accessed at** — 2026-10-14

<a id="unit-available-translation"></a>
## Available translation

- **Zh-cn**
  - **Title** — Strata 模型族契约与推理搜索空间
  - **Summary** — 先区分模型族几何约束、专家驻留、KV 状态和投机验证，再选择参数或实现改动。

<a id="unit-companion-material"></a>
## Companion material

- [SKILL.md](../../../../../repositories/strata/sub-skills/design-space/lesson.md)
