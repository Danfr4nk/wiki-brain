
---
domain: work
page_type: summary
status: active
date_created: 2026-06-22
date_modified: 2026-06-23
sources: ["bin/export-imessage-template.sh", "raw/self/context-core/CONTEXT_CORE_EXPANDED.md", "ingest-queue.md", "log.md", "/Users/daniel/imessage-extractor/README.md", "/Users/daniel/imessage-extractor", "/Users/daniel/messages-exporter", "danwiki_portal.py", "raw/self/message-csv/*", "raw/self/dox-md/BFS_BOOTLOADER_v2.md", "raw/self/dox-md/_ⒺⓍⓉⓇⒶⒸⓉ ⓂⒺⓈⓈⒶⒼⒺⓈ Pinned chat.md", "raw/self/dox-md/MAX_PRIME.md", "raw/self/chats/*"]
related: ["wiki/work/tech/grok-build/overview", "wiki/work/tech/max-framework/overview", "wiki/self/message-corpora/master-message-dump", "wiki/self/context-core", "wiki/self/gemini-activity/gemini-activity.md", "wiki/self/facebook", "wiki/people/*", "wiki/timeline/periods/2025-collapse", "wiki/legal/463-morgantown", "wiki/work/bfs-foods"]
tags: [digital-footprint, ai-collaboration, forensic-analysis]
---

# iMessage Tooling

## Overview
Tooling stack for extracting, exporting, and analyzing iMessage/SMS from `~/Library/Messages/chat.db` (local, read-only, forensic grade). Powers raw/self/message-csv/, imessage/, master-message-dump, and wiki ingest. Includes shell/py exporters, Electron dashboard app, portal TUI, and Grok Build integrations (responder noted in log).

**Key volumes (context-core):** 97,199 sent iMessages (2015–2025) + Twitter archive baseline; stable voice (lowercase fragment/ellipsis) since 2009.

