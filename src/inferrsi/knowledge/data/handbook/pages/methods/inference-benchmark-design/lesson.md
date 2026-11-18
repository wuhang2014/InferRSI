<!-- handbook
{
  "id": "inference-benchmark-design",
  "kind": "procedure",
  "aliases": [
    "checkout:inference-benchmark-design",
    "inferrsi.common.skills.inference_benchmark_design",
    "package:inferrsi.common.skills.inference_benchmark_design"
  ],
  "tags": [
    "benchmark",
    "evaluation",
    "serving",
    "measurement",
    "task-quality",
    "reference-parity",
    "agentic-coding",
    "work-agents",
    "aiperf",
    "tts",
    "full-duplex",
    "image-generation",
    "video-generation",
    "asr",
    "stream-boundaries",
    "treatment-delivery",
    "trial-validity",
    "protocol-audit",
    "trial-evidence",
    "result-origin",
    "oracle-boundary",
    "candidate-selection",
    "accepted-prefix",
    "state-restoration",
    "completion-accounting",
    "vla",
    "embodied",
    "action-chunks",
    "closed-loop",
    "gpu-timing",
    "profiler-attribution",
    "measurement-validity"
  ]
}
-->

# Inference Benchmark Design

> Recorded state `candidate` · empirical validation `not_run` · [Source](../../../../skill_library/methods/inference-benchmark-design/SKILL.md) · [Scope and provenance](../../../../skill_library/methods/inference-benchmark-design/metadata.json) · [Catalog record](../../../../repo_packs/inferrsi/knowledge/common/skills/inference-benchmark-design.json) · [Catalog revision](../../../../repo_packs/inferrsi/knowledge/_provenance.json) · [Parent reading](../../library/overview.md)

Select task quality gates, reference parity checks and performance workloads for text, agentic coding, work agents, cache-aware ASR, TTS, full-duplex audio/video, image, video and VLA inference. Covers AIPerf AgentX/Exgentic replay, vLLM/SGLang benchmark boundaries, VLA action-chunk timing and quality, SLO-aware metrics and InferRSI integration.

Status: candidate. Source-grounded from vllm-evolve @ 43cc82c and
InferRSI evidence framework @ 4c8e1285.

<a id="unit-select-the-task-and-its-evaluation-contract"></a>
## Select the task and its evaluation contract

Read [task-specific benchmark selection](references/task-benchmark-selection.md)
when choosing quality evaluators, reference parity and a performance workload.
It covers text, agent replay, TTS, three full-duplex task families, images and
videos, with pinned provenance from InferRSI issue #60. Use the
[command templates](references/benchmark-commands.md) for entry points and a
bounded HTTP smoke. These references are candidate knowledge, not qualification
of every model or backend.

For cache-aware speech recognition, read the
[ASR stream-boundary procedure](references/cache-aware-asr-stream-boundaries.md)
before selecting tests or comparing chunk latency. It separates startup/steady geometry, decoded
progress, stream-slot reuse, reset, EOU and EOF; its source tests and
author benchmark reports are not local model or serving qualification.

For streaming TTS measurements tied to playback deadlines or dependent chunks,
read [dependency-aware TTS playout](references/dependency-aware-tts-playout.md).
It traces server PCM credit, client playback events, independent batching work
and partial pipeline costs at one pinned source; it adds no hardware coverage,
runtime or locally reproduced quality/performance result.

For VLA and robot deployment comparisons, read
[observation-to-action timing and closed-loop quality](references/embodied-cpp-boundary-and-quality.md).
Define the complete CPU-action boundary, distinguish generated and replayed
horizons from the control clock, and reconcile per-task quality, precision and
the measured source revision. Freeze latency/jitter and quality objectives for
the actual control use case; per-generated-action cost is amortization.

For treatment-enabled tuning comparisons or claimed protocol integrity, read
[treatment delivery and trial validity](references/autotunebench-trial-validity.md).
Trace feedback to the eligible consumer input and apply the frozen arm-validity
precedence before interpreting benefit, saturation or a null.

For GPU timing comparisons, read
[measurement validity and profiler attribution](references/gpu-measurement-validity.md).
Separate normal E2E timing from profiler replay, test within-run attribution
assumptions and retain work counts plus the predicted mechanism signature.
This is candidate guidance; its task-supplied observations remain unverified.

