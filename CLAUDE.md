# Personal Wiki — second brain

A custom wiki system that aims to be as exhaustive and detailed as possible about its creator, Dan Frank: biography, history, cognitive traits, ideology, tendencies, and every other datapoint that points back to the real person. It fills knowledge gaps as they are found and updates as time passes.

**This file governs process — the operations and how to run them.** Read it with the rest of the governing set. When any two disagree, the "wins on" column decides.

| **File** | **Governs** | **Wins on** |
| --- | --- | --- |
| `STRATEGY.md` | what we're doing and why; the core loop | intent |
| **CLAUDE.md** (this file) | the operations | process |
| `EXTRACTION_SPEC.md` | how deep to mine a source before writing | depth |
| `STYLE_GUIDE.md` | page format and the substance standard | format |
| `CONNECTIONS_SPEC.md` | typed edges and their claims | edges |
| `SYNTHESIS_SPEC.md` | altitude — how conclusions stack | climbing |
| `WORK.md` | what is outstanding, and in what order | sequence |
| `skills/INDEX.md` | what agents have learned about *changing* this repo | technique |

`BACKLOG.md` = standing work. `LLM_HANDOFF.md` = the exact resume point. `skills/` = durable technique, and it is subordinate to every row above: a skill operationalizes policy and never overrides it.

## Start and end every session here

**At the start of every session, read ****`LLM_HANDOFF.md`** to understand current state, recent changes and immediate priorities. **When you end, update it** — what you accomplished and the exact focus for the next model. This is what makes the work continuous across sessions and models.

**Then run ****`bin/wiki-work`****.** It is the one list, it is mandatory, and it is not optional reading. Outstanding work used to live in six files and two frontmatter flags, every one of which relied on somebody remembering to look; a session that read four of the six was indistinguishable from one that read all six. This aggregates them and separates the two kinds:

- **Obligations** — a red gate, a question parked by the portal, an answer staged on a page, a synthesis whose premise moved under it, a portal edit nobody normalised. Somebody or something is waiting on each one. There are usually a handful. A failing gate sits above all of them because it blocks every commit; on 2026-08-21 `bin/wiki-connect check` sat red on `main` with 70 errors after a portal save deleted 56 typed-edge claims, and nothing surfaced it, because nothing had to.

- **Standing work** — the ingest queue, the mined edge and cluster candidates, the backlog. Hundreds of entries, worked top-down by choice rather than drained, each in the file built for it.

**The order is fixed, and step 4 is the one that gets skipped:**

1. read `LLM_HANDOFF.md` and `operator-log.md`

1. run `bin/wiki-work` — see what is outstanding *before* you start

1. **do what the operator actually asked for**, in full

1. **then come back and drain the obligations, from the top**

1. anything still outstanding goes into `LLM_HANDOFF.md` with a reason — never silently

**Before you change anything mechanical, run ****`bin/wiki-lessons route "<what you are about to do>"`****.** `LLM_HANDOFF.md` says where we are and `WORK.md` says what is owed; `skills/` says *how not to break this repository doing it*, and it is the one of the three that is about technique rather than state. The router names the skills whose triggers intersect your surface and you load those — it is step 2 of `skills/INDEX.md`'s routing algorithm, run rather than remembered.

This is a real step and it was inert until 2026-08-30. The section shipped declaring "mandatory session behavior" while this file — the only file that can make anything mandatory here — did not mention it, so nothing loaded it and nothing checked it. That is precisely the defect `bin/wiki-work` was built to end, arriving again in a seventh file: a corpus of instructions that relies on somebody remembering to look is one that a session can skip without the skip being visible. It now gates (`bin/wiki-lessons check`) and its unvalidated candidates surface as obligations.

**At the end, write back what you learned.** If the session exposed a repeatable failure mode, a hidden invariant, a command sequence that prevents a recurring failure, or a trap specific to this repository, that is a skill — see the LEARN operation below. A lesson that stays in the session transcript is a lesson the next agent pays for again.

That order is deliberate in both directions: the operator's request never waits behind the queue, and the queue never waits on somebody noticing it.

**Nothing in ****`WORK.md`**** can be ticked off.** Every row is a live condition recomputed on each run — there is no ledger, no checkbox and no `done` command, because a list that can be marked complete independently of the thing it describes is a list that can lie, and the first lie it would tell is that a question somebody is waiting on has been answered. An item leaves the list when what it points at changes. Record what you did in `log.md`, as always.

`operator-log.md` and `bin/wiki-gaps pending` still exist and are still worth opening: the log is the durable half — append-only, survives `clear`, and records what was *already* integrated so a session can tell a fresh answer from an old one without reading git history. `bin/wiki-work` will not let you miss that there is one; the log tells you its history.

## STANDING DIRECTIVE — the Annie moratorium (2026-08-23, operator)

**we are trying to date ally so stop writibg that in textibg annie**

The operator's instruction, verbatim in substance: *we can no longer include texts or any narrative anything about Annie, due to the unpredictable nature of her situation and the apparent danger she is in.* This is a safety directive about a living person, not an editorial preference, and it outranks every priority elsewhere in this file — including `queue.md`'s CRITICAL row, which stood for weeks telling each session that the next 212 export was the highest-value pending ingest. That row is closed. So is every other standing instruction that would have pulled Annie messages in.

**What is forbidden, from today:**

- Filing any new Annie message export, metadata dump, group-chat export or screenshot into `raw/` or `inbox/` — including exports already named in `queue.md` or `BACKLOG.md` as pending.

- Writing any new narrative, event, timeline entry, synthesis, typed-edge claim or dated line about Annie, or extending an existing one past what the wiki already says.

- Quoting any Annie message not already quoted on a page.

- Answering a `sage/` question with new Annie material. A question that can only be answered that way is answered from what the wiki already holds, or it is declined with this directive as the stated reason.

**Where it is enforced mechanically.** `bin/wiki-plain` — the READER'S DIGEST layer — holds this directive as code rather than as something a session has to remember, in two rules. A page substantially about her gets no plain-language twin at all (`new` refuses, `next` never proposes it, `check` fails if one appears); and **no file under ****`plain/`**** may name her at all, whatever its source page says.** The second rule is the guarantee: the first draws a line somebody could argue about, and the second means no new prose about her enters that layer regardless of where the line fell. A plain-language retelling adds no facts, but it is new writing about her, rebuilt to be read by people who could not read the original, and published on a public site — squarely what this directive stops. The pattern and the threshold are `MORATORIUM` and `INCIDENTAL` at the top of that file, and `tests/test_wiki_plain.py` pins them. Only the operator changes either.

**What is unchanged, and must stay unchanged:** every existing Annie page. This directive is a stop, not a retraction and not a redaction. Nothing already written is deleted, softened or rewritten, because the operator asked for nothing to be done differently — only for the record to stop advancing.

**Where the record stops.** The wiki's account ends at the last contact it already states — **2026-08-19, 15:15:33**, the last message on `wiki/people/annie-ulmer.md` (`date_range_end: 2026-08-19`). Treat that as the current state of the world: *Dan has not spoken to Annie since the last date the wiki records.* Do not date-check it against an export, do not "confirm" it, and do not bump it. If a source you are reading for some other purpose runs past that date on this thread, stop reading at it and take nothing from beyond.

An export was uploaded to a session on 2026-08-23 that runs past that date. It was **not** filed to `raw/`, not copied into the repository, and nothing was derived from it — deliberately, under this directive. That is the correct handling of the next one too.

## The four things that matter most

1. **Depth is the binding constraint.** There are 438 pages; there are not enough *details on them*. A pattern can only be found among details that were written down, and synthesis reasons from `wiki/`, not `raw/` — so anything dropped at extraction is a connection nobody can ever make. Read sources to exhaustion, write long, keep the mundane. `EXTRACTION_SPEC.md`.

1. **Findings get written back — and so do mentions.** A conclusion that spans several pages is written into *each* of them as a typed edge whose claim states the finding, not left on one page for the others to rediscover: `STRATEGY.md`'s core loop, step 6, and the step most often done partially. **The mention is the half nobody notices is missing.** When a source names a person, work, place or concept that already has a page, that page is owed the evidence *before any finding exists* — core loop step 3, `EXTRACTION_SPEC.md` move 9, the CROSSLINK operation below. It has no symptom when skipped: the page you wrote reads as complete, and the page you did not touch cannot discover that a source is talking about it. Nineteen twitter year pages were written by reading every tweet in every year and still left the concert record, a health row, an alias's discography and a person's whole page untouched by what those tweets said about them.

1. **Never clear a stale warning by bumping a date.** Re-read the premise that moved, decide whether the conclusion survives, record the decision. This is the one move that corrupts the system quietly.

1. **Every conclusion is checked against the person before it is written.** A pattern found across N pages is a fact about those N pages until it has been read against Dan's cognitive stack, measured personality profile, historical precedent, attitudes and the forces acting on him, his current security and prosperity, health, romantic state, age and upbringing, geographic and ethnic culture, religious or ideological programming, and axiomatic politics. This is **the constitution pass**, it is mandatory and deterministic rather than a matter of judgment, and its eleven registers and worked failure case are in `SYNTHESIS_SPEC.md`. A rule that survives it is stronger; a rule that only survives by not looking is not a finding.

