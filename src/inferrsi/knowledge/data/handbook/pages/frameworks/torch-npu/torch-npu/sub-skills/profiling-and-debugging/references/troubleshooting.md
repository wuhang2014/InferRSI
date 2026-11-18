<!-- handbook
{
  "id": "frameworks/torch-npu/torch-npu/sub-skills/profiling-and-debugging/references/troubleshooting",
  "kind": "reference",
  "tags": [
    "torch-npu",
    "ascend",
    "pytorch",
    "profiling-and-debugging"
  ]
}
-->

# Profiling troubleshooting

> Recorded state `candidate` · empirical validation `not_run` · license `NOASSERTION` · [Source](../../../../../../../../skill_library/frameworks/torch-npu/torch-npu/sub-skills/profiling-and-debugging/references/troubleshooting.md) · [Scope and provenance](../../../../../../../../skill_library/frameworks/torch-npu/torch-npu/sub-skills/profiling-and-debugging/metadata.json) · [Parent reading](../lesson.md)

| Symptom | Check and recovery |
|---|---|
| Empty trace | Confirm active schedule reached, `prof.step()` called and activities supported. |
| CPU events only | Check actual NPU activity/runtime collector; CPU activity is not accelerator verification. |
| Memory timeline absent | Enable shapes, memory and stack or modules; inspect warnings and output path. |
| Collection exists but viewer/parser fails | Preserve raw trace; report analysis failure separately and use a compatible parser. |
| Timing changes greatly with debugging | Restore launch blocking/sanitizer settings and compare synchronized measurements. |
| Trace has missing device metrics | CANN feature/metric support can differ by stack/hardware; report unavailable counters explicitly. |
| Sanitizer reports use after free/race | Route to memory lifetime and producer/consumer ordering, then rerun the reduced case. |

A produced trace is evidence to inspect, not a PASS on throughput, convergence,
service SLO or hardware health.
