# MIGRATION.md

Moving wiki-brain into `github.com/Danfr4nk/wiki-brain`. Delete this file when
the last row of the table is done.

## Status

| Piece | State |
| :---- | :---- |
| Authoritative message corpus | **Done** — `corpus/`, `bin/corpus-*`, [`CORPUS_POLICY.md`](CORPUS_POLICY.md) |
| Shelving of prior extracts | **Done** — [`shelf/`](shelf/) |
| Wiki body — `wiki/`, `raw/`, `bin/`, `app.py`, governing docs | **Waiting on a push from the Mac** |

PR #1 merged on 2026-09-08, so the corpus work is on `main`. That changes how
the Mac push has to be done — see the warning below.

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

> **Do not force-push `main`.** An earlier draft of this file said to, which was
> correct only while `main` held a one-line placeholder. PR #1 merged on
> 2026-09-08 and `main` now carries the corpus, the tooling and
> `CORPUS_POLICY.md`. A force-push would delete all of it. `--force-with-lease`
> does **not** save you here: once you have fetched, the lease is satisfied and
> the overwrite goes through.

Your local history and `main` have no commit in common, so they get joined
once, explicitly, with `--allow-unrelated-histories`. Both sides survive.

```sh
cd ~/path/to/wiki-brain-main1

git status                      # confirm the tree is clean and complete
git log --oneline | head -5     # confirm the history you expect is here

git remote add origin https://github.com/Danfr4nk/wiki-brain
# already have an origin? point it here instead:
#   git remote set-url origin https://github.com/Danfr4nk/wiki-brain

git fetch origin
git merge origin/main --allow-unrelated-histories
```

That merge stops on two conflicts. Both are expected, and the branch was
shaped to keep them small:

- **`.gitignore`** — take the **union**. Your rules (`exports/`, `site/`,
  `corpus_*.md`, the intake-ledger note) *plus* the corpus rules
  (`corpus/messages.csv`, `corpus/private/`, `shelf/**`). Drop nothing from
  either side; the corpus rules are what keep 498 people's messages out of a
  public git history.
- **`README.md`** — **yours wins outright.** The version on `main` is a
  placeholder written to be replaced. Keep yours, then add one line under
  "The governing documents" pointing at `CORPUS_POLICY.md`.

```sh
git add .gitignore README.md
git commit                      # completes the merge
git push -u origin main         # ordinary push, no force
```

Then confirm nothing was lost:

```sh
ls corpus/ bin/corpus-*         # corpus tooling still present
bin/corpus-verify               # corpus intact (needs corpus/messages.csv locally)
git log --oneline | head        # both histories present
```

**No git history on the Mac?** If `git log` errors, the folder was never a
repository. Say so and take the zip route instead — zip the folder, upload it,
share it "anyone with the link" — and it gets committed here as a first import
on top of `main`, with no merge needed.

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
