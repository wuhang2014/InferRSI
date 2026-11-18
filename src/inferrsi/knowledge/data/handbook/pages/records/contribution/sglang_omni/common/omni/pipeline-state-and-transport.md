<!-- handbook
{
  "id": "sglang_omni.common.omni.pipeline_state_and_transport",
  "kind": "record",
  "aliases": [
    "package:sglang_omni.common.omni.pipeline_state_and_transport"
  ],
  "tags": [
    "pipeline",
    "dag",
    "scheduler",
    "replicas",
    "streaming",
    "transport"
  ],
  "carry": [
    "unit-when-this-applies",
    "unit-limits-of-this-evidence"
  ]
}
-->

# SGLang-Omni stage DAG, process replicas and transport lifetime

> Recorded state `imported` · locally verified `false` · evidence level `guidance` · [Source](../../../../../../../repo_packs/sglang_omni/knowledge/common/omni/pipeline-state-and-transport.json)

Map normal, fan-in, streaming and terminal edges separately while preserving request identity, abort state and sender-buffer ownership.

`contribution` · `sglang_omni` · `common` · `omni.*`

<a id="unit-when-this-applies"></a>
## When this applies

- **Hardware** — `[]`
- **Software**
  - sgl-project/sglang-omni source snapshot 2cfb3b67becb437b70751defe37e63d3af4eedb0
- **Conditions**
  - Resolve the exact PipelineConfig, model variant, process placement and device topology.
  - Annotate scheduler, process replica, TP ranks, tensor device and state owner per stage.

<a id="unit-putting-the-idea-to-work"></a>
## Putting the idea to work

- Trace admission through terminal merge and cancellation before changing placement or buffering; a process replica copies its stages and is not TP.
- Keep shared local objects read-only and preserve the appropriate CUDA IPC or relay completion lifetime; only active fan-in sources should block completion.

<a id="unit-how-to-check-it"></a>
## How to check it

- Test ordered chunks before EOS, aborted preparation/late outputs, fan-in completion and repeated cleanup.
- Validate local versus cross-process/native transport behavior on the actual placement and hardware.

<a id="unit-limits-of-this-evidence"></a>
## Limits of this evidence

- This revision has no generic public transport selector and no supported OmniScheduler.event_loop_overlap toggle.
- Stage-list order need not equal execution order; transport implementation files do not imply selectable production support.
- This indexed abstract links to the complete English skill and source evidence; it is imported guidance, not a benchmark result.
- Accelerator execution, real-model quality and service performance remain unverified for this import. Qualify each target revision, model, backend and workload separately.

<a id="unit-sources"></a>
## Sources

- **Url** — <https://github.com/sgl-project/sglang-omni/blob/2cfb3b67becb437b70751defe37e63d3af4eedb0/sglang_omni/config/schema.py>
- **Type** — source
- **Commit** — 2cfb3b67becb437b70751defe37e63d3af4eedb0
- **Accessed at** — 2026-10-14

- **Url** — <https://github.com/sgl-project/sglang-omni/blob/2cfb3b67becb437b70751defe37e63d3af4eedb0/sglang_omni/comm/router.py>
- **Type** — source
- **Commit** — 2cfb3b67becb437b70751defe37e63d3af4eedb0
- **Accessed at** — 2026-10-14

- **Url** — <https://github.com/sgl-project/sglang-omni/blob/2cfb3b67becb437b70751defe37e63d3af4eedb0/sglang_omni/scheduling/omni_scheduler.py>
- **Type** — source
- **Commit** — 2cfb3b67becb437b70751defe37e63d3af4eedb0
- **Accessed at** — 2026-10-14

<a id="unit-available-translation"></a>
## Available translation

- **Zh-cn**
  - **Title** — SGLang-Omni 阶段 DAG、进程副本与传输生命周期
  - **Summary** — 分别梳理普通、汇聚、流式和终止边，保持请求身份、取消状态与发送缓冲区所有权。

<a id="unit-companion-material"></a>
## Companion material

- [SKILL.md](../../../../../repositories/sglang-omni/sub-skills/sglang-omni-architecture/lesson.md)
