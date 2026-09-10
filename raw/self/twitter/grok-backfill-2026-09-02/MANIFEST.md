# Twitter backfill — grok-backend session 2026-09-02

Source: X search + thread fetch via grok-backend, written to `inbox/twitter-backfill/` only. `raw/` was not touched.

Tooling constraint (read this first): this session does **not** have a full X account-export API. Search returns at most 10 posts per query. User lookup did not return `created_at` or `statuses_count`. Where that blocks a deliverable, the file is empty or incomplete and named below. Rows that *are* present were returned by the backend; none were invented.

Account: `@danfrank` / user id `16430736`. Public (not protected) as of this session.

## 1. Account creation date and time

**Not returned.** `x_user_search` for `@danfrank` gave id, name, bio, followers (252), avatar — not `created_at`. Profile syndication endpoints were unreachable from this session.

What *was* retrieved, and must not be confused with a backend `created_at`:

- Earliest tweet this session retrieved: `932618140` at `2008-09-24T04:52:36` UTC, text `i fucking looove winter park. this town is unreal.`

- `from:danfrank until:2008-09-24` and `from:danfrank max_id:932618139` both returned **no results**.

- `#MyTwitterAnniversary` tweet `1573610222916194304` at `2022-09-24T09:48:08` UTC: `14 years of pointless nothingness but at least I got the @danfrank handle #MyTwitterAnniversary` (1 like; photo `https://pbs.twimg.com/media/FdaWJzrWYAQFdjW.jpg`).

Those facts are consistent with creation on 2008-09-24. They are **not** a backend creation datetime. Do not cite them as one.

## 2. Total tweet count (all types, all time)

**Not returned.** No `statuses_count` on the user object. I will not estimate from search windows.

Existing archive holds 2,525 originals. This session cannot say how far that is from the truth.

## 3. Per-file row counts

| **file** | **rows** | **complete?** |
| --- | --- | --- |
| `01-pre-2009-10-20.jsonl` | 213 | **no** — lower bound from 10-result search windows |
| `02-thread-1548831640528510976.jsonl` | 3 | **yes** — full conversation |
| `03-repairs.jsonl` | 15 | **partial** — named (a) eight + named (c) six + the 2016 ulmdub row. (b) skipped |
| `04-gapfill-2009-2013.jsonl` | 0 | **skipped** |
| `05-reposts.jsonl` | 5 | **no** — latest 10-cap native RTs only |

## 4. Exclusion directive

excluded_under_directive: 0

No retrieved row mentioned `@Lo_weez` or “Annie”. Nothing was dropped. The 01 window predates her; 02/03 named ids did not hit the rule. 05 latest RTs did not hit the rule. Because 04/05/01 are incomplete, a later full export still has to apply the rule.

## 5. What could not be retrieved (named)

### Skipped wholesale

- **`04-gapfill-2009-2013.jsonl`**: a complete 2009–2013 dump cannot be produced at 10 results/query. File is empty rather than a fake complete set. Overlap from 01 (2009-01-01..2009-10-19 fragments) is *not* copied here.

- **`03(b)`**** null engagement for all of 2009–2013 and 2026**: same reason. I did not write guessed 0s over the 123 archive rows. Search *does* return integer engagement (almost always 0 on 2008–2009 originals); that is recorded on the 01 rows that exist, not as a 2009–2013 census.

- **`03(a)`**** remaining truncated ids**: archive has **129** texts ending in `…` / `...`, not 114. This file repairs the **eight ids named in the request** only. The other 121 were not re-fetched. Live text for those eight is what the thread fetch returned (often a `t.co` URL, not an expanded entity). Two of the eight (`368618598568194048`, `369480715974369280`) came back **without** the SoundCloud URL the archive stored in broken form; I did not copy the archive URL in. That is a live-backend gap, not a reconstruction.

- **Full ****`05-reposts.jsonl`**: only the five most recent `filter:nativeretweets` hits (search cap 10, five of which had usable original text/media). Seventeen years of amplification is not here.

- **User ****`created_at`**** and ****`statuses_count`**: see §§1–2.

- **Expanded URL entities**: thread/search tools returned `t.co` (and some `tinyurl`/`twitpic`/`bit.ly` as originally posted). I did not expand them from the damaged archive strings.

### 01 paging holes (file is a lower bound)

Windows used: month-end 10-result slices plus denser paging on 2008-09-24, 2008-10, 2008-11, 2008-12, 2009-10-14..19. Each window that returned 10 hits is truncated at 10 — there are more tweets in those months. Months with 10 hits (definitely incomplete): 2008-10, 2008-11, 2008-12, 2009-02, 2009-03, 2009-04, 2009-05, 2009-06, 2009-07, 2009-08, 2009-09, 2009-10 (pre-20th). 2008-09-24 itself returned 6 for `since:2008-09-24 until:2008-09-25` and is the strongest candidate for a complete day. 2009-01 returned 8.

