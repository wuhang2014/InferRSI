<!-- handbook
{
  "id": "case.vllm-gdn-source-contract",
  "kind": "case",
  "aliases": [
    "checkout:case.vllm-gdn-source-contract"
  ],
  "carry": [
    "unit-when-this-applies",
    "unit-limits-of-this-evidence"
  ]
}
-->

# vLLM GDN source-contract cases

> Recorded state `candidate` · [Source](../../../../../skill_library/methods/kernel-writing-guide/cases/vllm-gdn-source-contract.md) · [Scope and provenance](../../../../../skill_library/methods/kernel-writing-guide/cases/vllm-gdn-source-contract.json) · [Parent reading](../lesson.md)

These four representative scenarios qualify source reasoning for the
[Qwen3-Next GDN contract](vllm-gdn-causal-conv-contract.md).
Source: [vLLM](https://github.com/vllm-project/vllm). State: candidate.
Source identity and scope: [case record](../../../../../skill_library/methods/kernel-writing-guide/cases/vllm-gdn-source-contract.json).
Native execution is `not_run`; agent efficacy is `not_evaluated`.
These cases do not report a reproduced failure or a performance result.

<a id="unit-1-mixed-phases-and-one-token-initialization"></a>
## 1. Mixed phases and one-token initialization

**Request:** A Qwen3-Next batch contains a resumed one-token request and a
first one-token prefill with `is_prefilling=True`. Explain which convolution
and recurrent paths the pinned vLLM source selects. Treat a following mixed
batch with a longer prefill separately. Do not run the model.

**Expected reasoning:**

- Name Qwen3NextDecoderLayer's `linear_attention` caller and interleaved layout.
- Use prior-state/prefill metadata as well as query length; a first one-token
  chunk can require the prefill route to mask recycled state.
- If any non-speculative prefill rows exist, identify the varlen forward
  convolution over the non-speculative portion.
- In a mixed non-speculative batch, identify decode-first recurrent update,
  rebased prefill cumulative lengths, prefill-row state slicing and output stitch.
- Distinguish this from speculative-row reclassification.

**Failure signals:** Treat every one-token row as decode; select a decode-only
conv for the entire mixed batch; pass unre-based offsets to the prefill
recurrence; claim model execution from source classification.

<a id="unit-2-requested-backend-versus-actual-branch"></a>
## 2. Requested backend versus actual branch

**Request:** An operator proposal says that selecting FlashInfer for GDN
prefill also replaces Qwen3-Next's decode convolution, and that an installed
fused CUDA MTP symbol proves it will run. Audit that statement from the pinned
caller without certifying any GPU.

**Expected reasoning:**

- Separate requested from effective prefill selection and retain source predicates.
- Separate convolution from recurrence dispatch and explain the packed decode guard.
- Follow Qwen3-Next's `gqa_interleaved_layout=True` into fused-MTP rejection;
  distinguish implicit fallback from explicitly requesting the rejected CUDA mode.
- State that XPU SYCL is an adjacent fused whole-layer exception whose behavior
  cannot be imposed on the chosen CUDA-facing path.
- Require actual dispatch evidence before claiming a backend ran.

**Failure signals:** Infer selection from package presence, default flags or
symbol names; generalize a separate-conv rule to every model/backend; turn a
source predicate into hardware compatibility or speedup.

<a id="unit-3-reordered-state-rows-and-speculative-progress"></a>
## 3. Reordered state rows and speculative progress

**Request:** A worker wants to reuse the vLLM conv update while reordering
requests. It proposes using batch positions as cache-row IDs and a persistent
`cache_seqlens` ring cursor. Describe the compatible state contract and the
evidence still needed.

**Expected reasoning:**

- Separate convolution history, GDN recurrent matrix and attention KV.
- Derive row IDs from the engine mapping; preserve mapping across reorderings.
- State the per-rank history and recurrent shapes and account for SD/DS orientation.
- Explain initial-state masks, first-chunk zero history, recurrent-state clearing,
  null padding and request-count versus token-count metadata.
- Identify `num_accepted_tokens-1` as the inspected speculative read offset;
  packed cumulative lengths are batch offsets, not a persistent cursor.
- Retain in-place history writes and distinguish converted-input aliasing from
  unconditional original-input mutation.
- Keep physical row allocation/release/recycling outside the inspected boundary.

**Failure signals:** Copy standalone-package cursor semantics into this API;
equate batch index with cache row; preserve stale first-chunk state; assume
convolution and recurrent state are attention KV or ignore state writes.

<a id="unit-4-proving-a-binding-with-an-unidentified-hf-caller"></a>
## 4. Proving a binding with an unidentified HF caller

**Request:** A model label is given, with no HF implementation revision.
Can the worker bind vLLM's named causal-conv functions directly and claim GDN
acceleration? Return a source-backed readiness decision and the missing evidence.

**Expected reasoning:**

- Identify the vLLM in-tree import and registered core call chain.
- Keep the concrete HF implementation and its calling schema unknown.
- Request only the source needed to establish the HF caller, projection/layout,
  state ownership, phase guards, output and mutation contract.
- Do not infer equivalence with the standalone Dao package, external FlashInfer
  or vendored FLA implementations from an import or a shared symbol name.
- Separate source compatibility, installed/built operator, actual dispatch,
  numerical/state correctness and measured performance.
- Propose independent first/resumed, mixed, reordered, padded and speculative
  checks only where the eventual bound implementation supports them.

**Failure signals:** Invent a model-to-HF implementation mapping; prescribe an
unverified installation; assert numeric correctness, hardware support or speedup.

<a id="unit-rubric-and-uncovered-work"></a>
## Rubric and uncovered work

| Capability | Previous owner material | Added representative rubric | Evaluation |
|---|---|---|---|
| Phase classification | Generic verify-before-benchmark guidance | Concrete first/resumed, mixed and speculative branch checks | Source-supported; not_evaluated |
| Effective operator selection | General framework choice | Requested/effective recurrence, separate conv and fused-path exclusions | Source-supported; not_evaluated |
| State lifecycle at the call boundary | General correctness rules | Row mapping, initialization, history mutation and accepted-token offset | Source-supported; not_evaluated |
| Binding readiness | General reference/numeric validation | Concrete import/registration plus explicit unidentified-HF boundary | Source-supported; not_evaluated |

The upstream metadata and convolution tests express relevant intent, but were
not run for these cases. Native backend execution, independent numeric/state
comparison, concrete HF binding, physical allocator lifecycle, backend builds,
performance and agent outcome comparisons remain uncovered.

<a id="unit-when-this-applies"></a>
## When this applies

- Source-only qualification of the pinned Qwen3-Next CUDA-facing GDN caller
- Mixed prefill/decode, packed/speculative metadata and state-row contracts

<a id="unit-limits-of-this-evidence"></a>
## Limits of this evidence

- Native kernel/model/device execution not_run
- Representative agent evaluation not_evaluated
- No concrete HF binding, external implementation equivalence, hardware compatibility or performance claim
- Physical state allocation, release and recycling outside the readset

<a id="unit-classify-one-token-gdn-rows-with-prefill-and-prior-state-metadata"></a>
## Classify one-token GDN rows with prefill and prior-state metadata

- **Outcome** — failure_signal
- **Reason** — The first one-token chunk may require the prefill route to mask recycled state. Mixed non-speculative input with any prefill row uses varlen forward convolution; the recurrent split requires decode-first handling, rebased prefill lengths and an output stitch.
- **Revisit when** — Inspect first and resumed one-token rows and a mixed batch with longer prefill. Treat speculative-row classification as a separate test.
- **Keywords**
  - vLLM
  - Qwen3-Next
  - one-token prefill
  - varlen
  - mixed batch
  - rebased seqlens
- **Scope** — regime_bound

<a id="unit-verify-actual-gdn-and-convolution-branches-after-requesting-flashinfer"></a>
## Verify actual GDN and convolution branches after requesting FlashInfer

- **Outcome** — failure_signal
- **Reason** — Requested FlashInfer prefill does not resolve decode convolution. Inspect the packed decode guard and effective recurrence selection. Qwen3-Next’s interleaved GQA layout excludes the inspected fused CUDA MTP option, while XPU SYCL has its own whole-layer route.
- **Revisit when** — Record the effective operator on the intended backend and distinguish an automatic fallback from an explicitly rejected CUDA configuration.
- **Keywords**
  - FlashInfer prefill
  - decode conv
  - packed decode
  - fused CUDA MTP
  - gqa_interleaved_layout
  - XPU SYCL
- **Scope** — regime_bound

<a id="unit-use-mapped-state-rows-and-the-accepted-token-offset-in-speculative-updates"></a>
## Use mapped state rows and the accepted-token offset in speculative updates

- **Outcome** — failure_signal
- **Reason** — Batch position and cumulative packed offsets do not own persistent history. The inspected speculative read uses num_accepted_tokens minus one. Convolution history writes and the recurrent matrix must retain their own initialization, padding and row semantics.
- **Revisit when** — For padded and reordered requests, compare both writes using real cache-row mapping, accepted-token metadata and per-rank layout.
- **Keywords**
  - causal_conv1d_update
  - cache_seqlens
  - num_accepted_tokens
  - speculative
  - row mapping
  - conv state
- **Scope** — regime_bound

<a id="unit-resolve-the-concrete-hf-caller-before-attempting-a-vllm-conv-binding"></a>
## Resolve the concrete HF caller before attempting a vLLM conv binding

- **Outcome** — failure_signal
- **Reason** — A common symbol name does not establish equivalence between the vLLM in-tree call chain and standalone Dao, FlashInfer or vendored FLA paths. The unidentified HF implementation leaves projection, state ownership and mutation contracts unresolved.
- **Revisit when** — Pin the caller and compare initial, resumed, mixed, reordered, padded and speculative cases that the eventual binding supports, including state and output parity.
- **Keywords**
  - HF binding
  - causal conv
  - GDN
  - in-tree import
  - Dao
  - state ownership
- **Scope** — regime_bound

<a id="unit-source-files"></a>
## Source files

- [vllm-gdn-source-contract.json](../../../../../skill_library/methods/kernel-writing-guide/cases/vllm-gdn-source-contract.json)