**Registers 1, 2 and 11 are weighted, not merely consulted.** They name the cognitive stack, the measured personality profile and the political axioms — and a page states a score without saying how much weight a conclusion may put on it, so the pass could be run honestly and still rest the whole argument on a trait nothing has corroborated. `bin/wiki-traits assess <trait>` answers that before you lean on one, and `SYNTHESIS_SPEC.md`'s trait-filter table says what each cell obliges. As of the first run **seven traits are load-bearing across the corpus and none is currently measurable** — four have no reviewed proxy, three had every proxy read and found to catch something else. That is a fact about the instrument, not about Dan: **silence is not falsification**, and it constrains what a synthesis may claim rather than what is true.

## Architecture — plain files, one direction of flow

inbox/  →  raw/  →  wiki/  →  caakehorn/home public/wiki/   exports/ (generated,

typed &     immutable   compiled    derived snapshot, never edited            disposable)

uploaded    source      knowledge      ▲             │

▲                │       │             │  a question is asked

│                ▼       │             ▼

│             plain/ ────┘   sage/questions/ ◄──────┐

│        the same finding,    parked until a        │

│        in plain English     session answers it    │

└──────────────────────────────────────────────────┘

the answer is filed to raw/ and staged

onto every page it cites

One loop closes here that no other operation closes: a question comes *in* from outside the repository, and the work of answering it goes back into `raw/` and `wiki/` as new material. The corpus is bigger after a question than before it.

- **`inbox/`** — staging. Material arrives via `bin/capture` or by being dropped in. On ingest, MOVE the file to the right `raw/` subdirectory, then synthesize. Never leave a file in both.

- **`raw/`** — immutable source archive, organized `raw/<domain>/<collection>/`. Never modify or delete anything here except when filing from `inbox/`. **`raw/self/context-core/CONTEXT_CORE_EXPANDED.md`**** is the primary authoritative source for facts about Dan** — curated, internally cross-checked, explicit about its own gaps. Check it first on any self/mind/timeline topic; treat other sources as supplementary or corrective to it unless they carry a specific dated correction it lacks. Source tiers and per-source traps: `EXTRACTION_SPEC.md`.

- **`wiki/`** — the compiled product: accumulated understanding, not a cache of `raw/`. Domains: `self`, `timeline`, `people`, `mind`, `work`, `interests`, `health`, `places`, `legal`, `meta`. Add a domain only when several pages clearly don't fit an existing one. `meta` (added 2026-08-26) is the wiki describing itself rather than Dan: `wiki/meta/journeys/` holds curated cross-domain reading paths (`page_type: journey`, `STYLE_GUIDE.md`), and `wiki/meta/{digest,recent-activity,open-questions}.md` are on-site mirrors of `DIGEST.md`/`RECENT.md`/`OPEN.md`, regenerated by `bin/wiki-digest` — the mirrors exist because the portal's sync only reads `wiki/**` and `sage/questions/**` (see the portal bullet below), so a root-level file is otherwise invisible on the live site. `wiki/**/archive/` holds pinned oversized artifacts (`status: archived`) — exempt from budgets, never updated.

- **`plain/`** — the **READER'S DIGEST** layer: one plain-language twin per page, mirroring `wiki/`'s tree exactly (`plain/mind/synthesis/fayette-return.md` is the twin of `wiki/mind/synthesis/fayette-return.md`). The portal serves the pair as two editions behind one switch in the header. A twin is a **rendering of a page, not a page**: no typed edges, no `synthesizes:`, no Gaps, no index entry, nothing to cite — so no synthesis can ever reason from a simplification instead of from the finding. It lives outside `wiki/` for that reason and because `bin/wiki-lint` globs `wiki/**` and would otherwise double the page count and orphan-warn forever. Called `plain/` rather than `digest/` because `bin/wiki-digest` and `DIGEST.md` already exist, mean something entirely different, and *write files*. See the TRANSLATE operation below and `bin/wiki-plain`.

- **`sage/`** — questions put to the wiki **from outside it**. The portal has a question box; anyone through the door can ask something about Dan and the question lands in `sage/questions/` as a file. Nothing answers it automatically — there is no model behind the box and no workflow that calls one. It is parked, `bin/wiki-work` lists it at priority 1, and a session answers it properly. Not in `raw/` because these files mutate (`pending` → `answered`); the immutable artifact is the capture written to `raw/self/sage/` at answer time. See `sage/README.md` and the ANSWER operation below.

- **`intake/`** — the **intake ledger**: a finite quantity enters the record, every known disposition of it is recorded after that, and at depletion the ledger reconciles what is known and preserves what is unknown. `events.jsonl` is an append-only log and the source of truth; `units.json` is a projection regenerated from it and safe to delete; `substances.json` is the select box. Its point is not dose-counting — it is the anti-unreliable-narrator layer, a first-party dated dataset to set against a page's narrative the way `bin/text-metrics` is set against a page's claims about how he writes. **⚠ Its data is TRACKED, in a public repository** — `intake/events.jsonl` and `intake/units.json` are readable by anyone, permanently, and git history cannot be un-published. That is an operator decision taken on 2026-08-30 knowing what it publishes, after two arrangements that each defeated the ledger's purpose: gitignored kept the record out of reach of every session that might cite it, and sealed (`bin/intake seal`, AES-256-GCM) kept the analysis layer from reading it too. **A ledger the wiki cannot open has no reason to be here.** To reverse: make the repo private FIRST, verify it, and only then decide whether ignoring the files is still wanted — in that order, always. The sealing machinery still works and is one commit away. Note what `.gitignore` never covered: it governs `git add` only, so it never touched GitHub's contents API, which is how both the portal and ボスの部屋 write from a browser.

**The public face is ****`wiki/health/intake-ledger.md`** — the ledger rendered as a wiki entry, generated by `bin/intake page` and served on the portal like any other page, because the portal's sync reads `wiki/**` and nothing else. It is **evidence, not a claim**: every unit, every event and every correction, stating no finding. A finding drawn from the ledger still reaches an ordinary page through the normal operations — never the generated one, which is overwritten on every write. It is gated on drift and it deliberately withholds `report`'s per-unit `Rate of consumption ... g / day`, which extrapolates a unit's quantity across a full day from however long that unit lived and is not a daily figure.

**The analysis surface is ****`intake/SUMMARY.md`**** and ****`intake/units.json`** — both generated on every write, both committed, and both there so a session can reason about intake without parsing JSONL or reimplementing the arithmetic. **Read the coverage figure before quoting any mean from them.** A finding drawn from the ledger still reaches a page through the normal operations, cited to a unit id and a date range with its coverage attached — never as a bare mean.

- **`testimony/`** — the **testimony veracity ledger**: every first-person assertion the corpus has recorded, what settled it, and the arithmetic over the settled ones. `events.jsonl` is an append-only log and the source of truth; `testimonies.json` is a projection regenerated from it and safe to delete; `SUMMARY.md` is the analysis surface. **It is the missing half of CLOSE.** That operation already says an operator answer is T0 testimony rather than proof and must be checked against `raw/` where it can be — and the wiki has been doing that for months, landing each result as a blockquote on one page and then forgetting it. Page 41 has no idea that the same person's date claims came back eight weeks early on page 12, so the next answer is weighed exactly as credulously as the first. This is where the result of the check is kept. **Two numbers, and collapsing them would be a lie**: *veracity* is how often he turns out to be right, *calibration* is whether his own stated confidence tracks that — and only the second makes an **unproven** claim assessable, because an unproven claim offers nothing to check but the class it belongs to and the confidence it arrived with. **`unfalsifiable`**** scores zero and never negative**: punishing him for the archive's gaps would make the number a measure of the corpus rather than of the man. **⚠ Like the intake ledger it is TRACKED, in a public repository**, and the same reversal order applies — private first, verify, then decide. `testimony/README.md`.

**The public face is ****`wiki/meta/testimony-veracity.md`** — generated by `bin/wiki-testimony page` and served on the portal like any other page. It is **evidence, not a claim**: every record, every adjudication and the arithmetic, stating no finding. A finding drawn from the ledger reaches an ordinary page through the normal operations, never the generated one, which is overwritten on every write. It carries its own sample bias in a section that cannot be dropped — the standing directive filters the record, and a score drawn from a filtered sample that does not announce the filter is worse than no score.

- **`claims/`** — **the claim validity ledger: what was true, when it stopped being true, and what the wiki still asserts anyway.** Same shape as the two above — `events.jsonl` is the append-only record, `claims.json` a regenerable projection, `SUMMARY.md` the analysis surface. **It fills a hole under the load-bearing beam.** Every date field in this repository is about the *page*: `date_created` and `date_modified` say when the file moved, `date_range_*` says what span of evidence it covers. **Nothing said when an assertion stopped being true**, so nothing could notice when one did — and the whole case for a second brain over a RAG is that today's conclusion is tomorrow's premise. A premise that quietly expired keeps reading as present tense and keeps getting cited. `bin/wiki-climb check` fires when a premise *file* is edited; it cannot fire when a premise *lapses*.

