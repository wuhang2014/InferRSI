<!-- handbook
{
  "id": "vllm_omni.common.diffusion.upstream_review_gates",
  "kind": "record",
  "aliases": [
    "package:vllm_omni.common.diffusion.upstream_review_gates"
  ],
  "tags": [
    "review",
    "request_state",
    "shared_kernels",
    "reproducibility",
    "source_integrity",
    "artifact_provenance",
    "framework_boundaries",
    "cross_model_regression"
  ],
  "carry": [
    "unit-when-this-applies",
    "unit-limits-of-this-evidence"
  ]
}
-->

# Upstream review gates for optional acceleration and evidence ownership

> Recorded state `imported` · locally verified `false` · evidence level `guidance` · [Source](../../../../../../../repo_packs/vllm_omni/knowledge/common/diffusion/upstream-review-gates.json)

Review framework policy boundaries, all shared-component consumers, optional backend prerequisites, request-state lifetime, portable reproduction, and independent artifact provenance before promoting an optimization.

`contribution` · `vllm_omni` · `common` · `diffusion.*`

<a id="unit-when-this-applies"></a>
## When this applies

- **Hardware** — `[]`
- **Software**
  - Diffusion frameworks with optional extensions and singleton model state
- **Models**
  - Models sharing numerical operator contracts
- **Conditions**
  - A candidate is being prepared for upstream review
  - Benchmarks emit per-trial artifact manifests

<a id="unit-what-the-source-reports"></a>
## What the source reports

- **Guidance.** A hardware/dtype match does not establish compiler, header, library or collective availability. Keep optional acceleration opt-in, or coordinate one initialization decision across all ranks.
- **Guidance.** Singleton model state must not extend request prefix-KV lifetime. Use request ownership or weak identity and cleanup on success, error, cancellation and dropped step-mode requests; keep graph buffers separate.
- **Guidance.** Reusable math belongs in the target common operator layer; model-specific dispatch and approximation policy stay in adapters. Preserve reduction order, casts and dtype/compile/autograd fallbacks.
- **Guidance.** Tracked source changes remain in the fingerprint even if output directories overlap source. Exclude only the active run untracked artifact directory.
- **Guidance.** Generated files resolve beneath their own trial; references and duplicate/cross-trial paths cannot substitute for independent outputs. Final integrity or cleanup errors still produce failed records.
- **Guidance.** Published evidence uses portable paths, complete before/after timings, image checksums and frozen validators. Historical source-pair claims are distinct from rebased-head comparisons.
- **Guidance.** Framework dispatch and framework tests remain model-neutral. Reuse explicit common configuration; keep model policy in adapters and topology/build prerequisites in the owning backend instead of duplicating model/device/version condition chains.
- **Guidance.** Shared component or script changes require a direct and transitive consumer inventory, regression evidence for other affected models, and explicit coverage gaps. One model E2E result cannot establish another model quality or performance.
- **Guidance.** Keep benchmark code and acceptance criteria outside the candidate optimization change. Pin the same independently reviewed evaluator for both arms; archive historical results without treating them as validation of a later revision.
- **Guidance.** Prefer full-model E2E coverage for normal model behavior. Add focused tests for cache invalidation, errors, fallback selection and shared consumers only where E2E does not exercise the contract; avoid repeated production-shape matrices.
- **Guidance.** Prefer module-level imports for ordinary dependencies; retain documented lazy imports where transitive optional kernels or backend libraries would otherwise become unconditional platform requirements.
- **Guidance.** Share identical kernel eligibility predicates across consumers. Colocate small ownership-only types with their consumer instead of adding modules for speculative growth. Explain low-precision round trips that reproduce eager intermediate rounding.

<a id="unit-putting-the-idea-to-work"></a>
## Putting the idea to work

- Demonstrate each correctness issue with existing E2E coverage or a focused regression for a boundary the E2E suite does not exercise.
- Use a benchmark and quality evaluator reviewed and frozen independently of the candidate optimization; changes to the evaluator require a separate review and campaign.
- Publish complete campaign archives and hash manifests, while preserving legacy records.
- Remove obsolete selection knobs and their model-specific framework tests when consolidating configuration.
- Attach a consumer-to-test coverage map, including fast/fallback paths, layouts, dtypes, hooks, gradients and applicable encoder/decoder integration.

<a id="unit-how-to-check-it"></a>
## How to check it

- Exercise unavailable-extension default selection without CUDA.
- Drop a populated request cache and check weak references after success/error/interrupt and step-mode cancellation.
- Run all consumers of moved shared operators, including their numeric CUDA contracts.
- Reject output aliasing and source changes under overlapping output roots.
- Re-run native full-service quality and comparable current-base/current-head measurements after rebase.
- Verify default dispatch does not load optional extensions and explicit common settings reach the selected backend without model or device-name predicates.
- Record source/environment/test commands and all skips or failures for every affected consumer; mark missing coverage INCONCLUSIVE rather than generalizing target-model E2E evidence.
- Verify that the candidate diff cannot edit its scoring benchmark or frozen quality criteria.
- Map added tests to failure modes missing from existing E2E coverage and remove duplicated successful-path checks.
- Exercise imports with optional backend modules unavailable; preserve eager intermediate roundings and dropped-request weak-reference cleanup when consolidating helpers or ownership types.

<a id="unit-limits-of-this-evidence"></a>
## Limits of this evidence

- This record imports review guidance; it is not a benchmark or an accelerator support claim.
- Local regression and E2E results belong to the review-response report and its pinned evidence, not this portable record.

<a id="unit-sources"></a>
## Sources

- **Url** — <https://github.com/vllm-project/vllm-omni/>
- **Type** — review_guidance
- **Commit** — 443b3e97c09af3f5bd9399ef3b3ec8e7b0215852
- **Accessed at** — 2026-10-12

- **Url** — <https://github.com/vllm-project/vllm-omni/>
- **Type** — review_guidance
- **Commit** — d57480f5054e6c377a04225840b24e6355244dd9
- **Accessed at** — 2026-10-12

- **Url** — <https://github.com/vllm-project/vllm-omni/>
- **Type** — review_guidance
- **Commit** — 6550e3f626e5c38fb7bf8a487f397797447fde33
- **Authors**
  - timzsu
- **Accessed at** — 2026-10-13

- **Url** — <https://github.com/vllm-project/vllm-omni/>
- **Type** — review_guidance
- **Commit** — e36d48ba47eef4b4954b6c4d97fd42471525fd30
- **Authors**
  - timzsu
- **Accessed at** — 2026-10-13
