# Style Guide — page format and the substance standard

The binding rules for every page in `wiki/`.

`STRATEGY.md` wins on intent, `CLAUDE.md` on process, `EXTRACTION_SPEC.md` on how deep to mine a source, `CONNECTIONS_SPEC.md` on edges, `SYNTHESIS_SPEC.md` on altitude, and **this file on format**. `bin/wiki-lint`, `bin/wiki-connect check` and `bin/wiki-climb check` mechanically enforce the vocabularies below — run all three before every commit.

# Part 1 — Substance

These rules outrank everything in Part 2. A page is not good because it is tidy; it is good because it tells you what matters.

The failure mode of this wiki's early drafts was **inventory masquerading as insight**: message counts and source citations up top, while the actual story — who this person is to Dan, what happened, why it mattered — was buried or missing.

## 1. Write long. This is the standing directive.

**The operator's standing instruction is longer, denser, more exhaustive entries than the current standard, and no page has yet been too long.** Short, choppy pages are the failure mode; a page should be as long as its subject earns, which is usually longer than the first draft.

This is not a stylistic preference, and the reasoning matters because it changes what you do when you are unsure whether to include something:

The wiki's product is patterns found across pages. A pattern can only be found among details that were written down. Every detail dropped is a connection nobody can make later, because synthesis reasons from `wiki/`, not from `raw/`.

So a detail's value is not its own apparent significance — significance gets assigned later, by the climb. Its value is the **surface area** it adds. The trivial-looking fact is exactly the one that turns out to be the third instance of a shape. **When in doubt, include it.**

`bin/wiki-lint` warns at 40 KB. That warning is **advisory** — it means "check that navigation still works," never "shorten this." Never trim earned content to clear it, and never cite it as a reason to leave something out. Split a page only when a genuine navigational improvement results, not to hit a number.

## 2. Every data point gets an entry

Total coverage is the standing ambition: every story, friend, place, perspective, development and thought. Thinness is not a reason to withhold a page — a `status: stub` a later pass can deepen beats a fact that lives nowhere.

The one boundary is **one page per entity**, which always wins over coverage. Before creating a people page, grep for the person under every known name, alias and handle. Merge, never fork. Resolve identity through two independent contact exports before writing, not from the page title (`EXTRACTION_SPEC.md`, "Traps by source type") — a page can be about the wrong human and read perfectly.

## 3. The first-paragraph test

After the title, the first paragraph must answer, in plain language, the question a stranger would ask. Corpus statistics come LAST, never first.

- **Person** — Who is this to Dan, what is the current state of the relationship, and what one thing defines it?

- **Event** — What happened, when, who was involved, and what changed because of it?

- **Period** — What years, what defined daily life then, and how did it begin and end?

- **Concept / synthesis** — State the thesis in one or two sentences, then prove it. Not "this page collects material about X."

## 4. Consequence over chronology

Order sections by importance, not by the order sources were ingested. If the Eli incident is why the relationship ended, it appears on page one of `annie-ulmer.md`, not as row 14 of a timeline table.

## 5. Say the load-bearing thing plainly

If the sources support "she gaslit him for months and the gaslighting hurt more than the affair," write that sentence. Do not scatter it across evidence fragments and hope the reader assembles it. Attribute contested claims to their source and flag genuine contradictions — but do not hedge documented conclusions into mush.

## 6. An entry accumulates

A page carries **two** things: what was known at ingestion, and what has since been *produced* by using it in analysis against the rest of the corpus. The second layer is the difference between a record and a live node.

Concretely: when a synthesis concludes something about this page, that conclusion comes back here — as a typed edge whose claim states the finding (`CONNECTIONS_SPEC.md`), and, where it is load-bearing, as a sentence in the prose. A page used as evidence five times that shows no trace of it will be re-read from scratch the sixth time.

This is why **the page grows rather than being rewritten**. Integrate new material where it belongs in the existing argument; do not append a dated "new information" section at the bottom. That is how pages rot into changelogs.

## 7. Gaps and negative results are content

If something important is unknown — why the 2021–22 corpus goes near-silent, where he'll live after the house sells — say so in a **Gaps** section rather than silently omitting the topic.

Negative results belong on the page too, with the same weight as positive ones. "Checked the reading log; the novel is not in it" is a finding, and usually a cheap falsifier.

