<!-- handbook
{
  "id": "torch-npu",
  "kind": "procedure",
  "aliases": [
    "checkout:torch-npu",
    "inferrsi.ascend.skills.torch_npu",
    "package:inferrsi.ascend.skills.torch_npu"
  ],
  "tags": [
    "torch-npu",
    "ascend",
    "pytorch"
  ]
}
-->

# TorchNPU operating graph

> Recorded state `candidate` · empirical validation `not_run` · license `NOASSERTION` · [Source](../../../../../skill_library/frameworks/torch-npu/torch-npu/SKILL.md) · [Scope and provenance](../../../../../skill_library/frameworks/torch-npu/torch-npu/metadata.json) · [Catalog record](../../../../../repo_packs/inferrsi/knowledge/ascend/skills/torch-npu.json) · [Catalog revision](../../../../../repo_packs/inferrsi/knowledge/_provenance.json) · [Parent reading](../../../library/overview.md)

Operate and diagnose TorchNPU on Ascend across installation, PrivateUse1 dispatch, operator development, memory and streams, graphs and compilation, HCCL, precision and profiling, with pinned source evidence and explicit backend limits.

Use for Ascend/pytorch's TorchNPU adapter. Collect exact torch/torch-npu builds,
CANN/driver/hardware, the selected eager/compile/distributed mode, tensor
shape/dtype/layout and a bounded reproduction. This is a source-derived
candidate, not a validated installed stack. NPU, CANN, HCCL and optional compiler
checks remain `BLOCKED_REQUIRED_BACKEND` until exercised on the actual backend.

Choose the narrowest route, then compose routes when the failure crosses an
ownership boundary:

| User goal or symptom | Owning procedure |
|---|---|
| Install, select versions, missing shared library, build/package mismatch | [Installation and compatibility](sub-skills/installation-and-compatibility/lesson.md) |
| Missing `torch.npu`, import ordering, unsupported op or hidden CPU fallback | [PrivateUse1 and dispatch](sub-skills/privateuse1-and-dispatch/lesson.md) |
| Add an overload/custom op; fix schema, backward or Meta support | [Operator development](sub-skills/operator-development/lesson.md) |
| Async corruption, stream waits, allocation reuse, pinned copies, memory retention | [Memory, streams and events](sub-skills/memory-streams-and-events/lesson.md) |
| NPUGraph replay, `torch.compile`, graph breaks, compiler choice or eager fallback | [Graph and compile](sub-skills/graph-and-compile/lesson.md) |
| Multi-rank launch, HCCL/P2P, hangs, work completion or sharding boundary | [Distributed and HCCL](sub-skills/distributed-and-hccl/lesson.md) |
| Training migration, autocast/scaler, overflow, optimizer or checkpoint state | [Training and precision](sub-skills/training-and-precision/lesson.md) |
| Trace collection, memory timeline, async exception or sanitizer | [Profiling and debugging](sub-skills/profiling-and-debugging/lesson.md) |

For migration shims, serialization/export, fused modules, RPC, DTensor/FSDP,
FXRT deployment and fault tooling, read [support workflows](references/support-workflows.md).
The [capability inventory](references/capability-inventory.md) distinguishes
substantive inspection from directory discovery and names remaining boundaries.

<a id="unit-operating-contract"></a>
## Operating contract

1. Qualify the environment before executing a device workflow. Run
   `python <SKILL_ROOT>/scripts/inspect_environment.py` for package metadata only;
   use `--device` explicitly for a tiny allocation/matmul/completion check.
2. State the relevant source mechanism and the actual last inspected boundary.
   Use [the evidence ledger](references/source-map.md) and
   [immutable provenance](references/repo-provenance.md) for revision alignment.
3. Establish correctness before changing precision, compilation, allocator or
   overlap policy. Keep producer ordering, storage lifetime and completion
   observations distinct.
4. Use [runtime smoke examples](../../../../../skill_library/frameworks/torch-npu/torch-npu/scripts/runtime_smoke.py) only after selecting
   their exact case and `--run`; the default is non-executing. The
   [operator contract checker](../../../../../skill_library/frameworks/torch-npu/torch-npu/scripts/operator_contract.py) requires only
   standard-library Python and checks declarations, not a device kernel.
