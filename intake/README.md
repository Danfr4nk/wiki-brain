# `intake/` — the intake ledger

A finite object enters the record. Every known disposition of that object is recorded after it. At closure the system reconciles what is known, preserves what is unknown, and computes only what the evidence actually supports.

That sentence is the whole design. Everything below is how it is enforced.

Run it with `bin/intake`, from the local app at **Special:Intake**, or from **`/ledger`** in [`caakehorn/home`](https://github.com/caakehorn/home) — the portal, which is the one interface that is in your pocket.

## Why a unit and not a dose

A dose diary records *"I did X at 8:30"* and can answer almost nothing afterwards, because the number it holds has no denominator. This tracks the **unit** — a finite quantity that entered the record at a known time — and then records every known disposition of that unit until it is gone.

UNIT RECEIVED  ──▶  UNIT RECORD          substance · initial quantity · unit ·

(finite, dated)      received_at · source · status

│

│  each intake event consumes some of it

▼

INTAKE EVENT         occurred_at · quantity? · measurement

(repeatable)         type · descriptor · note

│

▼

CLOSURE              how it ended, and what happened to

(reconciled)         anything unaccounted for

│

▼

UNIT REPORT          duration · counts · mean/median/min/max

(computed)           · intervals · peak window · phases

Only with a denominator can the ledger reach the questions worth asking: how long 3.5 g actually lasts, whether the first dose runs larger than the rest, whether consumption accelerates toward depletion, how often a unit is gone inside a day. A list of doses cannot answer any of them.

## Three kinds of event, because precision is not always available

| **kind** | **what it holds** | **counts toward** |
| --- | --- | --- |
| `measured` | `0.18 g` on a scale | everything |
| `estimated` | `~0.2 g` with a confidence | everything, flagged |
| `unquantified` | `"one line"`, `"two hits"` | event counts, timing, clustering — **never** a quantity statistic |

The third is the one that matters. A system that only accepts grams loses the behavioural record — the count, the timing, the clustering — every time the scale is not to hand, and it loses it *silently*. Here the event is still real:

Unit #1 had 13 consumption events over 40 hours. Ten were quantitatively measured, accounting for 2.45 g. Three were logged without a reliable quantity.

That is more honest than inventing precision, and it is strictly more data than refusing the event. **Every quantity figure this tool prints carries the share of events it was computed from**, so a mean over 10 of 13 events never gets to look like a mean over 13.

## The arithmetic is deliberately incomplete

Open 3.5 g, log ten events totalling 2.7 g, close the unit — this tool will **not** tell you the average dose was 0.35 g. It does not know what happened to the other 0.8 g, and inventing a distribution for it produces a number that looks like evidence and is not.

So closing a unit asks two questions. *How did it end* — consumed, discarded, transferred, unknown. And, if quantity is unaccounted for, *what was that quantity* — a final intake, a measurement discrepancy, a spill, a transfer. `bin/intake close` refuses to proceed without an answer:

$ bin/intake close 1 --disposition consumed

intake: 1.05 g is unaccounted for — say what happened to it:

--resolution final_intake|discrepancy|lost|transferred|other

Answer `final_intake` and the remainder is written as one **estimated, low-confidence** intake event, and the report says so wherever it shows up:

COVERAGE

1.05 g of the quantified total is a single remainder written off at close,

not a watched dose.

Reconciliation is a recorded decision with a timestamp, never a silent subtraction.

## Event-sourced, in plain files

`events.jsonl` is the **source of truth**: append-only, one JSON object per line, never rewritten. `units.json` is a **projection** — regenerated from the log on every write, and safe to delete (`bin/intake rebuild` returns it identical). `substances.json` is reference data: the select box, and the one file here meant to be edited by hand.

Nothing is ever edited in place. A mistyped `0.5 g` becomes an `event_corrected` record naming the original, the correction and the reason:

{"type":"intake_logged","id":"intake_evt_01M…","data":{"quantity":0.5,"unit":"g"}}

{"type":"event_corrected","data":{"target":"intake_evt_01M…",

"fields":{"quantity":0.05},"reason":"decimal entry error"}}

The ledger shows `0.05 g`. The log remembers both, and that a correction was needed two minutes later is itself evidence about how the logging happens.

**JSONL rather than SQLite**, which the first sketch called for. This repository is plain files under git and that is not incidental to it: a JSONL line diffs, greps, survives every tool here, and shows up in `git log` as the history it already is. `sqlite3` is stdlib and would have worked — it would just have been the only unreadable file in the corpus.

## ⚠ The ledger is public. Read this before you log anything.

`intake/events.jsonl` and `intake/units.json` are **tracked, in a public repository**. That means the record of what was consumed, and when, is readable by anyone who finds this repo, permanently — git history cannot be un-published.

That is a decision, taken on 2026-08-30, and the operator took it knowing what it publishes. It is written here rather than left implicit because it is not a thing anybody should discover by accident.

**Why it was taken.** The ledger exists so the wiki can set a dated first-party record against a page's narrative — that is the whole reason it lives in wiki-brain rather than in a phone app. Two earlier arrangements each defeated that:

- **Gitignored** kept the record out of the repo and therefore out of reach of every session, agent and synthesis that might have cited it.

- **Sealed** (`intake/events.enc`, AES-256-GCM under the site passphrase) kept a public repo from publishing anything readable — and kept the analysis layer from reading it too. A ledger the wiki cannot open has no reason to be here.

Plaintext is the only arrangement where the thing works as designed. The privacy cost is real, it is not mitigated, and it is the price of the feature.

**To reverse it: make the repository private FIRST, verify it, and only then decide whether ignoring the files is still wanted.** In that order, always.

The sealing machinery is still in the repo and still works — `bin/intake seal` and `bin/intake open`, with `bin/aesgcm.py` underneath — so this is one commit away from being reversible if the trade ever stops being worth it.

### What `.gitignore` never covered

Worth keeping, because it is easy to get wrong in both directions. `.gitignore` governs `git add`: it covers the CLI and the local app. It has no effect whatsoever on GitHub's contents API, which is how both `/ledger` in the portal and ボスの部屋 on the leviathan site write here, from a browser, with no working tree involved. An ignored path is committed by that API without complaint.

So an ignore line was never the whole guard even when it was there, and anyone reinstating one should know it protects exactly one of the three write paths.

## Why it lives in wiki-brain

Because this is the anti-unreliable-narrator layer. The wiki reasons from what was written down, and prose recollection of consumption is the least reliable testimony a person gives about themselves.

*"I barely used anything that weekend."*

The ledger does not argue. It says: `Aug 14–16 — 37 logged intake events across 4 units`, with timestamps. It is a first-party dated dataset that can be set against a page's narrative the way `bin/text-metrics` is set against a page's assertions about how he writes, and it is meant to be cited in exactly that way.

**The ledger is evidence; a page is a claim, and the distinction survives the fact that the ledger now has a page of its own.** `wiki/health/intake-ledger.md` is the record *rendered* — every unit, every event, every correction, generated by `bin/intake page` and served on the portal like any other entry. It exists because the portal's sync reads `wiki/**` and nothing else, so until it was written the only way to see the record was to open a JSONL file in this repository. It states no finding, argues nothing, and concludes nothing about the person.

A **finding** drawn from the ledger still goes onto an ordinary page through the normal operations, cited to a unit id and a date range with the coverage figure attached — never onto the generated page, which is overwritten on every write and would lose it. `wiki/health/cocaine.md` and `wiki/health/chemical-architecture.md` are the worked examples.

Two things the generated page does deliberately. It is **gated**: a hand-edit is drift and `bin/intake check` fails on it, because a hand-written snapshot of a growing log is wrong the day after it is written and nothing would say so. And it **withholds the per-unit rate** — `report`'s `Rate of consumption ... g / day` — rather than printing it with a caveat, on the grounds that a number nobody can quote wrongly is worth more than a number with a warning beside it.

## The commands

bin/intake                          active units, recent events, what to do next

bin/intake substances               the select box — list it

bin/intake substance add "Kratom" --category other --unit g

bin/intake new cocaine 3.5g --at "2026-08-29 13:42" --source "…"

bin/intake log 1 .18g                       measured

bin/intake log 1 .2g --estimated            estimated, medium confidence

bin/intake log 1 --descriptor "one line"    unquantified, still an event

bin/intake log 1 180mg                      converts within the unit's family

bin/intake adjust 1 .3g --kind spill --note "knocked off the table"

bin/intake correct <event> --quantity .05g --reason "decimal entry error"

bin/intake void <event> --reason "logged against the wrong unit"

bin/intake close 1 --disposition consumed --resolution discrepancy

bin/intake reopen 1 --reason "closed it by mistake"

bin/intake report 1                 the unit report, plus every event

bin/intake stats --substance cocaine --since 2026-01-01

bin/intake units --all

bin/intake rebuild                  units.json from the log

bin/intake capture                  file raw/ archives for closed units missing one

bin/intake check                    the gate — runs inside bin/wiki-check

bin/intake export                   the whole ledger as one JSON document

### What the portal does not do

`close` files the unit's archive to `raw/health/intake/` as well as appending the `unit_closed` event. The portal and ボスの部屋 write events straight to `events.jsonl` through the contents API and never call `close`, so a unit closed from a phone — which is most of them — reaches the ledger with **no archive entry at all**, and no gate reports it, because the capture lives outside the data `check` compares. Run `bin/intake capture` after ingesting an export. A capture written that way says `BACKFILLED` on its face and explains that its figures were computed later, from the log as it then stood: the archive's whole warrant is that it cannot be quietly restated, so one that *was* written later must not carry the sentence claiming otherwise.

### One figure that is not what it looks like

`report` prints `Rate of consumption — N g / day`. That is the unit's quantity extrapolated across 24 hours from however long the unit actually lived. A 0.75 g unit consumed over an evening reports **1.89 g / day**, which is not a statement about any day. It is a restatement of the unit's lifespan. Do not cite it as a consumption rate, on a page or anywhere else.

Units convert inside a family and never across one: milligrams are grams, millilitres are not, and `2 tab` is never `2 g`. A cross-family log is an error, not a coercion.

## What the unit report computes

Duration · event counts by measurement type · quantified total split into measured and estimated · remaining · mean, median, smallest, largest dose · dose variability (CV) · mean and median interval · rate of consumption · peak usage window · first dose against the later mean · a time-of-day histogram · and the **phases** — first 25% / middle 50% / final 25% of the unit *by quantity consumed*, with a velocity comparison between the ends.

Phases are cut by quantity rather than by elapsed time on purpose: the question they answer is whether consumption accelerates toward depletion, which is about how fast the material went, not how the clock ran. Unquantified events carry no quantity, so they are placed by falling inside a phase's time span and counted separately — they never move a boundary.

`bin/intake stats` runs the same reasoning across every unit ever opened: unit size and duration distributions, how often a unit is gone inside 24 hours, dose distribution and variability per substance, month-by-month drift in mean dose, and the time-of-day profile of every event in the ledger.
