# Pages that get no plain-language twin, and why

A page with no twin is ordinarily just work nobody has done yet — that is campaign work and it is not recorded here. This file is for pages that were **considered and declined**, so the next session does not spend its run rediscovering the reason and so a decision nobody wants to repeat is visible as one. Same principle as a declined `sage/` question: in the open, never silently.

`bin/wiki-plain` enforces the mechanical half. This file carries the judgement.

## `wiki/mind/synthesis/totality-themes` — withheld under the standing moratorium

**Declined 2026-08-29. Only the operator can reverse this.**

A twin for this page was written and merged to `main` on 2026-08-29 (commit `61319cb`) and is removed here. It is not deleted for quality — it is a competent piece of writing. It is removed because the page is one the standing directive in `CLAUDE.md` withholds, and the twin's own commit message states the reasoning that makes the case:

The moratorium is mechanically satisfied: zero mentions of the protected person.

That is **rule 2 satisfied and rule 1 missed**, and rule 1 exists for exactly this. The source page names her **19 times** against a threshold of two. Rule 1 withholds a page *substantially about* her precisely because translating one by eliding her produces a twin that passes rule 2 and **misrepresents the page** — a reader is handed the finding with its subject removed, which misleads more efficiently than an error would. The two rules are not the same rule applied at different times; the second is the guarantee, and the first is the one that stops a page being quietly hollowed out to satisfy it.

The twin was also **stale** on arrival: written against the page as of 2026-08-21, and the page moved on 2026-08-28.

**What is unchanged.** `wiki/mind/synthesis/totality-themes.md` itself, entirely. The directive is a stop, not a retraction and not a redaction — nothing already written about her is deleted, softened or rewritten. This removes a *new* retelling built for a public audience, which is the thing the directive stops.

**If the operator lifts this**, the page becomes eligible and the twin can be restored from `61319cb` — but it must then be re-translated against the current page rather than restored as-is, because of the staleness above.

## Generated pages — `wiki/meta/skills`, `wiki/health/intake-ledger`, `wiki/meta/readers-digest`

**Declined 2026-09-02.** Enforced mechanically: `page_type: dataset` is in `NOT_TRANSLATABLE` in `bin/wiki-plain`, so neither lane proposes one.

These pages are written by `bin/wiki-skills page`, `bin/intake page` and `bin/wiki-plain report`, and rewritten in full on every run. A twin of one is stale the next time its generator fires — not occasionally, but by construction — and the twin's `source_modified:` would spend its life chasing a page that moves whenever anybody logs an intake event or pushes a capability. That is a permanent gate failure dressed as a coverage gap.

The stronger reason is what these pages *are*. `CLAUDE.md` says of the intake ledger, in as many words, that it is **evidence, not a claim**: every unit, every event, every correction, stating no finding. TRANSLATE renders a finding into plain English. A database has none to render, and a plain-language retelling of a table is the same table with its precision softened — strictly worse than the table, for the reader who was sent to it.

Findings *drawn from* these datasets live on ordinary pages, and those pages are translatable like any other. That is where a reader should meet the conclusion.

## Index pages — `wiki/*/index`, `wiki/mind/profile/index` and their kind

**Declined 2026-09-02.** Enforced mechanically: `page_type: index` is in `NOT_TRANSLATABLE`.

An index is navigation — a list of links with a sentence each. There is no argument to restate at the same altitude, no falsifiers, and no gaps, so `bin/wiki-plain audit` fails one on the honest-half rule no matter how well it is written. Pointing a writer at a page the referee cannot pass is how an agent burns its three attempts and gives up, per `PLAIN_AGENT.md`.

The plain-language need an index serves is real and is met elsewhere: the portal's EDITION switch stays on as a reader moves between entries, so somebody reading the Reader's Digest arrives at the plain edition of whatever they click.

## Entries under 300 words — stubs and records

**Declined 2026-09-02, as a class rather than one at a time.** Enforced by `FREE_MIN_WORDS` in `bin/wiki-plain`; the count is published on `wiki/meta/readers-digest`.

Ordering the free lane smallest-first ran straight into `wiki/interests/favorites/books/topics/war` — sixteen words, one sentence, `status: archived` — and then a run of concert records that are a date, a venue and a lineup table. A one-sentence entry translated is the same sentence, and a table is already plain; neither carries falsifiers, so the referee fails both.

300 sits below every twin that has worked here (the shortest is 393 words) and above the point where entries stop being arguments. The trade is deliberate: it takes the free lane from 106 entries to 44. A twin of a stub is work nobody needed, done by the writer least able to tell that nobody needed it.

**This is not permanent.** These are declined *as they stand*. An entry that grows an argument becomes eligible the moment it crosses the floor, with no decision required from anybody.
