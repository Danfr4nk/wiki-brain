# Connection Retrofit Audit Report

Generated: 2026-08-20

## Summary

| **Metric** | **Value** |
| --- | --- |
| Total pages | 476 |
| Non-index pages | 459 |
| Prose edges | 3,323 |
| Avg outdegree | 7.0 |
| Typed connections (with claims) | 1,678 |
| Bare `related:` entries (untyped) | 996 |
| Pages with bare `## Related` footers | 68 |
| Islanded pages (index-only inbound) | 36 |

## Retrofit Work Remaining

1. **996 bare ****`related:`**** entries** — these are untyped frontmatter entries awaiting conversion to typed `connections:`

1. **68 pages with ****`## Related`**** footers** — these footers are banned per STYLE_GUIDE.md and must be converted to typed edges or deleted

1. **36 islanded pages** — these pages have no inbound prose edges (only reachable from indexes)

## Islanded Pages (36)

These pages are reachable only from indexes and have no inbound prose connections:

- wiki/interests/favorites/music/artists/angels-and-airships.md

- wiki/interests/favorites/music/artists/bloc-party.md

- wiki/interests/favorites/music/artists/codeseven.md

- wiki/interests/favorites/music/artists/every-avenue.md

- wiki/interests/favorites/music/artists/guster.md

- wiki/interests/favorites/music/artists/head-automatica.md

- wiki/interests/favorites/music/artists/mayday-parade.md

- wiki/interests/favorites/music/artists/rilo-kiley.md

- wiki/interests/favorites/music/artists/saosin.md

- wiki/interests/favorites/music/artists/terminal.md

- wiki/interests/favorites/music/artists/the-academy-is.md

- wiki/interests/favorites/music/artists/the-dresden-dolls.md

- wiki/interests/favorites/music/artists/the-early-november.md

- wiki/interests/favorites/music/artists/the-hush-sound.md

- wiki/interests/favorites/music/artists/the-maine.md

- wiki/interests/favorites/music/artists/the-subways.md

- wiki/interests/favorites/music/artists/vertical-horizon.md

- wiki/interests/favorites/music/artists/we-the-kings.md

- wiki/people/annie-ulmer-personality-assessment.md

- wiki/people/brennan-meadows.md

- wiki/people/bruce-burish.md

- wiki/people/matt-kraus.md

- wiki/people/nathan-king.md

- wiki/people/suzanne-frank-personality-assessment.md

- wiki/people/tom-wallisch.md

- wiki/self/chats/9-11-chat.md

- wiki/self/chats/photo-ingest-pinned.md

- wiki/self/concepts/astrology-star-signs.md

- wiki/self/concepts/chatgpt.md

- wiki/self/concepts/claude-code.md

- wiki/self/concepts/claude.md

- wiki/self/concepts/gemini.md

- wiki/self/concepts/llm.md

- wiki/self/concepts/wiki-brain.md

- wiki/timeline/master-timeline.md

- wiki/work/tech/vibe-coding-games.md

## Cross-Domain Edge Coverage

| **Domain Pair** | **Edges** |
| --- | --- |
| health <-> interests | 1 |
| health <-> legal | 1 |
| health <-> mind | 11 |
| health <-> people | 18 |
| health <-> places | 3 |
| health <-> self | 1 |
| health <-> timeline | 10 |
| health <-> work | 3 |
| interests <-> legal | 0 |
| interests <-> mind | 67 |
| interests <-> people | 35 |
| interests <-> places | 2 |
| interests <-> self | 45 |
| interests <-> timeline | 81 |
| interests <-> work | 7 |
| legal <-> mind | 12 |
| legal <-> people | 26 |
| legal <-> places | 3 |
| legal <-> self | 3 |
| legal <-> timeline | 7 |
| legal <-> work | 5 |
| mind <-> people | 319 |
| mind <-> places | 16 |
| mind <-> self | 104 |
| mind <-> timeline | 157 |
| mind <-> work | 50 |
| people <-> places | 54 |
| people <-> self | 180 |
| people <-> timeline | 392 |
| people <-> work | 91 |
| places <-> self | 3 |
| places <-> timeline | 22 |
| places <-> work | 5 |
| self <-> timeline | 68 |
| self <-> work | 27 |
| timeline <-> work | 16 |

## Recommendations

1. **Priority 1:** Convert 996 bare `related:` entries to typed `connections:` with claims

1. **Priority 2:** Delete or convert 68 `## Related` footers

1. **Priority 3:** Wire 36 islanded pages into the graph with typed edges

1. **Priority 4:** Address disconnected domain pairs (interests <-> legal has 0 edges)

Note: This is a mechanical audit. Deciding relationship types and writing claims requires Claude judgment.
