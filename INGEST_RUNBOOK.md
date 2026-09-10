# PHASE B INGEST RUNBOOK — reproduce the cross-corpus wiki-synthesis pass

**Connections addendum (2026-07-17):** every page written or updated in an ingest pass must carry a `connections:` block per `CONNECTIONS_SPEC.md` (typed edges with claims, inverse edges on targets). `bin/wiki-connect check` is a commit gate alongside `bin/wiki-lint`. Read `STRATEGY.md` if this is your first session.

**Synthesis addendum (2026-07-26):** ingest raises the floor; it is not the whole job. `SYNTHESIS_SPEC.md` adds the **CLIMB** operation and the `synthesizes:` field (wiki pages a page reasons FROM, as against `sources:` for raw paths). Two obligations land on every ingest pass: (1) `bin/wiki-climb check` joins the commit gates, and a page it marks **stale** must be re-checked against its moved premise rather than date-bumped; (2) when a pass touches a page that some synthesis page reasons from, expect to owe that synthesis page a look. If an ingest makes you think "this is the third time I've seen this shape," stop and climb instead of filing the fourth instance.

Self-contained instruction. Hand this to any model/agent and it should be able to perform the task exactly as done on 2026-07-15: read Phase B RAW sources, file them into `raw/`, and write ~5,000 words per pass of NEW connective synthesis that EXTENDS existing wiki entries (never bulldozes them).

## 0. WHO YOU ARE AND WHAT THIS IS

You are an agent working on **Dan Frank's "wiki-brain"** — a personal second brain: a hand-built wiki that tries to capture, in exhausting detail, one person's entire factset, historical record, and cognitive/personality profile.

