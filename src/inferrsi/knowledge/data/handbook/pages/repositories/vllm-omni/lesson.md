<!-- handbook
{
  "id": "repositories/vllm-omni",
  "kind": "procedure"
}
-->

# vLLM-Omni engine knowledge

> license `Apache-2.0` · [Source](../../../../skill_library/repositories/vllm-omni/SKILL.md) · [Parent reading](../../library/overview.md)

Explain, tune and extend vLLM-Omni multi-stage AR, diffusion and media-output inference with source-grounded search spaces and validation.

Use this skill to explain, configure, tune or extend **vLLM-Omni** stage-based autoregressive, generation and diffusion execution. Multimodal input alone does not select this skill; its distinguishing boundary is heterogeneous output and model-owned execution pipelines.

This is a source-grounded portable candidate at `52194f24fa42e14d1c5e096f4bea4dc7f95cffa1`. It is not a GPU certification or a complete model catalogue. Read [provenance](references/repo-provenance.md) when the checkout or installed packages differ.

<a id="unit-source-and-responsibility-map"></a>
## Source and responsibility map

Choose the scope before applying the existing procedures. The dates below are
the original inspections of two separate source snapshots.

| Decision scope | Canonical entry | Retained source / inspection | Evidence boundary |
| --- | --- | --- | --- |
| Stage/model topology, deployment, streaming measurement and step/output contracts | [Architecture](sub-skills/omni-architecture/lesson.md), [serving](sub-skills/omni-serving/lesson.md) and [extension](sub-skills/omni-validation/references/validation.md) | `52194f24fa42e14d1c5e096f4bea4dc7f95cffa1`; 2026-10-14; Apache-2.0 | Original source-derived candidate; establish the selected model/backend and producer/consumer contract |
| Abort submission/receipt, wait-only timeout, partial output, logical cleanup and deferred transfer release | [Abort validation](sub-skills/omni-validation/lesson.md) and its [completion boundaries](sub-skills/omni-validation/references/abort-acknowledgment.md#unit-keep-three-completion-boundaries-separate) | `18c3bd5d2d4323bc7adca1ac3c465c4a53bbfb6e`; 2026-10-22; Apache-2.0 | Bounded CODE / TEST-SOURCE; logical acknowledgment and native transfer reclamation are separate completion boundaries |

Keep each row with its own [provenance](references/repo-provenance.md) and
[evidence](references/evidence.md). The later readset supplements only the
abort path; the two snapshots do not define a jointly tested runtime or
compatibility range.

<a id="unit-route-by-decision"></a>
## Route by decision

| Need | Load |
|---|---|
| Explain data/control flow, derive a constrained engine search space | [Architecture and search](sub-skills/omni-architecture/lesson.md) |
| Choose deployment, stage placement, streaming and performance experiments | [Serving and tuning](sub-skills/omni-serving/lesson.md) |
| Add/change a pipeline, runner or connector; verify correctness | [Extension and validation](sub-skills/omni-validation/lesson.md) |

Read only the relevant branch. Source links in [evidence](references/evidence.md) resolve to the pinned revision; instructions and decision criteria are bundled here. Native test commands require a matching engine checkout and environment.

<a id="unit-shared-procedure"></a>
## Shared procedure

1. Identify exact model revision, task/output modality, reference implementation, GPU topology, software revisions, input/output shapes, concurrency and latency/quality contract. State unknowns; do not invent an optimal configuration.
2. Trace `PipelineConfig` → deploy resolution → orchestrator → stage pool/client → scheduler/runner → connector/output processor. Keep topology ownership separate from placement and resource knobs.
3. Label each proposal **existing setting**, **implementation change**, or **research extension**. A dataclass field is not proof that every model/backend supports it.
4. Establish a real-model baseline with the smallest supported concurrency. Preserve model, sampling, generated duration/resolution, seeds and quality target while tuning execution.
5. Compare correctness before latency, then report queue time, stage time, transfer time, peak memory and modality-specific end-to-end metrics. Preserve rejected trials and fallback paths.

<a id="unit-constraints-that-change-decisions"></a>
## Constraints that change decisions

- `PipelineConfig` and `StagePipelineConfig` own fixed model semantics and stage topology. Changing those requires a registered model variant and new validation; deploy YAML does not define arbitrary new model stages.
- A replica is not a model stage or a tensor-parallel rank. Stateful chunks must retain request/replica affinity until completion, cancellation or explicit failure handling.
- Async chunk transfer, AR continuous batching, diffusion request batching, diffusion step scheduling and streamed final media are different capabilities.
- Do not apply a Thinker quantization recipe to Talker/codec/VAE components without a compatible implementation and quality evidence.
- Successful YAML parsing, imports, CPU probes or mock tests do not establish GPU execution, media quality or throughput.

Return a decision with source evidence, feasible alternatives, assumptions, validation gates and recovery steps. No speedup is established by this skill alone.

<a id="unit-source-files"></a>
## Source files

- [LICENSE](../../../../skill_library/repositories/vllm-omni/LICENSE)
- [references/repo-routing-metadata.json](../../../../skill_library/repositories/vllm-omni/references/repo-routing-metadata.json)
