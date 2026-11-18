<!-- handbook
{
  "id": "frameworks/torch-npu/torch-npu/sub-skills/training-and-precision/references/troubleshooting",
  "kind": "reference",
  "tags": [
    "torch-npu",
    "ascend",
    "pytorch",
    "training-and-precision"
  ]
}
-->

# Precision troubleshooting

> Recorded state `candidate` · empirical validation `not_run` · license `NOASSERTION` · [Source](../../../../../../../../skill_library/frameworks/torch-npu/torch-npu/sub-skills/training-and-precision/references/troubleshooting.md) · [Scope and provenance](../../../../../../../../skill_library/frameworks/torch-npu/torch-npu/sub-skills/training-and-precision/metadata.json) · [Parent reading](../lesson.md)

| Symptom | Recovery/check |
|---|---|
| Scaler silently disabled with warning | Check `is_enabled()` and actual device availability before treating a step as AMP coverage. |
| `Attempting to unscale FP16 gradients` | Inspect parameter/gradient dtypes and selected scaler contract; avoid blanket model-half conversion as a fix. |
| Duplicate unscale error | Move clipping to one unscale boundary per optimizer after accumulation. |
| BCELoss rejected under autocast | Use a mathematically suitable logits-based loss, or an explicitly FP32 region; validate numerical equivalence. |
| Updates skipped on some ranks | Compare overflow consensus, scale state and collective order through HCCL. |
| Fused optimizer changes results | Compare state, hyperparameters, combined buffers and one-step gradients before benchmarking. |
| Resume differs after save/load | Check model/optimizer/scaler/RNG state and async completion; preserve exact checkpoint placement. |

Treat persistent nonfinite values as a correctness issue requiring a reduced
reproduction. A static source explanation cannot clear NPU numerical validation.
