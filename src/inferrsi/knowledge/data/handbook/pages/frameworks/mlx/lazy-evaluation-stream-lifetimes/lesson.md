<!-- handbook
{
  "id": "lazy-evaluation-stream-lifetimes",
  "kind": "procedure",
  "aliases": [
    "checkout:lazy-evaluation-stream-lifetimes",
    "inferrsi.common.skills.lazy_evaluation_stream_lifetimes",
    "package:inferrsi.common.skills.lazy_evaluation_stream_lifetimes"
  ],
  "tags": [
    "mlx",
    "lazy-evaluation",
    "stream",
    "buffer-lifetime",
    "synchronization"
  ]
}
-->

# Diagnose MLX evaluation and lifetimes

> Recorded state `candidate` · empirical validation `not_run` · license `MIT` · [Source](../../../../../skill_library/frameworks/mlx/lazy-evaluation-stream-lifetimes/SKILL.md) · [Scope and provenance](../../../../../skill_library/frameworks/mlx/lazy-evaluation-stream-lifetimes/metadata.json) · [Catalog record](../../../../../repo_packs/inferrsi/knowledge/common/skills/lazy-evaluation-stream-lifetimes.json) · [Catalog revision](../../../../../repo_packs/inferrsi/knowledge/_provenance.json) · [Parent reading](../../../library/overview.md)

Diagnose MLX lazy evaluation, cross-stream ordering and array-buffer lifetimes when timing, memory use or asynchronous results disagree with expectations.

Use for an MLX workload with misleading submission timings, missing cross-stream dependencies, unexpected retained memory, or a result read before completion. Do not use as an LLM request scheduler, a model KV-cache policy, a compiler/fusion guide, or proof that a backend is installed.

This is a source-derived candidate. Runtime behavior and performance remain unverified. Read the [pinned source map](references/source-map.md) and [execution contract](references/execution-lifetime.md). CPU, Metal and CUDA have distinct implementations; `common` catalog placement describes framework-level guidance and does not certify portability.

<a id="unit-inputs"></a>
## Inputs

Collect the actual MLX revision/package build, backend and device, Python/C++ entry point, array shapes/dtypes, primitive streams, evaluation/read boundary, transformation context, and a bounded reproduction. For timing, retain warmup policy, inputs and the measured work boundary. For memory, distinguish live array references, in-flight buffers, allocator cache and synchronized measurements.

<a id="unit-procedure"></a>
## Procedure

1. **Locate the producer.** Follow the operation to its primitive and stream. At the source pin, `add` creates an array with an `Add` primitive and input dependencies; creating that graph is separate from evaluating it (F1).
2. **Locate the actual completion boundary.** Separate graph construction, `async_eval` submission, `eval`, and scalar/host reads. `eval` waits; an array marked `evaluated` can still carry an unfinished event. Record the explicit stream synchronized by the measurement rather than assuming the default stream covers every queue (F2).
3. **Trace dependency ordering.** Within one evaluation, cross-stream inputs use fences. Across asynchronous evaluations, unfinished events are waited on when their producer and consumer streams differ. A CPU/GPU device change is tracked separately from a same-device stream change. Preserve that dependency path before changing stream placement (F3).
4. **Trace ownership after graph detachment.** A non-tracer array can lose primitive/input graph references after scheduling while backend work still owns input buffers. Inspect the selected backend's retention mechanism and any donation path; dropping a Python variable is not proof that in-flight storage can be reused (F4).
5. **Classify the symptom.** Submission-only timings require a completion-boundary correction; retained in-flight memory requires completion evidence; cached allocator memory needs separate allocator evidence. For an error, inspect the evaluation cleanup and event-error path before calling it a leak or deadlock. Do not add a fallback that hides the original failure (F5).
6. **Choose the smallest discriminating validation.** Use the [validation reference](references/validation.md). First test the selected CPU semantics when applicable, then the actual Metal/CUDA path when the claim depends on it. Preserve inputs, dtype, stream topology and correctness checks. Benchmark only after identifying the executing path and timing boundary.

<a id="unit-output-and-stop-conditions"></a>
## Output and stop conditions

Return a compact producer → eval → dependency wait → backend → availability/cleanup trace, an ownership table, the observed symptom, one proposed next check, and passed/failed/not-run evidence tied to the actual build. Stop when the trace answers the question. If the required backend is absent, retain a source-supported diagnosis and the exact runtime gap; do not replace device evidence with CPU import success.

Do not claim a speedup from lazy graph construction time, infer fusion from lazy evaluation, infer zero data-movement cost from unified memory, or transfer Metal callback details to CUDA. A framework test does not establish model quality or serving behavior.

<a id="unit-when-this-applies"></a>
## When this applies

- **Scope** — MLX evaluation/stream/buffer diagnosis at the pinned implementation; qualify the actual backend separately.
- **Prerequisites** — Access to the pinned MLX execution/lifetime contract and a bounded reproduction with an identified evaluation/read boundary; device-dependent conclusions need the actual selected backend.
- **Input contract** — MLX revision/build, backend/device, Python/C++ entry, array shapes/dtypes, primitive streams, evaluation/read boundary and transformation context; timing needs warmup/work boundaries, while memory needs live references, in-flight buffers, allocator cache and synchronized observations.
- **Produced artifact** — A producer/evaluation/dependency-wait/backend/availability-cleanup trace, ownership table, observed symptom and one discriminating check with build-bound actual evidence status.
- **Failure modes** — Timing graph construction or submission as execution, assuming evaluated means completed, synchronizing only the default stream, or treating graph detachment/Python deletion as reusable storage can misdiagnose time or memory.
- **Refusal point** — Stop when the trace answers the question; if the required backend is absent, retain the source-supported diagnosis and exact runtime gap rather than substituting CPU import success.

<a id="unit-putting-the-idea-to-work"></a>
## Putting the idea to work

- Separate graph construction, async_eval submission, eval and host reads, and record which stream the measurement actually synchronizes.
- Preserve the dependency-wait path and selected backend buffer-retention/donation contract before changing streams or assuming storage can be reused.
- Distinguish live, in-flight and allocator-cached memory; inspect the real error/cleanup path before proposing a leak fix or hiding the failure.

<a id="unit-limits-of-this-evidence"></a>
## Limits of this evidence

- Source-derived candidate; no local native-backend, model, service or efficacy validation.
- Static content checks do not promote this candidate or establish installed API conformance.

<a id="unit-source-files"></a>
## Source files

- [metadata.json](../../../../../skill_library/frameworks/mlx/lazy-evaluation-stream-lifetimes/metadata.json)
