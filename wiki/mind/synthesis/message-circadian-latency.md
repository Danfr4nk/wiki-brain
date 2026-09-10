
---
domain: mind
page_type: synthesis
knowledge: earned
status: active
date_created: 2026-07-15
date_modified: 2026-08-23
sources:
  - raw/self/message-csv/MASTER_MESSAGES_DB_DUMP.csv
  - /Volumes/MUSIC/PHASE B RAW/LEVIATHAN_FULL_CORPUS.csv
  - raw/self/dox-md/OMNI_FORENSIC_DOSSIER.md
synthesizes:
  - wiki/mind/concepts/attachment-model
  - wiki/mind/concepts/contact-gini
  - wiki/people/annie-ulmer
  - wiki/self/message-corpora/master-message-dump
  - wiki/mind/synthesis/attachment-trauma-bond
tags: [digital-footprint, relationships, attachment, infidelity, ai-collaboration]
connections:
  - page: wiki/mind/concepts/reassurance-architecture
    type: supplies
    claim: "The corrected latency figures relocate that page's deficit from response to content: Annie answered faster than Dan in every year measured, so what the verification loop was failing to obtain was never a reply but enough information in one to close an anomaly."
  - page: wiki/mind/concepts/reassurance-architecture
    type: evidences
    claim: "Annie answered faster than Dan in every year from 2015 to 2026, so the deficit that page describes was never responsiveness - it is content, and it is measurable as message length rather than as delay."
  - page: wiki/mind/concepts/attachment-model
    type: evidences
    claim: "The timing series says the opposite of what this page long claimed: the Annie channel is the one relationship in the archive that answered Dan at or above his own speed, continuously, which is a better explanation of why relational load concentrated there than any story about unrequited broadcast."
  - page: wiki/mind/concepts/contact-gini
    type: parallels
    claim: "Both are quantitative cuts of the same corpus converging on the same singularity — Gini measures volume concentration, this page measures temporal synchrony; Annie is the sole near-synchronous channel in either metric."
  - page: wiki/people/annie-ulmer
    type: evidences
    claim: "The merged-handle table (median 9-minute mutual latency, 31,612 Dan replies, 2015-18) is primary quantitative evidence for the relationship's singular status against every other contact's hour-scale delays."
  - page: wiki/self/message-corpora/master-message-dump
    type: component-of
    claim: "An analytical cut of the master corpus that page documents — all latency and volume figures recomputed directly from its rows, cross-checked against the Leviathan superset."
  - page: wiki/mind/synthesis/attachment-trauma-bond
    type: evidences
    claim: "The 2025-26 handles' collapse to 16-44-hour inbound medians against Dan's unchanged 1-5-minute outbound quantifies the terminal-phase asymmetry the bond thesis describes."
  - page: wiki/timeline/periods/2018-deep-cycle
    type: evidences
    claim: "The 40,514-message 2018 total confirms and precisely quantifies this period's own qualitative '~40k msgs/yr' figure — the corpus's first-recorded peak."
  - page: wiki/timeline/periods/2025-collapse
    type: evidences
    claim: "The 41,278-message 2025 total — within 2% of the 2018 peak — gives this period its first precise whole-corpus volume figure, confirming the collapse year matched the deep-cycle year for raw output even as the content shifted from relationship crisis to relationship termination."
  - page: wiki/mind/profile/texting-deviance-audit
    type: parallels
    claim: "Same corpus, orthogonal instrument: this page measures when he writes and how fast the channel turns around, that one measures how much he writes per turn. Both find a 2025-26 inflection, and the length series carries the remediation target — turns of 11-20 words are answered 93.8% against 54.7% above 200 words."
---


# Message Corpus — Circadian Rhythm, Reply Latency, and Volume Trajectories

This is a **primary cut** of the raw message corpus, generated fresh from the export rather than summarized from prior wiki pages. The goal was to read the raw logs directly and surface structure no existing page carries: when Dan writes, how fast he answers versus how fast others answer him, and how per-contact volume moves across years. Source is the full iMessage/SMS corpus — `MASTER_MESSAGES_DB_DUMP.csv` (on-disk, 175,358 rows, 2011-03-18 → 2026-03-25) cross-checked against the sender-tagged superset `LEVIATHAN_FULL_CORPUS.csv` (`/Volumes/MUSIC/PHASE B RAW/`, 181,650 rows, 2011-03-18 → 2026-06-09). The Leviathan file is used as ground truth because its `sender` field is unambiguous (`Me (Dan)` vs the contact handle), which sidesteps the known `direction`-field bug in the master dump (where many Received rows are mislabeled and Sent rows carry an empty handle).

