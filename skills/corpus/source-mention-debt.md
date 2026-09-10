status: active scope: corpus triggers:

- writing a page from a large corpus that names people, works, places or events

- picking up a corpus a previous pass already mined

- adding a typed edge to a page assembled from a source

- asked whether a source has been fully worked, or what a mined corpus still owes sources:

- wiki/interests/concert-record/index.md — "The twitter cross-check"

- wiki/people/katie-fletcher.md — "The primary record — eleven days in August 2013"

- wiki/health/chemical-architecture.md — "Nicotine: eighteen years, five delivery systems"

- wiki/interests/music/aliases/sloppp.md — "The twitter archive roughly triples the documented 2013 output"

- bin/wiki-crosslink

- tests/test_wiki_crosslink.py validated: 2026-09-04 supersedes: []

# A source's debt to the pages it did not get written onto is invisible from both ends

## Instruction

1. **After writing a page from a corpus, run ****`bin/wiki-crosslink scan <page>`** before considering the source worked. It reads the corpora the page's own `sources:` name, inside the page's own date range, and lists entities that have pages the page does not link.

1. **Read the rows it prints. Every one.** Roughly every single-token name match is a false positive — this pass got Rick Santorum under "Rick", Tom Cruise under "Tom", Jack Ü under "Jack" and slim jims under "slim". The tool emits candidates; the edge comes from reading.

1. **Go at the target page's claims about itself first.** Sort the candidates by whether the target asserts something checkable about its own completeness or limits. That is where the value is concentrated and it is not close.

1. **Write the edge even when there is no finding.** A mention is an obligation on its own: the target page's evidence base is short and it has no way to discover that. The claim states what the target did not have, not that a mention exists.

1. **Run ****`bin/wiki-crosslink reciprocal`**** before committing.** An edge whose target never got told is half an edge. An edge into a generated page is not debt and the tool already knows the list.

1. **Say what did not survive the wider match.** A pattern found on the first handful of pairs is a hypothesis; extend the match before writing it, and when it dissolves, put the dissolution on the page.

## Why

**This is the only obligation in the repository with no symptom.** A red gate announces itself, a parked `sage/` question sits at priority 1 in `bin/wiki-work`, a stale premise fires a warning. A source that named forty things and got linked to three is indistinguishable — from the page, from `WORK.md`, from `bin/wiki-lint` — from a source that named three. The page reads as finished because it *is* finished. What is unfinished is on pages nobody is looking at, and those pages cannot report a gap they have no mechanism to detect.

The measured case, 2026-09-04. Nineteen `wiki/self/twitter/` year pages had been written across two sessions by reading every tweet in every year, to a high standard, carrying 130 typed edges. A scan of the same archive against the same pages found the pages had never been told about:

| **Page** | **What it was missing** | **What the page said about itself** |
| --- | --- | --- |
| `interests/concert-record/index` | three Orlando concerts, four corroborations | *"the master table below is the complete record"* |
| `people/katie-fletcher` | six dated posts, a handle, a Vine from inside the event it narrates | *"everything known arrives through Dan's later AI-session narration"* |
| `health/chemical-architecture` | eighteen years of dated nicotine evidence and an onset year | the row *"has no ledger entries at all and remains description"* |
| `interests/music/aliases/sloppp` | 20 more 2013 releases; 16 in one month against a table showing 1 | discography *"reconstructed from posted links"* |

**Every one of those pages stated its own limit, and the limit was wrong.** A page that says what it does not know is telling you where to point the next source — and it will keep saying it, indefinitely, because nothing else will ever check.

The 39 one-way edges found the same day are the same defect from the other side: the finding was written where it was discovered and the page it was about never heard.

## Validation

`bin/wiki-crosslink scan <page>` on a page you have just finished. If it names targets you did not consider, the source was not worked out. `bin/wiki-crosslink reciprocal <prefix>` must reach 0 for the tree you touched; `bin/wiki-crosslink check` prints the repository-wide total and always exits 0 by design, because a gate that blocked unrelated commits on a one-way edge would acquire an escape hatch and stop being a gate.

## Known limits

**The scan can only look for names somebody already wrote a page for.** Entities with no page are exactly the ones it cannot see, and finding those is `EXTRACTION_SPEC.md` move 3, done by reading. The two moves are complementary and neither substitutes for the other.

**It finds no conceptual link at all.** Everything above is string matching over proper nouns. A tweet that is evidence for a synthesis without naming anything — which is most of the interesting ones — is invisible to it, and the operator's original ask was explicitly for those. This skill covers the mechanical half only; the conceptual half is a reading job and always will be.

**It only reads corpora it has a reader for.** `CORPORA` in `bin/wiki-crosslink` holds three entries as of 2026-09-04 — the twitter archive and both message exports, the latter two by importing `bin/mine-messages`' reader rather than writing a second one, which is the only way to inherit that file's three traps instead of its interface. The Facebook export, the YouTube history, the Gemini activity, the concert table and the favorites list are all still unread, and `wiki/interests/music/overview` carries absence claims derived from the message corpus that have never been checked either way.

**The right scope depends on the corpus.** `--against` reads the rows naming a page and asks what else they name — correct for a broadcast archive, wrong for messages, where a five-to-fifteen-word row that names one person almost never names a second. It returned **0 candidates across 7 pages** on the message dump. `scan --conversation` scopes by counterparty instead, joining a page's infobox `handles:` to the corpus's handle field: 30 people pages resolve, 41,349 rows, 51 candidates. `bin/wiki-crosslink handles` is the coverage view — and **138 people pages carry no ****`handles:`**** at all**, which is the message corpus's version of the alias gap.

**A page name that is also ordinary English produces confident garbage.** `say anything` returns 134 rows in the message dump and **none is the band**; `the office` returns 77 and **none is the show**. Both are reported `high` because the rule is "more than one token". They are now flagged with the count marked not-evidence — flagged rather than demoted, because some really are the band. This is the one class of the judgment failure that is mechanically catchable; the rest still is not.

**A string two pages both claim is evidence for neither.** `@alexisarmel` is in one person's `aliases:` and in another's infobox `handles:`; 85 rows about the first came back as 101 mentions of the second. `scan` now marks such candidates `contested`, and a contested candidate is not a candidate until the row is read.

**The moratorium binds the candidate column too.** It was enforced on the page being scanned and not on the pages being offered as targets, which is the same worklist. Fixed and pinned in `tests/test_wiki_crosslink.py`.
