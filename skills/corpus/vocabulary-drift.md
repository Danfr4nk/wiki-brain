status: active scope: corpus triggers:

- a per-year or per-era table built by keyword matching

- a claim that a subject is absent from a corpus, or went quiet

- a step change or inflection dated from counts over a long corpus

- building a regex to measure a topic across more than a few years sources:

- wiki/mind/synthesis/2020-left-turn.md — "What failed: any finer claim about the pre-2020 years"

- wiki/interests/music/overview.md — "And what the public record says"

- bin/mine-tweets — the docstring's five traps validated: 2026-09-02 supersedes: []

# A keyword count over a long corpus measures your vocabulary, not the corpus

## Instruction

1. **Before writing that a subject is absent, quiet, or stepped up in year N**, re-run the count with a pattern wide enough to produce false positives, and **read every hit**. If the broad pattern returns nothing at all, it is still too narrow.

1. **Read the years the count scores lowest**, in full, before believing the low score. That is where the failure hides, and on a 17-year corpus it is cheap — the quiet years are quiet.

1. **Build the pattern from the era you are measuring, not from the era you know.** A political vocabulary, a music vocabulary and a technology vocabulary all drift; the words Dan used in 2011 are not the words he used in 2024.

1. **State the denominator next to the share.** 24% of 25 originals is six tweets.

1. Where two patterns disagree, **publish the coarse shape both agree on and withdraw the fine claim** — do not offer a third table as if it settled it.

## Why

Keyword counting fails asymmetrically: it can only under-report, and it under-reports **most where the subject matter is least like the pattern's source era** — which is exactly where a corpus is most interesting. The result does not look broken. It looks like a finding, with a number attached.

This cost a published claim on 2026-09-02. `wiki/mind/synthesis/2020-left-turn` was given a table showing a first political step in 2017 (4.0% → 11.1%, "nearly tripling") that separated *engagement* from *identity*, plus a "documented off period" of 1.2–4.0% across 2013–2016. Both were withdrawn the same day. Re-measured with the vocabulary Dan actually used then — Troy Davis, capital punishment, Paterno, the Catholic Church, Occupy, Santorum — 2016 is **9.3%** not 4.0%, so the 2017 step is 9.3% → 11.1% and is not a step; 2013 is **7.8%** not 1.4%, so the off period was mostly the pattern failing to see.

The tell was in the archive the whole time. On **21 September 2011** — a year the first pattern scored at 1.3% — Dan posted four times across the Troy Davis execution, including a fully argued position on capital punishment. A year scored as near-empty contained an evening of sustained political writing.

The same failure had already produced two near-misses that day: a narrow music pattern gave "eleven years of silence" where the honest figure was ten and began on a different date, and a politics pattern reported **2026 as 0.0%** when it is **23.1%** — missing "EVERYBODY🙏HATES🙏ISRAEL🙏", Curtis Sliwa's "antizionist credentials", and "It's Irish Zionism" because none of that vocabulary existed in the pattern's source years.

## Validation

Run the count twice with deliberately different vocabularies and compare. If the per-year figures move, the finer claims are not measurable this way and only the shape both patterns agree on may be published. `bin/mine-tweets timeline '<narrow>'` against `bin/mine-tweets timeline '<broad>'` reproduces the 2026 case on the archive as committed.

## Known limits

This does not rescue keyword counting; it bounds it. Even the broad pattern is a keyword list and is still an undercount of unknown size — which is why rule 5 says withdraw the fine claim rather than publish a better table. Where a real answer is needed, the year has to be read.

Not yet tested against `bin/mine-messages` over the 196,399-message dump, where `wiki/interests/music/overview` carries several absence claims derived exactly this way and never checked. That is the obvious next place for this to earn or lose its keep.
