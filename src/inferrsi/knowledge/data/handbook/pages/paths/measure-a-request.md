<!-- handbook
{"id": "measure-a-request", "kind": "path", "tags": ["benchmark", "timing", "admission", "quality"]}
-->

# Measure one inference request and its cohort

Start with a timing result and finish with a sentence that names the work,
population and completion event it describes. You can work through this path
with the retained observations and a sheet of paper.

<a id="unit-readings"></a>
## Reading order

1. Identify the event that stops a timer. [Locate completion](../foundations/measurement-boundaries.md#unit-completion)
2. See how a real array implementation signals readable output. [MLX source observations](../records/dependency/mlx/mlx/execution/evaluation-completion.md#unit-what-the-source-reports)
3. Find the three different occupancy averages in one trace. [Drama3 admission and drain](../methods/inference-optimization-casebook/cases/admission-drain-occupancy.md#unit-observation)
4. Explain which requests belong in your denominator. [Keep the population in the denominator](../foundations/measurement-boundaries.md#unit-cohort)
5. Decide what must be held fixed across the two arms. [Controls for a comparison](../methods/inference-benchmark-design/lesson.md#unit-what-must-be-pinned-before-comparing-two-runs)

<a id="unit-exercise"></a>
## Exercise

A colleague divides the whole-trace mean decode occupancy by the configured
concurrency and concludes that the scheduler left half its slots idle while
clients were arriving. Use the case to identify the missing interval label.

The whole trace includes drain. The recorded admission-only pure-decode mean
was 60.718 out of 64, while the whole-trace mean was 28.146. Those observations
describe a particular trace and cohort. A scheduler change would need a new
matched comparison with all requests and quality gates. [Original interpretation and limits](../methods/inference-optimization-casebook/cases/admission-drain-occupancy.md#unit-interpretation)
