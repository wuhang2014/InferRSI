<!-- handbook
{
  "id": "audit-h3-runtime-residency",
  "kind": "procedure",
  "aliases": [
    "checkout:audit-h3-runtime-residency",
    "inferrsi.common.skills.audit_h3_runtime_residency",
    "package:inferrsi.common.skills.audit_h3_runtime_residency"
  ],
  "tags": [
    "h3.c",
    "MiniMax-H3",
    "apple-silicon",
    "metal",
    "diffusion",
    "video",
    "audio",
    "multimodal-conditioning",
    "adaln",
    "model-residency",
    "ssd-streaming",
    "int8",
    "bf16"
  ]
}
-->

# Audit h3.c runtime residency and numerical paths

> Recorded state `candidate` · empirical validation `not_run` · license `MIT` · [Source](../../../../../skill_library/repositories/h3-c/audit-h3-runtime-residency/SKILL.md) · [Scope and provenance](../../../../../skill_library/repositories/h3-c/audit-h3-runtime-residency/metadata.json) · [Catalog record](../../../../../repo_packs/inferrsi/knowledge/common/skills/audit-h3-runtime-residency.json) · [Catalog revision](../../../../../repo_packs/inferrsi/knowledge/_provenance.json) · [Parent reading](../../../library/overview.md)

Audit MiniMax-H3 generation in h3.c on Apple Silicon by tracing conditioning, AdaLN precompute, DiT residency, Metal precision paths, SSD streaming and audio/video decoding.

Source-derived candidate for `antirez/h3.c` at
`8974cc055ea9c02fcd14cc27dfda3e1027c05153`. Use for MiniMax-H3
text/image/video/audio conditioning, memory-fit diagnosis, kernel changes or a
dedicated-engine design derived from this C/Metal runtime. Start with the
[source readset and architecture](references/source-notes.md). Native execution,
media quality, performance and behavioral skill efficacy are **not_run**.

<a id="unit-inputs-and-decision"></a>
## Inputs and decision

Record the runtime revision/patches, macOS/SDK/GPU, memory budget, selected FL2VA
or Ref2VA checkpoint and complete component/format inventory. Freeze the prompt,
ordered reference media, requested and aligned frames, output/internal canvas,
steps, seed, layer/reuse/token policies, all precision controls, preview and
interactive-cache state. An installed engine name or a successful metadata load
does not identify this execution configuration.

Produce a phase ledger and one smallest discriminating check. The useful output
is a supported cause, invariant, counter-explanation and falsifier; model-file
bytes alone do not decide whether a workload fits unified memory.

<a id="unit-procedure"></a>
## Procedure

1. **Resolve the executing pipeline.** Follow `h3_generate` through the
   [phase ledger](references/phase-residency.md). Ordered references select the
   separate Ref2VA DiT; FL2VA first/last-frame conditioning still needs both the
   video input encoder and the Qwen vision/language path. Audio conditioning and
   audio output decoding are different calls. Count the selected input and
   output components without adding alternative checkpoints or repeated shared
   files. Use the [retained weight inventory](../../../../../skill_library/repositories/h3-c/audit-h3-runtime-residency/references/minimax-h3-weight-inventory.json)
   for its exact checkpoint selections, not as a universal model-size constant.
2. **Check representation before capacity.** The raw loader validates exact
   names, rank, shape and BF16/F32 dtype. Runtime symmetric int8 conversion is
   different from loading MLX affine `U32` bundles. A smaller published bundle
   needs a compatible engine or an explicit conversion; matching bit width is
   insufficient. Keep header validity and payload integrity separate.
3. **Trace ownership across phases and requests.** Distinguish host embeddings,
   media/latent/output buffers, shared Metal tensors, file-backed mappings,
   AdaLN tables and prepared-model/decoder caches. In the one-shot path the DiT
   is freed before decoding; preview and interactive retention can overlap
   phases. Audit cache keys and clear/reset boundaries before diagnosing a leak
   or assuming a warm request has cold-request memory behavior.
