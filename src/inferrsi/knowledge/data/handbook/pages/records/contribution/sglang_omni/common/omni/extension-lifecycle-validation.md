<!-- handbook
{
  "id": "sglang_omni.common.omni.extension_lifecycle_validation",
  "kind": "record",
  "aliases": [
    "package:sglang_omni.common.omni.extension_lifecycle_validation"
  ],
  "tags": [
    "extension",
    "model_integration",
    "prepared_request",
    "cancellation",
    "eos",
    "validation"
  ],
  "carry": [
    "unit-when-this-applies",
    "unit-limits-of-this-evidence"
  ]
}
-->

# SGLang-Omni extension ownership and lifecycle validation

> Recorded state `imported` · locally verified `false` · evidence level `guidance` · [Source](../../../../../../../repo_packs/sglang_omni/knowledge/common/omni/extension-lifecycle-validation.json)

Place model, request-builder, scheduler, runner and communication changes at their actual owners and test completion plus abort/streaming failures.

`contribution` · `sglang_omni` · `common` · `omni.*`

<a id="unit-when-this-applies"></a>
## When this applies

- **Hardware** — `[]`
- **Software**
  - sgl-project/sglang-omni source snapshot 2cfb3b67becb437b70751defe37e63d3af4eedb0
- **Conditions**
  - Fix architecture, checkpoint, endpoint and input/output behavior before selecting a similar pipeline.
  - Choose the reference pipeline by scheduling and state requirements rather than modality alone.

<a id="unit-putting-the-idea-to-work"></a>
## Putting the idea to work

- Keep framework contracts model agnostic and use existing preprocessing/state/vocoder helpers only when their semantics match.
- Preserve preparation/inflight/aborted ownership; splitting processes may require moving local shared state to a supported payload boundary.

<a id="unit-how-to-check-it"></a>
## How to check it

- Test invalid input, abort during preparation, late chunks, EOS/flush, repeated requests and resource cleanup.
- On required hardware compare streaming/non-streaming completion, usage, finish reasons, quality and latency at baseline and concurrency.

<a id="unit-limits-of-this-evidence"></a>
## Limits of this evidence

- Mocked or CPU lifecycle tests do not validate the real model, accelerator or media quality.
- A factory or registry import failure should be diagnosed at its consumer rather than hidden or silently ignored.
- This indexed abstract links to the complete English skill and source evidence; it is imported guidance, not a benchmark result.
- Accelerator execution, real-model quality and service performance remain unverified for this import. Qualify each target revision, model, backend and workload separately.

<a id="unit-sources"></a>
## Sources

- **Url** — <https://github.com/sgl-project/sglang-omni/blob/2cfb3b67becb437b70751defe37e63d3af4eedb0/docs/developer_reference/tts_model_integration.md>
- **Type** — source
- **Commit** — 2cfb3b67becb437b70751defe37e63d3af4eedb0
- **Accessed at** — 2026-10-14

- **Url** — <https://github.com/sgl-project/sglang-omni/blob/2cfb3b67becb437b70751defe37e63d3af4eedb0/sglang_omni/scheduling/prepared_request_queue.py>
- **Type** — source
- **Commit** — 2cfb3b67becb437b70751defe37e63d3af4eedb0
- **Accessed at** — 2026-10-14

- **Url** — <https://github.com/sgl-project/sglang-omni/blob/2cfb3b67becb437b70751defe37e63d3af4eedb0/tests/unit_test/scheduling/test_prepared_request_queue.py>
- **Type** — source
- **Commit** — 2cfb3b67becb437b70751defe37e63d3af4eedb0
- **Accessed at** — 2026-10-14

<a id="unit-available-translation"></a>
## Available translation

- **Zh-cn**
  - **Title** — SGLang-Omni 扩展职责与生命周期验证
  - **Summary** — 将模型、请求构建、调度、执行和通信改动放在实际职责边界，并验证完成、取消和流式失败。

<a id="unit-companion-material"></a>
## Companion material

- [SKILL.md](../../../../../repositories/sglang-omni/sub-skills/sglang-omni-extension/lesson.md)
