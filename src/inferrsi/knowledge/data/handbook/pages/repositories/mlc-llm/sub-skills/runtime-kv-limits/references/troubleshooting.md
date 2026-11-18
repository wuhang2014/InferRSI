<!-- handbook
{
  "id": "repositories/mlc-llm/sub-skills/runtime-kv-limits/references/troubleshooting",
  "kind": "reference",
  "tags": [
    "mlc-llm",
    "tvm",
    "metal",
    "artifact-contract",
    "target",
    "sdk",
    "module",
    "stream",
    "kv-cache",
    "compiled-limits"
  ]
}
-->

# Limit and cache troubleshooting

> Recorded state `candidate` · empirical validation `not_run` · license `NO_LICENSE` · [Source](../../../../../../../skill_library/repositories/mlc-llm/sub-skills/runtime-kv-limits/references/troubleshooting.md) · [Scope and provenance](../../../../../../../skill_library/repositories/mlc-llm/metadata.json) · [Parent reading](../lesson.md)

| Symptom | First check | Recovery or stop |
| --- | --- | --- |
| Runtime context/prefill exceeds a compiled model | Per-model clamp before cross-model minimum | Reconcile exact metadata/config; a helper does not modify native configuration |
| All compiled prefill declarations are unspecified | Required finite aggregate assertion | Supply actual compiled evidence; do not invent a finite native default |
| Lower runtime prefill did not reduce reserved memory | Nested compiled workspace prefill | Compare compiled artifact/allocation provenance; do not equate preference with shape change |
| Metal working-set number treated as free memory | DeviceAPI attribute and other allocations | Preserve estimator assumptions; require actual pressure/allocation evidence |
| Explicit capacity above automatic cap called impossible | Automatic versus explicit branch | Inspect full override validation; do not promote an auto choice into universal admission |
| A cache IR name is offered as FlashInfer proof | Target-specific lowering and CUDA gates | Metal TIR path and native route need their own evidence |
| Structural IR/compile test is called cache parity | Exact assertion type and actual device | Stop the numerical/model/service claim until real matched execution |

Return source/config identities, conflicting value origins, bounded declaration
result and remaining native evidence. Do not repair the engine, fetch a model or
start a service merely to inspect this graph.