4. **Preserve the schedule contract.** AdaLN tables are indexed by the actual
   video/audio schedule, conditioning presence, modality tags and layout.
   Each projection is submitted and released before loading the next. Rebuild
   when those dependencies change; do not replace conditioning timesteps or
   collapse audio/video rows because their step counts match. See the
   [schedule and cache invariants](references/phase-residency.md#unit-adaln-and-prepared-state).
5. **Classify every numerical change.** Follow
   [precision and streaming](references/precision-and-streaming.md). Separate
   BF16-preserving fusions from int8 approximation, BF16 output-head conversion,
   layer thinning, velocity/core reuse, token reduction and internal-canvas/RoPE
   changes. On M5, 50 layers and `--reuse 1` still allow default int8 paths.
   Select the explicit BF16 controls and F32-head diagnostic when that is the
   frozen reference. A kernel parity result is not full audio/video quality.
6. **Choose the residency tradeoff that addresses the measured phase.** Qwen
   prefetch overlaps current-layer compute with future-layer reads and increases
   resident buffers. Mapped persistent DiT weights remain file-backed; explicit
   SSD mode instead rotates two BF16 matrix slots and disables int8. It changes
   I/O and command boundaries. Reducing DiT residency will not resolve a VAE,
   reference-media or host-output peak. Track physical/compressed/swap memory
   alongside tensor counters and storage reads.
7. **Run the matching check when resources exist.** The
   [validation recipe](references/validation.md) maps native targets, required
   fixtures and proposed probes to these invariants. Preserve skipped fixtures,
   startup/first/warm timing, both output modalities and all failed trials.
   The [Apple feasibility comparison](references/minimax-h3-apple.md) is retained
   imported research; neither its upstream measurements nor packaged-reader
   tests qualify a new Mac, workload or 64 GiB memory budget.

<a id="unit-report-and-stop"></a>
## Report and stop

Return a table with `phase`, `component and format`, `owner`, `resident weights`,
`runtime/host buffers`, `overlap`, `release or reuse boundary`, and
`observation/unknown`; then the exact check, actual outcome and remaining gap.
Stop at unavailable model/fixture/backend resources or the accepted experiment
budget. Reading this skill does not install an engine, download weights, run a
distiller, authorize a campaign or promote this candidate. Missing target
evidence remains unverified/INCONCLUSIVE.

<a id="unit-when-this-applies"></a>
## When this applies

- **Scope** — MiniMax-H3 joint audio/video C/Metal runtime audit: raw checkpoint compatibility, input encoders, schedule precompute, phased/cached residency, numerical controls and SSD streaming on Apple Silicon. Common catalog placement is a discovery classification, not cross-backend qualification.
- **Prerequisites** — Access to the pinned source architecture and selected component/format inventory; native checks need matching model, fixture and backend resources within an authorized experiment budget.
- **Input contract** — Runtime revision/patches, macOS/SDK/GPU and memory budget, FL2VA/Ref2VA selection, component formats, prompt and ordered media, requested/aligned frames, canvases, steps/seed, layer/reuse/token/precision policies and preview/interactive-cache state.
- **Produced artifact** — A phase/component/owner ledger with resident weights, runtime/host buffers, overlap, release/reuse boundaries and observations/unknowns, followed by a discriminating check, actual result and remaining gap.
- **Failure modes** — Estimating fit from model-file bytes, confusing runtime int8 with incompatible MLX bundles, ignoring preview/cache overlap, or reducing DiT residency to address a VAE/host-output peak can produce a wrong capacity diagnosis.
- **Refusal point** — Stop at unavailable model/fixture/backend resources or the accepted experiment budget; missing target evidence remains unverified/INCONCLUSIVE.

<a id="unit-putting-the-idea-to-work"></a>
## Putting the idea to work

- Resolve the actual conditioning and output components before counting residency; do not add alternative checkpoints or count shared files twice.
- Trace one-shot, preview and interactive ownership separately, including AdaLN schedule dependencies and prepared-cache reset boundaries.
- Classify approximation and precision controls before comparison, then measure the relevant phase with tensor, physical/compressed/swap and storage observations.

<a id="unit-limits-of-this-evidence"></a>
## Limits of this evidence

- Native h3.c/Metal execution, target peak memory, audio/video quality, performance, service behavior and skill efficacy were not run.
- Only the bounded readset was inspected; complete kernel, driver/MPSGraph, tokenizer, FFmpeg, concurrent-caller and failure-path coverage is not established.
- The retained inventory authenticates only prior JSON header observations, not weight payloads; full official versus selected truncated/packed export inventories are distinct.
- Upstream 128 GB M5 Max results and tracked DiT bytes do not qualify a 64 GiB target, a different workload or total physical memory.
- MIT covers the h3.c source; retained BSD-3-Clause notices and independent model/export/tool licenses remain separate. UNKNOWN source-license fields are unresolved.

<a id="unit-source-files"></a>
## Source files

- [LICENSE](../../../../../skill_library/repositories/h3-c/audit-h3-runtime-residency/LICENSE)
- [metadata.json](../../../../../skill_library/repositories/h3-c/audit-h3-runtime-residency/metadata.json)
- [references/minimax-h3-weight-inventory.json](../../../../../skill_library/repositories/h3-c/audit-h3-runtime-residency/references/minimax-h3-weight-inventory.json)
- [references/source-identity.json](../../../../../skill_library/repositories/h3-c/audit-h3-runtime-residency/references/source-identity.json)
