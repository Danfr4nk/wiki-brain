## name: wiki-housekeeping description: > The periodic LINT sweep over this wiki — the judgment half of housekeeping, after `bin/wiki-check` has run the mechanical half. Triage the standing lint and connect warnings, work the stale-premise cascade, hunt contradictions and claims superseded by newer raw, find entities mentioned repeatedly with no page, drain the outstanding obligations in `WORK.md`, and write the pass up in `log.md` and `LLM_HANDOFF.md`. Use this whenever the operator asks to tidy, clean up, sweep, lint, audit, do housekeeping or "general maintenance" on the wiki; whenever they ask what is outstanding, what is stale, or what needs fixing; whenever they ask you to work through the warnings, the backlog, or `WORK.md`; and at the end of a long content session when nobody has asked but the repo has moved a lot. Reach for it too when a pass has just merged and you want to know what it left behind. This is NOT the pre-commit gate chain — that is `bin/wiki-check`, one command, and this skill calls it first.

# Wiki housekeeping — the sweep that needs a reader

## What this is, and what it is not

`bin/wiki-check` is the mechanical half: regenerate, gate, scan, four seconds, exit non-zero if anything is red. It is deterministic and it needs nobody. Run it, but do not confuse running it with having done housekeeping.

This skill is the other half — the sweep `CLAUDE.md` files under **LINT (periodic)**, which is one paragraph there because it is mostly judgment and judgment does not compress into a checklist. Every item below is a question about meaning that a script cannot answer: *is this warning telling me to do something? did this conclusion survive its premise moving? are these two pages disagreeing, or describing two different things?*

The single most important thing to understand before starting: **most warnings in this repository are not defects, and clearing them is the failure mode.** More on that in step 1, because it is where a housekeeping pass most often does damage.

## Step 0 — the gate outranks everything

bin/wiki-check          # regenerate, gate, scan

A red gate blocks every commit in the repository, so it is priority 0 and nothing below matters until it is green. If it is red, read what failed rather than pattern-matching the fix — on 2026-08-21 `bin/wiki-connect check` sat red on `main` with 70 errors because a portal save had written a 2026-08-13 snapshot back over three later passes, deleting 56 typed-edge claims and ~30KB of prose. The fingerprint was two frontmatter dates moving *backwards in one commit*. The fix was recovery from a prior commit, not editing the errors away. **An error that appeared without anybody editing that page is a corruption question, not a lint question.**

Then read `bin/wiki-work` before doing anything else, so you know what is outstanding *before* you start rather than discovering it after.

## Step 1 — triage the warnings, and mostly leave them alone

Warnings are advisory by design and the tools say so in their own output. Today the entire standing backlog is three categories. Learn them, because the correct action differs sharply and two of the three are "do nothing":

**`page is NNKB — unusually long`**** (10 pages).** Almost always **leave it**. `CLAUDE.md` is explicit: size warnings *"mean 'check navigation,' never 'shorten'"* and **"never trim earned content to clear one."** These are the deepest pages in the wiki — `annie-ulmer` at 143KB, `master-timeline` at 662KB — and depth is the binding constraint the whole project is fighting for. The only legitimate response is to ask whether *navigation* into the page has broken: are there headings, is it reachable, does the domain index describe what is in it. If navigation is fine, the warning has done its job by making you look. Record that you looked; change nothing.

**`index is NNKB (budget NNKB) — likely session noise`**** (3 indexes).** This one is usually **real**. An index is navigation, not content, so it has no earned prose to protect. Growth here is typically a pass appending entries without pruning. Tighten the phrasing, group by domain, keep every link.

**`bare '## Related' footer — convert to Connections`**** (65 pages).** Real work, and the largest standing campaign in the repo — but it is **not** a mechanical find-and-replace, and treating it as one is how you get 65 empty edges. A typed connection carries a `claim:` stating *what is true across the two pages* (`CONNECTIONS_SPEC.md`), and a claim you have not earned by reading both pages is worse than the bare list you replaced, because it looks like knowledge. Work these a few at a time, from pages you have just read anyway. Converting three with real claims beats converting thirty with "these are related."

The general rule underneath all three: **a warning is a request to look, not an instruction to change.** Deciding a warning is correct-as-is and recording that decision is a complete and successful outcome.

## Step 2 — stale premises, which are never mechanical

`bin/wiki-climb check` reports pages whose `synthesizes:` members have moved underneath them. This is the item `CLAUDE.md` names as *the one move that corrupts the system quietly*:

**Never clear a stale warning by bumping a date.** Re-read the premise that moved, decide whether the conclusion survives, record the decision.

So for each one: open the member page that moved, find *what* changed in it, and ask whether the synthesis still follows. Three honest outcomes, all fine:

