<!-- handbook
{
  "id": "ascend-model-adaptation",
  "kind": "procedure",
  "aliases": [
    "checkout:ascend-model-adaptation",
    "inferrsi.ascend.skills.ascend_model_adaptation",
    "package:inferrsi.ascend.skills.ascend_model_adaptation"
  ],
  "tags": [
    "ascend",
    "npu",
    "model-adaptation",
    "fp8",
    "multimodal",
    "vllm-ascend"
  ]
}
-->

# Ascend Model Adaptation

> Recorded state `candidate` · empirical validation `not_run` · [Source](../../../../../skill_library/hardware/ascend/ascend-model-adaptation/SKILL.md) · [Scope and provenance](../../../../../skill_library/hardware/ascend/ascend-model-adaptation/metadata.json) · [Catalog record](../../../../../repo_packs/inferrsi/knowledge/ascend/skills/ascend-model-adaptation.json) · [Catalog revision](../../../../../repo_packs/inferrsi/knowledge/_provenance.json) · [Parent reading](../../overview.md)

Patterns for porting LLM/VLM model adapters to Ascend NPU: FP8 checkpoint handling, KV replication with TP, multimodal feature validation order, graph mode startup, and feature-status reporting. Source-grounded from vllm-ascend production experience. Use when adapting a new model checkpoint to run on Ascend via vllm-ascend or a similar framework.

Status: candidate. Source-grounded from vllm-ascend @ `bc8115ed7fdc7e500320b5de70742ef049b4c1a2`. Read [source-notes](references/source-notes.md) for immutable references and attribution boundaries. Unverified locally (no NPU). Verify against your CANN version and checkpoint format.

<a id="unit-choose-the-versioned-owner-three-tier-responsibility"></a>
## Choose the versioned owner & three-tier responsibility

This entry retains the historical model-adapter documentation pin `bc8115ed`. Use it for checkpoint onboarding, FP8 loading, KV-head replication and multimodal validation order.

To prevent duplicate definitions and maintain strict attribution boundaries across repository owners, InferRSI adopts the following routing convention:
1. **Tier 1 — vLLM Generic Mechanism (`repositories/vllm/`)**: PagedAttention block allocation, KV cache indexing, preemption scheduling, worker RPC protocols. Does not assume NPU or CANN specifics.
2. **Tier 2 — vLLM Ascend Plugin Features (`hardware/ascend/` & `hardware/host/`)**: Model checkpoint weight mapping, FP8 load-time dequantization into BF16, TP-aware KV-head replication, runtime ACLGraph model runner, and native host KV offload descriptor pooling.
3. **Tier 3 — Ascend / CANN / TorchNPU Bottom Constraints (`hardware/ascend/`)**: Lower-level driver and device constraints such as `aclmdlExecute`, geExecutor, HCCL mesh scratch, TorchNPU caching allocator, H2D/D2H copy streams.

