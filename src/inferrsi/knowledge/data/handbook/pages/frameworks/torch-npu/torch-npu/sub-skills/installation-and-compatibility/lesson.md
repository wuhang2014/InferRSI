<!-- handbook
{
  "id": "frameworks/torch-npu/torch-npu/sub-skills/installation-and-compatibility",
  "kind": "procedure",
  "tags": [
    "torch-npu",
    "ascend",
    "pytorch",
    "installation-and-compatibility"
  ]
}
-->

# Install and qualify TorchNPU

> Recorded state `candidate` · empirical validation `not_run` · license `NOASSERTION` · [Source](../../../../../../../skill_library/frameworks/torch-npu/torch-npu/sub-skills/installation-and-compatibility/SKILL.md) · [Scope and provenance](../../../../../../../skill_library/frameworks/torch-npu/torch-npu/sub-skills/installation-and-compatibility/metadata.json) · [Parent reading](../../lesson.md)

Select a compatible TorchNPU, PyTorch, Python, CANN and driver stack; distinguish released wheels from source builds and diagnose import failures.

Use for a new Ascend environment, version mismatch, wheel/source build decision,
or missing CANN library. Start with [the stack procedure](references/stack.md).
Use [failure recovery](references/troubleshooting.md) before changing packages.

Inputs: hardware family, Linux architecture, driver/firmware/CANN versions,
Python ABI, exact torch/torch-npu builds, binary versus source intent, and access
to the device. Output: one explicit compatible stack proposal, installation
commands and separate import/device observations.

1. Separate the released package matrix from the source branch's build lines.
2. Establish driver, CANN and environment setup before package import.
3. Install matching PyTorch and TorchNPU package lines in a private environment.
4. Run [the bundled probe](../../../../../../../skill_library/frameworks/torch-npu/torch-npu/scripts/inspect_environment.py) without device
   execution, then use `--device` only on an authorized NPU host.
5. Record actual versions and all blocked checks; route missing backend
   registration to [dispatch](../privateuse1-and-dispatch/lesson.md).

Source-derived candidate: no wheel install, source build or NPU operation was
validated by this contribution. A clean pip dependency report is insufficient
to qualify the CANN/driver/device combination. Preserve `BLOCKED_REQUIRED_BACKEND`
when the actual Ascend environment is absent.

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

- [metadata.json](../../../../../../../skill_library/frameworks/torch-npu/torch-npu/sub-skills/installation-and-compatibility/metadata.json)
