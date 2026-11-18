<!-- handbook
{
  "id": "repositories/strata/sub-skills/tune-execution",
  "kind": "procedure"
}
-->

# Tune execution

> license `MIT` · [Source](../../../../../../skill_library/repositories/strata/sub-skills/tune-execution/SKILL.md) · [Parent reading](../../lesson.md)

Design and interpret controlled Strata tuning experiments for a specified model, hardware and workload, including expert residency, CPU/PCIe balance, prefill, KV, speculation and concurrency.

Read the [tuning procedure](references/tuning.md). Start with an existing working configuration and preserve its model paths and required options. Record resolved settings from startup logs; requested flags alone do not establish which path ran.

If hardware, workload or acceptable quality loss is missing, give a conditional experiment plan. Select one bottleneck and a small, meaningful candidate set. Use [design-space](../design-space/lesson.md) for architectural changes; require [validate-engine](../validate-engine/lesson.md) before accepting a candidate.

Deliver the baseline, candidate differences, feasibility conditions, correctness gates, raw-result locations, repeated measurements and decision. Report failures and regressions. Never transplant a documented speedup to different hardware or rank a numerically invalid candidate.
