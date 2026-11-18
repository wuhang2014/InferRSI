<!-- handbook
{"id": "conditional-bounds", "kind": "concept", "tags": ["roofline", "headroom", "evidence"]}
-->

# From a resource bound to a measurement

Suppose an operator must read a known number of bytes across one memory tier.
Dividing those bytes by a bandwidth gives a time. What that time means depends
on where the byte count and the bandwidth came from.

<a id="unit-floor"></a>
## Derive a conditional time floor

Let *F* be the required operations, *P* the matching peak operations per
second, *T* the required bytes at the chosen tier, and *B* that tier's peak
bytes per second. Execution must allow at least *F/P* seconds for computation
and *T/B* for traffic. With possible overlap, the larger of the two gives a
conditional floor. Each assumption travels with the result, including the
operation type, device count and traffic boundary. [Roofline input contract](../methods/performance-ceiling-analysis/references/roofline-contract.md#unit-input-fields)

<a id="unit-example"></a>
## Work through a synthetic example

In synthetic units, suppose the compute term is six seconds and the memory
term is ten. Ten seconds is the floor under those assumptions. If the measured
request takes twenty seconds, the subtraction alone cannot tell you which ten
seconds could be removed. Queueing, synchronization and other stages can all
contribute. Identify an interval the proposed change could affect and measure
it under the same workload. The packaged example carries actual units and the
assumptions for its own calculation. [Worked Roofline example](../methods/performance-ceiling-analysis/references/roofline-contract.md#unit-worked-caller-controlled-attachment)

<a id="unit-check"></a>
## Check the argument

What changes if *T* counts logical tensor bytes, while *B* describes physical
HBM traffic? The numerator and rate now describe different boundaries. Establish
the required traffic across HBM before using that term to constrain runtime.
Read the checkpoint and tensor evidence when pricing weight traffic. [Evidence to inspect first](../methods/performance-ceiling-analysis/lesson.md#unit-evidence-to-inspect-first)
