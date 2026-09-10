
---
domain: mind
page_type: synthesis
status: active
knowledge: earned
title: "Read-Receipt Forensics — chat.db Metadata and Its Traps"
aliases: ["read receipts", "date_read", "chat.db metadata"]
tags: [forensic-analysis, digital-footprint]
date_created: 2026-08-09
date_modified: 2026-08-28
sources: []
synthesizes:
  - wiki/mind/concepts/forensic-method
  - wiki/timeline/events/august-2026-unmasking
  - wiki/mind/profile/big-five-psychometrics
connections:
  - page: wiki/mind/concepts/reassurance-architecture
    type: instance-of
    claim: "Read-receipt timestamp analysis is the developed form of measurement substituting for reassurance, and it is a strictly worse substitute: it establishes that she was awake and cannot establish that the rule still holds."
  - page: wiki/mind/concepts/forensic-method
    type: component-of
    claim: "Three instrument-level defects found in a single extraction session, each of which silently produces a confident wrong answer rather than an error — the failure mode the method is least protected against."
  - page: wiki/timeline/events/august-2026-unmasking
    type: supplies
    claim: "Every wakefulness claim on that page depends on the directional asymmetry defined here; read the column as one thing and the same data yields the opposite conclusion."
  - page: wiki/timeline/events/august-2026-unmasking
    type: evidences
    claim: "Every claim about her wakefulness rests on chat.db date_read values whose directional asymmetry that page defines; read the wrong way the same column produces the opposite conclusion."
  - page: wiki/mind/profile/big-five-psychometrics
    type: caused-by
    claim: "This page's own reassurance-architecture citation — read-receipt analysis as 'measurement substituting for reassurance' — is one hop from its actual source: Trust at the 9th percentile, corpus-confirmed at 1.96x raised suspicion, is why a confirmation does not carry forward and a device-level metadata query gets run in the first place. Named directly here rather than left implicit."
---

# Read-Receipt Forensics — chat.db Metadata and Its Traps

Derived from a single extraction session, 2026-08-09. Three defects, each of
which **silently produces a confident wrong answer rather than an error.** That
is the failure mode the forensic method is least protected against, which is why
this is a page and not a footnote.

> **Sourcing note.** The session this page documents ran directly against the
> operator's local `chat.db` (macOS Messages, requiring Full Disk Access — see
> the extraction recipe below) rather than against a CSV filed in this
> repository's `raw/`. No `raw/` export corresponding to the 230-row
> `annie_metadata_24h.csv` extract cited throughout has been filed as of this
> ingest; `sources:` above is left empty rather than pointing at a file that
> does not exist on disk, per `bin/wiki-lint`'s source check. Filing that
> export is the open item — see `queue.md`.

## M1 — `date_read` is directional and asymmetric

The single most consequential fact about the column, and it is not documented
anywhere obvious.

```
ON is_from_me = 1  (messages you SENT)
    date_read = when THE OTHER PARTY opened your message.
    Requires THEIR read receipts to be ON. Absent entirely otherwise.

ON is_from_me = 0  (messages you RECEIVED)
    date_read = when YOU opened their message.
    Recorded LOCALLY, ALWAYS, regardless of anyone's settings.
```

Observed in the 2026-08-08/09 extract:

```
RECEIVED rows with date_read :  81 / 101   (all of them are Dan)
SENT     rows with date_read :  44 / 129   (all of them are her)
```

**Reading the column as one undifferentiated thing produces the conclusion that
the counterparty was continuously active all day.** She was not visible at all
before 23:10:40. Half the column is a log of the operator's own behaviour.

**Rule:** always split by `is_from_me` before computing any latency statistic.
Never aggregate across directions.

## M2 — `reply_to_guid` is not a reply marker

```
reply_to_guid == guid of the immediately preceding message :  179 / 181
reply_to_guid pointing anywhere else (a true inline reply) :    2 / 181
thread_originator_guid populated (the real marker)         :    2 / 230
```

`reply_to_guid` is **auto-populated with the previous message in the thread.**
It carries no intent. The genuine inline-reply marker is
`thread_originator_guid`.

**Consequence:** any argument of the form *"she replied inline to message X,
therefore she had the thread open, therefore the absence of a read receipt means
she disabled them"* is **void**. That argument was built and then withdrawn
during the 2026-08-09 session.

**Action owed:** audit the corpus for prior analysis that treated
`reply_to_guid` as intentional threading. Any such claim needs rechecking.

## M3 — SQLite type-affinity trap

`strftime('%s', ...)` returns **TEXT**. When compared against a **computed
expression** — which carries no column affinity — SQLite ranks INTEGER below
TEXT unconditionally, so the predicate is **silently false for every row**.

Reproduced directly:

```
expression >= strftime('%s','now','-24 hours')                 →  0 rows
expression >= CAST(strftime('%s','now','-24 hours') AS INTEGER) →  1 row
```

