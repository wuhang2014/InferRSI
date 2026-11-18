<!-- handbook
{
  "id": "mlx.mlx.execution.evaluation_completion",
  "kind": "record",
  "aliases": [
    "package:mlx.mlx.execution.evaluation_completion"
  ],
  "tags": [
    "mlx",
    "lazy-evaluation",
    "completion",
    "timing"
  ],
  "carry": [
    "unit-when-this-applies",
    "unit-limits-of-this-evidence"
  ]
}
-->

# MLX evaluation: distinguish graph construction, submission and readable completion

> Recorded state `imported` · locally verified `false` · evidence level `guidance` · license `MIT` · [Source](../../../../../../../knowledge_packs/dependency/mlx/mlx/execution/evaluation-completion.json)

At the pinned implementation, creating an array graph and marking it evaluated do not alone establish host-readable completion; eval and array waits provide separate completion boundaries.

`dependency` · `mlx` · `mlx` · `execution.evaluation_completion`

<a id="unit-when-this-applies"></a>
## When this applies

- **Software**
  - ml-explore/mlx at bff10220c742907f0c68e55ff174aaea56f74e3d; later revisions require reinspection
- **Conditions**
  - Actual backend, streams, shapes/dtypes and evaluation boundary are recorded.
  - CPU, Metal and CUDA source paths are distinguished; discovery or catalog placement is not runtime qualification.

<a id="unit-what-the-source-reports"></a>
## What the source reports

- **Source observation.** Array construction retains its primitive and inputs. async_eval submits unscheduled outputs; eval waits on existing output events or the eval_impl synchronizer.
- **Source observation.** is_available distinguishes evaluated arrays with unfinished events from available arrays. array::eval evaluates unscheduled arrays and otherwise waits.

<a id="unit-consequences-for-a-downstream-project"></a>
## Consequences for a downstream project

- An InferRSI transfer hypothesis for a matching MLX workload; no implicit vLLM, MLX-LM or other engine compatibility is claimed.

<a id="unit-putting-the-idea-to-work"></a>
## Putting the idea to work

- Identify the exact eval, stream synchronization or host-read boundary before interpreting submission time as completed work.

<a id="unit-how-to-check-it"></a>
## How to check it

- On a separately authorized matching build, retain identical inputs and compare async submission timing with an explicit completion boundary and checked results.

<a id="unit-limits-of-this-evidence"></a>
## Limits of this evidence

- This card addresses read readiness, not cross-stream dependency wiring, allocator policy or model performance.
- Source map originally inspected 2026-10-21; these bounded implementation ranges were rechecked 2026-10-23. No MLX backend test or performance measurement was run.

<a id="unit-sources"></a>
## Sources

- **Type** — source_code
- **Url** — <https://github.com/ml-explore/mlx/blob/bff10220c742907f0c68e55ff174aaea56f74e3d/mlx/array.cpp#L19-L39>
- **Commit** — bff10220c742907f0c68e55ff174aaea56f74e3d
- **Accessed at** — 2026-10-21
- **Rechecked at** — 2026-10-23
- **Content sha256** — 1b00e14138d085ae990c2db3f97a8bf28315ea46218d7ee7f9bcade22977a643

- **Type** — source_code
- **Url** — <https://github.com/ml-explore/mlx/blob/bff10220c742907f0c68e55ff174aaea56f74e3d/mlx/array.cpp#L129-L158>
- **Commit** — bff10220c742907f0c68e55ff174aaea56f74e3d
- **Accessed at** — 2026-10-21
- **Rechecked at** — 2026-10-23
- **Content sha256** — 1b00e14138d085ae990c2db3f97a8bf28315ea46218d7ee7f9bcade22977a643

- **Type** — source_code
- **Url** — <https://github.com/ml-explore/mlx/blob/bff10220c742907f0c68e55ff174aaea56f74e3d/mlx/transforms.cpp#L367-L395>
- **Commit** — bff10220c742907f0c68e55ff174aaea56f74e3d
- **Accessed at** — 2026-10-21
- **Rechecked at** — 2026-10-23
- **Content sha256** — f37ce2b416a38e75fe26ed1762f1bb99bb0e0475d925051a5abb5040bd8e56da

<a id="unit-attribution"></a>
## Attribution

- Copyright © 2023 Apple Inc. Source observations are paraphrased; no implementation code is copied.

<a id="unit-companion-material"></a>
## Companion material

- [SKILL.md](../../../../../frameworks/mlx/lazy-evaluation-stream-lifetimes/lesson.md)
