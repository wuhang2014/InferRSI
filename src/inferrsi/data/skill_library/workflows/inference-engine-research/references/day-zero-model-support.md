# Day-zero LLM support: vLLM and SGLang

Observed: 2026-11-12. External announcement discovery; empirical validation: **not_run**.
Selected inventory, not exhaustive coverage. Dates are article publication dates, not independently verified model launch dates. Readset: official indices and article titles; Mistral additionally includes Usage and model-runner requirements. Other article bodies are not distilled deployment procedures.

| Engine | Model | Published | Official announcement |
| --- | --- | --- | --- |
| vLLM | Mistral Large 4 | 2026-10-29 | https://vllm.ai/blog/2026-10-29-mistral-large-4 |
| vLLM | Muse Spark Open | 2026-10-15 | https://vllm.ai/blog/2026-10-15-muse-spark-open |
| vLLM | Qwen3.8-2.4T-A95B | 2026-08-12 | https://vllm.ai/blog/2026-08-12-qwen3.8 |
| SGLang / Miles | Kimi K3.1 Pro | 2026-11-04 | https://www.sglang.io/blog/kimi-k3.1-pro-day0-support |
| SGLang / Miles | MiniMax M3.1 Flash | 2026-10-22 | https://www.sglang.io/blog/minimax-m3.1-flash-day0-support |
| SGLang / Miles | Step 5 Preview | 2026-10-14 | https://www.sglang.io/blog/step-5-preview-day0-support |
| SGLang / Miles | DeepSeek-V4.1 | 2026-09-09 | https://www.sglang.io/blog/deepseek-v4.1-day0-support |

Discovery sources: [vLLM model-support index](https://vllm.ai/blog/tags/model-support) and [SGLang blog](https://www.sglang.io/blog). URLs are live; immutable document revisions and retained byte hashes are **unknown**. Observation dates do not freeze source bytes.

## Deployment boundary

Day-zero announcements identify candidate support, not a stable-package guarantee. The Mistral article supplies a model-specific `vllm/vllm-openai:mistral-large-4` image and requires model runner V2. Its tag is not an immutable image digest. No image was downloaded or tested.

## Qualification procedure

1. Select checkpoint, task/modality, dtype, quantization and device. Distinguish preview and updated checkpoints.
2. Read the selected article, deployment recipe and release notes. Resolve engine commit/release, dependency versions and image digest; distinguish special images, development branches and released packages. Unknown identities remain unknown.
3. Inspect registration, loading and effective backend dispatch. Qualify text, vision, tool parsing, speculation and RL separately. Miles integration does not qualify every serving feature.
4. Freeze model, tokenizer, configuration and asset hashes; compare matched prompt encoding, reasoning mode, sampling, stopping and output decoding.
5. Run authorized correctness/quality and end-to-end service checks under frozen gates. Missing evidence remains INCONCLUSIVE; publisher numbers are not local measurements.

No engines, weights or dependencies were installed and no accelerator execution occurred. These records do not extend the executable registry or qualify Ascend. An absent pairing means not covered, not unsupported.

See the separate [DeepSeek model-host inventory](../../../repositories/deepinfer/bound-windowed-attention-replay/references/deepseek-v41-model-hosts.md). The unsuffixed announcement does not establish 1017 compatibility.
