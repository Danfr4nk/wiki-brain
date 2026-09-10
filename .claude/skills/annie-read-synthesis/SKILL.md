## name: annie-read-synthesis description: RETIRED 2026-08-23 under the Annie moratorium in CLAUDE.md. Do not invoke. Kept only as a record of how the spread used to work.

# Annie Read — Synthesis & Spread  ·  RETIRED

**DO NOT RUN THIS SKILL.** Retired 2026-08-23 by operator directive — see `CLAUDE.md` § "STANDING DIRECTIVE — the Annie moratorium". Its entire purpose is to take a new Annie read batch and push it across the wiki, which is the precise thing now forbidden. There are no read batches any more. Nothing below is an instruction; it is kept so a future session can see what was stopped and why, rather than rebuilding it from scratch under a new name.

Step 1 (`forensic-message-analysis`) reads a window and writes two pages. This skill is step 2: it takes what those two pages now say and makes the rest of the wiki carry it.

A read batch that stays on `annie-record.md` has been discovered once. This skill is how it gets discovered permanently.

## 0. Non-negotiables — read before anything

**Repository.** All work happens in `~/wiki-brain`. Pages are `wiki/**.md`.

**Never touch ****`caakehorn/home`****.** Its `public/wiki/**` is a build artifact regenerated from `wiki-brain` hourly; anything written there is deleted within the hour, *including changes that merged*. If you are editing a page as JSON, you are in the wrong repository — stop and re-orient.

**Never modify ****`raw/`****.** It is the immutable source archive. No renames, no `.bak` files, no deletions. If a file is in your way, work around it.

**Never ****`git add -A`****.** Stage the exact files you changed, by path.

**Never work on ****`main`****.** Branch first (§1).

**Do not read messages in this skill.** You are reasoning from `wiki/`, not from `raw/`. If you find yourself opening a CSV, you have drifted into step 1. The one exception is §4.4 (verifying a new number), which requires `bin/annie-corpus` and says so explicitly.

**Do not ask the operator which findings to apply.** Apply everything that passes §3. Bring back only the items §3 sends to HOLD.

## 1. Setup — exact commands, no searching

Do not run `find` over the home directory. The paths are known.

cd ~/wiki-brain

git checkout main && git pull origin main

git checkout -b annie-synthesis-<window>   # e.g. annie-synthesis-2015-12

ls wiki/timeline/annie-record.md wiki/timeline/annie-read-notes.md

If either file is missing or does not contain the window you are synthesizing, **stop and report**. Do not reconstruct it from `caakehorn/home`.

Read in full, in this order:

1. `wiki/timeline/annie-record.md` — the events

1. `wiki/timeline/annie-read-notes.md` — ledger, open leads, motifs, corrections queue

1. `CONNECTIONS_SPEC.md` and `SYNTHESIS_SPEC.md` — you will be held to both

## 2. Build the evidence table — before you write anything

This is the gate that everything else passes through. Produce it first, as a file, and keep it open.

For every candidate finding in the batch, one row:

| **#** | **Claim (one sentence)** | **Verbatim quote that establishes it** | **Date + time** | **Speaker** | **Target page(s)** |
| --- | --- | --- | --- | --- | --- |

**The quote must be copy-pasted from ****`annie-record.md`****, not remembered.** Open the page, find the line, paste it. If you are typing a quote from memory you are fabricating it.

### Cite-or-cut

A row with no verbatim quote does not become a wiki edit. It becomes either:

- an **open lead** in `annie-read-notes.md`, or

- nothing.

There is no third option. "The read shows…" is not evidence; the quote is.

### The four disqualifiers

Cut any row where:

1. **The quote does not contain the claim.** If the claim is "Suz supplied the cocaine" and the quote is Dan saying *"It was my money"*, the row is cut.

1. **The claim names someone the quote does not name.** An unnamed person in the record stays unnamed. Identity is established by two independent references, not by one plausible match.

1. **The date cited is outside the corpus.** The corpus opens **2015-11-28**. Any cross-reference to an earlier date is fabricated unless it cites a `raw/` file.

1. **Two people share a first name.** Check the entity ledger before attributing anything to a bare first name.

### Already known wrong — do not reintroduce

These were asserted in earlier passes and are false on the record's own text:

- **"turd boy" is not established as Emilio.** On 2015-11-29 the man is unnamed; Emilio first appears 2015-12-02. This remains an **open lead**, and closing it by inference corrupts `bond-switch-2015`.

- **The Dec 29 $200 is Dan's own money.** Annie: *"that $200 wasn't even your own"*; Dan: *"It was my money."* It is not a Suz supply event. (The ~$120 from Suz on Dec 31 is separate and is real.)

- **The Dec 9 "I have to talk to you" texts are Zach Clingan, not Zachariah Harshman.** Two different people.

- **`zgurd`**** is not whiskey.** It is bought from Suz in quantity and is the subject of the "stay away from coca" plan. If you cannot establish what a slang term means, put it in the ledger as unresolved — do not gloss it.

## 3. Disposition — every surviving row goes to exactly one place

Decide per row. Write the disposition into the table.

**EDGE** — the finding changes how two existing pages relate, but adds no new prose. → §4.1

**SECTION** — the finding is a story an existing page should tell and currently doesn't. → §4.2

**GROUND** — the finding is about an entity/event/place with no page. → §4.3

**CLIMB** — the same shape now appears on 3+ ground pages. → §4.4

**HOLD** — real, quotable, but its meaning depends on something you cannot settle. Write it to `annie-read-notes.md` open leads and report it to the operator at the end. Do not guess to clear a HOLD.

Two rules on this step:

- A finding that only restates what a page already says is **not** a finding. Drop it.

- If a cluster resists synthesis, **say so in ****`synthesis-queue.md`**** with a line of reasoning.** A cluster that won't climb is knowledge. Never write a page whose thesis is "these things are related."

## 4. Apply

### 4.1 EDGE — typed connections

Edges go in frontmatter, both directions. Vocabulary is closed (`CONNECTIONS_SPEC.md`) — invent nothing.

Directional pairs: `causes`/`caused-by`, `evidences`/`evidenced-by`, `instantiates`/`instance-of`, `precedes`/`follows`, `supplies`/`supplied-by`, `component-of`/`contains`. Symmetric: `contradicts`, `parallels`, `mirrors`, `co-occurs`. No inverse needed: `escalates`, `resolves`, `contextualizes`.

connections:

- page: wiki/timeline/annie-record

type: evidenced-by

claim: "Suz arrives at 5 AM on 2015-11-30 with a line of cocaine and an offer of a car conditional on evicting Alexis — the family did not merely approve the switch, it brokered it and paid."

**The claim must transmit the finding, not point at it.** Test: a reader who lands on this page and reads only the `connections:` block should come away with the conclusion.

# fails — names a relationship, transmits nothing

claim: "This page relates to the 2015 Annie read."

# passes — readable cold

claim: "Dan names procurement as the reason Alexis cannot leave (2015-11-29, 'she doesn't have another drug source'), which is the earliest instance in the corpus of the supply mechanism, applied to the departing partner."

Choosing `co-occurs` where the evidence supports `causes` is a substance failure; choosing `causes` where it only supports `co-occurs` is a provenance failure. **The type is the analytical commitment.**

Any `causes`, `contradicts`, `instantiates` or `parallels` edge must **also** be argued in body prose on at least one of the two pages, with the wikilink inside the argument — not in a list. `## Related` / `## See also` footers are banned.

### 4.2 SECTION — sub-headers on existing pages

This is the "double-click" work: a thread from the read that an existing page should now tell properly.

- **Integrate where it belongs in the existing argument.** Do not append a dated "new information" section at the bottom — that is how pages rot into changelogs.

- **Order by consequence, not chronology.** If the Dec 2 family confrontation is the defining event of Annie's first month, it goes near the top of the relevant section, not in row 14 of a table.

- **Write long.** The standing directive is longer, denser, more exhaustive. No page has yet been too long. The 40 KB lint warning is advisory and means "check navigation," never "shorten."

- Every quoted line keeps its **date and time**. Header time and body quotes must agree — if the header says `~13:05` and the quotes are 17:53, the header is wrong.

- Corrections to existing claims use a flagged block, never a silent edit:

> **CORRECTED [2026-08-17]:** This page previously placed "YOU ARE MY

> EVERYTHING" on "day two/three." The read dates it to 2015-11-29 03:24 —

