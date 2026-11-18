<!-- handbook
{
  "id": "qwen3_tts_engine.ascend.audio.codec_constants_and_state",
  "kind": "record",
  "aliases": [
    "package:qwen3_tts_engine.ascend.audio.codec_constants_and_state"
  ],
  "tags": [
    "codebook",
    "codec",
    "streaming",
    "snake",
    "state"
  ],
  "carry": [
    "unit-when-this-applies",
    "unit-limits-of-this-evidence"
  ]
}
-->

# Qwen3-TTS codec: cache fixed codebooks and retain request-owned causal state

> Recorded state `imported` · locally verified `false` · evidence level `guidance` · [Source](../../../../../../../knowledge_packs/peer/qwen3_tts_engine/ascend/audio/codec-constants-and-state.json)

Avoid repeated codec normalization and history reconstruction under fixed evaluation weights; preserve per-request convolution and attention state.

`peer` · `qwen3_tts_engine` · `ascend` · `audio.tts`

<a id="unit-when-this-applies"></a>
## When this applies

- **Hardware**
  - Ascend 910B1 source campaign; other devices require independent qualification
- **Software**
  - Qwen/Qwen3-TTS-12Hz-1.7B-CustomVoice
  - InferMatrixLab/qwen3-tts-engine source snapshot; consult source evidence for measured revisions
- **Conditions**
  - Frozen evaluation weights and a stable model/device/dtype for the cache lifetime.
  - Streaming decoder semantics and history window must match the reference model.

<a id="unit-what-the-source-reports"></a>
## What the source reports

- **Upstream reported.** CachedQuantizer materializes normalized codebooks once and preserves the sequential residual-quantizer accumulation order.
- **Upstream reported.** IncrementalCodec retains causal convolution history and attention cache; CodecSlots supplies separate arena indices and frame positions for active streams.
- **Upstream reported.** Optional Snake constants and a BF16 contiguous Triton activation path are present. Their presence does not establish an isolated speedup.

<a id="unit-consequences-for-a-downstream-project"></a>
## Consequences for a downstream project

- vLLM-Omni: cache immutable codebook normalization inside the owning decoder; retain its existing stream ownership instead of copying the standalone scheduler.
- A downstream cache needs explicit invalidation on weight reload, device/dtype conversion and training; the standalone fixed-weight helper is not a general reload-safe module.

<a id="unit-putting-the-idea-to-work"></a>
## Putting the idea to work

- Treat each mechanism as a separate transfer experiment; do not multiply isolated or combined-stack gains.

<a id="unit-how-to-check-it"></a>
## How to check it

- Compare quantizer and waveform outputs over multiple chunk partitions, first/last chunks and residual-codebook counts.
- Interleave streams, cancel/reuse slots, poison old history and replay graph buffers to detect cross-request leakage.
- Measure eager and captured activation paths separately; keep unfused fallback if fusion regresses.

<a id="unit-limits-of-this-evidence"></a>
## Limits of this evidence

- The source helper assumes immutable evaluation weights and does not implement general cache invalidation.
- Codec fusion can lose to eager execution for some shapes; do not infer an operator gain from whole-engine throughput.
- Imported source guidance only; no InferRSI accelerator, audio-quality or end-to-end reproduction.

<a id="unit-sources"></a>
## Sources

- **Url** — <https://github.com/InferMatrixLab/qwen3-tts-engine/blob/9f190577aa2a147c6840560a56c5996a6c4879a4/qwen3_tts_engine/cached_quantizer.py>
- **Type** — source_code
- **Commit** — 9f190577aa2a147c6840560a56c5996a6c4879a4
- **Accessed at** — 2026-10-19
- **Content sha256** — 75207d415dbe425f677c4974880b56a066785e10a1715e058a9e790507c0498a

- **Url** — <https://github.com/InferMatrixLab/qwen3-tts-engine/blob/9f190577aa2a147c6840560a56c5996a6c4879a4/qwen3_tts_engine/incremental_codec.py>
- **Type** — source_code
- **Commit** — 9f190577aa2a147c6840560a56c5996a6c4879a4
- **Accessed at** — 2026-10-19
- **Content sha256** — cb555a40604f06981db409f5fc0773b39a556eb87930aababb56299e37e7acc4

- **Url** — <https://github.com/InferMatrixLab/qwen3-tts-engine/blob/9f190577aa2a147c6840560a56c5996a6c4879a4/qwen3_tts_engine/codec_slots.py>
- **Type** — source_code
- **Commit** — 9f190577aa2a147c6840560a56c5996a6c4879a4
- **Accessed at** — 2026-10-19
- **Content sha256** — ac2187d6c85e052c3c06f1a761eb6f59f7324f0b9c79635687a7cb6ea129f838
