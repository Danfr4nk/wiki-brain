# Factstory Brief Template — the instruction block that ships with captures

**This file is the source of truth for the INGEST BRIEF that ****`leviathan/factstory.html`**** emits with each batch of hand-typed facts and stories.** The generator in the other repository must be regenerated from this file whenever it changes; otherwise offline ingests drift away from in-repo ones, which is the exact failure the brief exists to prevent.

Everything between the rules below is what gets pasted above the payload. The payload itself (`## N. THE PAYLOAD`) is generated per batch and is not templated here.

**Revision history of the instructions themselves:**

| **Date** | **Change** |
| --- | --- |
| 2026-08-01 | STRATEGY.md's core loop, coverage rule and live-node doctrine propagated in |
| 2026-08-02 | §1 repointed to the leviathan mirror after wiki-brain went private and its Pages feed 404'd |
| 2026-08-02 | Sections 2.5, 5.2b and 6 rewritten after the brief-#4 ingest: captures are testimony to be checked, not facts to be recorded; verification is a required step, not a courtesy; a reasoned non-climb is a finished climb |

## 0. What this file is, and what you are being asked to do

You are being handed facts and stories that a person typed by hand. **They exist in no export, no message log and no archive anywhere**, because they were only ever said out loud. Everything below the payload marker is the payload; everything above it is your instructions.

Your job, end to end:

1. Read the existing wiki so you write *into* a graph rather than beside it.

1. File each capture verbatim into `raw/` so every claim has provenance.

1. **Check the capture against the corpus before you write a word of prose.**

1. Write or revise the `wiki/` pages the captures touch — as prose, not notes.

1. Wire them in with typed edges carrying argued claims, **both directions**.

1. **Write any finding back into every entry it draws from.**

1. Append to `log.md`, update indexes and `queue.md`.

1. Open a pull request against `main`.

**This is a second brain, not a note pile.** A fact filed is worth little; a connection argued is the product. If you finish and have only added text without adding a single typed edge, you have not done the job.

### The core loop you are one turn of

**Story → Entry → Analysis → Synthesized finding → saved back to every entry it touches → repeat.**

The repository calls this **amortized insight**: analysis is expensive to do well, so it is done once, saved at every point where it is relevant, and every future pass starts from a higher floor instead of re-deriving what is already known.

Two consequences bind you directly:

- **Every data point gets an entry.** Every story, friend, place, perspective, development and thought. Thinness is not a reason to withhold a page — a stub marked `status: stub` beats a fact that lives nowhere. The only boundary is **one page per entity** — grep every alias and handle first, then merge rather than fork.

- **An entry is a live node, not a record.** Each page carries what was known at ingestion *and* everything later produced by using it in analysis against the rest of the corpus. If you conclude something about a page, that conclusion belongs **on** it.

**The one thing that would make this worse than doing nothing:** inventing detail. Everything you write must trace to one of these captures, to the corpus, or to a page already in the wiki. Where you are inferring rather than recording, say so in the text. Where you do not know, write a Gaps line. An honest gap is an asset; a confident fabrication corrupts every conclusion built on it later.

## 1. Orient — read the existing wiki first (it is publicly readable)

You do **not** need repo access to read the current wiki, but note where it now lives. `caakehorn/wiki-brain` went **private on 2026-08-02**, which took its GitHub Pages feed down with it — every `caakehorn.github.io/wiki-brain/...` URL (`llms.txt`, `agent/manifest.json`, `agent/corpus.md`, `llm/index.txt`) now 404s. The public mirror is served from the leviathan site instead:

| **What** | **URL** |
| --- | --- |
| **Everything, one file** (~2.6 MB) | `https://caakehorn.github.io/leviathan/data/wiki-data.json` |
| Human-readable wiki browser | `https://caakehorn.github.io/leviathan/wiki.html` |

That single JSON is the whole corpus. Read it **selectively**, not whole:

- `wikiPages.pages[]` — one object per page (`id`, `title`, `domain`, `page_type`, `status`, `summary`, `tags`, `links`, `connections`, `sources`, `aliases`). This is the light index; read it in full. It is what tells you which pages a capture touches and what typed edges already exist.

- `wikiText[<page id>]` — the complete body prose of one page, same key. Pull **only** the handful your captures touch; all 425 bodies will exhaust your context before you write anything.

- `wikiLog.ops[]` — operation history, if you need to see what changed when.

**The mirror lags.** It is rebuilt by a scheduled job on wiki-brain commits, so it can trail `main` by up to an hour; `source_commit` in the JSON names the exact commit it was built from. If a page you are revising was touched very recently, assume you may be reading a slightly stale copy of it and say so.

Domains: `self` · `timeline` · `people` · `mind` · `work` · `interests` · `health` · `places` · `legal`

The single most authoritative page is `wiki/self/context-core.md`. Where it and anything else disagree, it wins unless the other carries a specific dated correction.

**If you have no web access:** say so plainly at the top of your output, then write only *new* pages and do not claim to revise existing ones — you cannot revise a page you have not read, and guessing at its current contents will destroy earned work.

## 2. The rules you must not break

1. **Never write an untyped link.** Every connection gets a `type` from the §4 vocabulary and a `claim` sentence. If you cannot write the claim, do not make the connection.

1. **Never state a fact without a source that exists on disk.** A dangling `sources:` entry is a lint error.

1. **One page per entity.** Before creating a `people/` page, search the manifest for the person under every name, nickname and handle in the capture. Merge, never fork.

1. **Contradictions are flagged, not overwritten.** `> **CONTRADICTION:** <what the page says> vs <what the capture says>.` Revisions get `> **REVISED [YYYY-MM-DD]:** …`. **Never delete an existing conclusion because new material disagrees with it** — the disagreement is the valuable part.

1. **Revise, never regenerate.** Pages marked `knowledge: earned` are the product of reasoning done once and are not reproducible from source material. Edit them surgically.

1. **Complete sentences.** Every page must read as prose to a stranger opening it cold. No fragment chains, no dossier shorthand, no bullet soup.

1. **Tables hold numbers, prose holds meaning.** Never restate a table in prose.

1. **Dates are absolute.** Convert "last summer" to a year and flag uncertainty as `(~2019?)`. Never leave a relative date in a page. **And see §2.5 — an absolute date in a capture is not automatically the right one.**

1. **Paraphrase into ****`wiki/`****, keep verbatim in ****`raw/`****.** Quote a sentence or less only where the exact wording is itself the evidence.

1. **No session chatter in ****`wiki/`****.** No "I have added…", no notes to the operator. That belongs in `log.md`.

1. **Never leave a finding on one page.** If a conclusion draws on three pages, all three carry it.

## 2.5 A capture is testimony, not fact *(added 2026-08-02)*

**This is the section most likely to change what you produce.** The person who typed these entries is recounting from memory, sometimes years later, sometimes about the worst nights of their life. The memories are the point — nothing else in the corpus has them. The *dates and figures attached to them are the least reliable part*, and the corpus can usually settle them.

The brief-#4 batch is the standing example. Two long, vivid, internally consistent stories dated a sequence to **March–April 2017**. Seven independent records — a GEDCOM death date, two caregivers' dated message threads, an eviction notice, two condolence messages, and the participant's own thread — dated it to **2018**. The operator was wrong by exactly one year about the death of the person he describes as his single biggest life influence. That is not unusual and it is not a criticism; it is what memory does. What matters is that the model checked.

So, before writing prose:

- **Take every date, age, duration and count in the capture as a claim to be tested.** Search the corpus for the events around it.

- **The strongest corroboration is internal to the story.** In the example above, the decisive evidence was not the death certificate — it was that the third party the story turns on has no contact with Dan in the corpus until eleven months after the story says the encounter happened. Find the row that is *inside* the narrative.

- **When the capture and the corpus disagree, both go on the page.** Table the evidence, state which governs and why, and — separately and labelled as inference — say why the memory may have slipped if you can see a mechanism.

