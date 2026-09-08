# wiki-brain

Personal wiki (v2) — second brain. A lifelong biographical, psychological and
ideological record kept as plain Markdown: no apps, no databases, no APIs, just
text files, a few small scripts, and git for history.

> **Placeholder.** The real README arrives with the wiki body — see
> [`MIGRATION.md`](MIGRATION.md). When it lands it replaces this file wholesale;
> nothing here needs preserving except the pointer to `CORPUS_POLICY.md`.

## What is here so far

```
corpus/          the authoritative message record + derived statistics
shelf/           superseded per-contact extracts (inventory only; contents gitignored)
bin/             corpus-verify, corpus-stats, corpus-query
CORPUS_POLICY.md what counts as message evidence, and what no longer does
MIGRATION.md     migration status and the remaining steps
```

## The corpus

192,140 messages, 2011-03-19 → 2026-09-07, across 577 threads and 498
counterparties. It supersedes the earlier per-contact extracts, which were
accurate but silently partial — [`CORPUS_POLICY.md`](CORPUS_POLICY.md) explains
why that distinction retired them and what they may still be used for.

```sh
bin/corpus-verify                            # integrity check against the manifest
bin/corpus-stats                             # rebuild derived statistics
bin/corpus-query --who "Name" --context 3    # read it in situ
bin/corpus-query --text "topic" --stats      # who and when, no transcript
```

`corpus/messages.csv` is gitignored — it is 498 other people's phone numbers and
private words, and this repository is public. Only the shape of the data is
published, with counterparties as salted hashes.
[`corpus/README.md`](corpus/README.md) covers the layout and how to restore the
corpus on a fresh clone.

`CORPUS_POLICY.md` joins the six governing documents and outranks all of them on
message evidence specifically: where a conclusion already in the wiki disagrees
with the corpus, the conclusion is what changes.
