# CORPUS_POLICY.md

What counts as message evidence, and what no longer does.

Governs any wiki page, claim or synthesis that rests on text messages. Where
this disagrees with a conclusion already written in the wiki, **this wins and
the conclusion is the thing that has to change.**

---

## The two tiers

| Tier | What | Where | May support a claim? |
| :---- | :---- | :---- | :---- |
| **Authoritative** | The complete Messages export — 192,140 messages, 2011-03-19 → 2026-09-07 | `corpus/messages.csv` | Yes |
| **Shelved** | Every earlier per-contact extract, transcript and pasted fragment | `shelf/` | **No — see below** |

There is no third tier. A message-derived claim either traces to the corpus or
it is unsupported.

## Why the old extracts were retired

The prior material was produced one counterparty at a time — exports like
`imessage_export_+1724XXXXXXX_20260715013702` and
`imessage_724XXXXXXX_both_all_now`. Each was accurate about the thread it
covered. The problem was never accuracy; it was **frame**.

The corpus now measures what those fragments were missing:

- **498 distinct counterparties.** The extracts covered a handful.
- **52 group threads / 882 messages** that per-contact exports cannot represent
  at all, because a group conversation is not any one person's thread.
- **A 15-year span** in which the same person appears under several handles —
  a phone number, an iCloud address, a `@vzwpix.com` gateway. A single-handle
  extract shows a relationship stopping dead where it only changed channel.

## The failure mode this exists to prevent

**In a fragment, absence of evidence looks exactly like evidence of absence.**

That is the specific way the old extracts produced wrong conclusions, and it is
silent — a partial export never announces what it left out. Read one thread in
isolation and you will reliably infer things that the complete record
contradicts: that contact stopped, that a subject was never discussed, that a
period was quiet, that someone was not around. Every one of those is a claim
about what is *not there*, and a fragment cannot support a claim about what is
not there. Only the complete corpus can.

So the extracts were not demoted for being false. They were demoted for being
**silently partial**, which is worse, because a false document can be caught by
reading it and a partial one cannot.

## What shelved material may still be used for

Exactly one thing:

> **To establish what was previously believed, and to show why it was wrong.**

A shelved extract is evidence *about the reasoning*, never evidence *about the
past*. Concretely:

- ✅ "The 2026-07 extract contained no messages after March, which is why
  `wiki/people/<name>.md` said the friendship lapsed. The corpus shows 340
  messages after that date. The claim was an artifact of the export window."
- ✅ Reconstructing which pages inherited a since-disproven premise.
- ❌ Citing a shelved extract as the source for anything that happened.
- ❌ "The corpus doesn't show it, but the old extract does." The corpus is a
  superset. If something appears only in a fragment, that is a bug to
  investigate, not a fact to keep — open it in `BACKLOG.md`.

When a shelved extract is cited under the permitted use, name it as shelved and
link the corrected claim. That is what `RETRACTED.md` is for.

## Re-verifying an existing claim

Any wiki claim that traces to message evidence predating 2026-09-08 is
**unverified** until checked against the corpus. Unverified is not the same as
wrong — most will survive. It means the claim has not yet been read against the
complete record.

```sh
bin/corpus-query --who "Name"  --from 2018-01-01 --to 2018-12-31
bin/corpus-query --text "phrase from the claim" --context 3
bin/corpus-query --text "topic" --stats        # who and when, no transcript
```

`--context` is the one that matters most. The fragment-era mistake was reading
quotes out of the exchange they sat in, and a quote with three messages either
side of it is a different quote.

Then do one of three things, and record which in `log.md`:

1. **Confirmed** — cite the corpus, drop the extract reference.
2. **Corrected** — rewrite the claim, note the correction in `RETRACTED.md`.
3. **Withdrawn** — remove it; log it in `RETRACTED.md` with the frame error
   that produced it.

Silently leaving a claim in place is not one of the three.

## Known limits of the authoritative corpus

It is authoritative, not perfect. Stating the gaps here so they do not become
the next round of confident wrong conclusions:

- **3,086 messages (1.6%) cannot be placed in a thread.** They are sent
  messages carrying no counterparty field. They are counted and excluded from
  per-thread figures rather than guessed at, so thread totals are floors, not
  exact counts. `summary.json → unattributable_to_a_thread`.
- **156 of 498 counterparties resolve to a name.** The rest are bare handles.
  An unnamed handle is not a stranger; it is an unmatched contact card.
- **Attachments are referenced, not stored.** `has_attachments` and the
  filename columns survive; the images do not. 8,120 messages carry one.
- **Deleted messages are absent.** Messages deleted before the export was taken
  are not in `chat.db` and so are not here. The corpus is complete with respect
  to the database, which is not the same as complete with respect to history.
- **The gap years are real.** 2021 has 282 messages and 2022 has none. That
  reflects the source database, and it is the one place where the
  absence-of-evidence rule above needs care in the corpus itself.

## Integrity

The corpus is gitignored — it is not Dan's data alone, and this repository is
public. Because git cannot notice it changing, `corpus/manifest.json` records
its size, SHA-256, row count and columns.

```sh
bin/corpus-verify          # does the file still match the manifest?
bin/corpus-verify --write  # re-record after a legitimate re-export
bin/corpus-stats           # re-derive corpus/derived/ after any change
```

Run `bin/corpus-verify` before any session that reasons from the corpus. A
conclusion drawn from a corpus that has silently drifted is the same class of
error this policy exists to end.
