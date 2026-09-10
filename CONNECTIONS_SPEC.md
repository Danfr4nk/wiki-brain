# Connections Spec — typed edges with claims

Adopted 2026-07-17. One of the six governing documents (see `STRATEGY.md` for the full set and what each wins on): `STYLE_GUIDE.md` governs page format, `EXTRACTION_SPEC.md` governs how deep to mine a source, and **this file governs the format and discipline of inter-page connections**. `bin/wiki-connect check` mechanically enforces it. It exists because the graph audit of 2026-07-17 found the wiki quantitatively linked (2,006 prose edges, 6.5 avg outdegree) but semantically under-connected: 33% of all links were bare list items or "## Related" footer dumps carrying zero information about WHY the pages relate, 1,620 `related:` frontmatter entries were untyped and only 31% reciprocal, 56 real pages were reachable only through indexes, and 2,838 page-pairs had concrete shared evidence (same raw sources, unlinked name mentions, co-citation) with no connection made. A second brain whose edges are adjacency lists is an index. The edges have to be propositions.

## The unit: a connection is a claim

A connection between two pages is a **typed edge with a one-sentence argued claim**, stored in frontmatter and (for load-bearing edges) argued in prose. "Related: tom" tells a future reader nothing. "Tom `supplies` the neurochemical stack whose delivery failures are the proximate trigger of the May 2026 rupture" is knowledge — it survives being read cold, it is greppable, and it composes: chains of typed edges are themselves queryable arguments (X causes Y, Y evidences Z).

## Frontmatter format

`connections:` replaces `related:` as pages are retrofitted (see protocol below — do not bulk-convert). `related:` remains legal on untouched pages but is deprecated; new pages MUST use `connections:`.

connections:

- page: wiki/people/tom

type: supplies

claim: "Tom is the physical supply line for the engineered stack; his delivery failures in spring 2026 are the proximate trigger of the friendship's rupture."

- page: wiki/mind/synthesis/attachment-trauma-bond

type: instantiates

claim: "The 87% re-engagement loop documented for Annie reappears here at lower amplitude — block/unblock cycling with Tom in May 2026 — showing the pattern is architectural, not partner-specific."

Rules:

- `page`: wiki path, no .md needed, must resolve.

- `type`: from the controlled vocabulary below. Invent nothing.

- `claim`: one complete sentence, ≥25 chars, that a stranger could evaluate. It states the relationship, not the existence of one. "These pages are related" is a lint failure in spirit even where it passes mechanically.

- 3–10 connections per page. If a page earns more than 10, the excess usually means a missing junction page (below).

## Edge type vocabulary

Directional pairs (write the inverse on the target page — `check` warns when missing):

| **type** | **inverse** | **meaning** |
| --- | --- | --- |
| causes | caused-by | A is a documented cause/driver of B |
| evidences | evidenced-by | A is primary evidence for the claim B makes |
| instantiates | instance-of | A is a concrete case of pattern/concept B |
| precedes | follows | temporal/causal sequence (timeline spine) |
| supplies | supplied-by | material/logistical dependency |
| component-of | contains | part/whole |

Symmetric (same type on both pages):

| **type** | **meaning** |
| --- | --- |
| contradicts | the pages make incompatible claims — MUST also carry a `> **CONTRADICTION:**` block per CLAUDE.md rule 7 |
| parallels | same structure in different domains/eras (the highest-value type: this is where synthesis lives) |
| mirrors | inverted/complementary structure |
| co-occurs | documented joint presence without asserted causation — the weakest legal type; use when the evidence stops short of a stronger claim |

Directional, no inverse required: `escalates`, `resolves`, `contextualizes`.

Choosing `co-occurs` when the raw would support `causes` is a substance failure; choosing `causes` when the raw only supports `co-occurs` is a provenance failure. The type IS the analytical commitment.

## Prose requirement for load-bearing edges

Any edge typed `causes`, `contradicts`, `instantiates`, or `parallels` must also be argued in the body prose of at least one of the two pages — a sentence or paragraph where the wikilink appears inside the argument, not in a list. The frontmatter edge is the queryable record; the prose is where the reasoning lives. `## Related` / `## See also` footers are banned on retrofitted pages: if a footer link deserves to exist, it deserves a typed edge and a claim; if it can't earn a claim, delete it.

## The inverse claim carries the finding (added 2026-08-01)

Two different things both produce an inverse edge, and they are held to different standards. Confusing them is why some inverse claims say nothing.

**A retrofit inverse** — added while converting a legacy `related:` list — may be frontmatter-only and may simply restate the relationship from the other side. Its prose pass comes later (retrofit protocol step 4).

