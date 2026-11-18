<!-- handbook
{
  "id": "frameworks/torch-npu/torch-npu/sub-skills/training-and-precision",
  "kind": "procedure",
  "tags": [
    "torch-npu",
    "ascend",
    "pytorch",
    "training-and-precision"
  ]
}
-->

# Validate training and precision

> Recorded state `candidate` · empirical validation `not_run` · license `NOASSERTION` · [Source](../../../../../../../skill_library/frameworks/torch-npu/torch-npu/sub-skills/training-and-precision/SKILL.md) · [Scope and provenance](../../../../../../../skill_library/frameworks/torch-npu/torch-npu/sub-skills/training-and-precision/metadata.json) · [Parent reading](../../lesson.md)

Migrate a bounded TorchNPU training step, select autocast and gradient-scaling behavior, compare optimizer/checkpoint state and diagnose precision failures.

Use for a first NPU training step, autocast/GradScaler, gradient clipping,
overflow, fused optimizer migration or numerical mismatch. Read [the precision procedure](references/training.md)
and [failure recovery](references/troubleshooting.md).

Inputs: model/loss/optimizer, input dtype/layout, gradient accumulation, scaler,
distributed mode, expected tolerances and exact stack. Output: one-step
correctness/overflow/state comparison with a named validation scope.

1. Establish FP32 eager forward/backward and optimizer behavior.
2. Introduce autocast and scaling deliberately; check finite gradients and
   skipped steps separately from loss values.
3. Unscale before clipping, and update the scale only at the optimizer boundary.
4. Run [the bundled AMP case](../../../../../../../skill_library/frameworks/torch-npu/torch-npu/scripts/runtime_smoke.py) with
   `--case amp --run` on an NPU; preserve disabled-scaler and overflow observations.
5. Test optimizer/checkpoint changes separately, then add distributed or graph
   execution through their owning routes.

A finite one-step loss is not convergence, numerical-quality, throughput or
service evidence. Custom-op gradients belong to [operator development](../operator-development/lesson.md).

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

- [metadata.json](../../../../../../../skill_library/frameworks/torch-npu/torch-npu/sub-skills/training-and-precision/metadata.json)
