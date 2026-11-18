<!-- handbook
{"id": "test-a-speedup", "kind": "path", "tags": ["roofline", "quality", "validation", "negative evidence"]}
-->

# Evaluate a proposed speedup

A faster kernel, a plausible compute bound and an end-to-end result answer
three different questions. Work from the proposed mechanism to a comparison
that could decide whether it helps the requested workload.

<a id="unit-prerequisites"></a>
## Prerequisites

Name the completed work and cohort used by a timing result. [Timing a request](../foundations/measurement-boundaries.md#unit-completion)

<a id="unit-readings"></a>
## Reading order

1. Derive the compute and traffic terms for one operation. [Conditional time floor](../foundations/bounds.md#unit-floor)
2. Work a dimensional example and identify the missing measurement. [Synthetic bound](../foundations/bounds.md#unit-example)
3. Place the timer at the observed completion event. [Locate completion](../foundations/measurement-boundaries.md#unit-completion)
4. Inspect a change that passed operator checks and failed image quality. [Qwen B300 fused RMSNorm and RoPE](../methods/inference-optimization-casebook/cases/qwen-b300-rejected-directions.md#unit-require-full-image-parity-for-fused-q-k-rmsnorm-and-complex-rope)
5. Match the conclusion to the available comparison. [Evidence verdicts](../workflows/rsi-evidence/lesson.md#unit-verdicts)

<a id="unit-exercise"></a>
## Exercise

What would justify revisiting the rejected fusion in step four? Identify the
specific numerical behavior a changed implementation would preserve. Check
the operator under those conditions, then compare complete native images
under the frozen quality protocol. A service speedup also needs the full
service comparison. [Recorded rejection and revisit condition](../methods/inference-optimization-casebook/cases/qwen-b300-rejected-directions.md#unit-require-full-image-parity-for-fused-q-k-rmsnorm-and-complex-rope)
