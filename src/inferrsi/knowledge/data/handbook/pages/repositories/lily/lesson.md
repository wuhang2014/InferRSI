<!-- handbook
{
  "id": "lily",
  "kind": "procedure",
  "aliases": [
    "checkout:lily",
    "inferrsi.common.skills.lily",
    "package:inferrsi.common.skills.lily"
  ],
  "tags": [
    "lily",
    "rust",
    "metal",
    "apple-silicon",
    "mlx-affine-q4",
    "session-prefix",
    "numerical-validation",
    "benchmark-provenance"
  ]
}
-->

# Lily inference engineering

> Recorded state `candidate` · empirical validation `not_run` · license `NO_LICENSE` · [Source](../../../../skill_library/repositories/lily/SKILL.md) · [Scope and provenance](../../../../skill_library/repositories/lily/metadata.json) · [Catalog record](../../../../repo_packs/inferrsi/knowledge/common/skills/lily.json) · [Catalog revision](../../../../repo_packs/inferrsi/knowledge/_provenance.json) · [Parent reading](../../library/overview.md)

Investigate Lily's exact Qwen3.6-35B-A3B MLX-affine-Q4 contract, Metal state and kernels, strict greedy text API, token-prefix session cache and source-qualified validation or benchmark plans.

Use this source-derived candidate to investigate representation, state or
qualification questions in `perplexityai/pplx-garden/lily`. It is not a generic
Metal/MLX runner. Read [source and method provenance](references/repo-provenance.md)
before applying it to a different revision, model or device.

<a id="unit-route-the-question"></a>
## Route the question

| Question | Route | Expected result |
| --- | --- | --- |
| A nominally 4-bit model fails to load, or memory/sequence capacity is unclear | [model-runtime](sub-skills/model-runtime/lesson.md) | Exact architecture/layout and ownership/capacity contract |
| A request is rejected, or equal keys/history do not reuse state as expected | [serving-cache](sub-skills/serving-cache/lesson.md) | Strict API, token-prefix and state-lifetime diagnosis |
| CPU references look green, a golden is ignored, or MLX comparisons disagree | [qualification](sub-skills/qualification/lesson.md) | Matching native evidence, version and metric boundaries |

The focused routes bundle safe offline screening/request support where useful.
Those helpers do not invoke Rust, compile shaders, load tensors, tokenize a real
checkpoint or start inference. Their positive result is not native acceptance.

<a id="unit-establish-the-execution-tuple"></a>
## Establish the execution tuple

Record engine/source and Cargo lock/toolchain, macOS/chip/GPU family, exact
checkpoint and tensor payload identities, config/affine layout, tokenizer/chat
template and output-stop identity. Add sequence/output budgets, greedy policy,
input history, prefix-cache state, workload and quality/measurement requirements.

Equal nominal bit width, file size, API name or `prompt_cache_key` does not
identify equivalent tensors, rendered tokens or valid recurrent/KV state.
Separate reported benchmark identity from the checked-out runner's version.

<a id="unit-native-preparation-boundary"></a>
## Native preparation boundary

The source requires Rust 1.92, macOS 26 and Apple GPU family 10/M5 or newer.
For an authorized source build the public command is
`cargo build --release --locked`; shader source is compiled at runtime, not by
an offline metallib step. Inspect an installed binary's help before any model
run. Building a package does not supply its supported checkpoint or qualify it.

This extraction has neither Cargo/Rust nor a compatible Mac/model environment.
AREX's Python-package preparation was explicitly adapted to native Rust/Metal
identity and small offline helper checks. No installed Python distribution,
Rust test run or native backend success is fabricated.

<a id="unit-work-one-bounded-hypothesis"></a>
## Work one bounded hypothesis

1. Read the selected bundled contract and failure notes.
2. Resolve exact input representation and actual API semantics before tuning.
3. Trace owner, logical token frontier, allocation, cache key and release or
   restore boundary. Matching visible text is weaker than exact token identity.
4. Preserve the source's extra request lookahead slot when budgeting; do not
   replace its checked arithmetic with only prompt-plus-visible-output length.
