# PLAIN_AGENT.md — running the READER'S DIGEST campaign on a cheap model

This file is the operating manual for pointing a **weak, fast, cheap coding agent** at the `plain/` backlog and letting it run unattended. It is written for a model that will forget the rules between turns, will not go and read a spec, and — asked whether its own output is slop — will say no.

So none of the quality control here is advice. All of it is arithmetic, in `bin/wiki-plain audit`, wired into `bin/wiki-check` as a gate. The agent cannot commit past it, and cannot argue with it. That is the whole design: **the model is the writer, the tool is the editor, and the tool has the last word.**

Humans and strong models writing twins should read the TRANSLATE operation in `CLAUDE.md` instead. This file is the reduced, mechanised version of it.

## Two lanes, and this file is the free one

Two writers work this backlog at once and they are not interchangeable. The split is arithmetic in `bin/wiki-plain` rather than a convention either is trusted to remember, because the failure mode of a convention here is both of them translating the same page and neither noticing.

| **Lane** | **What is in it** | **Who** |
| --- | --- | --- |
| `major` | 900 words and up — the dense findings | a strong model, following `CLAUDE.md`'s TRANSLATE operation |
| `free` | 300 to 899 words, **worked smallest first** | a weak unattended agent, following this file |

**Everything below is the free lane.** Pass `--lane free` and the tool will not hand out anything else — including if you name a page yourself, which it refuses with the lane and the page's length in the message.

Three things are in neither lane and no agent should go looking for them: entries about other people, generated pages (`page_type: dataset`), and entries under 300 words. The reasoning for each is in `plain/DECLINED.md`. The counts are on `wiki/meta/readers-digest`, so work held back is visible as held back rather than looking like work nobody got to.

The ordering is the part worth understanding. The free lane runs **smallest first** on purpose: a weak model's failure on a long page is silent. It returns a fluent, confident summary of the first three paragraphs, which reads fine, passes every arithmetic rule the referee has, and is the one defect `audit` structurally cannot see. Keeping the lane on pages that fit in one context is what stops that happening, and it is why the lane is not simply "the rest of the backlog".

## The one-command loop

Everything the agent needs for one page comes out of one command, including the rules and the full text of the page:

bin/wiki-plain task --lane free     # the free lane's next page — smallest first

bin/wiki-plain task --lane major    # the major lane's next page — densest first

bin/wiki-plain task <slug>          # a specific page

bin/wiki-plain next --lane free 10  # look at the queue without claiming anything

`task` picks the page, scaffolds `plain/<slug>.md` with the frontmatter already correct, prints the rules, and prints the whole source page. It **refuses** a page withheld under the standing moratorium in `CLAUDE.md`, and it never proposes one.

Then the agent writes the file, and:

bin/wiki-plain audit <slug>         # the referee. FAIL lines are instructions.

Fix every `FAIL`, run it again. On `PASS`:

bin/wiki-check                      # all gates, including the audit

git add plain/ && git commit -m "translate: <slug>"

That is the loop. One page per run, start to finish, then stop.

## The prompt

Paste this verbatim as the agent's task. It is deliberately short — a long prompt is a prompt a small model stops following halfway down.

You write plain-English versions of technical wiki pages, one page per run.

Run this and read ALL of its output, including the page at the bottom:

bin/wiki-plain task --lane free

It tells you which file to write and prints the rules. Follow them exactly.

Write the file. Then run:

bin/wiki-plain audit <slug>

Every line starting with FAIL is an instruction. Do what it says and run the

command again. Repeat until it prints PASS.

When it prints PASS:

bin/wiki-check

git add plain/ && git commit -m "translate: <slug>"

Then STOP. Do not start another page in this run.

HARD RULES — breaking any of these is worse than doing nothing:

- Write exactly one file: the plain/... path the task named. Nothing else.

- NEVER create, edit or delete anything under wiki/, raw/, or bin/.

- NEVER use a number that is not in the page you were given.

- NEVER change source_modified: in the file. It is already correct.

- If audit still FAILs after 3 attempts: delete the file you were writing,

print one line saying which page you gave up on and why, and stop.

- If any command errors, or the page is refused, stop and report. Do not

improvise, do not pick a different page, do not edit the tool.

## What the referee actually checks

`bin/wiki-plain audit` fails a twin on any of these. Each message says what to do about it, because the agent will paste the message back to itself as its next instruction.

