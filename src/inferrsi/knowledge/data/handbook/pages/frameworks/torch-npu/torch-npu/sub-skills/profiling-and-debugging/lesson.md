<!-- handbook
{
  "id": "frameworks/torch-npu/torch-npu/sub-skills/profiling-and-debugging",
  "kind": "procedure",
  "tags": [
    "torch-npu",
    "ascend",
    "pytorch",
    "profiling-and-debugging"
  ]
}
-->

# Profile and debug TorchNPU

> Recorded state `candidate` · empirical validation `not_run` · license `NOASSERTION` · [Source](../../../../../../../skill_library/frameworks/torch-npu/torch-npu/sub-skills/profiling-and-debugging/SKILL.md) · [Scope and provenance](../../../../../../../skill_library/frameworks/torch-npu/torch-npu/sub-skills/profiling-and-debugging/metadata.json) · [Parent reading](../../lesson.md)

Capture bounded TorchNPU CPU/NPU traces, memory timelines and synchronization-aware diagnostics; distinguish collection, parsing, completion and performance claims.

Use for kernel/communication/host gaps, memory traces, async exceptions or stream
sanitizer diagnosis. Read [the profiling procedure](references/profiling.md)
and [failure recovery](references/troubleshooting.md).

Inputs: tiny correct reproduction, stack/backend, selected activities, bounded
schedule, trace output location and question to discriminate. Output: trace
collection/analysis status, relevant events/counters, completion boundary and
one source-grounded hypothesis.

1. Reproduce correctness without profiling.
2. Select CPU/NPU activities and minimal trace options.
3. Advance the schedule with `prof.step()` and verify actual artifacts.
4. For memory timelines include the required shape/memory/stack-or-module options.
5. Use [the bundled profile case](../../../../../../../skill_library/frameworks/torch-npu/torch-npu/scripts/runtime_smoke.py) with
   `--case profile --run --output <NEW_TRACE_DIRECTORY>` on a qualified host.

For async error location use a fresh bounded run with the documented launch
blocking setting, then restore the normal timing mode. Profiling overhead and
microbenchmarks do not establish L4 service performance. Device trace collection
remains `BLOCKED_REQUIRED_BACKEND` without NPU/CANN profiling support.

<a id="unit-when-this-applies"></a>
## When this applies

- **Scope** — Source-grounded TorchNPU operation and diagnosis; qualify the selected installed stack independently.
- **Prerequisites** — Compatible Linux, PyTorch, TorchNPU, CANN, driver and authorized Ascend device access for device execution.
- **Input contract** — Exact stack identities, bounded workload, tensor metadata and intended correctness/measurement boundary.
- **Produced artifact** — A source-supported procedure or diagnostic trace with actual pass/fail/not-run observations.
- **Failure modes** — Confusing registration with device readiness, CPU fallback with NPU execution, or source inspection with runtime proof.
- **Refusal point** — Withhold backend correctness/performance conclusions when required device/runtime evidence is missing.
- **Hardware** — Ascend NPU required for device, stream, graph, precision, profiling and HCCL checks.

<a id="unit-limits-of-this-evidence"></a>
## Limits of this evidence

- Source-derived candidate; installed API and NPU/CANN execution were not validated.
- BLOCKED_REQUIRED_BACKEND: Linux Ascend NPU/CANN stack, multi-rank HCCL and optional compiler runtime checks remain unavailable.
- No model quality, benchmark gain, service/E2E claim or candidate promotion follows from static checks.
- Representative pinned op-plugin inspection does not cover every operator or external CANN kernel implementation.

<a id="unit-source-files"></a>
## Source files

- [metadata.json](../../../../../../../skill_library/frameworks/torch-npu/torch-npu/sub-skills/profiling-and-debugging/metadata.json)
