<!-- handbook
{
  "id": "audit-sglang-diffusion-lifetimes",
  "kind": "procedure",
  "aliases": [
    "checkout:audit-sglang-diffusion-lifetimes",
    "inferrsi.common.skills.audit_sglang_diffusion_lifetimes",
    "package:inferrsi.common.skills.audit_sglang_diffusion_lifetimes"
  ],
  "tags": [
    "sglang",
    "diffusion",
    "stage",
    "state",
    "residency",
    "cancellation"
  ]
}
-->

# Audit SGLang diffusion lifetimes

> Recorded state `candidate` · empirical validation `not_run` · license `Apache-2.0` · [Source](../../../../../skill_library/repositories/sglang/audit-sglang-diffusion-lifetimes/SKILL.md) · [Scope and provenance](../../../../../skill_library/repositories/sglang/audit-sglang-diffusion-lifetimes/metadata.json) · [Catalog record](../../../../../repo_packs/inferrsi/knowledge/common/skills/audit-sglang-diffusion-lifetimes.json) · [Catalog revision](../../../../../repo_packs/inferrsi/knowledge/_provenance.json) · [Parent reading](../lesson.md)

Diagnose SGLang multimodal_gen stage state, component residency and request timeout/deletion when grouped outputs interfere, a module remains resident, or stopped waiting is mistaken for stopped execution; requires pinned source or a concrete trace.

Status: candidate. Empirical validation: **not_run**. This is a source-grounded
diagnostic procedure, not backend qualification or a performance recipe.

Use for composed diffusion pipeline stage scheduling, scheduler-object aliases,
component-use intervals, and the distinction between client/job termination and
worker/device completion. Use the existing SGLang owner for LLM Radix/HiCache and
topology guidance. SGLang-Omni, full pool/disaggregated execution, realtime/rollout
sessions, model-specific kernels and quality tuning are outside this readset.

Read the [source notes](references/source-notes.md) before use. Evidence is
SGLang `df13d5dce31abfeff0e701a62e8c39a136758e6c` (Apache-2.0); the older LLM
and HiCache pins are independent. CODE and TEST-SOURCE describe inspected source;
all proposed runtime checks and benefits remain HYPOTHESIS until tested.

<a id="unit-select-the-matching-sglang-entry"></a>
## Select the matching SGLang entry

