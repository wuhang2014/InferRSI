<!-- handbook
{
  "id": "frameworks/torch-npu/torch-npu/sub-skills/privateuse1-and-dispatch",
  "kind": "procedure",
  "tags": [
    "torch-npu",
    "ascend",
    "pytorch",
    "privateuse1-and-dispatch"
  ]
}
-->

# Trace registration and dispatch

> Recorded state `candidate` · empirical validation `not_run` · license `NOASSERTION` · [Source](../../../../../../../skill_library/frameworks/torch-npu/torch-npu/sub-skills/privateuse1-and-dispatch/SKILL.md) · [Scope and provenance](../../../../../../../skill_library/frameworks/torch-npu/torch-npu/sub-skills/privateuse1-and-dispatch/metadata.json) · [Parent reading](../../lesson.md)

Trace TorchNPU initialization, PrivateUse1 registration, lazy device setup, operator dispatch and explicit CPU fallback boundaries.

Use when `torch.npu` is missing, a tensor unexpectedly executes on CPU,
PrivateUse1 registration conflicts, an autograd path fails, or import loads
unexpected compiler state. Read [registration and dispatch](references/dispatch.md)
and [failure recovery](references/troubleshooting.md).

Inputs: plugin/torch revision, fresh-process import order, autoload settings,
operator schema/overload, tensor devices/dtypes and gradient context. Output:
an initialization or dispatch trace with the selected kernel/fallback and the
first failing boundary.

1. Locate failure in core extension, backend registration, patches, lifecycle
   barrier or optional feature setup.
2. Separate renamed PrivateUse1/device methods from actual runtime initialization.
3. For one operator, identify schema, dispatch key, implementation and fallback.
4. Check forward, autograd and Meta paths independently; route missing kernels
   to [operator development](../operator-development/lesson.md).
5. Validate with a fresh interpreter and the actual NPU stack. Record CPU fallback
   rather than describing a CPU result as NPU coverage.

For broad CUDA-to-NPU migration, [the support reference](../../references/support-workflows.md)
describes the opt-in transfer shim and its process-wide effects. Importing this
skill never enables that shim.

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

- [metadata.json](../../../../../../../skill_library/frameworks/torch-npu/torch-npu/sub-skills/privateuse1-and-dispatch/metadata.json)
