<!-- handbook
{
  "id": "records/contribution/inferrsi/overview",
  "kind": "guide"
}
-->

# InferRSI skill discovery index

> [Source](../../../../../repo_packs/inferrsi/knowledge/README.md)

Generated abstracts for all 80 registered skills in `data/skill_library/`.
Their complete procedures, references and cases ship in the same package.
`skill-index.json` maps stable skill IDs to categorized directories. The
reference and searchspace matrices
remain the maintained knowledge views. Do not edit generated files by hand.

Index status `imported` and `locally_verified: false` describe these discovery
records. Original status, provenance, license declarations and limitations
are preserved under `skill_metadata`; absent fields remain absent. Unknown
licenses remain unknown. Indexing grants no execution permission or validation.

These are knowledge abstracts (`--kind knowledge`), with namespaced package
IDs distinct from explicitly selected `checkout_ref` skills. Ascend/CUDA
procedures use their corresponding backend; shared methods use `common`.

`_provenance.json` holds the shared source snapshot: the full source
revision and the registry hash. Stored records (schema 2) keep only their own
fields and resource hashes; the catalog restores the schema-1 `sources` entry and
registry hash from the snapshot, so editing one skill regenerates only its record
and the snapshot.

```bash
inferrsi knowledge search 'profiling' --repo-type inferrsi --limit 50
inferrsi collect --repo-type inferrsi --kind knowledge --limit 50 --material
```

After committing changes to skill bodies, resources or the registry, regenerate from a
development installation with the skills extra. The source revision must
contain the current input paths and bytes (Git checkout filters are respected).
`source_files` hashes identify the canonical Git bytes, not a validation result.

```bash
python tools/build_skill_index.py --source-revision <committed-source-revision>
python tools/build_skill_index.py --source-revision <committed-source-revision> --check
```

`--check` detects missing, stale and unexpected generated records without writing;
use the `source_revision` recorded in `_provenance.json`.
References and cases ship with their owning skill, not as duplicate knowledge abstracts.

