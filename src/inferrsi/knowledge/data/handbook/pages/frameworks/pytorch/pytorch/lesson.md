<!-- handbook
{
  "id": "pytorch",
  "kind": "procedure",
  "aliases": [
    "checkout:pytorch",
    "inferrsi.common.skills.pytorch",
    "package:inferrsi.common.skills.pytorch"
  ],
  "tags": [
    "pytorch",
    "tensor",
    "autograd",
    "training",
    "compiler",
    "distributed",
    "repository-guide"
  ]
}
-->

# PyTorch operating graph

> Recorded state `candidate` · empirical validation `not_run` · license `NOASSERTION` · [Source](../../../../../skill_library/frameworks/pytorch/pytorch/SKILL.md) · [Scope and provenance](../../../../../skill_library/frameworks/pytorch/pytorch/metadata.json) · [Catalog record](../../../../../repo_packs/inferrsi/knowledge/common/skills/pytorch.json) · [Catalog revision](../../../../../repo_packs/inferrsi/knowledge/_provenance.json) · [Parent reading](../../../library/overview.md)

Operate and diagnose PyTorch installation, tensors and autograd, training and data, compilation and export, accelerator lifetimes, distributed execution, checkpointing, profiling and custom operators from pinned repository evidence.

Use this graph to plan a PyTorch workflow or isolate a source, API, numerical,
compiler, device, communication or serialization failure. It covers the major
repository workflows through eight routes. **Candidate** describes knowledge
state; source breadth does not mean every file or backend was executed.

Read [provenance](references/repo-provenance.md) before transferring a recipe to
another revision. The pinned source is `pytorch/pytorch` at
`9a90a4fefcaafa63ac984621963a6fcc66aee68c` (`2.16.0a0` source version).
Installed-wheel observations are a distinct evidence class. Accelerator and
distributed backend qualification must use the actual target stack.

| User task | Route | Expected artifact |
| --- | --- | --- |
| Choose a wheel/backend; build Python or LibTorch; repair import/ABI | [installation and build](sub-skills/installation-and-build/lesson.md) | Environment/build identity and smoke result |
| Tensor layout/device/dtype, missing gradient, sparse/nested, torch.func | [tensor, dispatch and autograd](sub-skills/tensor-dispatch-autograd/lesson.md) | Tensor/alias/gradient contract |
| nn/optim, training/eval, DataLoader, AMP, SDPA, activation recompute | [training and data](sub-skills/training-and-data/lesson.md) | Bounded step with state and data checks |
| Dynamo guards, Inductor, FX, export, ONNX, TorchScript/mobile migration | [compiler and export](sub-skills/compiler-and-export/lesson.md) | Graph/shape/deployment contract |
| OOM, allocated versus reserved bytes, streams, graph replay | [memory, streams and graphs](sub-skills/memory-streams-and-graphs/lesson.md) | Storage/stream lifetime ledger |
| torchrun, c10d, DDP/FSDP2/DTensor, serialization and DCP | [distributed and checkpoint](sub-skills/distributed-and-checkpoint/lesson.md) | Rank/collective schedule and restore plan |
| Trace/time/memory, nonfinite results, backend/compiler isolation | [profiling and debugging](sub-skills/profiling-and-debugging/lesson.md) | Reproduction and bounded measurement |
| torch.library, FakeTensor, gradients, C++/CUDA/SYCL extension | [custom operators and extensions](sub-skills/custom-operators-and-extension/lesson.md) | Schema, numerical and registration checks |

Start by identifying source commit or distribution version, wheel backend tag,
Python/OS, device and driver/runtime, workload shapes/dtypes/layouts, grad mode,
state/seed and the smallest failing example. Run the bundled
[environment inspector](../../../../../skill_library/frameworks/pytorch/pytorch/scripts/inspect_environment.py) in the chosen environment:

```bash
python <SKILL_DIR>/scripts/inspect_environment.py
python <SKILL_DIR>/scripts/inspect_environment.py --require-backend cuda
```