This produced a zero-byte export that initially read as a substantive finding
about the data rather than a bug in the query. No error was raised.

**Canonical form** — cast explicitly, and keep the arithmetic on the right so
the index on `m.date` is usable:

```sql
AND m.date >= (CAST(strftime('%s','now','-24 hours') AS INTEGER) - 978307200) * 1000000000
```

Note also that a column *with* INTEGER affinity coerces the TEXT operand
correctly, so the same comparison works in one query and fails in another. That
inconsistency is what makes it dangerous.

## M4 — Absence of metadata is weak evidence in this corpus

```
SENT rows with NO delivered_at at all :  41 / 129
```

Clustered rather than random — a device-sync artifact (Mac vs. phone), not a
signal about the counterparty. **Any argument from a missing timestamp must
carry this caveat.** The record is incomplete by construction.

## Extraction recipe

Full-metadata pull for a single handle, macOS. Copy the database first — reading
it live risks a lock, and the `-wal` file holds messages not yet checkpointed
into the main file.

```bash
cp ~/Library/Messages/chat.db* /tmp/ ; sqlite3 -header -csv /tmp/chat.db "
SELECT datetime(m.date/1000000000+978307200,'unixepoch','localtime') sent_at,
  CASE m.is_from_me WHEN 1 THEN 'SENT' ELSE 'RECEIVED' END direction,
  CASE WHEN m.date_delivered>0 THEN datetime(m.date_delivered/1000000000+978307200,'unixepoch','localtime') END delivered_at,
  CASE WHEN m.date_read>0 THEN datetime(m.date_read/1000000000+978307200,'unixepoch','localtime') END read_at,
  CASE WHEN m.date_read>0 THEN (m.date_read-m.date)/1000000000 END secs_to_read,
  m.is_read, m.is_delivered, m.is_sent, m.is_delayed, m.error, m.item_type,
  m.associated_message_type, m.thread_originator_guid, m.service, m.guid, m.ROWID,
  COALESCE(m.text,'') text
FROM message m
WHERE m.ROWID IN (SELECT message_id FROM chat_message_join WHERE chat_id IN
   (SELECT chat_id FROM chat_handle_join WHERE handle_id IN (<ROWIDs>)))
AND m.date >= (CAST(strftime('%s','now','-24 hours') AS INTEGER)-978307200)*1000000000
ORDER BY m.date;" > ~/Desktop/out.csv
```

Resolve handle ROWIDs first — a contact may have several, and a `LIKE '%2449%'`
pattern will sweep in unrelated numbers:

```bash
sqlite3 /tmp/chat.db "SELECT ROWID, id FROM handle WHERE id LIKE '%<digits>';"
```

Requires **Full Disk Access** on the terminal. Without it the `cp` fails; do not
suppress its stderr, or the failure presents as an empty result set.

`m.text` is NULL for most recent messages on Monterey — the body lives in
`attributedBody` as a serialised `NSAttributedString`. This extract is for
metadata; pull text separately and join on timestamp.

## Why this page exists

Three of the four defects above produced, at some point in one session, a
**confident and wrong** intermediate conclusion: a zero-row result read as a
finding, a directional column read as undirectional, and an auto-populated field
read as intentional. None raised an error. The forensic method's exposure is not
to hard failures — it is to instruments that lie quietly and in the direction of
whatever is already suspected.

## RE-CHECKED [2026-08-20] — M4 gains its best real-world case, and the flagship example's scope was an artifact

Flagged stale against [[wiki/mind/concepts/forensic-method]] (edge additions
only, no claim on this page affected) and
[[wiki/timeline/events/august-2026-unmasking]], which gained substantive
prose. The second one matters.

**A scope correction on the worked example.** The unmasking page framed August
8–9 as ending with an unanswered message at 03:41:32. The fuller export filed
2026-08-20 shows the exchange resumed at 08:19 the same morning and ran all
day. That is a scope artifact of the 24-hour metadata extract, not an error in
the method — but it is exactly the failure mode **M4** warns about, applied to
a page's *framing* rather than to a single row: the absence of traffic at the
edge of an extraction window looks like the absence of traffic.

**M4 gains its strongest case, and it is not about metadata at all.** M4 holds
that in this corpus the absence of a signal is weak evidence. The August 16–19
window supplies a harder version of the same lesson, one level up:
**the presence of a signal does not identify its author.** At least six inbound
rows on Annie's 212 handle across July–August 2026 were typed by
[[wiki/people/jerel-coles|Coles]] holding her phone, in three separate
episodes, all during crises. There is no column for this. Read-receipt
analysis is especially exposed to it, because a receipt proves a *device* was
unlocked and looking, and this corpus now contains documented periods in which
the person holding that device was not its owner.

**Recommended addition to the extraction recipe, unimplemented.** Before
drawing a behavioural inference from device-level metadata in any window, check
whether the window overlaps a known third-party-access episode. The three known
ones are 2026-07-26 05:39–05:57, 2026-08-16 23:42–23:53 and 2026-08-18
21:46–21:50. Whether earlier ones exist has not been checked, and the only
detector available is register.

