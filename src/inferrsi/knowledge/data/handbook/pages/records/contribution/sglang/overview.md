<!-- handbook
{
  "id": "records/contribution/sglang/overview",
  "kind": "guide"
}
-->

# SGLang knowledge

> [Source](../../../../../repo_packs/sglang/knowledge/README.md)

Named JSON records are retrieval abstracts with source attribution, conditions,
validation plans and explicit verification state. The complete English skills
provide the detailed procedures and evidence maps; they are not per-entry
Markdown copies of the catalog records.

Full library: [English skill](../../../repositories/sglang/lesson.md).

All entries are imported guidance with `locally_verified=false`. `common` means
backend-independent guidance within this repository, not verified backend
support. The pack uses caller-supplied external commands and supplies no model
launcher. GPU/NPU execution, model quality and performance need separate
target-environment evidence.

<a id="unit-entries"></a>
## Entries

| Component | Record |
| --- | --- |
| llm | [SGLang scheduler, RadixCache and HiCache state ownership](common/llm/runtime-radix-hicache.md) |
| llm | [SGLang TP/DP/EP, PD transfer and extension ownership](common/llm/parallelism-and-extension.md) |
| llm | [SGLang controlled tuning and model-quality gates](common/llm/tuning-and-validation.md) |

<a id="unit-maintenance"></a>
## Maintenance

Keep IDs stable and add a navigation row for every record. Retain pinned source
attribution and limitations; omit PR links. Keep detailed procedures in the
linked full skills, and update abstracts when their source contracts change.
Catalog or CPU tests do not promote imported guidance to validated runtime
evidence. Follow the shared [knowledge maintenance contract](../vllm_omni/overview.md#unit-maintaining-the-pack).
