<!-- handbook
{
  "id": "mlc-llm",
  "kind": "procedure",
  "aliases": [
    "checkout:mlc-llm",
    "inferrsi.common.skills.mlc_llm",
    "package:inferrsi.common.skills.mlc_llm"
  ],
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

# MLC LLM compiled Metal and runtime contracts

> Recorded state `candidate` · empirical validation `not_run` · license `NO_LICENSE` · [Source](../../../../skill_library/repositories/mlc-llm/SKILL.md) · [Scope and provenance](../../../../skill_library/repositories/mlc-llm/metadata.json) · [Catalog record](../../../../repo_packs/inferrsi/knowledge/common/skills/mlc-llm.json) · [Catalog revision](../../../../repo_packs/inferrsi/knowledge/_provenance.json) · [Parent reading](../../library/overview.md)

Investigate MLC LLM compiled Metal artifact/schema, Apple target and pinned TVM module/storage/stream contracts, and compile/runtime KV limits without confusing canonical metadata, codegen or automatic estimates with runnable native model qualification.

Use this source-derived **candidate** for the boundary between model-package
metadata, compiled target artifacts and real native runtime behavior. Begin
with [source identity](references/repo-provenance.md). MLC and its exact TVM
fork/gitlink are separate source owners; an arbitrary newer TVM is not an
interchangeable implementation.

<a id="unit-route-by-the-failed-contract"></a>
## Route by the failed contract

| Question | Canonical owner |
| --- | --- |
| Do normalized tasks, parameter schema, executor/adapter roles and parameter-only resources agree? | [artifact-contract](sub-skills/artifact-contract/lesson.md) |
| Do target/host/SDK/suffix/prefix, payload format, runnable module and selected storage/stream agree? | [metal-build-runtime](sub-skills/metal-build-runtime/lesson.md) |
| Which compiled/runtime limit or workspace input is actually controlling the KV path? | [runtime-kv-limits](sub-skills/runtime-kv-limits/lesson.md) |
| What remains outside these source contracts, including rights and native evidence? | [scope and notices](references/scope-and-notices.md) |

<a id="unit-establish-the-actual-boundary"></a>
## Establish the actual boundary

1. Record MLC revision, TVM gitlink/build, model/tokenizer/quantized parameter
   identity, target/host/SDK, compiled artifact/format and runtime device. A
   canonical interface or parameter-schema hash does not hash tensor bytes,
   authenticate exports, select a device or prove native consumer support.
2. Identify which consumer implements the interface. The inspected artifact
   manifest is **opt-in**, first consumed by WebLLM. The native engine does not
   consume that contract at this pin; a valid sidecar cannot imply native
   support for its model/task ABI.
3. Separate metadata checks, IR/codegen, serialization/export, real runtime
   factory/load, pipeline creation, dispatch, stream completion, numerical
   behavior and model/service results. Each requires distinct evidence. A
   serializable kind=metal fallback is explicitly non-runnable.
4. Follow actual compiled metadata and configuration sources. Runtime preference,
   compile-time bound, nested workspace shape and explicit engine override are
   different values. The Metal working-set attribute and automatic-capacity
   constants do not establish free memory, safe allocation or universal limits.
5. Use only the selected bundled standard-library helper on explicit synthetic
   or anonymized declarations. Helpers do not import MLC/TVM, run Pydantic,
   initialize submodules, inspect weights/binaries, invoke a compiler or probe a
   device. Their narrow domains are not complete upstream input validators.

<a id="unit-native-preparation-and-evidence-limits"></a>
## Native preparation and evidence limits

The source pyproject declares 0.20.0.dev0; no installed package/build is implied.
MLC's native Python package loads TVM/serving integration, and original artifact
tests also import TVM DataType/model definitions and Pydantic. Even apparently
pure schema/codegen/IR tests require the actual prepared native stack. A
standalone Python declaration helper is not that stack or a passing source test.

This graph ships no installer, model-loading recipe or checkout-dependent source
test command. Compiler/native tests require separately prepared, version-matched
MLC/TVM/FFI dependencies and Apple SDK/device where applicable; broad compile or
integration loops can exercise many models and are not small default checks.
No compiler/live API/CLI/original source test or actual Metal/model execution is
claimed. Required native evidence remains `BLOCKED_REQUIRED_BACKEND / not_run`.

Return identities, actual versus declared facts, route/invariant, negative
signal and smallest missing native discriminator. Candidate empirical validation
is `not_run`. Helper, source hash, packaging or generic compile success does not
qualify cache correctness, physical fit, model quality, latency/service gains or
broad skill efficacy. No portable acceptance bar is derived from source test
constants or implementation crossover/capacity values.

<a id="unit-when-this-applies"></a>
## When this applies

- **Scope** — Selected artifact/Apple target/pinned TVM Metal consumer and KV configuration source contracts. Common catalog categorization is not CPU inference or Apple qualification.
- **Prerequisites** — Access to the pinned MLC and exact TVM fork/gitlink contracts; native checks require separately prepared matching MLC/TVM/FFI and the applicable Apple SDK/device stack.
- **Input contract** — MLC revision, TVM gitlink/build, model/tokenizer/quantized-parameter identity, target/host/SDK, compiled artifact/format, runtime device and the actual compiled/runtime configuration sources.
- **Produced artifact** — An identity and actual-versus-declared boundary report for artifact, Metal runtime or KV-limit ownership, with a negative signal and smallest missing native discriminator.
- **Failure modes** — Treating a schema hash as payload authentication, an opt-in WebLLM artifact contract as a native-engine ABI, serializable Metal fallback as runnable, or automatic capacity estimates as free memory can create unsupported qualification claims.

<a id="unit-putting-the-idea-to-work"></a>
## Putting the idea to work

- Identify the interface's actual consumer before using a valid artifact manifest as evidence of native model/task support.
- Separate codegen/export from runtime factory/load, pipeline creation, dispatch and stream completion; a serializable kind=metal fallback can still be non-runnable.
- Trace runtime preference, compile-time bounds, nested workspace inputs and explicit overrides separately before interpreting a KV or working-set estimate.

<a id="unit-limits-of-this-evidence"></a>
## Limits of this evidence

- Source-derived candidate; original compiled CPU/native tests, compiler/live API/CLI/model/Metal/fit/quality/service/performance execution not_run; required native BLOCKED_REQUIRED_BACKEND.
- Opt-in artifact manifest first targets WebLLM; native engine ignoring that ABI is not qualified by canonical metadata agreement.
- Serializable kind=metal fallback can be non-runnable; codegen/export/pipeline/submission and actual load/dispatch/completion differ.
- Helpers screen narrow explicit canonical metadata, literal target strings or limit clamping only; no general Pydantic/TVM emulation, actual tensor/weight/export authentication or GPU/memory simulation.
- Full model/tokenizer/quantization/VLM/RNN/speculation/disaggregation/CUDA/scheduler/dependency implementation and broad skill efficacy remain outside selected contracts.
- NO_LICENSE is unavailable machine SPDX metadata, not legal absence; both source owners Apache LICENSE/NOTICE bytes are independently retained.

<a id="unit-source-files"></a>
## Source files

- [LICENSE](../../../../skill_library/repositories/mlc-llm/LICENSE)
- [metadata.json](../../../../skill_library/repositories/mlc-llm/metadata.json)
- [references/mlc-notice.md](../../../../skill_library/repositories/mlc-llm/references/mlc-notice.md)
- [references/repo-routing-metadata.json](../../../../skill_library/repositories/mlc-llm/references/repo-routing-metadata.json)
- [references/source-identity.json](../../../../skill_library/repositories/mlc-llm/references/source-identity.json)
- [references/tvm-license.md](../../../../skill_library/repositories/mlc-llm/references/tvm-license.md)
- [references/tvm-notice.md](../../../../skill_library/repositories/mlc-llm/references/tvm-notice.md)
