# Skill Changelog

## 2026-09-04 — promoted `repo/silent-permission.md` (active)

**Why now:** the promotion test in `PROTOCOL.md` §3 is "explained the same class of failure more than once", and it has, in two different tools, on the same standing directive. `bin/wiki-plain`'s guard shipped with a word-boundary hole that let `annie_metadata_24h.csv` through; `bin/wiki-crosslink`'s read `scalar(fm, "title")` when **288 of 497 pages carry no ****`title:`**** field**, leaving nine pages about her invisible to it — `annie-record`, `ellen-ulmer`, `shelbie-annie-threesome-april-2019` among them. Neither was found by reading the code. Both looked correct.

**Validated by** `tests/test_wiki_crosslink.py::MoratoriumNameResolution` (five cases, one of them a regression naming all nine real pages) and the existing `tests/test_wiki_plain.py`. Also carries the second-direction rule: a test that only asserts the refusal is satisfied by a guard that refuses everything, and this repository has a measured reason (197 of 497 pages) for one guard being deliberately narrower than the other.

Append-only. Every promotion, revision, deprecation and retirement, with its date and its reason. `PROTOCOL.md` §6 forbids silently changing what a skill means, so a skill that is not named here has entered the corpus with no account of why it should be believed — and `bin/wiki-skills check` fails on exactly that.

## 2026-09-02 — GPT-5.6 Luna handoff

- Added `repo/pr-completion.md` as an active cross-agent completion rule. It makes final-state verification explicit: inspect the final diff, regenerate and gate derived surfaces, verify the target branch and PR, and do not treat a successful write/API response as proof that the requested artifact exists. This operationalizes the repository's existing session-loop, change-safety and derived-surface requirements at the point where an agent is about to say "done".

- Added `corpus/source-chain.md` as an active provenance rule. It carries the existing synthesis and connection specifications into a reusable workflow: preserve the path to raw evidence, distinguish observation from inference, preserve contradictions, and make derived calculations reproducible.

- Registered GPT-5.6 Luna in `skills/registry/manifests/` with its available repository, web, file-retrieval and Python-analysis capabilities. No secret values are recorded.

## 2026-08-30 — the subsystem is wired in

The section shipped earlier today as seven markdown files describing a system that did not exist: `CLAUDE.md` never mentioned `skills/`, so its "mandatory session behavior" was mandatory nowhere, nothing validated the corpus, and nothing surfaced what it was holding. This pass makes it real.

**Tooling and routing**

- Added `bin/wiki-lessons` — `check` (the gate), `scan` (regenerates `INDEX.md`), `route` (runs the routing algorithm rather than describing it), `list`, `status`, `next`, `new`. Written as `bin/wiki-skills` and renamed on merge: `#225` had taken that name the same day for the capability registry, which is a different tool over different data and was already public at `wiki/meta/skills.md`. Two tools, two names: **lessons** are what agents have learned about this repository, **skills** are what a model has.

- `INDEX.md` is now **generated** from the skill files. It previously carried a `Status` column duplicating each file's `status:` frontmatter — two sources of truth for one fact, which is the defect `WORK.md` exists to not have.

- `bin/wiki-lessons check` joined the gate chain in `bin/wiki-check`, and unvalidated inbox candidates now surface as obligations in `bin/wiki-work`.

- `CLAUDE.md` routes at the section: the governing set, the architecture map, the LEARN operation, the tools table and the pre-commit block.

**Promoted to ****`active`** — each traceable to a dated incident already in this repository's record:

- `repo/derived-surfaces.md` — write to the source, never to the surface it generates. Two December 2015 read passes were written into the portal's derived snapshot; one was deleted by the rebuild cron 39 minutes after merging (`log.md`, 2026-08-17). The mirror failure is drift: the 2026-08-20 audit found `llm/manifest.json` eleven pages behind `wiki/`.

- `repo/stale-premise.md` — never clear a staleness warning by bumping the date. Named in `CLAUDE.md` as the one move that corrupts the system quietly; promoted because it is mechanically implied by `bin/wiki-climb check` and `bin/wiki-plain check` (PROTOCOL §3, third clause).

- `corpus/message-mining.md` — use `bin/mine-messages` over grep, and `bin/text-metrics` for anything about length or cadence. Both tools carry the reasoning in their own docstrings: three properties of the dump make naive grep quietly wrong, and message-level counts hide the turn-level effect entirely (3.05x in 2026 against 1.23x in 2015–19).

- `repo/publication-surface.md` — `.gitignore` is not a privacy control; it governs `git add` and never touched the contents API the portal writes through. From the intake ledger's two failed arrangements and the operator's 2026-08-30 decision.

