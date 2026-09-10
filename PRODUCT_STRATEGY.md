# PRODUCT_STRATEGY — can this be sold, and as what

**Status:** analysis, not doctrine. This file governs nothing. It is not part of the governing set in `STRATEGY.md`, it does not bind any operation in `CLAUDE.md`, and no page may cite it as a source. It is a commercial assessment of the repository written against the repository, dated 2026-09-06.

## The short answer

**Consultancy, and the packaged thing you give away.**

Not because the harness can't be built — it mostly already is, and that is precisely the problem. The machinery is the least defensible layer in the whole stack, and shipping it as the product means charging for the one part a competent person can rebuild in a fortnight with the same agent you used.

The defensible assets are, in order:

1. **The instruction corpus** — 30,073 words of governing spec that turn a general agent into something that produces this instead of slop.

1. **The failure catalogue** — the traps that each produced a wrong number first, and are now written down.

1. **You**, running the loop with a person who answers questions.

Only the first is packageable, and it is worth more as an open artifact than as a licence. Give the machinery away. Sell the build.

There is a fourth asset that is currently unusable, and getting it usable is the gating task for either path. That is §5.

## 1. What is actually here, measured

Numbers from the tree as of 2026-09-06, not from the README.

|  |  |
| --- | --- |
| Wiki pages | 503 (9.4 MB) |
| Raw corpus | 685 MB, 3,370 files |
| Tooling | 37 commands, 20,749 lines of stdlib Python |
| Tests | 450 |
| Governing spec | 30,073 words across 7 files (`CLAUDE.md` alone: 11,728) |
| Build window | 2026-08-21 → 2026-09-05, 231 commits |
| Knowledge split | 81 `earned` · 182 `mixed` · 27 `derived` |
| Outstanding | 140 obligations, 128 of them stale premises |

Two of those rows matter more than the rest.

**Sixteen days.** Whatever else is true, the build velocity is real, and it is the single most saleable fact in this document. A client engagement measured in weeks is a product. One measured in years is a hobby you are trying to invoice.

**128 stale premises.** The system accumulates maintenance debt at a rate that tracks its own output. This is not a defect — it is what an honest dependency graph looks like when the floor keeps moving — but it is a running cost, and any pricing model has to carry it. A brain you stop feeding does not sit still; it goes stale in a way the gates can see and the owner cannot.

### How person-specific is the machinery?

Less than you would expect. Across 25 of the 37 tools there are roughly 110 occurrences of a Dan-specific string, and exactly **six hardcoded ****`raw/`**** corpus paths**. The gates (`wiki-lint`, `wiki-connect`, `wiki-climb`, `wiki-plain`, `wiki-lessons`, `wiki-history`) are generic already. The ledgers (`intake`, `testimony`, `wiki-skills`) are schema-driven and generic already.

Porting `bin/` to a second person is a week, maybe two.

**Which is the argument against selling it.** If it is a week for you, it is a week for anyone who reads the public repo. The tooling is not a moat. It is a business card.

## 2. Where the ChatGPT read is right

Three things in that outline are correct and worth keeping:

- **Person-centric ontology, not topic-centric.** Right, and the tree proves it: 175 people pages against 98 interests pages. The unit of organisation is a life, not a filing cabinet.

- **Synthesis as the layer, not retrieval.** Right, and it is enforced rather than aspired to — `SYNTHESIS_SPEC.md`, the `synthesizes:` chain, the stale-premise gate. 81 pages are `knowledge: earned`, meaning they cannot be regenerated from `raw/`. That is the part a RAG cannot reproduce, and it is 16% of the corpus.

- **Provenance as the sacred property.** Right, and further along than the outline knows. Beyond `sources:` on 491 of 503 pages, there is `RETRACTED.md` (a claim shown false cannot silently reappear), `wiki-history` (a page cannot claim a date its own commit log does not support), and `wiki-plain audit` (a number in a plain-language twin that appears nowhere in the source page is a gate failure). Three independent mechanisms against the model feeding its own output back in as evidence.

## 3. Where it is wrong

### 3.1 It never mentions the input problem, which is the actual binding constraint

The entire outline is an architecture comparison. Architecture is not what stops this being a product. **Acquisition is.**

- **265 of 503 pages — 53% — depend on the message corpus.** That corpus is 174 MB of iMessage exports pulled off macOS `chat.db` with full disk access, across at least six overlapping dumps that *disagree with each other*. The lexicon work measured the collision: 36,716 shared rows at +4h and 23,624 at +5h, because one export is Eastern local and another is UTC. A first run reported 188,445 sent messages against a true 106,629. That is not an extraction wizard problem. That is forensics, per customer, every time.

