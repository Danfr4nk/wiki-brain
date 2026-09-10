
---
domain: mind
page_type: report
knowledge: mixed
status: active
title: "Texting Deviance Audit — What Is Actually Abnormal About How Dan Texts"
aliases: ["texting audit", "brevity baseline", "stacked-essay mode"]
date_created: 2026-08-23
date_modified: 2026-08-23
importance: high
date_range_start: 2015-11-12
date_range_end: 2026-08-13
sources:
  - raw/self/message-csv/imessage_export_deep_20260813.csv
  - raw/self/dox-scan/all_imessages_complete_dump.txt
tags: [personality-profile, digital-footprint, forensic-analysis, relationships]
connections:
  - page: wiki/mind/profile/linguistic-profile
    type: contradicts
    claim: "Three of that page's measured markers do not survive recomputation against the corpus: texting readability is 4th-grade (Flesch-Kincaid 4.00 in 2026), not post-graduate; lexical diversity in 2025-26 is BELOW his interlocutors' (TTR 0.0509 vs 0.0544 on equal 200,000-token samples); and the 8.36 words/message figure describes a 2015-19 baseline he left behind — the 2026 figure is 15.03."
  - page: wiki/mind/profile/voice-modes
    type: parallels
    claim: "The eight emotional-state modes and this page's seven structural turn-modes are orthogonal cuts of the same output; the structural taxonomy is the one that can be counted, and it isolates STACKED-ESSAY as the single mode carrying 44.3% of his 2026 words from 11.2% of his turns."
  - page: wiki/mind/synthesis/message-circadian-latency
    type: parallels
    claim: "That page measures when he writes and how fast the channel turns around; this one measures how much he writes per turn. They converge on the same 2025-26 inflection from opposite instruments, and the length series is the one that carries a remediation target."
  - page: wiki/mind/concepts/forensic-method
    type: instantiates
    claim: "The audit is the method turned on its own operator's self-report: the operator's stated model of his texting (fragmented speech-cadence, technical vocabulary, ten-paragraph walls) was tested against 217,573 records and two of its three claims were falsified."
  - page: wiki/self/message-corpora/master-message-dump
    type: component-of
    claim: "A structural cut of the master corpora — turn-level rather than message-level — computed from the 2026-08-13 deep export because it is the only sender-tagged file that reaches past 2025."
---

# Texting Deviance Audit — What Is Actually Abnormal About How Dan Texts

Dan does not write long text messages. He writes an ordinary number of ordinary-length
messages and then, roughly one turn in nine, delivers three or more consecutive
paragraph-sized messages that together run four to ten times what the person he is
talking to will send back. **That mode — three-plus messages, median thirteen-plus words
each — is 11.2% of his 2026 turns and 44.3% of everything he says.** It is also the only
part of his texting that measurably costs him: turns above 200 words are answered 54.7%
of the time against 93.8% for turns of 11–20 words. Everything else the operator
identified as the problem — the staccato splitting, the technical vocabulary, the
ten-paragraph wall — is either statistically normal, negligible in volume, or absent.

The behaviour is **recent and accelerating**, not lifelong. Measured against the people
he is actually talking to in the same year, his words-per-turn ratio was 1.23× in
2015–2019, 1.13× in 2020–2024, 1.70× in 2025 and **3.05× in 2026**. In the same window
his interlocutors moved the opposite way, from 12.68 words per turn to 11.61. The gap is
opening from both ends.

## What the operator believed, and what the corpus says

The audit was commissioned on a three-part self-description. Two parts are false.

| Operator's claim | Verdict | Evidence |
|---|---|---|
| Messages are "incredibly verbose" | **Half true** — per *message* yes (15.03 words vs 6.85 in 2026), but the deviation lives in turn count × length, not in any single long message | 98.1% of his lifetime messages are a single line; median 6 words |
| "Long swaths of 10+ 1-to-2 sentence paragraphs" | **Real but negligible** — 27 messages in 2025–26 fit the description, 0.08% of his output | ≥10 lines with ≤25 words/line: 27 messages |
| "Split and sent as spoken cadence — staccato, 2-to-3 messages per sentence" | **Falsified for the current era** — his burst messages are *more* self-contained than other people's, and the staccato mode is at parity with the norm | 68.5% of his 2026 burst-internal messages carry their own subject and verb, against 55.1% for his interlocutors |