**Recorded, unchanged in substance**

- `repo/session-loop.md` and `repo/change-safety.md` — promoted `active` on 2026-08-30 with the section itself; named here because the gate requires it and their arrival was never recorded.

## 2026-08-30 — the section, and the registry

- Created the canonical `skills/` subsystem for persistent, cross-model operational learning.

- Added routing (`INDEX.md`), lifecycle rules (`PROTOCOL.md`), candidate capture (`INBOX.md`), and initial repository skills.

- Added the registry: `skills/registry/`, an append-only cross-model database of what each model actually has — skills, MCP servers, plugin tools, subagents, harnesses and this repository's own commands. Written by `bin/wiki-skills`, rendered public at `wiki/meta/skills.md`, gated in `bin/wiki-check`. This makes the third mandatory session step in `README.md` a real operation rather than an intention; it had named a "running directory" that did not exist.

- Promoted `agents/registry-push.md` to active — the instruction for a model told to update the skills in the wiki. Seeded with 51 capabilities from one model; the diff view is worth nothing until a second model pushes.

- **2026-09-02 — promoted ****`corpus/vocabulary-drift.md`**** to active.** A keyword count over a long corpus measures the pattern's vocabulary, not the corpus. Promoted on the third occurrence in one session, and the first that reached a page: `wiki/mind/synthesis/2020-left-turn` was published with a "two steps, not one" finding — a 2017 political step separating engagement from identity, and a 2013–2016 off period — and both were withdrawn the same day when re-measurement with era-appropriate vocabulary moved 2016 from 4.0% to 9.3% and 2013 from 1.4% to 7.8%. The two earlier occurrences were near-misses (a music silence off by a year and a start date; 2026 politics reported as 0.0% when it is 23.1%) and were held in `INBOX.md` on the ground that one author on one corpus is not independent confirmation. A defect that reached a synthesis page is different evidence from a near-miss, which is what moved it. Still bounded rather than solved — see the skill's Known limits, and the untested `bin/mine-messages` absence claims it names.

- **2026-09-04 — promoted ****`corpus/source-mention-debt.md`**** to active.** A source's debt to the pages it did not get written onto is invisible from both ends. Promoted on `PROTOCOL.md` §3's second and third tests together rather than on a second occurrence: a command validates it (`bin/wiki-crosslink scan` / `reciprocal`, written the same day), and `STRATEGY.md`'s core loop plus `CONNECTIONS_SPEC.md`'s inverse-edge rule already implied it mechanically — the loop's step 3 and the reciprocal obligation both existed and neither had a tool, an operation, or any way to tell they had been skipped. The occurrence that produced it: nineteen `wiki/self/twitter/` year pages, written across two sessions by reading every tweet in every year and carrying 130 typed edges, had never been read back onto the pages the tweets were about. One scan found four pages whose own stated limits were wrong — a concert log calling itself complete while missing three shows, a person's page saying everything known about her came from AI narration against six contemporaneous posts, a substance row calling itself undated against eighteen years of dated evidence, and a discography short by twenty releases in one year — plus 39 one-way edges, the same defect seen from the other side. Promoted rather than parked because the failure has no symptom: nothing goes red, nothing enters `WORK.md`, and a source that named forty things and got linked to three is indistinguishable from one that named three. A candidate parked in `INBOX.md` would have been found by the same nobody who was already not finding this. Bounded, and the bounds are on the skill: it is string matching over proper nouns, so it cannot see an entity with no page (that is `EXTRACTION_SPEC.md` move 3) and it cannot see a conceptual link at all — which was half of what the operator asked for, and remains a reading job.

## 2026-09-06 — promoted `corpus/lexical-proxy-load.md` (active)

A lexical proxy good enough to start a conversation is not good enough to gate one. Promoted on first authoring rather than parked in `INBOX.md`, because both of `PROTOCOL.md` §3's tests were met inside the session that found it: the same class of failure explained **nine** separate wrong results (six Tier A proxies and three reach patterns, each named in the skill with the string that breaks it), and `tests/test_wiki_traits.py` validates the instruction mechanically — `VerdictCap.test_unreviewed_cannot_contradict` is the regression.

The occasion was `bin/wiki-traits`' first run reporting `CONTRADICTED LOAD` on the Fe deficit — an instruction to re-read 37 pages, 17 of them synthesis — off a proxy whose every match was Dan being comforted rather than comforting. The tool now caps an unreviewed proxy at `silent`, which is the instruction stated as code.