- **166 pages — 33% — rest on ****`CONTEXT_CORE_EXPANDED.md`**, a 2,750-word hand-compiled seed whose own header credits it to CATO_BOOTLOADER, MAX_PRIME, OPERATING_MANUAL, a stylometric analysis and a full Twitter analysis 2009–2024. **A third of the corpus stands on a document that was itself the output of prior work that predates this repo entirely.** A new customer starts with nothing there and no way to buy it.

- The rest of the acquisition surface — a Facebook archive, Google Location History, a YouTube watch history back to 2010, Gemini and ChatGPT exports, Ancestry, a Twitter archive — is each a separate flow with its own request wait, its own format, and its own silent trap.

You can automate the *fetching*. You cannot automate the reconciliation, and the reconciliation is where the numbers go wrong. Any packaged product ships a wizard that pulls six exports and then produces a corpus nobody has checked. It will be confidently wrong at scale, and the confident wrongness is exactly the failure this repo has spent thirty thousand words learning to prevent.

### 3.2 The scorecard is scoring the wrong axis

"Personality modeling ★★★★★ potential" and "self-model evolution ★★★★★ potential" are not capabilities. They are a plan. The competitors' ★★ is a shipped ★★. Scoring your intention against their implementation and concluding you lead is the exact motivated reasoning the wiki's own constitution pass exists to catch. Run it on the outline: it fails.

### 3.3 The confidence bar chart is a fabricated number, and this repo already knows it

The outline's mock-up:

TYPE 5 — CONFIDENCE: 87%

Supporting evidence

Education   ████████████

Career      █████████

**Do not build this.** `bin/psychometrics` already exists, already runs trait-hypothesis-against-corpus-evidence, and already established — the hard way — why that display would be a lie. Its own docstring:

failure to corroborate is not falsification. A trait can be real and leave no lexical trace, because people do not narrate their own architecture in text messages.

Four core axioms were tested lexically against 106,629 sent messages, controlled against 110,944 received from 503 other handles. **Three were invisible.** The clearest negative was *time = countdown* — a trait the corpus is confident about and the language does not carry at all.

So the evidence is asymmetric and the display has to be too: a high ratio is positive evidence; a low ratio is corpus silence; only an *inversion* — a low-scored facet showing markedly elevated language — is evidence against. There is no denominator that makes 87% meaningful, and rendering one produces the most dangerous artifact this system can emit: a fabricated quantity that reads as proof. That is a gate failure in `bin/wiki-plain audit` for the same reason.

**The asymmetry is the differentiator, not a limitation to design around.** Everybody else in that competitive survey will ship the bar chart, because the bar chart demos well. Being the only one that says "the corpus does not carry this" is the whole credibility position. It costs you the dashboard. Take the trade.

## 4. Your three value claims, ranked

You named three. They are not equal and the ranking is not the one you gave.

### First: no re-typing context. This is the only one with a measurable before/after.

You buried it as the second point. It is the product.

Evidence it is real, from inside the repo: `CONTEXT_CORE_EXPANDED.md` describes itself as *"the single document loaded every session, until a retrieval layer exists."* You already built the crude version of this product and have been running it for months. **The wiki is the retrieval layer that document says is missing.** That is not a pitch, it is a deployment already in progress with a predecessor to measure against.

And it is the only claim here you can *demonstrate under controlled conditions*: same hard question, same model, with and without the wiki. Record both. That comparison is the sales asset, and no competitor in the survey can run it, because none of them has a populated specimen to run it on.

### Second: the destination you can read.

Real, and correctly identified as the thing that separates this from an MCP server. A skill you install is a capability; a place you go is a possession. People pay for possessions.

But be honest about what it competes with, because it isn't Obsidian. It is the felt experience of being *understood*, which currently has a free competitor that is very good at faking it and improving fast. The wiki wins that comparison on one axis only: **every sentence traces to evidence, and the system tells you when it doesn't know.** Lead with the falsifiers.

### Third: personality profiles as the next big step.

Right instinct, wrong direction — see §6.

### The fourth one you didn't name, which may be the best of them

`bin/wiki-testimony` currently reports: **22 testimonies, 14 settled, veracity 57/100.**

That is the system scoring its own owner's first-person accuracy against primary sources, and finding him right slightly more than half the time.