5. Freeze workload, checkpoint/version, numerical/quality controls and metrics
   before comparing. Gates and campaign revisions belong in an acceptance issue.
6. Distinguish source inspection, offline helper checks, compiled native tests,
   real Metal operators, matched-model goldens and service measurements.

<a id="unit-stop-and-report"></a>
## Stop and report

Return exact source/model/device identity, observation, invariant, alternate
cause, smallest falsifier, actual check result and remaining gap. Stop at
unsupported format/API, missing compiler/backend/checkpoint, unfrozen gates or
the authorized budget. Do not install a toolchain, download a model, alter the
API or weaken an ignored/golden test merely to obtain a green result.

Required native compiler/Metal/model evidence remains blocked. CPU reference
functions and Python screening are not GPU test execution; skipped or ignored
cases do not become passing evidence. No quality, performance, service or
behavioral skill-efficacy qualification is claimed. Final partial-candidate
admission is a separate informed decision, not automatic import.

Source [Apache-2.0 license](../../../../skill_library/repositories/lily/LICENSE) and [NOTICE](../../../../skill_library/repositories/lily/NOTICE.md) are retained.
`NO_LICENSE` is the actual AREX unauthenticated-CLI fallback, not a legal finding;
model weights and third-party material retain their own obligations.

<a id="unit-when-this-applies"></a>
## When this applies

- **Scope** — Exact Lily source/checkpoint/layout/API/cache/qualification investigation; common catalog classification is not CPU inference or cross-device support.
- **Prerequisites** — Access to the exact Lily source/model-layout/API contracts; native checks require the matching Rust/Metal/checkpoint environment and frozen comparison requirements.
- **Input contract** — Source revision, Cargo lock/toolchain, macOS/chip/GPU family, checkpoint and tensor payload identities, affine configuration/layout, tokenizer/template/stops, sequence/output budgets, greedy policy, input history, prefix-cache state and quality/measurement requirements.
- **Produced artifact** — A source/model/device-bound representation, serving-cache or qualification diagnosis with the observation, invariant, alternate cause, smallest falsifier, actual result and remaining native gap.
- **Failure modes** — Equal bit width, file size, API names or prompt_cache_key do not establish tensor/token/state equivalence; ignoring the extra lookahead slot can understate request capacity, and green CPU references do not replace matched-model Metal goldens.
- **Refusal point** — Stop at unsupported formats/APIs, missing compiler/backend/checkpoint, unfrozen gates or the authorized budget; do not weaken ignored/golden tests to obtain a green result.

<a id="unit-putting-the-idea-to-work"></a>
## Putting the idea to work

- Resolve exact affine representation and strict API semantics, then trace token frontier, cache key and restore/release ownership.
- Retain the source's extra request lookahead slot in capacity arithmetic rather than counting only prompt and visible output.
- Separate reported benchmark version from the checked-out runner and distinguish offline screening, native compilation, Metal operators and matched-model goldens.

<a id="unit-limits-of-this-evidence"></a>
## Limits of this evidence

- Cargo/Rust1.92, supported M5/macOS26/Metal and model resources are unavailable; native evidence remains BLOCKED_REQUIRED_BACKEND.
- Offline Python helper checks are not Rust serde/loader/tokenizer, native kernel/state/cache, model quality, service or performance validation.
- Current benchmark source and later report have distinct package/harness identities; negative long-context prefill observations remain author-reported.
- Only selected source bodies are mined; complete kernel/format/platform/failure coverage and behavioral skill efficacy remain unverified.
- NO_LICENSE is the actual unauthenticated GitHub CLI fallback, not a legal conclusion; lily Apache-2.0 LICENSE and NOTICE are independently retained.

<a id="unit-source-files"></a>
## Source files

- [LICENSE](../../../../skill_library/repositories/lily/LICENSE)
- [NOTICE.md](../../../../skill_library/repositories/lily/NOTICE.md)
- [metadata.json](../../../../skill_library/repositories/lily/metadata.json)
- [references/repo-routing-metadata.json](../../../../skill_library/repositories/lily/references/repo-routing-metadata.json)
- [references/source-identity.json](../../../../skill_library/repositories/lily/references/source-identity.json)
