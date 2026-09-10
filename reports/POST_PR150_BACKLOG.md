# Wiki-Brain Post-PR-150 Remediation & Research Backlog

**Generated:** 2026-08-20 **Auditor:** Free Agent (Yashuwa) **Scope:** Mechanical discovery, triage, and prioritization for the next phase of Wiki-Brain improvement after PR #150.

## 1. CURRENT STATE REPORT

### 1.1 Quantitative Snapshot

| **Metric** | **Value** | **Tool** | **Freshness** |
| --- | --- | --- | --- |
| Wiki pages | 476 | `find wiki -name '*.md'` | Live |
| Raw files | 3,316 | `find raw -type f` | Live |
| LLM manifest pages | 465 | `llm/manifest.json` | STALE (should be 476) |
| LLM manifest generated | 2026-08-18 | `llm/manifest.json` | 2 days old |
| DIGEST page count | 470 | `DIGEST.md` | STALE (should be 476) |
| Prose edges | 3,323 | `bin/wiki-connect audit` | Live |
| Avg outdegree | 7.0 | `bin/wiki-connect audit` | Live |
| Typed connections | 1,678 | `bin/wiki-connect audit` | Live |
| Bare `related:` entries | 996 | `bin/wiki-connect audit` | Live |
| Pages with `## Related` footers | 68 | `bin/wiki-connect audit` | Live |
| Islanded pages | 36 | `bin/wiki-connect audit` | Live |
| Pages with `synthesizes:` | 28 | `bin/wiki-climb check` | Live |
| T2 junction pages | 14 | `bin/wiki-climb audit` | Live |
| T3 doctrine pages | 14 | `bin/wiki-climb audit` | Live |
| Domains with no junctions | 3 | `bin/wiki-climb audit` | Live |
| wiki-lint errors | 30 | `bin/wiki-lint` | Live |
| wiki-lint warnings | 24 | `bin/wiki-lint` | Live |
| wiki-climb errors | 9 | `bin/wiki-climb check` | Live |
| Live contradictions | 33 | `DIGEST.md` | From 2026-08-19 |
| Open gaps | 332 | `DIGEST.md` | From 2026-08-19 |
| Standing predictions | 13 | `DIGEST.md` | From 2026-08-19 |
| Never-cited raw files | 2,229 | `reports/source-coverage.md` | From 2026-08-20 |
| Pages modified before Aug 1 | 215 | `reports/temporal-audit.md` | From 2026-08-20 |
| Entity candidates (no page) | 788 | `reports/entity-candidates.md` | From 2026-08-20 |
| Graph candidates in queue | 100 | `reports/graph-candidates/top-100.md` | From 2026-08-20 |

### 1.2 Domains

| **Domain** | **Pages** |
| --- | --- |
| people | 165 |
| interests | 143 |
| mind | 60 |
| self | 40 |
| timeline | 37 |
| work | 15 |
| health | 4 |
| places | 8 |
| legal | 4 |

### 1.3 Known Immediate Problems

1. **LLM manifest stale**: 465 pages vs 476 actual. 11 pages missing.

1. **DIGEST stale**: Says 470 pages, should be 476.

1. **9 ****`sources:`**** → ****`synthesizes:`**** errors**: New pages (personality assessments, ally-and-dan-love-as-destiny, astrology-star-signs) have wiki paths in `sources:` instead of `synthesizes:`.

1. **10 pages contain retracted "$750/week" figure**.

1. **7 pages cite phantom sources** (empty/header-only raw files).

1. **36 islanded pages** (18 are music artist favorites, 5 are LLM entries).

1. **30 pages with ****`status: archived`**** outside ****`archive/`**.

1. **215 pages not modified since before 2026-08-01**.

## 2. TOP 20 HIGHEST-VALUE OPPORTUNITIES

### Priority Formula

Priority ≈ (potential information gained) × (downstream impact) × (likelihood of being real) ÷ (estimated effort)

### The Top 20

| **#** | **TITLE** | **TYPE** | **PRIORITY** | **WHY** |
| --- | --- | --- | --- | --- |
| 1 | Gchat archive extraction (gmail_bodies.txt) | SOURCE_MINING | **HIGHEST** | 902KB, 2010-2013 daily life, only daily record of that period, 495+ conversation blocks. One correspondent's slice reorganized alexis-armel. The rest is unread. |
| 2 | Fix 9 `sources:` → `synthesizes:` errors | MECHANICAL | **HIGH** | Deterministic, low risk, immediately fixes wiki-climb check errors. Affects 4 pages. |
| 3 | Regenerate LLM manifest + DIGEST | MECHANICAL | **HIGH** | Deterministic, low risk. Brings machine-readable projection in sync with wiki. |
| 4 | Retracted "$750/week" correction cascade | QUALITY | **HIGH** | 10 pages carry retracted figure. 2 have correction blocks that never actually changed the text. Requires grep + manual correction. |
| 5 | Per-contact iMessage CSV sweep | SOURCE_MINING | **HIGH** | 16 CSVs, some covering 2022-2026 (absent from main dump). Rick Frank pass reversed a standing figure. Systematic sweep of uncited contacts. |
| 6 | ChatGPT export extraction (9.5MB JSON) | SOURCE_MINING | **HIGH** | dfrank-chatgpt-conversations-2022-2025.json. Contains Dan's own words and self-assessments. Not yet mined. |
| 7 | 36 islanded pages — wire into graph | CONNECTION | **HIGH** | 18 music artist pages reachable only from indexes. Need inbound prose edges or explicit demotion. |
| 8 | 30 pages `status: archived` outside archive/ | QUALITY | **HIGH** | Semantically wrong status makes pages look exempt from correction. 2018-deep-cycle was feeding false claim to timeline. |
| 9 | Contradiction resolution (33 live) | SYNTHESIS | **MEDIUM-HIGH** | OPEN.md lists 33 live contradictions. Resolving them improves model accuracy. |
| 10 | 2025-collapse cluster synthesis | SYNTHESIS | **MEDIUM-HIGH** | Appears in 5 synthesis queue clusters (scores 12.30-13.30). Cross-domain: people, self, timeline, work. |
| 11 | Relationship architecture synthesis | SYNTHESIS | **MEDIUM-HIGH** | Multiple synthesis clusters involve annie-ulmer, alexis-armel, bond-switch-2015, gemini-activity. Pattern worth investigating. |
| 12 | 215 stale pages review | QUALITY | **MEDIUM** | Pages with date_modified before Aug 1. Some may carry outdated claims. |
| 13 | Graph retrofit: 996 bare `related:` entries | CONNECTION | **MEDIUM** | Largest untouched hygiene block. Requires semantic judgment per pair. |
| 14 | Location History mining (50 files, 2014-2023) | SOURCE_MINING | **MEDIUM** | Semantic Location History JSON files. Can verify/falsify timeline claims. |
| 15 | Facebook Messenger HTML extraction | SOURCE_MINING | **MEDIUM** | Contains message-level data. Some already mined for behavioral findings. |
| 16 | Entity disambiguation (788 candidates) | ENTITY | **MEDIUM** | 788 entities with 3+ mentions and no page. Top candidates: New York (195), Dan Frank (161), Gazette Pavilion (161), Fayette County (148), Full Sail (128). |
| 17 | Interest evolution synthesis | SYNTHESIS | **MEDIUM** | Clusters 11, 13, 22 involve interests-as-era-markers, stand-up-comedy, video-games, teen-concert-years. |
| 18 | People significance audit | QUALITY | **MEDIUM** | 165 people pages. Dozens appear to be peripheral (1 mention, no temporal span). |
| 19 | OPEN.md gap closure (332 open gaps) | SOURCE_MINING | **MEDIUM-MEDIUM** | Many gaps name specific sources that could settle them. |
| 20 | Master timeline regeneration | MECHANICAL | **MEDIUM** | 599KB, generated by wiki-timeline. Should be in pre-commit block per BACKLOG. |

