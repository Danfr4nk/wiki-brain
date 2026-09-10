# MANIFEST — @danfrank reply corpus from operator video, 2026-09-04

## Files

| **File** | **Rows** | **Status** |
| --- | --- | --- |
| `SOURCE.md` | 288 transcribed blocks | complete — verbatim as supplied, immutable |
| `replies.jsonl` | 288 | complete — derived from `SOURCE.md`, one object per block |

`excluded_under_directive: 5` — five rows addressed to `@Lo_weez`. Nothing else about them is recorded here or anywhere else. Three of the five are already quoted on `wiki/self/twitter/2015.md` from an earlier source and are left untouched there; the standing directive in `CLAUDE.md` is a stop on the record advancing, not a retraction.

**Fields stripped for privacy: none.** The source is a public profile scroll. No DM content, contact details, device or login history, or third-party private data appears in it.

## What this source is worth

`raw/self/twitter/archive.jsonl` holds **2,718 originals and 22 replies**. That ratio is an artifact of the archive's originals-only inclusion rule, not of how the account is used — `TWITTER_PULL.prompt` names it as the Tier 3 hole: *"the corpus has my monologue and none of my dialogue."*

This batch is **255 replies and 33 originals**. After dedup, **186 of the replies are new**. The corpus's reply record goes **22 → 208, a factor of 9.5**.

|  | **Rows** |
| --- | --- |
| Transcribed (post-exclusion) | 288 |
| Already in `archive.jsonl` | 89 (31%) |
| **New to the corpus** | **199 (69%)** |
| — of which replies | 186 |
| — of which originals | 13 |

## Dating: what this source can and cannot support

The video carries X's **relative-age labels** ("2d ago", "3y ago") and **no timestamps**. A whole-year label floors to a one-year band, so the derived fields are `window_start` / `window_end` and **`created_at`**** is ****`null`**** on every row**. No row in this file carries a date, because the source does not contain one.

**The 89 rows that were already in ****`archive.jsonl`**** calibrate the other 199** — they carry a true timestamp from a source that has one, so the label model can be tested rather than assumed:

| **Check** | **Result** |
| --- | --- |
| True date falls inside the derived band | **81 / 89 = 91%** |
| Misses by ≤ 7 days (band-edge, off-by-one) | 6 |
| **Misses by > 400 days (gross)** | **2** |
| Median absolute error, year-labels | 259 days (as expected for a floored year) |

**The two gross misses are the finding, and they are the reason no row here is dated.** `@JimNorton "I've been saying 'yuckamundo'"` carries an **8y** label and is truly **2014-10-16** — an age of 11.9 years. `@whatdirt "another enormous thank you for the support"` carries a **13y** label and is truly **2014-10-31** — an age of 11.9 years. Two posts eleven days apart in reality carry labels four and a half years apart in the video. That is not a rounding error in any direction; it is label-to-post misalignment somewhere between the scroll, the screen recording and the transcription.

So: **the labels are good enough to place a row in a band and never good enough to date one.** A row in this file may be assigned to a year page only when the row's own content anchors it against a dated public event. `~2%` of rows will be in the wrong band and nothing in this file can say which.

## Content anchors used

Where a row names a datable public event, that is stronger than its label and is what a wiki page may cite. The anchors that were actually load-bearing:

| **Anchor** | **Fixes** | **Label** |
| --- | --- | --- |
| Federal death-row commutations, 2024-12-23 | the `@yashar` cluster (3 rows) | 1y |
| Hunter Biden pardon 2024-12-01 / Charles Kushner pardon | `@AaronDSiegel` cluster (4 rows) | 1y |
| UnitedHealthcare CEO shooting 2024-12-04; Altoona arrest 2024-12-09 | `@defnotbeka` | 1y |
| Huckabee named ambassador, 2024-11-12 | `@koorah` | 1y |
| Baltimore Key Bridge collapse, 2024-03-26 | `@RealMichaelKee` | 2y |
| Butler PA rally shooting, 2024-07-13 | `@Matt_True` ×2, `@RedpillDrifter` ×2, `@Dumas24939934` | 2y |
| Al-Ahli hospital strike, 2023-10-17 | `@spectatorindex` | 2y |
| OceanGate *Titan*, 2023-06-18..22 | six `@OceanGateExped` rows | 3y |
| Trump "major announcement", 2022-11-14 | the seven-part THEORY thread | 3y |
| Hurricane Sandy, 2012-10-29 | four `@OpieRadio` rows | 13y |

## The 2025 question, answered in the negative

`TWITTER_PULL.prompt` flags this as the thing most worth settling: the wiki calls 2025 *"the collapse-year silence: 13 originals, the lowest count in the archive"* and reasons from it elsewhere. The **1y** band (2024-09-04 .. 2025-09-04) straddles it, so this batch could in principle have overturned it.

**It does not.** Every one of the 28 rows in that band that can be anchored at all anchors to **November or December 2024** — the election aftermath, the Huckabee appointment, the Mangione shooting, the pardons and commutations. **Not one row in this source anchors to any month of 2025.** The silence survives contact with 199 new rows, which is a better reason to believe it than it had before.

## What this source still does not have

- **No ids, no timestamps, no URLs, no metrics.** Nothing here can be merged into `archive.jsonl` by `id`, which is that file's dedup key. Dedup against it was done on normalised text and is recorded per row (`in_archive`, `archive_id`, `archive_match`: `exact` | `fuzzy`).

- **No parent tweets.** Every reply here is one side of an exchange. Tier 3 of `TWITTER_PULL.prompt` asks for replies *with parents hydrated*, and this is the half without them: what he said, not what he was answering. Several rows are close to unreadable for that reason and are recorded anyway.

- **No completeness claim of any kind.** This is one scroll of one profile in one video. It is a **sample**, its selection rule is unknown, and per-band counts from it must never be read as per-year counts. The 3y band has 76 rows and the 17y band has 4; that is a fact about the video, not about the account.

- **Four blocks merge several consecutive posts** into one transcribed block (the `@Phloxenheim` whistleblower run, the `@axolotl_wav` block ending `@yimmybastard This checks out`, the GOP-debates block, and the "privilege" block). They are kept as transcribed rather than split on a guess.

- **One row is not Dan's.** `@ZacharyShumar "Most identity groups are a skinsuit for their own internal discontent"` is the parent of a Dan reply and is kept as the only hydrated parent in the file. `author_handle` distinguishes it.
