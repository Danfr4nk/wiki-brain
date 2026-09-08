# wiki-brain

Personal wiki (v2) — second brain. A lifelong biographical, psychological and
ideological record kept as plain Markdown: no apps, no databases, no APIs, just
text files, a few small scripts, and git for history.

This repository is the new home. It is **mid-migration** — read the next
section before assuming anything is here.

---

## Migration status

| Piece | State |
| :---- | :---- |
| Authoritative message corpus | **Landed.** 192,140 messages, tooling and policy in place |
| Corpus policy / shelving rules | **Landed.** [`CORPUS_POLICY.md`](CORPUS_POLICY.md) |
| Wiki body — `wiki/`, `raw/`, `bin/`, governing docs | **Not migrated.** Blocked, see below |

### What is blocking the wiki body

The staged copy in Google Drive (`My Drive/wiki-brain-main-1`) is **not a
faithful copy of the repository.** Every `.md` file in it was converted to a
Google Doc on upload, and that conversion is lossy in both directions.
Exporting `README.md` back out of Drive returns, among other damage:

- literal backslash escapes in the prose — `\+`, `\-`, `\#`
- fenced code blocks flattened into ordinary paragraphs, fences gone
- relative links rewritten into invalid absolute ones —
  `[AGENT_ACCESS.md](AGENT_ACCESS.md)` came back as
  `[AGENT\_ACCESS.md](http://AGENT_ACCESS.md)`

Migrating from that source would silently corrupt every governing document and
every wiki page — and silently is the operative word, because the damage is
plausible-looking Markdown, not an obvious break. The tree is also 1,000+ files
deep across 40+ folders, so the corruption would arrive faster than anyone
could review it.

**The fix is to migrate from the original folder on the Mac**, which is real
Markdown on a real filesystem, rather than from the Drive round-trip. The Drive
copy remains useful as a backup and as proof of what the tree contained.

---

## What is here now

```
corpus/          the authoritative message record + derived statistics
shelf/           superseded per-contact extracts (inventory only; contents gitignored)
bin/             corpus-verify, corpus-stats, corpus-query
CORPUS_POLICY.md what counts as message evidence, and what no longer does
```

### The corpus

192,140 messages spanning 2011-03-19 → 2026-09-07, across 577 threads and 498
counterparties. It replaces the earlier per-contact extracts, which were
accurate but silently partial — see [`CORPUS_POLICY.md`](CORPUS_POLICY.md) for
why that distinction retired them and what they may still be used for.

```sh
bin/corpus-verify                                   # integrity check
bin/corpus-stats                                    # rebuild derived stats
bin/corpus-query --who "Name" --context 3           # read it in situ
bin/corpus-query --text "topic" --stats             # who and when, no transcript
```

The corpus file itself is gitignored. [`corpus/README.md`](corpus/README.md)
covers the layout, what is published versus withheld, and how to restore it on
a fresh clone.

---

## Two open privacy items

Neither is a crisis and neither is mine to decide — both are recorded here so
they are decisions rather than defaults.

**1. This repository is public and the corpus is other people's data.**
`.gitignore` currently keeps `corpus/messages.csv`, `corpus/private/` and the
shelf contents out of git. That default differs from the earlier call to track
`intake/events.jsonl` in the open, and deliberately: that was Dan publishing
Dan. The message corpus is 498 other people's phone numbers, addresses and
private words, and they did not make that choice. Un-ignoring those lines
publishes them permanently. If the intent is to publish, make the repository
private first and verify it — in that order.

**2. The backing Google Sheet is world-readable.** As of 2026-09-08 the
`messages` sheet is shared "anyone with the link" — it downloads in full with
no credentials, which is how the corpus was fetched for this migration. Every
other file in the Drive folder is correctly private; this one is not, and it is
the most sensitive of them. Restricting it costs nothing if the exposure was
not deliberate.

---

## The governing documents

Six files govern the work, in the order a new reader should meet them. **They
are still in Drive and land here with the wiki body**, listed now so the shape
of the finished repository is visible.

| File | Governs |
| :---- | :---- |
| `STRATEGY.md` | what this repo is for and the core loop — **read first** |
| `CLAUDE.md` | the operations: ingest, query, climb, rewrite, lint |
| `EXTRACTION_SPEC.md` | how deep to mine a source before writing |
| `STYLE_GUIDE.md` | page format and the substance standard |
| `CONNECTIONS_SPEC.md` | typed edges and the claims they carry |
| `SYNTHESIS_SPEC.md` | altitude — how conclusions stack on conclusions |

`CORPUS_POLICY.md` joins that set and outranks all of them on message evidence
specifically: where a conclusion already in the wiki disagrees with the corpus,
the conclusion is what changes.
