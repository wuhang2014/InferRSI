<!-- handbook
{
  "id": "repositories/mistral-rs/references/scope-and-notices",
  "kind": "reference",
  "tags": [
    "mistral-rs",
    "metal",
    "candle",
    "paged-attention",
    "cache-layout",
    "prefill-metadata",
    "workspace",
    "prewarm",
    "native-evidence"
  ]
}
-->

# Scope, negative boundaries and attribution

> Recorded state `candidate` · empirical validation `not_run` · license `NO_LICENSE` · [Source](../../../../../skill_library/repositories/mistral-rs/references/scope-and-notices.md) · [Scope and provenance](../../../../../skill_library/repositories/mistral-rs/metadata.json) · [Parent reading](../lesson.md)

<a id="unit-selected-coverage"></a>
## Selected coverage

| Surface | Depth and limit |
| --- | --- |
| Decode layout/scale/specialization/workspace | Selected substantive Rust owner/consumer, MSL grouped consumer and test definitions; static metadata support only |
| Prefill metadata/positions/masks/workspace | Substantive host request parser and common MSL coordinate/mask consumer, selected native assertions and strict offline metadata/formula support |
| Actual-model prewarm and qualification | Model-derived device/layer/dtype/feature/limit routing, pipeline cache/preparation and source native-test evidence; no actual preparation/dispatch |
| Scheduler/prefix allocation/model memory | Narrow layout/default/caller context only; full scheduler admission, preemption/reuse/prefix manager and physical allocator audit excluded |
| Models/formats/quantization/MoE/multimodal | Selected attention feature boundaries only; no complete model catalog, loader/weight conversion, quantization quality or modality qualification |
| CLI/server/agents/tools/LoRA/distributed/CUDA | Named upstream surfaces, not extracted operating recipes; no service/tool execution, CUDA transfer of Metal claims or transport/performance qualification |

The graph is intentionally focused, not a claim to cover every public engine
capability. A generic neighboring attention API is not evidence for omitted
models or routes. No native numerical, memory-fit, model quality, service gain
or comparative skill-efficacy experiment has run.

<a id="unit-licenses-remain-source-specific"></a>
## Licenses remain source-specific

The source root [MIT LICENSE](../../../../../skill_library/repositories/mistral-rs/LICENSE) is retained unchanged. The component
[Apache-2.0 license](../../../../../skill_library/repositories/mistral-rs/references/apache-component-license.md) and
[paged-attention notice](../../../../../skill_library/repositories/mistral-rs/references/paged-component-notice.md) are also retained unchanged
under descriptive Markdown basenames so they ship as package resources. Their
original names and hashes are in the [source identity](../../../../../skill_library/repositories/mistral-rs/references/source-identity.json).
Root MIT does not erase the notice's identified Apple/Candle/MLX-derived
attention portions. No vendor kernel or model assets are copied into this graph.

New helper code retains its own declared license and source attribution. Runtime
API/schema validation is newly authored support, not an invented upstream
helper command. Dependency, tokenizer/model, generated/prebuilt artifact and
optional component rights remain separate from source licenses.

Every SKILL.md uses `license: NO_LICENSE` because the actual AREX GitHub CLI
resolver was unauthenticated and could not return an API SPDX value for this
pin. This is a warning fallback, not a legal conclusion that no license exists,
and does not replace independently retained source notices.

Source examples can instantiate models, access external assets or require
credentials; broad tests and installation scripts may fetch/build dependencies.
They are provenance-only here, not runtime checkout dependencies or permission
to execute. Use explicit synthetic inputs in bundled helpers. Do not capture
private paths, credentials, prompts or cache contents in shared reports.