| **Check** | **Why it exists** |
| --- | --- |
| **Fabricated numbers** | A quantity in the twin that appears nowhere in the page. This is the load-bearing one: a number reads as proof, so inventing one manufactures evidence. Single digits are exempt (prose counts things); spelled-out source numbers and `2011-12` year shorthand are resolved first, so only real inventions fail. |
| **Apparatus leaked** | `[[wiki/...]]`, `raw/` paths, `knowledge:`, typed-edge vocabulary. Machinery for maintaining the wiki, not part of the finding. |
| **Filler phrases** | "it's important to note", "a rich tapestry", "plays a crucial role", "in conclusion", "delve into" and friends. Every one carries no claim, and a twin is 100% claims. This is the house style of a model writing to fill space. |
| **Missing the honest half** | The page states its gaps or falsifiers and the twin does not. A reader shown only the confident half is being sold something — and this edition reaches the readers least equipped to notice. |
| **Too short** | Under 18% of the page. That is a summary. A twin is the same finding at the same altitude, not an abstract. |
| **Too hard to read** | Flesch-Kincaid above 12.5. The whole point is a reader who has never been here. |
| **Unfilled template** | A scaffold prompt left in the file. Half-written work blocks the gate on purpose. |
| **No pointer back** | The twin must tell the reader the full entry exists and carries the sources. |
| **Stale / orphaned / forbidden** | From `bin/wiki-plain check` — the twin's page moved, vanished, or is withheld. |

Two are warnings rather than failures: a twin that keeps under 25% of the page's figures, and one barely shorter than its page. Both mean "look at this", neither means "wrong".

## Scheduling it

The loop is deliberately **one page per invocation**. Do not build a wrapper that translates twenty pages in a single agent run: a small model degrades across a long session, and the failure is silent — page twenty is slop and page one was fine. One page, one commit, fresh context.

Cron, every 20 minutes:

*/20 * * * * cd /path/to/wiki-brain && /usr/local/bin/your-agent \

--prompt-file PLAIN_AGENT.prompt >> /tmp/plain-agent.log 2>&1

A shell loop with a pause is equally good and easier to stop:

while :; do

cd /path/to/wiki-brain || exit 1

git pull --ff-only

your-agent --prompt-file PLAIN_AGENT.prompt

bin/wiki-plain status | head -8

sleep 300

done

**Before scheduling anything, satisfy these three:**

1. `bin/wiki-plain report` shows work outstanding in the free lane. When the lane empties, `task --lane free` says so and the loop has nothing to do.

1. The agent runs on a branch, not `main`, and a human merges. The gate stops slop; it does not stop a plausible-but-wrong reading, and nothing mechanical can.

git checkout -B plain/free-lane origin/main

One branch for the campaign, one PR, commits appended as they land. Not a branch per page: twenty branches is twenty merges, and the point of the lane is that the work is uniform enough to review in batches.

1. You have read the first three twins it produces, in full, yourself. The audit tells you the twin carries the page's numbers. It cannot tell you the twin carries the page's *argument*. That check is yours and there is no substitute for it.

## Reporting

There is nothing for the agent to report and nothing for it to update. Progress is **derived**, not filed:

bin/wiki-plain report      # coverage, both lanes, and who wrote what

It reads the tree for coverage and the git log for attribution — by the author of the last commit to touch each twin — and regenerates `wiki/meta/readers-digest`, which the portal serves like any other entry. So the campaign is legible from a phone without anybody maintaining a ledger, and an agent that forgets to report has still reported, because its commits are the report.

Two consequences worth knowing:

- **The page is generated.** A hand-edit fails `bin/wiki-plain check`, which gates in `bin/wiki-check`. The fix is to rerun the tool, never to edit the page.

- **Attribution needs a full clone.** A shallow clone's log does not reach the commits that wrote most twins; the tool says so rather than publishing a wrong number. `git fetch --unshallow` if the writer column is missing.

The commit message is the one thing the agent must get right, because it is what the report and `bin/wiki-history` both read:

translate: <slug>

## What this cannot catch, and what to do about it

The referee is arithmetic. It will pass a twin that is faithful on every number and wrong about what the page means — a reversed causal direction, a hedge dropped, a conclusion stated more confidently than the page states it. Those are exactly the errors a cheap model makes most.

So: **spot-check on meaning, not on mechanics.** Pick one twin a day, read the page beside it, and ask only one question — *does the twin claim anything the page does not?* If yes, that is the finding; fix the twin, and if the same shape recurs, add it to the audit so it stops recurring.

A page that cannot be translated honestly is not translated. If the only way to write it is to leave out something that changes what the page says, the agent should delete the file and say so. That is a legitimate outcome and it is recorded in `plain/DECLINED.md` when a human confirms it.

## The moratorium

Non-negotiable and not the agent's to reason about. `CLAUDE.md` carries a standing operator directive about a living person. `bin/wiki-plain` enforces it as two mechanical rules — a page substantially about her gets no twin, and no file under `plain/` may name her at all — and `tests/test_wiki_plain.py` pins both. `task` and `new` refuse; `next` never proposes; `check` fails.

If an agent ever reports that it "worked around" a refusal, stop the loop and read what it wrote. Only the operator lifts any of this.
