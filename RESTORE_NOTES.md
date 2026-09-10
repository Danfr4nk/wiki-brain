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
   does not. Three colliding docs were renamed with a `.md` suffix:
   `llm/pages/interests/favorites/music.md`,
   `llm/pages/interests/favorites/music/artists.md`, and one more (see commit).
3. **`contacts`** — was a native Google Sheet in Drive; exported as
   `contacts.xlsx`.
4. **`.DS_Store`** files excluded per `.gitignore`.
5. **`raw/` source material** (~1,100 files) — arrives in a follow-up commit.
   The iMessage export inside it (third-party private messages) is excluded per
   the repo's own privacy machinery (`wb-check-publish`, sensitive flags).
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