For hybrid speculative state-restoration or completion evidence, read the
[NInfer validation contract](references/ninfer-state-and-completion-contracts.md).
Freeze a coupled checkpoint and same-physical-block state oracle; distinguish
zero accepted drafts from zero adopted inputs, logical commit from device
retirement, and selected steady intervals from complete-cohort denominators.
Its source contracts and historical author reports are not native parity results.

Freeze one primary objective, timing boundary, quality gates and sample/failure
accounting before optimization. Recorded agent task scores and replay completion
do not establish current task success; a VBench prompt workload does not compute
VBench quality. Missing coverage stays INCONCLUSIVE. Numeric gates and required
workload regimes are campaign choices, not repository-wide defaults.

<a id="unit-core-principle-goodput-over-throughput"></a>
## Core principle: goodput over throughput

Raw throughput (tokens/second, frames/second) is misleading because a system
can maximize throughput by accepting requests it then fails to serve within
the user's latency expectation. The meaningful metric is goodput: the rate of
requests that complete AND meet the declared SLO.

```
goodput = (requests completed within SLO) / time
```

A candidate that improves raw throughput by trading latency away cannot "win"
under a goodput metric if it causes SLO violations.
Source: vllm-evolve README @ 43cc82c.

<a id="unit-workload-regimes-to-select-for-the-campaign"></a>
## Workload regimes to select for the campaign

A single benchmark run at one concurrency level does not characterize serving
performance. These source-derived regimes answer different questions; choose
the required set from the deployment use case and freeze it before comparison:

| Regime | Load level | What it answers |
|--------|-----------|----------------|
| Throughput | Saturating load, with observed bottleneck and queue state | Max sustainable goodput at peak load |
| Latency | Low load | Responsiveness for latency-sensitive workloads |
| Replay | Real or representative trace | Behavior under actual production burstiness |

An optimization may improve one regime while degrading another. Report all
required regimes separately; do not aggregate into a single score without disclosing
how the aggregation was done.

For replay, standard trace sources (from vllm-evolve): BurstGPT, Azure,
ShareGPT, Mooncake. Use the trace that matches your actual deployment pattern.

<a id="unit-verdict-semantics"></a>
## Verdict semantics

The upstream vllm-evolve comparison labels are:

| Verdict | Condition |
|---------|----------|
| better | Improvement in all required regimes, no regression in any |
| worse | Regression in any required regime |
| inconclusive | Too noisy to distinguish (see below) |

These labels are not InferRSI's verdict enum. InferRSI uses PASS / FAIL /
INCONCLUSIVE and the campaign's frozen gates. `high_variance_inconclusive`
is a useful diagnostic reason: it means the
measurement signal is not strong enough to support a claim in either direction.
Do not report an inconclusive result as a win. Record it as INCONCLUSIVE and
note the variance level.
Source: vllm-evolve README @ 43cc82c.

<a id="unit-statistical-requirements"></a>
## Statistical requirements

Freeze repetition count, workload seeds and the decision rule in the campaign.
The upstream guidance recommends multiple seeds and median goodput with IQR or
range. State whether a repetition changes the workload seed or repeats identical
inputs. If using `max - min > threshold × median` as a noise gate, choose the
threshold in the acceptance plan; this skill defines no universal numeric bar.
InferRSI's built-in median/range summaries are descriptive, not a significance
test or automatic enforcement of that noise gate.

The decision of which regimes must improve and which must not regress is the
caller's policy, not the benchmark's. Encode it in a decision config file
(`decision.yaml` in vllm-evolve) so it is explicit, versioned, and auditable.

<a id="unit-audit-a-supplied-fixed-workload-report"></a>
## Audit a supplied fixed-workload report

Preserve the request-to-trial grouping and every observation covered by the
contract. Late requests and outliers remain included unless the frozen protocol
explicitly excludes them; retain exclusion and failure counts. Apply aggregation
in the declared order: a median of per-trial request means uses every included
request to calculate each trial mean, then takes the median across trials. A
pooled request median is a different statistic, especially with unequal trial
sizes. If the report omits an aggregation rule that changes the verdict, expose
that ambiguity rather than choosing one after seeing the result.

