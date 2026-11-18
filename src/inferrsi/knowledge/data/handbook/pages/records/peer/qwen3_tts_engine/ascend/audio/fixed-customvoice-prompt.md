<!-- handbook
{
  "id": "qwen3_tts_engine.ascend.audio.fixed_customvoice_prompt",
  "kind": "record",
  "aliases": [
    "package:qwen3_tts_engine.ascend.audio.fixed_customvoice_prompt"
  ],
  "tags": [
    "customvoice",
    "prompt",
    "embedding_cache",
    "prefill"
  ],
  "carry": [
    "unit-when-this-applies",
    "unit-limits-of-this-evidence"
  ]
}
-->

# Qwen3-TTS CustomVoice: cache only model-fixed prompt embeddings

> Recorded state `imported` · locally verified `false` · evidence level `guidance` · [Source](../../../../../../../knowledge_packs/peer/qwen3_tts_engine/ascend/audio/fixed-customvoice-prompt.json)

Prepare CustomVoice prompt embeddings directly, reusing fixed special-token and speaker/language prefixes while recomputing request-dependent text and instruction projections.

`peer` · `qwen3_tts_engine` · `ascend` · `audio.tts`

<a id="unit-when-this-applies"></a>
## When this applies

- **Hardware**
  - Ascend 910B1 source campaign; other devices require independent qualification
- **Software**
  - Qwen/Qwen3-TTS-12Hz-1.7B-CustomVoice
  - InferMatrixLab/qwen3-tts-engine source snapshot; consult source evidence for measured revisions
- **Conditions**
  - CustomVoice template and tokenizer behavior must match the inspected wrapper.
  - Model weights, device, dtype and speaker/language configuration stay fixed for the cache lifetime.

<a id="unit-what-the-source-reports"></a>
## What the source reports

- **Upstream reported.** CustomVoicePrompt caches special embeddings and prefixes keyed by normalized speaker and resolved language; it validates supported speakers/languages.
- **Upstream reported.** Request text and instruction projections are computed per call; returned trailing-text and pad embeddings are cloned.

<a id="unit-consequences-for-a-downstream-project"></a>
## Consequences for a downstream project

- vLLM-Omni: first compare its processor output with the reference prompt builder. Reuse only fixed embeddings at the correct model owner.
- Do not cache arbitrary request text or reuse prefixes across different models/adapters without identity and invalidation rules.

<a id="unit-putting-the-idea-to-work"></a>
## Putting the idea to work

- Treat each mechanism as a separate transfer experiment; do not multiply isolated or combined-stack gains.

<a id="unit-how-to-check-it"></a>
## How to check it

- Compare full inputs_embeds, masks and generation kwargs against the reference for English, Chinese, auto language, dialect speakers and nonempty instructions.
- Test repeated and changed text, mixed speakers and model reload; include unsupported-language and empty-input behavior.
- Then validate generated audio and service TTFA under the frozen workload; prompt parity alone is not a service result.

<a id="unit-limits-of-this-evidence"></a>
## Limits of this evidence

- This is a CustomVoice-specific template optimization, not a generic Qwen3-TTS task adapter.
- Fixed-weight cache lifetime and hard-coded template slicing require revalidation after tokenizer or model updates.
- Imported source guidance only; no InferRSI accelerator, audio-quality or end-to-end reproduction.

<a id="unit-sources"></a>
## Sources

- **Url** — <https://github.com/InferMatrixLab/qwen3-tts-engine/blob/9f190577aa2a147c6840560a56c5996a6c4879a4/qwen3_tts_engine/custom_voice_prompt.py>
- **Type** — source_code
- **Commit** — 9f190577aa2a147c6840560a56c5996a6c4879a4
- **Accessed at** — 2026-10-19
- **Content sha256** — 3c3b2d6a3c948159c85b0073d678b831b860f7c65aa68e6de43b7c3b9e64177c

- **Url** — <https://github.com/InferMatrixLab/qwen3-tts-engine/blob/9f190577aa2a147c6840560a56c5996a6c4879a4/qwen3_tts_engine/continuous.py>
- **Type** — source_code
- **Commit** — 9f190577aa2a147c6840560a56c5996a6c4879a4
- **Accessed at** — 2026-10-19
- **Content sha256** — ad803c1ebe062fce51b647c1f8ebedc8bf5a3acfaa2e4366bcfacfecb1549b3b
