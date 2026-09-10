## name: wiki-rewrite description: > Full wipe-and-rewrite of one or more existing wiki/ pages in this repository — re-researching every claim from raw/ rather than editing the prose in place, then rebuilding the page's typed edges, index entries, downstream corrections and staleness cascade. Use this whenever the operator asks to rewrite, redo, wipe, rebuild, re-research, overhaul, "fully flesh out", or "start over on" a named page or set of pages, whenever they paste wiki page URLs or paths with an instruction to redo them, and whenever they say an existing entry is thin, stale, wrong, or shouldn't keep its current structure. Also use it when a page turns out to be about the wrong person or to rest on a false number and needs rebuilding rather than patching. This is the rewrite counterpart to INGEST_RUNBOOK.md, which governs ingesting new sources — reach for this one when the target is a page that already exists.

# Wiki rewrite — wipe, re-research, rebuild

## What this actually is

A wipe-and-rewrite reads like a formatting job and is not one. **It is a re-derivation, and its product is the delta between what the page said and what the corpus says.** Discarding the old headings is the permission you have been given, not the goal. If you finish a rewrite and the page says the same things in a nicer order, the pass failed — not because the prose got no better, but because the reason the operator asked was that they suspected the page was carrying something untrue, and you did not go and check.

That suspicion is usually right. In the reference pass (four pages, logged 2026-08-08), **every single page carried at least one false claim that one well-aimed grep settled** — a wrong surname, a wrong date, a wrong message count, a wrong book. None of those errors were visible from reading the page. All of them were visible within about ninety seconds of opening `raw/`.

So the shape of the work is: inventory what the page asserts → go find out whether each assertion is true → let what you find decide the new structure.

## Before you touch anything

Read, in this order: `CLAUDE.md`, `LLM_HANDOFF.md` (the current state and resume points), `STYLE_GUIDE.md` (binding page format), `CONNECTIONS_SPEC.md` (typed edges). If the pages you are rewriting carry `synthesizes:`, or anything above them does, read `SYNTHESIS_SPEC.md` too. `EXTRACTION_SPEC.md` is required reading — it governs how deep to go into a source, and its traps section is what keeps you from counting the message corpus wrong.

Then **snapshot what you are about to destroy**, because this is the failure this repository has already had once and written down:

git show HEAD:wiki/<domain>/<page>.md > /tmp/claude-*/scratchpad/<page>.old.md

The 2026-08-02 `fran-coldren` rebuild dropped seven inverse edges other pages were pointing at and silently deleted a standing `CONTRADICTION` block. The edges were caught by a gate; the contradiction was caught only by luck on re-read. Before writing the new page, extract from the old one:

- the full `connections:` block (other pages point at these; deleting an edge strands its inverse)

- every `> **CONTRADICTION:**` and `> **REVISED [date]:**` block

- any resolved-prediction or falsification record

- the `Gaps` list — the old page's honest unknowns are research leads, and in the reference pass one of them (`zach-harshman`'s doubt about its own surname) turned out to be the thread that unravelled the whole page

"Wipe" governs the prose and the heading structure. It does not govern earned knowledge. A contradiction someone flagged in 2026-07 is a finding; carry it forward, or explicitly resolve it and say so.

## Phase 1 — inventory

Two lists, both cheap, both worth writing down before you read any raw.

**What the page claims.** Walk the old page and pull out every checkable assertion: dates, counts, names, spans, directions, ratios, attributions. These are your research targets. Do not skim past the ones that look boring — "22 messages" and "~2012–2015" both looked boring and both were wrong.

**What points at it.** Inbound links tell you which other pages will break and, more usefully, which other pages have been *relying* on the claim you are about to test:

grep -rln "<page-slug>" wiki/ *.md

grep -rn -A2 "page: wiki/<domain>/<page-slug>" wiki/

The second command gives you the existing inverse edges with their claims. You need these both to avoid stranding them and to know what type to pair when you rewrite your own block.

## Phase 2 — re-research from raw

**Start wide, not from the page's own ****`sources:`**** list.** That list is a floor and it was wrong on all four reference pages — it records what a previous pass happened to read, not what exists.

grep -ril "<subject name>" raw/ | head -40

grep -ril "<alias>" raw/          # and every handle, nickname, maiden name

Then read what comes back. The mechanics of each source type — the message dump's record format, how to walk a GEDCOM, how to strip the Facebook and Google activity HTML, where contact identities live — are in `references/corpus-recipes.md`. Read that file before writing greps against a source type you have not handled before; several of these formats will silently give you a wrong answer rather than no answer.

