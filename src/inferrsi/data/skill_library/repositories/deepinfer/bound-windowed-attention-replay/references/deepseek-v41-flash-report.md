# DeepSeek-V4.1-Flash technical report

## Source identity and readset

- Title: DeepSeek-V4.1-Flash: Pushing the Limits of KV Cache Compression.
- Authors: DeepSeek-AI.
- Paper: [arXiv:2609.19969v1](https://arxiv.org/abs/2609.19969v1), dated 2026-09-17.
- Versioned text: https://arxiv.org/html/2609.19969v1
- Versioned PDF: https://arxiv.org/pdf/2609.19969v1
- Accessed: 2026-11-12.
- Readset: abstract, introduction, sections 2.2 and 2.4.4; section headings identify further reading, not full-report review.
- Kind: external paper knowledge. Empirical validation: **not_run**.
- The paper version is its provenance; no Git revision is assigned to it. Full text remains at the source; no redistribution license is inferred.

## Scoped extraction

CED derives decoder global KV from encoder-boundary hidden states; local SWA state still requires replay (§2.2). CSA2 combines cross-layer KV and index reuse (§1). Main KV uses FP4, while SWA KV remains FP8 (§2.4.4). Bounded replay reconstructs SWA approximately from a suffix; it is not an exact-equivalence guarantee (§1).

## Relationship to existing knowledge

The [model-host inventory](deepseek-v41-model-hosts.md) records Hugging Face and ModelScope identities separately from this paper version.

Read the separate [implementation ledger](source-notes.md) and [validation plan](validation.md) before transferring this material. Their Git pin identifies a different artifact, not a reproduction of this paper. Paper-reported quality does not validate that implementation or another checkpoint, backend, or workload. Establish independent quality and end-to-end evidence before claiming gains. Training, benchmark tables, appendices, and the later 1017 checkpoint are outside this readset.