## 3. HIGH-VALUE SOURCE-MINING CAMPAIGNS

### 3.1 Campaign A: Gchat Archive (HIGHEST ROI)

- **Source:** `raw/self/dox-scan/gmail_bodies.txt`

- **Size:** 902 KB

- **Format:** Plain text chat archive

- **Date coverage:** ~2010-2013

- **Unique value:** Only *daily-life* record of 2010-2013. Everything else from that period is retrospective.

- **Evidence:** One correspondent's slice (495 conversation blocks under `lexieamb@gmail.com`) was read in August 2026 and reorganized `alexis-armel`. The rest is unread.

- **Work plan:**

  1. Read entire file to exhaustion

  1. Identify all named people

  1. Identify all dates or date bounds

  1. Identify all events, work, relationships, interests

  1. Contradict existing wiki claims where found

- **Recommended agent:** Claude (requires exhaustion reading, not mechanical)

### 3.2 Campaign B: Per-Contact iMessage CSV Sweep

- **Source:** `raw/self/message-csv/*_both_all_now.csv` (16 files)

- **Size range:** 2.8 KB → 19 MB

- **Format:** CSV

- **Date coverage:** Varies; some cover 2022-2026 (absent from main dump)

- **Unique value:** Most complete two-sided relationship records. Per-contact exports often contain messages absent from general dumps.

- **Evidence:** Rick Frank pass found a CSV that had never been cited anywhere and reversed a standing figure.

- **Work plan:**

  1. For each CSV, resolve phone number against a person page

  1. Check against that page's `sources:` list

  1. For uncited contacts, read the full CSV

  1. Reconstruct chronology and relationship patterns

  1. Cross-check against existing wiki claims

- **Recommended agent:** Claude (requires reading and cross-checking)

### 3.3 Campaign C: ChatGPT Export Extraction

- **Source:** `raw/self/chatgpt-export/dfrank-chatgpt-conversations-2022-2025.json`

- **Size:** 9.5 MB

- **Format:** JSON

- **Date coverage:** 2022-2025

- **Unique value:** Contains Dan's own words, self-assessments, and corrections. Often the only place certain thoughts are recorded.

- **Evidence:** Not yet mined. AI-secondary source (Dan's words are primary testimony; model's assertions are not).

- **Work plan:**

  1. Parse JSON structure

  1. Identify conversations containing Dan's own words

  1. Extract self-assessments, corrections, and testimony

  1. Attribute AI-generated material as such

  1. Write findings into relevant pages

- **Recommended agent:** Claude (requires understanding context and attribution)

### 3.4 Campaign D: Dox-Scan RTF/TXT Files

- **Sources:**

  - `raw/self/dox-scan/Shelbie Breakiron on 2019-04-17 at 16.08.35.rtf` (17.3 MB)

  - `raw/self/dox-scan/Untitled copy.rtf` (2.5 MB)

  - `raw/self/dox-scan/fullcombo 2.txt` (207 KB)

  - `raw/self/dox-scan/STYLE_MAP.rtf` (151 KB)

  - `raw/self/dox-scan/okay now i want you to consolidate everything you....rtf` (467 KB)

- **Format:** RTF/TXT

- **Date coverage:** Unknown (not yet read)

- **Unique value:** Unknown size of find. Could contain interview transcripts, dossiers, or other rich material.

- **Recommended agent:** Claude (requires reading)

### 3.5 Campaign E: Semantic Location History

- **Source:** `raw/self/location/2026-06-22-ingest/Location History (Timeline)/Semantic Location History/`

- **Files:** ~50 JSON files covering 2014-2023

- **Format:** JSON

- **Date coverage:** 2014-2023

- **Unique value:** Can verify/falsify timeline claims about where Dan was at specific times.

- **Evidence:** Residence timeline has gaps (spring-summer 2018 sleeping location unresolved).

- **Work plan:**

  1. Parse JSON for location clusters

  1. Map to timeline periods

  1. Resolve open gaps (e.g., spring-summer 2018)

- **Recommended agent:** Either (deterministic parsing + Claude for interpretation)

