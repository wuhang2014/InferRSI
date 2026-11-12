# DeepSeek-V4.1-Flash model hosts

Accessed: 2026-11-12. External model-discovery knowledge; empirical validation: **not_run**.

## Repository identities

| Checkpoint | Hugging Face | ModelScope |
| --- | --- | --- |
| DeepSeek-V4.1-Flash | [Model card](https://huggingface.co/deepseek-ai/DeepSeek-V4.1-Flash); [pinned files](https://huggingface.co/deepseek-ai/DeepSeek-V4.1-Flash/tree/314113f8a7dadb388215396ba5fbee2c610a04d6) | [Model page](https://modelscope.cn/models/deepseek-ai/DeepSeek-V4.1-Flash); revision unknown |
| DeepSeek-V4.1-Flash-1017 | [Model card](https://huggingface.co/deepseek-ai/DeepSeek-V4.1-Flash-1017); [pinned files](https://huggingface.co/deepseek-ai/DeepSeek-V4.1-Flash-1017/tree/08c8657f02291e11b6f6b63e0e16014f8e748518) | [Model page](https://modelscope.cn/models/deepseek-ai/DeepSeek-V4.1-Flash-1017); revision unknown |

## Provenance and inspected scope

- The [original official announcement](https://api-docs.deepseek.com/zh-cn/news/news260910/) links the original Hugging Face repository.
- The [1017 official announcement](https://api-docs.deepseek.com/zh-cn/news/news261017/) links both 1017 repositories. Treat 1017 as a separate checkpoint, not an alias for the original weights.
- Original Hugging Face revision comes from its [model API](https://huggingface.co/api/models/deepseek-ai/DeepSeek-V4.1-Flash); 1017 comes from the [commit page](https://huggingface.co/deepseek-ai/DeepSeek-V4.1-Flash-1017/commit/08c8657f02291e11b6f6b63e0e16014f8e748518). These identify inspected host metadata, not a tested runtime.
- Hugging Face listings advertise image-text-to-text, Safetensors, and MIT licensing. The original API names `DeepseekV41ForCausalLM`, model type `deepseek_v41`, and FP8 quantization metadata. Do not infer every tensor's precision from that tag.
- Both Hugging Face listings include `config.json`, tokenizer assets, `model.safetensors.index.json`, and 48 named weight shards. Listing inspection is not a complete manifest or weight-byte integrity check.
- ModelScope pages resolved but returned no readable body to the browser tool. The original listing was also located in search; the 1017 identity is independently linked by the official announcement. No ModelScope immutable revision or file inventory was obtained.

## Reuse limits

Full model-card bodies, configuration values, license files, and shard contents were not audited. Model weights were not downloaded or executed. Cross-host byte equivalence remains **unverified**; do not copy Hugging Face revisions onto ModelScope identities. Resolve each host's revision and freeze actual asset hashes before an experiment. Host-generated launch examples do not establish engine compatibility or service performance.

See the separately versioned [technical-report readset](deepseek-v41-flash-report.md) and [implementation ledger](source-notes.md). Neither establishes that both hosts distribute identical bytes.
