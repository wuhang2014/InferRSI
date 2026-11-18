<!-- handbook
{
  "id": "strata.common.llm.engine_validation_contract",
  "kind": "record",
  "aliases": [
    "package:strata.common.llm.engine_validation_contract"
  ],
  "tags": [
    "validation",
    "native_build",
    "numerical_parity",
    "cancellation",
    "concurrency"
  ],
  "carry": [
    "unit-when-this-applies",
    "unit-limits-of-this-evidence"
  ]
}
-->

# Strata engine validation from native builds to request lifecycle

> Recorded state `imported` · locally verified `false` · evidence level `guidance` · [Source](../../../../../../../repo_packs/strata/knowledge/common/llm/engine-validation-contract.json)

Keep source/CPU checks separate from required accelerator parity, model output, cancellation and matched performance evidence.

`contribution` · `strata` · `common` · `llm.*`

<a id="unit-when-this-applies"></a>
## When this applies

- **Hardware** — `[]`
- **Software**
  - Niko1221/Strata source snapshot 296b59d2f73c8f04a805df29c2fa97655adace78
- **Conditions**
  - Record executable/build hashes, model bytes, backend, tokenizer, resolved config and workload.
  - Use the matching source checkout for native tests and the supplied model for runtime gates.

<a id="unit-putting-the-idea-to-work"></a>
## Putting the idea to work

- Treat setup.py as an application installer/launcher rather than setuptools packaging or a smoke test.
- Freeze correctness and quality gates before comparisons; preserve source/CPU/device/model/service evidence as separate layers.

<a id="unit-how-to-check-it"></a>
## How to check it

- Run applicable no-download CPU checks, build the changed native backend and execute its actual parity targets.
- Test cache restoration, long prompts, concurrent slots, cancellation and the next request, then compare repeated same-day baseline/candidate runs.

<a id="unit-limits-of-this-evidence"></a>
## Limits of this evidence

- A configure/import check or absent fixture cannot certify the engine; unavailable required hardware leaves the campaign INCONCLUSIVE.
- Batch versus solo text differences require the applicable CPU/GPU rounding contract before attributing them to scheduling.
- This indexed abstract links to the complete English skill and source evidence; it is imported guidance, not a benchmark result.
- Accelerator execution, real-model quality and service performance remain unverified for this import. Qualify each target revision, model, backend and workload separately.

<a id="unit-sources"></a>
## Sources

- **Url** — <https://github.com/Niko1221/Strata/blob/296b59d2f73c8f04a805df29c2fa97655adace78/CMakeLists.txt>
- **Type** — source
- **Commit** — 296b59d2f73c8f04a805df29c2fa97655adace78
- **Accessed at** — 2026-10-14

- **Url** — <https://github.com/Niko1221/Strata/blob/296b59d2f73c8f04a805df29c2fa97655adace78/tools/ab_engine.py>
- **Type** — source
- **Commit** — 296b59d2f73c8f04a805df29c2fa97655adace78
- **Accessed at** — 2026-10-14

- **Url** — <https://github.com/Niko1221/Strata/blob/296b59d2f73c8f04a805df29c2fa97655adace78/tools/strata_bench.py>
- **Type** — source
- **Commit** — 296b59d2f73c8f04a805df29c2fa97655adace78
- **Accessed at** — 2026-10-14

<a id="unit-available-translation"></a>
## Available translation

- **Zh-cn**
  - **Title** — Strata 原生构建与请求生命周期验证
  - **Summary** — 区分源码及 CPU 检查、必需的加速器一致性、模型输出、取消清理和配对性能证据。

<a id="unit-companion-material"></a>
## Companion material

- [SKILL.md](../../../../../repositories/strata/sub-skills/validate-engine/lesson.md)