> hours after the first in-person meeting, in the same overnight burst.

Bump `date_modified` on every page you touch.

### 4.3 GROUND — new pages

**Before creating a people page, grep for the person under every known name, alias and handle.** One page per entity. Merge, never fork.

Required frontmatter, in this order — a page without it is a **hard ****`bin/wiki-lint`**** error**:

---

domain: people

page_type: entity

status: stub

date_created: 2026-08-17

date_modified: 2026-08-17

sources:

- exports/annie-corpus.csv

tags: [relationships, family]

connections:

- page: wiki/timeline/annie-record

type: evidenced-by

claim: "<the finding, stated>"

infobox:

name: Ellen Ulmer

relationship_to_dan: "Annie's mother"

known_for: "<one line>"

---

# Ellen Ulmer

`domain: people` pages **must** carry `infobox:` with at least `name` and `relationship_to_dan` or lint errors. `tags` come from the closed set in `STYLE_GUIDE.md` — do not invent one.

First paragraph answers the stranger's question: who is this to Dan, what is the state of it, what one thing defines it. **Corpus statistics come last.**

A `status: stub` a later pass deepens beats a fact that lives nowhere.

### 4.4 CLIMB — new synthesis pages

Only when the same shape appears on **3+ ground pages**. Do not climb to raise a number: three thin pages stacked make one thin page.

page_type: synthesis

knowledge: earned

synthesizes:

- wiki/people/annie-ulmer

- wiki/people/suzanne-frank

- wiki/timeline/annie-record

`sources:` is `raw/` paths only. `synthesizes:` is `wiki/` paths only. Crossing them is a `bin/wiki-climb check` error.

Requirements: thesis in the first two sentences, the controls that carry it, **at least one prediction**, and a Gaps section.

**Any new number must be verified against raw** — reasoning from pages does not license inventing figures. Use `bin/annie-corpus` and cite the file in `sources:`.

**Then wire it both ways.** Every page in `synthesizes:` gets an `instantiates` edge back, whose claim states what that page turned out to be evidence *of* — plus a prose sentence wherever the finding is load-bearing for that member. A synthesis whose members don't carry it back is half-built, and is the most common way good synthesis work fails to compound.

### 4.5 Where the work plan goes

A document about *what should be done* — "what gets linked, what needs a new page" — is **not** a wiki page. `wiki/` is accumulated understanding about Dan; a plan filed there gets indexed, mapped, word-counted and rendered as if it were biography.

Plans go in `synthesis-queue.md` or `BACKLOG.md`. Both already exist.

## 5. Update the two read pages

The batch's own pages move too:

- **`annie-read-notes.md`** — mark each applied correction `applied` with the date. Add every HOLD as an open lead. Add any slang term you could not resolve to the ledger as unresolved.

- **`annie-record.md`** — add the `[[wiki/…]]` cross-links the new edges imply. The record is described in its own frontmatter as *"the evidentiary floor the Annie page's claims are supposed to rest on."* An entry with no outbound link cannot be reached from the pages it is supposed to support.

## 6. Exit checklist — all of it, in order

Nothing is done until every line passes.

cd ~/wiki-brain

bin/wiki-lint && bin/wiki-connect check && bin/wiki-climb check   # ALL at 0 errors

bin/wiki-digest && bin/llm-publish

- All three gates report **0 errors**. Warnings are fine; errors are not. A "missing frontmatter" error means you skipped §4.3.

- `log.md` — appended as **findings, not activity**: what was wrong, what the evidence was, what changed.

- `LLM_HANDOFF.md` — new entry with what you did and the exact next focus. This file is read at the start of every session; if you don't update it, the next pass starts from a stale pointer.

- Staged **by path**, never `git add -A`.

- Committed on the branch from §1, not on `main`.

- **Pushed** — `git push -u origin <branch>`. A local commit is not a deliverable. Verify with `git log origin/<branch> -1`.

- PR opened against `wiki-brain`.

Then report to the operator:

1. What was applied — pages touched, edges added, sections written, pages created.

1. **Every HOLD**, with the quote and what would settle it.

1. Anything cut under §2, and which disqualifier it hit.

Report cuts and HOLDs plainly. A finding you declined to assert because the quote didn't support it is the skill working, not a failure — and it is the single most valuable thing you can hand back.