- **When the capture is right and the corpus was vague, say so loudly.** The same batch had the operator write "died in early 2017 from a heroin overdose. Date of death should be researched" — and the corpus produced the day, the hour, four recipients, the viewing and the funeral. That is the system working.

## 3. Frontmatter — every page carries exactly this shape

---

domain: self | timeline | people | mind | work | interests | health | places | legal

page_type: entity | event | concept | period | summary | synthesis | profile | report | chat | note | index

status: active | stable | stub | closed | archived

date_created: YYYY-MM-DD

date_modified: YYYY-MM-DD

sources:              # paths under raw/ ONLY, and they must exist

- raw/<domain>/captures/<the file you created>.md

tags: [topic, topic]  # closed vocabulary — see STYLE_GUIDE.md, do not invent

connections:          # see §4 — this is the important one

- page: wiki/people/someone

type: causes

claim: "One complete sentence a stranger could evaluate and try to falsify."

---

Optional, use where they earn their place: `title:`, `aliases: []`, `importance: critical|high|normal`, `knowledge: earned|derived|mixed`.

**`status`**** means what it says.** `closed` means a thing has formally *ended*, not that the page feels finished. Default for a finished page is `stable`.

**Every ****`domain: people`**** page must also carry an ****`infobox:`**** block** with at least `name` and `relationship_to_dan`.

**`sources:`**** is for ****`raw/`**** paths. ****`synthesizes:`**** is for ****`wiki/`**** paths.**

## 4. Typed edges — the vocabulary, and the inverse rule

A connection records **how** two pages relate, not that they do.

**Directional — you must write the inverse edge on the target page:**

| **type** | **inverse** | **meaning** |
| --- | --- | --- |
| `causes` | `caused-by` | A is a documented cause or driver of B |
| `evidences` | `evidenced-by` | A is primary evidence for the claim B makes |
| `instantiates` | `instance-of` | A is a concrete case of pattern/concept B |
| `precedes` | `follows` | temporal or causal sequence |
| `supplies` | `supplied-by` | material or logistical dependency |
| `component-of` | `contains` | part / whole |

**Symmetric — same type on both pages:**

| **type** | **meaning** |
| --- | --- |
| `contradicts` | incompatible claims — **must** also carry a `> **CONTRADICTION:**` block |
| `parallels` | same structure in different domains or eras — **the highest-value type** |
| `mirrors` | inverted or complementary structure |
| `co-occurs` | documented joint presence, no causation asserted — the weakest legal type |

**Directional, no inverse required:** `escalates`, `resolves`, `contextualizes`.

- **Invent no types.** Anything outside these tables fails validation.

- **The type is the analytical commitment.** `co-occurs` where the evidence supports `causes` is a substance failure; `causes` where it only supports `co-occurs` is a provenance failure.

- **Pair your types correctly.** `instantiates` pairs with `instance-of`; `contains` pairs with `component-of`. Writing `instantiates` on one side and `contains` on the other leaves *neither* side with an inverse and the checker warns on both.

- **3–10 connections per page.** More usually means a synthesis page is missing.

- **Any ****`causes`****, ****`contradicts`****, ****`instantiates`**** or ****`parallels`**** edge must also be argued in the body prose** of at least one of the two pages.

- **A new page with no inbound ****`[[wikilink]]`**** from existing prose is an orphan.** Always add at least one prose mention on a page that already exists.

### The inverse claim has to carry the finding

When you conclude something across several pages, the claim you write back onto each of them must state **what that page turned out to be evidence of** — not that a relationship exists.

The test: a reader who lands on the member page and reads only its `connections:` block should come away with the conclusion itself.

# FAILS — names a relationship, transmits nothing

- page: wiki/mind/synthesis/some-finding

type: instantiates

claim: "This page is one of the members of the some-finding synthesis."

# PASSES — the finding itself, readable cold, at the point of arrival

- page: wiki/mind/synthesis/some-finding

type: instantiates

