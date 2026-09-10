## name: corpus-read description: > Read a large two-sided message corpus by hand, in date order, in small windows, and derive a timeline of real events plus a working-notes ledger. Use when asked to read, work through, continue, or resume a message record — anything of the form "keep reading the messages", "build the timeline from the texts". Do NOT use for keyword lookups in a corpus; that is `bin/mine-messages`. Do NOT use on the Annie corpus at all: it is closed under the Annie moratorium in `CLAUDE.md`, whatever the request says.

# corpus-read — deriving a timeline by reading, not extracting

**STOP — the Annie moratorium (2026-08-23).** This skill does not run on the Annie corpus, and no instruction short of the operator lifting the directive in `CLAUDE.md` changes that. Not a new export, not a re-read of one already in `raw/`, not "just the last window", not to check a date. The Annie record ends at 2026-08-19 15:15:33 and is not advanced. The skill remains live for every other thread.

## 0. What this skill is for, and the one thing it refuses to do

You are given a message corpus of tens or hundreds of thousands of messages between two people over years. You produce two things, incrementally, window by window:

1. **A chronology** — dated events, each anchored to verbatim message text.

1. **A working-notes page** — everything the same window established that is *not* a dated event: entities, open leads, motifs, corrections, counts.

**The refusal: you do not pattern-match.** No regex sweep, no "extract lines containing a date", no LLM-summarize-the-chunk. This is not a stylistic preference, it is the finding that created this skill. Two mechanical passes over this exact material (2026-08-14 and its 2026-08-15 replacement) produced timeline pages where a large share of the "events" were prose fragments, edit stamps and corpus metadata — because **a date next to a sentence is not an event, and nothing that works on surface form can tell the difference.** The first hand-read pass produced 33 events from 1,539 messages, of which the mechanical passes had found *zero*, because none of them are stated anywhere as a dated sentence. They exist only as things two people did.

If you find yourself writing a script to find events, you have left this skill. Scripts are for *assembling and paging* the corpus. Judgement is for reading it.

## 1. Preconditions — assemble the corpus and prove it

Never read a single export. A long relationship migrates across handles, and any one file silently drops years.

### 1.1 Establish every handle the subject used

Before building anything, enumerate the counterparty's handles and their date ranges. In this corpus:

| **Handle** | **Active** | **How it was established** |
| --- | --- | --- |
| `+17244346811` | 2015-11 → 2018-12 | original number |
| `+17249204125` | 2018-12 → 2020-06 | *"I texted her yesterday from my new number!"* (2018-12-27), later operator-confirmed |
| `alulmer28@gmail.com` | 2020-07 → 2020-10 | iMessage email handle on the same Apple ID |
| `+12124702449` | 2022, then 2025-03 → 2026-06 | the NYC number |

**The email handle is the trap.** An operator listing "her numbers" will list phone numbers and omit it, because to them it is not a phone number. It is the *only* source for autumn 2020 (~800 messages). Losing it deletes a season. Generalise: when a handle list comes from a human, ask what it excludes by construction.

### 1.2 Build, de-duplicate, sort

`bin/annie-corpus build` merges every export carrying the subject's traffic into one de-duplicated, chronologically sorted CSV. Read `bin/annie-corpus` before running it; the two things that matter:

- **De-duplication key is ****`(timestamp, direction, text)`****.** Exports overlap heavily — one source contributed 94,855 new rows and the next contributed 0. That is expected, not a bug.

- **The blank-contact rule.** In a per-contact export (`imessage_<numbers>_…`) a `sent` row has an empty contact field — the contact is implied by the filename. In an all-contacts export the same blank means *unattributable*. Blanks may be claimed for the subject **only** from subject-scoped files. Getting this backwards silently imports other people's messages into the record.

### 1.3 Prove the build before you read a line

Run `build` and `coverage`, and check the totals against what the chronology page already claims. A correct rebuild here reproduces **97,768 unique messages, 2015-11-28 18:47:54 → 2026-06-05 00:37:42**. If your number differs, stop and find out why before reading — every downstream percentage is wrong otherwise.

