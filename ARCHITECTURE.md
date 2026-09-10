# ARCHITECTURE.md

Wiki Brain is a source-grounded, longitudinal knowledge graph and cognitive
modeling system. It archives raw evidence about a person and their surrounding
world, transforms that evidence into atomic facts, events, entities,
relationships, patterns and higher-order syntheses, and gives an LLM persistent
context for reasoning about that person — **without collapsing evidence,
interpretation and inference into the same layer.**

That last clause is the whole system. Everything below exists to enforce it.

---

## The constitutional law

```
RAW DATA → STRUCTURED FACT → INTERPRETATION → SYNTHESIS.  NEVER THE REVERSE.
```

And immediately beneath it:

> Every synthesis must be capable of being traced back to the evidence that
> produced it.

These are not aspirations in a style guide. They are a mechanically checked
invariant — see **The one invariant** below — and `bin/wb-validate` fails the
build when they are broken.

## Why an ordinary wiki cannot do this

A folder of Markdown pages has no way to stop a conclusion from becoming a
premise. Someone writes "the relationship was abusive" on a synthesis page,
and six months later that sentence is quoted on an event page as though it
were something that was observed at the time. Nothing in the filesystem
objects. The interpretation has silently become a fact, and the evidence that
would let anyone check it is gone.

That failure has a direction. It always runs *downward* — from conclusion into
evidence. So the system is built around a single directional rule, and the
validator enforces it on every commit.

## The six layers

Every node in the knowledge base sits at exactly one layer.

| L | Layer | What it is | Mutable? |
| :-- | :---- | :---- | :---- |
| **0** | `source` | Raw material as acquired. A message export, a photo, a transcript, a document. | **Never.** Append-only. |
| **1** | `datum` | One claim about one thing at one time under one context, with known provenance. | Corrigible |
| **2** | `entity` `event` `relationship` | Structured objects assembled from data. Who, what, when. | Corrigible |
| **3** | `interpretation` `contradiction` | What it might mean. Explicitly someone's reading, never a fact. | Freely revised |
| **4** | `pattern` | Recurrence detected across layer ≤3. | Freely revised |
| **5** | `synthesis` | Cross-domain model. The compressed cognitive picture. | Freely revised |

Mutability runs opposite to altitude, and that is deliberate. The higher a node
sits, the more disposable it is. An LLM's synthesis is the *most* disposable
thing in the system; the source it rests on is the least.

## The one invariant

> **A node may cite only nodes at a strictly lower layer.**

`cites` is the evidence relation. `L3 → L2 → L1 → L0` is legal. Anything level
or upward is not:

- A `datum` may not cite an `interpretation`. That is a conclusion laundered
  into evidence — the exact failure described above.
- A `pattern` may not cite another `pattern`. Patterns of patterns are
  syntheses; call them that and put them at L5.
- Nothing may cite a `synthesis`. A synthesis is a leaf. It is where reasoning
  ends, never where it starts.

The invariant makes the whole graph a DAG with layers as topological levels, so
"trace this conclusion to its evidence" is a guaranteed-terminating walk, and a
citation cycle is impossible by construction rather than by discipline.

Relations that are *not* evidence — `caused`, `resembled`, `contradicted`,
`preceded` — live in `edges`, which is unconstrained. Only `cites` is directional.

## Node anatomy

Markdown with TOML frontmatter. Machine-readable head, human-readable body,
neither destroying the other. Parsed with stdlib `tomllib` — no dependencies.

```markdown
+++
id         = "evt:2010-02-17-suboxone-start"
layer      = 2
type       = "event"
title      = "Started Suboxone"
confidence = "high"
cites      = ["dat:0412", "dat:0413"]

[when]
date   = "2010-02-17"
period = "early-recovery"

[[edges]]
rel    = "preceded"
target = "evt:2011-first-clean-year"
+++

## Summary

Prose for humans. The frontmatter is for machines. Both describe the same
node and neither is authoritative over the other.
```

### Fields every node carries

| Field | Meaning |
| :---- | :---- |
| `id` | `type:slug`. Stable forever. Renaming is a `supersedes` edge, never an edit. |
| `layer` | 0-5. Must match the type. |
| `type` | One of the types in the layer table. |
| `title` | Human label. |
| `confidence` | `high` `moderate` `low` `speculative` `unknown` |
| `cites` | Evidence. Strictly-lower layers only. |
| `edges` | Typed semantic relations. Any direction. |
| `when` | Temporal block — see below. |

### Layer-specific required fields

- **`source`** — `source_type`, `acquired`, `provenance`, `reliability`.
  Optionally `sensitive = true`, which withholds it from the published site.
- **`datum`** — `cites` naming at least one source. A datum without a source is
  not a datum; it is a belief, and belongs at L3.