### 3.6 Campaign F: Facebook Messenger HTML

- **Source:** `raw/self/facebook/facebook-ihatedanfrank/`

- **Files:** Multiple HTML files

- **Size:** 82 MB zip + extracted HTML

- **Unique value:** Message-level data from Facebook. Some already mined for behavioral findings (contact-gini, message-circadian-latency).

- **Evidence:** BACKLOG.md notes behavioral mining over lexical has produced strongest findings.

- **Recommended agent:** Claude (requires parsing HTML and extracting behavioral patterns)

### 3.7 Campaign G: Notes & Unfiled Documents

- **Sources:**

  - `raw/self/notes/drawer-dispute.md` (174 KB)

  - `raw/self/notes/manipulation-ethics.md` (144 KB)

  - `raw/self/notes/jimmy-pop.md` (139 KB)

  - `raw/self/dox-md/Little Caesars retaliation timing concerns (1).md` (113 KB)

  - `raw/self/dox-md/_AI_Protocol_for_Persuasion.md` (125 KB)

- **Format:** Markdown

- **Unique value:** Unfiled captures. Could contain operator testimony, corrections, or new evidence.

- **Recommended agent:** Claude (requires reading and integration)

## 4. ENTITY GAP REPORT

### 4.1 Top Entity Candidates (by mention count)

| **Entity** | **Mentions** | **Likely Domain** | **Notes** |
| --- | --- | --- | --- |
| New York | 195 | places | Not a person. Geographic entity. |
| Dan Frank | 161 | self | Already has dan-frank.md. |
| Gazette Pavilion | 195 | places | Concert venue. |
| Fayette County | 148 | places | Geographic. |
| Full Sail | 128 | work/education | University. |
| Westmoreland Fairgrounds | 119 | places | Concert venue. |
| Rolling Rock Town Fair | 114 | interests/event | Music festival. |
| Au Za | 113 | work | Restaurant (au-zaatar). |
| Claude Code | 91 | self/concepts | Already has page. |
| Vans Warped Tour | 88 | interests/event | Music festival. |

### 4.2 Entities Likely Needing Pages

| **Entity** | **Mentions** | **Likely Domain** | **Notes** |
| --- | --- | --- | --- |
| Rolling Rock Town Fair | 114 | interests/event | Major recurring event in corpus. |
| Vans Warped Tour | 88 | interests/event | Major recurring event. |
| Full Sail | 128 | work/education | University attended. |
| Gazette Pavilion | 195 | places | Concert venue. |
| Westmoreland Fairgrounds | 119 | places | Concert venue. |

### 4.3 Entities Probably Not Needing Pages

| **Entity** | **Mentions** | **Reason** |
| --- | --- | --- |
| New York | 195 | Geographic descriptor, not entity. |
| Dan Frank | 161 | Already has page. |
| Fayette County | 148 | Geographic descriptor. |
| Au Za | 113 | Already has au-zaatar.md. |
| Claude Code | 91 | Already has page. |

### 4.4 Work Plan

1. Review top 50 entity candidates in `reports/entity-candidates.md`

1. For each, determine if a page already exists under a different name

1. For genuine gaps, prioritize by mention count × number of source files

1. Create pages for highest-value missing entities

1. Add aliases to existing pages for alternate names

## 5. TIMELINE GAP REPORT

### 5.1 Pages Not Modified Since Before August 2026 (215 pages)

These pages may carry outdated claims. Key clusters:

- **June 2022:** self/twitter.md, self/chats/photo-ingest-pinned.md, interests/favorites/books/topics/*.md

- **June 2023:** self/favorites.md, self/facebook/*.md, work/tech/imessage-tooling/*.md

- **July 2023:** people/kim.md, people/felix.md, interests/favorites/music/artists/*.md

- **July 2024:** self/overview.md, work/index.md, work/tech/vibe-coding-games.md

- **July 2025:** interests/gore-vidal.md, interests/film-canon.md, interests/roman-republic.md

- **July 2026:** mind/psychosexual/*.md, mind/profile/*.md, mind/synthesis/*.md, people/*.md

### 5.2 Known Temporal Gaps (from LLM_HANDOFF.md and BACKLOG.md)

| **Gap** | **Status** | **Source** |
| --- | --- | --- |
| Spring-summer 2018 sleeping location | Unresolved | LLM_HANDOFF.md |
| Dec 1-31 Annie entries corrections | Not started | LLM_HANDOFF.md |
| 2021-2022 near-silence | Open question | STRATEGY.md |
| Why Suz thread collapsed July 2026 | Unresolved | LLM_HANDOFF.md |
| 463-morgantown mechanics-lien deadline | Elapsed, unobserved | BACKLOG.md |
| Coles two-address holding (22 months) | Unexplained | BACKLOG.md |

## 6. CONNECTION GAP REPORT

### 6.1 Quantitative

| **Metric** | **Value** |
| --- | --- |
| Bare `related:` entries | 996 |
| Pages with `## Related` footers | 68 |
| Islanded pages | 36 |
| Graph candidates in queue | 100 |

### 6.2 Islanded Pages (36)

**Music artist favorites (18):** angels-and-airships, bloc-party, codeseven, every-avenue, guster, head-automatica, mayday-parade, rilo-kiley, saosin, terminal, the-academy-is, the-dresden-dolls, the-early-november, the-hush-sound, the-maine, the-subways, vertical-horizon, we-the-kings

**LLM entries (5):** chatgpt, claude-code, claude, gemini, wiki-brain

**Other (13):** annie-ulmer-personality-assessment, brennan-meadows, bruce-burish, matt-kraus, nathan-king, suzanne-frank-personality-assessment, tom-wallisch, 9-11-chat, photo-ingest-pinned, astrology-star-signs, master-timeline, vibe-coding-games

### 6.3 Mechanically Convertible

Pairs from `connection-queue.md` with strong evidence:

| **Score** | **Page A** | **Page B** | **Evidence** |
| --- | --- | --- | --- |
| 12.9 | danielle-onesi | timeline/events/timeline.md | 3 shared sources, co-citation, shared tags |
| 12.6 | dan-annie-fallout-verdict | group-chat-closure | 4 shared sources, co-citation |
| 12.2 | vertical-authority-skepticism | self/context-core | shared source, co-cited from 19 pages |
| 11.9 | self/context-core | timeline/events/timeline.md | 2 shared sources |
| 11.2 | node-locking | gemini-activity | shared source, co-citation |

### 6.4 Requires Semantic Judgment

Most of the 996 bare `related:` entries. Determining type and writing claims requires reading both pages.

## 7. SYNTHESIS CANDIDATES

### 7.1 From Synthesis Queue (Top 10 Unclimbed Clusters)

| **#** | **Score** | **Domains** | **Members** | **Candidate Pattern** |
| --- | --- | --- | --- | --- |
| 1 | 14.15 | mind, people, self | phenomenology-lens, alexis-armel, annie-ulmer, core | Self-model as instrument |
| 4 | 13.50 | people, self | alexis-armel, annie-ulmer, core, gemini-activity | NY partners as informational environment |
| 6 | 13.50 | interests, timeline | mogzart, 2015-2016-annie-start, 2017-poverty-floor | Musical aliases as era-markers |
| 7 | 13.30 | people, self, timeline | annie-ulmer, eli, gemini-07, gemini-activity, 2025-collapse | AI as witness during collapse |
| 9 | 12.90 | people, self, timeline | alexis-armel, self/facebook, 2010s | NY social infrastructure |
| 10 | 12.90 | people, self, timeline | annie-ulmer, gemini-activity, 2015-2016-annie-start, 2017-poverty-floor | Partner transition mechanics |
| 11 | 12.90 | interests, mind, timeline | stand-up-comedy, interests-as-era-markers, teen-concert-years | Interest lifecycle |
| 12 | 12.90 | people, self, timeline | alexis-armel, annie-ulmer, gemini-activity, 2015-2016-annie-start | Partner overlap period |
| 13 | 12.90 | interests, mind, timeline | video-games, interests-as-era-markers, teen-concert-years | Digital entertainment as era-marker |
| 15 | 12.55 | mind, people, timeline | bond-switch-2015, alexis-armel, 2010s, uniontown-return | 2015 as pivot year |

### 7.2 Hand-Registered Candidates (from synthesis-queue.md)

1. **Information control as intimacy** — annie-ulmer, alexis-armel, annie-record, bond-switch-2015. Dan manages what partners know about previous partners. Three dated instances in 5 weeks. Held pending fourth instance and Dec corrections pass.

1. **The unaimable engine** — acquisition-drive, the-fall-of-fran, uniontown-hospital-vape-alarm, fran-death-vigil, 2015-retail-theft-arrest, big-five-psychometrics. Self-generated goals vs externally assigned. Falsified by employment record; replaced by the-embedded-objective.

## 8. QUICK WINS FOR CHEAP AGENTS

These are deterministic, low-risk, high-confidence changes that do NOT require semantic judgment.

### 8.1 Fix `sources:` → `synthesizes:` Errors (9 errors)

| **Page** | **Current** | **Should Be** |
| --- | --- | --- |
| wiki/people/annie-ulmer-personality-assessment.md | `sources: [wiki/people/annie-ulmer.md]` | `synthesizes: [wiki/people/annie-ulmer.md]` |
| wiki/people/suzanne-frank-personality-assessment.md | `sources: [wiki/people/suzanne-frank.md]` | `synthesizes: [wiki/people/suzanne-frank.md]` |
| wiki/self/concepts/ally-and-dan-love-as-destiny.md | `sources: [wiki/people/ally-lubin.md, ...]` | `synthesizes: [wiki/people/ally-lubin.md, ...]` |
| wiki/self/concepts/astrology-star-signs.md | `sources: [wiki/people/ally-lubin.md, ...]` | `synthesizes: [wiki/people/ally-lubin.md, ...]` |

**Action:** Move wiki paths from `sources:` to `synthesizes:` on 4 pages.

### 8.2 Regenerate LLM Manifest

**Action:** Run `bin/llm-publish` and commit the diff. Brings manifest from 465 to 476 pages.

### 8.3 Regenerate DIGEST/RECENT/OPEN

**Action:** Run `bin/wiki-digest` and commit the diff. Updates page count from 470 to 476.

### 8.4 Fix Broken Wikilinks

| **Page** | **Broken Link** | **Likely Target** |
| --- | --- | --- |
| wiki/people/diane-moore.md | [[wiki/people/dave-moore]] | wiki/people/dave-moore.md (remove backslash) |
| wiki/self/concepts/astrology-star-signs.md | [[wiki/self/concepts/dan-as-scorpio]] | Does not exist |
| wiki/self/message-corpora/master-message-dump.md | [[wiki/people/zaco]] | Does not exist |
| wiki/self/message-corpora/master-message-dump.md | [[wiki/people/contacts/]] | Directory does not exist |
| wiki/timeline/2015-annie-read-wiki-impact-analysis.md | [[wiki/…]] | Malformed link |
| wiki/timeline/annie-read-notes.md | [[wiki/…]] (3 instances) | Malformed links |

**Action:** Fix or remove broken links.

### 8.5 Wire Orphan Pages (4 critical)

| **Page** | **Issue** | **Action** |
| --- | --- | --- |
| wiki/people/annie-ulmer-personality-assessment.md | Orphan, no inbound links | Add `instantiates` edge from wiki/people/annie-ulmer.md |
| wiki/people/suzanne-frank-personality-assessment.md | Orphan, no inbound links | Add `instantiates` edge from wiki/people/suzanne-frank.md |
| wiki/self/concepts/astrology-star-signs.md | Orphan, no inbound links | Add `evidenced-by` edge from wiki/people/ally-lubin.md |
| wiki/self/concepts/ally-and-dan-love-as-destiny.md | Already connected | None needed |

### 8.6 Retracted String Fixes (10 pages)

| **Page** | **Retracted Strings** | **Action** |
| --- | --- | --- |
| wiki/legal/463-morgantown.md | $750/week, $750 | Replace with correct figure |
| wiki/mind/synthesis/estate-money-spine.md | $750/week, $750 | Replace with correct figure |
| wiki/mind/synthesis/supply-network.md | $750/week, $750 | Replace with correct figure |
| wiki/mind/synthesis/totality-themes.md | $750/week, $750 | Replace with correct figure |
| wiki/people/alexander-jackson.md | $750/week, $750 | Replace with correct figure |
| wiki/people/ally-lubin.md | $750/week, $750 | Replace with correct figure |
| wiki/people/david-beard.md | $750 | Replace with correct figure |
| wiki/people/suzanne-frank.md | $750/week, $750 | Replace with correct figure |
| wiki/self/concepts/claude.md | $750/week, $750 | Replace with correct figure |
| wiki/timeline/periods/2018-deep-cycle.md | $750/wk, $750 | Replace with correct figure |

**Note:** Some pages may have correction blocks that quoted the incorrect sentence without actually changing it. Requires reading each page.

### 8.7 Phantom Source Fixes (7 pages)

| **Page** | **Phantom Source** | **Action** |
| --- | --- | --- |
| wiki/mind/synthesis/bond-switch-2015.md | annie_group_chat_may31-june1_2026.csv | Flag citation as relying on empty source |
| wiki/mind/synthesis/dan-annie-fallout-verdict.md | END_FIGHT_full.csv | Flag citation as relying on empty source |
| wiki/self/message-corpora/master-message-dump.md | annie_group_chat_relaxed.csv, annie_group_chat_may31-june1_2026.csv, END_FIGHT_full.csv | Flag citations |
| wiki/self/message-corpora/source-coverage-index.md | 4 phantom sources | Flag citations |

**Note:** Per BACKLOG.md, do NOT delete the empty files. raw/ is immutable.

### 8.8 Fix `status: archived` Outside `archive/` (30 pages)

**Action:** For each page with `status: archived` outside `archive/`:

- If genuinely finished: change to `status: stable`

- If pinned artifact: move to `archive/` subdirectory

## 9. CLAUDE-ONLY RESEARCH QUEUE

For each item, a cheap agent should NOT do this because it requires interpretation, chronology reconstruction, entity disambiguation, causal analysis, or deciding whether evidence supports a claim.

### 9.1 Source Mining

| **Item** | **Why Claude** |
| --- | --- |
| Gchat archive extraction (gmail_bodies.txt) | Requires exhaustion reading, chasing proper nouns, noting contradictions |
| Per-contact iMessage CSV sweep | Requires reading full CSVs, reconstructing chronologies, cross-checking |
| ChatGPT export extraction | Requires understanding context, attributing AI vs human material |
| Dox-scan RTF/TXT files | Requires reading long documents, extracting findings |
| Semantic Location History | Requires parsing JSON, mapping to timeline, resolving gaps |
| Facebook Messenger HTML | Requires parsing HTML, extracting behavioral patterns |

### 9.2 Entity Work

| **Item** | **Why Claude** |
| --- | --- |
| Entity disambiguation (788 candidates) | Requires deciding if mentions refer to same entity, merging, or creating pages |
| Identity resolution | Requires cross-checking contact exports, name variants, handles |

### 9.3 Timeline Work

| **Item** | **Why Claude** |
| --- | --- |
| Spring-summer 2018 sleeping location | Requires reading message logs, reconciling conflicting addresses |
| Dec 1-31 Annie entries corrections | Requires reading, correcting, flagging |
| 2021-2022 near-silence explanation | Requires investigating absence of evidence |
| Suz thread collapse July 2026 | Requires reading messages before/after, identifying cause |

### 9.4 Synthesis Work

| Item | Why Claude | |---|---|---| | 2025-collapse cluster synthesis | Requires reading member pages, finding governing rule | | Relationship architecture synthesis | Requires reading partner pages, identifying patterns | | Interest evolution synthesis | Requires reading interest pages, identifying lifecycle | | Information control as intimacy | Requires reading dated instances, evaluating generalization | | NY partners as informational environment | Requires reading alexis-armel, annie-ulmer, gemini-activity |

### 9.5 Contradiction Resolution

| Item | Why Claude | |---|---|---| | 33 live contradictions (OPEN.md) | Requires reading conflicting claims, evaluating evidence, deciding which governs |

## 10. PRIORITIZED MASTER BACKLOG

### Format

Each item contains: ID, TITLE, TYPE, PRIORITY, STATUS, WHY_IT_MATTERS, EVIDENCE, AFFECTED_AREAS, ESTIMATED_EFFORT, RECOMMENDED_AGENT, DEPENDENCIES, NOTES.

### P0 — Immediate (deterministic, low risk)

**B-001:** Fix 9 `sources:` → `synthesizes:` errors

- TYPE: MECHANICAL | PRIORITY: P0 | STATUS: OPEN

- WHY_IT_MATTERS: Fixes wiki-climb check errors. Brings new pages into compliance with STYLE_GUIDE.md.

- EVIDENCE: `wiki-climb check` reports 9 errors

- AFFECTED_AREAS: 4 pages (personality assessments x2, ally-and-dan-love-as-destiny, astrology-star-signs)

- ESTIMATED_EFFORT: 5 minutes

- RECOMMENDED_AGENT: CHEAP_AGENT

- DEPENDENCIES: None

- NOTE: Move wiki paths from `sources:` to `synthesizes:`

**B-002:** Regenerate LLM manifest

- TYPE: MECHANICAL | PRIORITY: P0 | STATUS: OPEN

- WHY_IT_MATTERS: LLM manifest is 11 pages stale. Machine-readable projection should match wiki.

- EVIDENCE: manifest.json shows 465 pages, wiki has 476

- AFFECTED_AREAS: llm/manifest.json, llm/index.txt, llm/corpus.txt, llm/pages/

- ESTIMATED_EFFORT: 2 minutes

- RECOMMENDED_AGENT: CHEAP_AGENT

- DEPENDENCIES: None

- NOTE: Run `bin/llm-publish` and commit

**B-003:** Regenerate DIGEST/RECENT/OPEN

- TYPE: MECHANICAL | PRIORITY: P0 | STATUS: OPEN

- WHY_IT_MATTERS: DIGEST says 470 pages, should be 476.

- EVIDENCE: DIGEST.md shows "Pages | 470"

- AFFECTED_AREAS: DIGEST.md, RECENT.md, OPEN.md

- ESTIMATED_EFFORT: 2 minutes

- RECOMMENDED_AGENT: CHEAP_AGENT

- DEPENDENCIES: None

- NOTE: Run `bin/wiki-digest` and commit

**B-004:** Fix broken wikilinks

- TYPE: MECHANICAL | PRIORITY: P0 | STATUS: OPEN

- WHY_IT_MATTERS: Broken links harm navigation and agent retrieval.

- EVIDENCE: `wiki-lint` warnings

- AFFECTED_AREAS: 6 pages

- ESTIMATED_EFFORT: 10 minutes

- RECOMMENDED_AGENT: CHEAP_AGENT

- DEPENDENCIES: None

- NOTE: Fix backslash in dave-moore link, remove malformed [[wiki/…]] links

### P1 — High (high information value, some judgment required)

**B-005:** Retracted "$750/week" correction cascade

- TYPE: QUALITY | PRIORITY: P1 | STATUS: OPEN

- WHY_IT_MATTERS: 10 pages carry retracted figure. 2 have correction blocks that never changed the text.

- EVIDENCE: `wiki-lint` reports 19 retracted string errors across 10 pages

- AFFECTED_AREAS: legal/463-morgantown.md, mind/synthesis/estate-money-spine.md, supply-network.md, totality-themes.md, people/alexander-jackson.md, ally-lubin.md, david-beard.md, suzanne-frank.md, self/concepts/claude.md, timeline/periods/2018-deep-cycle.md

- ESTIMATED_EFFORT: 1-2 hours

- RECOMMENDED_AGENT: CLAUDE

- DEPENDENCIES: None

- NOTE: Correct figure is ~$14,000 from Dan to her in Aug-Oct 2018. Some pages may need CORRECTED block.

**B-006:** Gchat archive extraction

- TYPE: SOURCE_MINING | PRIORITY: P1 | STATUS: OPEN

- WHY_IT_MATTERS: Largest under-mined source. Only daily-life record of 2010-2013. One slice reorganized alexis-armel.

- EVIDENCE: 902KB, ~495 conversation blocks, only lexieamb slice read

- AFFECTED_AREAS: Multiple pages across self/, people/, timeline/

- ESTIMATED_EFFORT: 4-8 hours

- RECOMMENDED_AGENT: CLAUDE

- DEPENDENCIES: None

- NOTE: Highest ROI campaign per STRATEGY.md

**B-007:** Per-contact iMessage CSV sweep

- TYPE: SOURCE_MINING | PRIORITY: P1 | STATUS: OPEN

- WHY_IT_MATTERS: 16 per-contact CSVs. Rick Frank pass reversed a standing figure. Systematic sweep could find more.

- EVIDENCE: 16 files, some covering 2022-2026

- AFFECTED_AREAS: people/ pages for each contact

- ESTIMATED_EFFORT: 2-4 hours

- RECOMMENDED_AGENT: CLAUDE

- DEPENDENCIES: None

- NOTE: Cross-check each number against person page sources:

**B-008:** ChatGPT export extraction

- TYPE: SOURCE_MINING | PRIORITY: P1 | STATUS: OPEN

- WHY_IT_MATTERS: 9.5MB of Dan's own words and self-assessments. Not yet mined.

- EVIDENCE: dfrank-chatgpt-conversations-2022-2025.json

- AFFECTED_AREAS: Multiple pages across self/, people/, mind/

- ESTIMATED_EFFORT: 2-4 hours

- RECOMMENDED_AGENT: CLAUDE

- DEPENDENCIES: None

- NOTE: Attribute AI-generated material as such per EXTRACTION_SPEC.md

**B-009:** Wire 36 islanded pages into graph

- TYPE: CONNECTION | PRIORITY: P1 | STATUS: OPEN

- WHY_IT_MATTERS: 36 pages reachable only from indexes. Agents can't discover them via graph traversal.

- EVIDENCE: `wiki-connect audit` shows 36 islanded pages

- AFFECTED_AREAS: interests/favorites/music/artists/ (18), self/concepts/ (5), people/ (4), other (9)

- ESTIMATED_EFFORT: 1-2 hours

- RECOMMENDED_AGENT: EITHER

- DEPENDENCIES: None

- NOTE: Some music artist pages may be intentionally index-only. Verify before wiring.

**B-010:** Fix 30 pages with `status: archived` outside archive/

- TYPE: QUALITY | PRIORITY: P1 | STATUS: OPEN

- WHY_IT_MATTERS: Semantically wrong status makes pages look exempt from correction. 2018-deep-cycle was feeding false claim to timeline.

- EVIDENCE: 30 pages identified in archive-status-audit.md

- AFFECTED_AREAS: interests/favorites/ (12), self/chats/ (5), people/ (4), timeline/ (2), other (7)

- ESTIMATED_EFFORT: 30 minutes

- RECOMMENDED_AGENT: CLAUDE

- DEPENDENCIES: None

- NOTE: Change to `stable` or move to `archive/` subdirectory

### P2 — Medium (significant value, more effort)

**B-011:** Dox-scan RTF/TXT file extraction

- TYPE: SOURCE_MINING | PRIORITY: P2 | STATUS: OPEN

- WHY_IT_MATTERS: 5 large RTF/TXT files with unknown content. Could contain interview transcripts or dossiers.

- EVIDENCE: Shelbie Breakiron (17.3MB), Untitled copy (2.5MB), fullcombo 2.txt (207KB), STYLE_MAP.rtf (151KB), consolidate rtf (467KB)

- AFFECTED_AREAS: people/, timeline/, mind/

- ESTIMATED_EFFORT: 2-4 hours

- RECOMMENDED_AGENT: CLAUDE

- DEPENDENCIES: None

**B-012:** Semantic Location History mining

- TYPE: SOURCE_MINING | PRIORITY: P2 | STATUS: OPEN

- WHY_IT_MATTERS: Can verify/falsify timeline claims. 50 JSON files covering 2014-2023.

- EVIDENCE: ~50 files in raw/self/location/

- AFFECTED_AREAS: timeline/, places/

- ESTIMATED_EFFORT: 2-3 hours

- RECOMMENDED_AGENT: EITHER

- DEPENDENCIES: None

**B-013:** 2025-collapse cluster synthesis

- TYPE: SYNTHESIS | PRIORITY: P2 | STATUS: OPEN

- WHY_IT_MATTERS: Appears in 5 synthesis queue clusters. Cross-domain pattern.

- EVIDENCE: Clusters 7, 18, 19, 20, 21 (scores 12.30-13.30)

- AFFECTED_AREAS: people/annie-ulmer, self/gemini-activity, timeline/2025-collapse, work/au-zaatar

- ESTIMATED_EFFORT: 2-3 hours

- RECOMMENDED_AGENT: CLAUDE

- DEPENDENCIES: None

**B-014:** Relationship architecture synthesis

- TYPE: SYNTHESIS | PRIORITY: P2 | STATUS: OPEN

- WHY_IT_MATTERS: Multiple clusters involve partner transitions, block/unblock, dormancy.

- EVIDENCE: Clusters 4, 5, 10, 12

- AFFECTED_AREAS: people/annie-ulmer, alexis-armel, mind/synthesis/block-unblock-loop, dormancy-not-exit

- ESTIMATED_EFFORT: 2-3 hours

- RECOMMENDED_AGENT: CLAUDE

- DEPENDENCIES: None

**B-015:** Graph retrofit: convert bare `related:` to typed connections

- TYPE: CONNECTION | PRIORITY: P2 | STATUS: OPEN

- WHY_IT_MATTERS: 996 bare entries. Largest untouched hygiene block.

- EVIDENCE: `wiki-connect audit`

- AFFECTED_AREAS: All domains

- ESTIMATED_EFFORT: 4-8 hours

- RECOMMENDED_AGENT: CLAUDE

- DEPENDENCIES: None

- NOTE: Process in priority order: cross-domain first, then high-centrality pages

**B-016:** Entity disambiguation (top 50 candidates)

- TYPE: ENTITY | PRIORITY: P2 | STATUS: OPEN

- WHY_IT_MATTERS: 788 entity candidates. Top: New York (195), Dan Frank (161), Gazette Pavilion (161).

- EVIDENCE: reports/entity-candidates.md

- AFFECTED_AREAS: people/, places/, interests/

- ESTIMATED_EFFORT: 2-4 hours

- RECOMMENDED_AGENT: CLAUDE

- DEPENDENCIES: None

**B-017:** 215 stale pages review

- TYPE: QUALITY | PRIORITY: P2 | STATUS: OPEN

- WHY_IT_MATTERS: Pages with date_modified before Aug 1 may carry outdated claims.

- EVIDENCE: reports/temporal-audit.md

- AFFECTED_AREAS: All domains

- ESTIMATED_EFFORT: 2-4 hours

- RECOMMENDED_AGENT: CLAUDE

- DEPENDENCIES: None

**B-018:** OPEN.md contradiction resolution (33 live)

- TYPE: SYNTHESIS | PRIORITY: P2 | STATUS: OPEN

- WHY_IT_MATTERS: 33 live contradictions indicate model disagreements. Resolving improves accuracy.

- EVIDENCE: OPEN.md

- AFFECTED_AREAS: Various

- ESTIMATED_EFFORT: 3-6 hours

- RECOMMENDED_AGENT: CLAUDE

- DEPENDENCIES: None

**B-019:** Interest evolution synthesis

- TYPE: SYNTHESIS | PRIORITY: P2 | STATUS: OPEN

- WHY_IT_MATTERS: Clusters 11, 13, 22 involve interests-as-era-markers. Longitudinal pattern.

- EVIDENCE: synthesis-queue.md

- AFFECTED_AREAS: interests/, timeline/, mind/synthesis/interests-as-era-markers

- ESTIMATED_EFFORT: 1-2 hours

- RECOMMENDED_AGENT: CLAUDE

- DEPENDENCIES: None

**B-020:** Notes & unfiled documents extraction

- TYPE: SOURCE_MINING | PRIORITY: P2 | STATUS: OPEN

- WHY_IT_MATTERS: Unfiled captures could contain operator testimony or corrections.

- EVIDENCE: drawer-dispute.md (174KB), manipulation-ethics.md (144KB), jimmy-pop.md (139KB), Little Caesars (113KB), AI_Protocol (125KB)

- AFFECTED_AREAS: Various

- ESTIMATED_EFFORT: 1-2 hours

- RECOMMENDED_AGENT: CLAUDE

- DEPENDENCIES: None

### P3 — Lower priority (lower value or very high effort)

**B-021:** Facebook Messenger HTML extraction

- TYPE: SOURCE_MINING | PRIORITY: P3 | STATUS: OPEN

- WHY_IT_MATTERS: Message-level data. Some already mined for behavioral findings.

- EVIDENCE: raw/self/facebook/

- AFFECTED_AREAS: people/, self/

- ESTIMATED_EFFORT: 4-8 hours

- RECOMMENDED_AGENT: CLAUDE

- DEPENDENCIES: None

**B-022:** People significance audit

- TYPE: QUALITY | PRIORITY: P3 | STATUS: OPEN

- WHY_IT_MATTERS: 165 people pages. Many may be peripheral.

- EVIDENCE: 165 pages in people/

- AFFECTED_AREAS: people/

- ESTIMATED_EFFORT: 2-3 hours

- RECOMMENDED_AGENT: CLAUDE

- DEPENDENCIES: None

**B-023:** Master timeline regeneration

- TYPE: MECHANICAL | PRIORITY: P3 | STATUS: OPEN

- WHY_IT_MATTERS: 599KB, generated by wiki-timeline. Should be in pre-commit block.

- EVIDENCE: BACKLOG.md item

- AFFECTED_AREAS: timeline/master-timeline.md

- ESTIMATED_EFFORT: 5 minutes

- RECOMMENDED_AGENT: CHEAP_AGENT

- DEPENDENCIES: None

- NOTE: Add to CLAUDE.md pre-commit block

**B-024:** Agent architecture review

- TYPE: ARCHITECTURE | PRIORITY: P3 | STATUS: DEFERRED

- WHY_IT_MATTERS: LLM feed could be smarter. Wait until content work stabilizes.

- EVIDENCE: AGENT_ACCESS.md, reports/llm-feed-audit.md

- AFFECTED_AREAS: llm/, agent/

- ESTIMATED_EFFORT: 4-8 hours

- RECOMMENDED_AGENT: CLAUDE

- DEPENDENCIES: B-002 (manifest regeneration)

## 11. RECOMMENDED EXECUTION ORDER

### Phase A: Immediate Mechanical Fixes (1-2 hours)

1. B-001: Fix 9 `sources:` → `synthesizes:` errors

1. B-002: Regenerate LLM manifest

1. B-003: Regenerate DIGEST/RECENT/OPEN

1. B-004: Fix broken wikilinks

1. B-023: Add master-timeline to pre-commit block

### Phase B: Highest-Information Source Campaigns (8-16 hours)

1. B-006: Gchat archive extraction (HIGHEST ROI)

1. B-007: Per-contact iMessage CSV sweep

1. B-008: ChatGPT export extraction

1. B-011: Dox-scan RTF/TXT files

### Phase C: Quality & Correction (2-4 hours)

1. B-005: Retracted "$750/week" correction cascade

1. B-010: Fix 30 pages with `status: archived` outside archive/

1. B-009: Wire 36 islanded pages into graph

### Phase D: Entity & Timeline Reconstruction (4-8 hours)

1. B-016: Entity disambiguation (top 50)

1. B-012: Semantic Location History mining

1. B-017: 215 stale pages review

### Phase E: Connection Enrichment (4-8 hours)

1. B-015: Graph retrofit (996 bare `related:` entries)

1. B-018: OPEN.md contradiction resolution

### Phase F: Synthesis (6-12 hours)

1. B-013: 2025-collapse cluster synthesis

1. B-014: Relationship architecture synthesis

1. B-019: Interest evolution synthesis

### Phase G: Retrieval/LLM Optimization (deferred)

1. B-024: Agent architecture review (after content work stabilizes)

## 12. "DO NOT TOUCH YET" LIST

These areas should NOT be edited prematurely:

1. **The 240 ****`wiki-connect`**** warnings (bare ****`## Related`**** footers)** — Converting these requires reading both pages and deciding relationship types. Bulk conversion would introduce worse problems than it solves.

1. **Pages with ****`status: archived`**** outside archive/** — Do not change status without reading the page. Some may genuinely be pinned artifacts.

1. **Pages with retracted strings** — Do not grep-and-replace without reading context. Some mentions may be in CORRECTED blocks quoting the old claim.

1. **Empty phantom source files** — Do NOT delete. raw/ is immutable per 2026-08-13 doctrine.

1. **215 pages with old date_modified** — Do not bump dates without reading. Some may be accurate but simply not recently touched.

1. **87 pending graph candidates** — Do not mechanically add edges. Each requires reading both pages.

1. **Synthesis queue clusters** — Do not create synthesis pages without finding a governing rule.

1. **788 entity candidates** — Do not create pages without verifying identity and checking for existing pages under different names.

1. **Facebook Messenger HTML** — Do not start mining until higher-value sources (Gchat, CSVs, ChatGPT) are exhausted.

1. **Vector DB / RAG / MCP / Fancy search** — Not yet. Wait until content work stabilizes.

## APPENDIX A: TOOL OUTPUT REFERENCE

| **Tool** | **Command** | **Purpose** |
| --- | --- | --- |
| Corpus inventory | `bin/wiki-lint` (page count) | Count wiki pages |
| Graph health | `bin/wiki-connect audit` | Count edges, islands |
| Altitude | `bin/wiki-climb audit` | Count T1/T2/T3 |
| Staleness | `bin/wiki-climb check` | Find stale premises |
| Lint | `bin/wiki-lint` | Find errors/warnings |
| Drift | `bin/wiki-digest` | Generate DIGEST/RECENT/OPEN |
| Source coverage | `reports/source-coverage.md` | Never-cited raw files |
| Entity candidates | `reports/entity-candidates.md` | Entities with no page |
| Temporal audit | `reports/temporal-audit.md` | Pages with old date_modified |
| Connection retrofit | `reports/connection-retrofit.md` | Graph health details |
| Synthesis audit | `reports/synthesis-audit.md` | Altitude distribution |
| Graph candidates | `reports/graph-candidates/top-100.md` | Connection pairs |
| LLM feed audit | `reports/llm-feed-audit.md` | Manifest quality |

## APPENDIX B: KEY FILES REFERENCED

| **File** | **Purpose** |
| --- | --- |
| CLAUDE.md | Process governing doc |
| STRATEGY.md | Intent governing doc |
| EXTRACTION_SPEC.md | Depth governing doc |
| STYLE_GUIDE.md | Format governing doc |
| CONNECTIONS_SPEC.md | Edges governing doc |
| SYNTHESIS_SPEC.md | Altitude governing doc |
| BACKLOG.md | Standing work (40 items) |
| LLM_HANDOFF.md | Resume point (1491 lines) |
| AGENT_ACCESS.md | Agent entrypoints |
| synthesis-queue.md | Mined climb clusters (196 lines) |
| connection-queue.md | Mined edge candidates (641 lines) |
| RETRACTED.md | Retracted claims ledger |

*End of report.*
