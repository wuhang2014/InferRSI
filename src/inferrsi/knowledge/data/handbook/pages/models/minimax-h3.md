<!-- handbook
{
  "id": "model.minimax-h3",
  "kind": "profile",
  "carry": [
    "unit-limits-of-this-evidence"
  ]
}
-->

# MiniMax-H3

> locally verified `false` · evidence level `guidance` · [Source](../../../research_profiles/minimax-h3.json)

<a id="unit-component-roles"></a>
## Component roles

- **Role** — denoiser
- **Identity** — MiniMax-H3 joint video/audio DiT; select one task checkpoint

- **Role** — text_encoder
- **Identity** — Qwen3-VL-32B-derived language/vision encoder; inventory task-specific visual paths and selected full/truncated export

- **Role** — video_vae
- **Identity** — MiniMax-H3 video VAE, including input encoding and output decoding

- **Role** — audio_vae
- **Identity** — MiniMax-H3 audio VAE, including reference encoding and output decoding

<a id="unit-discovery-terms"></a>
## Discovery terms

- **Aliases**
  - MiniMax-H3
  - MiniMax H3
  - MiniMax_H3
- **Tasks**
  - diffusion
- **Modalities**
  - video
  - audio
- **Input modalities**
  - text
  - image
  - video
  - audio
- **Output modalities**
  - video
  - audio
- **Mechanisms**
  - quantization
  - offload
  - memory

<a id="unit-limits-of-this-evidence"></a>
## Limits of this evidence

- The profile supplies source-grounded discovery terms and component roles, not a parameter total, compatible engine/weight pair or target memory estimate.
- Quantization, offload and memory are investigation queries, not asserted supported settings.
- Inventory the actual selected weights, including task-specific encoder/decoder requirements; do not count alternative DiT checkpoints twice.

<a id="unit-sources"></a>
## Sources

- **Url** — <https://github.com/MiniMax-AI/MiniMax-H3/blob/d21241f0a4b3acbb34c97dae47fa417b7065e438/README.md>
- **Commit** — d21241f0a4b3acbb34c97dae47fa417b7065e438
- **Accessed at** — 2026-10-23

<a id="unit-companion-material"></a>
## Companion material

- [SKILL.md](../repositories/h3-c/audit-h3-runtime-residency/lesson.md)
- [minimax-h3-apple.md](../repositories/h3-c/audit-h3-runtime-residency/references/minimax-h3-apple.md)
- [minimax-h3-weight-inventory.json](../../../skill_library/repositories/h3-c/audit-h3-runtime-residency/references/minimax-h3-weight-inventory.json)
