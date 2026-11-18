<!-- handbook
{
  "id": "qwen3_tts_engine.ascend.audio.graph_batching_state_ownership",
  "kind": "record",
  "aliases": [
    "package:qwen3_tts_engine.ascend.audio.graph_batching_state_ownership"
  ],
  "tags": [
    "npu_graph",
    "prefill",
    "continuous_batching",
    "kv_cache",
    "ttfa"
  ],
  "carry": [
    "unit-when-this-applies",
    "unit-limits-of-this-evidence"
  ]
}
-->

# Qwen3-TTS NPU graphs: batch prefill while preserving request state

> Recorded state `imported` · locally verified `false` · evidence level `guidance` · [Source](../../../../../../../knowledge_packs/peer/qwen3_tts_engine/ascend/audio/graph-batching-state-ownership.json)

Amortize host dispatch with captured prefill/decode and codec graphs, bounded admission and reusable request slots.

`peer` · `qwen3_tts_engine` · `ascend` · `audio.tts`

<a id="unit-when-this-applies"></a>
## When this applies

- **Hardware**
  - Ascend 910B1 source campaign; other devices require independent qualification
- **Software**
  - Qwen/Qwen3-TTS-12Hz-1.7B-CustomVoice
  - InferMatrixLab/qwen3-tts-engine source snapshot; consult source evidence for measured revisions
- **Conditions**
  - Ascend graph support and prepared buffers for supported shapes.
  - Decode capacity, prefill admission and codec batching must be tuned under the actual workload.

<a id="unit-what-the-source-reports"></a>
## What the source reports

- **Upstream reported.** The runtime combines iteration-level scheduling, slot-owned KV, batched prefill and graph-captured codec state.
- **Upstream reported.** Prefill bucket padding appends dummy rows whose outputs are not admitted as real requests; attention masks and real lengths remain part of the computation.

<a id="unit-consequences-for-a-downstream-project"></a>
## Consequences for a downstream project

- vLLM-Omni: reuse its scheduler, request identities and graph ownership; copying the standalone arena is not a drop-in optimization.
- Graph capture and batch policy are separate hypotheses. Measure first-audio latency as well as throughput before choosing admission sizes.

<a id="unit-putting-the-idea-to-work"></a>
## Putting the idea to work

- Treat each mechanism as a separate transfer experiment; do not multiply isolated or combined-stack gains.

<a id="unit-how-to-check-it"></a>
## How to check it

- Exercise changing batch sizes, mixed prompt lengths, graph misses, cancellation, slot reuse and capacity growth.
- Verify retained outputs are not overwritten by subsequent replays and dummy rows cannot become requests.
- Separate startup capture and warmup from timed service; repeat paired baseline/candidate workloads with lifecycle and quality checks.

<a id="unit-limits-of-this-evidence"></a>
## Limits of this evidence

- Unseen shapes can incur capture work during service.
- Larger admission batches may improve throughput while delaying first audio.
- Standalone combined-stack measurements do not isolate graph or scheduler contributions.
- Imported source guidance only; no InferRSI accelerator, audio-quality or end-to-end reproduction.

<a id="unit-sources"></a>
## Sources

- **Url** — <https://github.com/InferMatrixLab/qwen3-tts-engine/blob/9f190577aa2a147c6840560a56c5996a6c4879a4/qwen3_tts_engine/continuous.py>
- **Type** — source_code
- **Commit** — 9f190577aa2a147c6840560a56c5996a6c4879a4
- **Accessed at** — 2026-10-19
- **Content sha256** — ad803c1ebe062fce51b647c1f8ebedc8bf5a3acfaa2e4366bcfacfecb1549b3b

- **Url** — <https://github.com/InferMatrixLab/qwen3-tts-engine/blob/9f190577aa2a147c6840560a56c5996a6c4879a4/qwen3_tts_engine/prefill_graph.py>
- **Type** — source_code
- **Commit** — 9f190577aa2a147c6840560a56c5996a6c4879a4
- **Accessed at** — 2026-10-19
- **Content sha256** — 7d2941dcf74e73168b3f6d4ecbda913532572a2b710c65053d08f1a32304fd2e

- **Url** — <https://github.com/InferMatrixLab/qwen3-tts-engine/blob/9f190577aa2a147c6840560a56c5996a6c4879a4/qwen3_tts_engine/codec_slots.py>
- **Type** — source_code
- **Commit** — 9f190577aa2a147c6840560a56c5996a6c4879a4
- **Accessed at** — 2026-10-19
- **Content sha256** — ac2187d6c85e052c3c06f1a761eb6f59f7324f0b9c79635687a7cb6ea129f838
