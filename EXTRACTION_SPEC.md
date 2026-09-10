# EXTRACTION SPEC — how deep to go into a source, and why deeper is the whole game

Binding alongside `STRATEGY.md` (intent), `STYLE_GUIDE.md` (page format), `CONNECTIONS_SPEC.md` (edges) and `SYNTHESIS_SPEC.md` (altitude). Those four govern what you write. **This one governs what you find before you write.**

It exists because the repository's limiting factor has changed. For the first year the constraint was coverage — there were not enough pages. That is no longer true: there are 438. The constraint now is **extraction depth**. Sources that have been "ingested" turn out, on a second reading, to contain three times what was taken from them the first time, and the findings left behind are not marginal — they are the ones that reorganise pages.

## The argument: depth of mining and length of entries are one requirement

The product of this system is not the facts. It is the **patterns found across facts that no single source states** (`STRATEGY.md`, "The core loop"). That has a mechanical consequence most passes miss:

A pattern can only be found among details that were written down. Every detail dropped at extraction is a connection that can never be made, by anyone, later — because the synthesis layer reasons from `wiki/`, not from `raw/`.

This is why "every trivial and potentially meaningless detail gets an entry" is not hoarding and not pedantry. A detail's value is not its own significance; it is the **surface area** it adds for the next climb to land on. The detail that looks meaningless in isolation is exactly the one that turns out to be the third instance of a shape — and it can only do that if it is on a page.

Worked cases, all of them details that looked like nothing at the moment of extraction:

- A street name in a stylised AI transcript — *"this house is on an adjacent lot to the 155 virginia avenue house"* — sat unread for months. It collapses a literary coincidence, a fifty-seven-year family seat and the geography that produced the defining relationship of Dan's adult life into one strip of ground. Nothing about it looked load-bearing.

- A `PLAC` line in a genealogy export moved a house's documented history back a decade and revealed the family's arrival there was a return from Florida — which then rhymed with the *other* side of the tree returning from Seattle within two years.

- A private word used unglossed in a 2011 chat about an electricity bill turned out to be the password on the last message of a relationship in 2025.

- A four-word aside about a grandmother, chased into the genealogy, closed two standing gaps and corrected the family tree.

None of those was the point of the source it came from. All of them were findable in the first pass. The reason they were not found is that the pass stopped when it had what it came for.

**So: length is not a style preference, and depth is not diligence theatre. They are the same instruction, and the instruction is that the corpus's analytical ceiling is set by how much got written down.**

## What "read" means here

A source is not read when you have searched it. It is read when it is **exhausted** — when a second careful pass by a fresh reader would find nothing material you did not.

That standard is high on purpose, and it is achievable, because `raw/` is finite and immutable. Budget accordingly: reading one source to exhaustion beats skimming five. The pass that produces four findings from one file has done more for the wiki than the pass that produces one finding from four, because the four findings can be read against each other.

Concretely, a source is exhausted when you can answer all of these:

1. What does it say that no other source in the corpus says?

1. What does it say that **contradicts** something already on a page?

1. Which proper nouns does it contain that have no entry, and did you chase each one?

1. Which numbers does it contain, and did you re-derive them rather than copy them?

1. What is conspicuously **absent** from it that you expected?

1. What in it looked mundane, and did you write that down anyway?

If any answer is "I did not check," the source is not read. Say so in the log rather than claiming the ingest.

## The eight moves

These are the operations that produce depth. They are listed in the order they tend to pay off, not the order you must run them.

### 1. Sweep wide before reading narrow

Never start from a page's declared `sources:` list. That list records what a previous pass happened to open, not what exists — and on every page examined in the 2026-08-08 rewrite pass it was incomplete.

grep -ril "<subject>" raw/ | head -40     # and every alias, handle, nickname,

# maiden name, misspelling

Read what comes back, including the files you do not expect to be relevant. The Facebook address book is not where you look for a novelist, and the genealogy export is not where you look for a house's occupancy — which is exactly why those findings were still sitting there.

