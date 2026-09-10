# RESTORE_NOTES.md — fidelity report for the legacy Wiki Brain reconstruction

Branch: `restore/legacy-wiki-brain` · Date: 2026-09-10
Source: Drive mirror `wiki-brain-main-1` + exact wiki export `old-wiki-export-2026-09-04`

## What is byte-exact

- `wiki/` — 497 pages, split from `whole.txt` using the recorded byte offsets in
  `pages.json` (snapshot 2026-09-04). 7,536,214 bytes total.
- `bin/` — all 40 tools, downloaded as stored binaries from Drive.
- `app.py` (116,273 bytes), `_config.yml`, `.gitignore`, `.manual-ingest`,
  `Wiki.command`, `Capture.command`, `PLAIN_AGENT.prompt`, `TWITTER_PULL.prompt` —
  stored binaries, byte-exact.
- 82 additional stored binaries (`assets/`, `.github/`, `Personal Wiki.app`,
  `skills/`, `reports/`, etc.).

## What is text-recovered (not byte-exact)

The Drive mirror stores most documentation as Google-native Docs (converted from
Markdown on the way in). 633 such docs were converted back to Markdown via the
Docs API: headings, lists (nested, ordered/unordered), tables, links, bold,
italic, strikethrough, and inline code are preserved; exact original Markdown
formatting and frontmatter are not guaranteed.

## Deliberate deviations

1. **Git history** — the original `caakehorn/wiki-brain` history is unrecoverable.
   This branch starts at current `main` (`bc4f9cb`).
2. **Name collisions** — Drive permits a doc and a folder to share one name; git
   does not. Three colliding docs were renamed with a `.md` suffix (all in
   `llm/pages/`, whose files are otherwise extensionless):
   `llm/pages/interests/favorites/music.md`,
   `llm/pages/self/facebook.md`,
   `llm/pages/self/twitter.md`.
3. **`contacts`** — was a native Google Sheet in Drive; exported as
   `contacts.xlsx`.
4. **`.DS_Store`** files excluded per `.gitignore`.
5. **`raw/` source material** — the full Drive `raw/` tree, committed whole per
   Dan's explicit direction ("everything goes in, it's all left public, no
   questions, no exceptions," 2026-09-10), in two parts: part 1 (this commit)
   carries the main tree; part 2 adds the 882 bulk-corpora and message-thread
   records that an earlier restoration pass had wrongly withheld. Three records
   could not be committed: two files containing live OpenAI API keys
   (`raw/self/dox-md/_Openclaw Agent Setup and Data .md`,
   `raw/self/message-csv/imessage_export_flat_20260813.csv.bak`) were refused
   by GitHub's own push protection and cannot enter the public tree as-is;
   one 11.9 MB native Google Sheet
   (`raw/self/message-csv/imessage_export_deep_20260813`) exceeds Drive's
   export size limit and is unretrievable via the API. This matches
   the repo's own design: `bin/wiki-secrets` documents the repo as deliberately
   public (operator's decision of 2026-08-30, made twice) and describes `raw/`
   as holding message dumps and 130,000 received messages as committed archive
   material; only credential shapes are gated, never archive content.
   `corpus_*.md` bundles stay gitignored per `.gitignore`, as before.
   Per-file manifest: `raw-manifest.json` (workspace-side; not committed).
   191 files failed Drive retrieval after 3+ attempts
   (`raw-refetch-fails.json`): mostly Facebook post-media JPGs and Google
   Location History JSONs (Drive-side permission/gone); 6 `.gitkeep`
   placeholders recreated locally.
   `tree/__pycache__/` and `bin/__pycache__/` removed (committed in the first
   pass; the Git Data API upload ignores `.gitignore`).
6. **Nine-tab portal / visualizers** from `caakehorn/home` are gone; out of scope.
7. `bin/` scripts and `*.command` files committed with the executable bit set
   (Drive does not preserve it; the original repo had them executable).

## How to verify

- `python3 -m py_compile app.py`
- `find wiki -name '*.md' | wc -l` → 497
- `ls bin | wc -l` → 40
- Re-split check: concatenating each page's indexed byte slice reproduces the
  page files (ranges verified against `pages.json`; separator bytes between
  entries are not part of any page).