**A write-back inverse** — added because a synthesis page concluded something about this page — is held to `STRATEGY.md`'s core loop, step 6, and must state **what this page turned out to be evidence of.** The test: a reader who lands here and reads only the `connections:` block should come away with the conclusion, not with a pointer to where the conclusion is kept.

# fails — names a relationship, transmits nothing

- page: wiki/mind/synthesis/dormancy-not-exit

type: instantiates

claim: "This page is one of the members of the dormancy-not-exit synthesis."

# passes — the finding itself, readable cold, at the point of arrival

- page: wiki/mind/synthesis/dormancy-not-exit

type: instantiates

claim: "Seventeen years of continuous presence after the 2009 breakup — Suzanne's closest friend, the cat's co-guardian, a Christmas fixture — is the cleanest case of a romantic role ending without the tie ending."

The corpus is read one page at a time by models with finite context, and they arrive at member pages far more often than at synthesis pages. A claim that merely points is a claim that will be skipped, and the conclusion behind it will be re-derived from less evidence. Full rationale: `SYNTHESIS_SPEC.md`, "The write-back obligation."

## The source-mention obligation (added 2026-09-04)

The write-back rule above covers a **finding**: a conclusion reached on one page, owed to the pages it was drawn from. This covers the case one layer below it, which is more common and has no rule of its own until now.

**When a source names something that already has a page, both pages are owed an edge — before any finding exists.**

A page assembled from a corpus records what its writer found interesting. That is a strict subset of what the corpus contains, and the difference is invisible from either end: the page reads as complete, and the target page has no way to learn that a source it never saw is talking about it. Nothing goes red. No warning fires. The wiki simply holds less than its own `raw/` does, at the one layer where it matters most, because synthesis reasons from `wiki/`.

The measured case: nineteen `wiki/self/twitter/` year pages, each written by reading its year in full, carried 130 typed edges between them. The same archive names the concert record, four artist pages, two people pages, an alias page and a health row — none of them linked, and one autumn of it was enough to falsify claims on three of those pages.

**What the claim says when there is no finding yet.** An edge is still a proposition, so a bare adjacency is still banned. State what the source *supplies*:

# fails — an adjacency wearing a claim's clothes

- page: wiki/self/twitter/2008

type: evidenced-by

claim: "The 2008 tweets mention this band."

# passes — says what the target page did not have

- page: wiki/self/twitter/2008

type: evidenced-by

claim: "'i miss the starting line.' (30 November 2008) is the only evidence in the corpus that the band meant anything to him beyond the 2005 tour bill this page otherwise rests on — posted during their hiatus, three years after the show."

The second is writable before anybody knows what it means, and it is what makes the mention reachable by the climb that eventually does.

**Where to point first: a page's claims about itself.** The highest-value mentions are the ones that hit a page's own stated completeness or stated limits. `wiki/interests/concert-record/index` said "the master table below is the complete record"; `wiki/people/katie-fletcher` said "everything known arrives through Dan's later AI-session narration"; `wiki/health/chemical- architecture` said the nicotine row "has no ledger entries at all and remains description". All three were checkable, and all three moved.

**Tooling, and its limits.** `bin/wiki-crosslink scan <page>` reads the corpora a page's own `sources:` name, inside the page's own date range, and lists entities with pages the page does not link. `bin/wiki-crosslink reciprocal` computes the inverse-edge debt this file requires but nothing measured. Both emit **candidates**. A candidate is a reason to open the source rows it prints; it is never a reason to write an edge, and a mention is not a relationship — a tweet naming Diplo is a consumption datapoint, not a Diplo relationship, and the type and claim can only come from reading.

**An edge into a generated page cannot be reciprocated**, and that is not a debt. `wiki/meta/testimony-veracity`, `wiki/meta/skills`, `wiki/health/intake-ledger` and the rest of `CLAUDE.md`'s generated surfaces are overwritten on every run; a hand-added inverse there dies silently and fails that generator's own check. `wiki-crosslink` knows the list and reports them apart from the debt rather than demanding work nobody may do.

## Junction pages — where cross-domain tissue accumulates

When 3+ pages across ≥2 domains share a typed pattern, the pattern gets its own `page_type: synthesis` page (domain: mind/ unless clearly owned elsewhere), and the member pages each carry an `instantiates` edge into it. This is the compounding mechanism: the junction page is earned knowledge that turns N pairwise observations into one reusable premise. Candidate junctions already visible in the mined queue (verify against raw before writing — do not write these from this list alone):

- **The supply network as a system** — Tom, Teddy, Johnny, the dealer contacts, intake-constancy, the work pages: currently N separate supply mentions, no page that treats procurement as one architecture with redundancy, failure modes, and the documented rupture pattern.