**Write each gap so it can be answered by one person in one paragraph.** Most gaps here are not waiting on a better export or a smarter tool — they are waiting on the operator, who can settle them in thirty seconds if the page asks a question rather than gesturing at a fog. *"No verification of the New York period"* is answerable; *"more research needed on this era"* is not. `bin/wiki-gaps` puts the whole list in front of him one page at a time, so a vague gap is a question that never gets asked.

## 8. Say what would prove you wrong

Any page carrying an argued conclusion — every `page_type: synthesis`, most `concept` pages, the load-bearing reads on entity pages — should state what it predicts and what would falsify it. This is the opposite of hedging. *"The rule predicts this severance holds"* is a claim the corpus can settle. *"Dan's relationships are shaped by attachment"* is not.

## 9. Corrections are flagged, never silent

Contradictions get an inline `> **CONTRADICTION:**` blockquote; revisions get `> **REVISED [YYYY-MM-DD]:**`; fixed errors get `> **CORRECTED [YYYY-MM-DD]:**` with the old claim visible and the evidence that killed it.

**When a prediction is settled, record the resolution — never edit the prediction away.** A conclusion that turned out wrong, corrected in place with its original visible, is the most valuable artifact this repository produces: it is where the model of Dan actually improves. The worked examples are `wiki/mind/synthesis/block-unblock-loop.md` (predicted the June 2026 severance would hold; falsified 52 days later; the rule is now wider and the failure is on the page) and the Closing Note on `wiki/people/annie-ulmer.md`. Quietly deleting a falsified claim destroys knowledge; flagging it creates some.

The same applies to the wiki's own errors. A rewrite that fixes a false claim says so, because otherwise the next reader re-derives the error from the same bad source.

## 10. Height is content too

Where the material you are holding is the third or fourth instance of a shape seen elsewhere, say so on the page and name the shape. If there is no page above it yet, that is a CLIMB candidate, not a footnote (`SYNTHESIS_SPEC.md`). The wiki's product is not the facts; it is what the facts turn out to be instances of.

## 11. A conclusion has to be about the person, not about the pages

Any page carrying an argued conclusion — every `page_type: synthesis`, most `concept` pages, every sage answer, and the load-bearing reads on entity pages — is checked against Dan's own constitution before it is written: cognitive stack, measured personality profile, historical precedent, the attitudes and forces acting on him, his security and prosperity, health, romantic state, age and upbringing, geographic and ethnic culture, religious or ideological programming, and axiomatic politics.

This is **the constitution pass**, it is mandatory and deterministic, and the full register list with a worked failure case lives in `SYNTHESIS_SPEC.md`. The rule here is the format consequence: **the page states the result.** Which registers moved the conclusion, which were checked and left it standing, and which the corpus cannot presently speak to — the last being a Gaps entry.

A pattern true of six pages is a fact about six pages. What makes it a fact about Dan is the mechanism underneath it, and this wiki usually already has that mechanism measured. Reaching for it is not decoration; a rule with a cognitive-function or psychometric mechanism under it predicts in domains the corpus has not sampled, and the same rule stated from behaviour alone does not.

## Exemplars

Before rewriting any page, read the exemplar of the same `page_type` and match its shape.

| **Kind** | **Exemplar** |
| --- | --- |
| Person (major) | `wiki/people/annie-ulmer.md`, `wiki/people/suzanne-frank.md` |
| Person (depth standard, 2026-08-08) | `wiki/people/alexis-armel.md` |
| Person (correction-led) | `wiki/people/zach-clingan.md` |
| Event | `wiki/timeline/events/eli-incident.md`, `wiki/timeline/events/the-fall-of-fran.md` |
| Place | `wiki/places/117-belmont-circle.md` |
| Synthesis | `wiki/mind/synthesis/supply-network.md`, `block-unblock-loop.md`, `estate-money-spine.md` |

# Part 2 — Format

## Prose rules

1. **Complete sentences.** No dossier shorthand, no fragment chains. A page must read as prose to a human opening it cold.

1. **Tables hold numbers, prose holds meaning.** Never narrate a table's contents in the surrounding text.

1. **Primary-source voice belongs on the page.** Verbatim first-person material from the subject — his own accounts, essays, correspondence — is an exception to the usual "keep verbatim in raw/" rule: when his wording carries the meaning, it goes on the page as a block quote rather than being paraphrased away. Other sourced verbatim still prefers `raw/` with a short citation.

1. **Attribute AI-generated material as such.** The Gemini/bootloader/CATO/DANSYNTH files are a model reasoning about the corpus, not a record of it. Dan's own words inside a session are primary testimony; the model's factual assertions are not evidence. Three words — "per the bootloader's own synthesis" — is the whole cost.

