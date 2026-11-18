<!-- handbook
{
  "id": "vllm_omni.common.diffusion.measurement_and_profiling",
  "kind": "record",
  "aliases": [
    "package:vllm_omni.common.diffusion.measurement_and_profiling"
  ],
  "tags": [
    "baseline",
    "profiling",
    "parallelism",
    "warmup",
    "quality_gate"
  ],
  "carry": [
    "unit-when-this-applies",
    "unit-limits-of-this-evidence"
  ]
}
-->

# Diffusion measurement and profiling discipline

> Recorded state `imported` · locally verified `false` · evidence level `guidance` · [Source](../../../../../../../repo_packs/vllm_omni/knowledge/common/diffusion/measurement-and-profiling.json)

Freeze the serving, single-request and benchmark commands; measure performance without diagnostic profiler overhead, then use targeted traces to choose one-variable experiments.

`contribution` · `vllm_omni` · `common` · `diffusion.*`

<a id="unit-when-this-applies"></a>
## When this applies

- **Hardware** — `[]`
- **Software**
  - vllm-omni guidance snapshot ee81f33001922f8d91dd09da0a57ee1531a8df82; parser flags and model capabilities must be checked at the target revision
- **Models**
  - Wan/Qwen/Flux-style image and video pipelines; adapt to other diffusion models
- **Conditions**
  - Named device SKU/count/topology, model revision, assets, seed, shape, frames, schedule, dtype, attention backend and compile state are frozen
  - Backend-native profiler and low-overhead stage timings are available or their absence is recorded

<a id="unit-what-the-source-reports"></a>
## What the source reports

- **Guidance.** Performance baseline and operator/host-stack diagnostic traces serve different purposes. PyTorch profiler, shape recording and stack collection can distort measured latency.
- **Guidance.** Compare client E2E, server inference, encode, denoise, decode and peak memory independently. A kernel or denoise win can be offset by decode, communication or transport.
- **Guidance.** For CFG-enabled models, compare CFG2×USP(world/2) with USP(world); treat HSDP primarily as capacity until an A/B demonstrates speed; tune VAE patch parallel only where its stage share is material.
- **Guidance.** Every optimization, including intended math-preserving layout/cache changes, needs artifact and numerical evidence. Quantization, sparse/approximate attention and reduced steps are quality-sensitive hypotheses.

<a id="unit-putting-the-idea-to-work"></a>
## Putting the idea to work

- Freeze explicit CLI argument vectors for server startup, single request, benchmark and diagnostic collection separately; retain raw responses and exit statuses.
- Run an explicit warmup policy and at least three measured repetitions for shortlisted fixed-work candidates; retain every sample and report median/mean plus spread in milliseconds.
- Collect operator+shape and host-stack traces as separate diagnostic runs. Start at rank 0; expand when imbalance/communication hypotheses justify it.
- Choose candidates from measured dominant stages and trace evidence; include both a latency objective and memory/quality constraints.

<a id="unit-how-to-check-it"></a>
## How to check it

- Confirm A/B source, assets, random seed, schedule, attention backend, precision, compile warmup and resource placement differ only in the tested variable.
- Run unprofiled baseline and candidate, validate output artifacts, measure stage and client timings, and compare against baseline self-run variance.
- Validate per-rank device memory and host memory; do not derive p95/p99 from three fixed-work repeats.
- On ROCm/Ascend use their appropriate profiling workflow; CUDA kernel/profiler evidence does not establish another backend.

<a id="unit-limits-of-this-evidence"></a>
## Limits of this evidence

- This is imported methodological guidance, not a performance result.
- Parallelism and compiler benefits depend on model implementation, shapes, topology and target software.
- No remote device run or upstream tool execution was performed by InferRSI during this import.

<a id="unit-sources"></a>
## Sources

- **Url** — <https://github.com/vllm-project/vllm-omni/blob/ee81f33001922f8d91dd09da0a57ee1531a8df82/.claude/skills/diffusion-perf-opt/SKILL.md>
- **Type** — skill
- **Commit** — ee81f33001922f8d91dd09da0a57ee1531a8df82
- **Accessed at** — 2026-10-09

- **Url** — <https://github.com/vllm-project/vllm-omni/blob/ee81f33001922f8d91dd09da0a57ee1531a8df82/.claude/skills/diffusion-perf-opt/references/optimization-playbook.md>
- **Type** — skill
- **Commit** — ee81f33001922f8d91dd09da0a57ee1531a8df82
- **Accessed at** — 2026-10-09