For a lower-is-better metric with a positive baseline, calculate percentage
reduction as `100 * (baseline - candidate) / baseline` and compare it with the
declared threshold before rounding. Check workload equivalence, output quality
and completion evidence separately from this arithmetic. Report the computed
threshold result and any missing evidence under the frozen contract's verdict
semantics; an attractive aggregate alone does not establish an accepted gain.

<a id="unit-what-must-be-pinned-before-comparing-two-runs"></a>
## What must be pinned before comparing two runs

Every valid A/B comparison requires these to be identical:
- Hardware (exact device SKU, driver version, firmware).
- Software stack (framework version, model weights revision).
- Input distribution (same trace or same generation config and seed).
- Benchmark configuration (concurrency levels, SLO thresholds, timeout).
- Warmup (same warmup protocol, excluded from measurement).
- Measurement protocol (same window duration, same number of seeds).

If any of these differ between the baseline and candidate run, the comparison
is invalid. "Same hardware class" is not the same as "same device."

<a id="unit-shared-machine-measurement-discipline"></a>
## Shared-machine measurement discipline

On shared infrastructure (multiple users, shared GPU/NPU allocation):

- Cross-window comparison is invalid. Run baseline and candidate within the
  same time window (interleaved or back-to-back in the same allocation).
- Record neighbor load state before each run. If it changes between runs,
  report the comparison as potentially confounded.
- Dedicate devices: do not share GPU devices between the baseline server and
  the candidate server in the same comparison run.

Source: MindIE-SD perf-gate skill @ 8481d39b (window discipline for NPU).

<a id="unit-what-a-benchmark-cannot-prove"></a>
## What a benchmark cannot prove

- A benchmark win at one concurrency level does not imply a win at other
  concurrency levels.
- A benchmark win with synthetic traces does not imply a win under real
  production traffic.
- A benchmark win on one model does not transfer to other models without
  re-running.
- A benchmark win on one hardware SKU does not transfer to other SKUs.
- Microbenchmark improvement does not imply E2E benchmark improvement.

State these scope boundaries explicitly in any report that cites benchmark
results.

<a id="unit-search-integrity-and-final-state-verification"></a>
## Search integrity and final-state verification

Freeze workload hashes, output/work semantics, permitted approximations, quality
checks, timing events and developer-versus-held-out splits. Verify that measured
work actually occurs; a quality pass does not certify a truthful timing path.
Keep fast probes separate from full evaluation, and preserve invalid, failed and
inconclusive trials. A simulator shortlist requires calibrated load/capacity
coverage and does not replace measurements.

Compare search methods at matched total budgets. Separate search/API cost from
steady-state serving cost; independent per-engine searches are not one equal-budget
engine-selection run. Keep different SLOs, baselines, resources and aggregation
rules explicit. Before reporting, restart the final code/config artifact and
validate that exact state; report best-seen results separately from delivered ones.

[Reviewed experiment discipline](../performance-ceiling-analysis/references/papers-20261015/govern-optimization-experiments/procedure.md)
and [source audit](../performance-ceiling-analysis/references/papers-20261015/references/inferencebench.md)
retain author-reported evidence and counterexamples. No local experiment is
established by integrating these notes.

For controlled kernel-agent comparisons, use the
[JustGoal source reference](references/justgoal-evaluation-contracts.md).
Keep model/budget/task scope, independent acceptance, released versus repaired
artifacts and workspace/stream/cache contracts explicit. Its results remain
author-reported; it adds no runner or device/performance qualification.

For source-bound kernel trial records, read
[trial identity, evaluator evidence and candidate selection](references/xeforge-trial-evidence.md).
Keep tool origin, actual oracle, unresolved performance, selection and delivered
eligibility distinct; a retained parity candidate is not a measured gain.

<a id="unit-evidence-trail-requirements-inferrsi-compatibility"></a>
## Evidence trail requirements (InferRSI compatibility)

