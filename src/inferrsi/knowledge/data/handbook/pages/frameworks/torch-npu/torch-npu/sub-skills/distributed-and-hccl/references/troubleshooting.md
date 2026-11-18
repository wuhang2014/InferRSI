<!-- handbook
{
  "id": "frameworks/torch-npu/torch-npu/sub-skills/distributed-and-hccl/references/troubleshooting",
  "kind": "reference",
  "tags": [
    "torch-npu",
    "ascend",
    "pytorch",
    "distributed-and-hccl"
  ]
}
-->

# HCCL troubleshooting

> Recorded state `candidate` · empirical validation `not_run` · license `NOASSERTION` · [Source](../../../../../../../../skill_library/frameworks/torch-npu/torch-npu/sub-skills/distributed-and-hccl/references/troubleshooting.md) · [Scope and provenance](../../../../../../../../skill_library/frameworks/torch-npu/torch-npu/sub-skills/distributed-and-hccl/metadata.json) · [Parent reading](../lesson.md)

| Symptom | Discriminating check and recovery |
|---|---|
| Device busy/wrong rank placement | Compare local rank to visible NPU count; assign one selected device per worker before group initialization. |
| Group hangs before first op | Check rendezvous/world size and missing ranks, then HCCL stack/device exposure. |
| Some ranks time out later | Compare the first diverging collective sequence, tensor size/dtype and subgroup membership. |
| Consumer sees wrong values after async launch | Wait on work from the actual consumer stream and preserve tensor lifetime; synchronize for host verification. |
| Future says complete but device still busy | Host future completion is not the HCCL end-event; observe device completion. |
| Memory grows with overlap | Inspect retained work/output references and configured allocator-protection mode; avoid deleting safety records. |
| LCCL/RPC/symmetric-memory path unavailable | Qualify that backend/dependency independently; do not substitute an HCCL one-op pass. |

Return a sanitized first-failure trace, exact configuration and rank comparison.
The full native stress/group tests remain blocked on a real multi-device stack.
