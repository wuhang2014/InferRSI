<!-- handbook
{
  "id": "sglang_omni.common.audio.serving_and_streaming_quality",
  "kind": "record",
  "aliases": [
    "package:sglang_omni.common.audio.serving_and_streaming_quality"
  ],
  "tags": [
    "audio",
    "tts",
    "streaming",
    "configuration",
    "serving",
    "rtf"
  ],
  "carry": [
    "unit-when-this-applies",
    "unit-limits-of-this-evidence"
  ]
}
-->

# SGLang-Omni serving recipes and streaming audio measurements

> Recorded state `imported` · locally verified `false` · evidence level `guidance` · [Source](../../../../../../../repo_packs/sglang_omni/knowledge/common/audio/serving-and-streaming-quality.json)

Resolve the model-specific config and endpoint, then compare first audio, chunk gaps, duration/RTF, errors and quality under controlled load.

`contribution` · `sglang_omni` · `common` · `audio.*`

<a id="unit-when-this-applies"></a>
## When this applies

- **Hardware** — `[]`
- **Software**
  - sgl-project/sglang-omni source snapshot 2cfb3b67becb437b70751defe37e63d3af4eedb0
- **Conditions**
  - Choose a supported model recipe, endpoint, reference audio and matching checkpoint/config class.
  - Retain platform dependencies, resolved config/diff/provenance and per-process memory budgets.

<a id="unit-putting-the-idea-to-work"></a>
## Putting the idea to work

- Resolve/explain with the proposed launch arguments, establish readiness and one complete audio/text result, then measure concurrency.
- Investigate the saturated admission/request-build/AR queue; distinguish weights, KV, graphs, vocoder and communication allocations for OOMs.

<a id="unit-how-to-check-it"></a>
## How to check it

- Check output modality, sample rate, SSE errors, EOS and complete content; HTTP 200 alone is insufficient.
- Repeat warm baseline/candidate trials on the same dataset and sampling with audio quality, latency distributions, duration/RTF and failures.

<a id="unit-limits-of-this-evidence"></a>
## Limits of this evidence

- Config resolution can import optional model dependencies or require cached/network metadata; it is not a dependency-free smoke test.
- Chunking and asynchronous decode options are model-specific, with no universal latency gain.
- This indexed abstract links to the complete English skill and source evidence; it is imported guidance, not a benchmark result.
- Accelerator execution, real-model quality and service performance remain unverified for this import. Qualify each target revision, model, backend and workload separately.

<a id="unit-sources"></a>
## Sources

- **Url** — <https://github.com/sgl-project/sglang-omni/blob/2cfb3b67becb437b70751defe37e63d3af4eedb0/benchmarks/eval/benchmark_omni_streaming_ttft.py>
- **Type** — source
- **Commit** — 2cfb3b67becb437b70751defe37e63d3af4eedb0
- **Accessed at** — 2026-10-14

- **Url** — <https://github.com/sgl-project/sglang-omni/blob/2cfb3b67becb437b70751defe37e63d3af4eedb0/benchmarks/eval/benchmark_tts_seedtts.py>
- **Type** — source
- **Commit** — 2cfb3b67becb437b70751defe37e63d3af4eedb0
- **Accessed at** — 2026-10-14

- **Url** — <https://github.com/sgl-project/sglang-omni/blob/2cfb3b67becb437b70751defe37e63d3af4eedb0/docs/developer_reference/tts_bench.md>
- **Type** — source
- **Commit** — 2cfb3b67becb437b70751defe37e63d3af4eedb0
- **Accessed at** — 2026-10-14

<a id="unit-available-translation"></a>
## Available translation

- **Zh-cn**
  - **Title** — SGLang-Omni 服务配方与流式音频测量
  - **Summary** — 解析模型专属配置和端点，在受控负载下比较首音频、分块间隔、时长/RTF、错误与质量。

<a id="unit-companion-material"></a>
## Companion material

- [SKILL.md](../../../../../repositories/sglang-omni/sub-skills/sglang-omni-serving/lesson.md)