1. **Dates are absolute.** Convert relative time at write time; flag uncertainty as `(~2019?)`.

1. **No agent chatter anywhere.** No session notes, ingest logs, temp paths, model names, or "this pass did X" — that history lives in `log.md` and the git log.

1. **Indexes are navigation only** — links plus one-line summaries. Index budgets stay tight (8 KB, master index 5 KB) precisely because pages do not.

## Frontmatter

Required fields, in this order:

---

domain: self | timeline | people | mind | work | interests | health | places | legal | meta

page_type: entity | event | concept | period | summary | synthesis | profile | report | chat | note | index | dataset | journey

status: active | stable | stub | closed | archived

date_created: YYYY-MM-DD

date_modified: YYYY-MM-DD

sources: []    # real raw/ paths that exist on disk — T0 evidence

---

`related: []` is **deprecated** — use `connections:` (`CONNECTIONS_SPEC.md`). It remains legal on untouched pages; new pages must not use it.

**`sources:`**** vs ****`synthesizes:`**** — keep the two straight.** `sources:` is for paths under `raw/` and nothing else. `synthesizes:` is for wiki pages this page *reasons from* — the premises it stands on. A `wiki/` path inside `sources:`, or a `raw/` path inside `synthesizes:`, is a `bin/wiki-climb check` error.

synthesizes:                  # wiki pages this page reasons FROM

- wiki/people/annie-ulmer

- wiki/people/tom

Declaring `synthesizes:` takes on an obligation: when one of those pages is modified after this one, `bin/wiki-climb check` marks this page **stale**, and clearing it means re-reading what changed and deciding whether the conclusion survives — recorded on the page as a `> **RE-CHECKED [date]:**` block. Never by bumping `date_modified`. Full rules in `SYNTHESIS_SPEC.md`.

### Optional fields

Use when they add value; never invent new ones.

title: "Human Title"        # when the filename isn't the natural title

aliases: ["nickname", ...]  # alternate names/handles for search & dedupe

tags: [topic, topic]        # 2–5, most relevant first, from the closed set below

importance: critical | high | normal   # triage for LLM context budgets

knowledge: earned | derived | mixed    # is this regenerable from raw/?

date_range_start / date_range_end: YYYY-MM-DD

changelog:                  # only on critical pages; newest first

- date: YYYY-MM-DD

note: "one line"

image: self                 # override the auto illustration; any path under assets/

pending_ingest: YYYY-MM-DD  # written by bin/wiki-gaps, removed by bin/wiki-gaps clear

`pending_ingest:` is the one field on this list that is **not** yours to write by hand. It means the page is carrying an operator answer nobody has acted on yet, and it is removed by the pass that acts on it — see CLAUDE.md, CLOSE. Its date is when the answer was staged, deliberately not the same thing as `date_modified`: a page holding an unintegrated answer has not moved yet.

### `status`

`active` = live situation, expect updates · `stable` = accurate, settled · `stub` = placeholder awaiting real content · `closed` = formally ended · `archived` = pinned artifact in an `archive/` dir, never updated, exempt from budgets.

Default for a finished page is **stable**, not archived. **`closed`**** means a thing has formally ended, not that the page feels finished** — the July 2026 reopening of `annie-ulmer.md`, marked closed six weeks earlier, is the standing cautionary example.

### `knowledge`

Marks what kind of understanding a page holds, so a future agent knows whether re-deriving it from `raw/` would lose anything:

- **`derived`** — mechanical compilation (counts, catalogs, timelines built from slugs). Safely regenerable.

- **`earned`** — a conclusion reasoned to once, not present literally in `raw/`. **Revise these, never regenerate them from scratch.** `page_type: synthesis` and most `concept` pages are earned.

- **`mixed`** — both (most people/event pages: derived tables carrying an earned read). Treat the earned prose as earned.

Absent means `mixed`. `bin/wiki-lint` rejects any other value.

### `tags` — closed set

Reuse these rather than inventing new ones. If a page genuinely needs a tag outside this list, add it to **both** this list and `VALID_TAGS` in `bin/wiki-lint`, so the set stays closed.

relationships, trauma-bond, infidelity, attachment, family,

addiction-recovery, mental-health, physical-health, grief,

legal, dui, financial-stress, housing, career,

music-production, personality-profile, ideology, politics,

forensic-analysis, ai-collaboration, digital-footprint,

uniontown-era, nyc-era, pets, non-monogamy, future,

