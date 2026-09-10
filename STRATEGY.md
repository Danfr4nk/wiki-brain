# STRATEGY — what this repository is doing and why (read me if you read nothing else)

Any model should be able to open this repository cold and continue the work correctly by reading this file. It states the strategy in plain language.

The governing set, in the order a new reader should meet it:

| **File** | **Governs** | **Wins on** |
| --- | --- | --- |
| **STRATEGY.md** (this file) | what we are doing and why | intent |
| **CLAUDE.md** | the operations — ingest, query, climb, lint | process |
| **EXTRACTION_SPEC.md** | how deep to go into a source before writing | depth |
| **STYLE_GUIDE.md** | page format and the substance standard | format |
| **CONNECTIONS_SPEC.md** | typed edges and their claims | edges |
| **SYNTHESIS_SPEC.md** | altitude — how conclusions stack on conclusions | climbing |

`BACKLOG.md` holds the standing work; `LLM_HANDOFF.md` holds the exact resume point.

## The purpose

This wiki is a second brain about one person, Dan Frank. Its job is to collect, store, and synthesize as much data as possible about his life, mind, history, ideology, environment, and relationship to reality — every story, every friend, every place, every perspective, every development, every thought. Every data point gets an entry.

Each entry carries two things: everything known about it as of ingestion, and everything later produced by using it in analysis alongside the rest of the corpus. A wiki entry is never just a record — it's a live node that accumulates conclusions drawn from reading it against everything else.

Beyond archiving, the wiki is an analytical instrument in its own right: it exists to **mine one life for hidden connections** — linkages between people, events, money, substances, music, work, and psychology that no single source states, but that the corpus proves when read across itself. A fact filed is worth little. A connection argued is the product.

## The core loop

The system runs on one repeating cycle:

**Story → Entry → Every entry the source touches → Analysis → Synthesized finding → Saved back to every entry it draws from → Repeat.**

1. A memory, fact, or document is captured once and filed immutably into `raw/`.

1. It's read from `raw/` **to exhaustion**, and that understanding is written into a durable `wiki/` page — this is a ground-floor entry.

1. **Every other page that source touches gets the touch written into it** — every person, work, place, event and concept it names that already has an entry, whether or not a conclusion came out of it. This step is not the write-back in step 6: that one moves a *finding* you reached, this one moves *evidence* the source contains, and it is owed the moment the source names something. It is also the step with no symptom when it is skipped — the entry you wrote reads as complete, the entries you did not touch have no way to learn a source is talking about them, and the corpus quietly ends up holding less than `raw/` does at the one layer synthesis reads from. `EXTRACTION_SPEC.md` move 9; `bin/wiki-crosslink` measures it.

1. Once enough ground entries exist, they're read *across* each other — not one at a time — looking for a pattern that no single entry states but that several together prove.

1. That pattern becomes its own finding: a synthesis, stated as a falsifiable claim, not a vague observation.

1. The finding is written back into **every ground entry it draws from**, via a typed connection with an argued claim — so the insight doesn't have to be re-derived the next time someone lands on that entry.

1. The finding itself becomes a premise for the *next* round: junctions can be read across each other to find doctrine, the same way ground entries were read across each other to find junctions.

This is **amortized insight**. Analysis is expensive to do well, so it's done once, saved at every point it's relevant, and each future pass starts from a higher floor instead of re-deriving what's already known. Nothing above this line is optional flavor text — it's the actual mechanism the rest of the spec files exist to support.

## Depth is the binding constraint

For the first year the limiting factor was coverage: there were not enough pages. That is no longer true — there are 438. **The limiting factor now is how deeply each source gets mined and how much of what is found actually reaches a page.**

The reason is mechanical, and it is the most important sentence in this file:

A pattern can only be found among details that were written down. Every detail dropped at extraction is a connection that can never be made, by anyone, later — because step 3 of the loop reasons from `wiki/`, not from `raw/`.