**Three ways a claim stops being usable, and collapsing them is a lie.** *Retracted* means it was never true — `RETRACTED.md` owns that, and `bin/wiki-lint` already fails if one reappears. *Corrected* means it was wrong when written — STYLE_GUIDE rule 9's blockquotes own that. *Expired* means it was true and then it stopped, and **nothing owned it.** The third is not a weaker version of the first two: *Dan lives in Morgantown* was **correct** in 2019, so retracting it says the wiki got it wrong and leaving it says he lives there now.

**`ended`**** is not ****`lapsed`****, and that distinction is the whole instrument.** `ended` means the state stopped and something *dates* the stopping. `lapsed` means the **record** stopped and the ending is unknown. `bin/wiki-traits` already refuses to read an instrument's silence as falsification; this is the same refusal one layer down, because **a corpus going quiet is a fact about the corpus.** So a lapsed claim carries `last_seen` and never `valid_to`, `asof` reports it as *unsettled* rather than false, and the gate fails on a lapse that has acquired an end date. **c004 is the worked case**: MOGZART lapsed in March 2016 and the page carried it as an "archive/revival candidate" for a decade, then he posted a jump-up DnB remix under the same name on 4 March 2026. A ledger that had recorded the silence as an ending would have been wrong about the world.

**Never extend a window to clear a ****`scan`**** hit** — that is rule 3 of "the four things that matter most" wearing a different hat. If the record stopped in 2016 the claim lapsed in 2016, whatever the page's `status` field says. An honest `unknown` beats a confident `active` nothing checked. **⚠ TRACKED, in a public repository**, on the same terms and with the same reversal order as the two ledgers above. `claims/README.md`.

**The public face is ****`wiki/meta/claim-validity.md`** — generated by `bin/wiki-claims page`, served on the portal like any other page, and **evidence rather than a claim**: it records windows and states no finding. What a window *means* is synthesis, and synthesis happens on an ordinary page. It carries its own sparsity in a section that cannot be dropped — the ledger is opt-in, so a claim absent from it is **unexamined, not timeless**, and reading its counts as coverage of the corpus is a category error.