- **Survives.** Write a `> **RE-CHECKED [date]** — premise moved, conclusion unaffected` block saying which page moved, what changed in it, and why the conclusion is untouched. The existing blocks on `the-cool-metric` and `single-channel` are the house pattern — note they name the specific claim that did *not* change, which is what makes them re-checkable later.

- **Narrows.** The conclusion holds in weaker form. Say so, restate it weaker, and strike the part that died.

- **Falls.** Retract it, in the open, per STYLE_GUIDE rule 9 — old claim visible, evidence that killed it beside it. A synthesis that turned out to be wrong is a finding worth more than the synthesis was.

The tell that this step was skipped is a `date_modified` that moved with no prose change. If you find one, that page's staleness was cleared without being resolved and it needs redoing.

## Step 3 — the sweeps that require reading

These have no tool and are the reason this is a skill. Do not attempt all of them every pass; pick by what the repo has been doing lately.

**Contradictions between pages.** `bin/wiki-digest` counts them (43 today) and `DIGEST.md` lists them. A held `> **CONTRADICTION:**` is not a bug — the repo deliberately holds two first-hand accounts open rather than settling them by seniority. What you are hunting is the *undeclared* kind: two pages asserting incompatible things as plain fact, neither aware of the other. Those get a contradiction block on both, or resolution against a primary source.

**Claims superseded by newer raw.** When an ingest lands, pages that reasoned from the older version of that material do not update themselves. Check pages whose `sources:` include a file that has since grown or been re-exported. The canonical case: a people page built from a partial CSV whose count was a `wc -l` line count rather than a record count.

**Entities mentioned 3+ times with no page.** Grep candidates out of `wiki/`, then judge — a name appearing three times in one page's prose is not a person the wiki owes an entry, but a name appearing across three unrelated domains usually is. Add the strong ones to `queue.md`; do not create thin stubs, which `CLAUDE.md` treats as a v1 failure mode.

**Broken links and orphans.** `bin/wiki-lint` catches these as errors, so by step 0 they are already fixed. Worth naming only so you do not go hunting for them by hand.

## Step 4 — drain the obligations

`bin/wiki-work` splits **obligations** (somebody or something is waiting) from **standing work** (hundreds of queue entries, worked by choice). Housekeeping drains obligations, from the top; it does not try to empty the queues.

`bin/wiki-work next` names the top item and the operation that clears it. The operations live in `CLAUDE.md`: a parked `sage/` question is an **ANSWER**, a staged operator answer or sage finding is a **CLOSE**, a stale premise is step 2 above. Each is a real pass over a real page — integrate the material into the argument where it belongs, cascade the correction into every page that inherited the gap, *then* bump `date_modified` and clear the flag.

Two things to hold onto here. **Clearing means integrated, never discarded** — a staged answer that was checked and rejected must not look the same from outside as one nobody acted on, so if an answer turns out to be wrong against a primary source, write that up and clear the flag anyway. And **nothing in ****`WORK.md`**** can be ticked off**: every row is a live condition recomputed on each run, so an item leaves the list when the thing it describes changes, not when you say it did.

If you drain none of them because the operator asked for something else, that is fine — but say so in the handoff with a reason, per `CLAUDE.md` step 5. Silence is the one option that is not available.

## Step 5 — write the pass down

Housekeeping that leaves no record is housekeeping nobody can build on.

**`log.md`**** — as findings, not activity.** The house style is *what was wrong, what the evidence was, what changed*. "Ran the gates, fixed some warnings" is worth nothing to the next session. "The `master-timeline` size warning is correct and the page should stay 662KB; navigation into it is via `index.md` only, which is the actual gap" is worth something.

**`BACKLOG.md`** takes what you found and consciously did not do. A queued item with a sentence of reasoning is a decision; an unqueued one is an omission.

**`LLM_HANDOFF.md`** gets the exact resume point — what you swept, what you deliberately left, and the first thing the next session should open.

Then `bin/wiki-check` once more and commit as `lint: <what you actually found>`.

## What a good pass looks like

Narrow and honest beats broad and shallow. A pass that re-checked two stale premises properly, converted four `## Related` footers with claims it earned by reading both pages, decided six size warnings were correct and said why, and closed one staged answer with its cascade — that is a strong pass, and it is maybe a quarter of the open items.

The anti-patterns, all of which look productive:

- Trimming pages to clear size warnings. Destroys the thing the project exists to accumulate.

- Bumping `date_modified` to clear staleness. Corrupts quietly and is hard to detect later.

- Converting `## Related` footers into typed edges whose claims are "these are related." Fills the graph with edges that assert nothing.

- Creating stub pages to clear "entity with no page." Thin pages are the failure mode v1 died of.

- Reporting the sweep as done when the obligations were not touched and the handoff does not say so.