A benchmark campaign that claims PASS under InferRSI's evidence framework
must produce:
```
evidence/<campaign-id>/
  plan/
    hypothesis.md         # what is being tested and why
    runspec.json          # frozen RunSpec (repo × revision × backend × device × model × scenario)
    slo.yaml              # declared SLO and threshold
    decision.yaml         # which regimes must improve / must not regress
  results/
    regime-throughput/    # raw metrics, logs, per-seed records
    regime-latency/
    regime-replay/
    verdict.json          # PASS / FAIL / INCONCLUSIVE with reasons
  patch/
    candidate.patch       # the exact change being evaluated
  validator/
    validate.py           # frozen validator script
```

A run without a frozen RunSpec is INCONCLUSIVE regardless of the metric values.
A run whose validator was modified after the plan was frozen is INCONCLUSIVE.
Source: InferRSI AGENTS.md and rsi-evidence skill @ 4c8e1285.

<a id="unit-scoped-internal-experience"></a>
## Scoped internal experience

Read the single authoritative [admission/drain occupancy case](../inference-optimization-casebook/cases/admission-drain-occupancy.md) when interpreting finite service cohorts. It separates recorded observation, action and interpretation; phase-selected occupancy is not end-to-end gain. The original frozen evidence remains linked, not copied. This shared reference is included in the packaged skill library; standalone folder export is not supported.

<a id="unit-when-this-applies"></a>
## When this applies

- **Scope** — Selecting task quality gates, reference parity checks and performance workloads for text, agentic coding, work agents, cache-aware ASR, TTS, full-duplex audio/video, image and video inference, and designing goodput-based multi-regime comparisons that fit InferRSI's evidence trail; interpreting treatment delivery, arm validity and stated-versus-observed protocol enforcement in supplied tuning reports; interpreting source-bound kernel trial origin, host evaluator outcomes, unresolved performance and measured-only versus manual candidate selection; designing and interpreting the selected NInfer hybrid speculative state-restoration and completion validation contract; designing or auditing VLA deployment comparisons with explicit observation-to-action boundaries, generated/replayed horizons, per-task quality and source/precision identity; assessing GPU timing validity and profiler-based attribution of kernel/inference gains
- **Prerequisites** — The primary objective, timing boundary, quality gates, sample/failure accounting, required regimes, repetitions, seeds and decision rule are frozen before optimization; baseline and candidate share hardware, software stack, input distribution, benchmark configuration, warmup and measurement protocol, and on a shared machine also one time window and dedicated devices; cache-aware ASR also requires the selected model/config and first/steady geometry, decoded clock and reset/EOU/EOF boundaries to be established; VLA comparisons also freeze generated/replayed horizons, initial-state/noise protocol and intended precision or quantization treatment
- **Input contract** — The task family and deployment use case; candidate quality evaluators and reference parity; the declared SLO and the caller's policy on which regimes must improve or must not regress; for an audit, a supplied fixed-workload report with request-to-trial grouping, exclusion and failure counts and the declared aggregation rule; for a treatment audit, the frozen delivery/arm-validity rules, run/candidate identities, feedback and consumer-input evidence, and per-arm raw records; for a kernel trial audit, complete saved candidate bytes and IDs, baseline/spec/reference/variant identities, result-origin fields, raw host outcome and return code, named gate and persisted ratio, actual oracle and the selecting/delivering caller; for the NInfer slice, a complete checkpoint/frontier identity, physical verify-block/state oracle, final adopted extents and correlated execution/termination records; for VLA audits, the declared CPU input/output boundary, source/fixture/checkpoint/processor identities, per-task trial scope and available raw records or explicit artifact gaps
- **Produced artifact** — A frozen benchmark design with evaluators, reference parity, primary objective, timing boundary, quality gates, required regimes, repetition and seed rules and an explicit decision config, plus the evidence-tree layout a PASS claim must produce; for a supplied report, the computed threshold result and missing evidence. Candidate knowledge, not qualification of any model or backend; for a treatment audit, a contract-bound eligibility and interpretation report separating treatment exposure, observed checks, comparator identity, anomaly disposition and source conflicts; for a kernel trial audit, a source-bound interpretation separating artifact/cohort identity, origin, oracle, performance resolution and selected-versus-delivered eligibility, without promoting kernel parity into a gain or whole-model acceptance; for the NInfer slice, a source-bound validation plan or report interpretation that separates state-oracle evidence, final adoption, retirement and workload denominators; for VLA reports, a timing/denominator and precision reconciliation with per-task quality/completion accounting and source-artifact limits; for GPU attribution, a source-grounded measurement plan or interpretation binding environment, paired timing, work counts, predicted signature and E2E decomposition with explicit assumptions and unresolved evidence
- **Failure modes**
  - Raw throughput is optimized in place of goodput, so requests served outside the SLO count toward a win
  - One concurrency level or one undisclosed aggregate score stands in for all required regimes
  - Recorded agent task scores or replay completion are read as current task success, or a VBench prompt workload as computed VBench quality
  - An upstream better/worse/inconclusive label is used as InferRSI's PASS/FAIL/INCONCLUSIVE verdict
  - Runs on the same hardware class, in different time windows or on shared devices are compared as if pinned
  - A quality pass is taken to certify that the timed work actually occurred
  - Best-seen results are reported as delivered without restarting and validating the final code/config artifact
  - A cache-aware ASR EOU is treated as EOF or full reset, nominal chunk duration as the decoded mel frontier, or shape-only geometry PASS as a native model-state test
  - An enabled treatment or stored feedback summary is taken as proof of delivery to the next eligible consumer
  - A failed arm-validity condition is overridden by a favorable best timing or a saturation/null interpretation
  - Complete gate keys or zero recorded failures are read as proof that every declared protocol check ran
  - A tool-origin measured marker or completed status is treated as a resolved performance gain
  - A displayed/manual best, baseline copy or edited candidate is reported as the eligible measured delivery
  - Ratio omission alone is assumed to clear an earlier ratio, or baseline agreement is treated as independent semantic correctness
  - Zero accepted drafts is treated as zero adopted input, or a matching token prefix is used to splice unrelated State and KV checkpoints
  - ResultReady or a commit receipt is treated as DeviceRetired, or selected full-batch intervals are compared with complete-cohort rates under one unlabeled denominator
  - Generated-action amortization is read as action-response latency or actual control frequency
  - Matching structural pair fields are taken to certify matched effective compute precision or quality equivalence
  - An aggregate VLA success rate conceals task-specific losses or missing/skipped episodes
  - A public current script, recorded experiment revision or binary hash is treated as the exact measured dirty source patch
  - Whole-device fallback memory is relabelled as process-attributed memory or compared with simulator-inclusive/allocator quantities
  - NCU replay durations are substituted for normal E2E evidence, or an untouched region is treated as a universal clock without checking common drift and critical-path assumptions
  - Unexplained gains, changed baseline modes or same-named JIT loads are adopted without binding actual work, module identity and predicted profiler signatures