**Rank your sources, and say so on the page.** This repository's raw tree mixes two very different kinds of evidence, and conflating them is how false claims get laundered into the wiki:

- **Primary** — message dumps and per-thread CSVs, the GEDCOM, contact exports, Goodreads/YouTube/Twitter takeouts, Facebook message threads. These record what happened.

- **AI-secondary** — the Gemini sessions, `THE_DAN_FRANK_BOOTLOADER.md`, `CATO_*`, `DANSYNTH.txt`, the various profile dumps. These are a model reasoning about the corpus, often confidently and often wrong. They are genuine sources for *what Dan said and thought* — his own corrections inside a session are primary testimony — but their factual assertions are not evidence.

In the reference pass, a Gemini session had asserted a property deed lookup it never showed, and the invented sale date had been sitting in the wiki as fact. When you keep an AI-secondary claim, mark it as one on the page.

**Verify every derived number with the right instrument.** Message counts, direction splits, date ranges and ratios are the figures the operator checks, and naive `grep` on the message dump is quietly wrong for three separate reasons documented in `EXTRACTION_SPEC.md`. Use `bin/mine-messages`:

bin/mine-messages grep '<pattern>' --from 2017-01-01 --to 2018-12-31

bin/mine-messages stats

This is not a formality. Writing this skill, a recount caught a per-day figure in the freshly-written page that had been eyeballed off a grep — 28 messages reported as 22. The instrument catches you; the eyeball does not.

Direction is the trap that produces the most confident wrong answers. `MASTER_MESSAGES_DB_DUMP.csv` marks nearly everything `Received`, so any page built from it reports one-sided threads. The old `zach-harshman` page said "22 messages, all received (export artifact)" — 22 was exactly the received count, there was no export artifact, and Dan's own 19 messages were simply invisible to the file the page was built from. **Any claim about what Dan said must come from ****`all_imessages_complete_dump.txt`****.**

**Resolve identity through the contact exports, not the page title.** If the subject is a person, do this before you write a word — a page can be about the wrong human and read perfectly. Cross-check `contacts.csv` against the Facebook address book; agreement across two independent exports is a real identification, and a single merged Google Contacts record is not. Recipe in `references/corpus-recipes.md`.

**Follow proper nouns outward.** The highest-value findings in the reference pass all came from chasing a name out of the subject's own material into somewhere else: a brother's name into the family tree, a street name into a third page, a nickname into an address book. Budget for this; it is where the delta lives.

## Phase 3 — find the organizing principle

Before writing, answer in one sentence: **what is this page actually about, now that you know what you know?** The new structure comes from that sentence.

This is the step that makes the rewrite worth the tokens, and it is the one that gets skipped. Worked examples from the reference pass:

- A novelist page reorganised from "here is a remarkable coincidence" to **"here is the correction record"** — because the coincidence was already written down three times and what nobody had was the four rounds of the operator killing a confident model's hypotheses, which is the thing the page is actually evidence of.

- A house page reorganised from a list of things that happened there to **"the family's return terminus, and the eight months it belonged to someone else"** — because the GEDCOM supplied an arrival and the message corpus supplied an afterlife, and neither was on the page.

- A person page reorganised around **"a misattribution corrected"** — because the identity finding was larger than anything in the subject's own record.

If you cannot write that sentence, you have not finished Phase 2.

## Phase 4 — write

Follow `STYLE_GUIDE.md`; it binds. The points that matter most under a rewrite:

- **The first paragraph answers the stranger's question** — who this is to Dan, what state the relationship is in, what one thing defines it. Corpus statistics go last.

- **Consequence order, not chronology or ingest order.**

- **Say the load-bearing thing plainly.** If the research supports "this page was about the wrong person," write that sentence in the lead.

- **Longer is the standing preference.** Lint's 8 KB warning is advisory. Never trim earned content to clear it.

- **Tables hold numbers, prose holds meaning** — and never narrate a table.

- **Corrections are flagged, not silently applied.** A rewrite that fixes a false claim writes `> **CORRECTED [date]:**` or `> **REVISED [date]:**` with the old claim visible and the evidence that killed it. This is the single most valuable artifact the pass produces: a future reader needs to know the wiki *was* wrong here, or they will re-derive the error from the same bad source.

- **Gaps are content.** Name what you could not settle, including anything you deliberately left as an open `CONTRADICTION`.

## Phase 5 — wire it back

A rewritten page is not finished until the graph agrees with it.

1. **Write the new ****`connections:`**** block** — typed edges, argued one-sentence claims, per `CONNECTIONS_SPEC.md`. Aim for 3–10.

