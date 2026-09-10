# MECHANICAL AUDIT REPORT

Generated: 2026-08-20 · Auditor: Free Agent (Yashuwa) · Revised: 2026-08-20 (review pass) Scope: Phases 0A-0L of the Wiki-Brain mechanical audit Corpus snapshot: **476 pages**, measured at branch commit `5355c0a`

**READ THIS FIRST — what this document is.** Every number below is the output of a mechanical scan. **A string match is not a finding**; it is a candidate that a reasoning pass has to confirm. The review pass found that treating matches as findings had already inflated two headline numbers by roughly an order of magnitude (see *Corrections*). Where a number has survived verification it is marked **verified**; where it has not, it is marked **candidate**. Do not cite an unmarked number.

**Reproducibility.** The scripts that produced most of these reports were not committed and the reports cannot be regenerated. See `reports/README.md` for which are reproducible and which are one-shot snapshots.

## Executive Summary

The wiki has **476 pages** across **9 domains**. The graph is quantitatively healthy (3,323 prose edges) but semantically under-connected: **996 bare ****`related:`**** entries** remain untyped, **36 pages are islanded**, and the LLM manifest is **11 pages stale**.

## Priority Matrix

### P0 — Can silently corrupt or misrepresent knowledge

| **Finding** | **Fix** | **Who** |
| --- | --- | --- |
| **verified** — LLM manifest stale (465 published vs 476 actual) | `bin/wiki-freshness` now detects this deterministically; run `bin/wiki-digest && bin/llm-publish` | Free |
| **verified** — Retracted `$750/week` asserted live on **1** page (`wiki/people/ally-lubin.md`) | Corrected in place 2026-08-20 with the old claim visible per STYLE_GUIDE rule 9 | done |
| **verified** — **4** empty/header-only raw files, **2** cited in `sources:` | `bin/wiki-lint` warns; a human must re-export or de-cite. Never substitute a different file | Human |

### P1 — Materially harms retrieval or provenance

| **Finding** | **Fix** | **Who** |
| --- | --- | --- |
| 996 bare `related:` entries | Convert to typed connections with claims | Claude |
| 68 pages with `## Related` footers | Convert or delete | Claude |
| 36 islanded pages | Wire into graph with typed edges | Claude |
| **candidate** — 30 pages `status: archived` outside `archive/` | **Mechanically unusual, not known to be wrong.** Semantic call only | Claude |
| 215 pages with `date_modified` before 2026-08-01 | Review for currency | Claude |

### P2 — Significant quality improvement

| **Finding** | **Fix** | **Who** |
| --- | --- | --- |
| 2,229 never-cited raw files | Source-mining campaigns | Claude |
| 2169 large never-cited raw files | Prioritize for extraction | Claude |
| **contested** — entity candidates with no page: **788** or **621**, see *Corrections* | Reconcile the two extractions before acting | Claude |

### P3 — Cosmetic / Low value

| **Finding** | **Fix** | **Who** |
| --- | --- | --- |
| Domain pairs with 0 edges (interests <-> legal) | Cross-domain connections | Claude |
| 24 disconnected domain pairs | Build cross-domain tissue | Claude |

## Phase 0 Audit Reports Produced

| **Section** | **Report** | **Status** |
| --- | --- | --- |
| A | corpus-inventory.json + .md | Complete |
| B | generated-drift.md | Complete |
| C | duplicate-frontmatter.md | Complete |
| D | archive-status-audit.md | Complete |
| E | phantom-sources.md | Complete |
| F | retraction-candidates.md | Complete |
| G | connection-retrofit.md | Complete |
| H | synthesis-audit.md | Complete |
| I | source-coverage.md | Complete |
| J | entity-candidates.md | Complete |
| K | islands.md | Complete |
| L | temporal-audit.md | Complete |
| M | llm-feed-audit.md | Complete |

## Free-Agent Safe Work (Phase 1)

Per Section 24 of the plan:

1. Add duplicate YAML key lint to `bin/wiki-lint`

1. Add generated-feed CI freshness check

1. Add retracted-string gate to `bin/wiki-lint`

1. Add master-timeline generation to required precommit

1. Fix stale root counts/index metadata

1. Fix obvious stale documentation

1. Add phantom-source detection

## Claude-Required Work (Phase 2+)

Per Section 28-38 of the plan:

1. Gchat exhaustive extraction (highest ROI)

1. iMessage per-contact CSV sweep

1. 240 connection retrofit (graph candidates)

