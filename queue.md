# Ingest Queue

*Items waiting for or in the middle of ingestion. **`bin/capture status`** lists the inbox.*

## Highest-value pending item

**ANNIE MORATORIUM — 2026-08-23.** Every Annie row below is closed by the standing directive in `CLAUDE.md`. No Annie export, metadata dump, group-chat export or screenshot is filed or mined from this date, and nothing new is written about her. The rows are struck through rather than deleted so that a future session can see the instruction was withdrawn on purpose and does not helpfully reinstate it.

| **Item** | **Priority** | **Notes** |
| --- | --- | --- |
| **~~Next export of the Annie 212 thread~~** | **INGESTED 2026-08-02** | Filed as `raw/self/message-csv/imessage_export_2124702449_20260802.csv`. All four open questions answered: the goodbye broke in 18 minutes; Dan DID contact Ellen (06:22 Jul 26); the exposure threat was executed and retracted the same day; the allegation was elaborated but not reported. The third party is still unidentified — and now known to be unidentified **by Dan's choice**, see [[wiki/people/the-unnamed-man]]. New event page: [[wiki/timeline/events/july-august-2026-reentanglement]]. |
| **~~The NEXT export of the Annie 212 thread~~** | **CLOSED — ANNIE MORATORIUM 2026-08-23** | Not pending, not deferred: **withdrawn.** Under the standing directive in `CLAUDE.md` ("STANDING DIRECTIVE — the Annie moratorium") no further Annie export is filed or mined, by any session, ever, unless the operator lifts it in person. The four questions this row carried — the Aug 2 apology to Suz, Annie's therapy, the supply arrangement, the announcement-predicts-non-execution rule — are **not open questions any more**; they are questions the wiki has decided not to answer. Do not reopen them from a new export. The record ends where `wiki/people/annie-ulmer.md` already ends, 2026-08-19 15:15:33. |
| **~~`annie_metadata_24h.csv`~~****~~ and ~~****~~`imessage_export_2124702449_20260809084846_.csv`~~** | **CLOSED — ANNIE MORATORIUM 2026-08-23** | The sourcing gap on [[wiki/timeline/events/august-2026-unmasking]] and [[wiki/mind/synthesis/read-receipt-forensics]] stays open and stays visible: those exports are **not** to be filed to `raw/`. An unfilled `sources:` on a page that names its provenance in prose is the lesser cost. Leave both pages exactly as they are. |
| **Arnu mechanics lien, 463 Morgantown** | **CRITICAL — matures ~2026-07-27** | Time-sensitive and unresolved in every source read. See wiki/legal/463-morgantown.md. |
| ~~The July 4 2026 email thread (Annie → Dan, re Milo/fireworks)~~ | **CLOSED — ANNIE MORATORIUM 2026-08-23** | Not to be retrieved. It is described where it needs to be described; it does not get archived. |

## Factstory batch of 2026-08-02 (brief #4) — INGESTED, queue cleared

Four manual captures (`wikibrainingestbrief4`). All four filed to `raw/` and synthesized on 2026-08-02; nothing from this batch remains pending.

| **Capture** | **Filed to** | **Landed on** |
| --- | --- | --- |
| Jay Lauer Death | `raw/people/captures/2026-08-02_010509_jay-lauer-death.md` | `wiki/people/jay-lauer.md` rewritten (death dated to Apr 10–11 2017 from the corpus); new `betherin-mechling`; `ellen-ulmer` thread origin; `supply-network` fatality section |
| The Fall of Fran (F-alliteration version) | `raw/self/captures/2026-08-02_031532_the-fall-of-fran-frank-s-fumes-force-four-fire.md` | New `wiki/timeline/events/the-fall-of-fran.md` + `uniontown-hospital-vape-alarm.md`; `arrangement-history` start date corrected |
| Fall of Fran (glyph version) | `raw/self/captures/2026-08-02_041331_fall-of-fran-alternate-version-ignore-glyph-fo.md` | `fran-coldren` caregiving-years expansion; `fran-death-vigil` keno morning + gap closure; new `diane-shrum`, `fred-adams`; `family-tree` corrected |
| Perspective: Complete Objective | `raw/mind/captures/2026-08-02_122411_perspective-complete-objective.md` | New `wiki/mind/concepts/acquisition-drive.md`; `big-five-psychometrics` contradiction; `vanessa-frank` ATM episode |

**Open from this batch, answerable only outside the corpus:** whether anything was ever filed after the April 2018 hospital vape incident (Fayette County magistrate records); Jay Lauer's exact date and cause of death (Fayette or Somerset County records — he was "from near Somerset"); and the date and authorship of Diane's exclusion letters.

