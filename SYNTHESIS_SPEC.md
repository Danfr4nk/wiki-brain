# Synthesis Spec — how the wiki reasons from itself

Adopted 2026-07-26. One of the six governing documents (see `STRATEGY.md` for the full set), binding on the same tier as `STYLE_GUIDE.md` (page format), `EXTRACTION_SPEC.md` (extraction depth) and `CONNECTIONS_SPEC.md` (edge format). This file governs **altitude** — how conclusions stack on top of conclusions, and what obligations a page takes on when it reasons from other pages instead of from `raw/`. `bin/wiki-climb` mechanically enforces it.

## Why this exists

`CLAUDE.md` has always claimed that "today's synthesized conclusion is tomorrow's premise." The repository did not enforce it. `bin/wiki-lint` requires every `sources:` entry to be a real path under `raw/`, which means a page reasoned entirely from four other wiki pages had no legal way to say so — it had to cite the raw material its inputs were built from, as though it had re-derived everything itself. The compounding was real but invisible, and invisible compounding cannot be checked, queued, or kept current.

Worse, nothing propagated. When a page changed, the pages that had reasoned from it went on asserting conclusions built on the old version. A second brain whose premises silently rot is a filing cabinet with extra steps.

This spec fixes both: it makes wiki-derived-from-wiki a first-class, declarable relationship, and it makes that declaration carry an obligation.

## The altitude ladder

Four tiers. Nothing here is new — the repository already contains all four — but naming them makes the ladder climbable on purpose rather than by accident.

| **Tier** | **What it is** | **Cites** | **Example** |
| --- | --- | --- | --- |
| **T0** | Immutable source | — | `raw/self/message-csv/*.csv` |
| **T1** | Ground page: one entity, event, period, or place, read out of `raw/` | `sources:` | `wiki/people/annie-ulmer` |
| **T2** | Junction page: one pattern found across 3+ ground pages | `synthesizes:` | `wiki/mind/synthesis/supply-network` |
| **T3** | Doctrine: one rule found across 2+ junctions, domain-general | `synthesizes:` | `wiki/mind/synthesis/block-unblock-loop` |

A page's tier is **computed, not declared** — `bin/wiki-climb audit` derives it from what the page cites. Do not add an `altitude:` field; the citations already carry the information, and a hand-maintained tier number would drift.

The ladder is not a hierarchy of quality. A T1 page can be the best page in the repository. It is a hierarchy of *inputs*, and its only purpose is to make one question answerable: what is not yet climbed?

## `synthesizes:` — the new field

sources:                          # T0 evidence: paths under raw/, must exist

- raw/self/message-csv/annie_all_time_logs.csv

synthesizes:                      # wiki pages this page REASONS FROM

- wiki/people/annie-ulmer

- wiki/people/tom

- wiki/people/rick-frank

Rules:

1. **`sources:`**** means raw. ****`synthesizes:`**** means wiki.** A path under `raw/` in `synthesizes:` is an error, and vice versa. Keeping them separate is the entire point: it makes the boundary between "read this once" and "reasoned from what we already understood" mechanically visible.

1. **Every entry must resolve** to a real page, and must not be the page itself.

1. **A page with ****`synthesizes:`**** is ****`knowledge: earned`**** by default.** If it is genuinely mechanical — a table assembled from other pages' numbers with no argument added — mark it `derived` explicitly and say why in one line.

1. **`synthesizes:`**** is not ****`connections:`****.** An edge says how two pages relate. `synthesizes:` says *this page would not exist without that one*. The overlap is expected and fine: most entries in `synthesizes:` also earn a typed edge. The difference is that a typed edge is a claim, and a `synthesizes:` entry is a dependency.

1. **A T2/T3 page still needs raw provenance for any new number it states.** Reasoning from pages does not license inventing figures. If you compute something new, verify it against `raw/` and cite the raw file in `sources:` alongside the `synthesizes:` list.

## The staleness rule — what makes this living rather than layered

**If page B declares ****`synthesizes: [A]`****, and A's ****`date_modified`**** is later than B's, B is stale.** `bin/wiki-climb check` reports it, and a stale page is a debt: the conclusion may still be right, but nobody has looked since its premise moved.