1. **Add the inverse on every target.** Pair the types correctly (`evidences`/`evidenced-by`, `instantiates`/`instance-of`, `component-of`/`contains`, `causes`/`caused-by`, `precedes`/`follows`; `contradicts`/`parallels`/`mirrors`/`co-occurs` are symmetric; `contextualizes`/`escalates`/`resolves` need no inverse). A mismatched pair warns on both sides and transmits nothing.

1. **Prose the load-bearing edges.** `causes`, `contradicts`, `instantiates` and `parallels` must be argued in the body of at least one of the two pages.

1. **Diff old edges against new.** Anything you dropped has a stranded inverse — either restore the edge or remove the inverse deliberately.

1. **Update the domain index** and any hub page whose one-line summary is now wrong.

1. **Propagate corrections downstream.** If the page was wrong, other pages probably repeat the error. In the reference pass a false claim about two five-starred books had already spread to `books.md`; it was corrected there in the same commit. Grep for the wrong fact, not just the page name.

If the identity changed, the page gets renamed: `git rm` the old file, create the new slug, sweep every inbound link, fix the index entry, and check the generated `llm/pages/**` path turns over. Say plainly in the log why the old name was wrong.

## Phase 6 — the staleness cascade

Rewriting a page makes every page that declares it under `synthesizes:` stale, and clearing those makes *their* dependents stale. Expect two rounds; the reference pass had exactly two.

bin/wiki-climb check

**Bumping ****`date_modified`**** to silence a staleness warning is the one prohibited move in this system.** Re-read what actually changed in the premise, decide whether the conclusion survives, and record the decision on the page as a `> **RE-CHECKED [date]:**` block — including when the answer is "survives unchanged," which is a real result and takes two sentences.

Treat these re-checks as findings rather than paperwork. In the reference pass they produced two: a synthesis about retention gained a boundary (the retention is *asymmetric* — the other party had not kept Dan's number), and another had two of its own named gaps moved by newly-read primary evidence. Both are things no one would have gone looking for.

## Phase 7 — ship

All three gates at **0 errors** before committing; warnings are acceptable and size warnings are advisory:

bin/wiki-lint && bin/wiki-connect check && bin/wiki-climb check

Then regenerate the committed artifacts, which the repo expects to track content:

bin/wiki-digest && bin/llm-publish

Then the record. `log.md` gets an append-only entry headed `## [YYYY-MM-DD] rewrite | <domain> | <what>`, written as findings rather than activity — what was wrong, what the evidence was, what changed. `LLM_HANDOFF.md` gets a new session entry at the top with gates, findings in order of value, and resume points; leave the older entries untouched, they are history.

Commit with `<op>: <short description>`, push with `git push -u origin <branch>`, open a **draft** PR describing the deltas rather than the file list.

## The failure modes, collected

Each of these has actually happened in this repository.

| **Failure** | **What it looks like** | **Guard** |
| --- | --- | --- |
| Reformatting instead of re-deriving | new headings, same facts | inventory the claims in Phase 1 and check each |
| Trusting `sources:` | research stops at the declared list | `grep -ril` the whole of `raw/` first |
| Laundering AI-secondary as fact | a Gemini-invented date sitting in the wiki | rank sources; mark what is secondary |
| Naive grep on the message dump | miscounts, truncated messages, missed curly apostrophes | `bin/mine-messages`, and read `EXTRACTION_SPEC.md` |
| Trusting direction from the CSV | "all received (export artifact)" | direction only from `all_imessages_complete_dump.txt` |
| Identity by page title | a page about the wrong person | resolve through two independent contact exports |
| Regenerating over earned content | dropped inverse edges, deleted contradiction blocks | snapshot and extract before writing |
| Silent correction | the false claim vanishes with no trace | `CORRECTED`/`REVISED` block with the old claim visible |
| Orphaned downstream error | the page is fixed, the pages quoting it are not | grep the wrong fact across `wiki/` |
| Date-bumping a stale premise | `wiki-climb check` goes quiet, nothing was read | `RE-CHECKED` block, always |

## Worked example

The four-page pass of 2026-08-08 — `jacob-bacharach`, `117-belmont-circle`, `zach-harshman`→`zach-clingan`, `alexis-armel` — is this protocol run end to end, including the rename, the downstream correction and the two-round staleness cascade. The findings and the reasoning are in `log.md` under that date, and the session summary is at the top of `LLM_HANDOFF.md`. Read them when you want to see what the delta is supposed to look like.