| Skill | Backend | Original declared status |
| --- | --- | --- |
| [ascend-aclgraph-capture-replay](../../../hardware/ascend/ascend-aclgraph-capture-replay/lesson.md) | ascend | candidate |
| [ascend-device-health](../../../hardware/ascend/ascend-device-health/lesson.md) | ascend | candidate |
| [ascend-distributed-parallel](../../../hardware/ascend/ascend-distributed-parallel/lesson.md) | ascend | candidate |
| [ascend-graph-mode](../../../hardware/ascend/ascend-graph-mode/lesson.md) | ascend | candidate |
| [ascend-model-adaptation](../../../hardware/ascend/ascend-model-adaptation/lesson.md) | ascend | candidate |
| [ascend-operator-profiling](../../../hardware/ascend/ascend-operator-profiling/lesson.md) | ascend | candidate |
| [ascend-operator-tuning](../../../hardware/ascend/ascend-operator-tuning/lesson.md) | ascend | candidate |
| [ascend-optimization-casebook](../../../hardware/ascend/ascend-optimization-casebook/lesson.md) | ascend | candidate |
| [ascend-performance-analysis](../../../hardware/ascend/ascend-performance-analysis/lesson.md) | ascend | candidate |
| [ascend-video-diffusion-optimization](../../../hardware/ascend/ascend-video-diffusion-optimization/lesson.md) | ascend | candidate |
| [ascendc-tiling-design](../../../hardware/ascend/ascendc-tiling-design/lesson.md) | ascend | candidate |
| [assess-serving-preemption](../../../methods/assess-serving-preemption/lesson.md) | common | candidate |
| [assess-split-backward-schedule](../../../methods/assess-split-backward-schedule/lesson.md) | common | candidate |
| [audit-afd-p2p-exchanges](../../../repositories/afd-plugin/audit-afd-p2p-exchanges/lesson.md) | cuda | candidate |
| [audit-fixed-workload-claim](../../../methods/audit-fixed-workload-claim/lesson.md) | common | candidate |
| [audit-flare-session-lifecycle](../../../repositories/flare-local-inference/audit-flare-session-lifecycle/lesson.md) | cuda | candidate |
| [audit-h3-metal-fasth3-semantics](../../../repositories/h3-metal/audit-h3-metal-fasth3-semantics/lesson.md) | common | candidate |
| [audit-h3-runtime-residency](../../../repositories/h3-c/audit-h3-runtime-residency/lesson.md) | common | candidate |
| [audit-llama-runtime-state](../../../repositories/llama-cpp/audit-llama-runtime-state/lesson.md) | common | candidate |
| [audit-recurrent-kv-finalization](../../../repositories/vllm-rlt/audit-recurrent-kv-finalization/lesson.md) | common | candidate |
| [audit-sd-cpp-residency](../../../repositories/stable-diffusion-cpp/audit-sd-cpp-residency/lesson.md) | common | candidate |
| [audit-sglang-diffusion-lifetimes](../../../repositories/sglang/audit-sglang-diffusion-lifetimes/lesson.md) | common | candidate |
| [audit-vllm-kv-lifetimes](../../../repositories/vllm/audit-vllm-kv-lifetimes/lesson.md) | common | candidate |
| [bound-windowed-attention-replay](../../../repositories/deepinfer/bound-windowed-attention-replay/lesson.md) | common | candidate |
| [budget-speculative-verification](../../../repositories/deepinfer/budget-speculative-verification/lesson.md) | common | candidate |
| [calibrate-serving-simulation](../../../methods/calibrate-serving-simulation/lesson.md) | common | candidate |
| [cann-attribution-overlap](../../../hardware/ascend/cann-attribution-overlap/lesson.md) | ascend | candidate |
| [cgroup-resource-controls](../../../hardware/host/cgroup-resource-controls/lesson.md) | common | candidate |
| [checkpoint-recovery-consistency](../../../methods/checkpoint-recovery-consistency/lesson.md) | common | candidate |
| [choose-parallel-training-plan](../../../methods/choose-parallel-training-plan/lesson.md) | common | candidate |
| [cite-check-downstream-pr](../../../workflows/cite-check-downstream-pr/lesson.md) | common | candidate |
| [claim-contract](../../../workflows/claim-contract/lesson.md) | common | candidate |
| [comfy-ui](../../../repositories/comfy-ui/lesson.md) | common | candidate |
| [competitor-scan](../../../workflows/competitor-scan/lesson.md) | common | candidate |
| [dcp-async-save-performance](../../../frameworks/pytorch/dcp-async-save-performance/lesson.md) | common | candidate |
| [dense-performance-evidence](../../../methods/dense-performance-evidence/lesson.md) | common | candidate |
| [diagnose-attention-bottlenecks](../../../hardware/cuda/diagnose-attention-bottlenecks/lesson.md) | cuda | candidate |
| [diagnose-vllm-admission-pressure](../../../repositories/vllm/diagnose-vllm-admission-pressure/lesson.md) | common | candidate |
| [diffusers-invocation-state](../../../frameworks/diffusers/diffusers-invocation-state/lesson.md) | common | candidate |
| [draft-acceptance-issue](../../../workflows/draft-acceptance-issue/lesson.md) | common | candidate |
| [dwarfstar](../../../repositories/dwarfstar/lesson.md) | common | candidate |
| [evaluate-elastic-serving-placement](../../../methods/evaluate-elastic-serving-placement/lesson.md) | common | candidate |
| [generation-cache-lifecycle](../../../repositories/mlx-lm/generation-cache-lifecycle/lesson.md) | common | candidate |
| [host-memory-management](../../../hardware/host/host-memory-management/lesson.md) | common | candidate |
| [host-overhead-optimization](../../../hardware/host/host-overhead-optimization/lesson.md) | common | candidate |
| [host-overhead-profiling](../../../hardware/cuda/host-overhead-profiling/lesson.md) | cuda | candidate |
| [husky](../../../repositories/husky/lesson.md) | common | candidate |
| [inference-benchmark-design](../../../methods/inference-benchmark-design/lesson.md) | common | candidate |
| [inference-optimization-casebook](../../../methods/inference-optimization-casebook/lesson.md) | common | candidate |
| [kernel-writing-guide](../../../methods/kernel-writing-guide/lesson.md) | common | candidate |
| [kv-tier-management](../../../repositories/lmcache/kv-tier-management/lesson.md) | common | candidate |
| [lazy-evaluation-stream-lifetimes](../../../frameworks/mlx/lazy-evaluation-stream-lifetimes/lesson.md) | common | candidate |
| [lily](../../../repositories/lily/lesson.md) | common | candidate |
| [lithos-metal](../../../repositories/lithos-metal/lesson.md) | common | candidate |
| [local-dream](../../../repositories/local-dream/lesson.md) | common | candidate |
| [mistral-rs](../../../repositories/mistral-rs/lesson.md) | common | candidate |
| [mlc-llm](../../../repositories/mlc-llm/lesson.md) | common | candidate |
| [mlx-swift-lm](../../../repositories/mlx-swift-lm/lesson.md) | common | candidate |
| [npu-skill-factory](../../../workflows/npu-skill-factory/lesson.md) | common | candidate |
| [optimization-search-policy](../../../methods/optimization-search-policy/lesson.md) | common | candidate |
| [os-process-placement](../../../hardware/host/os-process-placement/lesson.md) | common | candidate |
| [performance-ceiling-analysis](../../../methods/performance-ceiling-analysis/lesson.md) | common | candidate |
| [plan-activation-residency](../../../methods/plan-activation-residency/lesson.md) | common | candidate |
| [project-maya](../../../repositories/project-maya/lesson.md) | common | candidate |
| [pytorch](../../../frameworks/pytorch/pytorch/lesson.md) | common | candidate |
| [reason-hopper-kernels](../../../hardware/cuda/reason-hopper-kernels/lesson.md) | cuda | candidate |
| [repository-evolution-analysis](../../../methods/repository-evolution-analysis/lesson.md) | common | candidate |
| [rsi-evidence](../../../workflows/rsi-evidence/lesson.md) | common | candidate |
| [skill-evolution-playbook](../../../methods/skill-evolution-playbook/lesson.md) | common | candidate |
| [splash](../../../repositories/splash/lesson.md) | common | candidate |
| [storage-io-measurement](../../../hardware/host/storage-io-measurement/lesson.md) | common | candidate |
| [torch-npu](../../../frameworks/torch-npu/torch-npu/lesson.md) | ascend | candidate |
| [torchnpu-device-memory-lifecycle](../../../hardware/ascend/torchnpu-device-memory-lifecycle/lesson.md) | ascend | candidate |
| [torchnpu-pinned-host-memory-lifecycle](../../../hardware/ascend/torchnpu-pinned-host-memory-lifecycle/lesson.md) | ascend | candidate |
| [training-input-pipeline](../../../methods/training-input-pipeline/lesson.md) | common | candidate |
| [training-resource-budget](../../../methods/training-resource-budget/lesson.md) | common | candidate |
| [video-diffusion-optimization](../../../methods/video-diffusion-optimization/lesson.md) | common | candidate |
| [vllm-ascend](../../../repositories/vllm-ascend/lesson.md) | ascend | candidate |
| [vllm-metal](../../../repositories/vllm-metal/lesson.md) | common | candidate |
| [weight-loading-optimization](../../../methods/weight-loading-optimization/lesson.md) | common | candidate |

<a id="unit-source-files"></a>
## Source files

- [_provenance.json](../../../../../repo_packs/inferrsi/knowledge/_provenance.json)
