<!-- handbook
{
  "id": "calibrate-serving-simulation",
  "kind": "procedure",
  "aliases": [
    "checkout:calibrate-serving-simulation",
    "inferrsi.common.skills.calibrate_serving_simulation",
    "package:inferrsi.common.skills.calibrate_serving_simulation"
  ]
}
-->

# Calibrate a serving-simulation shortlist

> Recorded state `candidate` · empirical validation `not_run` · [Source](../../../../skill_library/methods/calibrate-serving-simulation/SKILL.md) · [Scope and provenance](../../../../skill_library/methods/calibrate-serving-simulation/metadata.json) · [Catalog record](../../../../repo_packs/inferrsi/knowledge/common/skills/calibrate-serving-simulation.json) · [Catalog revision](../../../../repo_packs/inferrsi/knowledge/_provenance.json) · [Parent reading](../../library/overview.md)

Build an evidence-gated serving-configuration shortlist from a profiled simulator while separating empirical predictions from physical bounds and near-capacity queueing risk.

Use when simulation or a cost model is proposed to reduce deployment experiments. This candidate extends existing `performance-ceiling-analysis`, `optimization-search-policy` and `inference-benchmark-design`; it does not replace their ceilings or measurement contract. Reading this skill does not authorize execution; follow the current task's scope.

<a id="unit-inputs-and-prerequisites"></a>
## Inputs and prerequisites

Require model/shape/dtype, actual kernel/runtime revision, graph mode, GPU/host/topology, request length and arrival distribution, total resources/cost basis, memory limits, latency definitions and percentile SLOs. Read [Vidur evidence](references/source-notes.md) and [evidence types](references/source-notes.md). If any essential identity is missing, mark that dimension unknown rather than borrowing a paper default.

For Infera serving-tuner output, read the [provenance reference](references/infera-serving-search/overview.md) before using a shortlist. It distinguishes actual fidelity, the seed-only comparator, evaluated-trial retention and scalar versus DES metrics; independent trace-ranking calibration remains proposed and `not_run`.

<a id="unit-procedure-p"></a>
## Procedure (P)

1. Classify each estimate: physical feasibility bound, measured attainable envelope, Amdahl-style conditional impact, or empirical prediction. Never label learned runtime output a bound.
2. Build operator dependency signatures: current tokens; phase and context-length distribution; KV bytes; communication payload plus topology. Keep prefill and decode separate. Record how sharding and memory planning enter the model.
3. Record calibration domain and held-out coverage. Preserve skewed attention cases, small-model host overhead and tile/shape transitions. If the predictor relies on summed KV volume, challenge batches with equal volume but unequal context distributions.
4. Validate plans must distinguish operator/iteration errors from static normalized execution time and dynamic E2E/queue delay. Include the intended load regime and capacity boundary; do not substitute a low-load check for an SLO claim. No checks are run under this skill without separate execution authorization.
5. Enumerate feasible configuration families under total resource cost and memory budgets. If using capacity binary search, verify the empirical monotonic/stationary premise and define its scheduling-delay threshold. Treat overloaded samples explicitly.
6. Filter on all latency/quality constraints together. Retain nondominated alternatives and uncertainty bands, including differing mechanisms, rather than one predicted winner. If uncertainty exceeds rank separation, label the ordering unresolved.
7. Produce a small future-measurement shortlist whose trials discriminate among competing explanations. Recalibration triggers include workload drift, kernel/graph/runtime changes, new hardware/topology and mismatched residuals.

<a id="unit-output"></a>
## Output

A bounded decision memo: input identities; model assumptions; evidence type; exact metrics/denominators; unsupported dimensions; candidates and predicted ranges; joint constraint checks; next discriminating trial; rollback/finalization requirements. Prediction and measurement columns must not be conflated.

<a id="unit-failure-stop-conditions"></a>
## Failure / stop conditions

Stop predictive certification if profiles are missing, topology is substituted, error grows near capacity, or host overhead is omitted. Do not assert universal error below9%: Vidur AppendixA has12.65% maximum error in a specified near-capacity case. Do not claim current vLLM, asynchronous PP or NPU support from this historical simulator paper.

<a id="unit-resource-contract"></a>
## Resource contract

The local `references/source-notes.md` retains the Vidur evidence. The [Infera reference](references/infera-serving-search/overview.md) and its [source record](../../../../skill_library/methods/calibrate-serving-simulation/references/infera-serving-search/source-record.json) retain the separate implementation example and its limits. These owner-local resources support selective consumption. Optional comparison notes and cases are linked through the owning ceiling skill. Existing InferRSI skill names above are reconciliation targets, not runtime dependencies.

<a id="unit-when-this-applies"></a>
## When this applies

- **Scope** — Building an evidence-gated serving-configuration shortlist when a profiled simulator or cost model is proposed to reduce deployment experiments; extends performance-ceiling-analysis, optimization-search-policy and inference-benchmark-design without replacing their ceilings or measurement contract
- **Prerequisites** — The packaged Vidur evidence and evidence-type notes are read; reading the skill does not authorize execution, and no validation check runs under it without separate execution authorization
- **Input contract** — Model, shape and dtype; actual kernel/runtime revision; graph mode; GPU, host and topology; request length and arrival distribution; total resources and cost basis; memory limits; latency definitions and percentile SLOs
- **Produced artifact** — A bounded decision memo with input identities, model assumptions, evidence type, exact metrics and denominators, unsupported dimensions, nondominated candidates with predicted ranges, joint constraint checks, the next discriminating trial and rollback/finalization requirements, keeping prediction and measurement columns apart; a shortlist for future measurement, not a measured result
- **Failure modes**
  - Learned runtime output is labeled a physical bound
  - A missing identity is filled with a paper default, or topology is substituted, instead of being marked unknown
  - A low-load check stands in for an SLO claim at the intended load regime and capacity boundary
  - A predictor that relies on summed KV volume hides batches with equal volume but unequal context distributions
  - Capacity binary search is applied without verifying its monotonic/stationary premise or treating overloaded samples explicitly
  - One predicted winner is reported when uncertainty exceeds rank separation
- **Refusal point** — Stops predictive certification when profiles are missing, topology is substituted, error grows near capacity or host overhead is omitted; labels an ordering unresolved when uncertainty exceeds rank separation; asserts neither universal error below 9% nor current vLLM, asynchronous PP or NPU support from the historical simulator paper

<a id="unit-putting-the-idea-to-work"></a>
## Putting the idea to work

- Classify every estimate as a physical bound, measured envelope, Amdahl-style conditional impact or empirical prediction before comparing configurations.
- Keep prefill and decode separate in the operator signatures, and record how sharding and memory planning enter the model.
- Recalibrate after workload drift, kernel/graph/runtime changes, new hardware or topology, or mismatched residuals.

<a id="unit-limits-of-this-evidence"></a>
## Limits of this evidence

- Source-derived candidate; no local efficacy validation.

<a id="unit-source-files"></a>
## Source files

- [metadata.json](../../../../skill_library/methods/calibrate-serving-simulation/metadata.json)
