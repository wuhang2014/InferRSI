<!-- handbook
{"id": "state-ownership", "kind": "concept", "tags": ["KV cache", "lifetime", "ownership"]}
-->

# When can storage be reused?

Consider a request whose response has been delivered while a background
transfer still reads its cache blocks. Returning those blocks to the pool
would let the next request overwrite data that the transfer still needs.
To decide when reuse is valid, follow both the request and the storage.

<a id="unit-ledger"></a>
## Trace one buffer through its owners

Draw one row per observed event. Record the request, the buffer or block
namespace, the producer, the last consumer and the signal that permits reuse.
If a worker submits a save, keep its completion event on the ledger. Look for
the scheduler action that consumes that event before returning the blocks.
The vLLM procedure spells out which events a concrete connector must expose.
[Evidence for the KV ownership ledger](../repositories/vllm/audit-vllm-kv-lifetimes/lesson.md#unit-required-evidence)

<a id="unit-check"></a>
## Test the transfer of the idea

An MLX graph releases its input references after dispatch. Which evidence
would you look for before counting the storage as available? Find the
backend-specific owner that keeps buffers alive for queued work, identify
its completion signal, then inspect the allocator's reuse policy. This uses
the same ownership question as the vLLM example. Each implementation supplies
its own answer. [MLX buffer lifetime](../records/dependency/mlx/mlx/execution/post-detachment-buffer-lifetime.md#unit-what-the-source-reports)
