<!-- handbook
{
  "id": "kernel-writing-guide",
  "kind": "procedure",
  "aliases": [
    "checkout:kernel-writing-guide",
    "inferrsi.common.skills.kernel_writing_guide",
    "package:inferrsi.common.skills.kernel_writing_guide"
  ],
  "tags": [
    "kernel",
    "triton",
    "cute",
    "cuda",
    "ascendc",
    "performance",
    "accelerator",
    "akg",
    "affine",
    "tail-guards",
    "causal-conv1d",
    "state-update",
    "vllm",
    "gdn",
    "causal-convolution",
    "transformers",
    "qwen3.5",
    "binding",
    "classification-prefill",
    "sglang",
    "prefill",
    "state-ownership"
  ]
}
-->

# Kernel Writing Guide

> Recorded state `candidate` · empirical validation `not_run` · [Source](../../../../skill_library/methods/kernel-writing-guide/SKILL.md) · [Scope and provenance](../../../../skill_library/methods/kernel-writing-guide/metadata.json) · [Catalog record](../../../../repo_packs/inferrsi/knowledge/common/skills/kernel-writing-guide.json) · [Catalog revision](../../../../repo_packs/inferrsi/knowledge/_provenance.json) · [Parent reading](../../library/overview.md)

Decision guide for writing custom inference kernels: when to write one, which framework to choose (Triton, CuTe DSL, CUDA C++, AscendC/TileIR), universal correctness rules that apply regardless of framework, and the verify-before-benchmark workflow. Use before starting any kernel implementation to avoid common correctness and performance pitfalls.

Status: candidate. Source-grounded from TensorRT-LLM `kernel-triton-writing`
and `kernel-cute-writing` skills @ f33e0e5f (NVIDIA/Apache-2.0). NPU-specific
content inferred from architecture parallels; verify against CANN/TileIR docs.

<a id="unit-searchspace-mapping"></a>
## SearchSpace mapping

Accelerator row → Optimize cell

Second-level targets: Kernel fusion, custom GEMM, attention variants, elementwise
chains, reduction kernels.

<a id="unit-when-to-write-a-custom-kernel"></a>
## When to write a custom kernel

Writing a kernel is expensive. Verify the bottleneck before starting.

**Write a custom kernel when:**
- A profiler (nsys/ncu or CANN msprof) confirms a specific kernel is on the
  critical path and near its hardware ceiling.
- Two or more adjacent operations can fuse: they share data that would otherwise
  go to/from DRAM between calls. The gain is the reduction in memory traffic,
  not the removal of Python overhead.
- A standard implementation exists but the specific dtype, shape, or quantization
  variant you need is not covered.

**Do NOT write a custom kernel when:**
- A single elementwise operation (relu, sigmoid on its own): the vendor library
  is already optimal.
- A standalone matmul: cuBLAS/CANN is better than a handwritten GEMM in almost
  all cases.
- Standard attention: use FlashAttention or the vendor's equivalent.
- The bottleneck is host-side scheduling: that is a Python/GIL problem, not a
  kernel problem. See `host-overhead-profiling`.

<a id="unit-qualify-an-existing-causal-convolution-operator"></a>
## Qualify an existing causal convolution operator

Before replacing or binding causal depthwise convolution, use the
[causal-conv1d contract](references/causal-conv1d-contract.md) to choose a
full-sequence forward call or an in-place state update. Check dtype, strides,
packed boundaries, state rows and circular-buffer cursors before substitution.
The [five decision cases](cases/causal-conv1d-dispatch-state.md) cover invalid
layouts, continuation state and unproved dispatch. Build targets and import
success do not establish the executing operator, numerical parity or a gain.

For a concrete Transformers Qwen3.5 caller, first use the
[two-version HF binding contract](references/hf-qwen35-gdn-binding.md) and
[source cases](cases/hf-qwen35-gdn-binding.md). Resolve module versus instance
binding, active forward overrides and cache state before substituting conv or
GDN. A cache-free classification adapter does not establish generation-state
support; package presence and matching names do not prove executed dispatch.

<a id="unit-framework-routing"></a>
## Framework routing

| Pattern | CUDA / Ampere+ | Ascend NPU |
|---------|---------------|------------|
| Fused elementwise chain (2+ ops sharing data) | Triton (`@triton.jit`) | TileIR / AscendC |
| Reduction (softmax, LayerNorm, RMSNorm) | Triton | TileIR / AscendC |
| Tiled GEMM with autotune | Triton | AscendC |
| GEMM with explicit shared memory / tensor core MMA | CuTe DSL (CUTLASS 4.x) | AscendC cube unit |
| Flash Attention variant | CuTe DSL or Triton | AscendC (custom) |
| Custom collective (AllReduce variant) | NCCL/custom CUDA | HCCL plugin |