## 2. Map coverage, and declare the holes as holes

Run `bin/annie-corpus coverage`. You get messages-per-month with `·` for zero.

**The governing rule, from ****`EXTRACTION_SPEC.md`****: a zero is data only when the system could have observed a one.** A month with no messages is a hole in the *archive*. It is not a quiet period in the *relationship*, and no page and no downstream synthesis may treat it as one.

This corpus's holes, and how to state them:

- **2020-11 → 2024-12 — 5 messages in four years.** Four years of a ten-year relationship with no surviving two-sided data in any export. This must be carried as a standing blockquote warning on the chronology page.

- **Interior holes inside a "dense" stretch.** The stretch labelled dense (2015-11 → 2020-10) still contains **three fully-zero months** — 2016-06, 2016-09, 2017-08 — and four near-zero ones (2016-02: 3 msgs, 2016-10: 2, 2020-05: 15, 2020-10: 7). A coverage table that says "dense — near-daily" over that range is *overstating the record*. Name the interior zeros.

- **Zero-days inside a month you are about to read.** December 2015 carries 12,146 messages but on only **18 of 31 days**. Dec 4–7 is a contiguous four-day hole; Dec 20–28 is a nine-day hole that swallows Christmas. Before reading a month, run `bin/annie-corpus days YYYY-MM` and write the missing days down. A reader who does not do this will narrate Christmas 2015 as something that did not happen.

**Never describe a month by its day-count when only some days carry traffic.** "December 2015 is 12,000 messages across 31 days" is false; it is 12,146 across 18 days with 13 days absent.

## 3. Size the window

`bin/annie-corpus days YYYY-MM` prints per-day counts. Size a session by messages, not by calendar span.

- **400–1,300 messages is one comfortable window** — typically one day in a dense stretch, or several days in a thin one.

- Read whole days. Never split a day across sessions; overnight bursts run past midnight and an event cut in half is an event misread.

- **Do not prioritise by volume.** 2015-11-29 carries 1,026 messages and yields 15 events; 2015-11-28 carries 110 and yields 9. Volume tracks *affect*, not incident. A high-volume day is usually two people gushing; the events are often in the quiet days where something was actually arranged.

Then `bin/annie-corpus read FROM TO`, and **read the whole thing, top to bottom, before writing anything.** Not skimmed for candidates. The reason is that most events in this material are only visible in sequence — three lines scattered over five hours that together place a person in a house.

## 4. What counts as an event

This is the entire skill. Everything else is bookkeeping.

### 4.1 The discrimination test

Before writing an entry, ask: **could someone who had not read this window have written this line?** If yes, it is not earned and it does not go on the page. "They were very much in love" fails. "Annie's first surviving message is hers, 18:47, and she abandoned her own birthday dinner to send it" passes.

Second test: **does it survive the removal of the affect?** On a 669-message day, perhaps 600 messages are endearments, emoji and reassurance. They are context, not content. What survives is what someone *did*, *arranged*, *disclosed*, *concealed*, or *paid for*.

### 4.2 The five things that make an event

Record an entry when the window establishes one of these:

1. **A fixed date, time, place or identity** the wiki lacks or has wrong. *"has to give y one more happy bday"* (2015-11-28 23:50) fixes Annie's birthday as November 28. *"I'm on 3 tee"* (01:57) fixes the meeting location.

1. **A first instance of a pattern later material makes central.** The concealment-as-reassurance move — *"Alexis doesn't know that you have any part in this… So you don't need to worry"* (11-28 19:01) — is the earliest instance in 97,768 messages of a shape the terminal-phase record runs on.

1. **An action, not a feeling.** A key confiscated. A car offered. A laptop taken back. A person removed from a house through a third party. Feelings are the medium; actions are the record.

1. **A mechanism — *****how***** something was accomplished.** The eviction is the model case: key confiscated (11-28) → property removed from the guest bedroom *"so she knows I could actually call the cops"* (11-30 00:35) → parents summoned (11-30 13:42) → a mother's 1pm inspection set as the deadline (12-01 09:27) → completion at noon. Each step reversible, none a scene. The mechanism is the finding; the completion date is trivia.