### 2. Read whole records, never matching lines

`grep` gives you the hit. The hit is almost never the finding; the finding is in the twenty messages around it, which supply the date, the interlocutor, the tone, and the reason it was said. A page built from matching lines reads like a concordance and misses the story it is standing in.

This has a hard mechanical version too: several sources in `raw/` are multi-line-per-record, so line-based tools give you a *fragment* and call it a message. See "Traps by source type" below.

### 3. Chase every proper noun outward

Each name, street, business, band, book, handle and place in a source is a lead into the rest of the corpus. The capture or the transcript is the **prompt, not the boundary**.

The highest-value findings in recent passes all came from this move: a brother's name into an obituary and a message thread, a street name into a genealogy export, a nickname into two contact exports, a book title into a reading log. Budget explicit time for it — it is where the delta lives, and it is the move that gets skipped when a pass is running long.

Any proper noun with no entry is either a new page or a line in `BACKLOG.md`. Nothing gets silently dropped.

### 4. Re-derive every number

Counts, date ranges, direction splits, ratios and spans are the claims the operator checks, and they are the claims most often wrong. Copying a number forward from an existing page launders an error into a second place.

Re-derive with the right instrument, not with `grep -c`. Writing this spec, a recount caught a per-day message figure in a page written the same day — eyeballed as 22, actually 28. The instrument catches you; the eyeball does not.

And **read your matches before believing your counts.** A lexical pattern scored age self-reference at 3.82× baseline and nearly became a published finding about how Dan experiences time; it was catching *"I'm 99% sure"* — percentages, not ages. Corrected, the real figure was n=8 across eleven years, half of it ad boilerplate. Every count gets spot-read before it gets written.

### 5. Compute the baseline, or don't state the rate

The message corpus contains its own control: 106,629 outbound messages against 110,944 inbound from 503 other people. **Any rate computed for Dan should be computed for the inbound baseline and reported as a ratio**, because most findings about how Dan writes are findings about how people text.

The worked case: raw counts made Dan look strikingly un-introspective — *"the thing about me"* appears **zero** times outbound. Against the baseline it evaporates; it appears zero times inbound too, because SMS is a near-zero- introspection medium for everyone in it. What survived the control was sharper and real (graded numeric confidence at 22× baseline, which is now a page).

A rate without a baseline is not a finding. It is a description of the medium.

### 6. Check what is absent

Absence is evidence, and it is the move nobody makes because there is nothing to grep for. You have to know what you expected.

- A novel the entire page was built around was **not in the reading log at all** — which broke the page's central claim.

- A person's phone numbers were **not in the message dump** — which proved the page was about somebody else.

- A predicted urgency vocabulary was **absent from eleven years of messages** — which did not falsify the axiom but established its jurisdiction, and that negative result changed how an entire spine document should be read.

Negative results get written down with the same weight as positive ones. State them on the page; they are the cheapest falsifiers the corpus produces.

### 7. Keep the mundane

The instinct to filter for significance at extraction time is the single most destructive habit available here, because significance is assigned later, by the climb, and the climb cannot reach what was filtered out.

The 495-block chat archive that reorganised a person page is *almost entirely mundane* — rent, shifts, lunch orders, baby-talk, a lost pill on a dresser. That is precisely its value: it is the only **daily** record of those years, written while things were happening rather than reconstructed afterwards by one participant during an argument about something else. The dramatic sources were already read. The boring one held the register, the private vocabulary, the household logistics and the undramatised texture, and every one of those turned into something.

When in doubt, write it down. The page budget is not a reason to drop a detail (`STYLE_GUIDE.md`, substance rule 4).

### 8. Follow a dangling citation into someone else's channel

