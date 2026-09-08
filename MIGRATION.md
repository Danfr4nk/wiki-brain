# MIGRATION.md

Moving wiki-brain into `github.com/Danfr4nk/wiki-brain`. Delete this file when
the last row of the table is done.

## Status

| Piece | State |
| :---- | :---- |
| Authoritative message corpus | **Done** — `corpus/`, `bin/corpus-*`, [`CORPUS_POLICY.md`](CORPUS_POLICY.md) |
| Shelving of prior extracts | **Done** — [`shelf/`](shelf/) |
| Wiki body — `wiki/`, `raw/`, `bin/`, `app.py`, governing docs | **Waiting on a push from the Mac** |

## Why the wiki body is not coming from Google Drive

`My Drive/wiki-brain-main-1` is a staging copy, not a faithful one. Every `.md`
file was converted to a Google Doc on upload, and the round-trip back is lossy.
Exporting `README.md` out of Drive returns, among other damage:

- backslash escapes through the prose — `\+`, `\-`, `\#`
- fenced code blocks flattened into paragraphs, fences gone
- relative links rewritten into invalid absolute ones —
  `[AGENT_ACCESS.md](AGENT_ACCESS.md)` came back as
  `[AGENT\_ACCESS.md](http://AGENT_ACCESS.md)`

Across 1,000+ files that corrupts every governing document, and it does it
*silently*: the output is plausible-looking Markdown, not an obvious break. The
Drive copy stays useful as a backup and as evidence of what the tree contained.
It is not the migration source.

The original folder on the Mac is real Markdown on a real filesystem, and it
has the git history. That is the source.

## Pushing from the Mac

`main` here currently holds a single placeholder commit (`53bbfe8`, a one-line
README) created when the repository was made. Your local history does not share
it, so an ordinary push is rejected as unrelated. Replacing the placeholder is
the correct move — there is nothing in it worth keeping.

```sh
cd ~/path/to/wiki-brain-main1

git status                      # confirm the tree is clean and complete
git log --oneline | head -5     # confirm the history you expect is here

git remote add origin https://github.com/Danfr4nk/wiki-brain
# already have an origin? point it here instead:
#   git remote set-url origin https://github.com/Danfr4nk/wiki-brain

git push -u origin main --force-with-lease
```

`--force-with-lease` rather than `--force`: it refuses if `main` has moved since
you last fetched, so it cannot quietly destroy work that arrived in the
meantime. Here it should replace one placeholder commit and nothing else.

**No git history on the Mac?** If `git log` errors, the folder was never a
repository — say so and take the zip route instead (zip the folder, upload it,
share it "anyone with the link"), and it gets committed here as a first import.

### After the push

`claude/wiki-brain-repo-migration-m79ey5` (PR #1) is based on the placeholder
commit, so once real history lands it needs rebasing onto it. Two files will
conflict, both expected, both already minimised so the resolution is small:

- **`.gitignore`** — resolve as the **union**. Your existing rules (`exports/`,
  `site/`, `corpus_*.md`, the intake-ledger note) plus the corpus rules added
  here (`corpus/messages.csv`, `corpus/private/`, `shelf/**`). Nothing is
  dropped from either side.
- **`README.md`** — **your real README wins outright.** The version on this
  branch is a placeholder standing in until yours arrives; it carries no
  content that needs preserving. Add a line pointing at `CORPUS_POLICY.md`
  under "The governing documents" and that is the whole merge.

Everything else on the branch is new files that your tree does not contain, so
they rebase without conflict.

## Then: reconcile the wiki with the corpus

Once the wiki body is in, the corpus work has a job to do. Any claim resting on
message evidence from before 2026-09-08 traces to a shelved fragment and is
**unverified** — not wrong, just not yet read against the complete record.

```sh
grep -rln "imessage" wiki/ raw/            # what cites the old extracts
bin/corpus-query --who "Name" --context 3  # check it against the corpus
```

Procedure and the confirmed / corrected / withdrawn rule are in
[`CORPUS_POLICY.md`](CORPUS_POLICY.md). Fill in the `Pages built on it` column
of [`shelf/MANIFEST.md`](shelf/MANIFEST.md) as you go — that column is what
turns a pile of dead files into a finite re-verification queue.

Two `raw/` artifacts are already listed there awaiting the move onto the shelf:
`imessage_export_+1724XXXXXXX_20260715013702` and
`imessage_724XXXXXXX_both_all_now`.