1. OPEN.md contradiction resolution

1. High-centrality synthesis review

1. People significance audit

1. Interest lifecycle audit

1. Turning-point synthesis

1. Relationship architecture synthesis

1. Current-state page creation

## Do-Not-Touch-Yet

- Agent architecture review (Phase 5) — wait until content work stabilizes

- Vector DB / RAG (Phase 5) — not yet

- MCP server (Phase 5) — not yet

- Fancy search UI (Phase 5) — not yet

## Corrections applied by the 2026-08-20 review pass

The three numbers below were wrong in the first version of this report. All three were wrong the same way: **a mechanical match was reported as a finding.**

### 1. "Retracted `$750/week` figure still on 10 pages" → **1 page**

The scan counted every occurrence of the string. Nine of the ten were *correctly-written corrections* — `STYLE_GUIDE.md` rule 9 requires a correction to keep the retracted claim **visible** — plus one unrelated legitimate `$750` (`wiki/people/david-beard.md`, an Aug 20 price negotiation) and one verbatim quote of the December 2018 accusation the false rate was generalised from, which is primary evidence and must stay.

Exactly **one** page asserted the retracted rate as live fact: `wiki/people/ally-lubin.md`, *"the period whose other documented facts are … $750/week borrowed from his mother."* Corrected 2026-08-20.

The gate in `bin/wiki-lint` now models the *claim* rather than the number and exempts correction contexts. It reproduces this result: **1 error before the fix, 0 after**, with no false positives across 476 pages.

### 2. "Phantom sources (10 files, 5 cited)" → **4 files, 2 cited**

Six of the ten were `.gitkeep` placeholders — empty **by design**, never cited as evidence. The four real ones are listed in `reports/phantom-sources.md`.

The "5 cited" figure came from matching *bare filenames anywhere in page text*. `raw/` holds **3,313 files under 1,430 distinct basenames — 1,041 basenames collide** (`0.html`, `1.html`, thousands of exported images), so a basename can never identify a source. Restricting the check to `sources:` frontmatter citations, which by convention carry repo-relative paths, gives **2** genuine citations of an empty file, both of `END_FIGHT_full.csv` (68 bytes, header only). Pages that *mention* these filenames in prose — `source-coverage-index` catalogues them deliberately — are correctly no longer flagged.

### 3. Entity candidates: **788 vs 621** — unresolved, do not cite either

| **Report** | **Figure** | **Generated** | **Population** |
| --- | --- | --- | --- |
| `reports/entity-candidates.md` | 788 | 2026-08-20 00:33:24 | "3+ mentions, no page", of 3,490 extracted strings |
| `reports/entities/ENTITY_CENSUS.md` | 621 | 2026-08-20 00:45:01 | "3+ mentions, no page", against 542 existing entity pages |

Two extractions twelve minutes apart, same stated criterion, 167 apart. The generating scripts were not committed, so **neither can be reproduced and neither is authoritative.** The review pass deliberately did not invent a third number by re-implementing an unknown algorithm.

Both lists are also visibly noisy at the top — the highest-scoring "entities with no page" are `New York` (195) and `Dan Frank` (161), i.e. a place name and the subject of the entire wiki. Treat the whole list as **unfiltered candidates**, not as a work queue.

**Next step:** write one committed extractor with a stated inclusion rule, run it once, supersede both reports.

## Verification status of every headline number

| **Number** | **Status** | **How to reproduce** |
| --- | --- | --- |
| 476 pages | verified | `bin/wiki-lint` (also `bin/wiki-freshness`) |
| 1 live retracted claim | verified | `bin/wiki-lint` + `RETRACTED.md` |
| 4 empty raw files / 2 cited | verified | `bin/wiki-lint` (warnings) |
| manifest 11 pages behind | verified | `bin/wiki-freshness` |
| 996 bare `related:` / 68 `## Related` / 36 islands | candidate | `bin/wiki-connect audit` (approximate — different tool, may differ) |
| 3,323 prose edges | candidate | not reproducible; script not committed |
| 28 climbed pages (6.1%) | candidate | `bin/wiki-climb audit` |
| 2,229 never-cited raw files | candidate | not reproducible; script not committed |
| 788 / 621 entity candidates | **contested** | not reproducible; see above |
| 30 archived-outside-archive | candidate | `reports/archive-status-audit.md` |
| 215 pages `date_modified` < 2026-08-01 | candidate | not reproducible; script not committed |