A page will sometimes cite a dated quote as evidence for *when* something happened without ever saying *why* — a precise date, a raw emotional line, and no cause attached. That gap is not always a limit of the source; it is often a sign that the cause was said to a **different person, on a different channel**, and nobody has cross-referenced the date yet. When a page states a fact and dates it precisely but cannot explain it, search that exact date across every other channel the corpus has for the people involved — not only the subject's own words to the person the page is about.

`annie-ulmer.md` carried "I'm really really scared that you won't want this anymore," dated December 2, 2015, for weeks with no explanation attached. The explanation was sitting four hours later that same night, in a message to a different person entirely — Dan's father — and surfaced only once that channel was read to exhaustion for an unrelated reason (move 8 as an accident, not a plan). Once found, it had to be written back to *both* pages: the page whose gap it filled, and the page whose channel it was found in (`EXTRACTION_SPEC` move 3 plus `CLAUDE.md`'s write-back rule, chained). Treat every dated-but-unexplained quote on any page as an open lead, not a finished fact — and when reading any channel to exhaustion, watch specifically for lines that date-match a gap already flagged elsewhere in the wiki.

### 9. Close the loop back onto every page the source already touches

Added 2026-09-04, after a pass over the twitter archive found what happens when this move is skipped for a year.

Move 3 chases a proper noun **outward** — into the rest of the corpus, looking for a page that does not exist yet. This move runs the same read **inward**: for every entity, place, work, event and concept in the source that *already has a page*, that page is owed something, and the page you are writing is owed an edge to it.

**The two are not the same job and the second one is the one that gets skipped.** Chasing a name outward produces a new page and feels like progress. Closing the loop inward produces an edge on a page you were not working on, and nothing on your own page looks worse for its absence — which is exactly why nineteen twitter year pages could be written by reading every tweet in every year, carry 130 typed edges between them, and still leave the concert record, the nicotine row, the SLOPPP discography and a person's entire page untouched by what those tweets said about them.

**The obligation is triggered by the mention, not by a finding.** This is the part that distinguishes it from the write-back rule below. A finding is a conclusion you reached; a mention is just the source naming something. Both create work:

- **A mention** means the target page's evidence base is incomplete and it does not know. *"i miss the starting line."* is not a finding about anything. It is the only trace in the corpus that a band on a 2005 tour bill meant something to him, and the band's page could not have known it existed.

- **A finding** means the target page's *argument* is affected, and it is governed by the write-back rule.

**Run it against the target's own claims, not only its topic.** The value is concentrated where the source contradicts something the page asserts about its own completeness. A concert log that calls itself "a complete record" and a person's page that says "everything known arrives through Dan's later AI narration" are both making checkable claims, and one autumn of one archive falsified both. **A page that states its own limits is a page telling you what to point the next source at.**

**Do it while the source is open.** The reading pass is the only moment the material is in front of somebody who has read it in context; six months later it is a grep. `bin/wiki-crosslink scan <page>` names the entities a source mentions that already have pages the page does not link, and `bin/wiki-crosslink reciprocal` names the edges whose targets never got told — but both produce candidates, and a candidate is a reason to go and read the rows, never a reason to write an edge.

**Two failure modes to expect, both of which this pass hit.** A string match over a long corpus finds Rick Santorum under "Rick", Tom Cruise under "Tom" and slim jims under "slim" — nearly every single-token name match was a false positive, so a match is where reading starts. And a tidy pattern found across six matched pairs may not survive the twelfth: a Facebook-to-Twitter release lag that looked like a clean five days ran from −1 to +28 days once the match was extended, and the tidy version is the one a later pass will reach for unless the page says it failed.

## Source tiers — and the laundering failure

`raw/` mixes two kinds of evidence and conflating them is how false claims get into the wiki wearing a citation.

**Primary — records of what happened.** Message dumps and per-thread exports; the GEDCOM; `contacts.csv` and the Facebook address book; Goodreads, YouTube, Twitter and Facebook takeouts; the Gchat archive; photographs and documents.