claim: "Seventeen years of continuous presence after the 2009 breakup is the cleanest case of a romantic role ending without the tie ending."

## 5. Procedure — do this in order

### 5.1 File every capture into `raw/` first

For each payload entry, create **one file**, verbatim, at `raw/<domain>/captures/<suggested raw filename from the entry table>`. The file is the entry's metadata header followed by its verbatim text — do not clean it up, do not paraphrase, do not correct its grammar or its dates. `raw/` is immutable source and its whole value is being untouched.

### 5.2 Decide the target pages

- If the entry declares a **target**, that page is authoritative — apply the capture there first, then propagate.

- Otherwise search for every person, place, event, employer and concept the capture names. Prefer **revising an existing page** over creating a new one.

- A single capture usually touches **three or more** pages. Ingesting it into one page and stopping is the most common failure.

### 5.2b Follow every proper noun into the corpus *(added 2026-08-02)*

Do not treat the capture as the boundary of the work. For each name, place and institution it mentions, search `raw/` before writing — including the sources nobody has re-read in months, like the genealogy export and the full message dump.

This is where the compounding actually happens, and the cost is low. In the brief-#4 batch, one throwaway clause — a hostile aside naming a grandmother — was followed into the GEDCOM's family records and produced three results no capture contained: two gaps that a page had explicitly named were closed (a maiden name, a first husband), a person with no page got one, and the repository's family tree turned out to have run the maternal line through the wrong grandparent for six weeks. None of that is in the capture. All of it was one search away.

**Also check whether the capture answers a gap somebody already wrote down.** Pages end with Gaps paragraphs naming exactly what is unknown. Grep them. When a capture closes one, mark it on the page as a closure with the date — that is the cheapest high-value edit available and it is how the wiki demonstrates it is accumulating rather than accreting.

### 5.3 Write

The first paragraph must answer the stranger's question — for a person: who is this to Dan, what is the current state, what is the defining thing; for an event: what happened and what changed. **Order by consequence, not chronology.** State load-bearing conclusions plainly. Put dates and counts in tables. End with a **Gaps** paragraph naming what is still unknown.

When you add to an existing page, integrate the material into the prose where it belongs. Do not append a dated "New information" section at the bottom — that is how pages rot into changelogs.

### 5.4 Wire it

Add the typed edges per §4, **including the inverse on every target page**, and at least one prose `[[wikilink]]` for each load-bearing edge. Bump `date_modified` on every page you touched.

Then do the step that is easy to skip: **if this ingest produced a finding spanning several pages, write that finding back into each of them** as a claim stating what that page turned out to be evidence of.

### 5.5 Log it

Append to `log.md` — newest at the bottom, never edit existing entries:

## [YYYY-MM-DD] ingest | <domain> | factstory capture — <short description>

<What came in, which pages it changed, what it settled, what it corrected, what

it opened, and what you were unsure about. This log is where uncertainty is

allowed to live — name it here rather than smoothing it into the pages.>

### 5.6 Update the indexes and the queue

If you created any page, add it to its domain index (`wiki/<domain>/index.md`) as a link plus a one-line summary. Indexes are navigation only. Record the batch in `queue.md`, including anything the corpus cannot answer and a human would have to look up elsewhere.

## 6. Climbing — and the reasoned refusal that counts as one

If these captures make you notice **the same shape across three or more pages spanning two or more domains**, and nothing in the wiki already states it, you may have a synthesis.

The test is strict: *can you write one sentence that is true of every member, is ****not**** true of the corpus generally, and that a stranger could try to falsify?* A page whose thesis is "these things are related" is worse than no page.

If you can, it carries: `page_type: synthesis`, `knowledge: earned`, a `synthesizes:` list naming every member, the thesis in the first two sentences, a table of members against the rule, the counterexample or control that makes it a claim rather than a mood, **at least one falsifiable prediction**, and a Gaps section. Each member gets an `instantiates` edge carrying the finding back.

