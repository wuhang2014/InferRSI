<!-- handbook
{
  "id": "xdit.cuda.diffusion.parallelism_freshness_and_topology",
  "kind": "record",
  "aliases": [
    "package:xdit.cuda.diffusion.parallelism_freshness_and_topology"
  ],
  "tags": [
    "sequence_parallel",
    "ulysses",
    "ring",
    "pipefusion",
    "cfg",
    "quality",
    "transfer_hypothesis"
  ],
  "carry": [
    "unit-when-this-applies",
    "unit-limits-of-this-evidence"
  ]
}
-->

# xDiT parallelism: separate current-state attention from stale-state pipelines

> Recorded state `imported` · locally verified `false` · evidence level `guidance` · [Source](../../../../../../../knowledge_packs/peer/xdit/cuda/diffusion/parallelism-freshness-and-topology.json)

USP, CFG splitting and PipeFusion have different topology, memory and quality tradeoffs; qualify each before combining them.

`peer` · `xdit` · `cuda` · `diffusion.*`

<a id="unit-when-this-applies"></a>
## When this applies

- **Hardware**
  - Multiple CUDA GPUs with recorded interconnect topology; model support is method-specific
- **Software**
  - xdit-project/xDiT at f7c16aa958379a9f0a0302350fe0e1bfcec5f23c; later revisions need reinspection
- **Conditions**
  - A supported diffusion pipeline and compatible sequence/head partitioning
  - Record CFG setting, denoising schedule and all parallel degrees

<a id="unit-what-the-source-reports"></a>
## What the source reports

- **Upstream reported.** USP combines Ulysses and Ring sequence parallelism. CFG parallelism splits the two guidance branches when CFG is active.
- **Upstream reported.** The source cost table labels Ulysses/Ring attention data as fresh and PipeFusion as using stale information. PipeFusion requires serial warmup steps that affect its benefit.

<a id="unit-consequences-for-a-downstream-project"></a>
## Consequences for a downstream project

- vLLM-Omni: compare sequence partition choices using exposed communication and memory, not only rank count.
- Treat PipeFusion as a separate quality-sensitive experiment, particularly for few-step/distilled models where warmup consumes much of the schedule.
- vllm-ascend: transfer topology reasoning only after independently checking collectives, rank ownership and numerical behavior.

<a id="unit-putting-the-idea-to-work"></a>
## Putting the idea to work

- Treat downstream impact as an InferRSI transfer hypothesis, not an upstream compatibility or performance result.

<a id="unit-how-to-check-it"></a>
## How to check it

- Measure denoise and whole-generation latency, communication overlap, per-rank memory and scaling under fixed model/seed/shape/steps.
- Evaluate output quality for each method and combination; test uneven token/head layouts and disabled CFG.

<a id="unit-limits-of-this-evidence"></a>
## Limits of this evidence

- Backend-specific implementations and model matrices do not transfer with the high-level method.
- Current-state attention still requires numerical validation; stale-state methods must not be advertised as lossless from a speed benchmark.
- Point-in-time source extraction, not a historical commit-delta audit. No local accelerator or model-quality reproduction was run.

<a id="unit-sources"></a>
## Sources

- **Url** — <https://github.com/xdit-project/xDiT/blob/f7c16aa958379a9f0a0302350fe0e1bfcec5f23c/README.md>
- **Type** — technical_document
- **Commit** — f7c16aa958379a9f0a0302350fe0e1bfcec5f23c
- **Accessed at** — 2026-10-15
- **Content sha256** — 07bfd6874db892623db179ca9cc7e51d3b7c2036bf624e50b7a6e314081979e9