## Factstory batch of 2026-08-02 (brief #5) — INGESTED, queue cleared

Five manual captures (`wikibrainingestbrief5`). All five filed to `raw/` and synthesized on 2026-08-02; nothing from this batch remains pending.

| **Capture** | **Filed to** | **Landed on** |
| --- | --- | --- |
| Bald Eagle Cummings | `raw/self/captures/2026-08-01_154050_bald-eagle-cummings.md` | New: `wiki/timeline/events/bald-eagle-cummings.md`; seven-springs gap closed |
| Picky Eater | `raw/self/captures/2026-08-01_154556_picky-eater.md` | `wiki/interests/food-and-diet.md` (rule falsified and restated); `the-deferred-audit` food row corrected |
| Fran name change | `raw/people/captures/2026-08-01_180942_fran-name-change.md` | `wiki/people/fran-coldren.md`; closed the coal-baron gap on `estate-money-spine` |
| Concerts update | `raw/interests/captures/2026-08-01_222556_concerts-update.md` | `wiki/timeline/events/teen-concert-years.md` — 36-show researched record, two contradictions flagged |
| Franki and the Fireworks | `raw/people/captures/2026-08-02_004832_franki-and-the-fireworks.md` | New: `franki-fireworks-day-2013`, `joe-croftcheck`; closed gaps on `franki-faris` and `chaos-preference` |