So the standing instruction is **longer, denser, more exhaustive entries**, and the standard for reading a source is *exhaustion* rather than retrieval: a source is read when a second careful pass would find nothing material you missed. Sources already marked ingested routinely turn out to hold three times what the first pass took, and the leftovers are not marginal — they are the findings that reorganise pages.

This is not hoarding. A detail's value is not its own significance, which is assigned later by the climb; it is the **surface area** it adds for the next climb to land on. The detail that looks meaningless at extraction time is exactly the one that turns out to be the third instance of a shape — and it can only do that if it is on a page. Page-size warnings are advisory and never a reason to drop content.

`EXTRACTION_SPEC.md` is the full doctrine: the eight moves, the source tiers, and the per-source traps that fail silently.

## Why altitude matters

The product isn't flat. Every conclusion written today is a **premise** available tomorrow:

- **Ground pages** carry entities and events read out of `raw/`.

- **Junction pages** carry the pattern found across three or more ground pages, spanning two or more domains.

- **Doctrine pages** carry the rule found across junctions.

Each layer declares its `synthesizes:` list, naming exactly what it was built from, so the dependency chain is visible, checkable, and stays current when something below it changes. The loop is meant to run forever: ingest raises the floor, CLIMB raises the ceiling, and the new ceiling becomes the floor for the next climb. A repository of accurate ground pages with nothing built on top of them is an archive. **The altitude is the brain.**

## The pipeline in one paragraph

Material enters `inbox/`, is filed immutably into `raw/`, and is read to exhaustion — the understanding extracted from it is written into `wiki/` as prose pages. From then on, reasoning happens FROM the wiki, returning to `raw/` only when the wiki is silent or a claim needs primary verification. Pages are either `derived` (mechanically regenerable from raw — counts, discographies) or `earned` (conclusions produced by reasoning — NOT regenerable, must be revised, never rewritten from scratch). `raw/self/context-core/CONTEXT_CORE_EXPANDED.md` is the single most authoritative raw source.

## Why connections are typed

The graph audit of 2026-07-17 found the wiki full of links that said nothing: "Related: tom" records that two pages touch, not how. That's an index, not a brain. Every connection is now a **typed edge with a claim** — a relationship type from a fixed vocabulary plus one argued sentence:

connections:

- page: wiki/people/tom

type: supplies

claim: "Tom is the physical supply line whose spring-2026 delivery failures are the proximate trigger of the friendship's rupture."

The claim is the knowledge. It survives being read cold, it can be grepped, and chains of typed edges compose into arguments (X causes Y, Y evidences Z). Full vocabulary and rules live in `CONNECTIONS_SPEC.md`. Bare `related:` lists and `## Related` footers are deprecated and being removed.

## The junction-page mechanism — and the operation that runs it

When three or more pages across two or more domains show the same pattern, that pattern earns its own synthesis page. Each member carries an `instantiates` edge into it; the new page declares `synthesizes:` listing its members. This is how N scattered observations become one reusable premise — the compounding mechanism, and the highest-value work in the repository. A discovered cross-domain pattern is worth more than any ten routine link fixes.

The operation is called **CLIMB**, alongside INGEST, QUERY, and LINT. `bin/wiki-climb candidates` mines the backlog into `synthesis-queue.md`; `bin/wiki-climb audit` shows which domains are all ground and no junction; `bin/wiki-climb check` reports **stale** pages — ones whose premises changed after they were written. Protocol in `SYNTHESIS_SPEC.md`. Two rules matter more than the rest:

- **A cluster you cannot state a falsifiable rule about gets rejected in the queue, with reasoning.** A considered non-synthesis is knowledge. A page whose thesis is "these things are related" is worse than no page.

- **When a conclusion is falsified, the failure stays on the page.** The block/unblock loop predicted the June 2026 severance would hold, and was wrong 52 days later because it scored dependency as material and missed a shared dog. The correction made the rule wider and truer — and that wider rule exists in no raw source anywhere. That is what this system is for.

