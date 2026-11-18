<!-- handbook
{
  "id": "frameworks/pytorch/pytorch/sub-skills/tensor-dispatch-autograd",
  "kind": "procedure",
  "tags": [
    "pytorch",
    "tensor-dispatch-autograd"
  ]
}
-->

# Tensor dispatch autograd

> Recorded state `candidate` · empirical validation `not_run` · license `NOASSERTION` · [Source](../../../../../../../skill_library/frameworks/pytorch/pytorch/sub-skills/tensor-dispatch-autograd/SKILL.md) · [Scope and provenance](../../../../../../../skill_library/frameworks/pytorch/pytorch/sub-skills/tensor-dispatch-autograd/metadata.json) · [Parent reading](../../lesson.md)

Diagnose PyTorch tensor layouts, dtype and device dispatch, autograd history, function transforms, sparse and nested tensor contracts.

Use this route for the task named in the description. Produce a tensor and gradient contract, then isolate the first wrong operator or dispatch boundary.
This is a source-derived **candidate**, with native backend checks separate from
source support. Read the root [provenance](../../references/repo-provenance.md)
when package, API or platform identity differs.

<a id="unit-operating-sequence"></a>
## Operating sequence

1. Record the concrete input contract, current behavior, desired result, package
   version and backend. Preserve a tiny eager or single-process control.
2. Read [workflows and mechanisms](references/workflows.md) and choose its
   matching branch. Check prerequisites before launching a build or device job.
3. Apply the smallest change at the first disagreeing boundary; preserve tensor
   shape, dtype, layout, device, mutation and gradient assumptions.
4. Check the predicted output and failure recovery using the linked helper or
   recipe. A software check cannot establish an unavailable device capability.
5. Return the artifact named above, checks actually run, unresolved conditions
   and the next discriminating check. Missing required backend execution stays
   **BLOCKED_REQUIRED_BACKEND**; efficacy stays **not_run** without measurements.

Read [troubleshooting](references/troubleshooting.md) when a prerequisite or
check fails. The references contain complete procedures and exact source
permalinks; the original source checkout is not a runtime prerequisite.

<a id="unit-when-this-applies"></a>
## When this applies

- **Scope** — Diagnose PyTorch tensor layouts, dtype and device dispatch, autograd history, function transforms, sparse and nested tensor contracts.
- **Prerequisites**
  - An explicitly selected installed torch environment; actual devices for backend-specific checks.
- **Input contract** — A bounded model, tensor, data or environment reproduction and expected behavior.
- **Produced artifact** — Produce a tensor and gradient contract, then isolate the first wrong operator or dispatch boundary.
- **Failure modes**
  - Transferring source facts to another wheel or backend without checking drift.
- **Refusal point** — Withhold backend success when the required device check cannot execute.

<a id="unit-limits-of-this-evidence"></a>
## Limits of this evidence

- Source-supported procedures are not full-repository execution coverage.
- Required unavailable backends retain BLOCKED_REQUIRED_BACKEND; no measured efficacy claim.

<a id="unit-source-files"></a>
## Source files

- [metadata.json](../../../../../../../skill_library/frameworks/pytorch/pytorch/sub-skills/tensor-dispatch-autograd/metadata.json)
- [scripts/tensor_contracts.py](../../../../../../../skill_library/frameworks/pytorch/pytorch/sub-skills/tensor-dispatch-autograd/scripts/tensor_contracts.py)