Earliest id in 01: `932618140`. Latest in 01: `5000240511` (`2009-10-19T20:53:44`).

### Incomplete field on one written row

- `2091767147227644233` (`05`): native RT of `@TheDarkEnjoyer`; search returned `RT @TheDarkEnjoyer:` with no original text. `quoted.text` is `null`. Video URL is present. Engagement `reposts=1570` is what the tool attached to the RT card (likely the original’s count, not Dan’s). Same caveat on the other four 05 rows’ `reposts` fields.

### Anniversary / profile media not written as a tweet row

`1573610222916194304` was retrieved and is described in §1. It is already in the existing archive window (2022) so it was not duplicated into 03.

## 6. 2016 “ulmdub birthday party” tweet

**Yes.**

| **field** | **value** |
| --- | --- |
| id | `696416822011289601` |
| created_at | `2016-02-07T19:34:43` (UTC) |
| text | `Had lit times playing @ulmdub birthday party last night at OSU` |
| type | original |
| likes / replies / reposts | 0 / 0 / 1 |
| media | 1 video, `https://video.twimg.com/ext_tw_video/696416801966559232/pu/vid/720x1280/eOlDnH7HoGrU7xG8.mp4` |
| url | [https://x.com/danfrank/status/696416822011289601](https://x.com/danfrank/status/696416822011289601) |

Exact text match to the secondary source. Authoritative row is in `03-repairs.jsonl`. The archive’s 2016 is not complete.

## 7. Protected / deleted / archived tweets this pass would have missed

- **Protected:** no. Account is public.

- **Deleted:** not enumerated. Every *named* id in the request still resolved (six “empty text” ids, eight truncated ids, the 1/3 thread root and both continuations, the 2016 ulmdub id). I have no list of ids that 404.

- **Archived / hidden by X:** not reported by these tools.

- **Missed by construction:** all pure retweets except five recent ones; all 2009–2013 tweets beyond the 10-hit windows; 121 unrepaired truncated rows; any tweet the search index no longer returns (deletes, unindexed media-only, etc.).

## Completeness policy used

Per the request: do the parts that can be done completely, leave the rest empty or explicitly incomplete, never invent a row.

- Done completely: **02** (3/3 thread, including the 3/3 which has no `(3/3)` marker in the live text).

- Done for named ids: **03(a) eight**, **03(c) six**, plus the 2016 gap in §6.

- Lower bound only: **01**, **05**.

- Empty on purpose: **04**, **03(b)**.

## 03(c) notes (the six “empty text” rows)

All six ids still exist. None are empty of both text and media:

| **id** | **live text** | **media** |
| --- | --- | --- |
| `475846682807394304` | `💯💯💯` | none returned |
| `899707641492119552` | `https://t.co/biuRe3oioO` | 1 photo |
| `1592495078790295552` | `https://t.co/SFwg36PUgv` | 1 photo; self-reply in the 2022-11-15 Gohmert thread (`conversation_id` `1592492864176803840`) |
| `1764269658339782856` | `https://t.co/OS7WLWS1v8` | 2 photos; self-reply to `1764269565305868291` |
| `1809006805739241691` | `https://t.co/jVhvKnkXG2` | 1 photo |
| `1855791546458689939` | `🔮` | none; **quote** of own `1544965084472135680` |

## Schema notes

- `id` / `conversation_id` / `in_reply_to_status_id` are strings.

- `created_at` is UTC `YYYY-MM-DDTHH:MM:SS` with no timezone suffix, converted from the GMT timestamps the tools returned.

- `source` is the literal `grok-backend`.

- `type` is `reply` when `conversation_id != id` or a parent status was visible in a thread fetch. A leading `@mention` with `conversation_id == id` was left as `original` (common in 2008–2009). `in_reply_to_status_id` is filled only when the parent id was actually observed, never copied from `conversation_id`.

- `is_self_thread` is true only when the observed parent is Dan’s own tweet.

- `quoted` is an object `{handle, text, id?}` for quotes/reposts, else `null`. Extra keys are allowed.

- Engagement integers are what the tools returned. Old originals are almost all 0. On `type=repost`, `reposts` may be the original’s count.

## Next merge

Dedup by `id` into `raw/self/twitter/archive.jsonl`. 01 will add pre-2009-10-20 originals the archive never had. 02 adds `1548831642017533952` and `1548831643321901056`. 03 overwrites the named damaged rows and inserts `696416822011289601`. 04 adds nothing. 05 is originals-by-design-excluded territory (pure RTs).