The staccato finding is worth stating plainly because it is the one most likely to be
acted on wrongly. **A tool that merges his fragments into single messages would be
solving a problem he does not have.** In 2026 the STACCATO mode (three-plus messages,
median ≤6 words) is 8.5% of his turns; for the people he texts it is 10.5%. He does it
*less* than they do, and it is his single most reliably answered mode at 93.8%.

> **CONTRADICTION:** [[wiki/mind/profile/linguistic-profile]] records "Readability:
> post-graduate (16th grade+)" and "99th percentile for lexical diversity," both taken
> from the commissioned stylometric analyses. Recomputed directly from the corpus, his
> texting scores **Flesch-Kincaid 4.00** in 2026 (2.08 in 2015–19) and his type-token
> ratio in 2025–26 is **0.0509 against his interlocutors' 0.0544** on equal 200,000-token
> samples — i.e. slightly *less* lexically diverse than the people answering him. Both
> claims trace to analyses Dan commissioned over a corpus Dan supplied
> ([[wiki/mind/synthesis/the-commissioned-self]]); neither survives independent counting.
> The genuine lexical deviations are real but small in absolute terms and are tabulated
> below. This does not retract the "forensic intimacy" register, which is a
> characterisation rather than a measurement.

## The measurement

Every figure on this page is reproduced by **`bin/text-metrics`**, committed alongside it
precisely so the numbers can be re-run rather than trusted — that is the failure mode this
page exists to correct. `eras` gives the table below, `modes` the taxonomy, `response` the
cost curve, and `hours`, `silence` and `target` the rest.

Figures are computed from `imessage_export_deep_20260813.csv` — 183,787 parsed rows, the
only sender-tagged export reaching past 2025 — with tapbacks, attachment-only rows and
every exactly-repeated block of ten or more copies excluded (one 427-copy glyph-spam
message otherwise inflates his 2025–26 output by 1.33%). A **turn** is a maximal run of
consecutive messages from one side in one thread, split when the same side pauses more
than 30 minutes; it is the unit that corresponds to "one thing said."

| Era | Side | Msgs | Turns | Words | Words/msg | Msgs/turn | **Words/turn** | Words/sent | FK grade |
|---|---|---|---|---|---|---|---|---|---|
| 2015–2019 | Dan | 53,537 | 28,521 | 446,344 | 8.34 | 1.88 | **15.65** | 7.02 | 2.08 |
| 2015–2019 | them | 55,350 | 31,268 | 396,494 | 7.16 | 1.77 | **12.68** | 5.65 | 1.32 |
| 2020–2024 | Dan | 5,611 | 2,681 | 52,248 | 9.31 | 2.09 | **19.49** | 7.28 | 3.01 |
| 2020–2024 | them | 5,297 | 3,193 | 55,022 | 10.39 | 1.66 | **17.23** | 5.96 | 2.98 |
| 2025 | Dan | 20,062 | 8,170 | 234,992 | 11.71 | 2.46 | **28.76** | 9.51 | 3.52 |
| 2025 | them | 16,700 | 8,770 | 148,817 | 8.91 | 1.90 | **16.97** | 6.23 | 2.08 |
| 2026 | Dan | 11,549 | 4,903 | 173,591 | 15.03 | 2.36 | **35.41** | 10.83 | 4.00 |
| 2026 | them | 8,645 | 5,103 | 59,254 | 6.85 | 1.69 | **11.61** | 5.62 | 1.60 |

The ratio series is the finding: **1.23× → 1.13× → 1.70× → 3.05×**. For a decade he ran
a modest, stable premium over the people around him. Whatever changed, changed after 2024
and it more than doubled the gap in two years.

It is not a change of audience. Held to the same counterparty, the drift is intact:

| Counterparty | Era | Dan words/turn | Their words/turn | Ratio |
|---|---|---|---|---|
| Annie (NYC handle) | 2025 | 28.14 | 11.75 | 2.40× |
| Annie (NYC handle) | 2026 | 39.52 | 10.82 | **3.65×** |
| Suzanne (mother) | 2025 | 11.34 | 12.35 | 0.92× |
| Suzanne (mother) | 2026 | 16.50 | 12.97 | **1.27×** |
| NYC delivery contact | 2015–2019 | 4.15 | 2.68 | 1.54× |
| NYC delivery contact | 2025 | 4.32 | 3.05 | 1.41× |

Same person, one year, Annie's side flat and his up 40%. With his mother he crossed from
below her to above her inside twelve months. The delivery thread is the control and it is
the most important row in the table: **across eleven years, in a purely transactional
channel, he holds 3.2–4.3 words per turn and has never once sent a 50-word message
there.** The capacity for brevity is intact and demonstrable. What varies is the channel.