Two earlier captures from this series had been committed to root-level `stories/` and `facts/` directories outside the inbox→raw→wiki flow (PR #70) and were therefore filed but never ingested. Those directories are removed and their contents are now in `raw/` where they belong.

## Inbox — pending ingestion

| **Item** | **Priority** | **Notes** |
| --- | --- | --- |
| ~~2026-07-11_140000_ANCESTRY_DNA.txt~~ | **RESOLVED 2026-08-26** | Read in full. Two of three layers were already-absorbed: the multi-section AI narrative analysis shares verbatim phrasing ("psychic sinkhole," "trauma-coded geography") with `raw/self/dansynth/DANSYNTH.txt`, already fully synthesized into `wiki/mind/synthesis/ancestral-dialectic.md`; the embedded ChatGPT export ("Familial Analysis and Insights," recovered from malformed JSON via targeted regex extraction — see the raw file's own header note) is Dan re-pasting the same 515-person Ancestry.com GEDCOM already captured, more completely and accurately, in `raw/self/ancestry/extracted/Daniel Frank family tree.txt` and summarized in `wiki/self/lineage/family-tree.md`. One genuinely new, GEDCOM-verified fact survived: Daniel Shrum (1884–1918, Greensburg), a collateral great-granduncle whose 1918 census/death record the AI's "weird and interesting" riff surfaced correctly — added to `wiki/self/ancestry.md`'s Shrum paragraph, with the AI's "died during the 1918 flu pandemic" reading flagged as plausible-timing inference rather than documented cause of death. Filed to `raw/self/ancestry/ANCESTRY_DNA.txt`. |
| ~~2026-07-11_140001_google-takeout-manifest.html~~ | **RESOLVED 2026-08-26** | Byte-identical (md5 `fb7622e7…`) to already-filed `raw/self/archives/google-data-export-index-20260623.html`, already cited on `wiki/self/location-history.md` (archived — the underlying export, 99 files/66.1MB/2024-05-14, is separately filed under `raw/self/location/2026-06-22-ingest/`). Removed from inbox rather than re-filed; no new fact. |
| ~~2026-07-12_152457_add-individual-entry-for-personality-pro.md~~ | **DONE 2026-08-26** | Triaged: MBTI/Enneagram/etc. already covered by `wiki/mind/profile/`; the autism/neurodivergence request was the real gap — new page `wiki/mind/profile/neurodivergence.md`. Removed from inbox. |
| Jared/Tricia Google Voice export (pending, from Dan) | MEDIUM | Full export requested for the "picture" story context; jaredtricia.md written from a partial ChatGPT-pasted transcript in the meantime — revisit once the fuller export lands |
| Nabeel thread (2019-05-14/19, ~confirmed genuinely Annie) | MEDIUM | New page candidate — rich paid-client thread, only partially transcribed in raw/people/annie-ulmer/escort-messages-chatgpt-export-2025-08.md; needs the full message export before writing a page |
| Jason thread ((516) 589-0711, 2020-06-10/17) | MEDIUM | New page candidate — "Lily"/"Annie" dual-alias client, boyfriend-filming negotiation; same status as Nabeel above |

## Carried over from old repo (raw/ present, synthesis pending)

| **File** | **Priority** | **Notes** |
| --- | --- | --- |
| raw/self/dox-md/tom_kristin_master_dossier.md | MEDIUM | Expand wiki/people/tom.md; add Kristin people page |
| raw/self/dox-md/MAX_PRIME.md | MEDIUM | Populate wiki/work/tech/max-framework/overview.md |
| raw/self/dox-md/ulmer_dui_megadoc.md | LOW | Annie DUI detail — check for gaps vs existing pages |
| raw/self/dox-md/The-Eli-incident-investigation.md | LOW | Check against wiki/timeline/events/ |
| raw/self/dox-md/Annie 10-Year… Forensic Report.md | LOW | Supplement wiki/mind/synthesis/attachment-trauma-bond if gaps |
| raw/self/message-csv/MASTER_DUMP_PART_1_ARCHAIC.csv | RESOLVED (2026-07-18) | Misnamed — 124k rows but only 1 in 2011, nothing 2012–14; earliest real text 2015-11-12. Has NO pre-2015 content. Corpus genuinely starts ~Nov 2015. Do not re-attempt for pre-2015; overlaps master dump for 2015–19. |
| raw/self/message-csv/ (remaining CSVs) | LOW | Thread-specific slices |

## Re-synthesis queue (lint 2026-07-11: 22 oversized pages)

Superseded 2026-08-08: the page-size budget was raised to 40 KB because depth is the standing directive (STYLE_GUIDE.md substance rule 1). Size warnings are advisory and are not a backlog item. Worst offenders: ai-collaborative-analysis (21 KB, still contains v1 agent chatter in frontmatter), forensic-methodology (20 KB), context-core (14 KB), youtube-watch-history (14 KB).

## External acquisitions

- Twitter @danfrank: yearly wiki pages up at wiki/self/twitter/ (originals + quote-tweets). Spreadsheet 2013-08-17–2026-04-07 complete. 2009–mid-2013 and late 2026 still being scraped live onto the same pages. Official X Settings zip still welcome as a completeness check.

  - **MINING PASS 1 DONE 2026-09-02** (PR #239). `bin/mine-tweets` built; eight pages outside the twitter tree now reason from the archive — the 2010 move dated, the tattoos thesis falsified, the pre-2014 location window filled, the ten-year production silence measured. Details and the ranked next steps are in `LLM_HANDOFF.md`.

  - **MINING PASS 2 PENDING — the people pass is the highest-value remainder.** `bin/mine-tweets handle` splits 40+ handles into address/mention/RT-quote with year spans. Six handles with 6+ tweets have wiki pages and have not been mined: @ericjester (22), @danpolyak (21), @shane_brannan (19), @woodguts (17), @lo_weez (17, 2015–2020), @ulmdub (6). @alexisarmel (84) is mined only for the January 2010 tattoo. Then: the 2012→2024 politics arc, the October 2012 Sandy liveblog (no event page exists), the February 2013 Codecademy badges, and 2009 (165 originals, unmined).

- iMessage chat.db: bin/export-imessage-template.sh existed in old repo but never ran (needs Full Disk Access)

## Completed

- **2026-07-11 migration:** 562 MB raw/ archive (3,166 files), 261 wiki pages remapped into 9 domains, indexes rebuilt, lint clean (0 errors). Old repo at `~/wiki project` untouched, now safe to archive.

## DanAnnie dossier corpus (discovered 2026-07-11 — page audit)

| **Item** | **Priority** | **Notes** |
| --- | --- | --- |
| Full synthesis of 6 unread DanAnnie dossiers (raw/self/dox-scan/: MasterRecord_FINAL, TenYears_WithAmendments, TheoryOfEverything_Updated, CompleteRecord_Final, CompleteAnalysis_Final, MoralAnalysis_SFW; "2"-prefixed files are byte-identical dupes) | DONE | 2026-07-13: read into annie-ulmer.md (full rewrite), then propagated into eli-incident, eli, attachment-model, conflict-architecture, attachment-trauma-bond, dec-2025-spike, group-chat-closure, 2015-2016-annie-relationship-start, march-2026-terminal-phase, au-zaatar, suzanne-frank, tuquick, tom, 2025-collapse. Remove this row on next queue cleanup pass. |
| Locate compiled full-record files: Dan_Annie_Full_Text.txt, 1_year_triad_logs.csv, 7_days_212_logs.csv, 14_day_212_logs.csv | MEDIUM | Cited by dossiers, absent from disk — likely on the machine where the dossiers were generated. Drop into inbox/ when found |

## Google Drive DOX corpus import (2026-07-13, in progress)

- User pointed at a Google Drive folder (RTF:TXT / MD / CSV subfolders) mirroring raw/self/dox-scan + dox-md + message-csv. RTF:TXT and CSV subfolders are ~fully duplicate of existing raw/ (confirmed by filename diff — no action needed). The MD subfolder (+ a "New Folder With Items" nested subfolder) contains ~48 files NOT already in raw/self/dox-md/ — genuinely new chat exports.

- Background agent dispatched to download all 48 new files verbatim into raw/self/dox-md/ (mechanical only, no synthesis). Check `git status --short raw/self/dox-md/` for what landed; check for `.gdrive-fetch-failures.txt` in repo root for any that failed.

- **DONE 2026-08-26.** Most of this cluster was already synthesized into `wiki/work/bfs-foods.md` in an earlier pass (Anita/Brandon/Timmy/Marty, PA §260.3, the POS fraud vector, the Timmy precedent) — the note above was stale by the time this session found it. Two files remained genuinely unmined: `Little Caesars retaliation timing concerns (1).md` (the fuller export, 1920 lines vs. 787) and `Reverse chronological context upload.md`. Read both to exhaustion: they are the self-correcting multi-session thread the note anticipated — a model catching its own escalating drift (chaotic-franchise-incompetence read → orchestrated-campaign read) across three chained sessions, and Dan's own mid-session correction that he did **not** explicitly refuse the $50 and the Monday hours cut preceded the demand conversation entirely, not followed it same-day. Added as a `> **CORRECTED [2026-08-26]:**` block on bfs-foods.md, with the Legal posture section's "textbook retaliation" claim walked back accordingly — the underlying wrong (an illegal off-books demand, a real hours cut) survives; the clean causal shape does not. Hypothesis A/B both remain live per the source, consistent with the page's existing treatment.

- **CHECKED 2026-08-26, no new facts.** `wiki/people/jacob-bacharach.md` already mines this file exhaustively — verified by grepping the raw source for the page's four open gaps (the page 227-228 book-title contradiction, whether Dan ever told Bacharach about the house, the Suz-sold-May-2020 date, the Nathan Bacharach death-date discrepancy). All four remain genuinely open in the source too; none has a resolution sitting unmined. Negative result recorded rather than silently assumed.

- **CHECKED 2026-08-26, already done.** `wiki/interests/rock-irrelevance-thesis.md` already cites and is built from this file (`raw/self/chats/The 2nd most famous 'Jimmy Pop' in Pennsylvania .md`) in full.

- **DONE 2026-08-26.** `"___ The J6 Chat copy.md"` is byte-identical (md5) to the already-cited `raw/self/chats/j6-chat.md` — no action needed. `"___ The J6 Chat.md"` (no "copy") is the same chat exported further — 126 additional lines where Dan uploads a Babbitt-shooting FOIA package, a USPP operational-planning FOIA, the Select Committee report excerpt, and the public J6 timeline, and the model reads each against the hypothesis. New subsection "The FOIA-document pass" added to `wiki/mind/synthesis/political-psyops.md`, explicit that every specific claim is the model's summary of an uploaded document not yet independently verified against a primary source in `raw/`.

- LOW: "Attachment System Collapse.md", "Analyzing manipulation and ethical intent in data.md", "Interpersonal manipulation...toxic dynamic.md" (+ dup), "Honest assessment...", "Uncompromising analysis...", "Reassessing decade-long relationship dynamics...", "Ethics of leaving without communication.md" — more Annie-gaslighting-mechanism report iterations; spot-check for any NEW finding not already in annie-ulmer.md/attachment-model.md/conflict-architecture.md (most content looks like re-derivations of what's already synthesized — the "91 love-to-request" / "44 crisis pivots" counts are PRIOR/lower than the final dossier's 187:4 and 44 already on the page; treat final dossiers as authoritative per their own supersession claims).

- LOW: MAX/bunker-core chats ("_Psychological Warfare and Social Engineering.md", "_Openclaw Agent Setup and Data.md", "MNEME_BUILDKIT_v02.md", "Max.md", "stylometric_analysis.md", "agent.md", "_Antigravity's Test and Naming Ceremony.md", "Fake hacker dashboard scripts.md") — route to wiki/work/tech/max-framework or mind/concepts/exocortex.

## Google Drive — DANMODEL folder (spotted 2026-07-20, MINED same day — see wiki/work/tech/danmodel.md)

- DONE 2026-07-20: new page wiki/work/tech/danmodel.md — a working voice-cloning ML pipeline (39,378 stimulus-response pairs extracted from Dan's own message corpus; Jaccard baseline + TF-IDF RAG generator using a CATO_COMPACT self-voice persona prompt; a blind LLM-judge eval harness whose results were never found on disk). raw/self/danmodel/ holds extraction_summary.txt, PIPELINE_NOTES.md (faithful architecture transcription — the 5 .py scripts could not be safely byte-transcribed, see that file's own note), and reaction_pairs_heldout.jsonl (4,570 rows, verbatim, verified). The 34,808-row train.jsonl (~16MB) exceeded this session's Drive download tool limit and was not filed. `PHENOMENOLOGY_LENS.md` and `CONTEXT_CORE_EXPANDED (1).md` in that same Drive folder were NOT checked this pass (assumed duplicates per naming, per the general pattern already established for this folder tree) — worth a quick hash/diff check in a future pass if anyone wants certainty.

- Broader 2026-07-20 Drive browse (list_recent_files + folder crawl of DOC SCAN/**DOX/~~DOCS, TEXTS, Semantic Location History) found nothing else new — TEXTS folder matches already-filed raw/self/message-csv/ exactly (imessage_7244346811, imessage_2124702449, ANNIETEXTS, imessage_7249204125); Location History/Chrome/Search year-folders match the already-ingested Google Takeout mirror. The NEW LOADER/DOX/MEMORY folders were already confirmed fully triaged in prior sessions (see LLM_HANDOFF.md).

- LOW: misc pinned chats / one-offs ("_Queen-Goddess's Digital Orbit.md", "_Freeskiing's Early 2000s Cultural Revolution.md", "_Delicate Situation, Cognitive Prosthetic.md", "_Photo Thread PT II.md", "_Two Options, Choose Wisely.md", "_Deconstructing a Chaotic 24 Hours.md", "_Dan Frank's Digital Forensic Inventory.md", "Creating robust video essays from scripts.md", "_The Waiter's Visible High.md" [likely dup of dansynth/TheWaitersVisibleHigh.md], "_Grok's Nudity-Fueled Carnage Exposé.md", "_Lexie's Unpleasant Basement Descent.md", "u.md", "Extracting Sent and Received.md", "_✧✧ DANFRANK-ISM'S ✧✧ Pinned chat.md") — read and route on next general enrichment pass; none flagged as high-priority on title alone.

## Google Drive DOX2 corpus import (2026-07-13, second folder, in progress)

- User shared a second, larger Drive folder (root id 1aoKUSaqRiUWbRl0n8B0dxzUBK_yEjHHa). Structurally different from the first: 10 top-level files + 12 subfolders. Confirmed the user wants EVERYTHING archived, including location history and Chrome browser history, not just narrative text.

- Background agent dispatched to mirror the Drive folder tree into `raw/self/google-drive-export/` verbatim (docs → .md via read_file_content; JSON/binary/images → base64 download + decode). Priority order given to the agent: (1) ~35 modest docs (NEW LOADER, FULL DATA STACK, LOGS, suz, Gemini Chats/heart.pdf, iMessage Analysis Toolkit, top-level files), (2) ChatGPT 4o History subfolder (real ChatGPT conversation exports, genuinely new corpus vs. the existing Gemini-only chat archive), (3) art-reference images, (4) location-history year-folders (Semantic Location History-1, Semantic Location History 2, Location History (Timeline)/Semantic Location History — monthly JSON files per year, 2016 onward), (5) Takeout/Chrome (Bookmarks + a ~71MB History.json, likely to be skipped as oversized) and Takeout/Search.

- Check `raw/self/google-drive-export/` tree once the agent completes; check for `.gdrive2-oversized-skipped.txt` and `.gdrive2-fetch-failures.txt` in repo root for anything that didn't land.

- HIGH: Once landed, prioritize synthesis/routing for: `NEW LOADER/OMNI_FORENSIC_DOSSIER.md` and `NEW LOADER/THEORY OF EVERYTHING 31 MAR` (a dated Annie dossier variant not yet cross-checked against the final MasterRecord/TenYears dossiers already synthesized into annie-ulmer.md — verify it doesn't contain any NEWER superseding facts); `FULL DATA STACK/Full Personality Profile` + `SEXUAL PROFILE` + `Pattern Mapping` (cross-check against wiki/mind/profile/ cluster for gaps); the ChatGPT 4o History JSON exports (a parallel AI-chat corpus to the existing Gemini activity — may contain material not covered by wiki/self/chats/).

- LOW/ARCHIVAL ONLY: location-history JSON and Chrome History.json — explicitly archived per user request but NOT expected to be synthesized into narrative wiki pages; if ever needed for a places/ or self/location-history.md enrichment pass, mine from here.

## Enrichment backlog (2026-07-13, from user directive — "thousands of trivial missing things")

- HIGH: chats/ pages cleanup — remove /tmp paths + HTML-comment agent chatter; rewrite to prose (gemini-02/-18/-21 worst)

- HIGH: people primary cast depth pass (rick-frank, tom, eli, anita, fran-coldren...) — mine LIFE_EVENTS_CALENDAR + message CSVs per person, per the annie.md standard

- MED: GRIPNOTIC/MOGZART full release catalogs (needs SoundCloud/Spotify export ingest — ask user for exports)

- MED: places/ expansion: 12 Bryer Ave, Uniontown, NYC chapters, Ohiopyle, Seven Springs, Au Za'atar location page

- MED: health/ expansion: withdrawal-episodes page, somatic record, sleep/vampire schedule

- MED: timeline events that deserve articles: 2015 Combos arrest done; candidates from calendar — Fran deathwatch (2018), freezer phone, J6 watching, Feb 2025 return drive

- LOW: work/tech: Bunker Core page, MAX interview system page (CATO §PROJECTS has specs)

- LOW: dedupe `related:` lists created by the 2026-07-13 link rewrite (some pages now link forensic-method twice)

- MED: "Target G" — VERIFIED 2026-07-20: this item is stale. The Jan 2026 Suzy-call/blackout male is already fully documented in prose on wiki/people/annie-ulmer.md ("Target G (January 2026)" section, incl. the "Caitlin's husband" identity clue and the unresolved Tuquick-identity question) and wiki/people/suzanne-frank.md ("The 'Suzy' call" section). No further ingest needed.

- HIGH: DANSYNTH full-depth ingest — the scrape covers ~5%; mine raw/self/dansynth/DANSYNTH.txt session-by-session (maxwellhill, photo-archive, Chappelle/Ket, Valeria JSON audit) for the remaining facts; resolve flagged contradictions (Fran death date, Bacharach house, Morley Seattle thread). Franki/Katie order RESOLVED 2026-07-13 (summer 2013, per wiki/people/franki-faris.md).

- MED: mine raw/people/valeria/message_1.json directly (4,884 IG msgs 2022–2025) for dated milestones (departure date to Chile, gap analysis, 2024–25 frequency) and raw/self/dansynth/TheWaitersVisibleHigh.md remainder (Sergio mediation transcript → possible sergio entity page)

- MED: raw/self/dox-scan/FULL TWITTER ANALYSIS.txt (~500 lines, year-by-year 2009-2019+ forensic Twitter analysis) — only spot-checked so far (Alexis/Orlando era, @Lo_weez resolution 2026-07-14); a full pass would likely surface more dated social-graph and voice-evolution detail per year

## ChatGPT conversations.json export (2026-07-20, first pass)

- Located and downloaded the operator-referenced ChatGPT export (`5e1e05d7-.json`, 375 conversations, 2022-12-10 to 2025-07-01) via direct upload after Drive's MCP tools proved too size-limited (download_file_content times out >5MB; read_file_content mangles JSON with markdown-escaping and truncates at ~900K chars). Full 375-conversation title/date/msg-count index built at scratchpad `conversations_index.tsv` (not committed — regenerate from the uploaded json if needed).

- Sampled and mined ~10 of 375: "Mom Info Logged" (confirmed FULLY DUPLICATE of already-ingested facts — Danielle/Franki/Alexis/Annie dating chronology, Fran/Arnold Palmer/Ira Coldren biography — no new signal, strong confirmation of wiki completeness on this thread); "Relationship Breakdown Summary" (2025-04-27, genuinely new — mined into new page wiki/timeline/periods/feb-apr-2025-return-and-rupture.md, filling the Feb-Apr 2025 gap between the Jan 2025 affair discovery and the Aug-2025-onward terminal-phase record); "Whisk AI Prompt Injector" / "Whisk Emergency Fabric Design" (both low-value tangents, NOT related to any fabricated-evidence tool despite the title similarity — false lead, no wiki action); Franks Auto/Suboxone Buzz/Zalgo meltdown/Caregiver Pay (skimmed, appear to restate already-documented facts, not deep-read).

- HIGH: "Camming Career Review" (2025-06-07, 22 msgs) — extracted to scratchpad, not yet read/cross-checked against erotic-architecture.md / arrangement-history.md.

- HIGH: "Babbitt Shooting Psy-Op Debate" (2025-06-15, 22 msgs) + earlier "Ashli Babbitt Sheepdipped." (2023-03-16) + "Jan 6 Intelligence Evidence." (2023-04-03, 31 msgs) — extracted to scratchpad, not yet cross-checked against wiki/self/chats/j6-chat.md and wiki/mind/synthesis/political-psyops.md; this ChatGPT thread predates the existing Gemini-based J6 material by ~2 years and may be the original source.

- **DONE 2026-08-26 (partial — one file located).** Only one of the cluster's named conversations exists as a full file in `raw/`: `raw/self/dox-scan/DAN IDEAL FACE.rtf`. It resolves what the project is: a literal, quantified physical "ideal type" specification — ~20 attributes (face shape, jawline, eyes, nose, lips, hair given as an RGB hex range) each scored 1–10, plus a five-item named "vibe" archetype scoring (Ethereal Addict Chic, Post-Soviet Waif, etc.), evidently built as an AI-image-generation prompt spec. Added as a new section on `wiki/mind/concepts/erotic-architecture.md` ("The quantified ideal — engineering desire itself"), deliberately drawing no line from the generic, unnamed specification to any real person documented elsewhere in the corpus. The other ~11 titles in the cluster ("Facial Proportions Analysis," "3D Face Model Specs," etc.) are activity-log titles only — no corresponding full conversation export exists in `raw/` to mine further.

- MED: "Interpersonal Analysis Request" (2025-04-26, 73 msgs) and "Conflict Analysis Framework" (2025-04-28, 8 msgs) — likely adjacent/overlapping with the already-mined "Relationship Breakdown Summary"; check for additional non-duplicate detail.

- MED: "Breakup Brain Dump" (2025-05-24, 26 msgs), "Personality Breakdown IRL" (2025-06-01, 32 msgs), "Emotional Blowout Breakdown" (2025-06-07, 13 msgs) — later 2025 relationship/identity content, unread.

- LOW: ~180 early conversations (Dec 2022 - Oct 2023) are overwhelmingly generic political/history/ideology discussion (Trotsky, Bolshevism, Capitol riot hearings, Opie & Anthony, Napoleon, French Revolution, MBTI/INTP typology, election-probability modeling) — same register as already-documented political-psyops.md and the profile/ cluster; spot-checked several titles against existing pages, no contradiction found, low expected marginal yield. Deprioritized for a full read; worth a title-level rescan only if a specific gap is later identified.

- LOW: "Franks Auto Supermarket History" (x2), "Uniontown..." cluster (x4), "NYC..." history cluster (x6, April 2024) — local-history trivia conversations, low biographical yield expected, not yet confirmed duplicate.

- Raw archival: the full source export is now saved at `raw/self/chatgpt-export/dfrank-chatgpt-conversations-2022-2025.json` (375 conversations, valid JSON, 9.5MB) plus two extracted single-conversation text files for the conversations actually mined (relationship-breakdown-summary-2025-04-27.md, mom-info-logged-2025-05-23.md). To extract any other conversation by id or title, parse the full json (see `conversations_index.tsv` regeneration note above) — do not re-fetch from Drive, its MCP tools cannot handle this file size.

- NOT YET LOCATED: the larger ~35.7MB `dfrankconversations.json` companion export (same title seen repeatedly in Drive search results, likely a superset or different account/date-range) — the operator uploaded only the ~9.5MB `conversations.json`-class file; ask for the larger one directly if a fuller pass is wanted, since Drive's own MCP tools cannot fetch it (session-expired on every attempt, confirmed 4x on different file IDs of the same size class).

### ChatGPT export — 2026-07-20 follow-up

- "Babbitt Shooting Psy-Op Debate" (2025-06-15) checked against j6-chat.md/political-psyops.md: CONFIRMS the already-documented "Operation Wildfall"/hybrid J6 thesis (same 95%-real/narrative-weaponization verdict) rather than adding new claims — but establishes the thesis is 7 months older than the Gemini codification date and was independently rederived on a second AI platform. Added as a chronology note on political-psyops.md. |- [x] "Camming Career Review" (2025-06-07) checked: an image-analysis conversation (Dan uploaded cam-show screencaps not accessible as text) that produced only AI flourish/pseudo-academic prose with no concrete new facts (no names/dates/numbers) — lower value than the title suggested. No wiki action.

## [2026-08-09] extreme-sports direct-drop ingest — DONE

- Source filed: `raw/self/captures/2026-08-09_122727_extreme-sports.md`

- Pages written: extreme-sports, matt-kraus, nathan-king, tancredi-calabrese, tom-wallisch

- Identity correction: tan-calabrese → tancredi-calabrese split handled

- Gates clean: wiki-lint 0 errors · wiki-connect check 0 errors · wiki-climb check 0 errors, 0 stale

## [2026-08-20] August severance ingest — DONE, with named follow-ups

- Sources filed: `imessage_export_2124702449_20260820.csv` (6,495), `imessage_export_7248123683_20260820.csv` (97), `raw/self/audio/2026-08-16_Morgantown_St_call-recording.m4a` + README, `raw/self/analysis/2026-08-18_forensic-analysis-morgantown-call.md`

- Both exports read in full; 2 pages written, 24 updated; gates clean

- **HIGH: transcribe the 927 s audio** and file the transcript beside it — every quotation from it in `wiki/` is currently T2

- **HIGH: verify whether the email to Annie's parents was sent** (sent-mail folder). Open `CONTRADICTION` on `august-2026-morgantown-call`

- **HIGH: export the Ally thread 2026-08-13 → 20** — still missing, now blocking the slot-refill control added to `ally-and-dan-love-as-destiny`

- **MED: sweep pre-July-2026 corpus for third-party-handle episodes** — three known, all found by register alone, no detector exists

- **MED: recover the three drug-screen images** (2026-08-14 13:17/14:08/14:11) behind `mind/concepts/document-fabrication`

- **MED: the "molesting" video and the Oct 2019 MMF video** — both circulating as leverage, neither examined by anyone writing this wiki

- Note: `annie_metadata_24h.csv` and the 2026-08-09 212 export cited by `august-2026-unmasking` are **still** not in `raw/` (standing since 08-09)

## [2026-08-20] group-chat capture + accusation adjudication — DONE, one gap created

- Filed `raw/people/captures/2026-08-20_group-chat-retraction-and-the-uncleared-name.md`

- Gap closed: the unnamed act in the Aug 19 final hour has a referent

- Adjudicated the "made her fuck guys for drugs" accusation on `arrangement-history` — false as stated, three limbs tested, falsifier named

- **~~HIGH: export the three-party group chat (Dan / Annie / +1 724 812 3683).~~** **CLOSED — Annie moratorium 2026-08-23.** Not exported. The two findings keep resting on the transcribed screenshot and the "Yesterday 6:33 AM" date stays an inference, labelled as one.

- **~~MED: the arrangement record is almost entirely Dan-side correspondence.~~** **CLOSED — Annie moratorium 2026-08-23.** The falsifier stays named and stays unaddressed; an Annie-voice account is not to be acquired. Original note: named as the live falsifier on `arrangement-history`. An Annie-voice account of any documented encounter would move it more than any further Dan-side volume can.

## [2026-08-21] portal lost-update — one page recovered, the cause not yet established

- **HIGH: establish how commit ff905fc stripped 56 typed-edge claims.** `wiki/people/annie-ulmer.md` was saved from the portal on 2026-08-21 with a snapshot of the **08-13** page, deleting three later passes, the infobox and every `type:`/`claim:` on 56 edges. Recovered the same day. The portal's `src/wiki/publish.ts` says `fmRaw` was introduced precisely to stop the frontmatter rebuild from deleting claims, so either that path was bypassed or the browser was running pre-`fmRaw` code against a stale snapshot. Two frontmatter dates moved *backwards* in the same commit, which is the signature to look for on any other page. **Until it is understood, assume it can happen again to any page edited in the app.**

- **MED: sweep every page for the same signature.** A save whose `date_modified` is older than the commit before it, or whose `connections:` block has `- page:` entries with no `type:`. The connect gate catches the second; nothing catches the first.

## [2026-08-31] intake ledger, first export — INGESTED

The ledger had been running on the phone since 2026-08-30 while `intake/events.jsonl` sat tracked at zero bytes on `main`. The export covering that night was filed this pass.

| **Item** | **Status** | **Notes** |
| --- | --- | --- |
| `intakeledger20260831.jsonl` (17 events, 4 units) | **INGESTED 2026-08-31** | Merged into `intake/events.jsonl` by set union on event id, which is the documented merge and is now order-safe. Findings written onto [[wiki/health/cocaine]] and [[wiki/health/chemical-architecture]]; per-unit archives backfilled to `raw/health/intake/`. Three `bin/intake` defects fixed on the way in — see `log.md`. |

**Standing, for the next export.** The ledger is not an inbox item and does not arrive through `inbox/`: it is written from a phone into `intake/events.jsonl` through GitHub's contents API, so most of the record will already be in the repo before any session sees it. What a session owes it is the *reading* — the merge is only the mechanical half. Re-run `bin/intake capture` after any pass that finds closed units (the portal does not file the `raw/` archive), and read `intake/SUMMARY.md`'s coverage line before quoting any figure from it.

**One figure to never quote.** `bin/intake report` prints a per-unit `Rate of consumption ... g / day`. It extrapolates the unit's quantity across 24 hours from however long the unit lived, so a unit consumed in an evening reports a daily rate more than double what was consumed that day. It is not a daily figure and no page may cite it as one.
