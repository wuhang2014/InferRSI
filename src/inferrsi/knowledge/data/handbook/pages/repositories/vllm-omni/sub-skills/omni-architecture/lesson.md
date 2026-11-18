<!-- handbook
{
  "id": "repositories/vllm-omni/sub-skills/omni-architecture",
  "kind": "procedure"
}
-->

# Architecture and search

> license `Apache-2.0` · [Source](../../../../../../skill_library/repositories/vllm-omni/sub-skills/omni-architecture/SKILL.md) · [Parent reading](../../lesson.md)

Map vLLM-Omni stage ownership and derive constrained architecture or execution search spaces.

Use for source understanding or AI-generated engine design. Read [architecture and search dimensions](references/architecture.md), then the [evidence map](../../references/evidence.md).

Trace one concrete request through its chosen pipeline before generalizing. Record each stage's input/output contract, state owner, schedule unit, device, communication and terminal condition. Classify each candidate as an existing setting, implementation change or research extension.

Produce a dependency-constrained search table with legal domains, feasibility checks, quality constraints and measurements. Hold workload and model semantics fixed for execution experiments. Lower resolution, fewer denoise steps, quantization and approximate caches require their own quality budget.

If a field or capability is absent from this snapshot, mark it as a proposed extension. If two documents disagree, inspect their pinned implementation and tests; report residual uncertainty. Route runnable deployment questions to [serving](../omni-serving/lesson.md) and proposed code changes to [validation](../omni-validation/lesson.md).
