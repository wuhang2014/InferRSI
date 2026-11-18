<!-- handbook
{
  "id": "splash",
  "kind": "procedure",
  "aliases": [
    "checkout:splash",
    "inferrsi.common.skills.splash",
    "package:inferrsi.common.skills.splash"
  ],
  "tags": [
    "splash",
    "apple-silicon",
    "metal",
    "ane",
    "dflash2",
    "memory-plan",
    "prefix-cache",
    "persistent-cache"
  ]
}
-->

# Splash inference engineering

> Recorded state `candidate` · empirical validation `partial_cpu_only` · license `NO_LICENSE` · [Source](../../../../skill_library/repositories/splash/SKILL.md) · [Scope and provenance](../../../../skill_library/repositories/splash/metadata.json) · [Catalog record](../../../../repo_packs/inferrsi/knowledge/common/skills/splash.json) · [Catalog revision](../../../../repo_packs/inferrsi/knowledge/_provenance.json) · [Parent reading](../../library/overview.md)

Investigate Splash model-format compatibility, automatic memory planning, Metal and ANE execution, DFlash2 verification, cache and request identity, and correctness-gated serving measurements.

Use this source-derived candidate to diagnose an inference or serving question,
select a bounded change and state the check that could falsify it. It is not a
complete upstream manual or a certified Apple backend recipe. Read
[source and method provenance](references/repo-provenance.md) before reuse.

<a id="unit-route-the-work"></a>
## Route the work

| Question | Route | Expected result |
| --- | --- | --- |
| A format is rejected, a model will not fit or a cache cap is surprising | [runtime-planning](sub-skills/runtime-planning/lesson.md) | Compatible representation and memory-owner ledger |
| Prefix reuse, persistent cache, request isolation or Responses history is confusing | [serving-cache](sub-skills/serving-cache/lesson.md) | Identity, state-lifetime, admission and recovery ledger |
| Draft acceptance rises but speed/answers change; an ANE or precision path differs | [qualification](sub-skills/qualification/lesson.md) | Semantic control, actual path and matching proof ladder |

Use the bundled [request builder](../../../../skill_library/repositories/splash/scripts/request_template.py) to prepare a
small Chat Completions body offline. It prints JSON; it never contacts a server,
installs Splash, launches a client or downloads a model. Its deliberately small
option set is not the complete upstream API.

<a id="unit-establish-the-execution-tuple"></a>
## Establish the execution tuple

Record source/build revision, macOS and Apple device, target checkpoint/format/
quantization and artifact identity, compatible draft, tokenizer/template and
vision selection. Add context, cache/memory controls, KV and recurrent-state
precision, ANE setting, verifier-row policy, concurrency/priority, sampling,
prompt/output/quality controls and cold/warm/persistent-cache state.

An API model alias is not a new weight selection. Equal bit width does not
prove loader/kernel compatibility. A seeded request does not freeze cache,
batch/chunk or adaptive-verification scheduling.

<a id="unit-native-preparation-boundary"></a>
## Native preparation boundary

The source targets Apple Silicon M3 or newer and macOS 26.4 or later. The public
release installation is `brew install incoai/tap/splash`; an authorized operator
can inspect `splash serve --help` before loading anything. Installation and
serving are separate actions: the normal serve path can download target/draft
weights. Do not run it solely to inspect an option.

Splash is a native Metal/C++ runtime with Python server/installer modules, not
a pip-installable project. This extraction adapted AREX's package inspection
to isolated, explicit source-module identity/signature checks. Linux Python
logic does not validate the actual Metal/ANE/model path.

<a id="unit-work-a-bounded-hypothesis"></a>
## Work a bounded hypothesis

1. Read the selected route and nearest bundled mechanism/failure reference.
2. Separate source observation, upstream measurement and proposed experiment.
3. Identify representation, owner, validity key, lifetime and reclaim/rollback
   boundary before tuning a numeric control.
4. Freeze workload, semantic reference and measurement boundaries before a
   comparison. Keep campaign pins and gates in the acceptance issue.