- **The estate/money spine** — Fran's 2020 distribution ($144,069.31), the 337 Saratoga sale, the Rick/PNC trust thread, the 2017–2018 poverty floor: money events currently live on person and event pages with no page tracing the capital timeline as a single causal chain.

- **The block/unblock loop as portable architecture** — documented for Annie (127/110), reappearing with Tom (May 2026): attachment-trauma-bond covers Annie; the generalization across partners/friends is unwritten.

- **Interests as era-markers** — the 2024 Roman-immersion year, the 2012–13 O&A binge, the 2020 left turn: interest pages currently island (5 of them index-only); each is dateable and should carry `precedes`/`follows`/`contextualizes` edges into timeline periods.

## Retrofit protocol (per page, never bulk)

Same discipline as ingest — one page per pass, fully:

1. Run `bin/wiki-connect candidates` if the queue is stale; take the page's pairs from `connection-queue.md` plus its existing `related:` list.

1. For each candidate/related entry: re-read enough of both pages (and raw, when the claim needs it) to commit to a type and write the claim. A pair with no defensible claim is REJECTED in the queue file with one line of reasoning — a considered non-edge is also knowledge; do not link it anyway.

1. Write the `connections:` block; delete `related:`; convert or delete the `## Related` footer; ensure load-bearing edges appear in prose.

1. Add the inverse edge on each target page. Frontmatter only is fine for a *retrofit* inverse; its prose pass will come. A *write-back* inverse — one carrying a synthesis finding — is held to the higher bar above and must state the finding itself.

1. `bin/wiki-connect check` and `bin/wiki-lint` must both pass.

1. log.md: `## [YYYY-MM-DD] connect | <domain> | <page> (N edges, M rejected)`. Commit.

Priority order for the retrofit: (1) the 56 islanded pages — they need inbound prose edges or an explicit demotion decision; (2) the 13 synthesis pages — the capstones must be wired in, not orphaned (dan-annie-fallout- verdict, 2020-left-turn, music-as-identity, and message-circadian-latency are currently islands, which is the single most damning audit finding); (3) top of connection-queue.md by score; (4) everything still carrying `related:`.

## Worked example — wiki/people/tom.md

Current state: 9 untyped `related:` entries + a `## Related` footer of six dot-separated links. Retrofit (claims below are supported by the page's own body text; a real pass verifies against raw):

connections:

- page: wiki/mind/synthesis/vertical-authority-skepticism

type: evidences

claim: "Tom is the positive-case exhibit: the clearest safe lateral (peer, non-paternal) attachment in the corpus, against which the vertical-suspect pattern is measured."

- page: wiki/mind/concepts/attachment-model

type: instantiates

claim: "The May 2026 block/unblock cycling with Tom shows the conflict architecture running on a peer bond at lower amplitude — the model is partner-independent."

- page: wiki/people/kristin

type: contains

claim: "The intense late-2025 Kristin thread enters the graph through Tom's social circle; he is the introduction vector."

- page: wiki/people/annie-ulmer

type: co-occurs

claim: "Tom is a recurring selected participant in the 2018–2024 arrangement, chosen because aftermath with a friend was manageable — see arrangement-history for the framework."

- page: wiki/timeline/periods/2025-collapse

type: supplies

claim: "During the Annie collapse Tom is simultaneously crisis anchor and supply line; the dual role is what makes the spring 2026 supply failures a relationship-ending event rather than a logistics problem."

The footer is deleted; each of these already has or gains a prose sentence. `gemini-activity` and `gemini-18` from the old footer are REJECTED as edges (they are source-provenance, which `sources:` already records — a chat that mentions Tom is not a relationship between pages).

## Tooling

- `bin/wiki-connect audit` — graph health: edges, islands, claim coverage, domain-pair matrix.

- `bin/wiki-connect candidates [N]` — regenerates `connection-queue.md` from four evidence signals (shared raw sources ×2.0, unlinked co-mentions ×1.5, co-citation ×0.5, tag overlap ×0.75 reinforcement; cross-domain pairs boosted 1.4× because cross-domain tissue is the scarce resource).

- `bin/wiki-connect check` — lints typed edges (resolution, vocabulary, claim length), warns on missing inverses and surviving bare footers. Run alongside `bin/wiki-lint` before every commit.

- `bin/wiki-crosslink scan <page>|--all` — the source-mention obligation computed: entities named in a page's own cited corpus, inside its own date range, that have pages it does not link. Candidates only.

- `bin/wiki-crosslink reciprocal [prefix]` — the inverse-edge debt this file requires, counted rather than remembered; `check` prints the total and always exits 0, because a one-way edge still carries its claim and a gate that blocked unrelated commits on it would acquire an escape hatch.
