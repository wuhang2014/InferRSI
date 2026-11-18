<!-- handbook
{
  "id": "case.sglang-gdn-source-contract",
  "kind": "case",
  "aliases": [
    "checkout:case.sglang-gdn-source-contract"
  ],
  "carry": [
    "unit-when-this-applies",
    "unit-limits-of-this-evidence"
  ]
}
-->

# SGLang GDN source-contract cases

> Recorded state `candidate` · [Source](../../../../../skill_library/methods/kernel-writing-guide/cases/sglang-gdn-source-contract.md) · [Scope and provenance](../../../../../skill_library/methods/kernel-writing-guide/cases/sglang-gdn-source-contract.json) · [Parent reading](../lesson.md)

These are four source-grounded prompts and rubrics, not observed failures,
executed model/agent evaluations or performance results. State: candidate;
native execution `not_run`; agent efficacy `not_evaluated`.
The [case record](../../../../../skill_library/methods/kernel-writing-guide/cases/sglang-gdn-source-contract.json) owns source identity and scope.

<a id="unit-1-a-prefill-flag-does-not-replace-both-operators"></a>
## 1. A prefill flag does not replace both operators

**Request:** A Qwen3.5 proposal selects FlashInfer prefill and claims that it
also switches decode convolution to CUDA. Explain the pinned source selection
without importing SGLang or certifying a GPU.

**Expected reasoning:** Trace the linear decoder, `RadixLinearAttention`,
hybrid wrapper and concrete GDN backend. Resolve per-runner base/prefill/decode
overrides before inspecting effective dispatcher classes. The automatic
FlashInfer default affects prefill, with distinct SM9/FP32 and SM10/BF16/CUDA13
predicates. GDN imports Triton conv forward/update and rebinds only the CUDA
prefill function. Ordinary decode still uses its Triton update alias. A
separate CUDA update wrapper and its `cache_seqlens` argument do not establish
this caller's selected path. Require executing-operator evidence for any run.

**Failure signals:** Use one backend label for convolution and recurrence;
equate an explicit flag, package availability or a registered symbol with
executed dispatch; claim sm89 compatibility from an SM9/10 automatic default.