1. **An absence with an address.** *"Whenever you wake up, you have love letters in your inbox"* (11-30 06:51) establishes that the most deliberate writing of the first week went through an **email channel the message archive does not contain**. A named, chaseable gap is a first-class event. A vague one ("we probably don't have everything") is not.

### 4.3 What is not an event

- A sentiment, however intense or however many times repeated.

- A plan that is never executed and never referred to again.

- A restatement of something already on the page. **An event is recorded once, at its earliest instance**; later occurrences go to the motif tracker (§6.3), not back onto the chronology.

- Anything you inferred from other wiki pages rather than from this window. That is a *connection*, and it belongs in the entry's prose, explicitly marked — never in the headline.

### 4.4 Events span messages, and often span hours

The golf-course meeting is six messages over forty minutes plus a confirming line thirteen hours later. The Alexis assault is four messages at 05:04–05:06 plus a retelling at 12:14. **Do not look for the message that "is" the event.** Look for the set of lines that together make it undeniable, and cite them all.

## 5. Writing the chronology entry

### 5.1 Anatomy

**YYYY-MM-DD[, HH:MM or HH:MM–HH:MM] — <the finding, stated as a claim>.**

<Verbatim quotes with timestamps, in sequence.> <What they establish, and why

it matters.> <Any correction to an existing page, with a [[wikilink]].>

The headline is a **claim, not a label.** "Suz supplies cocaine and offers a car, conditional on evicting Alexis" — not "Suz visit". If the headline could head a different day's entry, it is too vague.

### 5.2 Quote discipline — non-negotiable

- **Quotes are exact.** Typos, missing apostrophes, autocorrect wreckage and all: *"K I'm on gold course"* keeps the typo. Every one of the first pass's 33 entries was checked against the corpus and all quoted strings matched character-for-character. Hold that standard; it is what makes the page usable as evidence.

- **Every quote carries ****`HH:MM`****.** Every one.

- Consecutive messages from one speaker may be joined with `/`.

- Elide inside a quote with `…`, never across speakers.

- Attribute when it is not obvious from the text who is speaking.

### 5.3 Mark every inference as an inference

This is the failure mode this skill most needs to prevent, because it is the one the first pass actually committed. The entry for the golf-course meeting ends: *"The location is the ****3rd tee**** of the Uniontown Country Club course."* The corpus establishes *"I'm on 3 tee"* and *"meet you on the golf"*. **It does not name the club anywhere in the window.** The club identity is imported from other knowledge and stated as flat fact.

The page's own method note promises "where a reading is uncertain it says so." Keep that promise mechanically:

- Sourced by this window → state it plainly.

- Inferred from another wiki page → say so and link it: *"the course is presumably Uniontown CC, per [[wiki/interests/golf]] — not named in this window."*

- Genuinely ambiguous → *"reading uncertain"*, and put it in Open Leads.

An unmarked inference is worse than a gap, because the next reader cannot tell it apart from evidence.

### 5.4 Where the entry contradicts the wiki, say so on the spot

A read pass earns its cost mainly through corrections. Three from the first pass:

- The dossiers quote *"I met someone that instantly changed my life"* with no address. The corpus shows it said **to Annie**, 2015-11-29 03:28, an hour after the first meeting — and that the substantive follow-on (*"And I was alright with that for so long that I forgot I was sad"*) was never quoted.

- *"YOU ARE MY EVERYTHING"* is dated "day two/three" by the period page. It is 2015-11-29 **03:24**, hours after the first meeting.

- Every existing account treats Annie as unattached at the switch. She was not: *"my fam and dude are here"* (01:35), *"turd boy"* (02:49), **"I am going to get rid of him just like you just did"** (02:52). **The switch was mutual and simultaneous.**

Write the correction into the entry, link the page it corrects, and queue it in the notes page's corrections table (§6.4). Do **not** silently fix the other page mid-read — that is a separate pass, and losing your place in the corpus to do it is how a read dies.

