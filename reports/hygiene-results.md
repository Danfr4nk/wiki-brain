# Hygiene Fixes Applied

Generated: 2026-08-20

## Fixes Applied

### 1. Duplicate YAML Key Detection

**File:** `bin/wiki-lint` Added check for duplicate top-level keys in YAML frontmatter. Uses raw text parsing to catch duplicates that `yaml.safe_load` silently collapses.

### 2. Retracted-String Gate

**File:** `bin/wiki-lint` + `RETRACTED.md`

- Created `RETRACTED.md` ledger for tracking retracted claims

- Added grep gate that scans all wiki pages for retracted strings

- First entry: `$750/week`, `$750/wk`, `$750 per week`, `$750`

- Result: 10 pages flagged for containing retracted strings

### 3. Phantom-Source Detection

**File:** `bin/wiki-lint`

- Added detection of empty/header-only files in `raw/`

- Cross-references against wiki page citations

- Result: 5 phantom sources found, cited by 7 wiki pages

### 4. Missing Infoboxes Fixed

**Files:**

- `wiki/people/annie-ulmer-personality-assessment.md` — added infobox

- `wiki/people/suzanne-frank-personality-assessment.md` — added infobox

### 5. Valid Tags Updated

**File:** `bin/wiki-lint`

- Added `future` to `VALID_TAGS` (used by `wiki/self/concepts/ally-and-dan-love-as-destiny.md`)

## Remaining Phase 1 Items

### Generated-Feed CI Freshness Check

**Not yet implemented** — requires GitHub Actions workflow addition. Should fail CI if `bin/llm-publish && git diff --exit-code llm/` produces changes.

### Master-Timeline Pre-Commit Hook

**Not yet implemented** — requires CLAUDE.md update. Should add `bin/wiki-timeline generate` to the "before every commit" list.

### Stale Root Counts/Index Metadata

**Not yet implemented** — requires regenerating DIGEST/RECENT/OPEN and updating master index.

### Stale Documentation

**Not yet implemented** — requires a pass through governance docs.

## Error Summary

After fixes, `bin/wiki-lint` reports:

- **30 errors** (19 retracted strings, 7 phantom sources, 4 documentation issues)

- **23 warnings** (broken wikilinks, large pages, orphan pages)

The retracted string and phantom source errors are expected findings that require Claude judgment to resolve.