Source: [backend aliases/policy](https://github.com/sgl-project/sglang/blob/16176278d0180f1a1a578e53e6eef432577876c2/python/sglang/srt/layers/attention/linear/gdn_backend.py#L1-L374),
[ordinary decode](https://github.com/sgl-project/sglang/blob/16176278d0180f1a1a578e53e6eef432577876c2/python/sglang/srt/layers/attention/linear/gdn_backend.py#L850-L918).

<a id="unit-2-cuda-input-can-select-stride-aware-triton-prefill"></a>
## 2. CUDA input can select stride-aware Triton prefill

**Request:** A CUDA prefill replacement assumes the SRT convolution wrapper
always uses its CUDA kernel and returns a separate output. The caller passes
a transposed `[channels, total_tokens]` view and CPU sequence lengths. Audit
both assumptions and the continuation-state contract.

**Expected reasoning:** Measure actual strides in an authorized execution;
source selection is `last_stride != 1 and seq_lens_cpu supplied`, or no CUDA
path. That selects Triton, whose wrapper allocates a separate output while
updating indexed state. The CUDA branch may make a contiguous copy and returns
its mutated input buffer. Preserve cumulative token boundaries, row IDs and
`extend_prefix_lens > 0` initial-history mask. Recurrent initialization is
separate from that mask. The GDN recurrence flag cannot decide this conv branch.

**Failure signals:** Infer strides from shape; assume unconditional input
aliasing or no mutation; let packed requests read each other's history;
assume the conv mask clears the recurrent matrix.

Source: [prefill caller](https://github.com/sgl-project/sglang/blob/16176278d0180f1a1a578e53e6eef432577876c2/python/sglang/srt/layers/attention/linear/gdn_backend.py#L920-L941),
[SRT wrapper](https://github.com/sgl-project/sglang/blob/16176278d0180f1a1a578e53e6eef432577876c2/python/sglang/srt/layers/attention/mamba/causal_conv1d.py#L38-L136),
[Triton wrapper](https://github.com/sgl-project/sglang/blob/16176278d0180f1a1a578e53e6eef432577876c2/python/sglang/kernels/ops/mamba/causal_conv1d_triton.py#L408-L589).

<a id="unit-3-reordered-rows-and-strided-pools-must-keep-both-state-writes"></a>
## 3. Reordered rows and strided pools must keep both state writes

**Request:** A worker reorders requests and uses a strided state pool. It
proposes using batch positions as state IDs and discarding temporary prefill
state after returning output. Describe the compatible standard-path contract.

**Expected reasoning:** Resolve request-row → Mamba-row mapping and the
translation boundary. Distinguish conv history `[channels, W-1]` from temporal
state `[Hv/P, V, K]`; use resolved shapes for non-divisible head sharding and
independent state dtypes. First use requires fresh state; allocation marking
and pool clear declarations are not proof of the entire reset schedule.
Non-CPU ordinary extend gathers non-contiguous state into identity-indexed
copies and scatters both updated tensors back. Cumulative token offsets are
batch layout, not a ring cursor. Keep padding, target-verify intermediate
buffers and ReplaySSM lifetimes outside this ordinary-path assumption.

**Failure signals:** Reuse batch index as persistent identity; equate temporal
state with attention KV; lose gather/scatter write-back; treat a successful
output computation as proof that continuation, reset or recycling is correct.

Source: [mapping/ownership](https://github.com/sgl-project/sglang/blob/16176278d0180f1a1a578e53e6eef432577876c2/python/sglang/srt/mem_cache/memory_pool.py#L1586-L1688),
[state gather and write-back](https://github.com/sgl-project/sglang/blob/16176278d0180f1a1a578e53e6eef432577876c2/python/sglang/srt/layers/attention/linear/gdn_backend.py#L1012-L1227).

<a id="unit-4-fresh-classification-prefill-is-not-decode-or-multi-item-scoring"></a>
## 4. Fresh classification prefill is not decode or multi-item scoring

**Request:** A one-shot HF classifier wants to reuse SGLang's GDN/conv path.
The proposal cites prefill-only MIS support and omits caller-binding,
initialization and quality checks. State what transfers and what remains open.

**Expected reasoning:** Use fresh whole-sequence conv and GDN prefill contracts
only after identifying the actual HF worker/revision, projection order, gates,
normalization, dtype/layout, sequence boundaries, zero initial state and
mutation schema. No continuous-batching manager, decode loop, speculative
rollback or ReplaySSM ring is required merely because SGLang has them. MIS
requires separate delimiter-based query/item branching, zero cached prefixes,
Triton prefill and no page-major layout; the workload label does not prove
equivalent logits. Require independent output/state parity, classifier quality
and a complete timed comparison on the required hardware before promotion.

**Failure signals:** Present source reasoning or packaged reads as a binding,
native test, quality pass or service gain; confuse a generic classifier with
MIS; assume unused returned cache makes internal state writes dispensable.

Source: [MIS constraints](https://github.com/sgl-project/sglang/blob/16176278d0180f1a1a578e53e6eef432577876c2/python/sglang/srt/layers/attention/linear/gdn_backend.py#L68-L164),
[query/item branching](https://github.com/sgl-project/sglang/blob/16176278d0180f1a1a578e53e6eef432577876c2/python/sglang/srt/layers/attention/linear/gdn_backend.py#L1231-L1299).

These interpretations use only the pinned SGLang source. Root licensing is
[Apache-2.0](https://github.com/sgl-project/sglang/blob/16176278d0180f1a1a578e53e6eef432577876c2/LICENSE);
the conv adaptation notices credit vLLM contributors and Tri Dao. No external
kernel implementation or model weights are imported by this case bundle.

<a id="unit-when-this-applies"></a>
## When this applies

- Pinned Qwen3.5/Qwen3-Next GDN caller/backend qualification
- Separate causal-conv phase/layout/state contracts and conditional one-shot classification-prefill transfer

<a id="unit-limits-of-this-evidence"></a>
## Limits of this evidence

- Native kernels, models and devices not_run
- Agent efficacy not_evaluated
- No HF binding, sm89/backend qualification, numerical/model-quality or performance claim
- Whole reset/cancellation/radix eviction, speculative and ReplaySSM lifecycles outside this readset

<a id="unit-resolve-prefill-recurrence-and-decode-convolution-separately"></a>
## Resolve prefill recurrence and decode convolution separately

- **Outcome** — failure_signal
- **Reason** — On the pinned path, the CUDA GDN prefill convolution alias can be rebound while ordinary decode keeps the Triton conv-update alias. A FlashInfer prefill setting or a CUDA update symbol does not show that decode was dispatched there.
- **Revisit when** — Trace runner-level overrides and effective aliases through the owning backend. Check the SM9/FP32 and SM10/BF16/CUDA13 prefill predicates before asking for an execution trace.
- **Keywords**
  - SGLang
  - GDN
  - FlashInfer prefill
  - Triton conv update
  - decode convolution
  - effective dispatch
- **Scope** — regime_bound

<a id="unit-use-the-actual-last-axis-stride-and-sequence-lengths-to-classify-convolution-pre"></a>
## Use the actual last-axis stride and sequence lengths to classify convolution prefill

- **Outcome** — failure_signal
- **Reason** — Even a CUDA input can take Triton when last_stride != 1 and seq_lens_cpu is supplied. That path returns a distinct output while updating state; the CUDA branch returns the modified input buffer it uses.
- **Revisit when** — Inspect strides, packed token offsets and row IDs. Verify the prefix-history mask for convolution independently of recurrent state initialization.
- **Keywords**
  - causal_conv1d
  - CUDA prefill
  - Triton stride
  - seq_lens_cpu
  - aliasing
  - initial-history mask
- **Scope** — regime_bound

<a id="unit-preserve-both-state-write-backs-through-a-reorder-and-noncontiguous-gather"></a>
## Preserve both state write-backs through a reorder and noncontiguous gather

- **Outcome** — failure_signal
- **Reason** — Ordinary non-CPU extend maps requests to persistent Mamba rows. With noncontiguous pools it gathers indexed copies and scatters both convolution history and the GDN matrix back. A correct immediate output does not exercise their later use.
- **Revisit when** — Check fresh and continued requests after a reorder and compare both state tensors at their mapped rows. Account for separate dtypes and head sharding.
- **Keywords**
  - Mamba rows
  - strided state pool
  - gather scatter
  - conv history
  - temporal state
  - request reorder
- **Scope** — regime_bound

<a id="unit-prove-hf-classifier-parity-before-transferring-an-sglang-prefill-path"></a>
## Prove HF classifier parity before transferring an SGLang prefill path

- **Outcome** — failure_signal
- **Reason** — A fresh whole-sequence classifier can use prefill reasoning only after identifying its worker and state contract. MIS additionally assumes delimiter-driven query/item branches, zero cached prefixes, Triton and a compatible layout.
- **Revisit when** — Pin the HF caller and check layout, gates, zero state, mutation behavior, output/state parity and classifier quality before timed comparison.
- **Keywords**
  - HF classifier
  - MIS
  - multi-item scoring
  - one-shot prefill
  - zero state
  - caller binding
- **Scope** — regime_bound

<a id="unit-source-files"></a>
## Source files

- [sglang-gdn-source-contract.json](../../../../../skill_library/methods/kernel-writing-guide/cases/sglang-gdn-source-contract.json)
