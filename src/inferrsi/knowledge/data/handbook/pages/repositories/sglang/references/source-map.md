<!-- handbook
{
  "id": "repositories/sglang/references/source-map",
  "kind": "reference"
}
-->

# Pinned source map

> [Source](../../../../../skill_library/repositories/sglang/references/source-map.md) · [Parent reading](../lesson.md)

All links resolve into the exact source commit below. Line ranges were checked against the local clean checkout. These are selected evidence excerpts, not whole-file certification. Native skills are source material and do not override the current user's scope.

`16176278d0180f1a1a578e53e6eef432577876c2`

<a id="unit-e01"></a>
## E01

Process/request flow. [python/sglang/srt/entrypoints/engine.py:243-258](https://github.com/sgl-project/sglang/blob/16176278d0180f1a1a578e53e6eef432577876c2/python/sglang/srt/entrypoints/engine.py#L243-L258)

<a id="unit-e02"></a>
## E02

Scheduler normal/overlap loops. [python/sglang/srt/managers/scheduler.py:1939-2045](https://github.com/sgl-project/sglang/blob/16176278d0180f1a1a578e53e6eef432577876c2/python/sglang/srt/managers/scheduler.py#L1939-L2045)

<a id="unit-e03"></a>
## E03

Chunk/prefill merge boundary. [python/sglang/srt/managers/scheduler.py:3766-3835](https://github.com/sgl-project/sglang/blob/16176278d0180f1a1a578e53e6eef432577876c2/python/sglang/srt/managers/scheduler.py#L3766-L3835)

<a id="unit-e04"></a>
## E04

ScheduleBatch to ForwardBatch to model. [python/sglang/srt/managers/tp_worker.py:603-651](https://github.com/sgl-project/sglang/blob/16176278d0180f1a1a578e53e6eef432577876c2/python/sglang/srt/managers/tp_worker.py#L603-L651)

<a id="unit-e05"></a>
## E05

Graph and forward-mode dispatch. [python/sglang/srt/model_executor/model_runner.py:1932-2031](https://github.com/sgl-project/sglang/blob/16176278d0180f1a1a578e53e6eef432577876c2/python/sglang/srt/model_executor/model_runner.py#L1932-L2031)

<a id="unit-e06"></a>
## E06

Memory layer ownership. [python/sglang/srt/mem_cache/README.md:8-83](https://github.com/sgl-project/sglang/blob/16176278d0180f1a1a578e53e6eef432577876c2/python/sglang/srt/mem_cache/README.md#L8-L83)

<a id="unit-e07"></a>
## E07

Radix prefix namespace and alignment. [python/sglang/srt/mem_cache/radix_cache.py:364-417](https://github.com/sgl-project/sglang/blob/16176278d0180f1a1a578e53e6eef432577876c2/python/sglang/srt/mem_cache/radix_cache.py#L364-L417)

<a id="unit-e08"></a>
## E08

Radix eviction and active locks. [python/sglang/srt/mem_cache/radix_cache.py:552-616](https://github.com/sgl-project/sglang/blob/16176278d0180f1a1a578e53e6eef432577876c2/python/sglang/srt/mem_cache/radix_cache.py#L552-L616)

<a id="unit-e09"></a>
## E09

Unified tree components and HiCache. [python/sglang/srt/mem_cache/unified_cache/components/README.md:1-121](https://github.com/sgl-project/sglang/blob/16176278d0180f1a1a578e53e6eef432577876c2/python/sglang/srt/mem_cache/unified_cache/components/README.md#L1-L121)

<a id="unit-e10"></a>
## E10

HiCache tier sharing and prefetch. [docs/docs/advanced_features/hicache_design.mdx:20-115](https://github.com/sgl-project/sglang/blob/16176278d0180f1a1a578e53e6eef432577876c2/docs/docs/advanced_features/hicache_design.mdx#L20-L115)

<a id="unit-e11"></a>
## E11

Memory and HiCache knobs. [python/sglang/srt/arg_groups/fields/memory.py:26-170](https://github.com/sgl-project/sglang/blob/16176278d0180f1a1a578e53e6eef432577876c2/python/sglang/srt/arg_groups/fields/memory.py#L26-L170)

<a id="unit-e12"></a>
## E12

Admission and chunking knobs. [python/sglang/srt/arg_groups/fields/schedule.py:27-100](https://github.com/sgl-project/sglang/blob/16176278d0180f1a1a578e53e6eef432577876c2/python/sglang/srt/arg_groups/fields/schedule.py#L27-L100)

<a id="unit-e13"></a>
## E13

Speculative algorithm/draft knobs. [python/sglang/srt/arg_groups/fields/spec.py:28-108](https://github.com/sgl-project/sglang/blob/16176278d0180f1a1a578e53e6eef432577876c2/python/sglang/srt/arg_groups/fields/spec.py#L28-L108)

<a id="unit-e14"></a>
## E14

TP, replica DP, attention DP. [python/sglang/srt/arg_groups/fields/parallel.py:47-105](https://github.com/sgl-project/sglang/blob/16176278d0180f1a1a578e53e6eef432577876c2/python/sglang/srt/arg_groups/fields/parallel.py#L47-L105)

<a id="unit-e15"></a>
## E15

Legacy attention-DP migration. [python/sglang/srt/arg_groups/parallel_hook.py:39-61](https://github.com/sgl-project/sglang/blob/16176278d0180f1a1a578e53e6eef432577876c2/python/sglang/srt/arg_groups/parallel_hook.py#L39-L61)

<a id="unit-e16"></a>
## E16

PD roles and transfer settings. [python/sglang/srt/arg_groups/fields/disagg.py:52-79](https://github.com/sgl-project/sglang/blob/16176278d0180f1a1a578e53e6eef432577876c2/python/sglang/srt/arg_groups/fields/disagg.py#L52-L79)

<a id="unit-e17"></a>
## E17

PD allocation protocol constraints. [docs/docs/advanced_features/pd_disaggregation.mdx:23-72](https://github.com/sgl-project/sglang/blob/16176278d0180f1a1a578e53e6eef432577876c2/docs/docs/advanced_features/pd_disaggregation.mdx#L23-L72)

<a id="unit-e18"></a>
## E18

Model registry and EntryClass. [python/sglang/srt/models/registry.py:20-159](https://github.com/sgl-project/sglang/blob/16176278d0180f1a1a578e53e6eef432577876c2/python/sglang/srt/models/registry.py#L20-L159)

<a id="unit-e19"></a>
## E19

Attention registry. [python/sglang/srt/layers/attention/attention_registry.py:41-79](https://github.com/sgl-project/sglang/blob/16176278d0180f1a1a578e53e6eef432577876c2/python/sglang/srt/layers/attention/attention_registry.py#L41-L79)

<a id="unit-e20"></a>
## E20

Kernel placement and lazy inventory. [python/sglang/kernels/README.md:11-91](https://github.com/sgl-project/sglang/blob/16176278d0180f1a1a578e53e6eef432577876c2/python/sglang/kernels/README.md#L11-L91)

<a id="unit-e21"></a>
## E21

Runtime config ownership. [.agents/skills/sglang-runtime-context/SKILL.md:8-111](https://github.com/sgl-project/sglang/blob/16176278d0180f1a1a578e53e6eef432577876c2/.agents/skills/sglang-runtime-context/SKILL.md#L8-L111)

<a id="unit-e22"></a>
## E22

Native kernel organization. [.agents/skills/kernel-organization/SKILL.md:8-78](https://github.com/sgl-project/sglang/blob/16176278d0180f1a1a578e53e6eef432577876c2/.agents/skills/kernel-organization/SKILL.md#L8-L78)

<a id="unit-e23"></a>
## E23

CI layout, registration, execution. [test/README.md:12-101](https://github.com/sgl-project/sglang/blob/16176278d0180f1a1a578e53e6eef432577876c2/test/README.md#L12-L101)

<a id="unit-e24"></a>
## E24

Serving benchmark CLI. [python/sglang/benchmark/serving.py:2260-2508](https://github.com/sgl-project/sglang/blob/16176278d0180f1a1a578e53e6eef432577876c2/python/sglang/benchmark/serving.py#L2260-L2508)

<a id="unit-e25"></a>
## E25

Benchmark warmup and flush. [python/sglang/benchmark/serving.py:1482-1535](https://github.com/sgl-project/sglang/blob/16176278d0180f1a1a578e53e6eef432577876c2/python/sglang/benchmark/serving.py#L1482-L1535)

<a id="unit-e26"></a>
## E26

One-batch CLI. [python/sglang/benchmark/one_batch.py:227-280](https://github.com/sgl-project/sglang/blob/16176278d0180f1a1a578e53e6eef432577876c2/python/sglang/benchmark/one_batch.py#L227-L280)

<a id="unit-e27"></a>
## E27

KL consistency meanings. [.agents/skills/kl-consistency-test/SKILL.md:8-88](https://github.com/sgl-project/sglang/blob/16176278d0180f1a1a578e53e6eef432577876c2/.agents/skills/kl-consistency-test/SKILL.md#L8-L88)

<a id="unit-e28"></a>
## E28

Serve/version command dispatch. [python/sglang/cli/main.py:1-57](https://github.com/sgl-project/sglang/blob/16176278d0180f1a1a578e53e6eef432577876c2/python/sglang/cli/main.py#L1-L57)

<a id="unit-e29"></a>
## E29

Deprecated launch module. [python/sglang/launch_server.py:68-86](https://github.com/sgl-project/sglang/blob/16176278d0180f1a1a578e53e6eef432577876c2/python/sglang/launch_server.py#L68-L86)

<a id="unit-e30"></a>
## E30

Deprecated benchmark module. [python/sglang/bench_serving.py:1-22](https://github.com/sgl-project/sglang/blob/16176278d0180f1a1a578e53e6eef432577876c2/python/sglang/bench_serving.py#L1-L22)

<a id="unit-e31"></a>
## E31

Dependency declarations. [python/pyproject.toml:1-106](https://github.com/sgl-project/sglang/blob/16176278d0180f1a1a578e53e6eef432577876c2/python/pyproject.toml#L1-L106)

<a id="unit-e32"></a>
## E32

Dynamic SCM version. [python/pyproject.toml:259-264](https://github.com/sgl-project/sglang/blob/16176278d0180f1a1a578e53e6eef432577876c2/python/pyproject.toml#L259-L264)

<a id="unit-e33"></a>
## E33

Source license. [LICENSE:1-25](https://github.com/sgl-project/sglang/blob/16176278d0180f1a1a578e53e6eef432577876c2/LICENSE#L1-L25)

<a id="unit-e34"></a>
## E34

CLI field to option mapping. [python/sglang/srt/arg_groups/arg_utils.py:285-349](https://github.com/sgl-project/sglang/blob/16176278d0180f1a1a578e53e6eef432577876c2/python/sglang/srt/arg_groups/arg_utils.py#L285-L349)

<a id="unit-e35"></a>
## E35

CPU CI registration checker. [scripts/lint/check_registered_tests.py:91-141](https://github.com/sgl-project/sglang/blob/16176278d0180f1a1a578e53e6eef432577876c2/scripts/lint/check_registered_tests.py#L91-L141)

<a id="unit-e36"></a>
## E36

Native CPU kernel tests. [test/registered/unit/kernels/test_kernels_namespace.py:1-77](https://github.com/sgl-project/sglang/blob/16176278d0180f1a1a578e53e6eef432577876c2/test/registered/unit/kernels/test_kernels_namespace.py#L1-L77)

<a id="unit-e37"></a>
## E37

New model integration guide. [docs/docs/supported-models/support_new_models.mdx:8-76](https://github.com/sgl-project/sglang/blob/16176278d0180f1a1a578e53e6eef432577876c2/docs/docs/supported-models/support_new_models.mdx#L8-L76)

<a id="unit-e38"></a>
## E38

Expert parallel size. [python/sglang/srt/arg_groups/fields/parallel.py:266-285](https://github.com/sgl-project/sglang/blob/16176278d0180f1a1a578e53e6eef432577876c2/python/sglang/srt/arg_groups/fields/parallel.py#L266-L285)

<a id="unit-e39"></a>
## E39

Benchmark warmup argument. [python/sglang/benchmark/serving.py:2659-2665](https://github.com/sgl-project/sglang/blob/16176278d0180f1a1a578e53e6eef432577876c2/python/sglang/benchmark/serving.py#L2659-L2665)
