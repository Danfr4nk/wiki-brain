# CROSSLINK_CAMPAIGN.md — running the whole wiki through the source-mention pass

The CROSSLINK operation (`CLAUDE.md`) was written on 2026-09-04 against one corpus and nineteen pages. This file is the plan for running it across the **whole** repository, and it exists because that is not one session's work and must survive being handed between models.

**Read ****`CLAUDE.md`****'s CROSSLINK operation first.** This file is sequencing and tooling; that one is the method, and nothing here overrides it.

## The situation, measured 2026-09-04

|  |  |
| --- | --- |
| wiki pages | **497** |
| typed edges | 2,666 |
| pages with **zero** typed edges | **106** (38 people, 29 interests, 18 self) |
| one-way edges owing an inverse | **77** |
| pages stating a **checkable limit about themselves** | **157** |
| substantial `raw/` corpora cited by pages | **8** |
| corpora `bin/wiki-crosslink` can read | ~~1~~ **3** (2026-09-04, Phase 2 #1) |
| pages that cite the twitter archive | **42** |
| pages the twitter archive **actually names** (`coverage`) | **20** |
| pages **any** readable corpus names, after the message reader | **100** |
| pages nothing names that **cite a corpus anyway** | **74** (plus 79 synthesis/concept, which nothing can name) |
| pages carrying no `aliases:` at all — the index's blind spot | **389** |
| pages with no unambiguous name at all (bare first names) | **99** (44 people) |
| cost of a scan / of `coverage` over the whole wiki | ~1.5s per page / **3.2s**, all three corpora |

**Rows three to five are the whole problem.** Scanning is free — the entire wiki triages in about three seconds against a quarter of a million source rows. Reading is not. And until Phase 0 the tool pointed the reading in the wrong direction, while the index could not see 389 of the pages it was supposed to be finding.

## Four findings from Phase 0, two of which corrected this file's own estimates

### 1. `scan` read only corpora a page already cites, which was backwards — fixed

`scan_page` took the page's own `sources:` and kept the ones it had a reader for, so a page was checked against the corpora it was **already built from**. Every finding in the pilot came from the opposite move.

`scan --against <corpus>` now exists. But the first run of it returned *the same candidate list for every page*, because a date range is not a scope: a person's page spanning 2009–2025 matches every entity in seventeen years. Against mode now first finds the rows that **name the page itself**, and looks only inside those — "in what this corpus says about X, what else does it name?", which is the question the obligation is actually about.

A page whose names never appear returns *"the corpus is silent on it"* in milliseconds. That is a real negative and it is most of the answers.

### 2. The value is concentrated and the concentration is measurable

157 pages make a checkable claim about their own limits — "the complete record", "everything known arrives through", "no ledger entries at all and remains description". Every pilot finding landed on such a page, and four falsified the claim outright.

`scan` now ranks candidates by the **target's** self-limit score, and `--queue` orders the whole wiki by it. Before this, scanning the concert record put Katie Fletcher (7 self-limit claims) below 82 SLOPPP mentions.

### 3. **Correction — "184 pages unlocked" was wrong. It is 20.**

This file first estimated the `--against` unlock at 184 pages, from date-range overlap with the twitter archive. Overlap is not mention. Running `coverage` across all 497 pages: **20 are actually named by the archive**, eight of which do not cite it. The rest overlap in time and the corpus says nothing about them.

**The twitter archive is close to exhausted**, which the pilot's yield already hinted at. That is good news for sequencing — it means the corpus is done, not that the campaign is small — but this file said otherwise and the number was never checked before it was written down.

### 4. **The real bottleneck is ****`aliases:`****, and it is missing on 389 pages**

Matching is exact-phrase on a page's title, and a title is almost never how a thing is written in a source.

`wiki/interests/opie-and-anthony` is the worked case. The archive names it **61 times** — `o&a` 8, `opie` 25, `cumia` 10, `@OpieRadio` 18 — and the exact string *"opie and anthony"* appears **zero** times. `coverage` therefore reports the corpus silent on it, which is a false negative produced entirely by missing frontmatter.

**395 of 497 pages carry no aliases at all.** Every corpus reader built from here on inherits this blindness, so populating `aliases:` is worth more than any further work on the matcher, and it must come before the readers rather than after. `bin/wiki-crosslink entities --missing` is the list, ranked so that multi-word titles — the ones sources abbreviate — come first.

### The false-positive rate, unchanged and still the reason to triage

Of roughly 240 pilot candidates, about 29 were high-confidence and ~20 actionable — **under 10%**. Single-token names ("Rick" → Rick Santorum, "Tom" → Tom Cruise, "slim" → slim jims) were near-100% noise. High confidence is now the default and `--low` opts in.

## Phase 0 — the instrument — **DONE 2026-09-04**

- `scan --against <corpus>`, scoped by the page's own names rather than by its date range. The date-range requirement was dropped once the name filter made it redundant; it was blocking 246 pages for nothing.

- High confidence by default, `--low` to opt in.

- Candidates ranked by the target's self-limit score; `--queue` orders the wiki.

- `coverage` — which readable corpora actually name a page. The triage step: run it before scanning, because most page/corpus pairs are silent.

- `entities --missing` — the 389-page alias gap.

- **The moratorium is a refusal, not a warning**, and deliberately narrower than `bin/wiki-plain`'s: scoped to her own pages by title and alias, because porting that tool's body-mention threshold across would refuse 197 of 497 pages — `interests/golf`, `self/tattoos`, `music/aliases/sloppp` — for no safety gained. The rest of the directive constrains what a session *writes*, and `scan` prints that reminder on any page naming her.

- **A parsing bug fixed that predated all of this.** `aliases: ["Lex", "@alexisarmel"]` kept the quotes on every entry after the first, so every quoted `@handle` was silently demoted to a low-confidence single token. It cost 83 of 84 matching rows on one page.

**Two items deferred with reasons, not dropped.** `crosslink report` (a derived campaign page) and `crosslink audit` (the fabrication referee — every dated quote in a claim must appear verbatim in the corpus it cites) are both still right. Neither is the blocker: the audit matters once there is volume to police, and there is not yet; and a campaign page that reports on a campaign which cannot see 389 of its own pages would mostly report the blindness. **Aliases first.**

## Phase 2 reader #1 — the message corpus — **DONE 2026-09-04**

**Out of order on purpose, and the ordering this file gave was wrong.** Phase 0.5 was placed before the readers on the argument that a reader inherits the index's blindness. True, and incomplete: the alias test is *"what does the record actually call it"*, and until a corpus is readable there is no record to put the question to. The dependency runs both ways, and the message reader was the cheap side of it — because **it already existed**.

`bin/mine-messages` carries the reader for `raw/self/dox-scan/all_imessages_complete_dump.txt` along with the three traps that make naive reading of that file wrong: multi-line records reassembled, curly quotes folded (they outnumber straight ones 28,904 to 19,978 in his sent text), and direction trustworthy. `bin/wiki-crosslink` now **imports** it rather than reimplementing it, which is the only way to inherit the traps rather than the interface. Phase 2's own warning — *"a reader written without them produces confident wrong candidates"* — is answered by not writing one.

### Correction: the two message exports are not two forms of one corpus

This file said *"two forms of one corpus, so dedupe or double-count"*. Dedupe is required and the rest is wrong. Measured on (timestamp, first 120 normalised characters):

|  | **rows** |
| --- | --- |
| `dox-scan/all_imessages_complete_dump.txt`, unique | 215,057 |
| `message-csv/MASTER_MESSAGES_DB_DUMP.csv`, unique | 174,775 |
| in both | 124,379 |
| **only in the CSV** | **50,396** |
| **only in dox-scan** | **90,678** |

Neither subsumes the other. Reading only the dump loses 50,396 rows, and with them **all of 2026** — the CSV is the only message corpus that reaches this year (9,896 rows) and it holds 41,278 for 2025 against the dump's 27,850. Both are declared readable, they share a `family`, and rows are deduped across them whenever both are in play.

### Correction: `bin/mine-messages`' own docstring is out of date on the CSV

That file says the CSV *"marks nearly everything **`Received`**"*, and directs any claim about what Dan said to the dump instead. As the file stands today it splits **88,988 Sent / 86,370 Received**. The real limitation is a different one and it survives: **69,869 of those Sent rows carry no ****`contact_handle`**** at all**, so the CSV can say what he wrote and, four times in five, not to whom. Sound for a corpus-wide claim, unsound for a per-relationship one. The docstring has been corrected; the trap is now recorded where the reader is.

### The matcher had to be rebuilt to survive the corpus

One `re.search` per row against the high-confidence band — a 19,418-character alternation — took **50.1s** over the 217,573-record dump, and `coverage` would have run it once per page. An inverted token index over the same rows finds the same 862 in **0.6s**. The index only decides which names to *test*; every surviving candidate is confirmed with a real word-boundary regex, so nothing is matched that the alternation would not have matched. `coverage` over all 497 pages against all three corpora is **3.2s**.

### Two defects the new corpora exposed, both older than the corpora

1. **The moratorium was enforced on the scan's subject and not on its candidates.** A scan of `interests/concert-record/index` offered her page as a target with 101 mentions. A candidate list is a worklist whichever column her name lands in. Now withheld in `render_hits`, counted rather than silently dropped, and pinned by `tests/test_wiki_crosslink.py` — which is also the first test this tool has had, against `bin/wiki-plain`'s guard having been pinned since it shipped.

1. **A string two pages both claim was reported as evidence for both.** `@alexisarmel` is in one person's `aliases:` and in another's infobox `handles:`, so 85 rows about the first were rendered as 101 mentions of the second. The index always knew there were two owners; the renderer did not say. Candidates are now marked `contested` with the competing name.

## Phase 3, first page — `wiki/people/alexis-armel` — **DONE 2026-09-04**

The instrument is not the deliverable. One page, worked fully, the way INGEST works.

**What the pass found, and why the page could not have found it alone.** The page cites `FULL TWITTER ANALYSIS.txt`, an AI reading of the corpus, and had never had the primary archive in `sources:`. The archive holds 85 rows naming her. The derived file was not wrong about any of them — it had never been asked the question that needs a denominator. Her share of his @-tweets: **37.6% in 2010, 24.2% in 2013, 3.1% in 2014, 0% in 2015.** The public record of the six-year relationship ends **twenty-four months before the relationship does**, and four confounds die on the archive's own numbers, the sharpest being that 2014's **57 distinct @-handles is an all-time high**.

**This is what a self-limit claim is worth.** The page's Gaps section said the occupancy-without-activation claim "rests more on absence than on a positive measurement," and named coverage as the alternative it could not rule out. The measurement it wanted is a denominator, and a broadcast archive is the one corpus that has one. `--queue`'s ranking put this page where it was for exactly that reason.

**Written back:** `wiki/self/twitter/2014` (a correction — *"Alexis is still here"* was two tweets read without their denominator), `wiki/mind/concepts/the-cool-metric` (a new section: "splitting via irony" run on somebody already inside the filter), `wiki/mind/synthesis/the-unbroken-bond` (its first contemporaneous non-testimonial evidence), plus the `plain/` twin and ten stale-premise re-checks. Reciprocal debt on the tree touched: **0**.

### The cost nobody had measured: a re-check is as expensive downstream as a claim

Editing two hub pages made ten dependents stale. Working all ten honestly bumped nine `date_modified`s, which made nine of *their* dependents stale. Gate run against `main`, stashed and unstashed: **44 stale pages before, 44 after.** Nine cleared, nine created, **net zero** — the front moved one layer out.

That is the mechanism behind 104 stale premises surviving three handoffs untouched, and it changes how the campaign should be sequenced: **a crosslink pass that touches a hub page owes its whole first layer**, and the standing queue is drainable only breadth-first, in a pass that writes no new content. Filed to `skills/INBOX.md` with the measurement that would size the bigger prize — how much of that queue is the gate reporting its own bookkeeping — and with the reason it could not be run here (a shallow clone).

## Phase 2 reader #1, part two — the mode the corpus actually needed

**`--against`**** is the wrong question for a message corpus, and the queue proved it: 0 candidates across 7 pages.** That mode reads the rows naming a page and asks what else they name. A tweet is a self-contained utterance that often names several handles. A message averages five to fifteen words, and one that names somebody almost never names a second — so the mode returns nothing, and returning nothing looks exactly like a corpus with nothing to say.

**A message corpus knows something no broadcast archive does: who the counterparty is.** `scan --conversation` joins a page's infobox `handles:` to the corpus's own handle field and reads the whole conversation with that person. Measured: **30 people pages resolve, reaching 41,349 rows**, and the sweep returns **51 candidates** where `--against` returned 0.

`handles [prefix]` is the coverage view and the message corpus's own version of `entities --missing`:

|  |  |
| --- | --- |
| people pages whose handle resolves into a message corpus | **30** (41,349 rows) |
| pages declaring a handle the corpus does not have | 7 |
| **people pages carrying no ****`handles:`**** at all** | **138** |
| masked handles (`+1724***7658`) that resolved uniquely | **all of them** |
| handles claimed by two different pages | 1 — `+17249123381`, `people/zaco` and `people/zach-hendricks` |

Masking turned out not to be an obstacle: a ten-digit space with three unknowns and a known area code is unambiguous inside 504 contacts. A mask that matched two would be reported, not guessed at; none did.

### The "uncatchable" failure mode has a catchable class, and it was live

The honest-limit section below says crosslinking has no cheap unattended lane because its judgment failure produces plausible correctly-cited prose that no arithmetic detects. That stands. **But one class of it is arithmetic, and it was running at HIGH confidence:**

| **Name** | **Rows in the message dump** | **How many are the thing** |
| --- | --- | --- |
| `say anything` — a band with a page | **134** | **0** |
| `the office` — a show with a page | **77** | **0** (all a real estate office) |

Confidence is *"more than one token = high"*, on the reasoning that a bare first name matches anybody and a full name does not. A two-token name that is also ordinary English breaks that rule in the direction that matters, because the tool tells you to trust the match — and `coverage` was presenting the first of these as the wiki's top music result.

Such names are now **flagged, not demoted**, with the count marked as not-evidence: demoting hides the candidate behind `--low`, and some of them really are the band (Fall Out Boy is discussed by name in the Ally conversation). The word list is the corpus's own top 1,000 tokens rather than a hand-kept list, so it tracks how the record is actually written. It over-flags on purpose — `annie ulmer` trips it, because a surname belonging to the most-messaged person in the corpus is genuinely frequent in it. Dispersion was tried as a fix and abandoned: 504 handles, most of them a handful of messages, so even `say` reaches only 14.7% of conversations and nothing separates.

## Phase 0.5, rescoped and half-done — **2026-09-04**

Two measurements changed what this phase is.

### It is 281 pages, not 389

389 pages carry no `aliases:`, and that number was the estimate. But **concept and synthesis page names are wiki coinages a corpus cannot contain** — "the input clamp", "rooting for the fire" — so an alias on one of those is navigation, not a corpus name, and no amount of writing them will make a scan find anything. Excluding the page types no source could ever name:

| **page type** | **no aliases** | **has aliases** |
| --- | --- | --- |
| **entity** | **208** | 36 |
| period | 32 | 0 |
| event | 27 | 10 |
| summary | 20 | 1 |
| report | 14 | 1 |
| *concept* | *18* | *20* |
| *synthesis* | *40* | *21* |
| *(index, journey, chat, note)* | *27* | *3* |

**281 pages a corpus could plausibly name, 208 of them entity pages.** That is where the phase's value is, and it is where the second half lives too.

### The other half is `handles:`, and it buys more per entry

An alias buys a name match. A **handle** buys the entire conversation with that person — `scan --conversation`, above. `bin/wiki-crosslink handles` is the coverage view:

|  |  |
| --- | --- |
| people pages whose handle resolves into a message corpus | **30** (41,349 rows) |
| pages declaring a handle the corpus does not have | 7 |
| **people pages carrying no ****`handles:`**** at all** | **138** |

### And the aliases that already exist needed grading, not counting

`entities --audit`. Of 326 declared aliases, **233 appear zero times in any readable corpus** — and reporting that as a defect would be the mistake, for the same reason as above: they are coinages doing the navigation job, they match nothing, and they cost nothing.

**Six were doing neither job, and four are now deleted.**

| **Alias** | **Page** | **Rows matched** | **How many were the subject** |
| --- | --- | --- | --- |
| `the case` | `ally-and-dan-love-as-destiny` | 96 | **0** |
| `the drive` | `acquisition-drive` | 48 | **0** |
| `the Dude` | `people/james-dee` | 18 | **0** |
| `this person` | `people/the-unnamed-man` | 20 | **0** |
| `Anne Ulmer` | `people/annie-ulmer` | 415 | correct — her name |
| `Google AI` | `self/concepts/gemini` | 4 | **correct** — how he writes about it |

Every one of the four was reported at **high** confidence, because the confidence rule is "more than one token". **A wrong alias is worse than a missing one**: a missing alias makes the index blind, an ordinary-English alias makes it confidently wrong. The two survivors were kept by *reading the rows*, which is why the audit flags rather than deletes.

## Phase 0.5 — populate `aliases:` — **the remaining work**

389 pages, none of which the index can find under any name but their exact title. This is the cheapest work in the campaign and it gates everything after it. Worked by `entities --missing`, multi-word titles first, and it is ordinary page editing rather than a new operation.

The test for an alias is not "what could this be called" but **"what does the record actually call it"** — `o&a` and `@OpieRadio` are aliases because they appear in the corpus; "the Opie and Anthony Show" is not, because nothing writes that.

## The self-limit check that came out of Phase 3 — **`counts`****, 2026-09-04**

A page's stated `| Messages |` figure against the corpus its handle resolves into. **The defect had been found by hand four times and never by a tool** — `bruce-burish` and `zach-clingan` carry corrections saying the stated number "is exactly the received count", and `rod-banks` and `zach-hendricks` made it four.

`bin/wiki-crosslink counts` found **thirteen more**, nine understating by exactly the Received-only figure. `wiki/people/vaughn`: **228 stated, 582 actual, 354 of Dan's own messages uncounted** — on a page that said they "survive nowhere in it". All thirteen are corrected; none has had its prose re-derived, and each says so.

**The generalisable shape**: a page that explains an absence in its evidence ("export artifact", "his side only") is making a checkable claim about a corpus, and the explanation is more often the artefact than the absence is.

## Phase 1 — drain the 77 one-way edges

No searching required to find them; `bin/wiki-crosslink reciprocal` prints the list. Each still needs reading to write a claim that carries the finding rather than pointing at it. This is the cheapest real value in the repository and it is already computed.

## Phase 2 — corpus readers, in citation order (after 0.5, not before)

Each reader inherits its corpus's known traps. **A reader written without them produces confident wrong candidates**, which is worse than no reader.

| **Order** | **Corpus** | **Pages citing** | **The traps it must carry** |
| --- | --- | --- | --- |
| ~~1~~ **done** | `message-csv/MASTER_MESSAGES_DB_DUMP.csv` + `dox-scan/all_imessages_complete_dump.txt` | **106 + 95** | the three properties in `bin/mine-messages`' docstring, inherited by importing its reader; **two partly-overlapping corpora, not two forms of one** — deduped by `family` |
| 2 | `concerts/table.csv` | 48 | already joined once by hand; rows 6/16/17/24 still open |
| 3 | `favorites/FAVS MASTERLIST.csv` | 40 | 43 artist pages downstream |
| 4 | `gemini-activity/Gemini Activity.html` | 28 | 21.8 MB of HTML; T2 source, `skills/corpus/source-chain.md` governs |
| 5 | `facebook/facebook-ihatedanfrank/` | 20 | a directory of HTML, not a file |

**The message dump is first by a distance** — 199 page-citations, and `wiki/interests/music/overview` carries absence claims derived from it that have never been checked either way.

## Phase 3 — the passes, worked by value

1. The **157 self-limiting pages**, densest first (13 hit three or more categories; `wiki/timeline/master-timeline` hits five).

1. The **106 zero-edge pages** — 38 of them people. These are not islands because nothing connects to them; they are islands because nobody ran this.

1. Everything else, opportunistically, when a session is in the neighbourhood.

**Never as a sweep.** One page per pass, fully, exactly as INGEST works.

## The honest limit: this cannot be handed to a cheap unattended agent

`plain/` has a free lane because `bin/wiki-plain audit` is arithmetic — a number in the twin that appears nowhere in the page is a fabrication, and a grade level is a measurement. The tool has the last word and the model cannot argue with it.

**Crosslinking does not decompose that way.** Its two failure modes are:

- **Fabrication** — a quote or date that is not in the corpus. *Mechanically catchable*, and Phase 0.5 above is the check.

- **Judgment** — writing an edge from a false-positive match, or promoting a mention to a relationship. A tweet naming Diplo is a music-consumption datapoint, not a Diplo relationship. This failure produces **plausible, well-formed, correctly-cited prose**, and no arithmetic over two files detects it.

The second is the whole job. So the referee bounds the damage; it cannot replace the reader, and this campaign has no free lane. Anyone proposing one should be asked what would catch a confidently-written edge about the wrong Rick.

## What this costs, plainly

The pilot was 19 pages against 1 corpus: ~35 edges, 6 real findings, four falsified self-claims, one long session.

Revised after Phase 0, and the shape changed more than the total:

|  |  |
| --- | --- |
| Phase 0.5, aliases on 389 pages | 3–5 sessions — mechanical, batchable, gates everything |
| Phase 1, the 77 one-way edges | 2–3 sessions |
| Phase 2, four corpus readers | 1 session each, plus the message dump's traps |
| Phase 3, the passes | the long tail |

**Still fifteen to twenty-five sessions**, but the front of it is now cheap mechanical work rather than reading, which was not true when this file was first written. Worth saying up front so a session producing four edges and one finding is understood as on pace rather than as a bad day.

**And the twitter corpus is nearly done** — 20 pages named, most already worked. A session looking for volume should go to Phase 0.5, not back to the archive.

## Logging

`connect | <domain> | <source> → <N pages>` per `CLAUDE.md`. The campaign page is derived from those commits, which is why the prefix is load-bearing here and not merely a convention.
