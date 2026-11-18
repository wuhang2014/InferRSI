<!-- handbook
{
  "id": "project-maya",
  "kind": "procedure",
  "aliases": [
    "checkout:project-maya",
    "inferrsi.common.skills.project_maya",
    "package:inferrsi.common.skills.project_maya"
  ],
  "tags": [
    "project-maya",
    "model-specific-inference",
    "cuda",
    "rocm",
    "expert-tiering",
    "native-state",
    "speculation",
    "evidence-boundaries"
  ]
}
-->

# Project Maya inference engineering

> Recorded state `candidate` · empirical validation `partial_cpu_only` · license `NO_LICENSE` · [Source](../../../../skill_library/repositories/project-maya/SKILL.md) · [Scope and provenance](../../../../skill_library/repositories/project-maya/metadata.json) · [Catalog record](../../../../repo_packs/inferrsi/knowledge/common/skills/project-maya.json) · [Catalog revision](../../../../repo_packs/inferrsi/knowledge/_provenance.json) · [Parent reading](../../library/overview.md)

Investigate Project Maya model-family dispatch, representation and memory tiers, API versus native state, speculative decoding and source-qualified verification without treating safe CPU checks as CUDA/HIP or model evidence.

Use this source-derived **candidate** for model-specific inference questions in
`mw00/project-maya`. Read [source and method provenance](references/repo-provenance.md)
first. It is neither a generic model loader nor a verified inference engine.
The bundled helpers are offline support; reading this skill does not authorize
installation, engine startup, model downloads, GPU/API calls or host changes.

<a id="unit-route-by-the-failing-contract"></a>
## Route by the failing contract

| Question | Canonical procedure |
| --- | --- |
| Which model family/format, architecture guard, physical memory pool or residency tier? | [model-runtime](sub-skills/model-runtime/lesson.md) |
| API continuation, ownership, native slots, images, parallel state, cancellation or recovery? | [serving-state](sub-skills/serving-state/lesson.md) |
| Draft selection, rollback, calibration, quantization quality, benchmark or evidence level? | [qualification](sub-skills/qualification/lesson.md) |
| Build/setup side effects, missing tools or dependency/license ambiguity? | [troubleshooting](references/troubleshooting.md) and [license boundaries](references/license-boundaries.md) |

The retained snapshot has GLM, DeepSeek and MiniMax operating paths plus a newly
documented Qwen route. Coverage is intentionally asymmetric: selected core/state/
qualification bodies for the first three, shallow dispatch/format/guard evidence
for Qwen. Unmined deep kernels and unexecuted native/model paths stay explicit;
source presence or a common Python facade is not cross-family qualification.

<a id="unit-establish-identity-before-changing-a-setting"></a>
## Establish identity before changing a setting

1. Record the full source revision, actual executable/family, model and asset
   identities, representation, compiler/runtime/device, full rendered workload,
   sampling policy and active single/parallel route. A release label, common
   quant tier name or nominal bit width is insufficient.
2. Distinguish caller-supplied metadata from inspected bytes and executed results.
   Root MIT notices do not license every optional model asset; source code,
   weights, drafts, fonts and UI components have separate boundaries.
3. Identify the state/resource owner and lifetime. Shared weights are not private
   conversation state; API history is not native KV; unified physical memory
   must not be counted independently as both RAM and VRAM.
4. Select the relevant route, its local helper and its stop conditions. Preserve
   exact tokens/image identity and completion boundaries before attempting reuse
   or tuning. Never repair a slot header merely to make it appear compatible.
5. State a falsifiable hypothesis and the smallest safe check. A policy arithmetic
   result, simulated decision or request JSON can guide an investigation but
   cannot authenticate a model payload, actual fit, GPU cleanup or speedup.
6. For a native change, freeze correctness and comparison requirements before
   experiments, retain failures/negative observations, and distinguish component
   throughput from complete service/quality outcomes. Do not transfer a source
   tuner margin into a portable campaign acceptance bar.

