<!-- handbook
{
  "id": "frameworks/torch-npu/torch-npu/sub-skills/graph-and-compile",
  "kind": "procedure",
  "tags": [
    "torch-npu",
    "ascend",
    "pytorch",
    "graph-and-compile"
  ]
}
-->

# Choose capture and compilation paths

> Recorded state `candidate` · empirical validation `not_run` · license `NOASSERTION` · [Source](../../../../../../../skill_library/frameworks/torch-npu/torch-npu/sub-skills/graph-and-compile/SKILL.md) · [Scope and provenance](../../../../../../../skill_library/frameworks/torch-npu/torch-npu/sub-skills/graph-and-compile/metadata.json) · [Parent reading](../../lesson.md)

Choose and debug TorchNPU manual NPUGraph, npugraphs, npugraph_ex, TorchAir, Inductor and FXRT compilation routes with explicit storage and backend gates.

Use for graph replay, `torch.compile`, graph breaks, stale results, compiler
dependency failures or unexpected eager fallback. Read [the graph procedure](references/graphs.md)
and [failure recovery](references/troubleshooting.md).

Inputs: exact stack/revisions, backend name, eager function, input shapes/dtypes/
strides, mutation and aliasing, state/RNG, capture stream and output lifetime.
Output: selected backend contract, eager-versus-compiled/replayed comparison,
capture assumptions and unresolved compiler/device checks.

1. Establish a correct eager NPU result before capture.
2. Select manual NPUGraph, built-in graph backend, TorchAir, Inductor or FXRT
   explicitly; record optional compiler availability.
3. Preserve stable storage and legal stream/capture operations.
4. Compare updated-input replays, then benchmark after warmup and synchronization.
5. Use [the bundled graph case](../../../../../../../skill_library/frameworks/torch-npu/torch-npu/scripts/runtime_smoke.py) with
   `--case graph --run` for a tiny manual replay check, not compiler conformance.

Use [memory](../memory-streams-and-events/lesson.md) for pool/lifetime questions
and [operator development](../operator-development/lesson.md) for missing Meta
or custom-op registrations. TorchAir and CANN internals remain external evidence
boundaries; no backend speedup is established by this source study.

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

- [metadata.json](../../../../../../../skill_library/frameworks/torch-npu/torch-npu/sub-skills/graph-and-compile/metadata.json)