For the runtime capture/replay execution contract, follow [ascend-aclgraph-capture-replay](../ascend-aclgraph-capture-replay/lesson.md). Its wrapper evidence does not revalidate this entry or establish a compatible installed stack. For compiler pass options, follow [ascend-graph-mode](../ascend-graph-mode/lesson.md). For host offload descriptor pooling, follow [host-memory-management](../../host/host-memory-management/lesson.md). See the [version and responsibility table](../../../library/overview.md#unit-vllm-ascend-version-and-responsibility-routing) for their separate evidence boundaries.

<a id="unit-debug-order-for-a-new-checkpoint"></a>
## Debug order for a new checkpoint

Always follow this sequence. Each step gates the next.

1. Start with `--load-format dummy` — verifies the architecture path without
   real weights. Fast; exposes missing op support, shape errors, and import
   failures before spending time on weight loading.
2. Run with real weights — validates weight mapping and load-time stability.
   Exposes missing scale keys, wrong remap paths, and sharding mismatches that
   dummy runs do not catch.
3. Validate `/v1/models` endpoint, then one text request, then one multimodal
   request (if the model supports VL).

Do not sign off on a checkpoint with dummy-only evidence. Always report both
what dummy validated and what only real weights validated.
Source: `fp8-on-npu-lessons.md` § reporting-discipline.

<a id="unit-fp8-checkpoints-on-ascend"></a>
## FP8 checkpoints on Ascend

FP8 execution kernels are typically not supported on Ascend NPU at the operator
level in baseline stacks. The recommended path is to dequantize FP8 weights to BF16 during loading.

Pattern (Source facts vs. implementation interpretation):
- **Source Fact**: For each quantized weight, look for paired tensors: `<name>.weight` and
  `<name>.weight_scale_inv`. Upstream notes establish that load-time dequantization into BF16 is required when native FP8 execution kernels are unavailable on NPU, and enforce strict unpaired scale/weight checks where a missing scale key triggers loader failure.
- **Implementation Interpretation**: The arithmetic expression `weight = weight_fp8.to(torch.bfloat16) * weight_scale_inv` represents an implementation interpretation for checkpoints using reciprocal scale factors. Upstream notes do not define a single universal scale granularity: for block-quantized or per-channel checkpoints, shape handling, broadcasting, and expansion are checkpoint-specific.
- Keep strict unpaired scale/weight checks — a missing scale key causes silent
  corruption if not caught.

Common failure: the dummy run succeeds but real shard loading fails with a
missing FP8 scale key. This is a checkpoint issue, not a framework bug.
Source: `fp8-on-npu-lessons.md` § 1-2.

<a id="unit-kv-replication-with-tensor-parallelism"></a>
## KV replication with tensor parallelism

When `tp_size > num_key_value_heads` (GQA/MQA models), KV heads must be
replicated across TP ranks. This requires a distinct loading path.

Symptom: shape mismatch such as `128 vs 64` during model loading with TP.

Pattern:
- Detect KV-head replication explicitly: if `tp_size > num_key_value_heads`, load each
  KV head into all ranks that share it rather than sharding it.
- Use a local norm/shard loader for replicated KV heads.
- Do not assume uniform divisibility for all head dimensions — check each
  attention weight tensor separately.
Source: `fp8-on-npu-lessons.md` § 4.

<a id="unit-aclgraph-npugraph_ex-for-inference"></a>
## ACLGraph (npugraph_ex) for inference

ACLGraph uses capture-and-replay to reduce host scheduling overhead. It is
beneficial for fixed-shape inference with high-frequency identical kernel calls.

Startup behavior with graph mode enabled:
- Startup latency is much higher than eager mode: compile warmup, graph capture
  rounds, and multimodal encoder profiling all happen at start.
- Do not treat slow startup as failure unless logs show hard errors.
- Expected log confirmation: `Replaying aclgraph` appears during inference.

For stability: prefer `HCCL_OP_EXPANSION_MODE=AIV` with graph mode enabled.
Use `--enforce-eager` only as a temporary isolation fallback during debugging,
not as a default serving configuration. For the complete runtime wrapper dispatch contract, refer to [ascend-aclgraph-capture-replay](../ascend-aclgraph-capture-replay/lesson.md).
Source: `fp8-on-npu-lessons.md` § 5, `multimodal-ep-aclgraph-lessons.md` § 3.

<a id="unit-multimodal-feature-validation-order"></a>
## Multimodal feature validation order

For VL models, validate features in this order (each step's failure blocks the
remaining ones):

1. Single text request (`/v1/models` + `/v1/chat/completions`)
2. Single text+image request
3. Graph mode evidence (`Replaying aclgraph` in logs), if graph mode is expected
4. Capacity baseline: target context length + batch size
5. Concurrency expansion if needed

For MoE models only: also validate EP (Expert Parallelism) and flashcomm1.
For non-MoE models, mark EP/flashcomm1 as not applicable (N/A), not as failed.
Source: `multimodal-ep-aclgraph-lessons.md` § 1-2.

<a id="unit-layer-reduction-smoke-tests"></a>
## Layer-reduction smoke tests

Reducing `num_hidden_layers` speeds up smoke tests but does not remove the ViT
or multimodal encoder structure. A model with reduced layers still exercises the
attention, feed-forward, and encoding paths.

Require at least one full-layer validation before final sign-off. Reduced-layer
results are valid as a fast gate, not as a production quality result.
Source: `multimodal-ep-aclgraph-lessons.md` § 5.

<a id="unit-feature-status-reporting"></a>
## Feature-status reporting

Use exactly four categories in reports. Never use ambiguous phrases like
"not tested" or "partially supported":

| Status | Meaning |
|--------|---------|
| ✅ supported and verified | Feature ran and produced correct output on this checkpoint |
| ❌ framework-level unsupported | Framework has no code path for this feature |
| ⚠️ checkpoint missing | Weights/config do not provide the feature even if the framework supports it |
| N/A | Not applicable (e.g., EP/flashcomm1 on a non-MoE model) |

Distinguish "theoretical max" (from model config `max_position_embeddings`) from
"practical max" (largest value that actually starts and serves on the current
hardware and TP/EP configuration). Report both explicitly.
Source: `multimodal-ep-aclgraph-lessons.md` § 4, 6.

<a id="unit-when-graph-mode-is-validated-and-works-document-it-as-the-default-path"></a>
## When graph mode is validated and works, document it as the default path

If ACLGraph is validated and expected in production, the runbook should document
it as the default serving path. Eager mode should appear only under
troubleshooting/fallback. Do not leave a validated graph mode as an optional
variant the operator must remember to enable.
Source: `multimodal-ep-aclgraph-lessons.md` § 7.

<a id="unit-when-this-applies"></a>
## When this applies

- **Scope** — Checkpoint onboarding for LLM/VLM adapters on Ascend: weight/scale loading, KV-head replication under tensor parallelism and staged multimodal feature checks.
- **Prerequisites** — Check the installed CANN and checkpoint format against the versioned guidance; final sign-off requires real weights and at least one full-layer validation.
- **Input contract** — Checkpoint weights/configuration and scale keys, attention-head/TP configuration, model modalities and expected graph/capacity features.
- **Produced artifact** — A checkpoint/feature report separating dummy and real-weight evidence, applicable feature outcomes, and theoretical versus demonstrated serving capacity.
- **Failure modes** — Dummy-only success misses scale/remapping/sharding defects; blindly sharding replicated KV heads or accepting reduced-layer results can conceal loading or full-model failures.
- **Refusal point** — Stop on missing FP8 paired scale keys, unsupported tensor parallel KV-head split without replication, unverified multimodal visual encoder output, or failed base endpoint validation.

<a id="unit-putting-the-idea-to-work"></a>
## Putting the idea to work

- Gate onboarding in order: dummy architecture check, real-weight loading, model endpoint, text request and then multimodal request when the model supports VL; retain the evidence each stage actually supplies.
- Check weight/scale pairing and each attention tensor loading path, especially when TP exceeds the KV-head count; verify historical FP8 guidance against the actual stack.
- Expand capacity/concurrency only after basic modality and expected replay checks; mark MoE-only features inapplicable for non-MoE models and require full-layer validation before sign-off.

<a id="unit-limits-of-this-evidence"></a>
## Limits of this evidence

- Source-derived candidate; no local efficacy validation.
- Original typed source inventory is not normalized; retain source identities and limits in the procedure/readsets.

<a id="unit-source-files"></a>
## Source files

- [metadata.json](../../../../../skill_library/hardware/ascend/ascend-model-adaptation/metadata.json)