## The substance standard in one paragraph

The first paragraph of every page must answer the stranger's question (for a person: who is this to Dan, what is the current state, what is the defining thing; for an event: what happened and what changed). Order by consequence, not chronology. State load-bearing conclusions plainly. Name gaps explicitly. Tables hold numbers; prose holds meaning. Write long — the operator's standing directive is denser and more exhaustive entries than the current standard, and no page has yet been too long. Exemplar pages — imitate their shape — are `wiki/people/annie-ulmer.md`, `wiki/people/suzanne-frank.md`, `wiki/people/alexis-armel.md`, `wiki/timeline/events/eli-incident.md`. A page that is tidy but leads with corpus statistics instead of the story is a failed page.

## The five unbreakable rules

If you are unsure about anything else here, follow these and you cannot corrupt the system.

1. **Never write an untyped link.** Every connection gets a `type` from the CONNECTIONS_SPEC vocabulary and a `claim` sentence. If you cannot write the claim, do not make the connection — record the rejection in `connection-queue.md` with one line of reasoning.

1. **Never state a fact without a raw source that exists on disk.** Verify numbers and quotes against `raw/` before writing them; attribute AI-generated material as such. Never guess identities — grep all known names and handles first. Known trap: `MASTER_MESSAGES_DB_DUMP.csv` marks nearly everything `Received`, so any claim about what *Dan* said must come from `all_imessages_complete_dump.txt`.

1. **Never stop at what you came for.** A source is read when it is exhausted, not when it has answered your question. Chase every proper noun, re-derive every number, note what is conspicuously absent, and write down the mundane — the climb cannot reach what extraction filtered out (`EXTRACTION_SPEC.md`).

1. **Never clear a stale warning by bumping the date.** If `wiki-climb check` says a page's premise moved, read what changed and decide whether the conclusion survives, then record that decision on the page. Silencing it is the one move that corrupts the system quietly, because everything built above the page keeps compounding on a premise nobody re-checked.

1. **Leave the site as you found it, plus your work.** Run `bin/wiki-lint`, `bin/wiki-connect check`, and `bin/wiki-climb check` before committing; regenerate `bin/wiki-digest` and `bin/llm-publish` after a content pass; append to `log.md`; update `LLM_HANDOFF.md` with what you did and the exact resume point.

## The model of the product

What a finished piece of work looks like: the junction-page trio (`supply-network`, `estate-money-spine`, `block-unblock-loop`) for synthesis — verified members, typed edges with argued claims, inverse edges on every member, one governing rule stated plainly, gaps named. For ground pages, the four rewritten on 2026-08-08 (`alexis-armel`, `jacob-bacharach`, `117-belmont-circle`, `zach-clingan`) are the depth standard: every claim re-derived from raw, corrections flagged rather than silently applied, and the mundane kept.

Two things are worth more than volume of output. **Negative results** — "checked X, it is not there" — are cheap falsifiers and belong on pages. And **corrections of the wiki's own errors**, with the old claim left visible, are the most valuable artifact the repository produces, because they are where the model of Dan actually improves.

## Current campaign

Three run in parallel.

**Depth (extraction).** The binding constraint. Work `BACKLOG.md` §1 — the Gchat archive first, then behavioural rather than lexical mining, then second passes over sources already marked ingested. Per `EXTRACTION_SPEC.md`.

**Height (the climb).** Four domains — `self`, `timeline`, `work`, `places` — have three or more pages and nothing above any of them. Work `synthesis-queue.md` top-down, one climb per pass, per `SYNTHESIS_SPEC.md`. `bin/wiki-climb audit` shows live progress.

**Breadth (the retrofit).** Converting the legacy graph to typed connections, page by page, in the priority order in `CONNECTIONS_SPEC.md`, deepening body copy from raw in the same pass. `bin/wiki-connect audit` shows live progress.

See `LLM_HANDOFF.md` for the exact resume point.
