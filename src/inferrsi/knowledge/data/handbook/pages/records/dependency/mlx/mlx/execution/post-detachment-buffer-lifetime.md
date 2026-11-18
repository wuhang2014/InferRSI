<!-- handbook
{
  "id": "mlx.mlx.execution.post_detachment_buffer_lifetime",
  "kind": "record",
  "aliases": [
    "package:mlx.mlx.execution.post_detachment_buffer_lifetime"
  ],
  "tags": [
    "mlx",
    "buffer-lifetime",
    "detachment",
    "donation"
  ],
  "carry": [
    "unit-when-this-applies",
    "unit-limits-of-this-evidence"
  ]
}
-->

# MLX buffers: graph detachment does not end in-flight storage ownership

> Recorded state `imported` · locally verified `false` · evidence level `guidance` · license `MIT` · [Source](../../../../../../../knowledge_packs/dependency/mlx/mlx/execution/post-detachment-buffer-lifetime.json)

Non-tracer graph references can detach after scheduling while backend-specific captures or temporaries retain buffers needed by queued work.

`dependency` · `mlx` · `mlx` · `execution.buffer_lifetime`

<a id="unit-when-this-applies"></a>
## When this applies

- **Software**
  - ml-explore/mlx at bff10220c742907f0c68e55ff174aaea56f74e3d; later revisions require reinspection
- **Conditions**
  - Actual backend, streams, shapes/dtypes and evaluation boundary are recorded.
  - CPU, Metal and CUDA source paths are distinguished; discovery or catalog placement is not runtime qualification.

<a id="unit-what-the-source-reports"></a>
## What the source reports

- **Source observation.** array::detach clears primitive, input and sibling graph references. eval_impl marks arrays evaluated and detaches non-tracers after primitive dispatch.
- **Source observation.** The CPU dispatch captures buffers and temporaries; Metal commit/completion callbacks capture buffers; CUDA retains non-donated inputs and siblings as encoder temporaries. Donation and tracer handling are explicit and backend-specific.

<a id="unit-consequences-for-a-downstream-project"></a>
## Consequences for a downstream project

- An InferRSI transfer hypothesis for a matching MLX workload; no implicit vLLM, MLX-LM or other engine compatibility is claimed.

<a id="unit-putting-the-idea-to-work"></a>
## Putting the idea to work

- Trace the selected backend retention owner and actual completion before interpreting dropped graph/Python references as storage reclamation.

<a id="unit-how-to-check-it"></a>
## How to check it

- On a separately authorized matching backend, retain checked outputs while releasing graph references, then distinguish in-flight retention from post-completion allocator caching.

<a id="unit-limits-of-this-evidence"></a>
## Limits of this evidence

- This card establishes retention obligations, not allocator eviction, a universal reclamation threshold, zero-copy or memory savings.
- Backend mechanisms are not interchangeable. No native lifetime, memory, model or service validation was run.

<a id="unit-sources"></a>
## Sources

- **Type** — source_code
- **Url** — <https://github.com/ml-explore/mlx/blob/bff10220c742907f0c68e55ff174aaea56f74e3d/mlx/array.cpp#L114-L127>
- **Commit** — bff10220c742907f0c68e55ff174aaea56f74e3d
- **Accessed at** — 2026-10-21
- **Rechecked at** — 2026-10-23
- **Content sha256** — 1b00e14138d085ae990c2db3f97a8bf28315ea46218d7ee7f9bcade22977a643

- **Type** — source_code
- **Url** — <https://github.com/ml-explore/mlx/blob/bff10220c742907f0c68e55ff174aaea56f74e3d/mlx/transforms.cpp#L306-L315>
- **Commit** — bff10220c742907f0c68e55ff174aaea56f74e3d
- **Accessed at** — 2026-10-21
- **Rechecked at** — 2026-10-23
- **Content sha256** — f37ce2b416a38e75fe26ed1762f1bb99bb0e0475d925051a5abb5040bd8e56da

- **Type** — source_code
- **Url** — <https://github.com/ml-explore/mlx/blob/bff10220c742907f0c68e55ff174aaea56f74e3d/mlx/backend/cpu/eval.cpp#L24-L51>
- **Commit** — bff10220c742907f0c68e55ff174aaea56f74e3d
- **Accessed at** — 2026-10-21
- **Rechecked at** — 2026-10-23
- **Content sha256** — c672eb013f28f7ad41d2eca12fc3fca115d714ca2536d0b034aebb18c683718d

- **Type** — source_code
- **Url** — <https://github.com/ml-explore/mlx/blob/bff10220c742907f0c68e55ff174aaea56f74e3d/mlx/backend/metal/eval.cpp#L29-L68>
- **Commit** — bff10220c742907f0c68e55ff174aaea56f74e3d
- **Accessed at** — 2026-10-21
- **Rechecked at** — 2026-10-23
- **Content sha256** — b03bd6c3aabda6f246a5d15ae21dc7e856d18f5af0d488c25e02e484718dce50

- **Type** — source_code
- **Url** — <https://github.com/ml-explore/mlx/blob/bff10220c742907f0c68e55ff174aaea56f74e3d/mlx/backend/cuda/eval.cpp#L43-L78>
- **Commit** — bff10220c742907f0c68e55ff174aaea56f74e3d
- **Accessed at** — 2026-10-21
- **Rechecked at** — 2026-10-23
- **Content sha256** — b29e659d510fba268b0617bdc6ab899d76ff24d83561bc70611ee1f43585fafb

<a id="unit-attribution"></a>
## Attribution

- Copyright © 2023 Apple Inc. Source observations are paraphrased; no implementation code is copied.

<a id="unit-companion-material"></a>
## Companion material

- [SKILL.md](../../../../../frameworks/mlx/lazy-evaluation-stream-lifetimes/lesson.md)