5. Return exact stack identities, chosen path, observations and pass/fail/not-run
   scope. Restore a known-correct configuration if a bounded experiment fails.

Expected output is an executable proposal or diagnostic trace with explicit
verification state. Reading this graph does not authorize installations,
multi-rank launches, device reset, stress tests or arbitrary upstream scripts.
Use only the operations needed for the caller's authorized task.

<a id="unit-boundaries-and-related-owners"></a>
## Boundaries and related owners

Do not infer device readiness from registration, NPU coverage from CPU fallback,
memory safety from ordering alone, completed HCCL transfer from a host future,
compilation from an eager fallback, or service gains from submission timing.
CPU/helper/static checks cannot substitute for required accelerator execution.
No convergence, benchmark gain, L4 service result or candidate promotion is
established by this graph.

Existing skill IDs `torchnpu-device-memory-lifecycle` and
`torchnpu-pinned-host-memory-lifecycle` own focused allocator tuning at their
earlier exact source pin. Metadata declares those relationships; their evidence
is not refreshed here. This graph provides newer end-to-end operating routes
and preserves both revision boundaries.

Full-repository inventory does not mean every operator, CANN kernel, compiler
pass or device family was inspected. The pinned op-plugin readset covers real
adapter/generator/registration mechanisms; other gitlinks remain explicit
external dependencies. See [source-script decisions](references/source-script-inventory.md)
and [attribution and retained licenses](../../../../../skill_library/frameworks/torch-npu/torch-npu/references/NOTICE.md).

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

<a id="unit-declared-references"></a>
## Declared references

- [torchnpu-device-memory-lifecycle](../../../hardware/ascend/torchnpu-device-memory-lifecycle/lesson.md)
- [torchnpu-pinned-host-memory-lifecycle](../../../hardware/ascend/torchnpu-pinned-host-memory-lifecycle/lesson.md)

<a id="unit-source-files"></a>
## Source files

- [metadata.json](../../../../../skill_library/frameworks/torch-npu/torch-npu/metadata.json)
- [references/NOTICE.md](../../../../../skill_library/frameworks/torch-npu/torch-npu/references/NOTICE.md)
- [references/licenses/op-plugin-LICENSE.txt](../../../../../skill_library/frameworks/torch-npu/torch-npu/references/licenses/op-plugin-LICENSE.txt)
- [references/licenses/op-plugin-THIRD-PARTY.txt](../../../../../skill_library/frameworks/torch-npu/torch-npu/references/licenses/op-plugin-THIRD-PARTY.txt)
- [references/licenses/source-identities.json](../../../../../skill_library/frameworks/torch-npu/torch-npu/references/licenses/source-identities.json)
- [references/licenses/torch-npu-LICENSE.txt](../../../../../skill_library/frameworks/torch-npu/torch-npu/references/licenses/torch-npu-LICENSE.txt)
- [references/licenses/torch-npu-THIRD-PARTY.txt](../../../../../skill_library/frameworks/torch-npu/torch-npu/references/licenses/torch-npu-THIRD-PARTY.txt)
- [references/licenses/torch-npu-docs-LICENSE.txt](../../../../../skill_library/frameworks/torch-npu/torch-npu/references/licenses/torch-npu-docs-LICENSE.txt)
- [references/repo-routing-metadata.json](../../../../../skill_library/frameworks/torch-npu/torch-npu/references/repo-routing-metadata.json)
- [references/source-manifest.json](../../../../../skill_library/frameworks/torch-npu/torch-npu/references/source-manifest.json)
- [scripts/inspect_environment.py](../../../../../skill_library/frameworks/torch-npu/torch-npu/scripts/inspect_environment.py)
- [scripts/operator_contract.py](../../../../../skill_library/frameworks/torch-npu/torch-npu/scripts/operator_contract.py)
- [scripts/runtime_smoke.py](../../../../../skill_library/frameworks/torch-npu/torch-npu/scripts/runtime_smoke.py)
