# wiki-brain

A source-grounded, longitudinal knowledge graph and cognitive modeling system.
It archives raw evidence about a person and the world that produced them, turns
that evidence into atomic facts, events, entities, relationships, patterns and
higher-order syntheses, and gives an LLM persistent context for reasoning over
it — **without collapsing evidence, interpretation and inference into the same
layer.**

Published to GitHub Pages: **<https://danfr4nk.github.io/wiki-brain>**

> **One-time setup:** Pages must be enabled by hand — *Settings → Pages →
> Source: **GitHub Actions***. The workflow cannot do this for you:
> `configure-pages` has an `enablement` input, but it requires a Personal
> Access Token rather than the default `GITHUB_TOKEN`, and wiring up a secret
> is more work than clicking the setting once. Until it is set, `validate`
> passes and `deploy` fails.

---

## The constitutional law

```
RAW DATA → STRUCTURED FACT → INTERPRETATION → SYNTHESIS.  NEVER THE REVERSE.
```

Its mechanical form, checked on every build:

> **A node may cite only nodes at a strictly lower layer.**

That single rule is what stops a conclusion from becoming a premise. Without it
someone writes "the relationship was abusive" on a synthesis page, and months
later an event page quotes it as though it were observed at the time — the
interpretation has silently become a fact and the evidence that would let anyone
check it is gone. The failure always runs downward, so the rule is directional,
and `bin/wb-validate` fails the build rather than trusting anyone to be careful.

It also makes the citation graph a DAG with layers as topological levels, so
tracing any conclusion to its evidence terminates, and a citation cycle cannot
be written at all.

## The six layers

| L | Layer | What it is | Mutable? |
| :-- | :---- | :---- | :---- |
| **0** | `source` | Raw material as acquired | **Never.** Append-only |
| **1** | `datum` | One claim, one thing, one time, known provenance | Corrigible |
| **2** | `entity` `event` `relationship` | Structured objects assembled from data | Corrigible |
| **3** | `interpretation` `contradiction` | What it might mean. Someone's reading | Freely revised |
| **4** | `pattern` | Recurrence across layer ≤3 | Freely revised |
| **5** | `synthesis` | Cross-domain model | Freely revised |

Mutability runs opposite to altitude, deliberately. The higher a node sits, the
more disposable it is: an LLM's synthesis is the most disposable thing in the
system, and the source it rests on is the least.

Full design: **[`ARCHITECTURE.md`](ARCHITECTURE.md)**.

## Tools

```sh
bin/wb-validate                    # schema + the layer invariant
bin/wb-build                       # compile to site/ + graph.json + llms.txt
bin/wb-check-publish               # refuse to publish sensitive material
bin/wb-query "why did X happen"    # layered retrieval, not a dump
tests/test-invariant               # 15 regression tests on the invariant
```

Standard library only — no dependencies, no build step, no database. Nodes are
Markdown with TOML frontmatter: machine-readable head, human-readable body,
neither destroying the other.

```markdown
+++
id         = "evt:2026-09-08-rebuild-begins"
layer      = 2
type       = "event"
title      = "Rebuild on the six-layer architecture begins"
cites      = ["dat:0006-drive-copy-lossy"]
confidence = "high"

[when]
date = "2026-09-08"
+++

Prose for humans. The frontmatter is for machines.
```

## What the system refuses to do

- **Resolve contradictions automatically.** Both claims are preserved, dated and
  attributed. "The historical record is ambiguous" beats invented certainty.
- **Let synthesis mutate sources.** Concluding something adds an L3 node; it does
  not rewrite the events underneath.
- **Flatten hindsight onto the past.** If the subject believed "everything is
  fine" during a period later remembered as disastrous, both are kept.
- **Treat absence as evidence of absence.** Negative data is typed:
  `never_observed`, `explicitly_rejected` and `known_not_to_occur` are three
  different claims.
- **Confuse whose reading a claim is.** Every interpretation declares a
  `perspective` — `self`, `external`, `llm` or `other` — so "Dan believes X about
  himself, but the longitudinal record suggests Y" is expressible rather than a
  distinction that quietly disappears.

## Privacy

**This repository is public**, and the message corpus is not the subject's data
alone — it holds the phone numbers, addresses and private words of 498 other
people who did not choose to be published.

So the split is deliberate and enforced in three places:

- `.gitignore` keeps `corpus/messages.csv`, `corpus/private/` and the shelf
  contents out of git, whose history is permanent and searchable.
- `bin/wb-build` excludes any node marked `sensitive = true`, and the citations
  pointing at it — but *declares* the exclusion rather than hiding it, so a
  partial evidence trail never looks complete.
- `bin/wb-check-publish` runs before deploy and asserts the exclusion actually
  happened, against the built output rather than the source.

One thing worth stating plainly, because it is easy to conflate: **the gitignore
is not what protects this data.** The Google Sheet backing the corpus is
deliberately shared "anyone with the link" — a decision on the record, not an
oversight, documented in [`corpus/README.md`](corpus/README.md). Keeping the
corpus out of git history matters on its own terms. It does not narrow who can
reach the sheet. Two separate exposures; one of them is closed.

## Message evidence

[`CORPUS_POLICY.md`](CORPUS_POLICY.md) governs what counts as message evidence.
The complete export — 192,140 messages, 2011-03-19 → 2026-09-07, 577 threads,
498 counterparties — is authoritative. Every earlier per-counterparty extract is
shelved: retained as evidence of what was believed and why it was wrong, never
as evidence of what happened.

```sh
bin/corpus-verify                            # integrity against the manifest
bin/corpus-query --who "Name" --context 3    # read it in situ
```

## Migration

[`MIGRATION.md`](MIGRATION.md) tracks what is still to come across, and why the
Google Drive staging copy is not the source it is coming from.
