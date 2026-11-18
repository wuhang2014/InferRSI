<!-- handbook
{"id": "trace-shared-state", "kind": "path", "tags": ["asynchronous", "buffers", "KV cache", "events"]}
-->

# Trace shared state across an asynchronous boundary

Work from an unanswered question about reuse to a small event ledger. Keep
the names of the actual worker, scheduler, stream and buffer namespace in
each row so that a handoff can be checked against its implementation.

<a id="unit-prerequisites"></a>
## Prerequisites

Identify the event that a caller can observe when work completes. [Completion boundaries](../foundations/measurement-boundaries.md#unit-completion)

<a id="unit-readings"></a>
## Reading order

1. Sketch the lifetime of one cache block. [Build an ownership ledger](../foundations/state-ownership.md#unit-ledger)
2. Trace what the waiting scheduler can infer about external KV. [vLLM decision procedure](../repositories/vllm/audit-vllm-kv-lifetimes/lesson.md#unit-decision-procedure)
3. Follow the producer and consumer streams in a dependency. [MLX cross-stream ordering](../records/dependency/mlx/mlx/execution/cross-stream-dependency.md#unit-what-the-source-reports)
4. Check which host slot is safe to refill after an asynchronous copy. [One reusable host slot](../hardware/host/host-memory-management/lesson.md#unit-example-one-reusable-host-slot-current-stream-consumer)
5. Apply the ledger to a different owner. [Graph references and buffer storage](../foundations/state-ownership.md#unit-check)

<a id="unit-exercise"></a>
## Exercise

You have a worker-side “save submitted” event and a scheduler-side “response
finished” event for the same request. Can you mark the blocks reusable?

Keep the last-consumer and release columns open until you find evidence of
save completion and the scheduler's release decision for those block IDs.
Record the missing event and its owner. [Connector evidence and counter-signals](../repositories/vllm/audit-vllm-kv-lifetimes/lesson.md#unit-counter-signals-verification-and-escalation)