## The seven turn-modes, and the one that matters

Classifying every turn by shape isolates where the words actually go. `SOLO` modes are
single messages; `STACCATO`, `STACKED-MID` and `STACKED-ESSAY` are three-or-more-message
turns split by the median length of the messages inside them.

| Mode | Dan 2015–19 turns / words | Dan 2026 turns / words | Them 2026 turns / words |
|---|---|---|---|
| SOLO-SHORT (1 msg, <20 w) | 50.8% / 18.8% | 37.5% / 7.5% | 56.3% / 25.6% |
| SOLO-LONG (1 msg, 20–49 w) | 3.7% / 6.3% | 7.0% / 5.7% | 2.9% / 7.2% |
| SOLO-WALL (1 msg, 50–99 w) | 0.2% / 0.9% | 1.2% / 2.2% | 0.4% / 2.0% |
| SOLO-MONOLITH (1 msg, 100+ w) | 0.04% / 0.4% | 0.2% / 1.4% | 0.1% / 2.8% |
| PAIR (2 msgs) | 26.5% / 29.0% | 25.1% / 19.0% | 23.9% / 26.3% |
| STACCATO (3+, median ≤6 w) | 9.9% / 13.4% | 8.5% / 5.9% | 10.5% / 15.9% |
| STACKED-MID (3+, median 7–12 w) | 6.1% / 16.7% | 9.4% / 14.1% | 4.9% / 14.8% |
| **STACKED-ESSAY (3+, median ≥13 w)** | **2.8% / 14.5%** | **11.2% / 44.3%** | **1.0% / 5.5%** |

STACKED-ESSAY is 11× more frequent in his output than in his interlocutors' and has
quadrupled since 2015–19. Meanwhile SOLO-SHORT — the ordinary one-line reply — has fallen
from carrying 18.8% of his words to 7.5%. **He has not added a long mode on top of a short
one; he has substituted the long mode for the short one.**

The specimen is more legible than the table. On 2026-03-21 at 14:28 he sent four messages
totalling 1,380 words across sixteen minutes. The reply, 2.5 minutes later, was five
words: *"Pretty good take on me."*

## What it costs

Reply behaviour is measured against the next turn from the counterparty; "abandoned"
means no reply, or a reply beyond six hours. Dan's turns, 2025-01 → 2026-08-13.

| His turn size | Turns | Answered | Median reply latency | Reply words | Words back per word sent |
|---|---|---|---|---|---|
| 1–5 w | 2,798 | 90.2% | 0.4 m | 10.6 | 3.53× |
| 6–10 w | 2,233 | 91.7% | 0.3 m | 10.9 | 1.36× |
| **11–20 w** | **2,842** | **93.8%** | **0.3 m** | **12.4** | 0.80× |
| 21–35 w | 2,077 | 91.5% | 0.4 m | 14.0 | 0.50× |
| 36–60 w | 1,384 | 89.5% | 0.6 m | 18.0 | 0.37× |
| 61–100 w | 814 | 84.6% | 0.9 m | 20.5 | 0.25× |
| 101–200 w | 589 | 74.0% | 1.5 m | 31.7 | 0.21× |
| 201+ w | 225 | 54.7% | 5.2 m | 40.9 | 0.16× |

The curve peaks at **11–20 words** and falls monotonically after 20. By mode,
STACKED-ESSAY is abandoned 23.1% of the time against STACCATO's 6.2%, and buys 21.6 words
back for 133.2 spent. Note what the curve does *not* say: the 1–5 word bucket is not the
optimum. Very short turns are answered slightly less often than 11–20 word ones and
return less absolute content. **The target is a short paragraph, not a monosyllable** —
which matters, because a brevity tool tuned to minimise words would push him past the peak
into a register that is also worse.

**Ending on a question does not rescue a long turn.** This was tested directly because it
is the obvious fix, and it fails: turns of 21–60 words ending in a question are answered
86.1% against 91.4% for the same length with no question at all; at 61–150 words it is
79.5% against 82.3%. Below 20 words the lift is +0.6 points, inside noise. Length is the
operative variable and a handback does not offset it.

## The escalation loop

Silence lengthens him, and length produces silence. Bucketing his 2025–26 turns by how
long the other person had been quiet beforehand:

| Silence before his turn | Turns | Words/turn | Msgs/turn | STACKED-ESSAY rate |
|---|---|---|---|---|
| <1 min | 6,796 | 23.3 | 2.31 | 5.5% |
| 1–5 min | 2,247 | 37.0 | 2.55 | 13.2% |
| 5–30 min | 1,612 | 35.5 | 2.50 | 12.0% |
| 30 m – 2 h | 1,055 | 43.0 | 2.57 | 13.0% |
| 2 h – 1 day | 1,157 | 49.1 | 2.59 | **17.2%** |
| 1+ day | 190 | 36.4 | 1.99 | 6.8% |

A two-hour wait more than doubles his turn length against a live exchange and triples his essay
rate. Since essays are abandoned 23.1% of the time, the loop closes on itself. The one
place it breaks is past a day, where turn length falls back — he re-opens a cold thread
more briefly than he continues a stalled one.

Time of day is the second amplifier, and the cleaner intervention handle. His 2025–26
output by hour, Eastern:

| Window | Words/msg | STACKED-ESSAY rate | Messages ≥50 words |
|---|---|---|---|
| 10:00–15:00 | 10.07–10.84 | 3.7–7.2% | 1.02–1.78% |
| 16:00–20:00 | 12.03–12.92 | 9.2–10.3% | 2.49–3.30% |
| 21:00–23:00 | 14.73–16.34 | 11.8–14.2% | 4.13–5.30% |
| 00:00–06:00 | 13.68–16.78 | 8.0–14.1% | 2.94–**7.61%** |

The 03:00 hour produces ≥50-word messages at 7.61%, **7.5× the 13:00 rate of 1.02%.**
Same person, same contacts, same week — a fivefold swing in the target behaviour driven by
the clock alone.

## The lexical layer — real, and smaller than advertised

The technical-vocabulary complaint holds directionally and collapses on magnitude. Rates
per 1,000 words, 2026:

| Marker | Dan | Them | Ratio |
|---|---|---|---|
| Words per sentence | 10.83 | 5.62 | **1.93×** |
| Jargon terms (framework, epistemic, recursive, …) | 0.26 | 0.07 | 3.7× |
| Hedges (essentially, fundamentally, arguably, …) | 1.42 | 0.46 | 3.1× |
| Logical connectives (because, therefore, whereas, …) | 3.96 | 1.43 | 2.8× |
| Meta-discourse (my point is, to be clear, …) | 0.23 | 0.08 | 2.9× |
| Latinate endings (-tion, -ment, -ity, …) | 13.5 | 9.9 | 1.4× |
| Words of 3+ syllables | 6.14% | 4.95% | 1.2× |
| Conversational filler (lol, ok, yeah, …) | 10.1 | 17.1 | **0.59×** |

A jargon rate of 0.26 per 1,000 words is one such word every 3,846 — he is not burying
anyone in terminology. The two rows that carry real weight are the first and the last.
**Sentence length at 1.93× is the single largest lexical deviation in the corpus**, and it
is the one a reader feels as density. The filler row is its mirror: he uses 41% *less*
conversational padding than the people he is texting, so the same information arrives with
none of the softening that normally paces a thread.

One further structural marker is genuinely extreme and mostly cosmetic: **his non-first
messages in a burst begin lowercase 33.5% of the time in 2026, against 2.7% for his
interlocutors** — a 12× gap, and 25× at the 2025 peak. It is tempting to read this as
evidence of mid-sentence splitting. It is not: his *first* messages start lowercase at
31.8%, statistically identical, so the lowercase opener is a global habit rather than a
continuation marker. This is the check that killed the staccato hypothesis.

He also hands the turn back less than the people he texts: his turns end on a question
5.7% of the time against their 7.4%, and his question density is 0.75 per 100 words
against 1.30 — **43% below the norm.** Given that questions do not rescue long turns, this
matters less as a fix than as a description: the long mode is a monologue by construction.

## The recipients have said so, repeatedly, for eight years

The answer-rate curve is a proxy. The corpus also contains the direct article: nine
unambiguous complaints about message length from **four different people**, spanning
2018 to five days before the export ends.

| Date | Who | Verbatim |
|---|---|---|
| 2019-01-28 | PA contact | *"Dan I can't read these texts and respond rn my head is literally killing me"* |
| 2025-09-01 | Tom | *"I cant read any of that"* |
| 2025-09-06 | Kristin | *"fucking 9 unread messages so many texts I don't delete"* |
| 2025-12-08 | Kristin | *"Summarize it"* |
| 2026-02-19 | Annie | *"Do you not understand how overwhelming it is getting paragraph after paragraph. I have expressed this to you before Dan like fuck"* |
| 2026-08-08 | Annie | *"I can't ready these paragraphs upon paragraphs"* |