Four interfaces over one code path: `bin/intake`, Special:Intake in the local app, `/ledger` in the portal, and ボスの部屋 (`boss.html` in [`caakehorn/leviathan`](https://github.com/caakehorn/leviathan)) — the last two are the ones in his pocket, and therefore the ones most of the record will arrive through. Both write `intake/events.jsonl` directly through the contents API, byte-compatible with what the CLI appends; merges are set union by event id, so no two devices can lose each other's work. `intake/README.md`.

- **`lexicon/`** — **the personal dictionary, and the one layer of this wiki that counts instead of choosing.** `lexicon/words/` is a capture path written from the portal — a word Dan wants kept, with his own one-line gloss; it existed from 2026-08-27 with one file in it, was named in `.github/workflows/notify-portal.yml` and **nowhere else**, and so nothing ever surfaced it and nothing ever drained it. `lexicon/measured.json` is the projection: every word, bigram and trigram in his sent messages scored against the ones he received, plus the two registers he writes in and a per-year rate series. Regenerable and safe to delete, but committed, because `mine` takes ~90 seconds over four corpora and a gate that slow is a gate people switch off.

**Its point is that the other two lexicons are not measurements.** `wiki/interests/language/vocabulary-lexicon` holds 200 words Dan *selected*; `wiki/interests/language/personal-lexicon` holds ~25 an assistant *recalled* — and that page's central term turned out not to exist in the archive, while its own first version published mixed-voice `grep` counts as usage counts. Selected, recalled, counted are three different questions, and only the third can catch the first two being wrong. **The public face is ****`wiki/interests/language/measured-vocabulary`**, generated by `bin/wiki-lexicon page` — evidence, not a claim, like the intake and testimony ledgers; a finding drawn from it reaches an ordinary page through the normal operations.

- **`skills/`** — the two-layer agent-skills subsystem, with **one tool per layer, and they are not the same tool.**

The prose half is the **cross-agent operational memory**: what agents have learned about *changing* this repository, as opposed to what the repository knows about Dan. One instruction per file under a domain (`skills/repo/`, `skills/corpus/`), each carrying its trigger, the failure it prevents, and the command that validates it. `INDEX.md` is **generated** by `bin/wiki-lessons scan` — it used to carry a `Status` column duplicating each skill's own `status:` frontmatter, which is two sources of truth for one fact and the exact defect `WORK.md` exists to not have. `INBOX.md` holds candidates that are not yet validated; `PROTOCOL.md` is the lifecycle; `CHANGELOG.md` is the append-only record of every promotion, and a skill missing from it fails the gate, because an instruction with no dated account of why it should be believed is one nobody can audit. Reach it through `bin/wiki-lessons route "<task>"`, not by browsing.

The other half is **`skills/registry/`****, the cross-model database**: an append-only log of what each model actually *has* — skills, MCP servers, plugin tool links, subagents, harnesses, and this repository's own `bin/` commands — pushed by the model itself, so a session can find out what it is working with instead of rediscovering it. `events.jsonl` is the record; `registry.json` is a projection, regenerable and safe to delete. It is a log rather than a document because several models push from several branches and two appends merge as a set union, where one mutable file would make every concurrent push a conflict whose loser is dropped silently. **`wiki/meta/skills.md`**** is its public face**, generated by `bin/wiki-skills page` and served by the portal like any other page — the database is part of the corpus, not an appendix to it. **⚠ It writes to a public repository**: values never enter it, only names, and the tool refuses a credential shape rather than stripping it. `skills/registry/README.md` and `skills/agents/registry-push.md`.

**The two names.** `bin/wiki-lessons` routes and gates the prose — *lessons* are what agents have learned here. `bin/wiki-skills` writes the registry — *skills* are what a model has. Both landed on 2026-08-30, both were written as `wiki-skills` by sessions that could not see each other, and the second one was renamed on merge because the first was already public at `wiki/meta/skills.md`. They read different data, gate different things, and share no code.

- **`exports/`** — output of `bin/export-corpus`; never hand-edit, gitignored. **`skills/`**** and ****`.claude/skills/`**** are different things and the collision is unfortunate.** `.claude/skills/` holds Claude Code skills — `wiki-rewrite`, `wiki-housekeeping`, `corpus-read` — which are procedures for running one big *wiki operation*, invoked by name by one vendor's agent, and named in this file where that operation is defined. `skills/` is vendor-neutral, is loaded by trigger rather than by name, and holds the small durable lessons about not breaking the machinery — the kind of thing that would otherwise be rediscovered once per model. A procedure for an operation goes in `.claude/skills/`; a lesson about the repository goes in `skills/`. When a lesson is big enough to be a procedure, promote it and leave a pointer.

- **The portal** — [`caakehorn/home`](https://github.com/caakehorn/home) renders this wiki, and its `public/wiki/**` is a **derived snapshot of ****`wiki/`****, not a second copy of it.** A workflow there re-runs the derivation against this repo on dispatch *and every five minutes (nominally)*, deleting the directory and rebuilding it, so **anything written into ****`public/wiki/`**** is destroyed within minutes** — including a change that merged. If a session finds itself editing a page as JSON, it is in the wrong repository: pages are `wiki/**.md`, here. This is not a style preference; two December 2015 read passes were written into the snapshot and one was reverted 39 minutes after merging (restored 2026-08-17). **How long that takes depends on who made the edit, and the difference is worth knowing.** An edit made *from the portal* — a page saved, a question asked, a word caught — has the site's own browser code behind it, which fires `wiki-updated` at the portal directly and lands in seconds. An edit merged *here*, as a pull request, used to have no browser behind it and fired nothing, waiting on the portal's own schedule — see the next paragraph for why that stopped being good enough and what replaced it.

`.github/workflows/notify-portal.yml` is this repository's half of the fast path, and it is **live again as of 2026-08-31**, `push:` trigger and all — read the file's own header for the full account, because it is worth reading before touching this again. Short version: it was switched off earlier the same day on the theory that the portal's five-minutely schedule was a good enough backstop on its own. Checked against `caakehorn/home`'s actual Actions history a few hours later, it was not — three consecutive schedule-triggered runs of `sync-wiki.yml` landed at 05:29, 14:13 and 20:07, gaps of 8h44m and 5h54m, not the 5–15 minutes the schedule comment promises. GitHub does not reliably honor a `*/5 * * * *` schedule at that frequency; that is a platform limitation, not a bug in either workflow. **It needs ****`PORTAL_DISPATCH_TOKEN`**** in this repository's secrets — a fine-grained PAT on ****`caakehorn/home`**** with Contents: read and write — which nobody has added yet.** Until it is, the workflow fails loudly (not silently) on the next push touching `wiki/**`, `sage/questions/**`, `plain/**` or `lexicon/words/**`; that is deliberate, and the fix is to add the secret, not to touch the workflow. The five-minutely schedule stays on as the backstop for the fast path's own bad days, which is what it was supposed to be in the first place. **The portal's sync also reads this repository's git log**, not only its working tree: `scripts/build-wiki-history.mjs` there derives every page's full revision history from it, so that checkout runs at `fetch-depth: 0` and the derivation refuses a shallow one rather than publishing "created on the day the clone was cut". `docs/CORPUS.md` §1.5a over there is the format; `bin/wiki-history` here reads the same log for this side.

- **Meta files** (root): `index.md` master navigation · `log.md` append-only operation log · `operator-log.md` append-only ledger of operator additions (written by `bin/wiki-gaps`, never by hand) · **`WORK.md`**** the one outstanding-work list (written by ****`bin/wiki-work`****, never by hand)** · `skills/INDEX.md` the skill routing table (written by `bin/wiki-lessons`, never by hand) · `queue.md` pending-ingest ledger · `connection-queue.md` mined edge backlog · `synthesis-queue.md` mined climb backlog · `BACKLOG.md` standing work. Git is the history mechanism. Commit after every ingest with `<op>: <short description>`. Never commit secrets or `exports/`.

**That convention is now load-bearing twice.** The `<op>:` prefix is what makes the log readable as a record of *operations* rather than of saves, and two things read it that way: `bin/wiki-history` here, and the portal's page-history panel, which shows any reader every version an entry has ever had with the operation that produced it. A commit message that skips the prefix loses that page's row a label on a public site. A commit that bundles an ingest and a lint sweep loses the ability to say which one changed the paragraph. Neither breaks anything; both make the record less useful than it costs nothing to keep.

## Why this is a second brain, not a RAG

A retrieval system keeps the sources and re-derives every answer on demand; it never learns, and yesterday's reasoning is thrown away. This is the opposite. You read a source **once, to exhaustion**, reason out what it *means*, and write that understanding into `wiki/`. From then on you reason **from** the wiki. Knowledge compounds: today's synthesized conclusion is tomorrow's premise.

This has a hard consequence — the wiki is **not** a disposable cache of `raw/`. Two kinds of content live here:

- **Derived** content — message counts, discographies reconstructed from slugs, anything mechanical — is safely regenerable.

- **Earned** content — a thesis, a psychological read, a conclusion cross-referenced from many sources — is the product of reasoning done once. `raw/` does not contain it literally, and re-running the pipeline may not reproduce it. This is the actual point of the system.

So **never regenerate an earned page from scratch — revise it.** When new raw contradicts it, flag and correct; do not bulldoze and re-derive from zero. Pages declare which kind they are with `knowledge: earned | derived | mixed`.

The one sanctioned exception is a deliberate wipe-and-rewrite the operator has asked for, which has its own protocol — see the `wiki-rewrite` skill below.

## The operations

### INGEST — one source per pass, never parallel

**If you are given a general or unspecified instruction to "ingest," "do the Phase B ingest," "keep going on the wiki," or any open-ended synthesis task — read ****`INGEST_RUNBOOK.md`**** first and follow it exactly.** That file is the reproduction-grade instruction for the cross-corpus synthesis pass. Do not improvise the ingest workflow.

Parallel "swarm" ingests destroyed v1 (fragment prose, duplicate entities, wrong statuses). Ingest ONE inbox item per pass, fully:

1. Move it from `inbox/` to the right `raw/<domain>/<collection>/`.

1. **Read it to exhaustion** — not until it answers your question. `EXTRACTION_SPEC.md`.

1. Put quantified data (dates, counts) into tables on the target pages; re-derive every number rather than copying it forward.

1. Write or update every relevant page — typically the domain summary plus every person, event and concept the source touches.

1. Update the domain index and `index.md` if pages were added.

1. Update `queue.md`; append to `log.md`: `## [YYYY-MM-DD] ingest | <domain> | <source>`.

1. Run the three gates; commit.

Large exports (social media dumps, message CSVs) may take multiple passes; track progress in `queue.md` rather than half-finishing silently.

Captured notes may carry `targets: [wiki/...paths]` — a targeted note is a correction or expansion of those specific pages: apply it there first, then file the note into `raw/`. Humans also edit pages directly in the app; those appear in `log.md` as `edit | <domain> | human edit via app` — treat them as authoritative content but normalize formatting and frontmatter on the next pass.

### QUERY

Start at `index.md`, follow domain indexes, answer with citations to wiki pages. Reason **from** the wiki first; re-open `raw/` only when the wiki is silent on the question or a source is newer than the page that used it — otherwise you are re-doing settled work. If the synthesis is new and durable, save it as a page: that is how the brain grows.

### ANSWER — a question put to the wiki from outside it

QUERY is somebody in this repository asking the wiki something. ANSWER is somebody *outside* it doing so — through the portal's question box, which parks the question in `sage/questions/` and promises them an answer. `bin/wiki-work` lists it at priority 1 for exactly that reason: it is the only obligation in this repository where the person waiting cannot see whether anything is happening.

Read `sage/README.md` for the file format. The protocol:

1. **Read the question as asked**, not as you would have preferred it asked. It may be hostile, badly framed, or about something the corpus cannot settle. Answer the question that was typed.

1. **Retrieve properly.** Reason from `wiki/` first, then go to `raw/` for the proofs — `bin/mine-messages` over the message record rather than grep, and the per-contact CSVs where the question is about one relationship. A question about future behaviour is a question about the documented pattern; find the pattern's instances and its counterexamples both. **Then run the constitution pass** (`SYNTHESIS_SPEC.md`) — an answer about what Dan will do, or why he does something, is a claim about a specific mind in specific circumstances, and it is checked against the cognitive stack, the measured profile, the history, the material and health situation, and the ideology before it is filed.

1. **Cite every claim, and quote directly.** This is the standard the whole operation stands on. A sentence about what Dan does cites the page that establishes it; a sentence about what he *did* quotes the record with its date. An answer without proofs is an opinion with a citation style, and it is worth less than nothing here — it looks like evidence.

1. **Say where the record cuts the other way.** Every answer states its own strongest counter-evidence and what would falsify it. The corpus contains things that do not flatter its subject, and an answering system that routes around them is one nobody should believe on anything. Where the corpus genuinely cannot settle the question, that is the answer, and it is a real one.

1. **Never quote a sealed page.** `wiki.locks.json` in the portal repo names pages that ship as ciphertext precisely so the site cannot read them out. An answer that quotes one publishes through the back door what the seal exists to keep shut.

Then the five writes, none of them optional:

1. The answer into `sage/questions/<id>.md` — `status: answered`, `answered:`, `capture:` and every path in `cites:`. This is what the portal renders.

1. The immutable capture to `raw/self/sage/<id>.md`: question, answer, sources. `sage/` mutates; `raw/` is the record.

1. **The findings staged onto every page the answer cites**, under `## Sage findings — pending ingest` with a `sage_pending: YYYY-MM-DD` flag — the same shape as `bin/wiki-gaps`'s block and a **deliberately different key**. An operator answer is T0 first-person testimony; this is synthesis *about* the corpus, and the two must never be mistaken for each other on a page. As with a staged gap answer, do not bump `date_modified`: the page has not been corrected yet, and bumping it would clear the staleness warnings on every page that reasons from this one.

1. `log.md`: `## [YYYY-MM-DD] answer | <domain> | <the question, short>` — as findings, not activity.

1. `bin/wiki-work scan`, three gates at 0 errors, commit.

An answer that produced no finding worth staging stages nothing, and says so in the answer. That is a legitimate outcome — it means the wiki already knew — and it is still an answer.

A question that is abusive, is about somebody other than Dan, or cannot be answered from the corpus gets `status: declined` and a reason in the Answer section. Declined in the open, never deleted: the portal renders it, so a question nobody wants to answer is visible as one.

### CLIMB — the operation that raises altitude

The only operation that runs on `wiki/` rather than `raw/`. Where INGEST adds ground, CLIMB builds above it. **Full protocol in ****`SYNTHESIS_SPEC.md`**** — follow it exactly.** The short form:

1. `bin/wiki-climb candidates` maintains `synthesis-queue.md`. Take the top cluster, or one you have reason to prefer.

1. Read the member pages **in full** — you are reasoning from them.

1. Find the governing rule, **or reject the cluster in the queue with a line of reasoning.** A cluster that resists synthesis is knowledge too. Never write a page whose thesis is "these things are related."

1. **Run the constitution pass before writing** — check the candidate rule against the eleven registers (cognitive stack, measured profile, historical precedent, attitudes and forces, security and prosperity, health, romantic state, age and upbringing, geographic/ethnic culture, ideological programming, axiomatic politics). Mandatory, `SYNTHESIS_SPEC.md`. It is allowed to change or kill the conclusion, and its result goes on the page.

1. Write it: `page_type: synthesis`, `knowledge: earned`, `synthesizes:` listing every member, thesis in the first two sentences, the controls that carry it, at least one prediction, Gaps, and which registers moved the conclusion versus left it standing.

1. Wire it both ways. **Every member page gets the finding written back into it** — an `instantiates` edge whose claim states what this page turned out to be evidence *of*, plus a prose sentence wherever it is load-bearing. A synthesis whose members do not carry it back is half-built.

1. All three gates at 0 errors; log `climb | <domain> | <page>`; commit.

Climb when a cluster has survived two or more ingests, or immediately when an ingest makes you think "this is the third time I've seen this shape." Do not climb to raise a number: three thin pages stacked make one thin page.

### CROSSLINK — pay a source's debt to the pages it already touches

INGEST reads a source and writes the page it is *for*. This operation writes what the same source owes to every **other** page it named. It is the third step of `STRATEGY.md`'s core loop, `EXTRACTION_SPEC.md` move 9 in practice, and until 2026-09-04 it was the only step of the loop with no operation, no tool and no way to tell it had been skipped.

**It is the one obligation in this repository with no symptom.** A red gate announces itself. A parked question sits at priority 1. A stale premise fires a warning. A source that named forty things and got linked to three looks *exactly* like a source that named three — from the page, from the queue, from `WORK.md`, and from `bin/wiki-lint`. The page you wrote reads as finished, because it is finished; what is unfinished is somewhere else, on pages nobody is looking at, and those pages cannot report a gap they have no way to detect.

Run it after a substantial ingest, when picking up a corpus somebody else mined, and whenever `bin/wiki-crosslink scan` is what you would have to run to answer "has anything been done with this source since?"

1. **`bin/wiki-crosslink scan <page>`** — reads the corpora the page's own `sources:` name, inside the page's own `date_range_*`, and lists entities with pages the page does not link, with the dated rows that produced each. `--all` sweeps the twitter year pages.

1. **Read the rows. Every one.** The tool emits candidates and nothing else. Roughly every single-token name match is a false positive — Rick Santorum under "Rick", Tom Cruise under "Tom", slim jims under "slim" — and a two-token match still needs the row to establish what it is. **A mention is not a relationship**: a tweet naming Diplo is a music-consumption datapoint, not a Diplo relationship, and it may belong on a third page entirely.

1. **Go at the target page's own claims first.** The value concentrates where a source contradicts what a page asserts about its own completeness or its own limits. Three such claims fell in one pass: a "complete record" that was missing three concerts, a person's page saying "everything known arrives through Dan's later AI-session narration" against six contemporaneous posts, and a substance row saying it "has no ledger entries at all and remains description" against eighteen years of dated first-party evidence. **A page that states its own limits is telling you where to point the next source.**

1. **Write both ends**, per `CONNECTIONS_SPEC.md`'s source-mention obligation: a typed edge whose claim says what the target page did not have, and the material itself in prose wherever it changes what a page says. Keep the mundane — `EXTRACTION_SPEC.md` move 7 governs here too, and the value of a detail is the surface area it gives the next climb, not its own significance.

1. **`bin/wiki-crosslink reciprocal`** — the inverse-edge debt. An edge into a generated page is not debt and the tool knows the list; anything else owes an inverse that carries the finding rather than pointing at it.

1. **State what did not survive.** A pattern that dissolves on the wider match is a result and goes on the page — this pass had a Facebook-to-Twitter release lag that looked like a clean five days across six matched pairs and ran from −1 to +28 across twelve. The tidy version is the one the next session will reach for unless the page says it failed.

1. Three gates at 0 errors; log `connect | <domain> | <source> → <N pages>`; commit.

**What this operation is not.** It is not `bin/wiki-connect candidates`, which scores *page-pairs* on shared sources, tag overlap and co-citation — that mines the graph for pairs that look related. This reads the **source text** for what a page's own evidence base is missing, which is a different question with a different answer, and the two queues do not overlap.

### REWRITE — wipe and re-derive an existing page

When the operator asks to rewrite, wipe, redo, re-research or overhaul a page that already exists, **invoke the ****`wiki-rewrite`**** skill (****`.claude/skills/wiki-rewrite/`****) and follow it exactly.** INGEST governs new sources arriving; that skill governs an existing page being re-derived, and it carries the parts this pass gets wrong: snapshotting earned content before the wipe, ranking primary against AI-secondary sources, verifying derived numbers with `bin/mine-messages`, resolving identity through two independent contact exports, and working the staleness cascade without bumping a date.

### CLOSE — integrate an answer the operator has already given

Every other operation starts from a source. This one starts from the operator having sat down and answered something a page admitted it did not know. `bin/wiki-gaps` stages those answers; **applying them is not optional and is not low-priority work.** An answer sitting in a staging block is the wiki holding knowledge it has not absorbed — strictly worse than not having it, because `OPEN.md` now reads as if the question were still open somewhere and the answer is invisible to every page that needed it.

`bin/wiki-gaps pending` lists them; `OPEN.md` carries the same list under **Answered, awaiting ingest**. For each page:

1. **Read the whole page first**, then the staged blocks under `## Operator answers — pending ingest`. Each block carries the gap as the page stated it, the operator's answer verbatim, and the `raw/` path the answer was filed to.

1. Treat the answer as **T0 first-person testimony, not as proof.** It is the strongest source class the corpus has and it is still one source. Where it can be checked against `raw/` — `bin/mine-messages`, an export, a contacts file — check it, and say on the page which parts were corroborated and which rest on testimony alone. Where it *contradicts* something the page derived from a primary source, that is a `> **CONTRADICTION:**` to hold, not a disagreement to settle by seniority.

1. **Rewrite the page around the answer** — integrate it where it belongs in the existing argument. Do not leave the staged block in place as the answer's permanent home; that is the changelog rot STYLE_GUIDE rule 6 forbids.

1. Record the result inline as a `> **GAP CLOSED [YYYY-MM-DD]:**` blockquote with the original gap visible (STYLE_GUIDE rule 9), and cite the `raw/` capture in `sources:`.

1. **Cascade.** A gap is rarely local: every page that reasoned from the unknown, cited the gap, or carries a typed edge into this one gets the correction written back. This is the step most often skipped, and skipping it is what leaves a corrected page contradicting three uncorrected ones.

1. Bump `date_modified` **now** — the page has actually moved, which it had not when the answer was merely staged.

1. `bin/wiki-gaps clear <page>` to delete the staging section and the `pending_ingest:` flag. Clearing means integrated, never discarded: the answer is permanent in `raw/`.

1. Three gates at 0 errors; log `close | <domain> | <page> — <what the answer changed>`; commit.

If an answer turns out to be **wrong** against a primary source, that is a finding worth more than the answer was — write it up, keep both claims visible, and clear the flag anyway. A staged answer that was never acted on and a staged answer that was checked and rejected must not look the same from outside.

### ADJUDICATE — record what a first-person claim turned out to be worth

CLOSE integrates an answer the operator has given. **This one records whether it held up**, and it is the step that makes the corpus cumulative about its own most valuable and least verifiable source class. CLOSE step 2 already tells you to check the answer against `raw/` where it can be checked and to say on the page which parts were corroborated and which rest on testimony alone. That sentence describes an adjudication. Without this operation it is written once, on one page, and the next session starts from zero.

`bin/wiki-testimony` runs it; `testimony/README.md` is the full account.

1. **Record the claim when it arrives**, not when you get round to checking it. A claim nobody has checked is not a failure and does not score — it is the queue, and `bin/wiki-testimony list --pending` is the list of things the wiki is currently carrying on his word alone.

1. **Classify it as a proposition, not by subject matter.** A date is misremembered the same way whether it is about a job or a funeral; `bin/wiki-testimony taxonomy` prints every class.

1. **Capture the confidence he actually expressed.** This is the field the seed set could not have and the one the whole calibration half runs on. A hedge that turns out to be right is a *success*, and a system that cannot see the hedge will score it as a failure.

1. **Adjudicate against evidence, and name what settled it.** A confirmation by a primary document and a confirmation by something else he said are not the same event. `--tier none` with `--outcome confirmed` is refused.

1. **A miss must name its failure mode and its slant.** `check` fails without both, and `neutral` is a real slant that has to be given rather than assumed — the absence of self-serving error is only evidence if somebody looked for it. Without these columns this degenerates into a tally, and a tally predicts nothing about the next claim.

1. **Never edit an adjudication.** `adjudicate --revise --reason` supersedes it and the log keeps both. A veracity record that can be quietly rewritten is worth less than no veracity record at all.

1. Gates at 0 errors; log `adjudicate | <domain> | <the claim, short>`; commit.

**Read it before writing a synthesis that leans on testimony.** `bin/wiki-testimony assess --class <c> --confidence <x>` gives the prior and, if it is wrong, the failure mode and direction to expect. A class below `MIN_N` is refused as a prior and the tool says so rather than quoting a rate computed from three cases.

### EXPIRE — put a clock on a claim, and close the window honestly

CLOSE integrates an answer. ADJUDICATE records whether it held up. **This one records how long it stayed true**, and it is the operation that keeps compounding synthesis from compounding rot. `bin/wiki-claims` runs it; `claims/README.md` is the full account.

Run it when a page asserts a state rather than an event — a residence, a job, a relationship, a running project, a handle, a regimen — and when `bin/wiki-claims scan` says a page is asserting a live state on evidence that stopped.

1. **`bin/wiki-claims scan`** is the triage step. It reads frontmatter the corpus already maintains — `status: active` against a `date_range_end` years past, and `status: closed` on pages the ledger has never seen. It is deliberately **not** a prose grep: searching for "no longer" and friends was measured against this corpus and is roughly all false positives (121 hits, overwhelmingly quoted tweets in which somebody else is no longer something), the same lesson `bin/wiki-crosslink` learned about single-token name matches.

1. **Read the page before recording anything.** A candidate is a reason to read, never a reason to write. `record` takes the claim, its `--kind`, the date the record actually supports as `--valid-from`, and the pages it lives on.

1. **Close it as ****`ended`**** only if you can date the ending.** `--closure ended --on DATE` asserts that the state stopped on a day something establishes. If nothing dates it, it did not end — the record went quiet, which is `--closure lapsed --last-seen DATE`. The tool refuses the arguments of one band passed to the other, because swapping them publishes the corpus's silence as the world's.

1. **Say what closed the window.** `--because` is required in both bands. An expiry with no account of what closed it is a guess wearing a date, and the ledger cannot learn from it — the same rule ADJUDICATE applies to a miss.

1. **Never extend a window to clear a scan line.** Re-read what the evidence supports and record what it actually says. Rule 3, one layer down.

1. **An expiry is never edited** — `expire --revise --reason` supersedes it and the log keeps both, exactly as an adjudication does.

1. **Write the finding back to the page.** The ledger records the window; the page says what it means. A claim closed against a page still carrying `status: active` raises a warning rather than an error, because a page can legitimately stay active on *other* evidence — `mogzart.md` does exactly that.

1. `bin/wiki-claims page`, three gates at 0 errors; log `expire | <domain> | <the claim, short>`; commit.

**Read it before writing a synthesis that reasons about a past state.** `bin/wiki-claims asof <date>` is what the record holds true on a given day, and it reports lapsed claims as **unsettled** rather than false — a separate list, on purpose. Unknown is not false, and collapsing the two invents a measurement.

### TRANSLATE — write the plain-language edition of a page

The portal has an EDITION switch in its header: FULL is the wiki as written, READER'S DIGEST is the same finding told to somebody who has never read anything else here. This operation writes the second one. `bin/wiki-plain` runs it.

**What a twin is for.** Every page here is written for a reader who already knows the corpus, and that is the correct register for the technical wiki — but it means the wiki is unreadable to the people most likely to arrive at it through the front door. A twin is not a summary and not an abstract: it is the same finding at the **same altitude**, with the apparatus removed and the sentences rebuilt for somebody who does not have the context.

1. `bin/wiki-plain next --lane major` names the densest eligible pages with no twin yet. Take the top one, or one you have reason to prefer. **This operation is the major lane**; the free lane belongs to an unattended agent and is governed by `PLAIN_AGENT.md`, which is this operation mechanised down to what a weak model can follow. The two lanes are disjoint by construction, so neither writer has to check what the other is doing.

1. `bin/wiki-plain new <slug>` scaffolds `plain/<slug>.md` with `plain_of:` and `source_modified:` already filled in. It **refuses** a page under the standing moratorium; that refusal is not advisory and not yours to override.

1. **Read the whole page first.** You are translating a finding, not compressing a document — a twin written from the first three paragraphs is a summary, and the difference matters.

1. Write it. What goes, what stays:

  - **Keep every number, date, name and quantity.** Simplifying the language is the job; simplifying the *evidence* is inventing a second, weaker wiki.

  - **Keep the falsifiers and the gaps**, in plain words. A reader shown only the confident half is being sold something, and this edition reaches the readers least equipped to notice.

  - **Drop the apparatus**: typed edges, `synthesizes:`, provenance disclosures, `knowledge:` values, register tables, `raw/` paths. That is machinery for maintaining the wiki, not part of the finding.

  - **Explain the jargon rather than deleting the concept.** "Ti-dominance with no Fe-mediated grading function" becomes "his sense of his own worth runs on an on/off switch with nothing in between." The claim survives; the vocabulary does not.

  - Close with the standard pointer back to the full entry.

1. **A page you cannot translate honestly, you do not translate.** If the only way to write it is to leave out something that changes what the page says, that is a finding — say so where the next session will read it and move on. A misleading plain version is worse than none, because it is easier to read.

1. `bin/wiki-plain check` at 0 errors; log `translate | <domain> | <page>`; commit.

**The one rule that has teeth.** A twin records the version of the page it was written against, in `source_modified:`. When the page is revised the twin goes stale, and `bin/wiki-plain check` — which `bin/wiki-check` runs as a gate — fails until somebody deals with it. **Never clear it by bumping the date.** Re-read what moved, decide whether the plain version survives it, rewrite what did not. This is rule 3 of "the four things that matter most", one layer down, and it matters more here rather than less: a stale twin is a confident, readable, wrong account of what the wiki says, served to the one reader who cannot check it against anything.

Coverage is standing campaign work, not an obligation — a page with no twin serves the technical edition and says plainly that no plain version exists yet. Only a **broken** twin (stale, orphaned, or forbidden) is a gate failure.

**The campaign has a page: ****`wiki/meta/readers-digest`**, generated by `bin/wiki-plain report` from the tree and the git log — coverage, both lanes, what is held back and why, and who wrote each twin by the last commit to touch it. Generated, so a hand-edit fails `check`; derived, so nothing has to be kept up to date by hand and an agent that forgets to report has still reported. Pages held out of the lanes are **counted on it rather than dropped**, because an entry nobody will translate and an entry nobody has got to must not look the same from outside. What is held out, and why, is `plain/DECLINED.md`.

**The second gate: ****`bin/wiki-plain audit`****.** `check` asks whether a twin is broken; `audit` asks whether it is any good, and it gates too. Fabricated numbers (a quantity in the twin that appears nowhere in the page — the load-bearing check, because a number reads as proof), leaked apparatus, filler phrases, a dropped falsifiers-and-gaps section, a summary masquerading as a translation, prose above US grade 12.5, an unfilled scaffold. Every rule is arithmetic over the two files, so there is nothing in it for a writer to talk its way past — which is the point: this is the one layer of the repository a careless writer can degrade without leaving a trace.

**Running it unattended.** `bin/wiki-plain task` emits one page's entire writing task — the rules and the full source page — in a single blob, so a cheap model that will not remember a spec gets it re-injected every run. `PLAIN_AGENT.md` is the operating manual for pointing such an agent at the backlog: the loop, the prompt, what the referee catches, what it structurally cannot catch, and the spot-check that remains a human's job.

### LEARN — write back what the next agent should not have to rediscover

Every other operation moves knowledge about Dan. This one moves knowledge about **the work**: the trap you hit, the invariant you found by breaking it, the command sequence that turned out to matter. It runs at the end of a session, and it is the operation with no external prompt — nothing parks a question, nothing stages an answer, nothing goes red. If it does not occur to you to run it, it does not run. That is why it is written down here rather than left to judgment.

Ask one question before closing substantial work: **what did this session have to discover that the next one should not have to?**

1. **Nothing reusable → nothing to write.** Most sessions end here, legitimately. A skill corpus padded with restatements of `STYLE_GUIDE.md` is worse than a short one, because every entry costs the next agent a read.

1. **Something reusable but unproven → ****`skills/INBOX.md`****.** Write the *observation*, not the instruction: what actually happened, with enough context to reproduce the reasoning. `skills/PROTOCOL.md` §1 is explicit that a candidate starts as an observation, and the seed template is in the file. `bin/wiki-work` will surface it as an obligation so it does not sit unread.

1. **Something proven → a skill.** Promote only when one of `PROTOCOL.md` §3's three tests passes: it has explained the same class of failure more than once, a command or test validates it, or a governing spec already implies it mechanically. `bin/wiki-lessons new <domain>/<slug>` scaffolds the file.

1. **Revise rather than overwrite.** If an existing skill was nearly right, improve the instruction and keep the invariant; if it was wrong, mark it `deprecated` or `retired` and write the replacement with `supersedes:`. Never silently change what a skill means (`PROTOCOL.md` §6). A retired skill stays in the tree and in the index's History table on purpose: deleting it leaves the agent who remembers being told it with nothing to correct it.

1. **Record it in ****`skills/CHANGELOG.md`** with the date and the reason. This is not bookkeeping — `bin/wiki-lessons check` fails on a skill that is not named there, because an instruction the corpus cannot account for is one no later reader can weigh.

1. `bin/wiki-lessons scan`, then the gates; log `learn | skills | <what was promoted and why>`; commit.

**Do not promote a lesson to clear an inbox entry.** A candidate parked with its evidence still missing is doing its job; an instruction promoted early is worse than one still parked, because the index vouches for it and the next agent has no way to know it was a guess. Leaving it in the inbox with a note about what evidence is still needed is a complete and correct outcome.

### DECLARE — push what this model has into the skills database

Every other operation moves knowledge about Dan. This one moves knowledge about the machines: **what capabilities the model doing the work actually has.**

Several models work on this repository — Claude Code in a terminal, Claude in a browser, Codex, Cursor, whatever comes next — and each arrives with a different set of skills, MCP servers, plugin tools and subagents that none of the others can see. Without a shared record every session rediscovers the same surface, and a lesson one model learned about a tool the next model also has dies in a transcript nobody keeps.

**When the operator asks to update the skills in the wiki, this is the operation** — not editing a skill's prose, which is `skills/PROTOCOL.md`. Invoke the `wiki-skills` skill (`.claude/skills/wiki-skills/`); the full instruction is `skills/agents/registry-push.md` and the format is `skills/registry/README.md`. The short form:

1. `bin/wiki-skills push --scan --agent <id> --vendor <v> --surface <s>` — the repository's own half: the skills under `.claude/skills/` and `skills/`, every command in `bin/` with its own docstring as its summary, MCP servers configured in the tree, hooks, subagent definitions.

1. `bin/wiki-skills push -f skills/registry/manifests/<id>.json` — **the half no scan can see**: the model's own skills, MCP servers, plugin tool links, subagents and harness. Nothing in the working tree records these, so an undeclared capability is one no other model will ever learn about.

1. **Environment variable NAMES only, never a value.** This repository is public and its history cannot be un-published; MCP configurations are the most reliable place in an agent's environment to find a live key. The tool refuses a credential shape and names the field rather than stripping it — the refusal is correct and is not to be worked around by rephrasing.

1. `bin/wiki-skills page`, then the gates. The page is generated; a hand-edit fails `check` and the fix is to rerun the tool.

1. Read the other direction before substantial work: `bin/wiki-skills list --kind command` for what this repo gives you, and `bin/wiki-skills diff <a> <b>` for what another model has that you lack — including capabilities you both declare at **different digests**, meaning one of you has revised an instruction the other is still running.

A push that records nothing is a success: it is idempotent by content digest, and `0 new, 0 revised, 51 unchanged` means the database already had you. Log `declare | meta | <agent> — <what moved>` and commit.

### LINT (periodic)

Sweep for: broken links, orphan pages, contradictions between pages, claims superseded by newer raw data, entities mentioned 3+ times with no page, and **stale premises** (`bin/wiki-climb check`). Fix mechanically what you can; queue the rest in `BACKLOG.md`. A stale page is never fixed mechanically — re-read what changed in the premise before touching the dependent.

**Invoke the ****`wiki-housekeeping`**** skill (****`.claude/skills/wiki-housekeeping/`****) and follow it** whenever the operator asks to tidy, sweep, lint, audit or do housekeeping, and at the end of a session that moved the repo a lot. It carries the part this paragraph cannot: which warnings are requests to look rather than defects (the size warnings are, and trimming to clear one destroys earned content), how to work a stale premise without bumping a date, and how to drain obligations without mistaking a cleared flag for an integrated answer. The mechanical half is `bin/wiki-check`; the skill is the half that needs a reader.

## Tools (`bin/` — pure Python stdlib, no dependencies, no APIs)

| **Tool** | **Purpose** |
| --- | --- |
| `bin/capture` | human-facing input: interactive typing/pasting, one-shot facts, file upload (`-f`), `status` |
| `bin/mine-messages` | corpus mining over the full iMessage dump: `stats`, `grep`, `timeline`, `battery`, `entities`. **Use this instead of grep** — three properties of the dump make naive grep silently wrong |
| `bin/text-metrics` | turn-level style measurement: `eras`, `modes`, `contacts`, `response`, `hours`, `silence`, `target`. The instrument behind `wiki/mind/profile/texting-deviance-audit`. **Use this rather than ****`mine-messages`**** for anything about length or cadence** — message-level counts hide the effect entirely, because the unit of Dan's speech is the turn, not the message |
| `bin/wiki-check` | **the whole mechanical chain in one command** — regenerates, runs the three gates plus freshness, rescans `WORK.md`, in the one order that is correct. `--check-only` gates without writing (CI, review); `--quiet` for hooks. Exits 1 on any red gate. The judgment half is the `wiki-housekeeping` skill |
| `bin/wiki-lint` | frontmatter, links, orphans, sizes, duplicate frontmatter keys, retracted claims (`RETRACTED.md`), empty cited sources, **unresolved merge markers, assistant citation artifacts, malformed frontmatter blocks and master-index count drift**. Must be 0 errors before commit |
| `bin/wiki-freshness` | is the generated corpus (`llm/`) in sync with `wiki/`? Exact set difference against `llm/manifest.json`; never writes. Exit 1 on drift |
| `bin/wiki-connect` | `check` (typed-edge lint), `audit` (graph health), `candidates` (writes `connection-queue.md`) |
| `bin/wiki-crosslink` | **the source-mention obligation, computed.** `coverage [--silent]` is the triage step and comes first — which of the readable corpora actually name a page, 3s for all 497 against a quarter-million source rows, and inverted, the pages nothing names that cite a corpus anyway. `scan <page>\|--all` then reads the corpora a page's own `sources:` name, inside its own date range, and names every entity with a page the page does not link — with the dated rows behind each, because the output is candidates and a candidate is a reason to read; `--against <corpus>` asks the more productive question, "in what a corpus the page does *not* cite says about it, what else is named?", and `--queue` orders the wiki by how loudly a page states a limit about its own evidence. Reads the twitter archive and **both** message exports — the latter by importing `bin/mine-messages`' reader, traps and all, rather than writing a second one — and marks a candidate `contested` when two pages claim the same string. `reciprocal [prefix]` is the inverse-edge debt `CONNECTIONS_SPEC.md` requires and nothing measured; `entities` is the index of strings a scan can look for; `orphaned` names corpus-backed pages by edge count; `check` prints the debt and **always exits 0** — a one-way edge still carries its claim, and a gate that blocked unrelated commits on it would acquire an escape hatch. It knows the generated surfaces and never asks for an inverse on one. It writes no edges and must not be made to |
| `bin/wiki-climb` | `check` (validates `synthesizes:`, reports stale premises), `audit` (tier distribution), `candidates` (writes `synthesis-queue.md`) |
| `bin/wiki-digest` | regenerates `DIGEST.md`, `RECENT.md`, `OPEN.md`, and their `wiki/meta/` on-site mirrors — committed, safe to rerun any time |
| `bin/llm-publish` | builds `llm/`, the public LLM access point — **generated but COMMITTED**; rerun after any content pass |
| `bin/export-corpus` | concatenates the wiki into one markdown file for LLM ingestion, with a token estimate |
| `bin/wiki-search`, `bin/wiki-status`, `bin/wiki-tui` | search, status, terminal browser |
| `bin/ingest-pack` / `bin/ingest-apply` | the any-LLM paste-box route (`INGEST_PROTOCOL.md`) |
| `bin/wiki-work` | **the one outstanding-work list, and a required session step.** Aggregates every source of outstanding work — parked `sage/` questions, staged answers, stale premises, unnormalised portal edits, and the four standing queues — and separates obligations from campaign work. `scan` regenerates `WORK.md`; `next` names the top item and the operation that clears it; `check` prints the gate banner and always exits 0. No `done` command, by design |
| `bin/wiki-plain` | **the READER'S DIGEST layer.** `status` (coverage), `check` (the gate — stale, orphaned or forbidden twins, and drift on the generated campaign page), `audit [slug]` (**the anti-slop referee** — fabricated numbers, leaked apparatus, filler, a dropped honest half, reading level; gates in `bin/wiki-check`), `report` (campaign progress by lane and by writer; regenerates `wiki/meta/readers-digest.md`), `next [n] [--lane] [--synthesis]` (the queue), `new <slug>` (scaffold), `task [slug] [--lane]` (one page's whole writing task, rules and page included, for an unattended agent — see `PLAIN_AGENT.md`). **Two lanes**, arithmetic rather than convention, so two writers do not collide: `major` (≥900 words, densest first) and `free` (300–899, smallest first). Encodes the standing moratorium as two mechanical rules rather than leaving it to a session to remember, and **refuses** rather than warns — a lane is refused the same way |
| `bin/wiki-lessons` | **the gate and the router over ****`skills/`****.** `route "<task>"` names the skills a piece of work must load — the routing algorithm run rather than remembered; `check` gates (malformed frontmatter, a missing required section, an index that has drifted from the files, a superseded skill still routed, a skill absent from `CHANGELOG.md`); `scan` regenerates `INDEX.md`; `next` lists candidates awaiting validation; `new` scaffolds; `list`/`status` read the corpus. It deliberately does **not** judge whether a skill is *true* — that needs evidence and a second occurrence, per `PROTOCOL.md` §3 |
| `bin/wiki-gaps` | operator-facing: answer an open gap, or volunteer a fact the page never asked for, and stage it for the next pass. `pages [filter]` lists **every** page so any of them can take a manual addition; `list` lists only those with open items; `pending` lists what is waiting; `clear` closes the loop and marks `operator-log.md`. Reads gaps, open leads, corrections queues and "what's missing" sections alike |
| `bin/intake` | **the intake ledger.** `page` regenerates `wiki/health/intake-ledger.md`, the public database page (generated — a hand-edit fails `check`); `capture` backfills the `raw/` archive for units closed through the portal, which never calls `close`; `new` opens a unit, `log` records one intake against it (measured, `--estimated`, or `--descriptor "one line"` for an event with no reliable quantity), `correct`/`void` supersede an event without erasing it, `close` refuses to finish while quantity is unaccounted for, `report` prints the unit report, `stats` reads across every unit, `check` gates in `bin/wiki-check`. Event-sourced in plain JSONL. **Never prints a quantity statistic without the share of events it was computed from** — a mean over 10 of 13 events must not be able to look like a mean over 13 |
| `bin/wiki-testimony` | **the operator testimony veracity ledger.** `record` enters a first-person claim, `adjudicate` settles it against evidence (`--revise` supersedes, never edits), `score` prints the two numbers, `assess` gives the prior for an **unproven** claim, `profile` shows what and how the errors run, `taxonomy` prints every class and mode, `page` regenerates `wiki/meta/testimony-veracity.md`, `check` gates in `bin/wiki-check`. Event-sourced in plain JSONL. **`unfalsifiable`**** scores zero, never negative** — the corpus's gaps are not his failure. **Never prints a rate without its ****`n`**, shrinks class rates toward the global with a pseudocount, and refuses a class under `MIN_N` as a prior outright. Encodes the standing moratorium as a refusal rather than a warning |
| `bin/wiki-claims` | **the claim validity ledger — when a claim stopped being true.** `scan` is the triage step and reads *frontmatter*, never prose (the obvious "no longer" grep is ~all false positives on this corpus: 121 hits, overwhelmingly quoted tweets); `record` enters a claim and the window the evidence supports; `expire --closure ended |
| `bin/wiki-secrets` | **the credential scan on what is about to enter the record.** `check` gates in `bin/wiki-check`; `--staged` narrows it to what `git add` staged. `bin/wiki-skills` already refuses a secret shape at its own point of entry, but it owns one surface — a capture in `inbox/`, an export filed to `raw/`, a token pasted into a page while debugging had never been scanned by anything, and **this repository is public, so the failure is permanent rather than embarrassing**. **It scans the working diff and untracked files, NOT the tree**, and that is what keeps it switched on: `raw/` holds 130,000 received messages, a corpus that size contains key-shaped strings that are not keys, and a gate firing on immutable archive material would be disabled within a week. Never prints the value it found — six characters, because the output lands in CI logs. Adapted from `stancsz/second-brain`'s `scripts/ship_gate.py` |
| `bin/wiki-lexicon` | **the personal lexicon, counted rather than recalled.** `probe WORD` gives a word's per-year rate in Dan's own text and in his AI prompts; `distinctive` names what marks his speech against the 130,402 messages he received (log-odds with an informative Dirichlet prior, so a rare word cannot outrank a common one on ratio alone); `registers [--page]` measures a wordlist's density in each of his two first-party registers; `mine` recomputes `lexicon/measured.json` (~90s, deliberately not in `bin/wiki-check`'s generate list); `pending`/`show`/`new` work `lexicon/words/`; `page` regenerates `wiki/interests/language/measured-vocabulary.md`; `check` gates. **It reads both message exports and both AI exports through their existing readers rather than writing new ones** — and it converts the deep CSV from UTC to Eastern before the union, because the dump is local time and without that every shared message is counted twice (measured: 36,716 rows at +4h, 23,624 at +5h). **A count over a transcript is not a usage count**: the Gemini export interleaves Dan's prompts with the model's replies, so this splits on the `Prompted` boundary and reports only his half. It refuses to publish a frequency ranking over his Gemini prompts, because he pastes documents into them and the top of that list is `div`, `class`, `null` |
| `bin/wiki-history` | **the log as a record of the work.** Every operation commits `<op>: <description>`, so the git log is not a list of saves — it is a labelled record of every ingest, climb, close and portal edit that ever touched a page, and this reads it. `status` (revisions, span, by operation, the most revised), `page <slug>` (one page's revisions), `drift` (pages whose `date_modified` is behind the log — **a reading job, not a defect list**: a link cleanup across forty pages moves none of them), `check` (the gate). The gate is narrow on purpose: a page whose `date_modified` is *later* than the last commit that touched it. The file has not changed since, so the date is a claim git does not support — which is what rule 3 above looks like from outside. Pages edited in the working tree are exempt, or it would fire on every honest pass. Skips itself in a shallow clone |
| `bin/wiki-traits` | **the personality profile, cross-tested against the whole corpus — and the filter that result becomes.** `support` runs every trait as a directional prediction over four first-party registers; `reach` measures how much the wiki already leans on it; `map` is the quadrant those two axes make and the loud cells are the findings; `assess <trait>` is the interface the constitution pass calls before leaning on a trait as a mechanism; `review` is the proxy queue; `mine` recomputes `traits/measured.json` (~70s, deliberately not in `bin/wiki-check`'s generate list); `page` regenerates `wiki/mind/profile/trait-corpus-map.md`; `check` gates. **Support and reach are never added together**: reach is measured over pages written by agents that had read `wiki/mind/profile/`, so it records vocabulary adoption, not the trait, and it is never evidence. **An unreviewed proxy cannot confirm a score and cannot contradict one** — such a result is reported as `unreviewed`, a band distinct from `silent` (an instrument ran and found nothing) and from `no instrument` (every proxy was read and found to measure something else); collapsing the three would report a measurement that never happened. The cap exists because the heaviest verdict in the system is also the cheapest to manufacture. **No confidence percentage, ever** |
| `bin/wiki-skills` | **the cross-model skills database.** `push --scan --agent <id>` records what this repository supplies; `push -f <manifest>` records what a model brings that no scan can see — its skills, MCP servers, plugin tool links, subagents and harness. `list`, `show`, `diff <a> <b>` read it; `note` attaches an observation to a capability; `page` regenerates `wiki/meta/skills.md`; `check` gates in `bin/wiki-check`. Append-only JSONL with a regenerable projection, idempotent by content digest. **Values never enter it — environment variable NAMES only** — and it refuses rather than strips, because this repository is public |

## Before every commit

bin/wiki-check              # regenerate, gate, scan — the whole chain, ~4s, red exits 1

bin/wiki-check --check-only # gate without writing anything (CI, or reviewing a branch)

`bin/wiki-check` runs what used to be four hand-copied lines, **and it runs them in the order that is actually correct**, which the four lines were not: generators first, then gates, then the scan. `bin/wiki-lint` checks master-index count drift, so running it before `bin/wiki-digest` inspects numbers that are about to change; and `bin/wiki-freshness` exists to confirm the generators ran, so running it before them asks a question whose answer is guaranteed stale. In `--check-only` mode nothing is written and `wiki-freshness` becomes the real gate rather than a formality — it is what catches a content pass committed without regenerating, which is how the LLM manifest got eleven pages behind on 2026-08-20. The individual tools still work exactly as before:

bin/wiki-lint && bin/wiki-connect check && bin/wiki-climb check   # all at 0 errors

bin/wiki-plain check                                               # Reader's Digest twins current

bin/wiki-lessons check                                             # skills routed, well-formed, recorded

bin/intake check                                                   # ledger log and projection agree

bin/wiki-testimony check                                           # testimony ledger, projection and page agree

bin/wiki-skills check                                              # skills database, projection and page agree

bin/wiki-lexicon check                                             # measured lexicon projection and page agree

bin/wiki-traits check                                              # trait-corpus map projection and page agree

bin/wiki-claims check                                              # claim windows, and lapsed is not ended

bin/wiki-secrets check                                             # no credential shapes entering the record

bin/wiki-history check                                             # no page dated ahead of its own last commit

bin/wiki-digest && bin/llm-publish                                 # after any content pass

bin/wiki-freshness                                                 # confirms the two above actually ran

bin/wiki-work scan                                                 # WORK.md back in step with the repo

bin/wiki-lessons scan                                              # skills/INDEX.md back in step with the files

`bin/wiki-lint` ends every run with what `bin/wiki-work check` found. That banner is **advisory and never changes the exit code** — a question parked on Tuesday must not block Thursday's typo fix, because a gate that blocks unrelated work is a gate that gets an escape hatch, and an escape hatch is how a mandatory step stops being one. Read it anyway; it is the reminder that step 4 above is still waiting.

`bin/wiki-freshness` exists because the generated corpus is committed and drifts silently when a pass forgets to regenerate — the 2026-08-20 audit found the LLM manifest eleven pages behind. It compares the manifest's own page list against `wiki/` and names every page that is missing, orphaned or changed. It never writes; you fix drift by running the generators yourself.

**Retracted claims.** `RETRACTED.md` is a machine-readable ledger of claims shown to be false; `bin/wiki-lint` fails if one reappears as a live assertion. Correction blockquotes are exempt by design — STYLE_GUIDE rule 9 requires the old claim to stay visible where it is corrected — so documenting a retraction never trips the gate. Add a claim by appending a JSON block to that file; no tool edit is needed. Patterns must model the *claim*, never a bare number.

**Tests.** `python3 -m unittest discover -s tests` covers the lint gates and the freshness check.

Then append to `log.md` as **findings, not activity** — what was wrong, what the evidence was, what changed — and update `LLM_HANDOFF.md`.

Size warnings from `bin/wiki-lint` are **advisory**. They mean "check navigation," never "shorten." Never trim earned content to clear one.