CuTe DSL requires Linux x86_64, Python 3.10–3.13, Ampere+ (SM80+), and
`pip install nvidia-cutlass-dsl`. It is not available on NPU.

Source: TRT-LLM kernel-triton-writing + kernel-cute-writing @ f33e0e5f.

<a id="unit-universal-correctness-rules-apply-to-all-frameworks"></a>
## Universal correctness rules (apply to all frameworks)

These rules cause silent wrong results if violated. Check them before
benchmarking.

<a id="unit-1-transcendental-functions-require-fp32-inputs"></a>
### 1. Transcendental functions require FP32 inputs

`exp`, `log`, `erf`, `tanh`, and similar transcendentals cause errors or
undefined behavior with FP16/BF16 inputs in Triton. Pattern:

```python
# Wrong — silent error or wrong result with fp16/bf16:
result = tl.exp(x)

# Correct — cast to fp32, compute, cast back:
x_fp32 = x.to(tl.float32)
result = tl.exp(x_fp32).to(x.dtype)
```

Rule: any math function beyond `+`, `-`, `*`, `/` needs an fp32 cast round-trip.

Source: TRT-LLM kernel-triton-writing @ f33e0e5f, §FP16/BF16 Precision Rules.

<a id="unit-2-never-call-item-inside-a-kernel-wrapper"></a>
### 2. Never call `.item()` inside a kernel wrapper

`.item()` forces a CPU-GPU synchronization (~50–100 µs per call). This turns
into a pipeline stall if called inside the hot path.

```python
# Wrong — forces sync:
seed = some_tensor.item()

# Correct — use data pointer arithmetic, no sync:
seed = (some_tensor.data_ptr() % (2**31)) ^ n_elements
```

Source: TRT-LLM kernel-triton-writing @ f33e0e5f, §CPU-GPU Sync Avoidance.

<a id="unit-3-c-integer-division-semantics-triton-ascendc"></a>
### 3. C integer division semantics (Triton / AscendC)

Triton and most NPU DSLs use C semantics for `//` and `%`: they round toward
zero, not toward negative infinity like Python. This only matters when operands
can be negative (which they can in offset calculations).

```
Python:  -7 // 2  = -4,   -7 % 2  = 1
C/Triton: -7 // 2  = -3,   -7 % 2  = -1
```

Safe pattern: ensure all index and offset values are non-negative. If negative
values are possible: `(idx % BLOCK + BLOCK) % BLOCK`.

Source: TRT-LLM kernel-triton-writing @ f33e0e5f, §C Integer Division Semantics.

<a id="unit-4-pre-allocate-output-tensors"></a>
### 4. Pre-allocate output tensors

Allocating output inside the kernel wrapper on every call adds Python object
creation cost on the hot path. Accept a pre-allocated output buffer as a
parameter, or cache allocation outside the benchmark loop.

<a id="unit-5-use-fp32-accumulators-for-matmul-triton"></a>
### 5. Use FP32 accumulators for matmul (Triton)

Triton does NOT auto-promote fp16/bf16 inputs to fp32 for accumulation in
`tl.dot`. Always declare the accumulator as `tl.float32`:

```python
acc = tl.zeros((BLOCK_M, BLOCK_N), dtype=tl.float32)
```

<a id="unit-6-always-mask-loads-and-stores-for-non-divisible-shapes"></a>
### 6. Always mask loads and stores for non-divisible shapes

If `n_elements % BLOCK_SIZE != 0`, an unmasked load reads past the tensor
boundary. Always include a mask:

```python
mask = offsets < n_elements
x = tl.load(x_ptr + offsets, mask=mask)
tl.store(out_ptr + offsets, result, mask=mask)
```

<a id="unit-akg-affine-loop-tails-source-derived"></a>
### AKG Affine loop tails (source-derived)

For AKG-MLIR static CUDA elementwise loops, use the
[Affine tail-guard reference](references/akg-affine-tail-guards.md) to trace the
effective target, option precedence and loop bounds before interpreting a
non-divisible tile. The compiler can expand point-loop bounds and move the body
under an `affine.if`; both input reads and output writes need the valid-index
contract. The pinned fixture's FileCheck expectations describe IR structure,
not executed CUDA correctness or a tuning gain. This addition preserves the
handwritten load/store mask rule above and requires separate validation of
later lowering, synchronization and numerics. CPU/NPU tail strategies are not
qualified by the CUDA fixture.