<a id="unit-return-a-bounded-conclusion"></a>
## Return a bounded conclusion

Report the route and identities, evidence class, invariant, proposed check,
actual result, counter-signal, missing resource and next authorized action.
When required CUDA/HIP/model evidence is unavailable, keep
`BLOCKED_REQUIRED_BACKEND` and an unverified/INCONCLUSIVE conclusion. Do not turn
exit-zero skips, CPU simulations, source reports or green scaffold CI into native
PASS. Model quality, E2E service behavior and broad skill efficacy need separate
validation. Native/backend flags remain unverified until separately established.

<a id="unit-safe-support-and-source-boundaries"></a>
## Safe support and source boundaries

Each sub-skill owns a small bundled helper and detailed contract/troubleshooting
references. They are standard-library utilities, not model runners or copies of
unsafe setup/calibration scripts. Use their documented synthetic inputs; no
helper sends a request or installs dependencies. Source files are immutable
attribution links, not required runtime checkout paths. Keep this entire owner
folder when distributing it so the references, scripts and MIT notice remain.

<a id="unit-when-this-applies"></a>
## When this applies

- **Scope** — Model-specific dispatch/residency, API/native state and qualification investigation. Common catalog placement is not CPU inference or cross-device certification.
- **Prerequisites** — Access to the selected model-family runtime/state/qualification contract; native changes need frozen correctness/comparison requirements and the matching authorized CUDA/HIP/model resources.
- **Input contract** — Full source revision, actual executable/model family, model and asset identities, representation, compiler/runtime/device, rendered workload, sampling policy, single/parallel route, exact tokens/images and relevant completion observations.
- **Produced artifact** — A route/identity/evidence-class report with invariant, proposed check, actual result, counter-signal, missing resource and next authorized action; missing native requirements remain INCONCLUSIVE.
- **Failure modes** — Transferring coverage through a common facade or quantization name, confusing API history with native KV/private state, double-counting unified RAM/VRAM, or repairing a slot header to appear compatible can invalidate diagnosis.
- **Refusal point** — When required CUDA/HIP/model evidence is unavailable, retain BLOCKED_REQUIRED_BACKEND and an unverified/INCONCLUSIVE conclusion; exit-zero skips or CPU simulations cannot clear it.

<a id="unit-putting-the-idea-to-work"></a>
## Putting the idea to work

- Select the family-specific route and preserve the explicitly shallow Qwen coverage rather than transferring deeper GLM/DeepSeek/MiniMax evidence.
- Separate shared weights, private conversation state, API history and native KV; count unified physical memory once.
- Preserve exact token/image identities and completion boundaries before reuse, then test one falsifiable hypothesis without modifying slot headers to bypass compatibility.

<a id="unit-limits-of-this-evidence"></a>
## Limits of this evidence

- BLOCKED_REQUIRED_BACKEND: no actual CUDA/HIP/model/device, quantized payload, vision, parallel/state/restore or cancellation-cleanup evidence.
- Safe CPU slices and offline helpers cannot establish complete engine builds, memory fit, numerical/model quality, service/performance or broad skill efficacy.
- Qwen coverage is shallow routing/format/guard evidence; its deep runtime/state/kernels remain unmined/unverified. Other family coverage is bounded rather than exhaustive.
- Source reports and source-specific calibration margins are not local measurements or portable acceptance gates.
- NO_LICENSE is the actual unauthenticated gh resolver fallback; root MIT is retained independently and optional/model asset licenses remain separate.

<a id="unit-source-files"></a>
## Source files

- [LICENSE](../../../../skill_library/repositories/project-maya/LICENSE)
- [metadata.json](../../../../skill_library/repositories/project-maya/metadata.json)
- [references/repo-routing-metadata.json](../../../../skill_library/repositories/project-maya/references/repo-routing-metadata.json)
- [references/source-identity.json](../../../../skill_library/repositories/project-maya/references/source-identity.json)
