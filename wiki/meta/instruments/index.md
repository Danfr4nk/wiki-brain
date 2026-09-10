
---
domain: meta
page_type: index
status: active
date_created: 2026-09-02
date_modified: 2026-09-02
sources: []
---

# instruments — index

**The measurement layer.** Every other page in this wiki *argues*: it reads
sources, reasons from them, and states a conclusion somebody could disagree
with. The pages listed here do not. They are the outputs of tools built to
**measure** something about Dan from first-party dated data, and they publish
what the measurement says and nothing else.

The distinction is not decorative, and it is why this section exists rather
than the instruments being scattered as ordinary entries. A synthesis is only
as good as the reasoning behind it, and reasoning about oneself is exactly
where a person is least reliable. An instrument is the part of the corpus that
does not depend on anyone reasoning correctly — including the wiki.

[[wiki/meta/journeys/the-instrumented-channel]] tells the older half of this
story: five instruments built to measure one high-volume relationship, each of
which turned out to measure something wider than the channel it was built for.
That is the pattern. This page is the standing catalogue of the ones that
survived into tools.

## The three rules every instrument obeys

**1. Evidence, not claim.** An instrument page states no finding. It presents
every record and the arithmetic over them, and stops. A finding *drawn* from an
instrument reaches an ordinary page through the normal operations — never the
generated one, which is overwritten on the next write. This is what keeps the
measurement usable as evidence in an argument it is not itself making.

**2. Generated, never hand-edited.** Each page is regenerated from an
append-only log or from the corpus, and a hand-edit fails the gate in
`bin/wiki-check`. A number somebody could quietly adjust is not a measurement.

**3. It states its own limits, in a section that cannot be dropped.** Coverage,
sample bias, what the instrument structurally cannot see. `bin/intake` never
prints a quantity statistic without the share of events it was computed from;
`bin/wiki-testimony` never prints a rate without its `n` and refuses a class
below `MIN_N` as a prior outright. An instrument that cannot state its own
denominator will be believed as though it had one.

## The ledgers

Event-sourced: an append-only JSONL log is the source of truth, a projection is
regenerated from it and safe to delete, and the wiki page is the public face.
Nothing is ever edited in place — a correction supersedes and the log keeps
both.

| Instrument | Measures | Standing state | Page |
|---|---|---|---|
| `bin/intake` | a finite quantity enters the record, and every known disposition of it after that — the anti-unreliable-narrator layer for consumption | 4 units, 9 events | [[wiki/health/intake-ledger]] |
| `bin/wiki-testimony` | every first-person claim the corpus has recorded, what settled it, and two numbers over the settled ones — **veracity** (how often he is right) and **calibration** (whether his stated confidence tracks it) | 12 claims, 6 settled, veracity 57/100 | [[wiki/meta/testimony-veracity]] |

These two are the same idea pointed at different unreliability. The intake
ledger sets a dated first-party dataset against *"I barely used anything that
weekend."* The testimony ledger sets an adjudication record against *"it was
definitely 2014."* Neither calls him a liar; both make the question answerable
instead of rhetorical.

## The measures

No ledger of their own — they compute over a corpus on demand, and their
findings land on ordinary pages that cite them.

| Instrument | Corpus | What it is for |
|---|---|---|
| `bin/mine-messages` | 217,573 messages · 106,629 sent, 110,944 received · 503 handles · 4.55M characters of Dan's own text | **Use this instead of grep.** Three properties of the dump make naive grep silently wrong |
| `bin/text-metrics` | the same corpus, cut by **turn** rather than message | Length and cadence. Message-level counts hide the effect entirely, because the unit of his speech is the turn — [[wiki/mind/profile/texting-deviance-audit]] |
| `bin/mine-tweets` | 2,741 originals, 24 Sep 2008 → 1 Sep 2026, from three sources of different fidelity (1,412 spreadsheet · 1,098 live scrape · 231 backend) | The public record. Carries its own coverage share on every engagement figure, and excludes 125 truncated rows from length figures |
| `bin/psychometrics` | lexical probes run against the message corpus | Tests a personality claim against what he actually typed, with a within-medium control |
| `bin/wiki-history` | 3,832 revisions across 495 pages, 11 Jul → 2 Sep 2026 | The git log read as a record of *operations* rather than saves |

## What the instrument layer cannot see, as a layer

**It measures what was written down, in the media that survived.** Every
instrument here reads text he typed or a quantity he logged. The 2026-08-02
axiom test is the cleanest demonstration and it is worth reading before
trusting any of these: four load-bearing unconscious axioms were tested
lexically against all 106,629 outbound messages with 110,944 inbound as a
control, and on every explicit urgency construction but one he writes *less*
than the people texting him. That did not falsify the axiom. What it
established is narrower and more useful — **SMS is a near-zero-introspection
medium for everybody in it**, so the corpus has a jurisdiction, and the
psychological layer is outside it. See [[wiki/self/context-core]].

**Adjudication is not a random sample.** A claim gets checked when somebody had
a reason to check it, and the reasons correlate with it being surprising,
load-bearing, or already doubted. The testimony ledger's settled set
over-represents both spectacular confirmations and spectacular failures, and
says so on its own page.

**A standing directive filters what may be recorded.** `CLAUDE.md` carries a
moratorium on new writing about one living person. `bin/wiki-testimony` and
`bin/wiki-plain` enforce it mechanically, as a refusal rather than a warning.
At least one cleanly adjudicated confirmation is excluded by it. The exclusion
is correct and it is still a bias — a score drawn from a filtered record that
does not announce the filter is worse than no score.

**Two of these publish to a public repository**, knowingly, by an operator
decision on 2026-08-30: `intake/` and `testimony/` are tracked and readable by
anyone, permanently, and git history cannot be un-published. The reversal order
is fixed and stated in `CLAUDE.md` — **make the repository private first,
verify it, and only then decide whether anything else is wanted.** In that
order, always.

## Adjacent, and deliberately not listed above

These measure **the system** rather than the person. Same discipline, different
subject, so they live with the rest of `meta` rather than here:
[[wiki/meta/skills]] (what each model has), [[wiki/meta/readers-digest]] (the
plain-language campaign), [[wiki/meta/digest]], [[wiki/meta/recent-activity]]
and [[wiki/meta/open-questions]].

## Adding one

An instrument is worth building when a page is making a claim that a
first-party dated record could settle and nobody can check it. Then:

1. **Name what it measures and what it structurally cannot.** The second half
   is not modesty — it is the section that goes on the page, and a tool that
   cannot say what it is blind to should not publish a number.
2. **Event-sourced if the record accumulates** (append-only JSONL, a
   regenerable projection, corrections that supersede rather than edit);
   **compute-on-demand if it reads a corpus.** The intake and testimony ledgers
   are the reference implementations for the first shape.
3. **Generate the page.** `page_type: dataset` with a `chart:` block, and a
   `check` subcommand that fails when the page has drifted from the log.
4. **Gate it in `bin/wiki-check`** — in `GENERATE` if it writes into `wiki/`,
   *and* in `GATE`. Those two sets must match: a gate on a file no step
   regenerates is a trap, not a check.
5. **Add the row here**, and to the tools table in `CLAUDE.md`.

---

[[wiki/meta/index|meta]] · [[wiki/meta/journeys/the-instrumented-channel|The Instrumented Channel]] · [[wiki/self/concepts/wiki-brain|The wiki]]


