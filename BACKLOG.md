# BACKLOG — the single live work list

One file, so there is one place to look. Replaces `task.md` (v1 phase tracker, retired 2026-08-08 — four of its seven remaining targets were page names that never existed), `TO-DO-LIST.md` (operator's hand list, carried forward below), `LONG_TAIL_TRIAGE.md` (2026-07-18 verdicts, executed 2026-07-19 — see "Settled" at the bottom), `contact-review.md` (a worksheet for a quarantine that no longer exists) and the campaign backlog from `MESSAGE_MINING.md`.

## STANDING DIRECTIVE — the Annie moratorium (2026-08-23, operator)

**Read ****`CLAUDE.md`**** § "STANDING DIRECTIVE — the Annie moratorium" before working any item on this page.** No new Annie material enters this repository: no export, no metadata dump, no group-chat pull, no screenshot, and no new narrative, event, synthesis or typed-edge claim about her. The reason is her safety, not the wiki's taste, and only the operator can lift it.

Every item below that depends on new Annie material is **closed, not deferred**, and is struck through rather than deleted so nobody reinstates it as an oversight. Items about other people stay live even where an Annie page is downstream of them — what is forbidden is *acquiring and writing Annie material*, not the rest of the corpus continuing to exist.

Existing Annie pages are untouched and stay untouched. The record ends at the last contact already stated, **2026-08-19 15:15:33**. Dan has not spoken to Annie since the last date the wiki records.

**This is not the resume point.** `LLM_HANDOFF.md` holds the exact place the last session stopped and what to do next. This file holds the standing work that outlives any one session. Two machine-maintained queues sit alongside it: `connection-queue.md` (mined edge candidates, `bin/wiki-connect candidates`) and `synthesis-queue.md` (mined climb clusters, `bin/wiki-climb candidates`).

When you finish something here, delete the line — the file's value is that everything in it is live. When you decide *not* to do something, leave it with a one-line reason; a considered non-decision is knowledge, and it stops the next model re-proposing it.

## 1. Extraction — the standing campaign

Per `EXTRACTION_SPEC.md`, this is the repository's binding constraint. In rough expected-value order.

- **`raw/self/dox-scan/gmail_bodies.txt`**** — the Gchat archive.** The largest under-mined source in the repository. One correspondent's slice (495 conversation blocks under `lexieamb@gmail.com`) was read 2026-08-08 and reorganised `alexis-armel`; the rest is unread. It is the only *daily-life* record of 2010–2013 anywhere in `raw/` — everything else from those years is retrospective. Blocks are keyed `Subject: Chat with <name>`, unsorted, and mostly undated (43 of 495 in the read slice carried a `Date:` header), so report sample ranges rather than spans.

- **Per-contact CSV sweep.** `raw/self/message-csv/imessage_<number>_both_all_now.csv` files exist per phone number and are the most complete two-sided record of individual relationships in the corpus, but no systematic check has been run for which person pages are missing theirs. The 2026-08-11 Rick pass found one (`imessage_7243667777_both_all_now.csv`) that had never been cited anywhere and that reversed a standing figure three pages had been carrying forward from an AI dossier. `ls raw/self/message-csv/*_both_all_now.csv`, resolve each number against a person page, and check it against that page's `sources:` list. See `EXTRACTION_SPEC.md`'s "Traps by source type" for the check to run per-page going forward.

- **Behavioural mining over lexical.** What Dan *did* while unobserved — latency, initiation, abandonment, escalation, time-of-day. `contact-gini` and `message-circadian-latency` are the model and the corpus's strongest findings. Lexical passes have hit diminishing returns.

- **Corroboration sweep against ****`OPEN.md`****.** It lists every live contradiction, gap and standing prediction; many name a number or date the message corpus could settle. Work it top-down with `bin/mine-messages grep`.

- **Second passes over sources marked ingested.** Not redundant work: the first pass could not know what to look for, because the pages that would have told it what mattered had not been written. Every source re-read in the 2026-08-08 pass yielded findings the original ingest missed.

- **Test prediction 1 of ****`calibrated-confidence`****.** Run the graded-confidence pattern over the Facebook Messenger export, `gmail_bodies.txt` and the `raw/self/chats/` sessions. If Dan sits at inbound baseline in another channel, the finding is about iMessage rather than about him and must narrow.

- **Hedging study.** The 43 confirmed hits come from one pattern. *"odds are," "there's a good chance," "I'd bet," "probably," "I doubt"* are unmeasured and would put the finding on a far larger base.

- **`bin/mine-messages entities`**** needs a spam filter** — it currently drowns in bank alerts and brand names. Real candidates already surfaced with no page: **Ricky** (66 msgs, 2015–20), **Libby** (83, 2024–25), **Alice** (50, 2023–25), **Derrick** (29), **Michelle** (31). A sixth, **Lucy** (67, 2015–18), needs the one-page-per-entity check first — `wiki/people/lucy.md` exists and is the household dog, so the miner may be catching messages *about* her.

- **`"supposed to be"`**** at 2.17× baseline (n=123)** — the best-powered unexplained divergence in the lexical battery. An obligation/expectation frame running at twice baseline is a `mind/` finding waiting to be read.

## 2. Structure and coverage

- **Lineage split** (operator, standing). Separate the ancestry/23andMe material into a **family-tree** entry and a **genealogy** entry; give the full Ancestry tree data and a visual; expand the 23andMe entry with the full chromosomal and region-specific data. A hybrid 23andMe × Ancestry analysis page is wanted too, **clearly labelled speculative**.

- **The ****`raw/`**** wikilink question.** Ten wikilinks point into `raw/`, which is deliberately unpublished, so they render as broken on the site. Either publish a stub explaining `raw/` is private, or mark them so they stop reading as errors. Unresolved by design since 2026-08-08.

- **Domain height.** Four domains — `self`, `timeline`, `work`, `places` — have three or more pages and nothing above any of them. `bin/wiki-climb audit` shows live progress; `synthesis-queue.md` holds the mined clusters.

- **Two more full-section candidates for the portal** (opened 2026-08-29, from the crawl that produced THE DOCKET). Both are large, fully-structured datasets in `wiki/` that no room on the site currently reads:

  - **`wiki/timeline/master-timeline.md`** — 2,842 dated events across 79 years (1796–2027) drawn from 342 pages, three tiers, each linked back to the page *and section* that documents it, generated by `bin/wiki-timeline`. Fully machine-parseable (`- ★ **date** — description ↳ [[page]] · Section`). LEVIATHAN's CHRONOLOGY counts *date mentions* rather than events, and THE ATLAS is movement 2014–2024, so neither covers it. This is the strongest remaining candidate for a room.

  - **`raw/self/favorites/FAVS MASTERLIST.csv`** — 2,016 entries (1,860 music, 120 books, 25 art, 11 film) with ratings, tags and dates read. Carries `closing-the-set`'s thesis directly (86.7% of authors appear exactly once; half the shelf is two subjects through forty-four hands). **Note the honest shape:** the portal already declares this over there as LEVIATHAN's **THE SHELF**, status `SEALED` — "waiting on a corpus this site does not carry" — so the correct build is to light that instrument up, not to open a tenth room.

## 3. Named open questions

Each of these is a specific thing the corpus or the outside world could settle.

- **Which Bacharach novel the coincidence is in.** Dan attributes the Virginia Avenue passage to *The Bend of the World* and cites pages 227–228; Bacharach's own 2021 message names *The Doorposts of Your House and on Your Gates*, and the reading log holds only the latter. One page number checked against a physical copy closes it. (`wiki/people/jacob-bacharach`)

- **Where Dan actually slept, spring–summer 2018.** He gave out 117 Belmont Circle five times between February and September 2018, four of them after Fran's death, while the residence timeline has him at 155 Virginia Ave until February 2019 and an eviction notice was served there on 2018-03-29. A targeted read of that window would settle a timeline the wiki carries as "outcome undocumented."

- **The announcement rule, tested backwards.** All 127 exit declarations are announced by definition; the falsifier is the reverse case — a silent severance that executed. The one claim the corpus can attack on its own.

- **~~`the-unnamed-man`~~****~~ vs ~~****~~`tuquick-17248123683`~~** — **SETTLED 2026-08-09.** A FOREWARN lookup identified Tuquick as **Jerel Wayne Coles** (exact phone-number match, 2026-08-08); the operator then confirmed directly that Tuquick and the July 2026 unnamed man are the same person ("They are the same person — tuquick and unnamed," filed at `raw/people/captures/2026-08-09-tuquick-unnamed-man-correction.md`). [[wiki/people/jerel-coles]] is now the canonical entity page for all three identities.

- **Is Coles = Target G?** FOREWARN returned no marital data. `wiki/people/annie-ulmer.md` §Target G names him only as "Caitlin's husband."

- **Why did Coles hold two addresses (Uniontown/Connellsville) for 22 months, 09/2024–07/2026?** Unexplained; see `wiki/people/jerel-coles.md` §Open questions.

- **~~Does the "video proof / unconscious" accusation originate with Coles (2026-07-26, from Annie's phone) or with Annie (2026-05-31, 23:54)?~~** **CLOSED — Annie moratorium 2026-08-23.** Answering it means mining her thread and writing the result onto her page. Not run, and not to be run.

- **Independent docket verification of Coles's criminal record** via PA UJS (ujsportal.pacourts.us) — the FOREWARN capture is commercial-aggregator sourced, not court-verified.

- **~~The ~~****~~`annie_metadata_24h.csv`~~****~~ / ~~****~~`imessage_export_2124702449_20260809084846_.csv`~~****~~ sourcing gap.~~** **CLOSED — Annie moratorium 2026-08-23.** The exports are not to be filed. The gap on [[wiki/timeline/events/august-2026-unmasking]] and [[wiki/mind/synthesis/read-receipt-forensics]] stands, visible and unfixed, and that is the intended outcome.

- **`reply_to_guid`****-as-threading audit.** [[wiki/mind/synthesis/read-receipt-forensics]] finding M2 voids any prior analysis that treated `reply_to_guid` as an intentional reply marker rather than an auto-populated field. No such prior analysis has been identified yet — sweep for one.

- **The ****`463-morgantown`**** mechanics-lien deadline** (~2026-07-27) elapsed with no recorded outcome, and the date was always derived rather than documented. The risk is now unobserved rather than pending, which is worse. A Fayette County prothonotary/recorder search on the parcel answers it.

- **Outside-corpus lookups, all cheap:** Fayette County magistrate records for the April 2018 hospital incident; Fayette/Somerset records for Jay Lauer's exact date and cause of death; the date and authorship of Diane's letters; whether Champion, PA lies outside Fayette County (if so it is the line's only attested out-of-county residence in four generations).

- **The 187-of-191 love-to-request statistic is stale on five pages, and the fix is blocked by the moratorium, not forgotten.** `dan-annie-fallout-verdict`'s own 2026-07-18 REVISED block found the figure non-diagnostic — 97.2% of *all* her messages are equally request-adjacent at 24h, and the directional test (1h window) inverts it — and `wiki/people/annie-ulmer.md` already carries the correction. `wiki/mind/concepts/conflict-architecture.md`, `wiki/mind/concepts/attachment-model.md`, `wiki/mind/synthesis/the-binary-verdict.md`, `wiki/mind/synthesis/the-rescue-premise.md` and `wiki/people/annie-ulmer-personality-assessment.md` still cite the raw figure without it — found during the 2026-08-28 constitution pass on `dan-annie-fallout-verdict`, not fixed there. A correction requires stating what the statistic does and doesn't show about Annie's behavior, which is new Annie-adjacent prose the standing moratorium reserves to the operator's discretion — not attempted by this session. Fix once the moratorium lifts, or sooner if the operator says the correction itself is in scope.

## 4. Tooling and hygiene

- **HIGH — nothing gates ****`main`****, and four portal saves have now broken it in one day.** `bin/wiki-check --check-only` on push to `main` would be a ~4-second workflow with no side effects and would have caught both incidents within a minute. On 2026-08-13 a stale-snapshot save deleted 56 typed-edge claims and ~30KB of `people/annie-ulmer` and sat red for a day; on **2026-08-22** a portal save put two stray characters inside a wiki path in `people/ally-lubin` (`...2018-deep-cycle  im`) and turned `bin/wiki-connect check` red on `main` within four minutes of a merge; later the same day the stale-snapshot clobber recurred on `ally-lubin`, and a save to `annie-ulmer` duplicated its H1 and left `bin/wiki-freshness` red. **All four were found by a session happening to look**, the last one only because a check-in scheduled for another purpose re-ran the gates. The portal editor will save anything, so this class recurs by construction — the fix belongs in CI, not in vigilance.

- **The portal editor accepts keystrokes into structural fields.** Distinct from the stale-draft bug fixed by `draftIsStale`: here the payload was correct and fresh, and a cursor was simply in the wrong place. Worth a client-side check in `caakehorn/home` that a `connections[].page` value resolves before a save is accepted, and that infobox values do not end mid-word.

- **`leviathan/factstory.html`****'s INGEST BRIEF is out of lockstep** with `FACTSTORY_BRIEF_TEMPLATE.md` and has been since 2026-08-02. That repo is not always in session scope; regenerate when it is.

- **Enforce the disclosure line mechanically.** `bin/wiki-climb check` could warn when an `earned` page synthesizes a `mixed` one without stating what primary evidence it added. Ten of nineteen pages satisfy the substance and skip the sentence. Small, safe, with a clear spec behind it.

- **Swarm-era stubs still unrewritten:** `arnu`, `alexander-jackson`, `john-carney` — fragment prose and dossier shorthand. They carry correct typed edges; the bodies were never done.

- **`leviathan`****'s ****`WIKI_BRAIN_TOKEN`** is a fine-grained PAT that expires within a year and will break the hourly mirror sync identically when it does. A read-only deploy key via `actions/checkout`'s `ssh-key:` is the non-expiring alternative.

- **A ****`grep`**** gate for retracted strings** (opened 2026-08-18). Five pages were found carrying the retracted "$750/week" figure, two of them *underneath a correction block that quoted the sentence it had never changed*. No gate sees this: the pages lint clean, edges type-check, dates are current. A retracted claim is a string, and a pass that records one could register it in a `RETRACTED.md` ledger the gate then greps for across `wiki/`. This would have caught all five, including the `$750/wk` abbreviation that a `$750/week` sweep misses.

- **Regenerate ****`master-timeline`**** in the pre-commit block.** It was 484 events and 7 pages stale on 2026-08-18 because `bin/wiki-timeline generate` is not in CLAUDE.md's "before every commit" list, unlike `wiki-digest` and `llm-publish`. It is derived and cheap; there is no reason it should ever drift.

- **Lint duplicate frontmatter keys** (opened 2026-08-18). Three pages carried the same key twice, and because YAML keeps the *last* occurrence while `bin/wiki-climb`'s own reader collects *both*, the repo's gates and every standard parser disagreed about those pages' contents. `wiki/work/fastly-fsly.md` was silently dropping its membership in `2020-2021-market-era` — the page's entire reason for existing — and `wiki/people/jerad-friedline.md` was dropping `context-core`. The portal at `caakehorn/home` parses this frontmatter for real, so the derived snapshot was losing edges the gates said were present. All three are fixed; the check is four lines of Python and belongs in `bin/wiki-lint` so the class cannot recur. Worth auditing whether `fm_list`'s permissiveness hides anything else.

- **30 pages carry ****`status: archived`**** outside an ****`archive/`**** directory**, which `STYLE_GUIDE.md` reserves for pinned artifacts that are never updated. The status is being used to mean "finished" — the documented default for which is `stable`. This matters because it makes those pages look exempt from correction: `wiki/timeline/periods/2018-deep-cycle.md` was one of them and was feeding a false claim into the generated master timeline. Audit and re-status; `bin/wiki-lint` could then enforce the directory rule.

## 5. Settled — do not re-litigate

Kept because re-proposing these wastes a pass each time.

- **`wiki/people/contacts/`**** was eliminated on purpose** (commit `65f80c2`), and the quarantine concept with it. Stubs were promoted or merged. Any governance text still describing a contacts quarantine is stale; fix the text, do not recreate the directory.

- **The long-tail triage of 2026-07-18 is executed.** All six "MINE" targets (`sam`, `davey-fitzpatrick`, `vaughn`, `nick-mattie`, `urpaaa-at-yahoo-com`) and the `jason-bermejo` opener rewrite were completed 2026-07-19. The ACCEPTED-LEAF pages — annoying, bekah-fullem, brennan-meadows, bub, drew, jason-cole, josh-coccagna, kya-hansen, lisa-durbin, mike-cordaro, mohammed-bin-salman — are real prose pages, deliberately reachable from their index only. Do not churn them; revisit only if new raw evidence links them to a host page.

- **The swarm-stub category is believed empty.** All twelve 2026-06-23 template stubs under `wiki/people/` were rewritten by 2026-07-20. Before resuming that line of work, re-run the `date_created == date_modified` + 2026-06-23 heuristic to confirm, rather than assuming there is more.

- **`mind/psychosexual/taboo-and-boundary-testing`** is the known thinnest page. Rewrite only if a richer primary source surfaces; otherwise leave it.

- **`data/wiki-data.json`**** in the public ****`leviathan`**** repo carries the full body prose of every page, served unauthenticated.** Raised with the operator, who confirmed the exposure is intended. Making `wiki-brain` private did not make the wiki's contents private, and that is a decision, not an oversight.

## Phantom citations — sources cited but empty (opened 2026-08-14)

`bin/source-index` found four header-only files in `raw/self/message-csv/`, two of them cited by wiki pages as though they carried evidence:

- **`END_FIGHT_full.csv`** (68 bytes, 0 rows) — cited on `wiki/self/message-corpora/master-message-dump.md`, `wiki/timeline/events/end-fight.md`, `wiki/timeline/events/group-chat-closure.md` (credited specifically for "sequence details"), and `wiki/mind/synthesis/dan-annie-fallout-verdict.md`.

- **`annie_group_chat_may31-june1_2026.csv`** (68 bytes, 0 rows) — cited on `wiki/mind/synthesis/bond-switch-2015.md`.

- `annie_group_chat_relaxed.csv` (57 bytes) and `messenger_export_THREADKEY_HERE.csv` (0 bytes) — not cited anywhere.

**The work, not yet done:** for each of the five citing pages, determine whether any specific claim rests on the empty file *alone* rather than on a co-cited non-empty source. Every one of those pages also cites `THE END FIGHT.csv` (589 real rows) or `annie_all_time_logs.csv`, so the likely finding is that the empty citations are redundant decoration and no claim falls — but that is a hypothesis, not a result, and "likely redundant" is exactly the reasoning that let the `sic semper` inversion stand for two months. Do not close this by assuming.

Do **not** delete the empty files. `raw/` is immutable, and per the 2026-08-13 doctrine on artifacts that produced a documented failure, they are retained as the worked example behind this backlog item.

## [2026-08-21] Staleness: cleared to zero, and what it cost to check

`bin/wiki-climb check` reports **0 warnings**. Every pair previously recorded here — the fourteen from the 2026-08-19 five-climb pass and the nine from the 2026-08-20 severance ingest — was re-read against the premise that moved and carries a real `RE-CHECKED` block. None was cleared by bumping a date.

**Two were not cheap, exactly as this file predicted.**

- **`the-embedded-objective`**** ← ****`bfs-foods`** (flagged here as "the least cheap of the nine — do this one first"). It was right. The BFS row is doing work as the control proving that an absent payload collapses tenure to weeks, and the restoration message supplies a **second, incompatible account of why the job ended**: this page says Dan refused the $50 drawer shortage and the write-up, while his own 2026-08-11 retrospective says *"the only thing I did was go home 30 minutes before my shift"* — against a posted `NO HIRE: Daniel Frank` sign in two locations. A tenure ended by arbitrary employer action cannot be quoted as a clean control for a variable about Dan's own sustaining. The rule survives; the row now carries the qualification and Caviar is named as the stronger of the two controls.

- **`the-commissioned-self`**** ← ****`wiki-brain`** (flagged as "worth one check rather than an assumption"). Checked: the handle-is-not-a-person defect does **not** reach it, and for a structural reason worth keeping. The load-bearing count is **outbound** (17 appearances across 106,629 sent messages), and the defect is an inbound-attribution problem, so that measurement is immune by construction. The one inbound figure supports an *absence* claim that a third party on Annie's phone cannot fill.

**A cascade to expect next time.** Re-checking a page bumps its `date_modified`, which restarts the staleness clock for everything downstream of it — so the pass ran in four converging rounds (24 → 5 → 2 → 0) and the last three rounds were re-checks of pages whose premise had moved *only by gaining a re-check block*. Those are cheap and were verified rather than assumed, but the shape is worth knowing before starting: clearing N warnings costs more than N reads. Whether a page whose sole change is an added `RE-CHECKED` block should restart its dependents' clock is a real question about `bin/wiki-climb`'s semantics, and is left open deliberately — the conservative behaviour is the current one.

**Still open and untouched by that pass:** `the-unbroken-bond` ← `enneagram-5w4`. Not a staleness warning (the dates do not trip it) but the one flagged pair where the premise gained a **contradiction** rather than an addition: a 5w6 reading would change the sx/sp fusion account the bond page leans on. This remains the highest-value re-read in the psychological layer.

## [2026-08-19] Collect what other people say Dan is like

Named as the missing control on `wiki/mind/synthesis/the-commissioned-self`. The corpus holds 110,944 inbound messages from 503 handles and the wiki has **no independent characterisation of Dan by anyone who is not either him or an instrument he commissioned** — no clinician, no employer instrument, no third-party account. A pass over inbound messages for second-person description would give the psychological layer its first outside input, and it is cheap: `bin/mine-messages grep --dir Received` over a small set of framings (*"you always", "you're the kind of person", "that's so you"*) would produce a first sample in an afternoon.

## [2026-08-19] Two one-query questions the housing synthesis cannot answer

`wiki/places/the-unpapered-address` establishes that no lease, rent figure or signatory exists in the corpus for any of seven residences. Two of its gaps are answerable from outside `raw/` and would outrank the whole page:

- A **Fayette County recorder/prothonotary search** on the 463 Morgantown parcel — settles the elapsed Arnu mechanics-lien deadline, which has been open since ~2026-07-27 and is already flagged on `wiki/legal/463-morgantown`.

- The **307 E 76th lease signatory**. The rent is now known ($2,450 → $2,700); the name is not, and it decides whether Dan was ever a named party to a residential lease at all or only ever an occupant.

## Staleness left open by the 2026-08-20 August-severance ingest

Thirteen `bin/wiki-climb check` warnings stand after that pass. **Nine are its own**; four (`jerad-friedline`, `2020-2021-market-era`, `fastly-fsly` ← `context-core`, and `the-cool-metric` ← `interests-as-era-markers`) predate it. Eleven pages were re-checked properly during the pass, including the five where a conclusion could plausibly have moved (`the-unbroken-bond`, `dan-annie-fallout-verdict`, `ally-and-dan-love-as-destiny`, `read-receipt-forensics`, `single-channel`) — each carries a real `RE-CHECKED` block, none was cleared by bumping a date.

The nine below are believed cheap. **That belief is a hypothesis, not a result**, and each states its reason so a later pass can disagree with the reason rather than re-derive it:

| **Dependent** | **Premise that moved** | **Why it is believed cheap** |
| --- | --- | --- |
| `health/the-configured-body` | `health/cocaine`, `supply-network`, `the-deferred-audit` | All three moved by `RE-CHECKED` block only. The body page's argument is about maintenance vs. surveillance, not about supply topology. |
| `interests/food-and-diet` | `work/bfs-foods` | BFS moved for the 2026-08-11 job restoration — an employment fact, not a food one. |
| `mind/synthesis/the-embedded-objective` | `work/bfs-foods` | **The least cheap of the nine.** BFS gained the posted `NO HIRE: Daniel Frank` sign, in two locations, and the reversal being initiated by the same person who imposed the ban. That is institutional-arbitrariness evidence and may be live for this page's argument. Do this one first. |
| `mind/synthesis/alias-as-periodization` | `totality-themes` | `totality-themes` moved by `RE-CHECKED` block only. |
| `mind/synthesis/closing-the-set` | `forensic-method` | `forensic-method` moved by two typed-edge additions and no prose. One of them points at `document-fabrication`, which is about production rather than intake. |
| `mind/synthesis/the-commissioned-self` (×2) | `instrument-is-subject`, `wiki-brain` | Both moved by `RE-CHECKED` block only. But note: `wiki-brain`'s new block is the handle-is-not-a-person defect, and `the-commissioned-self` counts first-person self-description across the corpus — if any of those counts run over Annie's 212 handle, the attribution caveat reaches them. Worth one check rather than an assumption. |
| `people/jerad-friedline`, `timeline/periods/2020-2021-market-era`, `work/fastly-fsly` | `self/context-core` | **Pre-existing, not from this pass.** Standing since 2026-08-19. |
| `mind/concepts/the-cool-metric` | `interests-as-era-markers` | **Pre-existing**, standing 8 days. |

## Standing items from the 2026-08-20 ingest

- **HIGH — transcribe ****`raw/self/audio/2026-08-16_Morgantown_St_call-recording.m4a`****.** 927 s of primary audio; the only account of it in the wiki is two removes from the source (a T2 agent analysis quoting a PDF that is not in `raw/`). Every quotation on `wiki/timeline/events/august-2026-morgantown-call` and `wiki/people/jerel-coles` becomes checkable the moment this exists. This is the single highest-value action available on the August material.

- **~~HIGH — did the email to Annie's parents ever send?~~** **CLOSED — Annie moratorium 2026-08-23.** The `CONTRADICTION` on the event page is now permanent: it is not resolved, and the check that would resolve it — reading a sent-mail folder and writing a verdict about a disclosure threat aimed at Annie's family — is exactly what the directive forbids. Leave the blockquote exactly as it stands.

- **HIGH — export the Ally thread for 2026-08-13 → 20.** Named as missing by the 2026-08-19 audit and still missing. `wiki/self/concepts/ally-and-dan-love-as-destiny` is now making predictions across a severance it cannot see the other side of, and this pass added a slot-refill control to it that cannot be evaluated without the baseline.

- **MED — sweep the corpus for earlier third-party-handle episodes.** Three are documented (2026-07-26, 2026-08-16, 2026-08-18), all found by register alone. There is no column for this and no detector. Whether it happened before July 2026 has never been asked.

- **MED — the two videos.** The "molesting" video and the October 2019 MMF video are both circulating as leverage between three people and neither has been examined by anyone writing this wiki. The claim that turns on the first — eyes open at 0:37 — is Dan's, stated to two audiences, uncorroborated.

- **MED — recover the three drug-screen images** (2026-08-14 13:17, 14:08, 14:11). `wiki/mind/concepts/document-fabrication` rests entirely on the message thread describing them; the artifacts would settle how good the forgery actually was.

- **LOW — ****`wiki/people/index.md`**** is 23KB against an 8KB budget.** Standing lint warning, untouched by this pass.

- **~~Add a conflict-marker gate to ~~****~~`bin/wiki-lint`~~****~~.~~** **DONE 2026-08-20.** Shipped as `find_corrupt_text()`, and widened once a second class of invisible junk turned up the same day: eight **assistant citation artifacts** (private-use codepoints U+E000–U+F8FF wrapping a `filecite`/`turn` reference) in `morgantown-call-three-participant-ethical-analysis.md`. They render as nothing, survive copy-paste, and assert a source that points nowhere. The gate now catches both, with eleven tests — including a regression test that the whole wiki stays clean, and negative tests proving a setext underline and an `=======`-with-trailing-content are not markers.

## [2026-08-21] Sixty-five bare `## Related` footers — the last linking debt

`bin/wiki-connect check` is at **0 errors, 65 warnings**, and every warning is the same thing: a page whose relationships are still a legacy untyped `## Related` footer rather than typed `connections:` edges. Between them they carry roughly **960 untyped entries**.

The 193 missing *inverse* edges that used to dominate this gate were closed on 2026-08-21 and are not coming back; this is the remainder, and it is the half that cannot be done mechanically. A retrofit inverse may reuse its source's claim (`CONNECTIONS_SPEC.md`), but a **forward** edge has to choose a type, and the type is the analytical commitment — `co-occurs` where the evidence would support `causes` is a substance failure, and `causes` where it only supports `co-occurs` is a provenance failure. That is a judgment per entry, from the page's body, not a transformation of the footer.

Two were converted on 2026-08-21 as the worked examples of the cost: `people/emaly-minerd` (6 entries) and `people/trinity-st-clair` (4). Both took a full read of the page.

**Method, so the next pass does not re-derive it.** Convert a page, then re-run the reciprocity applier — each new forward edge opens an inverse warning on its target, so the gate count goes *up* mid-pass and only comes down at the end. Work in batches and finish with `bin/wiki-connect check` at the reciprocity step, or the count will look like a regression.

Highest-value first, by content weight: `self/tattoos` (8 entries), `mind/psychosexual/orchestration-and-voyeurism` (7), `interests/music/concepts/lyrics-as-timbre` (7), `self/facebook` (10), `interests/favorites/music` (15), `timeline/events/teen-concert-years` (6), `timeline/events/shelbie-annie-threesome-april-2019` (3). The `interests/favorites/music/artists/*` cluster is the long tail and the least urgent — those pages are deliberately index-reachable leaves.

## Open lead — @Woodguts (added 2026-09-02)

Seventeen tweets across 2009–2013, fourteen of them direct address, including *"When I grow up I want to be @Woodguts"* (2 Dec 2011) and a place in the four-name cohort Dan lists on 23 Feb 2012 alongside Polyak, Jester and Josh Brannan. Music-adjacent — *"ew Cubase"* (20 Jun 2010) is a DAW opinion, which puts him in the production orbit rather than the Uniontown one.

**Unidentified.** No match in `contacts.csv`, no appearance in any message export, no mention on any wiki page. Resolving the handle to a name would give the NYC-era social graph its fourth member; until then there is no page, because a page keyed to a handle with no identity would assert less than this entry does. `bin/mine-tweets handle woodguts` is the whole evidence base.

## Blocked — the portal has not published since 2026-09-02 04:47 UTC (added 2026-09-02)

**Symptom.** Nothing merged to `wiki-brain` after 04:47 has reached the live site. Five merges since then (#237, #239–#244 and #243) are not on the portal; `public/wiki` in `caakehorn/home` does not contain `wiki/meta/testimony-veracity` at all.

**Not the wiki-brain half.** `.github/workflows/notify-portal.yml` is working: `PORTAL_DISPATCH_TOKEN` **is** set — CLAUDE.md's claim that "nobody has added it yet" is stale and should be corrected — and run 77 at 17:58:41 logged `Dispatched wiki-updated (sage: 0, pages: 6, plain: 0, words: 0)` on an HTTP 204. The dispatch is being sent and accepted.

**The failure is in ****`caakehorn/home`****'s ****`sync-wiki.yml`****, at ****`npm run history:check`****.** Reproduced locally against a full-depth `wiki-brain` checkout at `e56d8f0`: every other step of the derivation passes — `sync-wiki.mjs` (496 pages), `build-wiki-history.mjs` (3,832 revisions, 3,832 reconstructions verified), `leviathan`, `wiki-instruments`, `core`, `docket` — and then:

✗ people/jerad-friedline @ e3c02f3b6b: git says +9/−2, this dataset says +8/−1

✗ self/concepts/astrology-star-signs @ 03425a4d53: git says +7/−1, this dataset says +0/−0

`check-history.mjs` exits 1, and the workflow is **all-or-nothing by design** — "every step above runs before anything is staged, so a build that fails leaves the whole snapshot at its previous state." So one unreproducible revision freezes publication of the entire corpus.

**Both failing revisions are from 2026-08-26** and neither page has been touched since, so this is not caused by any recent pass. `03425a4d` is a non-merge commit where git reports +7/−1 for the astrology page and the built dataset reports no change at all — a defect in `build-wiki-history.mjs`, which `check-history.mjs` is correctly refusing to publish over.

**The architectural finding, which outlives the bug.** A hard gate on a derived sub-feature is a hard gate on everything shipped beside it. The history dataset is one panel on a page; its correctness check currently has the authority to stop the wiki from publishing. Whatever fixes the two revisions, that coupling is worth revisiting: a history panel that cannot be reproduced should degrade to absent, not take the snapshot down with it.

**Cannot be fixed from wiki-brain.** The bug and the fix are both in `caakehorn/home`. This session has read-only access to that repository.

## The twitter tree dates by UTC, and a quarter of it is a day early

**Measured 2026-09-04.** `created_at` in `raw/self/twitter/archive.jsonl` is UTC. **687 of its 2,741 posts — 25.1% — were posted between 00:00 and 04:59 UTC**, which is the *previous* evening in New York. All nineteen `wiki/self/twitter/` year pages, and every page quoting a tweet date from them, use the raw field. So roughly one date in four across that tree is one day later than the day the tweet was actually written, and it is the evening tweets — disproportionately the personal ones — that carry the error.

Two dated examples already on pages: the two barbed `@alexisarmel` tweets filed as `2013-11-30` were posted at 22:12 and 22:31 EST on **29 November**; the Hitler/Eva Braun joke `wiki/self/twitter/2013` dates to 22 November was posted at 21:12 EST on **21 November**.

**Not a defect in the archive and not urgent.** The convention is at least consistent, which is why nothing has ever gone wrong because of it. It matters where a date is load-bearing — a same-day join against another corpus, an event's date, an ordering claim inside 24 hours. The fix is a decision before it is an edit: either convert at read time and re-date the tree, or keep UTC and say so on `wiki/self/twitter`. Whoever takes it should note that a re-dating cascades into every page that cites a tweet date, and that `bin/mine-tweets` and `bin/wiki-crosslink` both surface the raw field.