Nothing else in that competitive survey does this, and I doubt anything else *will*, because it requires building a mechanism whose whole purpose is to tell the paying customer they misremember things. It is the single most credible artifact in the repository — a personal-AI system that cannot be flattered by its subject — and it is also the most commercially frightening, which is why it is a moat. Anyone can promise an evidence-backed model. This is a system that publishes its own error rate about the person paying for it.

Two caveats that have to travel with it: n=14 is not a rate yet, and the page carries its own sample-bias disclosure because the standing moratorium filters the record. Both are correct handling and both must survive into any pitch.

## 5. The specimen problem — the gating issue for either path

The strongest idea in the ChatGPT outline is **"don't take our word for it, read the brain."** A live populated specimen beats any landing page.

**You cannot show this one to a prospect.** Not for taste reasons. For structural ones.

- 175 people pages, **128 of them slugged firstname-lastname** — real, findable people, on a public GitHub repo and a public portal.

- **Three named third-party psychological assessments**: `ally-lubin-cognitive-profile`, `suzanne-frank-personality-assessment`, `annie-ulmer-personality-assessment`. Living people, assessed by an AI, under their own names, in public, without consent.

- `wiki/people/annie-ulmer.md` is **23,763 words** about a person the standing directive in `CLAUDE.md` describes as being *in apparent danger* — and the moratorium correctly stops the record advancing while leaving 23,763 published words in place, because the operator asked for a stop, not a redaction.

- `intake/events.jsonl` publishes dated controlled-substance consumption, tracked, permanently, by explicit decision.

Every one of those is a defensible choice for a personal project. Every one of them is disqualifying for a sales asset, and the reason is not squeamishness:

**A prospect who reads the specimen learns exactly one thing: this system produces a public dossier on everyone you have ever texted, including psychological assessments they never agreed to, and you will not be able to take it back.**

The specimen does not sell the product. It *is* the objection, rendered at maximum fidelity. And it is the objection that kills the consumer version outright — you would be handing ordinary people a machine that builds non-consensual profiles of their families, and the first time one surfaces in a divorce filing, that is the whole story about the company.

### What to build instead

**A second specimen, on a public figure with a large public corpus.**

Decades of published writing, interviews, transcripts, public record. No consent problem, no third-party problem, corpus is free and already digital, and — the part that matters — **a prospect can independently check the synthesis against material they already know.** "Here is a rule about this person that no single source states, and here is the evidence chain, and you have read half the sources yourself" is a far stronger demonstration than a stranger's private life.

It also proves the thing the private specimen cannot: that the findings are produced by the method rather than by the intimacy of the data.

Then keep yours private. Make the repo private, in that order — private first, verify, then decide what else changes, exactly as `CLAUDE.md` already specifies for the ledgers. It stays the R&D environment and the thing you demo under NDA to a serious buyer. It stops being the shop window.

## 6. Personality: fewer instruments, tested harder

`wiki/mind/profile/` already carries Enneagram 5w4, INTP, Big Five, Socionics, and a deviance mapping. That is four overlapping instruments measuring substantially the same constructs, plus one that is not psychometrically respectable in a room with a skeptic.

**Adding a fifth framework is the move that makes this look like astrology stacking.** More frameworks agreeing with each other is not convergent validity; it is the same self-report laundered four ways. `bin/psychometrics` says so already: every one of those facet scores is an instrument Dan filled in, sitting next to 217,573 messages of measured behaviour that nobody had turned into anything testable.

The move that makes personality the signature is the opposite one:

1. **Promote ****`bin/psychometrics`**** from a tool to the front door.** The page a visitor lands on should be the instrument-versus-corpus comparison, not the profile. What the self-report claims, what the behaviour shows, where they diverge, and — loudly — where the corpus is silent.

1. **Report the asymmetry honestly** (§3.3). Corroborated / silent / inverted. Three states, never a percentage.

1. **Make the divergences the content.** A trait the person claims and the corpus contradicts is the most interesting object this system can produce, and it is the one thing no self-report instrument on earth can generate. Pair it with the testimony ledger's 57/100 and you have a coherent thesis: *this system's distinguishing feature is that it disagrees with its subject, with receipts.*

1. **Extend the within-medium control.** The Twitter archive is a third first-party register — broadcast rather than addressed — and per the handoff it is unmined for this. It tests whether the register split is about audience or medium. That is a real psychometric finding, cheap, and already queued.