<a id="unit-workflow-verify-before-benchmark"></a>
## Workflow: verify before benchmark

<a id="unit-qualify-a-stateful-serving-operator"></a>
### Qualify a stateful serving operator

For vLLM Qwen3-Next GDN convolution/recurrence reuse, read the
[pinned phase/state contract](references/vllm-gdn-causal-conv-contract.md) and
[representative source cases](cases/vllm-gdn-source-contract.md). Trace the
concrete caller, effective phase/backend, state-row mapping and in-place writes
before choosing an operator. The in-tree vLLM wrappers do not establish a
standalone-package or HF-worker binding. Source selection remains separate
from executed correctness, hardware qualification and performance.

For SGLang Qwen3.5 or Qwen3-Next, use the separate
[caller/backend contract](references/sglang-gdn-causal-conv-contract.md) and
[four source cases](cases/sglang-gdn-source-contract.md). Resolve the model's
linear layers, per-runner prefill/decode choices, architecture predicates,
conv aliases and state-row metadata before proposing reuse. A GDN prefill flag
does not select the convolution implementation. Keep one-shot classification
prefill distinct from decode, cached continuation and delimiter-based scoring;
source-derived transfer conditions are not an HF binding or execution result.
The [worker/engine cross-map](references/sglang-gdn-causal-conv-contract.md#unit-map-the-inspected-hf-workers-to-vllm-and-sglang)
connects the inspected Clef/PPLX bindings to both engine operator contracts;
its PPLX context follows the default GVA forward and the state-free adapter.

**Phase 1: Write the kernel with a reference function**

Every kernel must ship with three exports (used by companion verification and
benchmark scripts):

```python
kernel_fn = my_kernel_wrapper       # the implementation
reference_fn(*args) -> Tensor       # PyTorch reference with identical signature
get_inputs() -> list                # returns fresh CUDA/NPU tensors for testing
```

**Phase 2: Verify against reference**

Run `scripts/verify_kernel.py` (or equivalent) to check that the kernel output
matches the reference across a range of shapes and dtypes before any performance
measurement. Do not benchmark an unverified kernel.

Common verification failures:
- Shape boundary errors (off-by-one in mask)
- Accumulator dtype (fp16 accumulation in matmul)
- Transcendental precision (forgot fp32 cast)

**Phase 3: Profile to confirm bottleneck**

After verification, profile with ncu (CUDA) or msprof (Ascend) to confirm the
kernel has improved the target metric. An optimization that passes verification
but does not change the profiler output was not on the critical path.

<a id="unit-block-size-selection"></a>
## Block size selection

For Triton on CUDA:
- Start with `BLOCK_SIZE = 1024` for H100/Hopper, `512` for A100/Ampere.
- Block sizes must be powers of 2.
- For GEMM tiles (`BLOCK_M`, `BLOCK_N`, `BLOCK_K`): start from the tiled matmul
  skeleton configs in the source (128/256/64 for Hopper, 64/128/32 for smaller
  cards) and autotune from there.

For AscendC on Ascend NPU:
- The AI Core's local buffer (Unified Buffer / UB) is the equivalent of shared
  memory. Tile sizes must fit in UB.
- Cube unit (matrix unit) alignment requirements differ by SoC; check the CANN
  AscendC programming guide for the specific SoC target.
- TileIR (the higher-level DSL above raw AscendC) auto-tiles for standard
  patterns; use it before dropping to raw AscendC.

<a id="unit-starting-from-examples"></a>
## Starting from examples

For CuTe DSL on CUDA: find the closest example in the CUTLASS repo at
`https://github.com/NVIDIA/cutlass/tree/main/examples/python/CuTeDSL`.
Match the GPU architecture first (SM80 for Ampere, SM90 for Hopper, SM100 for
Blackwell). Study the example's structure; do not copy it verbatim since shapes,
dtypes, and problem dimensions differ.

For AscendC: consult the CANN AscendC operator development guide for your
specific SoC (Ascend 910B, 910C, etc.). Templates and intrinsics differ between
generations.

<a id="unit-attention-mechanisms-and-scoped-acceptance"></a>
## Attention mechanisms and scoped acceptance

Use [attention diagnosis](../../hardware/cuda/diagnose-attention-bottlenecks/lesson.md) when IO
reduction exposes scalar work, insufficient independent tiles, reduction costs,
compiler ordering or precision/layout overhead. Its
[mechanism notes](../../hardware/cuda/diagnose-attention-bottlenecks/references/mechanisms.md)
retain FlashAttention 1/2/3 assumptions, operation-class costs and counter-signals.
Tiling, recomputation, ownership and overlap change the resource balance; no
single utilization threshold or paper tile size selects a winner.

Preserve dense/sparse/quantized semantics, masks, dropout, output/gradient
accuracy and real buffer lifetimes. Verify the executing instruction schedule
before claiming overlap. Include conversion/preprocessing and exactness costs
in the measured boundary. NVIDIA primitives establish no Ascend support.
[Author-reported cases](../../hardware/cuda/diagnose-attention-bottlenecks/references/papers-20261015/cases/overlap-and-fp8-counter-signals.md)
are counterexamples to unconditional tuning rules, not local successes.

<a id="unit-limitations"></a>
## Limitations

- This skill is a routing and correctness guide, not a complete implementation
  reference. The source TRT-LLM skills contain full implementations for common
  patterns (fused GELU+dropout, softmax, LayerNorm, tiled GEMM, Flash Attention).
- CuTe DSL patterns are NVIDIA CUDA-only (Linux x86_64, SM80+).
- AscendC/TileIR patterns are source-inferred for this skill — verify against
  your specific CANN version and SoC before use. No local NPU verification done.
- Autotune (Triton `@triton.autotune`) adds substantial first-run compile cost.
  For serving, pre-warm the kernel at startup or cache the compiled binary.

<a id="unit-when-this-applies"></a>
## When this applies

- **Scope** — Deciding whether to write a custom inference kernel, routing a kernel pattern to Triton, CuTe DSL, CUDA C++, AscendC or TileIR, applying framework-independent correctness rules, and verifying the executing kernel against a reference before benchmarking; covers fused elementwise chains, reductions, tiled GEMM, attention variants, custom collectives, causal convolution and stateful serving-operator qualification
- **Prerequisites** — The applicable operator, caller/state and layout contracts are read before substitution, including the causal-conv1d contract and HF Qwen3.5 GDN binding; the CuTe DSL environment uses Linux x86_64, Python 3.10–3.13 and Ampere+ (SM80+) with nvidia-cutlass-dsl installed and no NPU target; the CANN programming guide for the specific SoC is consulted for AscendC
- **Input contract** — The candidate operation or operation chain, its shapes, dtypes, quantization and layout requirements, and the target execution phase; the target accelerator and framework constraints; for serving operators, the concrete caller, effective phase and backend, state-row mapping, cache or buffer lifetime and in-place-write behavior; a reference implementation with the same signature, a callable kernel wrapper and fresh CUDA or NPU test tensors; verification shapes and dtypes plus profiler output for the target metric
- **Produced artifact** — A write-or-decline decision for the candidate operation with the profiled bottleneck, fusable pair or required dtype, shape or quantization variant unsupported by the standard implementation that justifies it, a framework choice routed by pattern and accelerator, a correctness checklist covering fp32 transcendental round-trips, sync-free wrappers, C division semantics, pre-allocated outputs, fp32 matmul accumulators and masked boundary loads and stores, a starting block or tile size with its autotune and warmup cost noted, a kernel shipping kernel_fn, reference_fn and get_inputs, a reference-parity result across the verification shapes and dtypes, and a post-verification profiler reading on the target metric; for an existing causal-convolution or stateful serving operator, a qualification record naming the caller, phase, backend, state rows and in-place writes, with source selection kept apart from executed dispatch; a routing and correctness decision, not a complete implementation or a measured speedup
- **Failure modes**
  - A kernel is written for a standalone elementwise op, a standalone matmul or standard attention where the vendor library already wins
  - Host-side scheduling cost is treated as a kernel problem instead of being routed to host-overhead-profiling
  - Fusion is justified by removed Python call overhead rather than by the DRAM traffic the shared data no longer makes
  - A transcendental runs on fp16/bf16 inputs without the fp32 cast round-trip, so the error stays silent through benchmarking
  - tl.dot accumulates in the input dtype because Triton is assumed to promote fp16/bf16 to fp32 automatically
  - Negative offsets are computed assuming Python floor division while Triton or AscendC rounds toward zero
  - An unmasked load or store is accepted because the benchmark shapes happen to divide the block size
  - A kernel is benchmarked before it matches its reference, or a shape-boundary, accumulator-dtype or precision failure is read as a tuning problem
  - A verification pass is reported as a win although the profiler metric did not move, so the kernel was never on the critical path
  - Autotune compile cost is measured as steady-state serving latency instead of being pre-warmed or cached
  - A CuTe DSL pattern is routed to an NPU target, or a CUDA tail-guard, attention primitive or SM-matched example is assumed to carry to Ascend
  - A causal-conv1d or GDN operator is substituted on build success, import success or matching names without resolving dtype, strides, packed boundaries, state rows and cursors
  - An in-tree vLLM wrapper, a GDN prefill flag or a cache-free classification adapter is read as establishing the executed convolution path or generation-state support
- **Refusal point** — Declines to start a kernel until a profiler puts the target on the critical path near its hardware ceiling, a concrete fusable pair is identified, or the required dtype, shape or quantization variant is unsupported by the standard implementation, and sends host-bound cases elsewhere; refuses to benchmark an unverified kernel and withholds a gain whose profiler metric did not move; keeps operator source selection separate from executed dispatch, numerical parity and hardware qualification, so build or import success qualifies nothing; treats AscendC and TileIR content as source-inferred pending CANN and SoC verification with no local NPU run, treats the AKG Affine FileCheck expectations as IR structure rather than executed CUDA correctness, and reads author-reported overlap and FP8 cases as counterexamples to unconditional tuning rules; claims no Ascend support from NVIDIA primitives
- **Hardware** — CUDA Ampere+ and Ascend NPU have separate framework routes for each kernel pattern; CuTe DSL requires Linux x86_64, Python 3.10-3.13 and SM80+ with nvidia-cutlass-dsl and is unavailable on NPU; profiling uses ncu on CUDA and msprof on Ascend; the AscendC and TileIR guidance is source-inferred with no local NPU verification and requires validation against the specific CANN version and SoC

<a id="unit-putting-the-idea-to-work"></a>
## Putting the idea to work

- Confirm with nsys/ncu or msprof that the target kernel sits on the critical path near its hardware ceiling, name the adjacent operations whose shared data would otherwise round-trip through DRAM, or identify a required dtype, shape or quantization variant unsupported by the standard implementation, before writing any kernel.
- Ship every kernel with kernel_fn, reference_fn and get_inputs, pass reference parity across the verification shapes and dtypes first, and profile afterwards to confirm the target metric actually moved.
- Cast fp16/bf16 to fp32 and back for any math beyond +, -, * and /, declare tl.dot accumulators as tl.float32, and mask every load and store whose shape does not divide the block size.
- Start Triton at BLOCK_SIZE 1024 on Hopper and 512 on Ampere using powers of two, take GEMM tiles from the source skeleton configs (128/256/64 for Hopper, 64/128/32 for smaller cards) and autotune from there.
- On Ascend, reach for TileIR before raw AscendC, size tiles to fit the AI Core Unified Buffer and check cube-unit alignment against the CANN guide for the specific SoC.
- Match a CuTe DSL example to the GPU architecture (SM80 Ampere, SM90 Hopper, SM100 Blackwell) and study its structure instead of copying it, and pre-warm or cache autotuned kernels at startup so first-run compile cost stays out of serving latency.

<a id="unit-limits-of-this-evidence"></a>
## Limits of this evidence

- Source-derived candidate; no local efficacy validation.
- Original typed source inventory is not normalized; retain source identities and limits in the procedure/readsets.
- The typed vLLM entry covers only the new GDN reference; older source inventories remain incomplete.
- The vLLM and HF references identify separate source call contracts; no binary equivalence, executed backend, hardware qualification, numerical/model parity, performance or agent-efficacy evaluation.
- SGLang source contract only; native/backend/sm89 qualification, HF classification binding, numerical/model quality, performance and agent efficacy are not evaluated.
- The secondary PPLX caller readset has UNKNOWN repository licensing and source-only default/adapter evidence; no worker/kernel execution, model/quality/performance or stateful reuse is qualified.

<a id="unit-source-files"></a>
## Source files

- [metadata.json](../../../../skill_library/methods/kernel-writing-guide/metadata.json)
- [references/hf-qwen35-gdn-source.json](../../../../skill_library/methods/kernel-writing-guide/references/hf-qwen35-gdn-source.json)
- [references/licenses/sglang-LICENSE.md](../../../../skill_library/methods/kernel-writing-guide/references/licenses/sglang-LICENSE.md)
- [references/pplx-gdn-caller-context.json](../../../../skill_library/methods/kernel-writing-guide/references/pplx-gdn-caller-context.json)
- [references/sglang-gdn-source-files.json](../../../../skill_library/methods/kernel-writing-guide/references/sglang-gdn-source-files.json)
