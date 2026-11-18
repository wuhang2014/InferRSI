<!-- handbook
{
  "id": "mlx.mlx.execution.cross_stream_dependency",
  "kind": "record",
  "aliases": [
    "package:mlx.mlx.execution.cross_stream_dependency"
  ],
  "tags": [
    "mlx",
    "stream",
    "fence",
    "event"
  ],
  "carry": [
    "unit-when-this-applies",
    "unit-limits-of-this-evidence"
  ]
}
-->

# MLX streams: preserve producer-consumer dependency ordering

> Recorded state `imported` · locally verified `false` · evidence level `guidance` · license `MIT` · [Source](../../../../../../../knowledge_packs/dependency/mlx/mlx/execution/cross-stream-dependency.json)

The pinned evaluation path uses fences within one evaluation and unfinished events across asynchronous evaluations; a device label alone does not identify the stream dependency.

`dependency` · `mlx` · `mlx` · `execution.stream_dependency`

<a id="unit-when-this-applies"></a>
## When this applies

- **Software**
  - ml-explore/mlx at bff10220c742907f0c68e55ff174aaea56f74e3d; later revisions require reinspection
- **Conditions**
  - Actual backend, streams, shapes/dtypes and evaluation boundary are recorded.
  - CPU, Metal and CUDA source paths are distinguished; discovery or catalog placement is not runtime qualification.

<a id="unit-what-the-source-reports"></a>
## What the source reports

- **Source observation.** Dependency collection records stream differences and tracks device switches separately. Consumers wait on a same-evaluation fence or an unfinished event from a different stream before primitive dispatch.
- **Source observation.** synchronize(Stream) selects one stream; the no-argument overload selects the default stream of the default device.

<a id="unit-consequences-for-a-downstream-project"></a>
## Consequences for a downstream project

- An InferRSI transfer hypothesis for a matching MLX workload; no implicit vLLM, MLX-LM or other engine compatibility is claimed.

<a id="unit-putting-the-idea-to-work"></a>
## Putting the idea to work

- Record producer and consumer streams and preserve the existing fence/event path before changing stream placement.

<a id="unit-how-to-check-it"></a>
## How to check it

- On a separately authorized matching backend, vary same-stream and cross-stream producer-consumer placement with identical inputs and check outputs after the declared completion boundary.

<a id="unit-limits-of-this-evidence"></a>
## Limits of this evidence

- Ordering a consumer does not itself prove a host-completion wait or permission to release its storage.
- CPU/Metal/CUDA implementations require separate execution qualification; this source observation establishes neither cross-device compatibility nor throughput.

<a id="unit-sources"></a>
## Sources

- **Type** — source_code
- **Url** — <https://github.com/ml-explore/mlx/blob/bff10220c742907f0c68e55ff174aaea56f74e3d/mlx/transforms.cpp#L130-L159>
- **Commit** — bff10220c742907f0c68e55ff174aaea56f74e3d
- **Accessed at** — 2026-10-21
- **Rechecked at** — 2026-10-23
- **Content sha256** — f37ce2b416a38e75fe26ed1762f1bb99bb0e0475d925051a5abb5040bd8e56da

- **Type** — source_code
- **Url** — <https://github.com/ml-explore/mlx/blob/bff10220c742907f0c68e55ff174aaea56f74e3d/mlx/transforms.cpp#L255-L275>
- **Commit** — bff10220c742907f0c68e55ff174aaea56f74e3d
- **Accessed at** — 2026-10-21
- **Rechecked at** — 2026-10-23
- **Content sha256** — f37ce2b416a38e75fe26ed1762f1bb99bb0e0475d925051a5abb5040bd8e56da

- **Type** — source_code
- **Url** — <https://github.com/ml-explore/mlx/blob/bff10220c742907f0c68e55ff174aaea56f74e3d/mlx/scheduler.cpp#L14-L32>
- **Commit** — bff10220c742907f0c68e55ff174aaea56f74e3d
- **Accessed at** — 2026-10-21
- **Rechecked at** — 2026-10-23
- **Content sha256** — eb155cffd2b8715be847447037f3a0245ffc062d9b091e25d22647b801cebc63

<a id="unit-attribution"></a>
## Attribution

- Copyright © 2023 Apple Inc. Source observations are paraphrased; no implementation code is copied.

<a id="unit-companion-material"></a>
## Companion material

- [SKILL.md](../../../../../frameworks/mlx/lazy-evaluation-stream-lifetimes/lesson.md)