That is the personality layer worth cranking up. Not more labels with better graphics.

## 7. Which path

### Not: consumer product

Killed by three independent constraints, any one of which is sufficient.

- **Acquisition** (§3.1) — most people cannot get the corpus, and the ones who can will get a corpus nobody reconciled.

- **Consent** (§5) — a mass-market machine that profiles third parties by name is a liability event waiting for its first news cycle.

- **Corpus poverty** — the median person's message history is thin, recent, and mostly logistics. Feed this system a weak corpus and it produces confident pattern-matching over noise, which is worse than nothing and indistinguishable from the astrology apps it would be shelved next to.

### Yes: consultancy, narrow customer, weeks-long engagement

The customer is not "someone who wants a second brain." It is someone for whom a model of themselves has **instrumental** value:

- **Founders and operators** who want agents that can act with their judgment rather than their preferences — the buyer here is delegation, not introspection.

- **Writers and public figures** with a large existing corpus and a commercial reason to model voice and position.

- **Estate, legacy and biography work** — people with money, an archive, and a deadline. This is the segment where the third-party problem is smallest and the willingness to pay is highest.

- **Litigation and investigation support**, where a longitudinal evidence-chained model of one person's documented behaviour has an obvious price and an obvious buyer.

All four have the corpus, can pay, and have a reason that survives the question "why not just use ChatGPT memory."

Structure it as a fixed-scope build: acquisition and reconciliation, corpus ingest to the standard in `EXTRACTION_SPEC.md`, the synthesis climb, the personality instrument pass, handover with the gates running. Sixteen days is your evidence that the scope is real. Price the build, then price maintenance separately and honestly — 128 stale premises is what "unmaintained" looks like after two weeks.

### And: give the machinery away

Ship the governing set and `bin/` as an open agent skill pack. Not as a loss-leader gesture — because **it is not defensible and pretending otherwise costs you the distribution.**

What that buys:

- The spec becomes the reference standard for the category while the category is still being named. `EXTRACTION_SPEC.md`, `SYNTHESIS_SPEC.md` and the constitution pass are genuinely better thought out than anything in that competitive survey, and being the document everyone cites is a stronger position than being the vendor everyone forgot.

- Every person who tries it and stalls is a qualified lead who has already discovered the hard part is not the software. That is the entire consultancy pipeline, self-selecting.

- It costs you nothing you could have held. A week of reading reproduces it.

The line is: **the method is open, the build is the service, and the specimen is the proof.**

## 8. Next thirty days, in order

1. **Make ****`wiki-brain`**** private.** Private first, verify, then decide anything else — the order `CLAUDE.md` already specifies for the ledgers, applied to the whole repo. Everything below assumes this is done. Git history cannot be un-published, so this reduces future exposure, not past exposure; the third-party pages that are already indexed are a separate decision and it is yours, not mine.

1. **Run the context A/B and record it.** One genuinely hard question about a situation the corpus covers. Same model, cold versus wiki-loaded. This is the cheapest high-value asset available and it takes an afternoon.

1. **Pick the public-figure specimen and scope it.** Someone with a deep public corpus and a life with actual shape. Budget it against the 16-day precedent. This is the demo, and it is also the second data point on whether the method generalises — which you currently have zero evidence for.

1. **Rebuild the personality front door** per §6. `bin/psychometrics` output as a page, three-state reporting, divergences foregrounded, Twitter register added as the third control.

1. **Write the extraction guide as an open artifact.** Not a wizard — a documented reconciliation procedure with the traps in it, UTC collision included. It is genuinely useful, it is the best possible advertisement for knowing what you are doing, and it is the piece of the open pack that will actually get read.

1. **Only then** decide between packaging and consulting, with two specimens and a measured before/after instead of one specimen and an argument.

## What would change my mind

- **If the public-figure specimen fails** — if the synthesis layer turns out to need the intimacy of private data and produces nothing interesting over public record — then the specimen strategy dies, the demo problem becomes unsolvable, and this is a consultancy with no shop window. That is the load-bearing assumption and it is currently untested.

- **If acquisition tooling gets dramatically better** — a reliable cross-platform message export with reconciliation built in would remove the largest barrier and make the packaged path viable. Worth watching; not worth waiting for.

- **If the maintenance cost turns out to be lower than 128 stale premises suggests** — if most of that debt is cosmetic rather than substantive, the ongoing-service economics improve considerably. Auditable, and worth auditing before anyone quotes a retainer.