The point of the wiki is NOT retrieval (that's RAG). The point is **compounding synthesis**: you read a source ONCE, reason out what it *means*, and write that understanding into `wiki/`. From then on, every later agent reasons FROM the wiki, not from `raw/`. Today's synthesized conclusion is tomorrow's premise. The wiki grows to reflect what has actually been read and understood — a record of a shared journey through the data.

This wiki is also explicitly **built for LLMs/agents**. It is meant to act as a bootloader: give a future model (even a browser-based or third-party one) as close to the full contextual picture of Dan's reality as possible, so it has near-parity awareness with him. Write every page as if a future model will load it to understand the person. Depth and precision are the entire value.

**Hard standing directive from the operator (Dan):** lengthy, detailed, optimized articles containing profound insights and the connective threads that give the wiki its value. There is a style guide, but the operator's DIRECT instruction outranks it where they conflict. The genius here is compounding, narrowly selected, single-subject awareness — so the more you grasp the totality of the factset, the faster the value compounds.

## 1. HARD ENVIRONMENT FACTS (do not guess — these are verified)

| **Fact** | **Value** |
| --- | --- |
| Repo (local) | varies by machine — never hardcode a path; work from the repo root |
| Published site | `https://caakehorn.github.io/wiki-brain/wiki/` (live; see `AGENT_ACCESS.md`). Public mirror: `https://caakehorn.github.io/leviathan/data/wiki-data.json` |
| GitHub remote | `caakehorn/wiki-brain` (origin, https) |
| Default branch | `main` |
| Ingest branch pattern | `feat/<descriptive-slug>`, or whatever branch the session's standing instruction names |
| Gates | `bin/wiki-lint`, `bin/wiki-connect check`, `bin/wiki-climb check` — all three, 0 errors, from the repo root |
| Environment | usually macOS locally; sessions also run in a Linux container with no `gh` CLI (use the GitHub MCP tools there) |
| **Operator identity** | **Dan Frank** (`dfrank88@gmail.com`), b. 1988-11-01. On the local machine the home directory is `/Users/Suzanne` — that is his MOTHER's machine. IGNORE the directory name; Suzanne is NEVER the user. Everything in a session is Dan. |

The repo's own `CLAUDE.md` reinforces this: the wiki is about Dan Frank. Treat `raw/self/context-core/CONTEXT_CORE_EXPANDED.md` as the primary authoritative source for facts about Dan (biography, timeline, psychology, relationships, ideology). Other raw sources are supplementary or corrective to it.

## 2. GOVERNANCE FILES — READ THESE FIRST, IN THIS ORDER

All at repo root. Each says what it wins on when two disagree.

1. **`STRATEGY.md`** — read first. States the purpose, **the core loop** (Story → Entry → Analysis → Synthesized finding → **saved back to every entry it touches** → repeat), and the **five unbreakable rules**. Wins on intent.

1. **`CLAUDE.md`** — the operations: architecture (`inbox/ → raw/ → wiki/`), the second-brain principle (earned vs derived), ingest/query/climb/rewrite/lint, the tool table. Wins on process. Its standing rule: **update ****`LLM_HANDOFF.md`**** at the end of every session** with what you did and the exact next focus.

1. **`EXTRACTION_SPEC.md`** — how deep to go into a source before writing. This is the binding constraint on the whole project and the most important file for an ingest pass specifically: the eight moves, primary vs AI-secondary source tiers, and the per-source traps that fail *silently*. Wins on depth.

1. **`LLM_HANDOFF.md`** — cross-model coordination. Current state and what the last several sessions did. You MUST append to it at session end.

1. **`STYLE_GUIDE.md`** — page format and the substance standard. Wins on format. Note the operator's standing directive inside it: **longer, denser entries**; size warnings are advisory and never a reason to cut. Keep published wiki voice plain and human — do not carry LLM neologisms into derived prose, though you may quote them from source evidence.

1. **`CONNECTIONS_SPEC.md`** (edges) and **`SYNTHESIS_SPEC.md`** (altitude) — read both before wiring anything or writing a synthesis page.

1. **`BACKLOG.md`** — the standing work list, so you pick up something live.

1. **`AGENT_ACCESS.md`** — access/safety policy. Do NOT preserve any credentials/tokens/API keys you encounter in sources; redact, never replicate.

1. **`bin/wiki-lint`** — read it to know exactly what it validates:

  - `sources:` frontmatter paths MUST exist on disk under `raw/`, or it errors.

  - `wiki/`-prefixed internal links are checked for reachability.

  - `knowledge:`, when present, must be `earned | derived | mixed`.

  - `domain: people` pages require an `infobox:` with `name` + `relationship_to_dan`.

  - Page size produces **warnings, not errors**, and the budget is 40 KB.

## 3. THE TASK, PRECISELY

Per pass (a "pass" = one source or tight source-cluster, fully processed):

- Produce **~5,000 words of NEW connective synthesis** drawn from the Phase B RAW material, that EXTENDS existing wiki entries. New pages are fine when a cluster has no natural home, but prefer extending an existing earned page.

- **Only alter/append entries under ****`wiki/`****.** The `raw/` tree is immutable source except for the act of filing new sources into it.

- **File every source you use into ****`raw/`**** BEFORE you synthesize from it.** The Phase B material is pre-staged at `/Volumes/MUSIC/PHASE B RAW`; copy the relevant files into the appropriate `raw/<domain>/<collection>/` subdirectory (mirror the existing `raw/` layout — check `search_files` for where similar sources live). Do not leave a source only in Phase B RAW; the wiki must cite a `raw/` path that exists.

- **Extend, never bulldoze.** Earned synthesis already on disk is the product of reasoning done once — revise/build on it, do not regenerate from zero.

- **Cross-corpus [JOIN] findings** (insights that exist in no single corpus, only at the intersection) are the highest-value output. Label them as joins.

- **Behave like a forensic senior-analyst peer, not a helper.** Verify claims against primary data. Flag motivated reasoning both directions. Call logic slips. The operator's own session config (from CONTEXT_CORE_EXPANDED) wants: sycophancy OFF, performed-concern OFF, PRIMARY EVIDENCE = Dan's own data, addiction-framing DISABLED (chemical stack is engineered architecture), metacognition failure mode = the diagnosis→behavior gap (engage the gap, not the insight).

## 4. THE INGEST PROTOCOL (step by step, ONE cluster per pass)

1. **Pick ONE source or tight cluster** from `/Volumes/MUSIC/PHASE B RAW`. Don't parallelize; one pass, fully.

1. **File it into ****`raw/`** (correct subdir, mirroring existing layout). Verify the path exists afterward (`search_files` target=files).

1. **Read it COMPLETELY.** For large docs, paginate with `read_file` offset/limit until you've seen all lines.

1. **Map it to the wiki.** `search_files` the wiki for the entities, dates, and terms the source touches. Identify which existing pages the source would extend. Read those target pages (or the relevant sections) so you extend, not duplicate.

1. **Synthesize as EXTENSION.** Add new connective insight. If the source contradicts or sharpens a wiki figure, apply the contradiction/revision rules: flag it (a `> **REVISED [YYYY-MM-DD]:**` blockquote) and correct the page. Don't silently harmonize discrepancies.

1. **VERIFY NUMBERS FROM RAW.** This is the single most important discipline — see §6 Lesson 1. If a source states a derived rate/volume/count, recompute it from the raw export on disk before trusting it. The operator WILL catch unverified numbers, and was right to.

1. **Update frontmatter** on every touched page:

  - `status:` `stable` → `active` (it's now being actively revised).

  - `date_modified:` → today (`YYYY-MM-DD`).

  - `sources:` → ADD the new `raw/` path you filed (must exist on disk).

  - `related:` → ADD links to pages the new material connects to.

  - For synthesis pages, ensure `knowledge: earned` is set.

1. **Link any NEW page** from the relevant index (e.g. `wiki/mind/index.md` for mind-domain pages). Orphan pages fail the spirit of the project.

1. **Run ****`python3 bin/wiki-lint`****.** Fix every ERROR:

  - broken `wiki/` links (you referenced a page path that doesn't resolve),

  - `sources:` paths that don't exist on disk. WARNINGS (page size, orphans) are advisory and safe to ignore UNLESS your specific page is wildly over budget and splittable — otherwise leave them.

1. **Commit.** `git add -A` then `git commit -m "<op>: <short description>"` — message should name the source filed, the pages changed, and note `bin/wiki-lint: 0 errors`. One focused commit per pass is the established rhythm.

1. **Update ****`LLM_HANDOFF.md`** — append a dated `### [YYYY-MM-DD] - Session:` entry in the established style (see existing entries): model used, summary of sources filed + pages touched + key findings, and a Handoff Note listing the next natural passes. This is mandatory per `CLAUDE.md`.

1. **Push + open PR ONLY when the operator asks.** Otherwise leave the branch local. When asked: `git push -u origin <branch>`, then `gh pr create --base main --head <branch> --title "..." --body "..."`.

## 5. FRONTMATTER SPEC (exact — lint validates this)

Every `wiki/` page has YAML frontmatter. Minimum required:

---

domain: self | timeline | people | mind | work | interests | health | places | legal

page_type: entity | event | concept | period | summary | synthesis | profile | report | chat | note | index

status: active | stable | stub | closed | archived

date_created: YYYY-MM-DD

date_modified: YYYY-MM-DD

sources: []      # REAL raw/ paths that exist on disk — bin/wiki-lint checks this

related: []      # wiki page paths

---

Optional but expected on synthesis/concept pages: `knowledge: earned | derived | mixed`. Lint errors on bad `knowledge` values. `sources:` paths that don't exist → error. `wiki/`-prefixed links that don't resolve → error.

## 6. LESSONS / GOTCHAS (from the 2026-07-15 session — don't repeat)

**Lesson 1 — VERIFY derived numbers against raw. The operator caught a real error.** The Totality source doc claimed "~7 YouTube watches/day." That was computed from a *filtered subset* ("primary-role window"). Recomputed from the raw export on disk (`raw/self/youtube-watch-history/YOUTUBE WATCH HISTORY (2010-2025).html`): **17,426 timestamped watch events / 1,505 distinct active days = 11.58/day** (2007–2025). The real number was HIGHER, which strengthened (not weakened) the constancy thesis. Later, the browser-history corpus *independently* corroborated the fixed-rate thesis on the search side: **20.2 logged actions per active day across 5,391 active days**. Rule: any rate/volume/count stated by a source doc is suspect until you recompute it from the raw export. The operator values this more than agreement.

**Lesson 2 — Confirm corruption on disk before "fixing" it.** OCR'd source docs can show doubled/misspelled tokens in a terminal display (e.g. "announcement", "ambient", "counterpart"). In the 07-15 session, those turned out to be RENDERING artifacts — the file on disk was spelled correctly. Before patching spellings, inspect the real bytes (e.g. an `execute_code` script that prints `[ (c, hex(ord(c))) for c in seg ]`). Don't "correct" what isn't actually corrupted on disk.

**Lesson 3 — Wikilink path discipline.** Reference raw sources as `[[raw/self/.../FILE.md]]` (these pass lint; lint only checks `wiki/` links and source-path existence). Do NOT write `[[wiki/self/concepts/SOURCE]]` pointing at a raw file as if it were a wiki page — that breaks the link check. Use the `raw/` path.

**Lesson 4 — Lint is 0 errors / ~37 warnings, stably.** The warnings are all pre-existing page-size-budget notices on existing pages you didn't create. Don't chase them. Your job is 0 errors.

**Lesson 5 — Source historiography is itself content.** The bootloader doc carried a "v1 withdrew a claim / v2 restored it anchored to confirmed dates" arc. Port the REASONING, not just the conclusion. The correction narrative is part of the earned synthesis.

**Lesson 6 — Check before writing; duplication is a trap.** `DAN_COGNITIVE_PROFILE.txt` (filed in Phase B) is the CONTEXT_CORE_EXPANDED spine already well-ingested across the profile pages. Porting it again would be duplication, not a gap. Before extending, confirm the target page doesn't already carry the material.

**Lesson 7 — This is macOS; the operator is Dan, not Suzanne.** The home directory is `/Users/Suzanne` but that's his mother's machine. Never infer user identity from the path. The operator is Dan Frank throughout.

## 7. WHERE THE WORK STANDS

This runbook deliberately does not carry session state — it went stale twice doing so. Two files hold it, and both are current:

- **`LLM_HANDOFF.md`** — the exact resume point, newest entry at the top, with what the last session found, the gate results, and what to do next.

- **`BACKLOG.md`** — the standing work that outlives any one session: the extraction campaign, structural gaps, named open questions, and the settled decisions that should not be re-litigated.

Machine-maintained queues sit beside them: `queue.md` (pending ingest), `connection-queue.md` (mined edge candidates), `synthesis-queue.md` (mined climb clusters).

## 8. FIRST ACTIONS FOR THE NEXT AGENT

1. Read STRATEGY.md, CLAUDE.md, EXTRACTION_SPEC.md, LLM_HANDOFF.md.

2. git status && git branch -vv        # confirm the branch you should be on

3. bin/wiki-lint | tail -1             # baseline: expect "0 errors"

bin/wiki-connect check | tail -1

bin/wiki-climb check | tail -1

4. bin/capture status                  # what's waiting in inbox/

5. Pick ONE item: the top of LLM_HANDOFF.md's resume point, or one cluster

from BACKLOG.md. One source per pass, fully — never parallel.

6. File the source into raw/, read it TO EXHAUSTION (EXTRACTION_SPEC.md),

map it to wiki pages, re-derive every number from raw, write long,

wire typed edges both ways, run the three gates.

7. Append to log.md as findings; update LLM_HANDOFF.md; commit.

8. Push and open a PR when the operator asks, or per the session's standing

branch instruction.

## 9. DEFINING QUALITY BAR (what "exactly as done" looks like)

- Every quantitative claim traces to a `raw/` path in `sources:`.

- Rates/volumes recomputed from raw exports, not lifted from a doc's prose.

- New material is connective: it links pages, surfaces [JOIN] findings, and sharpens existing earned synthesis — it does not restate what's already there.

- Discrepancies between sources are flagged with `REVISED` blockquotes, not silently merged.

- Lint passes at 0 errors every commit.

- The handoff log gets a real, useful entry so the NEXT model doesn't re-derive settled work.

- **Every finding is written back into the entries it came from** (STRATEGY.md core loop, step 6). A [JOIN] finding that appears only in the synthesis and not on its members has been discovered once rather than permanently — the next model to land on the member page will re-derive it from less evidence. This is the quality bar item most often missed.

- **Coverage counts.** Every data point the source contains gets an entry. A fact read and not written down anywhere is a fact the brain cannot reason with later; a thin `status: stub` page beats an omission.

- Tone: forensic senior peer. Plain human voice in published prose (no LLM neologisms in derived writing). Lengthy and detailed by directive.

## 10. THE STORYTIME-MINING WORKFLOW (codified 2026-07-18 — operator-approved, repeatable)

For retiring `wiki/self/chats/` pages (gemini-XX, j6-chat, 9-11-chat, and the dox-md storytimes). This workflow ran successfully on Gemini-_02 and Gemini-_00 (2026-07-18); follow it exactly:

1. **Scrape the conversation start-to-finish** from its raw/ source (not from the chat wiki page — the page is a lossy summary).

1. **Extract ~50 discrete data points** (dates, names, amounts, claims, corrections). More for dense sources; the operator wants entries LONGER than the current standard.

1. **Operator approval** of the point list before entry (paste the list; wait). Skip only if the operator has pre-approved the batch.

1. **Research each point against the wider raw/ corpus** before writing — cross-check identities (grep all handles), verify numbers, run the contradiction rules against existing pages.

1. **Enter the points** into their proper home pages (person/event/period pages — the main sink is usually a full prose rewrite of one page), with typed `connections:` per CONNECTIONS_SPEC.

1. **Delete the chat page**, repairing every inbound link (`grep -r` first). The chat's content now lives in the wiki proper; the page was scaffolding.

1. Gates (`bin/wiki-lint` + `bin/wiki-connect check`), log.md, commit, and strike the chat from the candidates list in LLM_HANDOFF.md.

Remaining candidates at codification time: gemini-07 (Suzy call), gemini-13 (Bacharach), gemini-18, gemini-21, gemini-58, j6-chat, 9-11-chat, photo-ingest-pinned, extract-messages-pinned, danfrank-isms- pinned, and the dox-md storytimes (Cash register shortage, Drawer shortage, Little Caesars — mined 2026-07-18, verify before re-mining).