- **Refusal point** — Records missing coverage and high-variance results as INCONCLUSIVE rather than a win; a run without a frozen RunSpec, or whose validator changed after the plan was frozen, is INCONCLUSIVE regardless of metric values; sets no universal numeric gate or noise threshold; withholds causal treatment benefit/null conclusions when required delivery or arm eligibility is unverified, and preserves conflicts between stated protocol, exported code and source reports; withholds a kernel gain for unresolved performance or an unbound comparison and identifies missing independent semantic evidence when only baseline agreement is available; withholds native state-correctness and cancellation/reuse conclusions when the required same-block oracle, checkpoint identity or matching receipt is missing; withholds VLA quality-preservation, runtime-only attribution, control-rate or current-build conclusions when their required precision, per-task, timestamp or measured-source evidence is missing

<a id="unit-putting-the-idea-to-work"></a>
## Putting the idea to work

- Freeze one primary objective, timing boundary, quality gates and sample/failure accounting before optimization.
- Choose the required regimes from the deployment use case, report each separately, and record which must improve or must not regress in a versioned decision config.
- Use the replay trace that matches the actual deployment pattern.
- State the concurrency, trace, model, SKU and microbenchmark scope boundaries in any report that cites benchmark results.
- Trace treatment to its eligible consumer and apply the frozen arm-validity precedence before attributing benefit, saturation or a null.
- Bind the complete saved candidate and comparator cohort; keep result origin, actual oracle, named gate/ratio and delivered eligibility separate.
- For hybrid speculative comparisons, freeze the coupled restore point, same-physical-block oracle, zero-draft/zero-adoption controls and complete-cohort versus steady-phase denominators before interpreting a result.
- Separate complete VLA request cost, generated/replayed action denominators and actual control cadence; retain per-task quality and measured-source/precision limits.
- For GPU comparisons, retain timestamped clocks/temperature/power, same-run region shares and work counts; test the predicted mechanism signature and paired E2E change before adopting a gain.

