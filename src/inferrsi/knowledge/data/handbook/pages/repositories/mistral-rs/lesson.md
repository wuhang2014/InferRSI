<!-- handbook
{
  "id": "mistral-rs",
  "kind": "procedure",
  "aliases": [
    "checkout:mistral-rs",
    "inferrsi.common.skills.mistral_rs",
    "package:inferrsi.common.skills.mistral_rs"
  ],
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

# mistral.rs Metal paged-attention contracts

> Recorded state `candidate` · empirical validation `not_run` · license `NO_LICENSE` · [Source](../../../../skill_library/repositories/mistral-rs/SKILL.md) · [Scope and provenance](../../../../skill_library/repositories/mistral-rs/metadata.json) · [Catalog record](../../../../repo_packs/inferrsi/knowledge/common/skills/mistral-rs.json) · [Catalog revision](../../../../repo_packs/inferrsi/knowledge/_provenance.json) · [Parent reading](../../library/overview.md)

Investigate mistral.rs Metal paged-attention decode layouts, prefill coordinates and workspace, actual-model prewarm and native test evidence without treating static metadata or prepared pipelines as executed GPU correctness or performance.

Use this source-derived **candidate** for the Rust/Candle engine's native Metal
paged-attention path. It is a focused repository operating graph, not a generic
model catalog, a deployment guide or a verified engine. Read
[source and method provenance](references/repo-provenance.md) before using it on
a different checkout. Reading it does not authorize installation or execution.

<a id="unit-route-by-the-failed-contract"></a>
## Route by the failed contract

| Question | Canonical owner |
| --- | --- |
| Does HND/packed K/V, FP8 scale, GQA/head geometry, sliding decode or scratch agree? | [decode-contract](sub-skills/decode-contract/lesson.md) |
| Do packed/padded queries, absolute positions, masks/ranges and prefill workspace agree? | [prefill-contract](sub-skills/prefill-contract/lesson.md) |
| Did model warmup prepare the intended pipelines, and what did native tests actually prove? | [qualification](sub-skills/qualification/lesson.md) |
| Which other engine features, dependencies and licenses are outside this extraction? | [scope and notices](references/scope-and-notices.md) |

The selected source owns Rust shape/configuration/consumer code and actual MSL
attention, rather than merely naming an external backend. Candle supplies the
tensor/device integration. Shared ancestry with other Metal engines does not
make their cache layouts, scratch planners or synchronization interchangeable.

<a id="unit-establish-identity-before-proposing-a-change"></a>
## Establish identity before proposing a change

1. Record exact mistral.rs/Candle/native artifact revisions, Rust toolchain,
   Apple SDK/OS/device, actual model/cache dtype and representation, shape,
   strides/offsets, block table, context and execution limits. Model and asset
   identities are separate from source version or advertised support.
2. Identify the producer, view and native consumer of cache/metadata bytes.
   Equal element counts, a layout setting and physical alias identity differ.
   Decode and prefill deliberately have different supported geometry domains.
3. Select the smallest matching sub-skill and its bundled helper. Helpers use
   explicit synthetic/caller-declared JSON and Python standard library only.
   They do not import an engine, compile Rust, read weights, allocate device
   memory, emulate GPU computation or establish native eligibility.
4. Separate a static source predicate, pipeline preparation, actual kernel
   dispatch, numerical correctness, model quality and service performance.
   None automatically implies the next. Preserve unsupported cases, failed
   observations, skipped/gated tests and required missing evidence.
5. For an actual change or experiment, obtain its separate authority, freeze
   controls/acceptance gates and select discriminating native references before
   running it. Do not use source crossover constants or test tolerances as
   portable performance/quality acceptance bars.

<a id="unit-preparation-and-use-boundary"></a>
## Preparation and use boundary

This snapshot's workspace is version 0.9.5, edition 2021 and requires Rust 1.94.
The Metal feature requires a compatible Apple native stack plus matched Candle
revision and shader/build inputs. The source repository's broad workspace tests
can use model fixtures, tokens and downloads; they are not safe default checks.

This graph does not ship an installer. Use only an independently reviewed,
versioned upstream release/build procedure under separate installation
authorization. Do not execute remote shell installers or install Rust/SDKs just
to inspect this graph. If an authorized CLI is already installed, a bounded
identity/help check is:

```bash
mistralrs --version
mistralrs --help
```

Those public CLI invocations were **not run** here. Current inspection has no
Cargo/rustc or compatible Apple backend; no Rust compilation or live Rust API
inspection is claimed. The source/manual adaptation is explicitly partial.
Bundled helpers remain usable without the source checkout or inference package.

<a id="unit-return-a-bounded-result"></a>
## Return a bounded result

Report source/build identities, actual versus declared facts, route, invariant,
safe support result, counter-signal and smallest next authorized native check.
Required Metal/kernel/model validation remains `BLOCKED_REQUIRED_BACKEND` until
separately executed; compiler checks are `not_run`. Candidate state is not
promoted by helper tests, packaging, independent content review or a merged PR.
Memory fit, quality, service performance and broad skill efficacy are unverified.

<a id="unit-when-this-applies"></a>
## When this applies

- **Scope** — Selected native Metal paged decode/prefill layout/metadata/workspace and preparation/evidence investigation. Common catalog categorization is not CPU inference or hardware certification.
- **Prerequisites** — Access to the pinned Rust/Candle/MSL decode, prefill and qualification contracts; native comparisons need the matched Rust/Apple/Candle/shader stack and separately authorized frozen references.
- **Input contract** — mistral.rs/Candle/native artifact revisions, Rust toolchain, Apple SDK/OS/device, actual model/cache dtype and representation, shape/strides/offsets, block table, context and execution limits.
- **Produced artifact** — A source/build-bound route and invariant report with actual versus declared facts, safe support result, counter-signal and smallest next native check; unavailable Metal/kernel/model evidence remains blocked.
- **Failure modes** — Equating element counts with physical alias/layout identity, transferring decode geometry to prefill, or treating prewarm/pipeline preparation as actual dispatch can misclassify eligibility and native correctness.

<a id="unit-putting-the-idea-to-work"></a>
## Putting the idea to work

- Select decode, prefill or qualification by the failed contract, then follow cache/metadata bytes from producer through view to native consumer.
- Keep static predicates, pipeline preparation, kernel dispatch, numerical correctness and model/service outcomes as separate evidence steps; retain skipped or gated tests.
- Use the matched Candle revision and native shader/build inputs; broad workspace tests can require model fixtures, tokens and downloads.

<a id="unit-limits-of-this-evidence"></a>
## Limits of this evidence

- BLOCKED_REQUIRED_BACKEND: actual Rust/Candle/Apple Metal compilation, native tensor/cache/dispatch/parity/model/quality/service/performance evidence not_run.
- Cargo/rustc and compatible Apple SDK/device unavailable; no Rust package/toolchain or native dependency installation, live Rust API inspection or source test execution claimed.
- Offline helpers screen caller declarations, source byte formulas or boundary enumeration only; no tensor authentication, GPU simulation, native eligibility, scratch-capacity or physical-fit proof.
- Generic model/loading/quantization/server/agentic/distributed/CUDA paths and unmined specialized kernels remain explicit long-tail gaps; broad skill efficacy unmeasured.
- NO_LICENSE is the actual unauthenticated gh resolver fallback, not legal absence; root MIT and identified component Apache-2.0/NOTICE retained independently.

<a id="unit-source-files"></a>
## Source files

- [LICENSE](../../../../skill_library/repositories/mistral-rs/LICENSE)
- [metadata.json](../../../../skill_library/repositories/mistral-rs/metadata.json)
- [references/apache-component-license.md](../../../../skill_library/repositories/mistral-rs/references/apache-component-license.md)
- [references/paged-component-notice.md](../../../../skill_library/repositories/mistral-rs/references/paged-component-notice.md)
- [references/repo-routing-metadata.json](../../../../skill_library/repositories/mistral-rs/references/repo-routing-metadata.json)
- [references/source-identity.json](../../../../skill_library/repositories/mistral-rs/references/source-identity.json)
