# corpus/

The authoritative message record. 192,140 messages, 2011-03-19 → 2026-09-07.

Rules for what may be concluded from it live in
[`CORPUS_POLICY.md`](../CORPUS_POLICY.md). This file covers the mechanics.

## Layout

```
corpus/
  messages.csv      the corpus itself — GITIGNORED, see below
  manifest.json     size, SHA-256, row count, columns (committed)
  derived/          publishable statistics — no identities (committed)
    summary.json      aggregate counts, per-year totals
    threads.csv       per-thread shape, counterparties as salted hashes
  private/          identity material — GITIGNORED, never leaves the machine
    contacts.csv      Google Contacts export, for name resolution
    salt              keying salt for the hashes in derived/
    counterparties.csv  handle → name → thread_id map
```

## What is and is not committed

This repository is **public**. The split is deliberate:

- `derived/` is committed. It describes the *shape* of the data — how many
  messages, in how many threads, over what spans. Counterparties appear only as
  salted hashes, so it can be published without publishing anyone.
- `messages.csv` and `private/` are gitignored. They contain the phone numbers,
  email addresses and private words of 498 other people. Git history cannot be
  un-published, so the default is closed.

**The salt is load-bearing.** There are only ~10^10 possible US phone numbers;
an unsalted hash of one falls to brute force in seconds. `private/salt` is what
makes the ids in `derived/threads.csv` genuinely non-reversible. If the salt
leaks, everything derived from it de-anonymises with it. It is mode `600` and
gitignored, and it should never be committed, pasted or synced.

## Restoring the corpus on a fresh clone

The corpus is not in git, so a fresh clone has `derived/` but no
`messages.csv`. Re-export from the source of record:

> Google Sheets — **messages**
> `1WxR14bXRcBS6uyrSk4ZVsoyuu9EUE_l6LC3ruaK7ouA`

Download it as CSV to `corpus/messages.csv`, then:

```sh
bin/corpus-verify     # must match manifest.json
bin/corpus-stats      # re-derive derived/ and private/
```

If `corpus-verify` fails on a fresh export, the sheet has changed since
2026-09-08. That is not automatically wrong, but it is never routine: check
what changed, then `bin/corpus-verify --write` to re-record and
`bin/corpus-stats` to re-derive. Note it in `log.md`.

A new salt is generated on first run if none exists, which means the hashes in
`derived/threads.csv` will change. That is expected and harmless — the ids are
stable within a machine, not across machines. They exist to let threads be
compared to each other, not to be a permanent identifier.

## Tools

```sh
bin/corpus-verify              # integrity check against manifest.json
bin/corpus-verify --write      # re-record the manifest after a re-export
bin/corpus-stats               # rebuild derived/ and private/
bin/corpus-query --help        # search the corpus, print readable transcripts
```

All three are standard-library Python, matching the rest of the project.
Nothing here makes a network call.

## Source-of-record caveat

As of 2026-09-08 the backing Google Sheet is shared **"anyone with the link"** —
it downloads with no credentials at all. Anyone holding that URL has the whole
corpus. If that is not intended, restrict the sheet's sharing; the migration
notes in the root `README.md` cover it.