`<SKILL_DIR>` is this skill's installed directory; helpers run from any current
directory. Inspection reports bounded software facts, never automatic package
repair, model downloads or a performance verdict. Use the installation route
for the source-build recipe and current backend prerequisites.

For cross-route tasks, preserve the earliest incorrect boundary. A custom op
needs tensor/schema correctness before compiler eligibility; graph replay needs
stream/address lifetimes before timing; distributed resume needs allocation and
state ownership before throughput tuning. Use eager CPU as a control where it
represents the same semantics; preserve a missing device check separately.

Cross-cutting failures are in [troubleshooting](references/troubleshooting.md).
[Repository coverage](references/source-directory-coverage.md) explicitly maps
all top-level source directories and public module families to their owners or
exclusions. [Readset](../../../../../skill_library/frameworks/pytorch/pytorch/references/source-readset.json) distinguishes exact inspected
spans from tree inventory. [Script disposition](references/source-script-map.md)
explains bundled helpers and excluded source tooling.

Existing owners remain authoritative for their focused procedures:
[host memory management](../../../hardware/host/host-memory-management/lesson.md)
and [DCP async save performance](../dcp-async-save-performance/lesson.md).
Their source revisions and evidence stay independent; following a link does not
update their pins or qualify the current PyTorch snapshot.

Read [notices](references/notices.md) before redistribution. This InferRSI
package preserves the AREX operating-role, visibility and repository-license
fields in local-skill-v1 sidecars. It does not imply deployment into a managed
DisCo installation. No TorchNPU/PyTorch compatibility pairing is inferred.

<a id="unit-when-this-applies"></a>
## When this applies

- **Scope** — Major user workflows and selected deep mechanisms of pinned pytorch/pytorch source; exact device/operator qualification remains task-specific.
- **Prerequisites**
  - An explicitly selected installed torch environment for runtime helpers.
  - Actual required devices, supported build and trusted ranks/storage for backend/distributed operations.
- **Input contract** — A concrete model/tensor/data/environment reproduction and desired operation or expected behavior.
- **Produced artifact** — A route-specific environment, tensor/gradient, graph, memory/stream, rank/state or measurement contract with checked and missing evidence.
- **Failure modes**
  - Transferring pinned-source behavior to another release/backend without checking compatibility.
  - Confusing source inventory, CPU diagnostics and target backend execution.
- **Refusal point** — Withhold backend success and performance conclusions when required runtime or workload evidence is missing.

<a id="unit-limits-of-this-evidence"></a>
## Limits of this evidence

- Source-derived candidate; empirical efficacy not_run.
- Required CUDA/ROCm/MPS/XPU/external accelerator and NCCL/graph checks unavailable locally retain BLOCKED_REQUIRED_BACKEND.
- Installed CPU wheel 2.15.0+cpu is separate from pinned source 2.16.0a0; CPU diagnostics are not same-source native verification.
- No automatic compatibility pairing with independently pinned TorchNPU.
- Directory inventory does not imply every file/operator/device was semantically read or run.

<a id="unit-declared-references"></a>
## Declared references

- [host-memory-management](../../../hardware/host/host-memory-management/lesson.md)
- [dcp-async-save-performance](../dcp-async-save-performance/lesson.md)

<a id="unit-source-files"></a>
## Source files

- [LICENSE](../../../../../skill_library/frameworks/pytorch/pytorch/LICENSE)
- [metadata.json](../../../../../skill_library/frameworks/pytorch/pytorch/metadata.json)
- [references/repo-routing-metadata.json](../../../../../skill_library/frameworks/pytorch/pytorch/references/repo-routing-metadata.json)
- [references/source-readset.json](../../../../../skill_library/frameworks/pytorch/pytorch/references/source-readset.json)
- [references/upstream-NOTICE](../../../../../skill_library/frameworks/pytorch/pytorch/references/upstream-NOTICE)
- [scripts/inspect_environment.py](../../../../../skill_library/frameworks/pytorch/pytorch/scripts/inspect_environment.py)