**But an unclimbed cluster, written down properly, is a completed piece of work — not a failure** *(2026-08-02)*. Do not climb onto pages you created in the same pass: a synthesis resting on a concept page written that afternoon is the write-only anti-pattern with extra steps, and CLAUDE.md's rule is to climb after a cluster has survived two or more ingests. When you find a real cluster you should not yet climb, register it in `synthesis-queue.md` with three things:

1. the member pages and their domains,

1. the candidate sentence, stated so the next model can attack it, and

1. **the specific, cheap piece of work that would earn the climb** — the audit, the count, the falsifier to go looking for.

That entry is worth more than a thin synthesis page, and the next pass starts from it. Do not climb to raise a number. Three thin pages stacked make one thin page.

## 7. Output format

Think out loud first if it helps — everything outside these blocks is ignored. Then emit **complete files, never diffs**:

===FILE: wiki/people/example.md===

<the entire new content of the file, frontmatter included>

===END===

===FILE: raw/self/captures/2026-01-01_120000_example.md===

<the verbatim capture>

===END===

===LOG: ingest | <domain> | factstory capture — <one line>===

===COMMIT: ingest: <short description>===

Any number of `FILE` blocks; exactly one `LOG` and one `COMMIT`. For a page you are *revising*, the `FILE` block must contain the **whole page**. If you cannot reproduce a page in full because you could not read it, do not emit a `FILE` block for it — describe the change you wanted and let a human apply it.

If the repository is checked out locally, `bin/ingest-apply <your-response>.md` validates and applies this format directly.

## 8. Getting it into a pull request

Use the first route available to you.

**Route A — a terminal with the repo cloned**

git clone https://github.com/caakehorn/wiki-brain && cd wiki-brain

git checkout -b factstory/<YYYY-MM-DD>-manual-captures

# save the model response to response.md, then:

bin/ingest-apply response.md

bin/wiki-lint && bin/wiki-connect check && bin/wiki-climb check   # all must be 0 errors

git add -A && git commit -m "ingest: factstory manual captures"

git push -u origin HEAD

**Route B — browser only, no terminal.** Open the repo, press `.` for the browser editor, create each file at its path, and on the **first** file choose "Create a new branch for this commit and start a pull request," naming the branch `factstory/<YYYY-MM-DD>-manual-captures`. Commit every subsequent file to that same branch. Append the `LOG` entry to the bottom of `log.md`. Open the PR, titled with the `COMMIT` line.

**Do not commit to ****`main`**** directly.** The point of the branch is that a human reads the diff before it becomes truth.

## 9. Pre-flight checklist

Three validators (`bin/wiki-lint`, `bin/wiki-connect check`, `bin/wiki-climb check`) must report **0 errors**. If you cannot run them, check by hand:

- Every `sources:` path exists — i.e. you emitted a `FILE` block creating it.

- No `wiki/` path in `sources:`; no `raw/` path in `synthesizes:`.

- Every `connections:` entry has a `page`, a `type` from §4, and a `claim` that is a complete sentence of at least 25 characters.

- Every directional edge has its **correctly paired** inverse on the target.

- Every inverse claim carrying a finding **states the finding**.

- **Every date in every capture was checked against the corpus** (§2.5), and any disagreement is tabled on the page rather than silently resolved.

- **Every proper noun in every capture was searched for in ****`raw/`** (§5.2b).

- Any page Gaps paragraph this batch answers is marked closed, with a date.

- Every `[[wikilink]]` points at a page that exists or that you are creating.

- Every new page has at least one inbound `[[wikilink]]` from existing prose.

- Every page you touched has `date_modified` bumped to today.

- `page_type`, `status`, `domain` and every `tag` are values from the controlled vocabularies, spelled exactly.

- Every `domain: people` page carries an `infobox:` block.

- No relative dates and no agent chatter anywhere in `wiki/`.

- `log.md` appended, not edited; `queue.md` updated.

Then, in the PR body, state plainly: what you added, what you **corrected**, what you inferred rather than recorded, what you could not verify, and anything you decided **not** to do. That last one matters most — the operator needs to know where you stopped.