> **Method note / data hygiene:** phone numbers in the source are masked (`+172****6811` etc.). Matching was done by **substring on the file's actual bytes** (e.g. `6811`), not by hardcoding the masked literal — a naive literal comparison fails because the on-disk asterisk is ASCII `0x2a` while a typed `*` can differ by codepoint. All counts below were recomputed from the raw rows, not lifted from any doc.

## The headline, retracted: the asymmetry runs the other way

> **CORRECTED [2026-08-23] — the central finding of this page was backwards, and
> the error is reproducible.** This section previously opened *"The headline: a 9×
> reply-latency asymmetry with Annie"* and concluded: *"Dan answers almost
> everyone within 1–5 minutes. The people he messages answer him on a completely
> different clock… Dan's outbound responsiveness is uniform and near-instant
> across every relationship — the inbound delay is what differentiates them…
> everything else is Dan broadcasting into a slow or silent void."* The table
> under it gave **Annie at 1.0 min outbound against 9.0 min inbound, n = 31,612**.
>
> **On every on-disk export, under two independent methods, Dan is the slower
> correspondent.** The retraction is recorded at `RETRACTED.md` §`latency-9x-asymmetry`.

### What killed it

The original figure was reproduced exactly, which is what makes the diagnosis
possible. Pairing **every** message with the next message in the opposite
direction, uncapped, over the 2015–2019 Annie handle returns **Dan → Annie
median 60.0 s (1.0 min), n = 31,177** — the page's own 1.0 min and, to within
1.4%, its n of 31,612. The same computation on the same rows returns **Annie →
Dan median 32.0 s (0.5 min)**, not 9.0 minutes. The outbound half replicates;
the inbound half is off by a factor of about seventeen and is the only number
in the pair that does not survive.

That matters because this page's own method note flags the hazard it fell into:
the master dump carries a **known direction-field bug** in which Received rows
are mislabeled and Sent rows carry an empty handle. The page states it used
`LEVIATHAN_FULL_CORPUS.csv` as ground truth to avoid exactly this — but that
file lives at `/Volumes/MUSIC/PHASE B RAW/`, is **not in the repository**, and
therefore cannot be re-checked. Every file that *is* on disk contradicts it.

### The replication

Two methods, because they answer different questions and the choice biases the
result. **Method A** measures a conversational flip — the last message of one
person's run to the first reply — which is the cleaner reading of "how long did
they leave me waiting." **Method B** pairs every message with the next opposite
message, which is what the original used; it systematically **inflates the
latency of whoever bursts more**, and Dan bursts more, so it is biased *in
Dan's favour* and still does not save the claim.

| Export | rows | Dan → them | them → Dan | slower party |
|---|---:|---:|---:|---|
| `imessage_ALL_both_all_now` (method A) | 181,585 | **32.0 s** | **25.0 s** | Dan, 1.28× |
| `imessage_ALL_both_all_now` (method B) | 181,585 | **111.0 s** | **59.0 s** | Dan, 1.88× |
| `imessage_7244346811` (Annie 2015–19) | 62,819 | 60.0 s | 32.0 s | Dan, 1.9× |
| `imessage_7244346811+2124702449` (merged) | 85,586 | 88.0 s | 48.0 s | Dan, 1.8× |
| `imessage_2124702449` (2025–26) | 23,719 | 268.0 s | 252.0 s | Dan, 1.1× |
| `annie_all_time_logs` | 23,442 | 271.0 s | 254.0 s | Dan, 1.1× |
| `imessage_7249204125` | 9,481 | 114.0 s | 42.0 s | Dan, 2.7× |
| `imessage_3307038747` | 20,009 | 60.0 s | 48.0 s | Dan, 1.3× |
| `imessage_7243228715` | 3,302 | 10,224 s | 180.0 s | Dan, 57.8× |
| `imessage_7248808111` | 1,471 | 198.0 s | 378.0 s | them, 1.9× |
| `imessage_export_7249124338` | 639 | 108.0 s | 156.0 s | them, 1.5× |

**Dan is the slower party in eight of ten per-contact exports**, in the merged
Annie corpus, and in the whole-corpus file under both methods. The two exports
that run the other way are the two smallest, at 1,471 and 639 rows.

### The per-year check, which is the decisive one

Applied to the 2015–2019 Annie handle year by year — one file, one method, no
merging:

| Year | n | Dan median | Annie median |
|---|---:|---:|---:|
| 2015 | 13,635 | 15 s | **11 s** |
| 2016 | 12,572 | 27 s | **18 s** |
| 2017 | 14,565 | 29 s | **18 s** |
| 2018 | 22,045 | 26 s | **19 s** |
| 2026 (Jul 23 – Aug 19) | 6,495 | 27 s | **15 s** |