## 6. The second output — the working-notes page

**Reading is the expensive step and it is paid once.** Pulling a second kind of finding out of a window you have already read costs almost nothing. Re-reading 97,768 messages to recover something you noticed and did not write down costs the entire pass again. A read that records only *events* therefore discards, at the moment of maximum information, everything that is not an event.

So every pass writes **both** pages, **in the same session**. Notes captured after the fact are notes not captured.

Five sections, all updated every pass:

### 6.1 Entity ledger

Every named person, place, animal or thing at **first appearance**, with what the corpus itself says about it, and a status: `→ wiki/path` if a page exists, **no page** if it is a candidate. This is how you discover that "Shu", "Andre" and "Morgantown homeboy" exist at all.

### 6.2 Open leads

Chaseable questions, each **a specific thing to look for, not a topic.** Good: *"Dan's 'love letters' go to an inbox, not by text (11-30 06:51). Look: **`gmail_bodies.txt`** and any Gmail export, late Nov 2015."* Bad: *"investigate email."* Number them so later passes can close them by number.

### 6.3 Motif tracker

Patterns with **dated instances**, recorded now so a later synthesis can count them instead of re-reading. Each motif gets an ID (M1, M2 …), a one-line statement, and a growing list of dated instances. When a later window repeats a motif, you add an instance — you do not add a chronology entry.

### 6.4 Corrections queue

A table: page · standing claim · what the read shows. Mark each **applied** or **not yet applied**. This is the handoff to the pass that fixes the other pages.

### 6.5 Quantitative markers

Counts worth having but not worth computing yet, plus hard anchors — first "I love you" and its timestamp, sleep-cycle observations, initiation ratios. **Compute these from the corpus, not from memory** (see §8.3).

## 7. Bookkeeping — the resume contract

A read spanning many sessions dies at the handoff unless every pass leaves:

1. **A progress table row** — read-through date · messages read · % of total · events recorded. After the first pass: `2015-11-30 | 1,539 | 1.6% | 33`.

1. **An explicit resume pointer** — the literal next command: `bin/annie-corpus read 2015-12-01`.

1. **A sizing note for the next window** — what `days` says about it, and any zero-days inside it.

1. **A rate note** — what this pass cost and yielded, so the next reader can plan. Include the honest warning that early-relationship density is not representative.

### 7.1 The counts must reconcile — this is a real defect, not a nicety

The first pass's progress table claims **34 events**; the page body contains **33** (9 on 11-28, 15 on 11-29, 9 on 11-30). Its rate note claims *"two days of reading produced 25 events"*; those two days carry **24**. A consistent off-by-one in both places, most likely from an entry merged or dropped without updating the counters.

It is a small error that does exactly the wrong thing: the progress table is the one part of the page a future reader *trusts without checking*, because re-deriving it means re-reading. **Recount from the page body before writing the number**, every time:

grep -c '^\*\*[0-9]\{4\}-[0-9]\{2\}-[0-9]\{2\}' wiki/timeline/annie-record.md

And re-derive "messages read" from the corpus rather than adding up remembered per-day counts.

## 8. Verification gate — run before every commit

### 8.1 Every quoted string exists, verbatim

For each new entry, confirm the quote appears in the window you read. Batch this carefully: `grep -hc` over several files at once **misreports which file a match came from**. Check one file at a time, or you will "verify" a quote onto the wrong day.

### 8.2 Every quote is on the day it is filed under

Attribution drift is the easiest error to make and the hardest to see later. The first pass survives this check — 15/15 spot-checked quotes landed on exactly their stated day, including cross-day cases like Suz's phone call, where the *messages* are 11-30 13:48–13:49 and the *call* they describe is the night of 11-29 (*"My mom called me last night after she left"*). When an entry dates an event earlier than the messages that report it, say which is which.

### 8.3 Every derived number is re-derived, not remembered

The notes page states: *"Both parties' 'I love you' appears within 32 hours of the first in-person meeting (Dan 03:14, Annie 03:14, 2015-11-29)"* — and calls it *"a hard date for any later claim about escalation speed."*

