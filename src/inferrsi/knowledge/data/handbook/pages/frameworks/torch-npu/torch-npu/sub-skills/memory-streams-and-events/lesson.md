<!-- handbook
{
  "id": "frameworks/torch-npu/torch-npu/sub-skills/memory-streams-and-events",
  "kind": "procedure",
  "tags": [
    "torch-npu",
    "ascend",
    "pytorch",
    "memory-streams-and-events"
  ]
}
-->

# Trace memory and stream lifetimes

> Recorded state `candidate` · empirical validation `not_run` · license `NOASSERTION` · [Source](../../../../../../../skill_library/frameworks/torch-npu/torch-npu/sub-skills/memory-streams-and-events/SKILL.md) · [Scope and provenance](../../../../../../../skill_library/frameworks/torch-npu/torch-npu/sub-skills/memory-streams-and-events/metadata.json) · [Parent reading](../../lesson.md)

Reason about TorchNPU device and pinned-host ownership, stream dependencies, events, asynchronous copies, allocator caches and graph interaction.

Use for asynchronous corruption, unexpected memory retention, stream races,
pinned copy lifetime or misleading timings. Read [the ownership procedure](references/lifetimes.md)
and [failure recovery](references/troubleshooting.md).

Inputs: allocation owner, tensor/storage aliases, allocating/using streams,
event edges, host-copy boundaries, allocator configuration and exact build.
Output: ordering diagram, ownership table, synchronized measurements and one
bounded discriminating check.

1. Identify producer, consumer and completion boundaries.
2. Establish stream ordering and allocation lifetime separately.
3. Classify live, active, reserved and host-pinned memory independently.
4. Run [the bundled stream case](../../../../../../../skill_library/frameworks/torch-npu/torch-npu/scripts/runtime_smoke.py) with
   `--case streams --run` on the qualified NPU host.
5. Route capture to [graphs](../graph-and-compile/lesson.md) and communication
   ownership to [HCCL](../distributed-and-hccl/lesson.md).

The existing library owners `torchnpu-device-memory-lifecycle` and
`torchnpu-pinned-host-memory-lifecycle` retain their earlier immutable source
pins. Load them by declared metadata reference for allocator-tuning depth; do
not treat this newer operating graph as an update to their evidence.

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

- [metadata.json](../../../../../../../skill_library/frameworks/torch-npu/torch-npu/sub-skills/memory-streams-and-events/metadata.json)