<a id="unit-limits-of-this-evidence"></a>
## Limits of this evidence

- Source-derived candidate; no local efficacy validation.
- Original typed source inventory is not normalized; retain source identities and limits in the procedure/readsets.
- Task benchmark knowledge is distilled from issue #60 with selected pinned-source rechecks; no all-task runtime qualification or optimization benefit is established.
- Benchmark feasibility and package-consumption checks do not promote this candidate or replace task quality, repeated A/B and service qualification.
- The pinned NeMo-Speech.cpp ASR reference covers selected source/test definitions and author-reported benchmark boundaries; native model/device, decoder internals, quality, long-audio/load and service behavior remain not_run.
- JustGoal contributes source-only controlled-evaluation and kernel-acceptance guidance; its repaired/retested timings, released-pass counts and protocol differences are author-reported, not locally reproduced or a complete campaign runner.
- The AutoTuneBench reference is source-only: original operational checkpoint/prompt receipts remain unavailable, source contradictions remain explicit, and no tuning, device/performance or agent-efficacy validation was run.
- The Xe-Forge reference is source-only and limited to inspected host/manual/Claude trial paths; named-verdict update predicates and caller defaults remain explicit. Native tests, backend/model/quality/performance/service behavior and agent efficacy were not evaluated, and source/package checks do not promote whole-model support.
- The NInfer reference inspects selected Qwen3.5 GDN/MTP source contracts and unexecuted test definitions; its historical author measurements use a different engine revision. Native state/model/device/quality/performance and efficacy remain unvalidated.
- The Faster CosyVoice reference is source-only: server route credit and client simulated playback remain distinct, reported costs/quality retain their boundaries, overall source rights are UNKNOWN, and native/model/device/audio quality/service/performance are not_run with efficacy not_evaluated.
- The Embodied.cpp reference is source-derived: its public latency arrays allow arithmetic audit, but raw episode recount, exact measured script/dirty patch, effective dispatch and current model/device/service or efficacy qualification remain unresolved.
- The GPU measurement-validity reference is source-only. The within-run normalization and explanation-first adoption procedure is an unverified author proposal; four task-supplied numerical observations have no supplied raw evidence. GPU/profiler, model/quality, L1–L4 and efficacy validation were not run; legacy metric mappings require target-specific queries.

<a id="unit-declared-references"></a>
## Declared references

- [case.admission-drain-occupancy](../inference-optimization-casebook/cases/admission-drain-occupancy.md)
- [../inference-optimization-casebook/cases/admission-drain-occupancy.json](../../../../skill_library/methods/inference-optimization-casebook/cases/admission-drain-occupancy.json)
- [budget-speculative-verification](../../repositories/deepinfer/budget-speculative-verification/lesson.md)
- [audit-recurrent-kv-finalization](../../repositories/vllm-rlt/audit-recurrent-kv-finalization/lesson.md)

<a id="unit-source-files"></a>
## Source files

- [metadata.json](../../../../skill_library/methods/inference-benchmark-design/metadata.json)
- [references/autotunebench-source.json](../../../../skill_library/methods/inference-benchmark-design/references/autotunebench-source.json)
- [references/embodied-cpp-source.json](../../../../skill_library/methods/inference-benchmark-design/references/embodied-cpp-source.json)
- [references/faster-cosyvoice-source.json](../../../../skill_library/methods/inference-benchmark-design/references/faster-cosyvoice-source.json)
- [references/justgoal-source.json](../../../../skill_library/methods/inference-benchmark-design/references/justgoal-source.json)
- [references/ninfer-source.json](../../../../skill_library/methods/inference-benchmark-design/references/ninfer-source.json)
- [references/xeforge-source.json](../../../../skill_library/methods/inference-benchmark-design/references/xeforge-source.json)