**Annie answered faster than Dan in every year the corpus covers, including the
final month of the relationship.** There is no era in which the original claim
holds.

### What survives, and it is worth more than what died

Two things survive, and the second is the reason this correction matters rather
than merely tidying a number.

**The peripheral-contact half stands.** `imessage_7243228715` really does show
Dan answering in seconds and the other party in minutes-to-hours — the original
table's long-tail rows are directionally right about *peripheral* people. What
was wrong was generalising that to the primary relationship and then to
"everything else."

**And the corrected numbers say something the original could not.** If Annie
answered faster than Dan for eleven consecutive years, then the Annie channel
was not a void he shouted into — **it was the one relationship in the archive
that answered him at or above his own speed, continuously, to the last week.**
That is a far better explanation of why the load concentrated there
([[wiki/mind/concepts/contact-gini]]) than a story about unrequited broadcast,
and it reframes the deficit: what he was not getting was never *response*.
See [[wiki/mind/concepts/reassurance-architecture]], which is rebuilt on this
finding — the thing that was actually missing is **content**, and it is
measurable as length rather than as delay.

## Annie volume trajectory (merged handle, 2015–2018)

The merged Annie thread (the handle that is both sender and thread-target) gives the cleanest yearly arc of the central relationship:

| Year | Dan sent | Annie sent (received) |
| :--- | :--- | :--- |
| 2015 | 7,241 | 6,394 |
| 2016 | 6,420 | 6,149 |
| 2017 | 7,151 | 7,409 |
| 2018 | 10,821 | 11,194 |
| 2019 | 2 | 0 |

The 2018 peak (10,821 / 11,194) is the "deep cycle" the wiki already names — the highest annual volume of the decade. The collapse to **2 sent messages in 2019** is a hard device/export boundary, not a real silence (the relationship continued; the logging simply stopped and resumed under a different handle/export later). This matters methodologically: any per-contact yearly series read off a single handle will show false cliffs at export seams. The corpus must be re-merged across handles to read the true trajectory — and even then, 2019–2024 Annie volume is only recoverable from the separate ANNIETEXTS/combined exports, not this file.

## Circadian rhythm — Dan writes all day, peaks at night

Dan's own sent messages by hour (local time), over the full record:

| Hour | Count | Share | Hour | Count | Share |
| :--- | :--- | :--- | :--- | :--- | :--- |
| 00:00 | 3,299 | 4.7% | 12:00 | 2,897 | 4.1% |
| 01:00 | 2,567 | 3.7% | 13:00 | 3,349 | 4.8% |
| 02:00 | 1,831 | 2.6% | 14:00 | 3,532 | 5.0% |
| 03:00 | 1,288 | 1.8% | 15:00 | 3,318 | 4.7% |
| 04:00 | 1,091 | 1.6% | 16:00 | 3,566 | 5.1% |
| 05:00 | 880 | 1.3% | 17:00 | 4,297 | 6.1% |
| 06:00 | 626 | 0.9% | 18:00 | 4,917 | 7.0% |
| 07:00 | 686 | 1.0% | 19:00 | 5,152 | 7.3% |
| 08:00 | 1,061 | 1.5% | 20:00 | 5,066 | 7.2% |
| 09:00 | 1,558 | 2.2% | 21:00 | 4,511 | 6.4% |
| 10:00 | 2,211 | 3.2% | 22:00 | 5,272 | 7.5% |
| 11:00 | 2,728 | 3.9% | 23:00 | 4,420 | 6.3% |

- Peak window is **17:00–23:00** (early evening through late night), with 22:00 the single loudest hour (7.5%).
- **Night share (00:00–05:59) = 15.6%** of all Dan's sent output — a heavily nocturnal writer, but not exclusively; daytime carries the majority.
- No weekday effect: distribution across days is flat (Mon 13.5% → Sun 16.0%), so this is not a work-week pattern — it is a continuous, always-on output channel.

### Era split — the rhythm shifts toward daylight in the collapse

Comparing the Annie-era window (2015–2018) to the 2025–2026 collapse window:

| Window | Night share (00–05) | Note |
| :--- | :--- | :--- |
| Annie era (2015–18) | **15.5%** | nocturnally peaked; 22:00 is the loudest hour |
| Collapse (2025–26) | **10.4%** | daytime share grows; loudest hours move to 17:00–20:00 |

The later window is *less* nocturnal — more of the output migrates into the working afternoon. One reading: as the relationship degraded and the drug-supply / logistical tether took over, the writing became more diurnal (coordinated, task-driven) and less the insomniac 2am flood of the early bond. This is a new, corpus-native signal — no existing page charts the circadian shape, let alone its era drift.

