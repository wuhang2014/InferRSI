# The InferRSI inference handbook

Start with a question about an inference system. Each reading path works
through an example and ends with a question you can answer from the evidence.

| If you want to… | Start here |
| --- | --- |
| Tell what a timing result actually measures | [Measure one inference request and its cohort](pages/paths/measure-a-request.md) |
| Find out when an asynchronous consumer has finished with a buffer | [Trace shared state across an asynchronous boundary](pages/paths/trace-shared-state.md) |
| Decide what evidence would support a proposed speedup | [Evaluate a proposed speedup](pages/paths/test-a-speedup.md) |

For a particular engine, backend, framework, case or research source, browse
the chapters. Within a chapter, procedures link to the mechanisms, cases and
source material they use. [Table of contents](contents/README.md)

## Find a passage and use it

The installed CLI searches the text of individual sections as well as titles,
tags and established IDs. Copy a reference from the search results into
`read`. Use `links` to see where else a passage is taught.

```bash
inferrsi knowledge handbook search "admission drain" --kind case --limit 3
inferrsi knowledge handbook read "case.admission-drain-occupancy#unit-observation"
inferrsi knowledge handbook links "measurement-boundaries#unit-completion"
inferrsi knowledge handbook compose test-a-speedup
```

In a checkout you can also search the Markdown directly.

```bash
rg -in "host-readable" src/inferrsi/knowledge/data/handbook/pages
```

## How to read the evidence

The source line on each ported page leads to the original material. A catalog
card can be *imported*, its underlying procedure a *candidate*, and its
empirical validation *not_run*. Use the attached readset to see which code
or paper was inspected. Use the case's recorded workload and evidence limits
when carrying a finding into another reading.

This edition covers the packaged skill library, contribution, dependency and
peer records, and research profiles at the revision in the migration receipt.
Scripts, machine-readable inventories, original language fields, licenses and
notices can be read at their packaged source locations. Generated discovery
records resolve to the procedure they describe. The receipt maps each original
file to its handbook page or resource owner. [Migration receipt](migration.json)

To change a lesson, add a section, assemble a reading path or recover an
earlier revision, use the editing guide. [Editing and revisions](EDITING.md)
