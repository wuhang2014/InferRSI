<!-- handbook
{
  "id": "frameworks/pytorch/pytorch/sub-skills/distributed-and-checkpoint",
  "kind": "procedure",
  "tags": [
    "pytorch",
    "distributed-and-checkpoint"
  ]
}
-->

# Distributed and checkpoint

> Recorded state `candidate` · empirical validation `not_run` · license `NOASSERTION` · [Source](../../../../../../../skill_library/frameworks/pytorch/pytorch/sub-skills/distributed-and-checkpoint/SKILL.md) · [Scope and provenance](../../../../../../../skill_library/frameworks/pytorch/pytorch/sub-skills/distributed-and-checkpoint/metadata.json) · [Parent reading](../../lesson.md)

Set up or debug PyTorch c10d, DDP, FSDP2, DeviceMesh and DTensor, distributed checkpointing and trusted state serialization.

Use this route for the task named in the description. Produce a rank and collective schedule and a state-restore contract with explicit trust and backend boundaries.
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

- **Scope** — Set up or debug PyTorch c10d, DDP, FSDP2, DeviceMesh and DTensor, distributed checkpointing and trusted state serialization.
- **Prerequisites**
  - An explicitly selected installed torch environment; actual devices for backend-specific checks.
- **Input contract** — A bounded model, tensor, data or environment reproduction and expected behavior.
- **Produced artifact** — Produce a rank and collective schedule and a state-restore contract with explicit trust and backend boundaries.
- **Failure modes**
  - Transferring source facts to another wheel or backend without checking drift.
- **Refusal point** — Withhold backend success when the required device check cannot execute.

<a id="unit-limits-of-this-evidence"></a>
## Limits of this evidence

- Source-supported procedures are not full-repository execution coverage.
- Required unavailable backends retain BLOCKED_REQUIRED_BACKEND; no measured efficacy claim.

<a id="unit-source-files"></a>
## Source files

- [metadata.json](../../../../../../../skill_library/frameworks/pytorch/pytorch/sub-skills/distributed-and-checkpoint/metadata.json)
- [scripts/rank_contract.py](../../../../../../../skill_library/frameworks/pytorch/pytorch/sub-skills/distributed-and-checkpoint/scripts/rank_contract.py)
- [scripts/state_roundtrip.py](../../../../../../../skill_library/frameworks/pytorch/pytorch/sub-skills/distributed-and-checkpoint/scripts/state_roundtrip.py)