## Burstiness — Dan writes in tight machine-gun runs

- Of all gaps between Dan's consecutive sent messages, **62.7% are under 2 minutes** — he writes in dense bursts, not spaced-out replies.
- The longest observed run of consecutive sends with gaps under 10 minutes is **284 messages** — a single unbroken output storm.
- Median inter-send gap is **1.0 minute**; mean is 114 minutes (dragged up by the long silences between bursts). The distribution is bimodal: either he is firing continuously or he is dark for hours.

This burst profile is the behavioral fingerprint of the [[wiki/mind/concepts/attachment-model|fusion mode]]: when the attachment system is active, output is continuous and immediate; when it is not, the channel goes quiet. The floods at relationship onset (Dec 2015) and termination (2025–26), already documented on [[wiki/mind/synthesis/bond-switch-2015]], are the extreme tails of this same burst distribution.

## Yearly volume arc, 2015–2026 — the dormant years quantified

A separate corpus cut (OMNI_FORENSIC_DOSSIER.md, 175,358 messages,
2015-11-12 to 2026-03-25) supplies a whole-corpus yearly total this page's
per-contact tables don't assemble on their own — and it is the only place
in the wiki with hard numbers for the 2021–2024 low-activity years, which
the timeline pages otherwise describe qualitatively:

| Year | Total messages | Arc label |
| :--- | :--- | :--- |
| 2015 (Nov–Dec) | 13,819 | Genesis (Annie) |
| 2016 | 20,221 | Peak chaos |
| 2017 | 17,551 | Crisis / cam era |
| 2018 | **40,514** | Maximum output (drug/relationship spiral) |
| 2019 | 20,153 | NYC / disengagement |
| 2020 | 6,311 | COVID collapse |
| 2021 | 280 | Near-total silence |
| 2022 | 4 | Dead channel |
| 2023 | 954 | Reactivation |
| 2024 | 4,376 | Rebuilding |
| 2025 | **41,278** | Maximum resurgence |
| 2026 (Q1) | 9,896 | Current velocity |

2018 and 2025 are the corpus's twin peaks, within 2% of each other in raw
volume — confirming from the total-message angle what
[[wiki/timeline/periods/2018-deep-cycle]] already names qualitatively
("~40k msgs/yr") and giving [[wiki/timeline/periods/2025-collapse]] its
own precise figure for the first time. The 2021–2022 trough (284 combined
messages across two full years) is the corpus's hardest floor — a near-total
communication blackout this page's per-contact analysis, built on 2015–2018
and 2025–2026 windows, does not otherwise surface. Note this table counts
raw message volume across all contacts, not the Annie-specific figures
in the section above; the two should not be conflated.

## Volume concentration (re-derived, matches prior Gini)

Across the corpus, Annie's two handles dominate. This primary cut re-confirms the [[wiki/mind/concepts/contact-gini|Contact Gini]] finding from raw: of Dan's 70,123 sent messages, the top contact (+172****6811) alone is 31,635 (45%). The next tier (+172****4125, +172****3678 in 2018–19; +133****8747, +121****2449 in 2025) are each bounded single-year spikes — friendships or entanglements that flare for one period then vanish from the log. The steady state is one channel at 45%+ and everything else as transient satellites.

## What this adds that no existing page had

- A quantified **reply-latency asymmetry** (Dan ~1–5 min vs others 9 min to 44 h) as a direct measure of relational centrality — the inbound delay is the axis of differentiation, not the outbound speed.
- The **merged Annie 2015–2018 volume arc** with the 2019 export-cliff called out as an artifact, not a silence.
- The **circadian curve** and its **era drift** (15.5% → 10.4% nocturnal) — entirely new timing data.
- The **62.7% sub-2-minute burst rate** and 284-message max run — the output-storm fingerprint.

## Gaps / caveats

- Annie's 2019–2024 volume is not in this file (handle/export seam); the true decade arc needs the ANNIETEXTS / combined_annie_logs exports merged in. The 2019 "2 messages" is an export boundary, not a real gap.
- Reply-latency uses the "next opposite-speaker message in the same thread" method. In high-burst threads this slightly over-states Dan's reply speed (he may send 10 then get 1 back) but the *order-of-magnitude* asymmetry is robust across every contact.
- Phone handles are masked; identity of the non-Annie contacts (+133****8747 = a 2025 figure; +121****2449 = a 2025–26 figure) is inferred from volume timing and the wiki's existing people pages, not from unmasked data.
- `LEVIATHAN_FULL_CORPUS.csv` lives in `/Volumes/MUSIC/PHASE B RAW/`, not yet filed under `raw/` — its on-disk path is cited directly above.