**No method-level finding on this page is withdrawn.** M1–M3 are properties of
`chat.db` and are untouched.

## Gaps

The underlying `annie_metadata_24h.csv` this page's counts are drawn from has
not been filed to `raw/self/message-csv/` — see the sourcing note above. Prior
corpus analyses that used `reply_to_guid` as a threading signal (M2) have not
yet been audited; that audit is owed and is listed in `BACKLOG.md`.

> **RE-CHECKED [2026-08-18] — premise moved, conclusion unaffected and slightly
> strengthened.** [[wiki/mind/concepts/forensic-method]] moved on 2026-08-18: its
> claim that the July 2026 Leviathan dashboards were the method's first outward
> deployment was corrected to 2025-07-11
> ([[wiki/timeline/events/james-analysis-pdf]]), and it gained a terminal step,
> [[wiki/mind/concepts/the-handed-mirror]]. Neither touches this page, which is
> about four defects in `chat.db` metadata extraction and the class of error they
> produce. The correction is in fact the same species of finding at a different
> level: a confident wrong answer that raised no error, held for two months
> because a cited source had been read to eleven percent of its length. The
> instrument that lied quietly there was a reading pass rather than a query.

> **RE-CHECKED [2026-08-23] — premise moved by one typed edge, conclusion
> unaffected.** [[wiki/mind/concepts/forensic-method]] gained an `instance-of` edge on
> 2026-08-23 into [[wiki/mind/profile/texting-deviance-audit]]. No content this page
> depends on changed. The new instance does rhyme with this page's subject: the audit's
> decisive move was a control that disconfirmed the hypothesis being tested — Dan's
> *first* messages in a turn start lowercase at the same rate as his continuations, so
> the lowercase opener is habit, not sentence-fragmentation. That is the same class of
> check whose absence produced the four `chat.db` defects catalogued here.

> **RE-CHECKED [2026-08-26] — premise moved by one typed edge, conclusion
> unaffected.** [[wiki/mind/concepts/forensic-method]] gained an `instance-of` edge
> into the new [[wiki/mind/profile/lexicon]] page — the same evidence-cite/
> authority-invoke/render-a-finding machinery documented there for crisis analysis,
> observed running on a compliment instead. Nothing about `chat.db` metadata
> extraction is downstream of that finding.

## The constitution pass

Run 2026-08-28, against the eleven registers in `SYNTHESIS_SPEC.md`. This
page is a technical methodology page — SQLite column semantics and a
type-affinity bug — and most registers genuinely do not bear on it; forcing
a fit where the content is mechanical rather than psychological would be
exactly the decorative citation this pass exists to catch, not to produce.
One register does bear, and it was already implicit rather than absent.

| # | Register | Disposition |
|---|---|---|
| 1. Cognitive stack | **Checked, does not add a distinct mechanism.** Ti-dominance's demand for verified truth could be gestured at for why these queries get run at all, but it would be redundant with register 2's more specific, corpus-confirmed account — not cited, to avoid citing the same fact twice under two names. |
| 2. Personality profile | **Moved the conclusion, and made explicit what was already implicit.** This page's own pre-existing `reassurance-architecture` citation calls read-receipt analysis "measurement substituting for reassurance" without naming what that architecture runs on. [[wiki/mind/profile/big-five-psychometrics]]'s Trust 9 — corpus-confirmed at 1.96x — is the one hop back: a confirmation that doesn't carry forward is why a device-metadata query gets run in the first place. |
| 3. Historical precedent | **Checked, does not bear.** The four defects are properties of `chat.db`, not of a documented pattern in Dan's history. |
| 4. Attitudes and forces | **Checked, does not bear.** |
| 5. Security and prosperity | **Checked, does not bear.** |
| 6. Health | **Checked, does not bear.** |
| 7. Romantic and relational state | **Already load-bearing, at one remove.** The worked examples (the August 2026 window, the third-party phone-access episodes) are relational in content but this page's own thesis is about the instrument, not about what the instrument found. |
| 8. Age and upbringing | **Checked, does not bear.** |
| 9. Geographic and ethnic culture | **Checked, does not bear.** |
| 10. Religious and ideological programming | **Checked, does not bear.** |
| 11. Axiomatic politics | **Checked, does not bear.** |
| 12. Other — provenance | **Checked, left standing.** Trust 9 is corpus-confirmed rather than self-commissioned, which is the stronger half of the provenance gradient this session has tracked elsewhere — appropriate here, since it is the only register-level claim this page now carries. |

**What survived:** all four defects (M1-M4), the extraction recipe, and
every re-check block — none required a profile-layer citation to stand,
since they are properties of a database schema. **What the pass added:** a
name for the psychological driver this page's own prior citation already
gestured at without stating. **What it did not do:** manufacture a
cognitive-stack connection to a page whose actual content is a SQL
type-coercion bug.


