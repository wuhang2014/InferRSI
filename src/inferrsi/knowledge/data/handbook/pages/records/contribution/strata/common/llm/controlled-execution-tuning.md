<!-- handbook
{
  "id": "strata.common.llm.controlled_execution_tuning",
  "kind": "record",
  "aliases": [
    "package:strata.common.llm.controlled_execution_tuning"
  ],
  "tags": [
    "tuning",
    "expert_residency",
    "pcie",
    "mtp",
    "prefill",
    "batching"
  ],
  "carry": [
    "unit-when-this-applies",
    "unit-limits-of-this-evidence"
  ]
}
-->

# Strata expert residency, CPU/PCIe balance and bounded tuning

> Recorded state `imported` · locally verified `false` · evidence level `guidance` · [Source](../../../../../../../repo_packs/strata/knowledge/common/llm/controlled-execution-tuning.json)

Tune one measured bottleneck while retaining resolved settings, cache state, memory budgets, quality gates and failed trials.

`contribution` · `strata` · `common` · `llm.*`

<a id="unit-when-this-applies"></a>
## When this applies

- **Hardware** — `[]`
- **Software**
  - Niko1221/Strata source snapshot 296b59d2f73c8f04a805df29c2fa97655adace78
- **Conditions**
  - Start from an already working engine, model artifacts and target hardware.
  - Freeze source/build, model/tokenizer, topology, arrival pattern, output lengths and cache state.

<a id="unit-putting-the-idea-to-work"></a>
## Putting the idea to work

- Measure CPU task time, transfers, expert misses and window cost before changing workers, PCIe share, cache capacity, prefill or speculation.
- Separate cold startup, prompt processing and steady decode; repeat paired trials and retain regressions and invalid candidates.

<a id="unit-how-to-check-it"></a>
## How to check it

- Check resolved slot/group counts, memory headroom and actual active options rather than requested flags alone.
- Validate held-out quality, TTFT, concurrency and long-context memory in addition to decode throughput.

<a id="unit-limits-of-this-evidence"></a>
## Limits of this evidence

- The native calibration routine performs real generation and engine restarts; its decode heuristic is not a quality or service gate.
- Elastic VRAM and batch/MTP interactions are restricted by the actual model/backend path.
- This indexed abstract links to the complete English skill and source evidence; it is imported guidance, not a benchmark result.
- Accelerator execution, real-model quality and service performance remain unverified for this import. Qualify each target revision, model, backend and workload separately.

<a id="unit-sources"></a>
## Sources

- **Url** — <https://github.com/Niko1221/Strata/blob/296b59d2f73c8f04a805df29c2fa97655adace78/tools/calibrate.py>
- **Type** — source
- **Commit** — 296b59d2f73c8f04a805df29c2fa97655adace78
- **Accessed at** — 2026-10-14

- **Url** — <https://github.com/Niko1221/Strata/blob/296b59d2f73c8f04a805df29c2fa97655adace78/tools/strata_bench.py>
- **Type** — source
- **Commit** — 296b59d2f73c8f04a805df29c2fa97655adace78
- **Accessed at** — 2026-10-14

- **Url** — <https://github.com/Niko1221/Strata/blob/296b59d2f73c8f04a805df29c2fa97655adace78/include/strata/program/batch_groups.hpp>
- **Type** — source
- **Commit** — 296b59d2f73c8f04a805df29c2fa97655adace78
- **Accessed at** — 2026-10-14

<a id="unit-available-translation"></a>
## Available translation

- **Zh-cn**
  - **Title** — Strata 专家驻留、CPU/PCIe 平衡与受控调优
  - **Summary** — 围绕实测瓶颈调优，保留生效配置、缓存状态、内存预算、质量门槛和失败记录。

<a id="unit-companion-material"></a>
## Companion material

- [SKILL.md](../../../../../repositories/strata/sub-skills/tune-execution/lesson.md)