language, taste, vocabulary,

behavioral-change, boundaries, intensity, trust, consistency

Tags name *concepts*, never people or places — a page about Ally is linked to `wiki/people/ally-lubin`, not tagged `ally`. A person-name tag duplicates the wikilink graph badly: it cannot be followed, it does not appear in `bin/wiki-connect`, and it drifts the moment an alias changes.

There is **no** `author-stub` / `artist-stub` or other invented `page_type`: a stub is `page_type: entity` (or the appropriate type) with `status: stub`.

## The people infobox — mandatory classifier schema

Every `domain: people` page MUST carry an `infobox:` block with at least `name` and `relationship_to_dan`; `bin/wiki-lint` errors otherwise. The box exists so the corpus can be narrowed later ("all NYC female dealers," "all Uniontown family").

**Set a field only when the page body or raw gives a strong signal. Omit — do not guess — when unknown.** `unknown` is a valid explicit value for `sex`, `location` and `relationship_to_dan`.

infobox:

name: "Display Name"

dob: 1988-11-01                  # ISO; omit if not in corpus

sex: female | male | unknown     # recorded/observed sex per corpus, not self-identified gender

location: uniontown | nyc | remote | unknown

relationship_to_dan: partner | ex-partner | friend | family | dealer | coworker | contact | acquaintance | unknown

role: "cell phone store manager" # occupation / functional role; omit if not stated

first_contact: 2018-09-02        # defaults to date_range_start

handles: ["+172****5006", "@handle"]   # MASKED phones / handles, never full numbers

known_for: "the Jan 27 2019 'dead in 15 years' warning"   # one-line hook

- **`location`** — `uniontown` (incl. Brownsville/Perry/Uniontown-area), `nyc` (New York City / Brooklyn / East Village), `remote` (contact only, no physical proximity), or `unknown`.

- **`relationship_to_dan`** — the highest-value classifier for a wiki *about Dan*. `partner` (current), `ex-partner` (former romantic), `friend`, `family` (blood or by marriage), `dealer` (drug source), `coworker`, `contact` (acquaintance with no deeper tie), `acquaintance`, `unknown`.

Non-people pages may carry a freer `infobox:` (any of: born, status, type, aliases, occupation, known_for, relationship, partner, parents, location, duration, outcome, discovered, closed, diagnosis, medication, ideology, affiliation, period, notes). Values may contain `[[wikilinks]]`; they render as real links.

## LLM Quick Brief

Pages marked `importance: critical` should open, after the intro paragraph, with an `## LLM Quick Brief` section: one dense paragraph written for direct context injection — who/what this page covers and the load-bearing facts, self-contained, with wikilinks, under 200 words. Do not add briefs to ordinary pages.

## Chart-ready data — the `dataset` page type

Every quantified table in this wiki lives inside prose, which is correct for a reader but useless to the portal: it would have to scrape a markdown table to plot one, and a scrape breaks the moment a page's prose changes shape. A `page_type: dataset` page exists for the opposite case — a finding whose point *is* a chart, structured so the portal can render it without parsing prose at all. It is not a replacement for tables inside ordinary pages, and it is not where a number goes just because it could be charted; it is for a comparison or a trend that a chart states more clearly than a sentence does, and that is worth a page of its own for that reason.

**Mandatory ****`chart:`**** block**, in addition to every field an ordinary page carries (`domain`, `status`, `date_created`, `date_modified`, `sources`, `knowledge`, `connections:`, and `synthesizes:` for every page this one reasons from):

chart:

kind: line | bar | grouped-bar | area | scatter

title: "One-line chart title, as it should render"

x: { label: "X axis label", type: category | number | date }

y: { label: "Y axis label", type: number }

series:

- name: "Series label as it should render in a legend"

points:

"2015": 7242

"2016": 13954

- name: "A second series, same x-axis"

points:

"2015": 6394

"2016": 14395

`series:` is a list, never a single object — a dataset page with one series is legal, but the shape must stay list-of-series so a two-series page doesn't need restructuring later. Each `points:` map is `{x: y}`; keep every series on the same x-axis so a renderer can plot them together without re-keying. `bin/wiki-lint` requires `kind`, `title`, and at least one named, non-empty series — it does not and cannot check that the numbers are right, so **every value must trace to a source cited in ****`sources:`**** or a page named in ****`synthesizes:`**, exactly like a table in an ordinary page. A `dataset` page still needs the prose an ordinary page needs: what the chart shows, where the numbers come from, and what would be a wrong way to read it. The chart is the point; it is not a substitute for the argument.

