# Phantom Source Audit

Generated: 2026-08-20 00:29:32

## Summary

- **Phantom sources found:** 10 — **superseded, see banner**

**SUPERSEDED [2026-08-20 review pass]. The real figure is 4 files, 2 cited.** Six of the ten listed below are `.gitkeep` placeholders: empty **by design**, never cited as evidence, and now excluded (`STRUCTURAL_FILES` in `bin/wiki-lint`). The four genuine ones are: `raw/self/message-csv/END_FIGHT_full.csv` (68 B, header only), `annie_group_chat_may31-june1_2026.csv` (68 B), `annie_group_chat_relaxed.csv` (57 B), `messenger_export_THREADKEY_HERE.csv` (0 B).

The companion claim that 5 pages "cite" them was produced by matching bare filenames against whole page bodies. `raw/` holds **3,313 files under 1,430 distinct basenames — 1,041 of those basenames collide**, so a basename cannot identify a source. Checking `sources:` frontmatter citations instead (the documented convention, which uses repo-relative paths) gives **2** real citations, both of `END_FIGHT_full.csv`: `wiki/mind/synthesis/dan-annie-fallout-verdict.md` and `wiki/timeline/events/group-chat-closure.md`. Prose mentions — e.g. `source-coverage-index`, which catalogues these files on purpose — are correctly no longer flagged.

**This report is now reproducible:** `bin/wiki-lint` emits it as warnings. **Never substitute a different file for an empty one.** Re-export or de-cite.

## Phantom Sources

### raw/music/.gitkeep

- Size: 0 bytes

- Reason: zero bytes

- Not cited by any wiki page

### raw/self/message-csv/annie_group_chat_relaxed.csv

- Size: 57 bytes

- Reason: header-only (1 line)

- **Cited by 2 page(s):**

  - self/message-corpora/source-coverage-index.md

  - self/message-corpora/master-message-dump.md

### raw/self/message-csv/messenger_export_THREADKEY_HERE.csv

- Size: 0 bytes

- Reason: zero bytes

- **Cited by 1 page(s):**

  - self/message-corpora/source-coverage-index.md

### raw/self/message-csv/annie_group_chat_may31-june1_2026.csv

- Size: 68 bytes

- Reason: header-only (1 line)

- **Cited by 3 page(s):**

  - self/message-corpora/source-coverage-index.md

  - self/message-corpora/master-message-dump.md

  - mind/synthesis/bond-switch-2015.md

### raw/self/message-csv/END_FIGHT_full.csv

- Size: 68 bytes

- Reason: header-only (1 line)

- **Cited by 5 page(s):**

  - self/message-corpora/source-coverage-index.md

  - self/message-corpora/master-message-dump.md

  - mind/synthesis/dan-annie-fallout-verdict.md

  - timeline/events/group-chat-closure.md

  - timeline/events/end-fight.md

### raw/legal/bfs-dispute/.gitkeep

- Size: 0 bytes

- Reason: zero bytes

- Not cited by any wiki page

### raw/legal/463-morgantown/.gitkeep

- Size: 0 bytes

- Reason: zero bytes

- Not cited by any wiki page

### raw/tech/imessage-tooling/.gitkeep

- Size: 0 bytes

- Reason: zero bytes

- Not cited by any wiki page

### raw/tech/max-framework/.gitkeep

- Size: 0 bytes

- Reason: zero bytes

- Not cited by any wiki page

### raw/tech/grok-build/.gitkeep

- Size: 0 bytes

- Reason: zero bytes

- Not cited by any wiki page
