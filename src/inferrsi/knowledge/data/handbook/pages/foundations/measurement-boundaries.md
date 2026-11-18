<!-- handbook
{"id": "measurement-boundaries", "kind": "concept", "tags": ["measurement", "completion", "cohort"]}
-->

# What did the clock measure?

Two accurate timers can answer different questions about the same request.
Before interpreting either number, write down the event that starts the clock,
the event that stops it, and the work that has finished between those events.

<a id="unit-completion"></a>
## Locate the completion event

Imagine that a host queues work on an accelerator, returns to the caller, and
later waits for an output. A timer ending at the return measures submission.
A timer ending when the caller can read the checked output also covers the
outstanding work. To interpret either timer, identify who signals completion
and which stream or request that signal covers. The MLX record traces those
events to a particular implementation revision. [MLX evaluation and readable completion](../records/dependency/mlx/mlx/execution/evaluation-completion.md#unit-what-the-source-reports)

<a id="unit-cohort"></a>
## Keep the population in the denominator

A finite batch of requests has a last arrival. After that point requests can
finish while no new requests enter. The active decode batch can shrink during
this drain even when admission kept it nearly full. Label each interval and
count its completed work. Use the full request cohort when the question is how
long it took to serve everyone. The retained Drama3 case shows all three
averages and the annotation used to count steps. [Admission and drain observation](../methods/inference-optimization-casebook/cases/admission-drain-occupancy.md#unit-observation)

<a id="unit-check"></a>
## Check your interpretation

A change reduces host submission time. The last checked output arrives at
the same time for the same requests. Which claim does the observation support?

It supports a shorter submission interval under those controls. A service
claim needs the service metric, complete quality checks and the frozen
comparison for that workload. [Measurement and quality gates](../methods/inference-benchmark-design/lesson.md#unit-core-principle-goodput-over-throughput)
