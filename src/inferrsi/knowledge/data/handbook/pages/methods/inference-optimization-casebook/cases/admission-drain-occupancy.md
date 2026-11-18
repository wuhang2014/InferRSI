<!-- handbook
{
  "id": "case.admission-drain-occupancy",
  "kind": "case",
  "aliases": [
    "checkout:case.admission-drain-occupancy"
  ],
  "carry": [
    "unit-when-this-applies",
    "unit-limits-of-this-evidence"
  ]
}
-->

# Admission occupancy is not whole-run occupancy

> Recorded state `historical_observation` · [Source](../../../../../skill_library/methods/inference-optimization-casebook/cases/admission-drain-occupancy.md) · [Scope and provenance](../../../../../skill_library/methods/inference-optimization-casebook/cases/admission-drain-occupancy.json) · [Parent reading](../lesson.md)

Campaign INCONCLUSIVE. This extraction adds no performance validation. Kind,
origin, state and source identities belong to the
[typed source and scope record](../../../../../skill_library/methods/inference-optimization-casebook/cases/admission-drain-occupancy.json).

<a id="unit-observation"></a>
## Observation

In the recorded Drama3 B300 C64 continuous-admission diagnostic (256 requests),
the owning CPU annotations counted 802 scheduler steps: 1 prefill, 37 mixed,
762 decode and 2 empty. During the client-admission interval, pure decode averaged
60.718 active requests out of 64; final drain averaged 8.793. The whole-trace
pure-decode average was 28.146. Scheduled prompt entries may be chunks, not
unique requests. These are recorded diagnostic observations, not new measurements.

<a id="unit-action"></a>
## Action

The original investigation separated the client-admission and drain intervals,
counted scheduler execution annotations rather than PIECEWISE graph fragments,
and retained the full request cohort for acceptance. No measurement is rerun by
reading this case.

<a id="unit-interpretation"></a>
## Interpretation

A whole-run mean batch can be dominated by drain. Using it as sustained-admission
occupancy can misidentify scheduling headroom. Conversely, a near-full batch in
a selected interval does not establish a service speedup. Client in-flight counts
also include queueing and codec work; CPU/GPU clock alignment was approximate.
This interpretation is narrower than a causal diagnosis of the service limit.

<a id="unit-applicability-and-counter-signals"></a>
## Applicability and counter-signals

Use for finite autoregressive service cohorts with ongoing admission, mixed
prefill/decode and a final drain. Retain phase definitions and actual generated
work. Counter-signals include no ongoing admission, incomparable input/output
lengths, clocks that cannot be aligned and missing owning annotations. Kernel
sums, annotation unions and SM utilization are different quantities.

Keep all requests and complete quality/repetition groups in the end-to-end
acceptance metric. Do not replace it with a selected-phase rate or a model-only
microbenchmark. Hardware, model and runtime scope comes from the original frozen
plan; another engine or device needs its own evidence.

<a id="unit-preserved-evidence"></a>
## Preserved evidence

- [Acceptance issue #10](https://github.com/InferMatrixLab/InferRSI/issues/10).
- [Original diagnostic section at the inspected repository snapshot](https://github.com/InferMatrixLab/InferRSI/blob/c13027983b853fee3700de6aabde52b72e61885a/evidence/drama3-b300-scale150/results/diagnostic-lessons.md#continuous-admission-profile-and-mixed-backbone-2026-10-16).
- [Frozen plan](https://github.com/InferMatrixLab/InferRSI/blob/c13027983b853fee3700de6aabde52b72e61885a/evidence/drama3-b300-scale150/plan/plan.json).
- Original artifact identity, recorded raw trace and request metadata SHA256:
  the [typed source and scope record](../../../../../skill_library/methods/inference-optimization-casebook/cases/admission-drain-occupancy.json).
  Raw bytes were not independently retrieved or rehashed for this extraction.

The local frozen evidence remains untouched. Observation is carried from its
2026-10-16 report; extraction inspected that section on 2026-10-16. No missing
model pin, runtime revision or repeated acceptance outcome is reconstructed.

<a id="unit-when-this-applies"></a>
## When this applies

- Continuous admission, mixed prefill/decode and final drain
- Recorded Drama3 B300 C64 diagnostic only

<a id="unit-limits-of-this-evidence"></a>
## Limits of this evidence

- Campaign INCONCLUSIVE
- No new measurement or trace reproduction
- Selected-phase occupancy is not service throughput
- Raw evidence remains under its existing owner

<a id="unit-split-admitted-traffic-from-the-final-drain-when-reading-decode-occupancy"></a>
## Split admitted traffic from the final drain when reading decode occupancy

- **Outcome** — caveat
- **Reason** — Across the 256-request B300 diagnostic, pure decode averaged 60.718 of 64 active requests during admission, 8.793 in drain and 28.146 over the full trace. The trace-wide mean cannot identify how full decode was while requests were still entering.
- **Revisit when** — Mark the client admission interval and the final drain in the trace before using occupancy to select a scheduling hypothesis.
- **Keywords**
  - active decode batch
  - continuous admission
  - final drain
  - whole-run occupancy
  - C64
- **Scope** — local
- **Bounds** — Drama3 B300, 256 requests and a C64 continuous-admission diagnostic; approximate CPU/GPU clock alignment.

<a id="unit-count-scheduler-steps-using-owning-cpu-annotations"></a>
## Count scheduler steps using owning CPU annotations

- **Outcome** — caveat
- **Reason** — The owning CPU annotations count 1 prefill, 37 mixed, 762 decode and 2 empty steps, totaling 802. PIECEWISE fragments describe graph execution, and scheduled prompt entries may describe chunks.
- **Revisit when** — Verify annotation ownership, align the clocks and pair the counts with actual generated work when profiling another trace.
- **Keywords**
  - owning CPU annotation
  - PIECEWISE
  - mixed batch
  - prefill chunks
  - scheduler steps
- **Scope** — regime_bound

<a id="unit-carry-the-complete-cohort-into-the-service-gate"></a>
## Carry the complete cohort into the service gate

- **Outcome** — caveat
- **Reason** — Near-full decode occupancy in a selected interval is a diagnostic. The service decision still depends on all requests, complete quality and repetition groups, and the end-to-end metric.
- **Revisit when** — Use phase statistics to pick a hypothesis. Evaluate the resulting change with the unchanged complete cohort and matched frozen service controls.
- **Keywords**
  - acceptance gate
  - service throughput
  - request cohort
  - quality groups
  - model-only microbenchmark
- **Scope** — general

<a id="unit-source-files"></a>
## Source files

- [admission-drain-occupancy.json](../../../../../skill_library/methods/inference-optimization-casebook/cases/admission-drain-occupancy.json)