**Never invent a ****`dataset`**** page to avoid writing a table well.** If the finding is a handful of numbers inside a larger argument, a markdown table in the page that argument belongs to is still correct — `dataset` is for a comparison that stands on its own, is not a footnote to a larger page, and would lose something real if it were only prose. Exemplar: [[wiki/mind/synthesis/annual-volume-suz]].

## Themed journeys — the `journey` page type

A journey is a curated, ordered sequence of existing pages connected by one narrative thread — the wiki-brain equivalent of a reading list with an argument, not a folder. It exists because the wiki's default navigation (domain indexes, `connections:` edges) is organized by what a page *is*, and a journey is organized by what a *reader* wants to follow — a theme that cuts across domains and person pages the way a synthesis page's `synthesizes:` does, but for guiding a reader rather than proving a claim.

**Domain is ****`meta`** — a journey is about the corpus's own navigation, not about Dan directly, which is why it does not belong in `self`, `mind`, or any domain that describes him. `wiki/meta/` also holds the on-site mirrors of `DIGEST.md`, `RECENT.md`, and `OPEN.md` for the same reason: both are the wiki describing itself rather than describing its subject.

**Mandatory ****`journey:`**** block**, in addition to every field an ordinary page carries:

journey:

stops:

- page: wiki/people/tom

note: "One sentence: why this page is a stop, in this order."

- page: wiki/mind/synthesis/supply-network

note: "..."

- page: wiki/health/cocaine

note: "..."

`bin/wiki-lint` requires at least three stops, a `note:` on every one, and that every `page:` resolves to a real wiki page — it cannot check that the notes are true, so **the connecting narrative belongs in prose on the page, not only in the frontmatter**. A journey page's body should read as an essay that walks the stops in order, quoting or citing the documentary evidence (dates, figures, direct quotes) that ties them together — "these are related" is not a journey, the same way it is not a synthesis (`SYNTHESIS_SPEC.md`). Unlike a synthesis page, a journey is not required to state a falsifiable governing rule; it is allowed to simply be a well-argued guided tour. It should still name what the stops have in common precisely enough that a reader could predict what a fourth stop would need to qualify.

**Never invent a journey as a second, weaker index.** If the connecting thread does not survive being stated as one sentence a stranger could follow, it belongs in a domain index instead. **A journey through pages the Annie moratorium covers may link to Annie's existing pages exactly as published — never add narrative, synthesis, or connective claims about her that are not already written elsewhere in the wiki**, per `CLAUDE.md`'s standing directive. Exemplar: `wiki/meta/journeys/the-supply-line.md`.

## Linking

- Wikilinks use full repo-relative paths without extension: `[[wiki/people/annie-ulmer]]`. Piped labels are fine: `[[wiki/people/annie-ulmer|Annie]]`.

- Every non-index page must be reachable from its domain index (the lint orphan check enforces this), **and must link back to it** (the lint one-way-door check enforces this). The first half stood alone until 2026-09-05 and the corpus went the way the rule was written: 453 of 497 pages never linked their own index, all 168 people pages among them. A reader arriving from search or the portal's front page landed and stopped.

- **The ****`**Up:**`**** footer is the one sanctioned footer**, it is generated by `bin/wiki-crosslink breadcrumb --apply`, and it is not hand-written. It carries the ancestor index chain, plus previous/next where the siblings are a numeric run (the twitter years). Re-run the tool rather than editing one.

- `## Related` / `## See also` footers are **banned**. If a link deserves to exist it deserves a typed edge and a claim; if it cannot earn a claim, delete it. The `**Up:**` line is not an exception to this and does not test it: it makes no claim of relatedness, it points only at the index the page already sits under, and that index already links down. A footer that names a *peer* page is the banned thing, whatever it is titled.

## Capture-note handling

Captured notes may carry `targets: [wiki/...]` (from @-mentions) — apply the note to those pages first. Square-bracket lines like `[RENAME PAGE TO x]` are **operator instructions to the ingesting model**, not content: execute them (honoring all rules above, e.g. link updates on rename), and never copy the bracket text into a page.

A capture is **testimony, not fact**. Hand-typed memories are the only place some events exist, and the dates attached to them are the least reliable part. Check every date, age and count against the corpus before writing prose; when they disagree, table the evidence and say which governs rather than silently picking one. The standing example is the brief-#4 batch, which dated the Fran sequence to 2017 against seven independent records putting it in 2018.
