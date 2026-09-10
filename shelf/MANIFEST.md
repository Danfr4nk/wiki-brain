# Shelf manifest

Inventory of superseded message extracts. The files themselves are gitignored
(see [`README.md`](README.md)); this list is committed so the inventory stays
public and reviewable even though the contents are not.

One row per shelved artifact. Keep it accurate — the `Pages built on it` column
is what converts this from a list of dead files into a re-verification queue.

| Artifact | Taken | Covers | Span in extract | Pages built on it | Status |
| :---- | :---- | :---- | :---- | :---- | :---- |
| `imessage_export_+1724XXXXXXX_20260715013702` | 2026-07-15 | one counterparty | unknown | *not yet traced* | shelved, not yet imported |
| `imessage_724XXXXXXX_both_all_now` | unknown | one counterparty | unknown | *not yet traced* | shelved, not yet imported |

Both artifacts above are currently still in Google Drive under
`wiki-brain-main-1/raw/` and have not been moved onto the shelf yet — the
migration that would bring them across is still open (see `README.md`,
"Migration status"). They are listed now so the inventory exists before the
files arrive, rather than after.

## Filling in `Pages built on it`

This is the column that matters and it is the one that takes work. For each
shelved artifact, find the wiki pages whose message claims trace back to it:

```sh
grep -rln "imessage_export" wiki/ raw/          # explicit citations
bin/corpus-query --who "<counterparty>" --stats  # what the fragment covered
```

Then re-verify each page against the corpus per `CORPUS_POLICY.md` and record
the outcome — confirmed, corrected, or withdrawn — in `log.md`, with anything
withdrawn also going into `RETRACTED.md`.

A row whose `Pages built on it` still reads *not yet traced* is unfinished
work, not a completed shelving.