## Purpose Table
| Purpose | Description | Supporting Evidence |
|---------|-------------|---------------------|
| Forensic Extraction | Read-only access to chat.db for sent/received history without GUI | chat.db schema (message, handle, chat_message_join, attributedBody dec); Full Disk Access req |
| Bulk Export to CSV | Structured data for analysis/ingest (timestamps, direction, contact, text) | 37+ csvs in raw/self/message-csv/* ; annie_full_archive.csv target |
| GUI Dashboard | Operator-grade Electron app for query/paginate/export | imessage-extractor: queryBuilder.js exact templates, better-sqlite3 |
| Ingest to Wiki | Map exports → raw/ then wiki/ via portal or manual | danwiki_portal.py ; bin/wiki-ingest |
| Grok Build / Analysis | Responder auto + subagent deep dives on exports (BFS, legal, periods) | log; dox pinned extract chats; Grok tools (grep etc) |

## Tooling Inventory (Expanded)
| Tool | Type | Function / Path | Output / Notes |
|------|------|-----------------|----------------|
| export-imessage-template.sh | Bash + embedded py | SQLite extract (handles, chat joins, attributedBody dec); Full Disk Access; targets phones/AppleIDs; writes annie_full_archive.csv etc | raw/self/imessage/*.csv; "Ingest ... into dan-wiki" workflow |
| messages-exporter/ | Python | messages_export.py + tests; csv dumps; TUI progress | raw/self/message-csv/ (e.g. imessage_*.csv, targeted_extraction.csv) |
| iMessage Extractor (Electron) | macOS app | Desktop forensic; chat.db query; renderer; dmg builds; exact Apple epoch + Pattern A/B | /Users/daniel/imessage-extractor (dist/ dmg, queryBuilder.js); "Operator-grade" |
| danwiki_portal.py | Textual TUI | Fact entry + file ingest to wiki/raw; domain map (self→dox-md, tech→raw/tech); XAI key | Ingest queue / bin/wiki-* |
| Grok Build responder | Agentic | iMessage responder (glitched/spammed); subagent mode | log.md note; current wiki expansion uses Grok tools (grep/read/search_replace) |
| query / csv utils + pinned SQL | Supporting | imessage_7243228715_*, imessages_2124702449_* etc; Gemini-provided SQLite snippets for ad-hoc | BFS dates, Suz comms (Arnu/Felix 2026-02-10), John Carney refs; raw/self/dox-md extract chat |

**Chat.db Query Example (from pinned dox):** Uses datetime(m.date/1e9 + 978307200...) + joins for 21d/1y targeted CSVs on specific handles (e.g. 2124702449). Redirect > csv.

## Tooling Inventory Table

| Tool | Type | Function / Path | Output / Notes |
|------|------|-----------------|----------------|
| export-imessage-template.sh | Bash + embedded py | SQLite extract (handles, chat joins, attributedBody dec); Full Disk Access; targets phones/AppleIDs; writes annie_full_archive.csv etc | raw/self/imessage/*.csv; "Ingest ... into dan-wiki" workflow |
| messages-exporter/ | Python | messages_export.py + tests; csv dumps | raw/self/message-csv/ (e.g. imessage_*.csv, targeted_extraction.csv) |
| iMessage Extractor (Electron) | macOS app | Desktop forensic; chat.db query; renderer; dmg builds | /Users/daniel/imessage-extractor (dist/ dmg, queryBuilder.js); "Operator-grade" |
| danwiki_portal.py | Textual TUI | Fact entry + file ingest to wiki/raw; domain map (self→dox-md, tech→raw/tech); XAI key | Ingest queue / bin/wiki-* |
| Grok Build responder | Agentic | iMessage responder (glitched/spammed); subagent mode | log.md note; current wiki expansion uses Grok tools (grep/read/search_replace) |
| query / csv utils | Supporting | imessage_7243228715_*, imessages_2124702449_* etc | BFS dates, Suz comms (Arnu/Felix 2026-02-10), John Carney refs |

## Key Extracts / Evidence Surfaced

- BFS incident corpus: Anita/Brandon/Kim/Timmy texts (2026-05); group "brandon, +3".
- Housing: Suz msgs on 463 contractors (Arnu no-show, John Carney analysis 2026-03-27).
- Volumes feed [[wiki/self/message-corpora/master-message-dump]] (counts, top handles, silence patterns).
- Location + FB ingest parallel.
- Specific handle extracts: 2124702449 (NYC), 7249204125, 7244346811; multi-day windows via SQL redirection in pinned chats.

## Sources / Evidence Table
| Raw Source | Contribution | Cross |
|------------|--------------|-------|
| raw/self/message-csv/* (37 files) | Bulk CSVs (imessage_*.csv) for master dump, BFS, 463 | master-message-dump, legal |
| bin/export-imessage-template.sh | Template for annie_full + targeted; dec fn for attributedBody | imessage/ dir |
| raw/self/dox-md/_ⒺⓍⓉⓇⒶⒸⓉ...Pinned chat.md | Gemini SQL examples for 7d/21d/1y targeted pulls | Ad-hoc forensics |
| /Users/daniel/imessage-extractor | Full Electron spec + builds | README details epoch math, joins |

## Relation to Core / Legal / Tech

- [[wiki/self/context-core]] §2 voice + §5 work exit (BFS via Kim).
- Legal: drawer dispute reconstruction, 463 liens from csv fragments.
- Tech synergy: [[wiki/work/tech/grok-build/overview]] (Grok Build iMessage), [[wiki/work/tech/max-framework/overview]] (MAX for analysis of exports; CATO for forensic).
- Ingest: "iMessage via chat.db: export-imessage-template.sh exists... never run" (queue note); actual csvs in raw/message-csv from prior runs.
- [[wiki/self/facebook]]: Parallel archive for cross-validation of contacts/events.

**Cross-references:** [[wiki/work/tech/grok-build/overview]], [[wiki/work/tech/max-framework/overview]], [[wiki/self/message-corpora/master-message-dump]], [[wiki/self/context-core]], [[wiki/self/gemini-activity/gemini-activity.md]], [[wiki/self/facebook]], [[wiki/legal/463-morgantown]], [[wiki/work/bfs-foods]], [[wiki/people/anita]], [[wiki/people/arnu]], [[wiki/people/john-carney]], [[wiki/people/kim]] (all use csv evidence).

**Notes:** Requires macOS Full Disk Access. chat.db schema: message + handle + chat_handle_join + dec for attributedBody. Update raw/tech/imessage-tooling/ on new exports. Sources include workspace binaries + extracted csvs (defer raw). Grok subagent uses these for deep review. Raw/tech/imessage-tooling/ remains placeholder dir.