Use the [three-pin responsibility comparison](../lesson.md#unit-choose-among-source-pins)
for LLM engine or HiCache questions. The CUDA HiCache peer's stable catalog ID is
`sglang.cuda.llm.hierarchical_prefix_cache`; read it separately at its own pin.
Its prefix-KV host/storage policy does not establish this diffusion path's stage,
scheduler-instance, component-use, timeout or finalizer contracts. The engine
entry does not make these pins a tested compatible stack.

<a id="unit-required-inputs"></a>
## Required inputs

Record source/build revision, native versus Diffusers backend, actual pipeline
and executor class, model/weights revision, modality and shape, steps/scheduler,
seed/output count, grouped versus serial route, ranks/parallel mode, component
placement policy, warmup state, output-save mode and the observed symptom.
For timeouts/deletion collect request/job IDs and client/scheduler/worker events.
Keep unavailable inputs explicit; a server flag or successful import does not
establish actual dispatch or hardware behavior.

<a id="unit-bounded-procedure"></a>
## Bounded procedure

1. **Follow the real executor.** Trace client → scheduler dispatch → worker →
   composed-pipeline forward → installed residency manager → executor → stage.
   The default is `ParallelExecutor`; rank policies and collective participation
   are part of the contract (P1-P3, Q1-Q3, W1). Do not reason from SyncExecutor
   alone or apply the monolithic event loop to the pool route.
2. **Draw separate lifetimes.** Track request, stage, component-use interval,
   module instance, mutable diffusion scheduler, output finalizer and allocator
   cache. Request/stage `finally` cleanup begins only after the corresponding
   entry function succeeds (P4-P5). Locate setup failures separately.
3. **Explain retained modules before changing policy.** Inspect ordered component
   uses, prepare/wait, unconsumed prefetch cleanup, explicit placement, warmup
   hints, keep-ready rules and request-tail prefetch (M1-M7). Closing a use does
   not promise eviction; allocator-cache release and deferred-save completion
   have different owners (W2). Record actual strategy and allocated/reserved
   memory separately. Do not “fix” intentional residency by flushing each stage.
4. **Check aliases across reuse and concurrency.** Trace `Req.scheduler` from
   timestep preparation to denoising. The helper defaults to sharing the stage
   template, and existing request state wins. Inspect group fingerprints and
   declared shallow/tensor-clone/deepcopy output fields (S1-S6). The timestep
   duplicate-copy path deep-copies its scheduler; this does not establish every
   group's isolation. Before introducing overlap, test mutable state independence
   using the real selected scheduler and unchanged timesteps/seeds.
5. **Trace cancellation to execution.** A client timeout closes its socket;
   video deletion removes a store record and still has an abort TODO (C1-C4,
   E1-E3). Correlate worker dispatch/use/finalizer completion and a device trace
   before claiming stopped compute or reclaimed resources. Preserve unknown
   execution outcome after timeout. A mocked socket-close assertion (T1) proves
   no device cancellation contract.
6. **Choose one falsifying check.** Compare serial/grouped output equivalence and
   scheduler identities for a state problem; interval/event ordering and retained
   resources for a residency problem; or worker/device completion after a client
   timeout for cancellation. Hold model, backend, input shape, seeds and placement
   fixed. Change one ownership/concurrency policy only within authorized scope.

<a id="unit-expected-output-and-stop-conditions"></a>
## Expected output and stop conditions

Return a version-bound owner/event ledger, the first unresolved boundary, a small
causal hypothesis, the cheapest real discriminating check, and exact
passed/failed/not_run results. Include source links and missing dependencies.
Do not ship automatic mutation, cache eviction, cancellation or retries from this
guide. Stop performance claims when the executing path, cleanup or output quality
is unresolved; retain the failure and a known baseline. Cross-rank exceptions,
backend strategies, local IPC timeout retains and model-specific state need their
own bounded investigation rather than a blanket safety or leak conclusion.

InferRSI static/installed-package checks validate reading and packaging only.
Real GPU/NPU offload, collectives, cancellation latency, output quality and E2E
performance require separately applicable native evidence (D1-D3).

<a id="unit-when-this-applies"></a>
## When this applies

- **Scope** — Bounded monolithic multimodal_gen composed-pipeline state and lifecycle diagnosis; actual backend/model behavior requires native validation.
- **Prerequisites** — Pinned source or a concrete trace of the selected composed-pipeline executor and installed residency manager, with the applicable monolithic route identified.
- **Input contract** — Source/build, backend and executor/pipeline class, model revision, modality/shape, steps/scheduler/seed/output count, grouped/serial route, ranks, placement, warmup/save settings and symptom; timeout cases need correlated request/job and client/scheduler/worker events.
- **Produced artifact** — A version-bound owner/event ledger, first unresolved boundary, causal hypothesis, smallest real discriminating check, exact results and missing dependencies.
- **Failure modes** — Assuming all executors share the SyncExecutor contract, treating closed component use as eviction, assuming grouped schedulers are isolated, or reading socket close/job deletion as stopped device compute can misdiagnose ownership.
- **Refusal point** — Stop performance claims when the executing path, cleanup or output quality is unresolved; retain the failure and a known baseline rather than inferring a blanket leak or safety conclusion.

<a id="unit-putting-the-idea-to-work"></a>
## Putting the idea to work

- Trace the actual executor and separate request, stage, component-use, module, scheduler, finalizer and allocator-cache lifetimes.
- Check scheduler aliases and declared output-copy policies before introducing overlap; compare real serial/grouped outputs with fixed timesteps and seeds.
- Correlate worker, finalizer and device completion after client timeout or deletion; preserve an unknown execution outcome until that evidence exists.

<a id="unit-limits-of-this-evidence"></a>
## Limits of this evidence

- Source-derived candidate; upstream runtime and efficacy validation not run.
- Supplier verified one selected source blob, not the whole archive tree.
- No automatic grouped isolation, device cancellation, cross-rank recovery or performance claim.

<a id="unit-source-files"></a>
## Source files

- [LICENSE](../../../../../skill_library/repositories/sglang/audit-sglang-diffusion-lifetimes/LICENSE)
- [metadata.json](../../../../../skill_library/repositories/sglang/audit-sglang-diffusion-lifetimes/metadata.json)
