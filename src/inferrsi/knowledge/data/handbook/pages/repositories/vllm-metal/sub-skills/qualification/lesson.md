<!-- handbook
{
  "id": "repositories/vllm-metal/sub-skills/qualification",
  "kind": "procedure",
  "tags": [
    "vllm-metal",
    "apple-silicon",
    "mlx",
    "mps",
    "paged-kv",
    "kv-offload",
    "speculation",
    "deferred-execution",
    "evidence-boundaries"
  ]
}
-->

# Speculation, deferred execution and evidence

> Recorded state `candidate` · empirical validation `partial_cpu_only` · license `NO_LICENSE` · [Source](../../../../../../skill_library/repositories/vllm-metal/sub-skills/qualification/SKILL.md) · [Scope and provenance](../../../../../../skill_library/repositories/vllm-metal/metadata.json) · [Parent reading](../../lesson.md)

Qualify vllm-metal speculative pairing, hybrid rollback, deferred decode ownership and executed attention routes, then separate token accounting, numerical parity, quality and actual HTTP serving performance.

Use this route for claims that speculative decoding, GQA/NAX, native sampling
or decode pipelining is enabled, correct or faster. These are different claims.
This source-derived candidate provides an investigation procedure, not a
native/model/serving qualification or an empirical skill-efficacy result.

<a id="unit-freeze-the-question-first"></a>
## Freeze the question first

1. Record exact target/draft/tokenizer bytes, source/native/runtime versions,
   device, backend, executor/process topology, model format and dtype, cache
   policy, active flags, real input/output token IDs and measurement boundary.
   Separate kernel time, offline generation and client-observed serving.
2. Read [speculative and deferred contracts](references/speculation-and-pipeline.md).
   Check the supported method/state-family pairing before counting proposals.
   Draft acceptance cannot establish exact rollback or output parity.
3. For pipelined decode, trace submitted→pending→resolved token ownership.
   A request removed from runner maps must not be resurrected during backfill.
   An ineligible next step must barrier before mutating request state.
4. Read [dispatch and measurement](references/dispatch-and-measurement.md).
   Geometry/selector eligibility is not executed dispatch; a process-wide last
   dispatch sample is not per-request telemetry under concurrency.
5. For correctness, compare actual outputs and state across supported/fallback
   paths, partial acceptance, preemption, batch-membership changes and tails.
   Missing Apple native/model evidence remains `BLOCKED_REQUIRED_BACKEND`.
6. For performance, freeze the intended workload and gates, run repeated arms
   with controlled machine state and topology, retain failed/noisy/slow trials,
   and verify the worker's actual route separately from expensive captures.
   No helper or upstream reported number substitutes for that experiment.
7. Use the offline [record summarizer](../../../../../../skill_library/repositories/vllm-metal/sub-skills/qualification/scripts/summarize_serving_records.py)
   only to inspect descriptive completed subsets while retaining failure
   counts. It executes no engine and always returns evidence `INCONCLUSIVE`.
   Read its [schema and limits](references/record-schema.md) before use.

<a id="unit-synthetic-accounting-example"></a>
## Synthetic accounting example

From this sub-skill directory:

```bash
python scripts/summarize_serving_records.py records.json
```

The file must explicitly declare `metric`, identity strings and both variants'
measured execution records. Warmups are excluded; blocked/failed/cancelled rows
remain visible with null measurements. Never substitute SSE chunk counts,
characters or words for generated token IDs/usage.

<a id="unit-route-failures"></a>
## Route failures

- Unsupported config, native ABI or a wrong model path belongs to
  [platform/config](../platform-config/lesson.md).
- Cache capacity, prefix restore, sleep/wake and shared unified memory belong
  to [cache lifecycle](../cache-lifecycle/lesson.md).
- For lost pending rows, misleading sampler parity or mixed-workload routing,
  use [troubleshooting](references/troubleshooting.md).

<a id="unit-report-three-conclusions-independently"></a>
## Report three conclusions independently

Return (1) source-supported eligibility, (2) actual executed correctness/state
evidence, and (3) measurement/quality evidence with its exact boundary. A native
test that skips, a CPU reference embedded in a GPU test, an offline parser pass,
or successful scaffold CI is not a backend pass. Unsupported pairing is not
the same as unverified supported pairing. Preserve both negative observations
and required gaps; public performance/quality claims need separate acceptance.

<a id="unit-source-files"></a>
## Source files

- [scripts/summarize_serving_records.py](../../../../../../skill_library/repositories/vllm-metal/sub-skills/qualification/scripts/summarize_serving_records.py)
