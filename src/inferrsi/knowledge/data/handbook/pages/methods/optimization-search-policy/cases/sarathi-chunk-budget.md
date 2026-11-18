<!-- handbook
{
  "id": "case.sarathi-chunk-budget",
  "kind": "case",
  "aliases": [
    "checkout:case.sarathi-chunk-budget"
  ],
  "carry": [
    "unit-when-this-applies",
    "unit-limits-of-this-evidence"
  ]
}
-->

# Sarathi-Serve: choosing a chunked-prefill token budget

> Recorded state `candidate` · empirical validation `not_run` · [Source](../../../../../skill_library/methods/optimization-search-policy/cases/sarathi-chunk-budget.md) · [Scope and provenance](../../../../../skill_library/methods/optimization-search-policy/cases/sarathi-chunk-budget.json) · [Parent reading](../lesson.md)

This is an attributed, source-derived candidate decision example, not an
observed InferRSI incident. Its edition, source digest, readset and limitations
are in the [case record](../../../../../skill_library/methods/optimization-search-policy/cases/sarathi-chunk-budget.json). The source is Agrawal et al.,
*Taming Throughput-Latency Tradeoff in LLM Inference with Sarathi-Serve*,
[OSDI 2024 proceedings](https://www.usenix.org/system/files/osdi24-agrawal.pdf),
with the [publisher entry](https://www.usenix.org/conference/osdi24/presentation/agrawal).

<a id="unit-trigger-and-source-observation"></a>
## Trigger and source observation

Consider this mechanism when traces show that long prefills interrupt ongoing
token generation. Prefill processes a request's input tokens; decode generates
subsequent tokens. Time between tokens (TBT) measures the gap during generation,
whereas time to first token (TTFT) includes the wait before the first output.
A queue, memory shortage or suspended-request problem needs its own diagnosis
before attributing the delay to prefill interference.

In §§4.1–4.2, Sarathi-Serve splits a prefill across iterations and combines its
chunks with ongoing decodes. The source's scheduling order is:

1. Account for ongoing decodes first, at one token per decoding request.
2. Include partially completed prefills within the remaining token budget.
3. Admit new requests only when allocation permits and budget remains; size
   their prefill chunks to that remainder.

The budget covers the mixed batch, not just newly admitted prefill tokens.
Chunking limits prefill work in an iteration; it does not make that work free.
Figure 9 still shows added batch latency relative to decode-only execution.
The paper's algorithm describes this policy; its pseudocode is not a contract
for any current engine implementation.

<a id="unit-decision-and-costs"></a>
## Decision and costs

Treat the budget as a deployment-specific candidate parameter. Section 4.3
balances a tighter TBT target against several costs:

- Smaller chunks reduce prefill work per iteration, but can lower compute
  utilization and repeat fixed launch costs.
- Each later chunk attends to earlier chunks of the same prompt, rereading
  their KV cache. The paper distinguishes these additional memory reads from
  unchanged attention computation.
- Matrix tile boundaries affect execution cost. Neighboring token counts need
  not have neighboring runtimes.
- With pipeline parallelism, differences between batch runtimes can leave
  stages idle. Larger chunks can increase that variation; excessively small
  chunks incur their own efficiency costs.

The paper uses profiling and Vidur to select a capacity-maximizing budget for
a specified hardware, parallelism and TBT objective. This does not establish a
universal chunk size or turn a simulator prediction into a measured result.
Figure 14's prefill-overhead study is specific to Yi-34B with tensor parallelism
across two GPUs, prompts of 2K/4K/8K tokens and chunks of 512/1024/2048 tokens.
Its normalization is unchunked prefill runtime, not end-to-end service time.

<a id="unit-what-the-reported-comparison-establishes"></a>
## What the reported comparison establishes

Table 4 evaluates 128 requests for Yi-34B on two A100 GPUs, with a token budget
of 1024, separately for `openchat_sharegpt4` and `arxiv_summarization`. In both
traces, the combined design has lower P99 TBT than either component alone. Its
P50 TTFT is lower than chunked-prefills-only, but higher than hybrid-batching-only.
Thus the combined design trades some first-token latency against tighter token
gaps; it does not improve every metric over each alternative.

Section 5 generates arrival times with a Poisson distribution and filters total
request lengths above 8192 and 16384 tokens for the two traces, respectively.
The capacity experiments also require median scheduling delay to stay within
2 seconds alongside the model-specific P99 TBT objective. Preserve those load,
queueing and percentile definitions when interpreting the reported capacity;
Table 4 alone is not a capacity or fairness result.

<a id="unit-proposed-adaptation-and-rejection-conditions"></a>
## Proposed adaptation and rejection conditions

Before a separately authorized experiment, establish a matched workload,
model, hardware, engine revision, parallelism, memory limits and latency
objectives. Use the existing admission and preemption owners to distinguish
capacity limits from decode interruption, and the calibration owner to qualify
profiling or simulator estimates. This case adds no scheduler implementation.

Compare bounded budget candidates while holding those conditions fixed. Record
P99 TBT, P50 TTFT, queueing/scheduling delay, sustainable throughput, prefill
runtime and any relevant pipeline idle time separately. A lower TBT with an
unacceptable TTFT or queueing cost rejects that candidate under the frozen
objectives. If traces do not support prefill interference, or required evidence
is unavailable, retain the incumbent and the unresolved diagnosis. These are
proposed checks, not results from this host.

No current-engine compatibility, local speedup, fairness guarantee or empirical
skill efficacy is established. Section 6 leaves quantitative comparison with
prefill/decode disaggregation open. Raw paper assets and the missing historical
supplier synthesis are not part of this case; their redistribution rights are
not inferred from public readability.

<a id="unit-when-this-applies"></a>
## When this applies

- Source-supported hypothesis selection when observed long prefills interfere with ongoing decodes
- Chunked-prefill token-budget tradeoffs under specified latency, workload, hardware and parallelism conditions

<a id="unit-limits-of-this-evidence"></a>
## Limits of this evidence

- Paper-author observations and proposed adaptation checks are not local measurements or current-engine support.
- The combined design does not beat hybrid-only P50 TTFT in either Table 4 trace.
- No universal budget, fairness guarantee, quantitative disaggregation comparison or empirical skill efficacy is established.
- Raw source redistribution and adaptation permission remain UNKNOWN.
- The same case identity and central mechanism appeared in closed-unmerged PR 156; this independently written fixed-edition contribution does not recover the missing historical archive or establish novelty over its unavailable synthesis.

<a id="unit-subtract-active-decode-tokens-before-filling-a-mixed-batch-with-prefill"></a>
## Subtract active decode tokens before filling a mixed batch with prefill

- **Outcome** — caveat
- **Reason** — Sarathi-Serve budgets one token per ongoing decode first, then accounts for partial prefills and admits new prompt chunks with the remaining budget and allocation capacity. The extra work can still extend a decode iteration.
- **Revisit when** — Confirm trace evidence of prefill interference and verify that the target engine’s mixed batch implements the same ordering before adapting the policy.
- **Keywords**
  - Sarathi-Serve
  - mixed token budget
  - ongoing decode
  - chunked prefill
  - TBT
  - admission
- **Scope** — regime_bound

<a id="unit-compare-the-token-gap-gain-from-smaller-chunks-with-repeated-launch-and-kv-costs"></a>
## Compare the token-gap gain from smaller chunks with repeated launch and KV costs

- **Outcome** — tradeoff
- **Reason** — Smaller chunks bound prefill work per iteration but can reduce utilization and repeat fixed overhead. Later chunks attend back over earlier prompt chunks, causing extra KV-cache reads even though total attention computation is unchanged.
- **Revisit when** — Profile candidate sizes on the actual device and report prefill time, sustained throughput and token gaps together.
- **Keywords**
  - small chunks
  - KV cache reread
  - compute utilization
  - launch overhead
  - token gaps
- **Scope** — regime_bound

<a id="unit-sample-tile-boundaries-and-stage-imbalance-when-tuning-chunk-length"></a>
## Sample tile boundaries and stage imbalance when tuning chunk length

- **Outcome** — tradeoff
- **Reason** — The paper identifies tile boundaries and uneven pipeline batch runtimes as sources of nonlinear cost. Larger chunks can leave stages idle, while very small chunks also lose efficiency.
- **Revisit when** — Under the intended model and parallelism, profile nearby lengths on both sides of tile boundaries and include pipeline idle time when applicable.
- **Keywords**
  - tile granularity
  - pipeline parallelism
  - stage idle
  - chunk size
  - Vidur
- **Scope** — regime_bound

<a id="unit-read-the-reported-ttft-and-tbt-comparison-as-a-workload-conditioned-trade"></a>
## Read the reported TTFT and TBT comparison as a workload-conditioned trade

- **Outcome** — tradeoff
- **Reason** — For both Table 4 traces, the combined design lowered P99 TBT versus either component alone. Median TTFT was below chunked-only and above hybrid-only in that setup.
- **Revisit when** — Preserve separate percentile and load definitions before borrowing this comparison for a new service configuration.
- **Keywords**
  - P99 TBT
  - P50 TTFT
  - hybrid batching
  - chunked prefills
  - Table 4
  - Yi-34B
- **Scope** — regime_bound
- **Bounds** — 128 requests, Yi-34B on two A100s, 1024-token budget, separately for OpenChat and arXiv summarization.

<a id="unit-freeze-matched-arrival-queueing-and-latency-objectives-before-changing-a-serving"></a>
## Freeze matched arrival, queueing and latency objectives before changing a serving budget

- **Outcome** — caveat
- **Reason** — The reported capacity work combined a model-specific token-gap objective with a scheduling-delay limit and defined request length filters. An improvement to one latency number alone does not settle the deployment tradeoff.
- **Revisit when** — Hold workload, model, hardware, runtime and parallelism constant. Measure TTFT, TBT, scheduling delay and sustainable throughput and keep the incumbent when the required evidence is missing.
- **Keywords**
  - capacity tuning
  - Poisson arrivals
  - scheduling delay
  - TTFT TBT SLO
  - sustainable throughput
  - length filters
- **Scope** — general

<a id="unit-source-files"></a>
## Source files

- [sarathi-chunk-budget.json](../../../../../skill_library/methods/optimization-search-policy/cases/sarathi-chunk-budget.json)