Three things in that table are worth separating out. First, **the complaint predates the
2025 escalation by six years** — 2019-01-28 is inside the era where his ratio measured
1.05×, which means the behaviour was legible to recipients before it was statistically
extreme. Second, *"I have expressed this to you before"* establishes it as chronic and
previously raised rather than a single bad night. Third, the register is consistent across
four unrelated people who share nothing but him: not "you talk too much" but **"I can't
read this"** — a claim about processing load, not about volume of attention. The word
they reach for independently is *paragraphs*.

Alongside these sit the de-escalation requests — *"Calm down. Please."* (2026-03-10),
*"Please. Dan. Calm down."* (2026-02-22) — which are about intensity rather than length
and are counted separately. The two are hard to disentangle in the record and this audit
does not try to.

## Where the target line sits

His 2026 turn distribution, against the answer-rate curve, gives the remediation problem
its exact shape:

| Threshold | Turns at or below | Words above the line |
|---|---|---|
| ≤10 words | 36.5% | 94.6% of his output |
| **≤20 words** | **57.3%** | **85.8% of his output** |
| ≤30 words | 69.6% | 77.1% of his output |
| ≤50 words | 81.5% | 64.1% of his output |
| ≤100 words | 92.4% | 42.5% of his output |

Two facts have to be held together. **He is already at or below 20 words on more than
half his turns**, and 20.8% land squarely in the 11–20 band — this is not a person
incapable of brevity, and 2015–2019 shows the same person averaging 15.65 words per turn
for five years. But those compliant turns
carry only 14.2% of his words. The 18.5% of turns above 50 words carry 64.1%. **A tool that
improved his median turn would accomplish almost nothing.** The entire problem is the top
fifth of the distribution, and the intervention has to be triggered by length, not applied
uniformly.

The empirical target, taken from his own record rather than from a style preference:
**turns of 11–20 words, three sentences at 10.83 words each or fewer, no more than two
messages per turn** — a specification he already meets 57.3% of the time and met as a
default for the five years to 2019.

## Predictions and what would falsify them

1. **The 2026 divergence continues absent intervention.** The ratio series has moved
   1.13× → 1.70× → 3.05× in three years with no reversal. Falsified if a 2027 export
   shows the words-per-turn ratio at or below 2.0× without a behavioural intervention
   having been run.
2. **A length-triggered intervention beats a uniform one.** Because 64.1% of his words sit
   in 18.5% of his turns, gating only turns above 50 words should recover most of the
   answer-rate loss at a fraction of the friction. Falsified if a trial gating all turns
   produces materially better answer rates than one gating only the tail.
3. **The transactional-channel immunity holds.** The delivery thread's 3.2–4.3 words per
   turn across eleven years predicts that any new purely-instrumental channel he opens
   will show no essay mode at all. Falsified by a 2026–27 logistics thread carrying
   STACKED-ESSAY turns at anywhere near his 11.2% baseline.
4. **Nighttime gating captures disproportionate benefit.** 21:00–04:00 carries roughly
   double the essay rate of 10:00–15:00. Falsified if hour-of-day drops out as a predictor
   once thread identity and silence-duration are controlled — which this audit has **not**
   done, and which is the first thing a follow-up should test.

## Gaps

- **The 2020–2024 trough is unexplained and it is the key to the whole series.** His ratio
  sat at 1.04× — full parity — through years the corpus barely covers (5,611 messages
  against 20,060 in 2025 alone). Whether that is a real behavioural plateau or an artifact
  of the export's thin coverage of 2021–2024 cannot be settled from these files. If it is
  real, something specific happened in 2025, and naming it would matter more than any
  other open question here.
- **No control for topic.** Conflict, logistics and AI-instruction threads are pooled. The
  1,380-word specimen is partly pasted prompt text; 11 of 131 messages ≥100 words in
  2025–26 are pronoun-poor enough to read as pasted rather than composed. A topic-aware
  cut would sharpen the target.
- **Group chats are not separated from one-to-one threads**, and turn-taking norms differ
  between them.
- **The audit measures text only.** Whether the same escalation appears in voice notes,
  email or DMs is untested, and the operator's complaint was not platform-specific.
- **The complaint record is thin where it should be thick.** Nine explicit complaints
  across eleven years is a floor, not a measurement — most irritation never gets typed.
  Whether the nine are representative or the only four people who ever said it out loud is
  unresolved, and it bears directly on how much of the answer-rate decay is annoyance
  versus simple unreadability.