**AI-secondary — a model reasoning about the corpus.** The Gemini and ChatGPT sessions under `dox-md/`, `THE_DAN_FRANK_BOOTLOADER.md`, `THE_DAN_FRANK_MANUAL.md`, `CATO_*`, `DANSYNTH.txt`, the profile dumps.

AI-secondary sources are not worthless — they are often the only place a memory, a self-assessment or an argument is recorded, and **Dan's own words inside a session are primary testimony**, including his corrections of the model, which are frequently the most valuable content in the file. What is *not* evidence is the model's factual assertions. These files confabulate specifics with total confidence: invented property-deed lookups, invented publication chronologies, probability estimates that wander four orders of magnitude between sessions. More than one has been sitting in the wiki as fact.

When you keep an AI-secondary claim, **attribute it on the page as one.** Three words — "per the bootloader's own synthesis" — is the whole cost, and it lets the next reader know what they are standing on.

`raw/self/context-core/CONTEXT_CORE_EXPANDED.md` sits above both tiers: curated, internally cross-checked, and explicit about its own gaps. Check it first for any self/mind/timeline question and treat other sources as supplementary or corrective to it, unless they carry a specific dated correction it lacks.

## Traps by source type

Each of these fails **silently** — it returns a plausible wrong answer rather than an error — and each has already produced a false claim on a page.

**The iMessage dump** (`raw/self/dox-scan/all_imessages_complete_dump.txt`) — the only message source with trustworthy direction.

- Records span multiple lines. A record starts `TS|Sent|handle|…`; everything to the next header belongs to it. Line-based grep splits one message into several, miscounts, and cannot show you a whole message.

