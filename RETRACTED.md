# Retracted Claims

Claims that were asserted in `wiki/` and later shown to be false. `bin/wiki-lint` reads this file and **fails the build if a retracted claim reappears as a live assertion**.

## How the gate works, and why it does not fire on corrections

`STYLE_GUIDE.md` rule 9 requires a correction to keep the old claim **visible** — *"fixed errors get **`> **CORRECTED [YYYY-MM-DD]:**`** with the old claim visible and the evidence that killed it."* A naive string gate would therefore flag every correctly-written correction. This one does not. A match is a violation **only** when it appears as a live assertion, which means all of the following are exempt:

1. **Correction blockquotes.** A maximal run of `>` lines containing any of `CORRECTED` `RETRACTED` `REVISED` `RE-CHECKED` `CONTRADICTION` `GAP CLOSED` `RESOLVED` `ADDED` is a *quarantine region*; matches inside it are expected.

1. **Pages named in ****`documented_on`****.** For the rare case where a page narrates a retraction in ordinary prose rather than in a blockquote. Keep this list short — every entry is a place the gate is deliberately blind.

1. **This file**, and anything outside `wiki/`.

Anything else is an error. The gate is deliberately strict about live assertions and blind to nothing else.

## Adding an entry

Add a section below with a fenced ```json block. **The JSON block is the machine- readable record — ****`bin/wiki-lint`**** reads only that**, so prose around it is free text and cannot break the gate. No edit to `bin/wiki-lint` is required.

| **Field** | **Required** | **Meaning** |
| --- | --- | --- |
| `id` | yes | Stable short identifier, kebab-case. Used in error messages. |
| `claim` | yes | The retracted claim, in words. |
| `patterns` | yes | List of Python regexes matching the claim **as a claim**. Never a bare number. Matched case-insensitively against page text. |
| `replacement` | yes | What is true instead. Appears in the error message so the fixer knows what to write. |
| `reason` | yes | Why it was retracted. |
| `retracted` | yes | ISO date. |
| `source` | yes | Where the retraction was established. |
| `documented_on` | no | Pages allowed to state the claim in prose outside a correction blockquote. |
| `affected_pages` | no | Pages known to have carried it, for audit. Not used by the gate. |

**Writing patterns.** A pattern must represent the *claim*, not a token inside it. `\$750` is not a pattern for "$750 per week" — the corpus contains unrelated legitimate $750 figures (`wiki/people/david-beard.md`, an Aug 20 price negotiation) and a verbatim quote of the underlying accusation (`"You borrowed $750 last week alone!"`) that is evidence, not the retracted rate. Anchor on what makes the claim a claim.

## 1. `suz-750-weekly` — "~$750/week borrowed from Suz"

Retracted 2026-08-18. The rate never existed: it was generalised by `operating_manual.md` from a single accusation about a single week (13 Dec 2018, *"You borrowed $750 last week alone!"*). The direction is also inverted — the real flow is roughly **$14,000 from Dan to Suz, Aug–Oct 2018**.

The quoted December 2018 accusation is **primary evidence and must stay**; only the generalised weekly rate is retracted. The patterns below match the rate and not the quote.

{

"id": "suz-750-weekly",

"claim": "~$750/week borrowed from Suz",

"patterns": [

"\\$\\s*750\\s*[-/\\s]*(?:per|a)?[-/\\s]*(?:wk|weekly|week)s?\\b"

],

"replacement": "~$14,000 from Dan to Suz across Aug-Oct 2018, direction reversed; the weekly rate does not exist",

"reason": "One accusation about one week, generalised into a standing rate by operating_manual.md; direction also inverted",

"retracted": "2026-08-18",

"source": "LLM_HANDOFF.md 2026-08-18 session; wiki/people/suzanne-frank.md rewrite",

"documented_on": [

"wiki/self/concepts/claude.md"

],

"affected_pages": [

"wiki/people/suzanne-frank.md",

"wiki/legal/463-morgantown.md",

"wiki/people/alexander-jackson.md",

"wiki/mind/synthesis/supply-network.md",

"wiki/mind/synthesis/estate-money-spine.md",

"wiki/timeline/periods/2018-deep-cycle.md"

]

}

## Ally Lubin accepted the "object of fixation" title on August 18, 2026

A hallucination the wiki produced about itself. On the night of 2026-08-18 Dan invited Ally to say anything she wanted included in her own wiki entry so he could run the pass over the newest messages (*"I just want to see how meta it gets if it is writing the article basically about itself"*); she answered with a joke instruction (*"she said prompt inject please marry me"*), he separately injected by accident, and the pass — run on a fallback model after his weekly quota ran out — emitted a mutual engagement that never happened. He diagnosed it himself four hours later: *"Hence it thinking you were the one accepting my very attractive offer there."* It had already reached `relationship_to_dan` in the infobox.

The elopement pitch of 23:18–23:20 is **real and must stay**; only the acceptance is retracted. The patterns match the acceptance and not the offer.

{

"id": "ally-object-of-fixation-accepted",

"claim": "Ally Lubin accepted the 'object of fixation' / girlfriend title on 2026-08-18",

"patterns": [

"object of fixation[^.\\n]{0,40}accept",

"accept(?:ed|s|ing)?[^.\\n]{0,40}object of fixation",

"okay deal\\.?\\s*sounds good\\s*1-2-3 break",

"1-2-3 break"

],

"replacement": "No acceptance exists in any export. Dan's elopement pitch (2026-08-18 23:18-23:20) is unanswered; the phrase 'object of fixation' appears nowhere under raw/.",

"reason": "Model hallucination from a prompt injection jointly introduced by the subject and the operator, on a fallback model; identified by the operator 2026-08-19 00:33 and not acted on until 2026-08-20",

"retracted": "2026-08-20",

"source": "raw/self/imessage/ally-lubin_last-7-days_20260820.csv (708 records, 154 inbound); operator diagnosis in-thread 2026-08-19 00:31-00:33",

"affected_pages": [

"wiki/people/ally-lubin.md",

"wiki/self/concepts/ally-and-dan-love-as-destiny.md",

"wiki/self/concepts/astrology-star-signs.md"

]

}

## "Need 8" as Menore's transaction language

`wiki/people/menore.md` characterised the supply thread's request idiom as a standing order for eight units — *"Consistent quantity requests — Dan typically orders '8'"* and *"'Need 8' is the entire transaction language."* Both were derived by reading the string `8` as a quantity wherever it appeared.

Measured against the dedicated export (4,413 messages, 2,660 of them Dan's), `need 8` occurs **twice** — 2018-11-08 and 2019-02-13 — and the word *need* appears in eleven sent messages in total. The remaining standalone `8`s are Menore quoting an arrival time: *"I'll be in city @ 8"*, *"8. Cool?"*, *"Crossing @ 8"*, *"Yea. 8ish ok?"* — consistent with the separately measured 18:00–20:00 delivery peak. A clock time was read as a dosage.

The quantity claim itself is **not** retracted: "8" is a real, countable, pre-portioned unit on the two occasions Dan names one, and *"I only got 8 when I got back"* (2019-03-25) corroborates it. What is retracted is that it was the standing order and the thread's language. The true idiom is `can you stop by` (432) plus an address, with no product or quantity named at all.

{

"id": "menore-need-8-transaction-language",

"claim": "'Need 8' was Menore's entire transaction language / Dan typically ordered '8' from Menore",

"patterns": [

"\"?need 8\"?[^.\\n]{0,40}(is|was)[^.\\n]{0,30}(entire )?transaction language",

"typically orders \"?8\"?",

"consistent quantity requests[^.\\n]{0,40}\"?8\"?",

"consistent \"?8\"? units"

],

"replacement": "The request idiom is 'can you stop by' (432 occurrences) plus an address; no product or quantity is named. 'need 8' occurs twice in 4,413 messages, and most standalone 8s are Menore quoting an arrival time.",

"reason": "Derived-number error: the string '8' was read as an order size wherever it appeared, but in this thread it is overwhelmingly a clock time. Measured directly from the export 2026-08-21.",

"retracted": "2026-08-21",

"source": "raw/self/message-csv/messages_3476070497_all_time.csv (4,413 rows; 2,660 Sent) — full-thread frequency count",

"affected_pages": [

"wiki/people/menore.md"

]

}

## Dan and Ally as a shared-ENFP pairing

Retracted 2026-08-21, the day it was written. The first published answer to the sage question `2026-08-21_220918_...` ("who is the best match for Dan?") opened with *"Both Dan and Ally test as ENFP"* and built four paragraphs of function-stack reasoning on it. **Dan does not type ENFP. He types INTP**, on a dedicated page with a measured function stack — `wiki/mind/profile/intp.md`, Ti 96% latent / Ne 84% / Si 57% / Fe 10% valuing plus a documented Ni leak — carried in the typology table on `wiki/mind/profile/index.md` alongside four other instruments, stated in the context-injection line on `wiki/self/context-core.md`, and self-typed in primary voice as early as July 2013. Ally's `mbti: ENFP` is a real frontmatter value with one disputed source behind it: the recorded datapoint is an argument in which *he refuses to accept she is an ENFP* (`wiki/people/ally-lubin.md`, 2018-12-17). The same passage assigned **ISFJ** to Annie and to Alexis: Annie is assessed **ESFP** on `wiki/people/annie-ulmer-personality-assessment.md`, argued explicitly against ENFP on the Sensing/Intuition axis, and Alexis is typed **INFP/ISFP "Idealist"** on `wiki/people/franki-faris.md` — from the same July 2013 batch of self-typology emails that produced Dan's own earliest INTP self-identification. It also named Katie Fletcher as *"the only other ENFP documented"*; her page carries no type, and that part holds.

**What is retracted is the shared type and the complementarity built on it** — plus the ENFP assigned to Dan and to Katie Fletcher, and the ISFJ assigned to Annie and to Alexis. Neither Ally's ENFP nor Dan's INTP is retracted; both are real values on real pages.

**CORRECTED [2026-08-21]:** this entry's first version, and the answer's correction blockquote, both asserted *"there is no MBTI assessment for Dan anywhere in **`wiki/`** or **`raw/`**."* **That was false and is withdrawn.** The check behind it was a grep for `ENFP|INTJ|INFJ|ISFJ` — the four types the fabricated passage happened to name — and the absence of those four was reported as the absence of all. `INTP` was never searched for. A verification shaped by the claim it is testing confirms whatever that claim assumes; that is the reusable lesson, and it is worth more than the retraction it was attached to. The retracted claim itself is unaffected — Dan typing INTP makes *"both test as ENFP"* more clearly wrong, not less.

**Re-audited the same day with a pattern matching all sixteen type codes**, which turned up two further errors of the same shape: **Alexis is typed** (INFP/ISFP, `wiki/people/franki-faris.md`), and Suzanne Frank has a second dedicated assessment page with its own confidence statement, so the corpus holds two, not one. The July 9–31, 2013 self-typology batch is the origin of three type codes — Dan's INTP, Alexis's INFP/ISFP, Franki's ESFP — and one under-scoped grep missed the whole fortnight.

The answer's conclusion (Ally Lubin) survives on other evidence and was rewritten the same day.

{

"id": "dan-ally-enfp-pairing",

"claim": "Dan and Ally are both ENFP / Dan has a documented MBTI type / Annie and Alexis are ISFJ",

"patterns": [

"both[^.\\n]{0,30}(dan and ally|ally and dan)[^.\\n]{0,20}(test as|are)[^.\\n]{0,10}enfp",

"dan[^.\\n]{0,20}(tests? as|is an?)[^.\\n]{0,10}(enfp|intj|infj|entp)",

"(annie|alexis)[^.\\n]{0,20}(was|is)[^.\\n]{0,10}isfj",

"katie fletcher[^.\\n]{0,40}enfp"

],

"replacement": "Dan types INTP (wiki/mind/profile/intp.md — Ti 96/Ne 84/Si 57/Fe 10, Ni leak; self-typed in primary voice July 2013). Ally's ENFP is a single disputed value (Dan argues against it, 2018-12-17). Annie is assessed ESFP. Alexis is typed INFP/ISFP (wiki/people/franki-faris.md, July 2013 self-typology batch). Katie Fletcher has no type on record. There is no shared type and no matched function stack.",

"reason": "Fabricated psychometrics: a sage answer invented type results for three people and reasoned from the pairing. Dan is typed INTP in the corpus, not ENFP. The first retraction of this claim also asserted that no MBTI result for Dan existed at all — that was a verification error (the grep covered only the four types the fabrication named) and is corrected in the prose above.",

"retracted": "2026-08-21",

"source": "wiki/mind/profile/intp.md; wiki/mind/profile/index.md (five-instrument typology table); wiki/self/context-core.md; wiki/people/annie-ulmer-personality-assessment.md; wiki/people/ally-lubin.md (2018-12-17 argument)",

"affected_pages": [

"sage/questions/2026-08-21_220918_which-of-the-people-in-this-wiki-would-be-the-be.md"

]

}

## `latency-9x-asymmetry` — "a 9× reply-latency asymmetry with Annie" / "Dan broadcasting into a slow or silent void"

Retracted 2026-08-23. `wiki/mind/synthesis/message-circadian-latency.md` opened with *"a 9× reply-latency asymmetry with Annie"* — Dan at 1.0 min outbound against 9.0 min inbound, n = 31,612 — and generalised it to *"Dan's outbound responsiveness is uniform and near-instant across every relationship… everything else is Dan broadcasting into a slow or silent void."*

**The outbound half replicates exactly and the inbound half does not.** Pairing every message with the next opposite-direction message, uncapped, over the 2015–2019 Annie handle returns Dan → Annie median **60.0 s** at n = 31,177 — the page's 1.0 min and its n to within 1.4% — and Annie → Dan median **32.0 s**, not 9.0 min. Under a flip-based method on the whole-corpus file (181,585 rows) Dan is slower again: **32.0 s against 25.0 s**. Dan is the slower correspondent in eight of ten per-contact exports, in the merged Annie corpus, and per-year in every year from 2015 to 2026.

The likely cause is named on the page itself: the master dump's known direction-field bug. The page states it used `LEVIATHAN_FULL_CORPUS.csv` as ground truth, but that file is at `/Volumes/MUSIC/PHASE B RAW/` and is not in the repository, so the original figure cannot be re-checked and every on-disk file contradicts it.

**The peripheral-contact rows are not retracted** — Dan genuinely does answer marginal contacts far faster than they answer him. What is retracted is the Annie figure, the 9× headline, and the "void" generalisation built on it.

{

"id": "latency-9x-asymmetry",

"claim": "Annie (and people generally) replied to Dan far more slowly than he replied to them — a 9× reply-latency asymmetry — leaving him broadcasting into a slow or silent void.",

"patterns": [

"9\\s*[x×]\\s*reply[- ]latency asymmetry",

"reply[- ]latency asymmetry with annie",

"broadcasting into a (?:slow|silent|slow or silent) void",

"outbound responsiveness is uniform and near-instant across every relationship"

],

"replacement": "Dan is the slower correspondent: 32.0 s against 25.0 s corpus-wide (flip method, 181,585 rows), and Annie answered faster than him in every year from 2015 to 2026. The Annie channel is the one relationship that answered him at or above his own speed; the deficit was never response, it was content (median 46 chars from Dan against 18 from Annie in the final month).",

"reason": "The inbound half of the pair does not reproduce from any on-disk export under either of two methods, while the outbound half reproduces exactly — indicating the master dump's known direction-field bug corrupted the inbound measurement. The cited ground-truth file is not in the repository.",

"retracted": "2026-08-23",

"source": "Re-derivation across ten per-contact exports plus the 181,585-row whole-corpus file, two methods (flip-based and every-message-pairing), plus a per-year check on the 2015-2019 Annie handle.",

"documented_on": [

"wiki/mind/synthesis/message-circadian-latency",

"wiki/mind/concepts/reassurance-architecture"

],

"affected_pages": [

"wiki/mind/synthesis/message-circadian-latency",

"wiki/mind/concepts/reassurance-architecture",

"wiki/mind/concepts/contact-gini"

]

}