Clearing it is a real pass, not a date bump:

1. Read what actually changed in A (`git log -p`, or the page's `changelog:` and any `REVISED` blocks).

1. Decide whether B's conclusion survives it. Three outcomes, all legitimate:

  - **Survives** — add one line to B saying it was re-checked against the change and why it holds. Then bump `date_modified`.

  - **Needs revision** — a `> **REVISED [date]:**` block. Revise, never regenerate; see CLAUDE.md's second-brain rule.

  - **Is falsified** — see the next section. This is the valuable case.

1. Bumping `date_modified` without doing 1 and 2 is the one prohibited move in this spec. It silences the alarm and keeps the debt.

## Predictions and their resolution

A synthesis page that cannot be wrong is not a conclusion, it is a summary. The highest-value thing a T2/T3 page does is **state what it predicts**, so that the corpus can later settle it.

- Where a page's argument implies something not yet in evidence, say so plainly, in the body, marked as a prediction and scoped to what would falsify it.

- When new raw settles one, **record the resolution on the page rather than editing the prediction away.** A falsified prediction that is quietly deleted destroys the most valuable thing in the repository: a documented instance of the model being wrong in a specific, correctable way.

- The worked example is `wiki/mind/synthesis/block-unblock-loop.md`. It predicted the June 2026 severance could hold, scored the dependency as dead, and was falsified 52 days later by a channel it had not thought to count. The page now carries the failed prediction, the correction, and the widened rule — and the widened rule is *new knowledge that did not exist in any raw source*. That is the whole mechanism in one page.

This is the sense in which synthesis "generates new data": not by inventing facts, but by producing falsifiable structure whose failure is itself a finding.

## The write-back obligation — how insight gets amortized

Adopted 2026-08-01 from `STRATEGY.md`'s core loop. This is the counterpart to the staleness rule: staleness pushes information *down* the ladder when a premise moves, and write-back pushes it *up-and-back-out* when a conclusion is reached.

**A finding that lives only on the synthesis page has been discovered once. A finding written back into its members has been discovered permanently.**

When you write a T2 or T3 page, every page named in `synthesizes:` must come away carrying the finding:

1. **A typed edge back into the synthesis** — `instantiates` from the member, `instance-of` from the synthesis — on *every* member, without exception.

1. **A claim that states what the member turned out to be evidence of**, not merely that the two pages are related. The test: a reader who lands on the member page and reads only its `connections:` block should learn the conclusion the synthesis reached about it. "Franki Faris relates to dormancy-not-exit" fails. "Five days of occupancy in 2013 left no corpus and no later trace, which is the control bounding the retention rule to relationships that clear a tenure floor" passes.

1. **A prose sentence on the member** wherever the finding is load-bearing for that member — i.e. where a stranger reading the member page would be misled by its absence. Not every member needs one; the ones the argument turns on do.

The reason this is mandatory rather than encouraged is entirely practical. The corpus is read one page at a time, by models with finite context, usually arriving at a member page rather than at the synthesis. If the member does not carry the conclusion, the conclusion is invisible at the moment it is needed and gets re-derived — badly, from less evidence, by a weaker model. Every skipped write-back is a future re-derivation.

**This applies to revisions too.** When a synthesis is widened, corrected, or falsified, the members' claims are now stale in substance even though no tool will flag them — nothing checks that an inverse claim still says something true. Re-read them and update the ones the change touched.

## CLIMB — the fourth operation

`CLAUDE.md` defines INGEST, QUERY and LINT. **CLIMB** is the fourth, and it is the only one that increases altitude. It runs on the wiki, never on `raw/`.

One climb per pass, fully:

1. **Find the cluster.** `bin/wiki-climb candidates` maintains `synthesis-queue.md`: groups of 3+ pages that are densely connected to each other, span ≥2 domains, and have no page above them. Take the top scoring cluster, or one you have independent reason to prefer.

1. **Read the member pages in full.** Not their summaries — the pages. You are reasoning from them, so the reasoning has to touch them.

1. **Find the governing rule, or abandon the cluster.** The test: can you write one sentence that is true of every member, is not true of the corpus generally, and that a stranger could try to falsify? If not, record the rejection in `synthesis-queue.md` with a line of reasoning and move on. A cluster that resists synthesis is knowledge too. **Do not write a page whose thesis is "these things are related."**

1. **Run the constitution pass — mandatory, before the page is written.** The candidate rule is checked against the eleven registers below. This is not a citation formality; it is the step that decides whether the rule you found is a rule *about Dan* or a rule about the seven pages you happened to read. See "The constitution pass" below — **a synthesis page written without it is not finished, whatever else is on it.**

1. **Write the page.** `page_type: synthesis`, `knowledge: earned`, `synthesizes:` listing every member, thesis in the first two sentences, the rule stated plainly, a table of members against the rule, the controls or counterexamples that carry the argument, at least one prediction, a Gaps section, and the constitution pass's own result — which registers moved the conclusion, which were checked and left it standing, and which the corpus cannot presently speak to.

1. **Wire it, and write the finding back.** Typed edges both ways per `CONNECTIONS_SPEC.md`. Every member page gets an `instantiates` edge whose claim states what that page turned out to be evidence *of*, and a prose sentence wherever the finding is load-bearing for it. See "The write-back obligation" above — this step is the one that makes the synthesis compound instead of merely existing, and it is the one most often left half-done.

1. **Gates and log.** `bin/wiki-lint`, `bin/wiki-connect check`, `bin/wiki-climb check` — all three at 0 errors. `log.md`: `## [YYYY-MM-DD] climb | <domain> | <page> (N synthesized, M rejected)`. Commit.

## The constitution pass — the step that makes a conclusion about a person

Adopted 2026-08-28 by operator directive, and it is **critical, deterministic and not delegated to judgment**: it runs on every synthesis, every sage answer, and every earned conclusion on an entity page, whether or not the material seems to call for it.

### Why it exists

A pattern found across N pages is, on its own, a statement about **those N pages**. It becomes a statement about *Dan* only once it has been checked against the thing generating the behaviour — a specific mind, with a measured cognitive stack, running inside a specific body, history, family, county, class position, ideology and moment. Skip that check and the failure is not that the page is unsupported; it is that the page is **accidentally about the corpus's sampling** rather than about its subject, and it will read as authoritative anyway.

The failure has a worked example in this repository, which is why the rule is now written down. On 2026-08-28 three synthesis pages were written on cognition and relational architecture — `the-binary-verdict`, `no-platonic-channel`, `the-serial-monogamist` — and between them they cited **one of the eleven pages in ****`wiki/mind/profile/`**. The page specifically about how Dan's mind resolves questions cited **none of them**. It argued that verdicts come out binary while factual estimates come out graded, and never reached for `intp`'s measured **Ti at 96% against Fe at 10% valuing** — a dominant function whose entire job is "does this hold together, yes or no" set against a near-absent function that is the one that would produce a graded *relational* judgment. It argued trust has no stable middle value without citing **Trust at the 9th percentile** on `big-five-psychometrics`, which `reassurance-architecture` had already read as the reason a confirmation "decays" instead of carrying forward as a prior. The conclusions were not wrong. They were **re-derived from behaviour when the mechanism was already measured and sitting one directory away**, which is exactly the waste `STRATEGY.md`'s core loop exists to prevent.

### The eleven registers

Every one gets a decision. The decision may be *"checked, does not bear on this"* — that is a legitimate and useful outcome, and recording it is what makes the next pass cheap — but it may not be *silence*.

| **#** | **Register** | **Where it lives** |
| --- | --- | --- |
| 1 | **Cognitive stack** — function order, and what each function is *for* | `wiki/mind/profile/intp`, weighted by `wiki/mind/profile/trait-corpus-map` |
| 2 | **Personality profile** — measured traits, types, deviation scores | `wiki/mind/profile/`: `big-five-psychometrics`, `enneagram-5w4`, `socionics-and-attitudinal`, `deviance-mapping`, `neurodivergence` — **weighted by ****`wiki/mind/profile/trait-corpus-map`** |
| 3 | **Historical precedent** — has this shape happened before, and when | `wiki/timeline/`, `dormancy-not-exit`, `interests-as-era-markers` |
| 4 | **Attitudes, trends and forces** — what was moving in him and around him | `the-cool-metric`, `chaos-preference`, `intake-constancy`, `2020-left-turn` |
| 5 | **Current environment — security and prosperity** | `estate-money-spine`, `wiki/places/337-saratoga-drive`, `wiki/legal/463-morgantown`, `wiki/work/` |
| 6 | **Health** — chemical, physical, psychiatric | `wiki/health/`, `supply-network` |
| 7 | **Romantic and relational state** | `the-unbroken-bond`, `attachment-model`, `arrangement-history`, `wiki/people/` |
| 8 | **Age and upbringing** — how old he was, who raised him, what it cost | `wiki/timeline/periods/`, `rick-frank`, `suzanne-frank`, `fran-coldren` |
| 9 | **Cultural markers — geographic and ethnic** | `fayette-return`, `wiki/self/ancestry`, `ancestral-dialectic`, `wiki/places/` |
| 10 | **Religious and ideological programming** | `wiki/mind/politics/`, `2020-left-turn`, `wiki/self/concepts/` |
| 11 | **Axiomatic political belief** | `wiki/mind/politics/axioms`, `political-psyops`, `vertical-authority-skepticism`, weighted by `trait-corpus-map` |

Plus a standing twelfth slot: **any other personal factor the material itself raises.** The list is a floor, not a ceiling — it exists so that nothing on it is forgotten, not so that everything off it is excluded.

### The trait filter — what registers 1, 2 and 11 may actually carry

Adopted 2026-09-06 by operator directive. The registers above name *pages*. A page states a score; it does not say how much weight a conclusion may put on it. So the pass could be run honestly, every register given its decision, and the whole argument still rest on a trait nothing has ever corroborated — which is not a failure of diligence but of what a register pointing at a file can express.

**`bin/wiki-traits`**** computes the missing number, and ****`assess`**** is the interface:**

bin/wiki-traits assess ti_dominance    # before leaning on it as a mechanism

bin/wiki-traits map                    # the whole table, loud cells first

It reports two axes that are **never added together**:

- **Support** — the trait as a directional prediction against Dan's own behavioural output: sent messages against a within-medium control of received ones, plus tweets and his own turns in AI transcripts, ranked within register because no control exists for those.

- **Reach** — how much of the wiki already leans on the trait. **Reach is not evidence and never becomes evidence.** Those pages were written by agents that had read `wiki/mind/profile/`, so reach measures how often the writing process reached for a vocabulary. Of 483 entries, 122 carry personality vocabulary and 38 of 61 synthesis pages do.

**What the cell obliges, and this is the binding part:**

| **Cell** | **What a synthesis may do** |
| --- | --- |
| `earned` | Cite as mechanism. Measured, replicated, already reasoned from. |
| `UNDERUSED` | Cite as mechanism — and ask why this page was not already using it. |
| `THIN LOAD` | Cite with the register named; a single-medium result may be the medium. |
| `UNSUPPORTED LOAD` | **Not as a load-bearing mechanism.** State the silence on any page that invokes it. |
| `UNREVIEWED LOAD` | **As testimony, never as measurement.** No proxy has had its matches read. |
| `NO INSTRUMENT / LOAD` | **As testimony, and say so on the page.** Every proxy was read and found to catch something else. |
| `CONTRADICTED LOAD` | **Stop.** Re-read every page in the reach set before citing the trait again. |

**Silence is not falsification.** This is inherited from `bin/psychometrics` and it governs every row: three of four core axioms tested lexically were invisible, *time = countdown* the clearest negative. A trait can be real and leave no lexical trace, because people do not narrate their own architecture in text messages. So `silent` constrains how much weight a conclusion may place on a trait and says nothing about whether the trait is true. Only `INVERTED` is evidence against a score, and an unreviewed proxy is not permitted to produce one — see the tool's `PROXY_REVIEW` register for why that cap is load-bearing.

**Three bands mean three different things and are never interchangeable.** `silent` — an instrument ran and the corpus carried nothing. `unreviewed` — no trustworthy instrument ran, because no proxy for the trait has had its matches read. `no instrument` — every proxy built for it was read and found to measure something else. Only the first is a finding about the corpus; the other two are findings about the instrument, and a synthesis that treats them as silence is claiming a measurement that never happened.

**There is no confidence percentage, and one must never be added.** A percentage needs a denominator of things that could have disconfirmed, and silence is not one of them. Bands, and the counts under them.

### What the pass actually requires

1. **Name the mechanism, not just the pattern.** If a measured value explains the behaviour the page documents, the page cites it. A rule with a psychometric or cognitive-function mechanism under it is a different and better object than the same rule stated from behaviour alone: it predicts in domains the corpus has not sampled yet.

1. **Let the registers argue back.** The pass is allowed to *change the conclusion*, narrow its scope, or kill it. A rule that survives being read against the profile layer is stronger; a rule that only survives by not looking is not a finding.

1. **Check the register's own provenance before leaning on it.** Several carry live contradictions — `enneagram-5w4` holds a `CONTRADICTION` block recording that the only first-person self-typing in the record is **5w6sx RLOEI, not the 5w4 the page is named for**, and `the-commissioned-self` establishes that most of this layer is a commissioned instrument reading rather than something Dan lives out loud. A synthesis leaning on the sx/sp stack inherits that dispute and **must carry it forward**, not launder it into settled fact by citing the page without its caveat.

1. **Record the result on the page.** Which registers moved it, which were checked and left it standing, which the corpus cannot answer. The third category is a Gaps entry and often the most valuable thing the pass produces.

1. **Never let the pass become a citation ritual.** Adding `synthesizes: wiki/mind/profile/intp` without an argument that uses it is worse than omitting it, because it makes an unexamined page look examined.

### The anti-pattern this replaces

**The floating rule.** A conclusion true of its members, elegantly stated, falsifiable, wired correctly — and unattached to any fact about the person it claims to describe. It survives every mechanical gate in this repository. It is still the most common way a synthesis page is wrong, because a rule with no constitution under it cannot tell you which of its predictions to trust, and it will be cited as though it can.

### When to climb

Climb when the queue shows a cluster that has been sitting there through two or more ingests — that is the signal that the pattern is stable rather than an artifact of one source. Climb immediately, without the queue, when an ingest makes you think "this is the third time I've seen this shape."

Do not climb to raise a number. Three thin pages do not become one good page by being stacked; they become one thin page with a longer preamble. If the members are underwritten, the correct move is to deepen a member, not to build above it.

## Anti-patterns

- **The umbrella page.** A T2 page whose thesis is that its members share a topic. Topics are what indexes are for.

- **The laundered summary.** Restating member pages at lower resolution and calling the loss of detail "synthesis."

- **The unfalsifiable rule.** "Dan's relationships are shaped by attachment." True of everything, predicts nothing.

- **Silent staleness.** Bumping `date_modified` to clear a `wiki-climb check` warning without re-reading the premise. This is the one prohibited move.

- **Climbing on sand.** Building T3 doctrine on T2 pages that are themselves thin. Altitude does not add rigor; it inherits whatever the floor had.

- **The floating rule.** A conclusion that is true of its members, elegantly stated and correctly wired, but never checked against the cognitive stack, the measured profile, the history, the material circumstances or the ideology of the person it claims to describe. It passes every mechanical gate here and is still about the corpus's sampling rather than about Dan. See "The constitution pass" — this is the anti-pattern it exists to stop.

- **The write-only synthesis.** A T2/T3 page that is correct, well-argued, and wired to nothing — or wired with inverse claims so generic that a reader on the member page learns nothing. The finding exists but cannot be found from below, which is where readers actually arrive. This is the most common way good synthesis work fails to compound.

## Tooling

- `bin/wiki-climb check` — validates `synthesizes:` (resolution, no raw paths, no self-reference) and reports stale pages whose premises have moved since they were last touched. Exit 1 on errors. **Run alongside ****`bin/wiki-lint`**** and ****`bin/wiki-connect check`**** before every commit.**

- `bin/wiki-climb audit` — the altitude report: tier distribution, which domains are all-ground-no-junction, the deepest synthesis chains, and the pages carrying the most dependents (change those carefully).

- `bin/wiki-climb candidates [N]` — regenerates `synthesis-queue.md` from edge density, domain span, tag overlap and shared raw sources, scoring cross-domain clusters higher because cross-domain tissue is the scarce resource.