5. Confirm the path actually activated; retain fallbacks, admission waits,
   evictions, cancellations and errors instead of treating them as warmup noise.
6. Correctness and model quality precede ranking. A cache/parser/codec check
   cannot establish GPU state, a distributional guarantee or service SLOs.

<a id="unit-stop-and-report"></a>
## Stop and report

Return execution identity, observation, source-backed invariant, alternate
explanation, smallest discriminating check, actual result and unresolved gap.
Stop at unsupported formats, unavailable backend/model resources, unsafe service
exposure or the authorized budget. Do not change system settings or launch an
external coding client merely because imported guidance mentions one.

Required Metal/ANE/model/actual disk-state evidence remains
**BLOCKED_REQUIRED_BACKEND**. Source and CPU checks do not qualify performance,
quality, service operation or behavioral skill efficacy. Final admission of a
partially verified candidate requires an informed decision, not auto-import.

The source [Apache-2.0 license](../../../../skill_library/repositories/splash/LICENSE) and
[third-party notices](../../../../skill_library/repositories/splash/THIRD_PARTY_NOTICES) are retained. `NO_LICENSE` is the
actual AREX resolver's unauthenticated-CLI warning fallback, not a legal finding;
models and external tools retain their own licenses.

<a id="unit-when-this-applies"></a>
## When this applies

- **Scope** — Pinned Splash representation, planning, state/serving and verification investigation; common discovery does not qualify a different Mac/model/backend.
- **Prerequisites** — Access to the pinned representation/planning, serving-cache or qualification route; native checks need matching Apple/backend/model resources, an authorized workload and frozen semantic/measurement controls.
- **Input contract** — Source/build, macOS/device, target and compatible draft artifacts/formats, tokenizer/template/vision selection, context/cache/memory controls, KV/recurrent precision, ANE and verifier-row policy, concurrency/priority/sampling, quality controls and cache state.
- **Produced artifact** — An execution-identity report with observation, source-backed invariant, alternate explanation, smallest discriminating check, actual result and unresolved Metal/ANE/model/disk-state gap.
- **Failure modes** — Treating an API alias as new weights, equal bit width as loader/kernel compatibility, or a fixed seed as fixed cache/batch/adaptive-verification scheduling can invalidate the comparison; CPU cache/codec checks do not prove GPU state.
- **Refusal point** — Stop at unsupported formats, unavailable backend/model resources, unsafe service exposure or the authorized budget.

<a id="unit-putting-the-idea-to-work"></a>
## Putting the idea to work

- Resolve representation, memory/cache owner, validity key and reclaim/rollback boundary before tuning a numeric control.
- Freeze semantic and workload controls beyond the seed, and retain actual-path fallbacks, admission waits, evictions, cancellations and errors.
- Inspect options without starting the normal serve path, which can download target/draft weights; installation and serving require separate task authority.

<a id="unit-limits-of-this-evidence"></a>
## Limits of this evidence

- Required Metal/ANE/model/actual device and disk-state execution remains BLOCKED_REQUIRED_BACKEND; Python policy/codec checks do not clear it.
- Service performance, quality, native recurrent-state recovery and skill efficacy remain unverified.
- Only selected bodies were mined; not all formats, kernels, supported devices or release/client workflows.
- NO_LICENSE is the actual unauthenticated GitHub CLI resolver fallback, not a legal conclusion; Apache-2.0 and third-party notices are retained.

<a id="unit-source-files"></a>
## Source files

- [LICENSE](../../../../skill_library/repositories/splash/LICENSE)
- [THIRD_PARTY_NOTICES](../../../../skill_library/repositories/splash/THIRD_PARTY_NOTICES)
- [metadata.json](../../../../skill_library/repositories/splash/metadata.json)
- [references/repo-routing-metadata.json](../../../../skill_library/repositories/splash/references/repo-routing-metadata.json)
- [references/source-identity.json](../../../../skill_library/repositories/splash/references/source-identity.json)
- [scripts/request_template.py](../../../../skill_library/repositories/splash/scripts/request_template.py)