- Curly apostrophes outnumber straight ones **28,904 to 19,978** in Dan's sent text. A pattern written `i'm` misses most of its own matches.

- 2022 and 2026 are **absent entirely**. Nothing here speaks to the terminal phase; that lives in `raw/self/message-csv/`.

- Use `bin/mine-messages` (`stats`, `grep`, `timeline`, `battery`, `entities`).

**`MASTER_MESSAGES_DB_DUMP.csv`** marks nearly everything `Received`. Any page built on it describes a one-sided thread that is not one-sided; the tell is a page reporting "all received (export artifact)". **Any claim about what Dan said must come from the dump.**

**Per-contact ****`imessage_<number>_both_all_now.csv`**** exports — trustworthy for discovery, NOT trustworthy for completeness until cross-checked.** `raw/self/message-csv/` holds dozens of these, one per phone number, each carrying *both* directions for that single contact. They are easy to walk past because the filename is a phone number, not a name, and because the general dumps already look like they cover the same ground — genuinely useful for that reason, since a per-contact export is often the fastest way to find a relationship's real shape (who initiates, who goes quiet) without wading through the full dump. **But "all_now" in the filename is a claim, not a fact, and this pass caught the claim being false in the most damaging possible way.** A 43-line Rick Frank export, read and trusted as complete, produced a wrong, emotionally-loaded published finding — "a 12-day outbound burst, then a decade of silence" — that stood across three pages for several hours before a routine cross-check against `all_imessages_complete_dump.txt` turned up **over 1,600 messages** for the same number the "all_now" file had reduced to 43. The general dump is itself incomplete in different ways (2022 and 2026 absent entirely, per the next paragraph), so neither source alone is safe to call complete. **The rule: read the per-contact CSV first for orientation, but before publishing any claim about message count, last-contact date, or "silence," grep the same number against the full dump and reconcile the two — if they disagree, the fuller one wins, and the disagreement itself is worth a sentence on the page,** the way this correction now is on `rick-frank.md`. Treat "this export is titled all-time" with exactly the skepticism `EXTRACTION_SPEC` already tells you to apply to a dossier's paraphrase — a filename's promise is not a citation.

**Contact identity** — `contacts.csv` (Google) merges records aggressively, so one card can carry numbers belonging to two people. The Facebook address book (`facebook/**/other_personal_information/your_address_books.html`) is unmerged and is the tiebreaker. Agreement across both is an identification; a single Google card is not. This trap put an entire page on the wrong human. The same resolution move settles **quote attribution**, not only page identity: when a dossier paraphrases a message without naming who sent it ("his father's perceived financial judgment"), do not write the dossier's framing onto a page — grep the exact phrase against the raw message exports, take the phone number or handle attached to the hit, and resolve *that* against the address book before attributing the quote to anyone. A dossier's summary is a lead, not a citation.

**Facebook Messenger HTML** — each message is a `_3-95 _a6-g` div containing, in order, sender (`_a6-h _a6-i`), body (`_a6-p`), timestamp (`_a72d`). Newest first. The takeout also contains a duplicated nested tree; do not count a thread twice.

**The GEDCOM** (`raw/self/ancestry/extracted/`) — a `PLAC` under `DEAT` is a burial place as often as a death place, and Ancestry attaches sources loosely, so a citation's publication date may not match the event date. Report both rather than picking one.

**Goodreads / FAVS** — the shelving date is not the publication year, and shelf tags often contain the shelving year. Cross-check the `year published` column, and check whether a book the wiki claims was read appears in the export at all.

**Activity exports** (Gemini, YouTube, search history) — tag soup with timestamps several fields away from the item title, so window around the match rather than grepping lines. Excellent for dating an interest precisely, and for catching a story that says "autoplay" when the record shows two related videos watched two minutes apart at 1 AM, which is a search.

## What gets written down

Extraction is not finished at the point of discovery. The output of a pass is **prose on pages**, and the density standard is the one in `STYLE_GUIDE.md`: longer, denser, consequence-ordered, with tables holding the numbers.

- **Every proper noun gets an entry or a backlog line.** One page per entity always wins over coverage — merge, never fork — but nothing is dropped silently.

- **Every finding gets written back** into every page it touches, as a typed edge whose claim states the finding (`CONNECTIONS_SPEC.md`). A finding that lives only where it was discovered will be re-derived from less evidence next time.

- **Every page the source *****mentions***** gets the mention**, whether or not a finding came out of it (move 9). The write-back rule above covers conclusions; this covers evidence. A page whose subject appears in a source it has never been shown is a page reasoning from a smaller record than the corpus holds, and it has no way to discover that from where it sits.

- **Every contradiction gets flagged, not resolved by preference.** Table the evidence, say which governs and why.

- **Every negative result gets stated.** "Checked X, it is not there" is a page sentence, not a private observation.

- **Nothing gets compressed to fit a budget.** If a source earns 20 KB of page, it gets 20 KB of page.

## Standing extraction backlog

The live version is `BACKLOG.md`; this section names the structural gaps rather than the individual tasks, because they recur.

The largest known under-mined source is **`raw/self/dox-scan/gmail_bodies.txt`**, the Gchat archive. One correspondent's slice of it (495 conversation blocks) was read in August 2026 and reorganised a page; the rest is unread. It is the only *daily-life* record of 2010–2013 anywhere in `raw/`, and daily-life records are exactly what the corpus is otherwise poorest in — everything else from those years is retrospective.

Beyond it, the recurring shapes worth a dedicated pass:

- **Behavioural rather than lexical mining.** What Dan *did* while unobserved — latency, initiation, abandonment, escalation, time-of-day — has produced the corpus's strongest findings (`contact-gini`, `message-circadian-latency`), and lexical passes have hit diminishing returns.

- **Corroboration sweeps against ****`OPEN.md`**, which lists every live contradiction, gap and standing prediction. Many name a number or a date the corpus could settle; work it top-down.

- **Second passes over sources already marked ingested.** This is not redundant work. The first pass does not know what to look for, because the pages that would tell it what matters had not been written yet.

## Logging an extraction pass

Same bar as everything else: log the pass in `log.md` as findings rather than activity — what you found, what evidence, what changed. State what you checked and did **not** find. If you left a source partly read, say which part and why, so the next pass starts where you stopped instead of at the beginning.