Checked against the corpus, **both halves are wrong**. Annie's first is **02:47** (*"Babe I love you"*), not 03:14 — 27 minutes before Dan's. And the meeting is 01:52–~02:30 **the same night**, so the interval is **under twenty minutes**, not 32 hours. The claim understates its own finding by two orders of magnitude, and it was explicitly flagged as load-bearing for later work.

Any number offered as an anchor gets recomputed from `exports/annie-corpus.csv` at the moment it is written down.

### 8.4 Both pages moved in the same commit

If the chronology changed and the notes page did not, the pass is incomplete.

### 8.5 Repo gates

`bin/wiki-lint && bin/wiki-connect check && bin/wiki-climb check` at 0 errors; then `bin/wiki-digest && bin/llm-publish`. Append to `log.md` as **findings, not activity** — what was wrong, what the evidence was, what changed. Commit as `ingest: <what the window established>`.

## 9. Frontmatter

Both pages: `domain: timeline`, `status: active`, **`knowledge: earned`** — this is reasoning done once and must never be regenerated from scratch, only revised (`CLAUDE.md`, "why this is a second brain, not a RAG"). Chronology is `page_type: chronology`; notes are `page_type: reference`. List every export in `sources:`. Wire them to each other and outward with typed `connections:` per `CONNECTIONS_SPEC.md`.

## 9.5 Data Locations

The Annie Read project stores data in **two repos with a strict hierarchy**:

### caakehorn/wiki-brain (PRIMARY — source of truth)

- **Local clone:** `/Users/daniel/wiki-brain`

- **Record:** `wiki/timeline/annie-record.md` — markdown, not JSON-wrapped

- **Notes:** `wiki/timeline/annie-read-notes.md` — markdown

- **Raw exports:** `raw/self/message-csv/`

- **LLM_HANDOFF.md:** resume point and session log

- **queue.md:** ingest queue

### caakehorn/home (DERIVED — do not edit directly)

- **Local clone:** `/tmp/homeclone`

- **Record:** `public/wiki/pages/timeline__annie-record.json` — JSON-wrapped, update `body` field

- **Notes:** `public/wiki/pages/timeline__annie-read-notes.json` — JSON-wrapped, update `body` field

- **URL:** [https://caakehorn.github.io/home/brain/timeline/annie-record](https://caakehorn.github.io/home/brain/timeline/annie-record)

- **Notes URL:** [https://caakehorn.github.io/home/brain/timeline/annie-read-notes](https://caakehorn.github.io/home/brain/timeline/annie-read-notes)

**The home repo is derived from wiki-brain via ****`sync-wiki.yml`** (runs hourly and on dispatch). Edits to home's `public/wiki/` are overwritten by the sync. **Always edit wiki-brain first.** The home repo receives the content through the sync pipeline.

**Work in caakehorn/wiki-brain. Pages are wiki/**.md — edit those. Run bin/annie-corpus read FROM TO for the window, and update both wiki/timeline/annie-record.md and wiki/timeline/annie-read-notes.md in the same pass. Never edit public/wiki/** in caakehorn/home: it is a build artifact regenerated from this repo hourly, and anything written there is deleted within the hour.**

## 10. Known failure modes, in the order they actually occur

1. **Reaching for a script.** The instant the corpus feels too big, the urge is to grep for events. It produces garbage. Read a smaller window instead.

1. **Recording affect as incident.** Symptom: entries that would be true of any day. Apply §4.1.

1. **Unmarked inference.** Symptom: a specific proper noun that never appears in the window (§5.3).

1. **Count drift.** Symptom: the progress table disagrees with the body (§7.1).

1. **Remembered statistics.** Symptom: a clean-looking number nobody re-derived (§8.3).

1. **Treating a hole as a quiet period** (§2).

1. **Letting the notes page lag the chronology.** It is worthless the moment it is written from memory rather than from the open window (§6).

1. **Chasing a correction mid-read** and never returning to the corpus. Queue it; finish the window.