- **`interpretation`** — `perspective`, one of:
  - `self` — what the subject believes about themselves
  - `external` — what the accumulated evidence suggests
  - `llm` — what a reasoning system inferred
  - `other` — a third party's reading
  These never silently collapse into each other. "Dan believes X about himself,
  but the longitudinal record suggests Y" is a first-class expressible statement,
  and it is one of the most valuable things the system can say.
- **`contradiction`** — `cites` at least two conflicting nodes, and carries
  `resolved = false` by default. Contradictions are data. The correct output is
  often "the historical record is ambiguous," which beats inventing certainty.
- **`pattern`** — `evidence_count`, `counterexamples`. A pattern that has never
  looked for its own counterexamples is an anecdote.

## Time

A static profile of a human being is inadequate on its face — people are
longitudinal systems. Every node may carry `[when]`:

```toml
[when]
date       = "2018-03-04"      # exact
approx     = "spring 2018"     # fuzzy, when exact is unknown
start      = "2015-11"         # range
end        = "2019-07"
period     = "uniontown-years" # named life period
recurrence = "weekly"
age        = 29
```

Personality is therefore a trajectory, not a snapshot. `state` vs `trait` vs
`adaptation` is a required field on behavioral interpretations, because
"socially withdrawn" (state), "low sociability" (trait) and "avoids people
after repeated conflict" (adaptation) are three different claims that generic
personality language flattens into one.

Temporal contradiction is legal and expected. Someone can be X at 18, not-X at
25, and X again at 37. The system does not force consistency, because human
beings are historical processes rather than internally consistent databases.

## Typed edges

Links carry meaning. `A → B` is not enough.

`caused` · `influenced` · `contradicted` · `preceded` · `followed` ·
`depended_on` · `resembled` · `symbolized` · `belonged_to` · `occurred_during` ·
`resulted_from` · `evidences` · `challenges` · `supersedes` · `participated_in` ·
`located_at` · `about`

Causal vocabulary is deliberately graded, because the distinction between
sequence and causation is exactly where personal narrative goes wrong:

- `preceded` — temporal sequence only. Makes no causal claim.
- `influenced` — plausible contribution.
- `caused` — an explicit causal claim, and it requires
  `causal_basis = "stated" | "inferred" | "speculative"`.

"Event A preceded behavior B" and "Event A caused behavior B" are different
sentences, and the schema refuses to let them be written the same way.

## What the system refuses to do

- **Resolve contradictions automatically.** Both claims are preserved, dated
  and attributed.
- **Let synthesis mutate sources.** Concluding "this was abusive" adds an L3
  node. It does not rewrite the L2 events into "abuse occurred."
- **Flatten hindsight onto the past.** If the subject believed "everything is
  fine" during a period later remembered as disastrous, both are recorded. That
  is what makes reconstructing subjective reality at the time possible.
- **Treat absence as evidence of absence.** `negative` data distinguishes
  `never_observed`, `explicitly_rejected` and `known_not_to_occur`. These are
  not equivalent, and the corpus policy exists because conflating them is what
  produced the conclusions this rebuild supersedes.

## Repository layout

```
schema/          JSON Schema per node type — the enforceable contract
kb/              the knowledge base
  sources/       L0   raw material index
  data/          L1   atomic datapoints
  entities/      L2   people, places, institutions, artifacts, concepts
  events/        L2   what happened
  relationships/ L2   first-class relationship objects
  interpretations/ L3 readings, contradictions
  patterns/      L4   recurrence
  syntheses/     L5   cross-domain models
corpus/          the authoritative message record (gitignored; see CORPUS_POLICY.md)
bin/             wb-validate, wb-build, wb-query, corpus-*
site/            generated static site (gitignored, published to Pages)
```

## Retrieval, not dumping

An LLM should not ingest the whole wiki on every question. `bin/wb-query`
assembles layered context:

1. **Immediate** — directly relevant nodes
2. **Local** — their neighbours in the graph
3. **Historical** — what preceded them
4. **Pattern** — similar occurrences elsewhere
5. **Meta** — the broader model

Relevance is graph-based, not merely lexical: semantic proximity, temporal
relevance, relational distance, importance, confidence, recurrence and
contradiction all weigh. The best context is frequently not the text most
similar to the question.

## Published surface

`bin/wb-build` compiles to `site/`, deployed to GitHub Pages on every push to
`main`:

- Browsable HTML, one page per node, with citation chains rendered as
  navigable evidence trails
- `graph.json` — the full machine-readable graph
- `llms.txt` — discovery document for agents
- `agent/manifest.json` — endpoint map

**Nodes marked `sensitive = true` are excluded from every published artifact.**
The repository is public. Sources holding other people's private material stay
local, and their derived layers publish only what does not identify anyone —
the same split `corpus/` already uses, for the same reason.

## The central question

Everything serves one question:

> What is the smallest, most accurate model of this person and their
> environment that explains the largest amount of the available evidence?

Not the prettiest biography. Not the most flattering profile. Not the most
psychologically dramatic explanation. The highest-explanatory-power model —
one that can expand any conclusion back into the evidence that produced it.
