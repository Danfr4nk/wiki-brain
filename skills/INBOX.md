# Skill Inbox

Unvalidated observations and candidate instructions. This is deliberately append-oriented: do not promote a lesson by deleting the evidence that produced it.

## Entry template

### YYYY-MM-DD — short title

- **Observed during:** task / PR / incident

- **Surface:** files, commands, or subsystem

- **Observation:** what actually happened

- **Candidate invariant:** what appears to remain true

- **Candidate instruction:** what a future agent should do

- **Validation:** evidence needed before promotion

- **Status:** inbox | provisional

## Seed candidates

### 2026-08-30 — Persistent cross-agent learning loop

- **Observed during:** creation of the `skills/` section

- **Surface:** all non-trivial repository work

- **Observation:** repository instructions and handoffs preserve process and current state, but reusable lessons can otherwise remain trapped in individual model sessions.

- **Candidate invariant:** durable operational knowledge needs a canonical repository location independent of the LLM or agent that discovered it.

- **Candidate instruction:** capture reusable lessons in `skills/`, route future agents through `skills/INDEX.md`, and promote only validated instructions.

- **Validation:** multiple future agents can discover, follow, revise, and reuse the same skill without relying on the original conversation.

- **Status:** provisional

### 2026-08-30 — A generator's own output is not the published object

- **Observed during:** writing `tests/test_wiki_skills.py` for the skills database

- **Surface:** `bin/wiki-skills check`; applies to every generator here that gates its own output — `bin/wiki-digest`, `bin/llm-publish`, `bin/wiki-plain`

- **Observation:** the gate applied the standing-directive check to the page it had just *rendered*, not to the file on disk. The two are identical only when the drift check above it passed. A hand-edited page that named a person under the directive would have been reported as "the page is behind the database" — a true statement, and not the one that mattered. The check passed for the right reason only by accident of ordering.

- **Candidate invariant:** a check on generated output must run against **the artifact that ships**, not against a fresh render of it. The render proves what the tool *would* publish; only the file proves what is published.

- **Candidate instruction:** where a gate asserts a property of a generated file, assert it on the file's own bytes as well as on the render, and make the test assert the error *message* rather than the exit code — a test that only checks `!= 0` passes when a different error fires first, and will keep passing after the property stops being checked at all.

- **Validation:** `tests/test_wiki_skills.py::TestMoratorium::test_the_gate_catches_a_hand_edit_that_names_her` fails if either check is removed. Generalises `repo/change-safety.md` ("validate behavior, not merely successful commands") from HTTP 200 to a second case; promote after it catches a second instance in another generator.

- **Status:** provisional

### 2026-08-31 — A secret's absence must fail whatever the secret was for

- **Observed during:** diagnosing "the wiki takes up to an hour to reach the site", reported as the site being generally unreliable

- **Surface:** `.github/workflows/notify-portal.yml` here; `.github/workflows/deploy.yml` in `caakehorn/home`; the same shape is claimed for `ANTHROPIC_API_KEY` in `sage-drain.yml` by notify-portal's own header, unverified

- **Observation:** `notify-portal.yml` guarded its dispatch with `if [ -z "$TOKEN" ]; then echo notice; exit 0; fi`, deliberately, with a written rationale: a workflow that fails red over a secret nobody set is one people learn to ignore. `PORTAL_DISPATCH_TOKEN` then stopped being present on 2026-08-28 and the job reported **success eighteen consecutive times while sending nothing**, including runs where its own `What moved` step had counted a changed page. Confirming it needed the *receiving* repository's Actions log — `caakehorn/home` recorded no `repository_dispatch` for three days — because on this side there was no signal at all. The reported symptom was not "a workflow is broken" but "the whole site feels janky", which is what a silent hour of latency looks like from outside.

- **Candidate invariant:** the test is not whether a secret is set, it is **whether the job still accomplishes what its name claims without it**. `notify-portal` exists only to send the dispatch, so a missing token means the job did not happen and must be red. `scripts/wiki-locks.mjs` in the portal is the correct counter-example and should not be "fixed" to match: it requires `WIKI_LOCK_PASSPHRASE` only when `wiki.locks.json` actually seals a page, and no-ops cleanly when it seals none — the secret is conditional there, so its absence is genuinely not a failure.

- **Candidate instruction:** when adding a secret-guarded step, ask what the job still does without the secret. If the answer is "nothing it is named for", exit non-zero and name the secret, the permission it needs and the repository it belongs in. Reserve the quiet-skip branch for work that is genuinely optional, and where it is used, make the run *say which path it took* — a skipped step and a broken step are indistinguishable in the Actions UI. Never let the fallback's existence (here, an hourly cron) justify silence: a backstop that has quietly become the only mechanism is the thing most worth being told about.

- **Validation:** promote after this catches a second live instance. The candidates are already named above — `deploy.yml`'s gate-verifier step was skipped on every run this repository has ever made with nothing on the run to say so, and its adjacent comment asserted a consequence ("the site deploys with the door unconfigured") that was simply untrue and had never been checked; `sage-drain.yml` is claimed to share the shape and has not been read. Both were touched on 2026-08-31 but neither has yet *failed* in a way this rule predicted.

- **Status:** inbox

### 2026-08-31 — A tie-break that is arbitrary is a tie-break that will be wrong

- **Observed during:** filing the intake ledger's first portal export

- **Surface:** `bin/intake` `merge_lines`; the same shape is claimed for `skills/registry/events.jsonl`, which is also an append-only JSONL log merged as a set union across devices — unverified

- **Observation:** `merge_lines` sorted merged events by `(timestamp, id)`. Three of the four units in the first real export were opened, logged and closed in a single tap, which writes three events carrying the same timestamp *to the second*; the id is a ULID whose low half is random, so the tie-break ordered a causal burst arbitrarily. The merged log stated that a unit had been closed before it was opened, and `bin/intake check` rejected it. Nothing about the failure said "ordering" — the four errors read as events against unknown units, because a `unit_created` sorted after its own `intake_logged` means the unit does not exist yet at that line.

- **Candidate invariant:** where a total order is imposed on records that carry a causal relationship, the sort key must encode that relationship above any value chosen for uniqueness. A random tie-break is not neutral: it is a uniform draw over the orderings, most of which are wrong, and second-resolution timestamps make ties the normal case rather than the rare one.

- **Candidate instruction:** when sorting an event log for merge, rank by what each event *does* to the entity (created → mutated → closed) before falling back to the id, and keep the id in the key so concurrent devices still converge to identical bytes. Test with a burst whose ids deliberately sort against causal order — a fixture whose ids happen to agree with it passes either way and proves nothing.

- **Validation:** `tests/test_intake.py::TestMerge` — four cases, including a scrambled burst and an end-to-end merge that must survive `check`. Promote after this catches a second instance; `skills/registry/` is the named candidate, and `bin/wiki-skills` should be read for the same tie-break before it acquires two pushers in the same second.

- **Status:** inbox

### 2026-08-31 — A write path that skips the tool skips everything the tool also did

- **Observed during:** the same pass

- **Surface:** `bin/intake` `close_unit` vs. the portal and ボスの部屋 write paths; the same shape applies to any repository interface writing through GitHub's contents API rather than through `bin/`

- **Observation:** `bin/intake close` does two things — it appends the `unit_closed` event *and* files the unit's immutable report to `raw/health/intake/`. The portal and ボスの部屋 write events straight to `intake/events.jsonl` through the contents API, so they perform the first and not the second. Every one of the four units in the first export was closed and had no archive entry at all, and nothing anywhere reported a problem: `bin/intake check` validates the log against the projection, and the capture is in neither. `intake/README.md` describes the four interfaces as "four interfaces over one code path", which is true of the arithmetic and not of the side effects.

- **Candidate invariant:** when a second interface writes the same data store directly, it inherits the store's format and none of the writing function's side effects — and the side effects are exactly what no consistency check covers, because they live outside the data being checked.

- **Candidate instruction:** for each side effect a CLI write performs beyond the append, either give it a backfill command (`bin/intake capture`) or make the gate assert it. And where an artifact's value rests on *when* it was produced, a backfilled copy must say it was backfilled — the archive here carried "generated once at close, never revised", which would have been false on every file the backfill wrote.

- **Validation:** `tests/test_intake.py::TestBackfilledCaptures` pins the provenance line in both directions. Promote after a second interface-side-effect gap is found; the gate does not yet assert that a closed unit has a capture, which would be the stronger fix and is deliberately not done here — every unit closed before `bin/intake capture` existed would fail it retroactively, which is a red gate for history rather than for a defect.

- **Status:** inbox

### 2026-09-02 — A claim of absence needs a deliberately over-broad pattern first — **PROMOTED to ****`corpus/vocabulary-drift.md`****, 2026-09-02**

- **Observed during:** mining the @danfrank twitter archive for the production identity's public arc

- **Surface:** `bin/mine-tweets timeline`, `bin/mine-messages grep`, `bin/text-metrics` — any instrument used to establish that something is *not* in a corpus

- **Observation:** a narrow pattern (`soundcloud|ableton|mixtape|sloppp|mogzart|gripnotic|…`) returned zero hits for 2017 through 2025 and I was one step from writing "eleven years of public silence" onto `wiki/interests/music/overview`. Re-running with a deliberately over-broad vocabulary (adding `remix|mix|dj|producer|track|beat|studio|bass|edm|mastering`) returned hits in 2017, 2022 and 2024 — every one a false positive on reading (a double **bass** at a concert, "**beat** to death with a lead pipe", the "don**bas**" region, Biden "**beat** him", "**track** record"). The zero survived, but the *boundary moved*: the real last post is 7 March 2016, not somewhere in 2016, and the run is ten years rather than eleven. A narrow pattern that returns zero cannot distinguish "he never said it" from "he never said it *that way*", and it fails silently in the direction that makes the finding look stronger.

- **Candidate invariant:** a positive claim is supported by the hits you found; a negative claim is only as good as the hits you would have found. The two need opposite search strategies, and the absence claim needs the expensive one.

- **Candidate instruction:** before writing that something is absent from a corpus, re-run with a pattern wide enough to produce false positives, and **read every hit individually**. If the broad pattern returns nothing at all, the pattern is probably still too narrow. State the window's coverage alongside the zero — here the 2017–2025 window is spreadsheet-complete, which is what makes its zero a real zero rather than a retrieval gap, and the 2010–2012 counts are live-scrape floors where the same zero would have meant nothing.

- **Second instance, same day, and it generalises the rule:** mining the politics arc a few hours later, a pattern built from 2012–2024 political vocabulary (`trump|biden|obama|democrat|…`) returned **0.0% for 2026**. 2026 is not apolitical — it contains "EVERYBODY🙏HATES🙏ISRAEL🙏", a read on Curtis Sliwa's "antizionist credentials and… the new Tucker lane of nat con populism", and "It's Irish Zionism". None of those words were in the pattern. The corrected figure is **23.1%**. I was one edit from publishing "the politics sicko went silent in 2026", which is false and would have been the most quotable claim in the pass.

- **The stronger rule this implies:** the first instance looked like *a pattern too narrow*. This one is not narrowness — it is **drift**. A vocabulary changes across a seventeen-year corpus, and a keyword list built from the middle of that span reports the ends as empty. The failure is worst precisely where the corpus is most interesting: a year whose subject matter is *new* is the year a fixed pattern is least able to see. Any per-year table over a long corpus is exposed to this, not just absence claims.

- **Validation:** reproducible in both directions — `bin/mine-tweets timeline '<narrow>'` vs `'<broad>'` disagree about 2017/2022/2024 for music, and about 2026 for politics. Two instances now, and both PROTOCOL §3 tests pass. **Still not promoted, deliberately:** both occurrences are the same author, in the same session, on the same corpus, which is not the independent confirmation §3 is asking for. Promote when it catches someone else, or a different corpus — `bin/mine-messages` over the 196,399-message dump is the obvious next place, and `wiki/interests/music/overview` already carries several absence claims drawn from it that were never checked this way.

- **Third instance, and the one that promoted it:** the politics table built from the second instance was **published** on `wiki/mind/synthesis/2020-left-turn` claiming "two steps, not one" — a 2017 engagement step and a 2013–2016 off period. Both were withdrawn the same day: with era-appropriate vocabulary 2016 is 9.3% not 4.0% (so the "step" vanishes) and 2013 is 7.8% not 1.4%. A defect that reached a synthesis page is different evidence from a near-miss, and it is what moved this out of the inbox.

- **Status:** promoted → `skills/corpus/vocabulary-drift.md` (see `CHANGELOG.md`, 2026-09-02)

### 2026-09-02 — A self-entered profile field is testimony; the timestamp beside it is a record

- **Observed during:** dating the 2010 Brooklyn move against `wiki/self/facebook`

- **Surface:** `raw/self/facebook/facebook-ihatedanfrank/`; applies to any export that renders user-entered fields and system-generated ones into one table — Facebook, LinkedIn, dating profiles, `contacts.csv`

- **Observation:** `wiki/self/facebook` said "every field cross-checks against context-core" and was the wiki's strongest [DOC] anchor for the biographical spine. One field does not cross-check. `places lived: Brooklyn NYC from Jan 3, 2010` is wrong by eight weeks — the tweet archive has Dan in Florida through 28 February, posting "moving to brooklyn in 9 days" on the 20th. **The same export is right two rows up:** `work history` starts ishlab in March 2010, and `dan@ishlab.com` first appears in a tweet on 24 March. The export contradicts itself, and the split is not random — it is between what Facebook *recorded* (a relationship timestamp, a job entry, a birthday) and what Dan *typed into a form* at an unknown later date. Both render as plain rows in the same table with no visual difference, and `wiki/timeline/periods/2010s` had carried the January 3 date as one of two live candidates for six weeks because of it.

- **Candidate invariant:** provenance inside a single export is not uniform. A field's reliability tracks whether a machine or a person put the value there, and an export flattens that distinction away.

- **Candidate instruction:** before citing a profile export for a date, ask whether that specific field was generated or entered. `relationship … since November 28, 2015` can anchor a period page; `places lived: from Jan 3, 2010` cannot, and should be cited as testimony with the same weight as a memory. Where a self-entered field disagrees with a timestamped source, hold the contradiction on both pages rather than resolving by seniority — the export is still the better source for most of what it contains.

- **Validation:** promote after a second entered-vs-generated split is found in another export. `contacts.csv` and the dating-profile material are the named candidates; neither has been read for this distinction.

- **Status:** inbox

### 2026-09-02 — A transcribed source is not a mined source, and the tree makes it look finished

- **Observed during:** starting the tweet-mining pass

- **Surface:** any large export filed to `raw/` and rendered as `wiki/` pages — `wiki/self/twitter/`, `wiki/self/facebook/`, `wiki/self/youtube-watch-history`, the message corpora

- **Observation:** the twitter archive arrived as 2,525 originals in `raw/` plus eighteen dated yearly pages under `wiki/self/twitter/`, all `knowledge: derived`, all gates green, `queue.md` updated, hub written. Everything about it read as a completed ingest. But `grep -rln 'raw/self/twitter' wiki/ | grep -v '^wiki/self/twitter'` returned pages that mostly cited the *old 2019–2026 sample file*, not the archive — and the archive turned out to close a gap `wiki/timeline/periods/2010s` had declared in its own text, falsify the governing thesis of `wiki/self/tattoos`, and fill a window `wiki/self/location-history` recorded as "N/A". None of that is visible from the twitter tree, because a transcription page is complete *as a transcription* and no gate asks whether anything reasoned from it.

- **Candidate invariant:** rendering a source into `wiki/` satisfies every mechanical check while leaving step 4 of the INGEST operation ("write or update every relevant page") entirely undone, and the result is indistinguishable from a finished ingest by inspection of the tree.

- **Candidate instruction:** after filing a large source, run `grep -rln '<raw path>' wiki/ --include=*.md | grep -v '^<its own tree>'`. A count near zero means the source has been transcribed and not mined, whatever the queue says. Then read the target domains' **stated gaps** first — `wiki/timeline/periods/2010s` named the exact question the archive answered, in its own Gaps section, and that was the highest-value thing in the corpus.

- **Validation:** promote after this is run against a second transcribed source. `wiki/self/youtube-watch-history` and `wiki/self/facebook/posts` are the named candidates and have not been checked.

- **Status:** inbox

### 2026-09-02 — A silent no-op edit makes a commit message lie, and only the graph gate notices

- **Observed during:** writing tweet-mined typed edges onto `wiki/people/eric-jester.md`

- **Surface:** any scripted edit to frontmatter here — `python3 - <<'PY' … s.replace(...)`, `sed -i`, or an `Edit` whose old-string is approximate; `bin/wiki-connect check` is the detector

- **Observation:** the edge-adding script anchored on `- page: wiki/timeline/periods/full-sail-2008-2010\n    type: co-occurs`. The real types on that page were `instance-of` and `component-of`. `str.replace` found nothing, changed nothing, raised nothing, and the file was written back byte-identical. The script printed its success line, the prose edit in the *same* script succeeded, `bin/wiki-lint` passed, `bin/wiki-check` went green, and the pass was **committed and pushed** with a message describing edges that did not exist. It surfaced two commits later only because `bin/wiki-connect check` warned that the *other* end of the pair had no edge back.

- **Candidate invariant:** a scripted edit that no-ops is indistinguishable from one that worked, from everything except a checker that knows what the result should contain. The danger is not the missing edit — it is that the commit message, the log entry and the PR body all assert it happened, so the record is wrong in a way no later reader can detect by reading the repo.

- **Candidate instruction:** `assert old in s` before every `replace` in an edit script, one per anchor, and let it raise. It is one line and it converts a silent wrong record into a loud failure before the commit. Where an edit adds a **typed edge**, the assertion is not enough on its own: run `bin/wiki-connect check` and confirm the pair closed, because that is the only gate that knows an edge is missing. Note what did *not* catch it — `bin/wiki-lint`, `bin/wiki-check`, and reading the tool's own success output.

- **Validation:** reproducible — anchor a replace on a string absent from the target and the script exits 0 having done nothing. Promote after a second instance; the likely candidates are the same-shaped scripts used across this session's other page edits, which were asserted only where I happened to remember.

- **Status:** inbox

### 2026-09-02 — A generator whose output is gated must be in the gate's own generate list, or the gate is a trap

- **Observed during:** adding `wiki/meta/testimony-veracity.md`, the veracity ledger's public page

- **Surface:** `bin/wiki-check`'s `GENERATE` list; any tool that writes a page into `wiki/` and also gates on that page being current — `bin/intake page`, `bin/wiki-timeline generate`, `bin/wiki-plain report`, `bin/wiki-skills page`, `bin/wiki-testimony page`

- **Observation:** adding one page to `wiki/meta/` turned `bin/wiki-plain check` red with *"**`wiki/meta/readers-digest.md`** is behind the tree"*. That page is generated by `bin/wiki-plain report` from the tree and the git log, and its content includes a coverage denominator — so **any** pass that adds or removes a wiki page invalidates it. But `report` was not in `bin/wiki-check`'s `GENERATE` list, while the three other page-writing generators were. The failure is not the red gate; it is that the red gate names the *page* and not the generator, so a session that has never run `bin/wiki-plain report` gets an error pointing at a file it is told never to hand-edit, on a pass that has nothing to do with the plain-language layer. The file's own header already states the rule it was breaking: a generator that writes into `wiki/` has to run before `wiki-digest` counts pages and `llm-publish` copies them.

- **Candidate invariant:** the set of generators in `GENERATE` and the set of generated artifacts checked in `GATE` must be the same set. Where a gate can go red for a file no step in the chain regenerates, the chain has a trap in it — and it will be sprung by whichever unrelated pass happens to change the input, which is the pass least equipped to recognise it.

- **Candidate instruction:** when adding a tool that both writes into `wiki/` and gates on its own output, add it to `GENERATE` in the same commit as the gate, above `wiki-digest`. When a gate goes red naming a generated file you did not touch, look for the generator's own `report`/`page`/`generate` verb before assuming your change was wrong — and if the chain does not run it, that is the defect.

- **Validation:** reproducible — add any page under `wiki/` on a clean tree and `bin/wiki-check --check-only` goes red on `wiki-plain check` alone. Fixed for `wiki-plain report` in this commit. Promote after a second generator is found outside the list; `bin/wiki-gaps` and `bin/source-index` have not been checked for whether they write anything gated.

- **Status:** inbox

### 2026-09-02 — Every merge conflict in this repository is a generated-file conflict, and none of them should be resolved

- **Observed during:** two merges of `main` into one feature branch, four hours apart, on PR #243

- **Surface:** any branch in this repo open long enough for a content pass to land on `main` — `DIGEST.md`, `RECENT.md`, `OPEN.md`, `llm/**` (corpus, index, manifest, every touched page), `wiki/meta/{digest,recent-activity,readers-digest}.md`, `wiki/timeline/master-timeline.md`, `wiki/health/intake-ledger.md`, `wiki/meta/skills.md`

- **Observation:** merge 1 produced twelve conflicts, eleven of them generated. Merge 2 produced eleven, **all** of them generated. This is not luck: those files are committed derivations of the whole corpus, so *any* content pass on either side rewrites them wholesale, and two content passes always collide there. `llm/corpus.txt` alone is a 6.9 MB concatenation of all 494 pages — a three-way merge of it is meaningless work whose best possible outcome is identical to running one command. The trap is that git presents them exactly like a source conflict, and hand-resolving one produces a file that *looks* merged, passes `wiki-lint`, and is silently wrong until the next generator run overwrites it — or worse, doesn't, because the hand-merge happened to be self-consistent.

- **Candidate invariant:** a conflict in a derived file carries no information. The correct resolution never involves reading the diff, because the file's content is a pure function of inputs that both sides already merged cleanly.

- **Candidate instruction:** on any merge conflict here, first partition the list. For every generated path: `git checkout --theirs <paths>` (either side works — the content is about to be discarded), then `bin/wiki-check`, which regenerates all of them from source in the correct order, then `git add -A`. Resolve **only** the hand-written remainder by reading. On both merges here that remainder was at most one file (`LLM_HANDOFF.md`, where both sides had prepended a session entry and the resolution was "keep both, newest first"). Verify with `grep -rln '^<<<<<<< \|^>>>>>>> '` over `wiki/ llm/ *.md` before committing, because `--theirs` on a path git never marked conflicted silently does nothing.

- **The second-order finding, and it may be the more useful one:** a `git checkout` attempted mid-merge is refused with *"you need to resolve your current index first"* — which is a safety feature, not an error. Nothing is lost. Do not react to it by stashing or resetting.

- **Validation:** reproducible on demand — open any branch that touches `wiki/`, let one content pass land on `main`, merge. Two instances in one session. **Not promoted:** both are the same branch and the same operator, which is not the independent confirmation `PROTOCOL.md` §3 wants. Promote when a second branch hits it, which will not take long.

- **Status:** inbox

## An archive seam looks exactly like a change in behaviour (2026-09-03)

**Observed while writing narrative runs for ****`wiki/self/twitter/2009`****–****`2014`****.**

`skills/corpus/vocabulary-drift.md` covers one way a corpus lies about absence: a keyword pattern built from the wrong era under-reports. This is a second, independent mechanism with the same signature, and it bit three times in one session.

**What happened.** The twitter year pages are assembled from two sources — a live X scrape and an operator spreadsheet — and both have hard boundaries:

- Both scrape methods were **capped at ten results per month-bounded query**. The visible consequence is that January–September 2009, and much of 2010–2012, survives almost entirely as clusters on the **last one to three days of each month**, while the months walked more thoroughly run day to day. Read naively, that says he posted in bursts at month-ends for three quarters and then started posting daily. He did not. The cap did that.

- The operator spreadsheet begins **2013-08-17**. On the 2013 page, the apparent explosion of SLOPPP music activity begins in mid-August. **The source boundary and the apparent behavioural boundary are within a week of each other**, and the honest conclusion is that the page cannot date the project's start at all — the earliest surviving trace, 31 July, already says *"checking latest mix"*.

**Why it is worth a rule of its own.** Vocabulary drift is a defect in the *instrument* you build. This is a defect in the *corpus boundary*, and it is more dangerous for two reasons: it produces a sharp, dateable-looking transition rather than a vague under-count, and the date it produces is a real date — the date the archive changed — so it survives a sanity check. A model looking for inflection points will find one, and it will be spurious.

**The candidate rule.** Before writing any claim about when something started, stopped, intensified or went quiet on a page assembled from more than one source, plot the *source* of each row against time and check whether the claimed transition coincides with a source boundary. Where it does, the claim is unsupportable and the page should say so where a reader will hit it before the narrative — not in a footnote.

**The inverse matters just as much and is the useful half.** 2014 onward is spreadsheet-complete (170 of 171 rows), and **absence there is real evidence**. That is what made this session's strongest finding usable: the claim that Dan was repulsed by the 2014 Cumia firing fails partly because a complete year contains no post expressing discomfort. A rule that only says "distrust absence" would have thrown that away. The rule has to be **"establish coverage, then absence is evidence exactly as far as coverage extends."**

**Not promoted.** One corpus, one author, one archive, discovered by one session. It needs a second instance in a different corpus — `bin/mine-messages` over the iMessage dump is the obvious place, since that record has its own source boundaries and `wiki/interests/music/overview` already carries several unchecked absence claims drawn from it. Promote when someone hits it there, or when the coverage-plotting step is mechanised.

### 2026-09-04 — Working a stale premise honestly moves the front rather than clearing it

- **Observed during:** the CROSSLINK pass on `wiki/people/alexis-armel`, which edited two hub pages

- **Surface:** `bin/wiki-climb check`; `date_modified:`; every `> **RE-CHECKED**` blockquote in `wiki/mind/synthesis/`

- **Observation:** editing `the-cool-metric` and `alexis-armel` made ten dependents stale. All ten were worked to the standard CLAUDE.md rule 3 requires — premise re-read, decision recorded on the page, no date bumped blind — and one produced a real result (a candidate counterexample to `the-binary-verdict`'s "no documented middle value" row). Recording those results is itself a page edit, so nine `date_modified`s moved, so nine of *their* dependents went stale. Measured by running the gate against `main` with the work stashed and unstashed: **44 stale pages before, 44 after. Nine cleared, nine created, net zero.** The staleness front moved one layer outward and did not shrink.

- **Candidate invariant:** on a page with dependents, a *null* re-check ("premise moved, nothing here affected") costs exactly as much downstream as a claim actually changing, because the only thing the gate compares is two dates. The queue is therefore not drainable one page at a time by a session that also writes content — and this is the mechanism behind 104 stale premises surviving the 2026-09-02, 09-03 and 09-04 handoffs untouched. It is not that nobody got to it.

- **Candidate instruction:** two halves, and the second needs a decision the first does not. (a) A session that edits a hub page should expect to owe the whole first layer of re-checks and should say so before starting, rather than discovering it at the gate. (b) The queue should be drained **breadth-first in a dedicated pass that writes no new content**, working every page at one layer before touching the next, so each layer's bumps land together instead of interleaving with fresh edits.

- **Validation, and what would settle it:** the net-zero figure is solid — it is the gate run twice. The larger prize is unmeasured: **how many of the 113 stale pairs are premises whose only change was a re-check blockquote?** If most are, the gate is largely reporting its own bookkeeping, and `bin/wiki-climb check` could exempt a premise whose diff since the dependent's date is entirely blockquote additions. An attempt to measure this on 2026-09-04 was **abandoned as unreliable**: the session had a shallow clone reaching only to 2026-08-17, `git log` therefore showed one commit for files older than that, and the diff came back empty for 102 of 113 pairs — a clone artefact, not a result. **Re-run it after ****`git fetch --unshallow`**** before believing any number here.** Do not promote until that measurement exists; the instruction in (b) is cheap and safe, the tool change in the validation note is not.

- **Status:** inbox

### 2026-09-04 — One honest re-check clears every stale flag on the page, including the ones nobody read

- **Observed during:** the CROSSLINK pass on `wiki/people/vaughn`, working the first layer of re-checks it owed

- **Surface:** `bin/wiki-climb check`; `bin/wiki-work`; `date_modified:`; every `> **RE-CHECKED**` blockquote

- **Observation:** ten pages went stale from that pass. Each was worked to CLAUDE.md rule 3 — premise re-read, decision recorded on the page — and each then had `date_modified` bumped, which is the only way to clear the flag. **Those ten pages were carrying thirty-eight stale flags between them, not ten.** `wiki/self/context-core` had six, `wiki/places/the-unpapered-address` five, `wiki/health/the-configured-body` five, `wiki/mind/synthesis/spatial-behavior` four — accumulated against different premises over weeks. Every one of the thirty-eight cleared. **Twenty-eight of them were never read by anybody.** Measured by running the gate with the work stashed and unstashed: 125 stale pairs before, 99 after, 38 cleared and 12 created.

- **Candidate invariant:** staleness is a property of a *pair* (dependent, premise) and `date_modified` is a single scalar on the dependent, so the gate cannot express "I answered this one and not that one." Any honest re-check of one premise silently discharges every other premise's claim on the same page. **The stale queue therefore understates the real debt, and it understates it most on exactly the pages that get worked most** — a hub page with six flags is cleared by one session that answered one of them.

- **How this relates to the entry above.** That one measured the *front moving* (nine cleared, nine created, net zero) and concluded the queue is drainable only breadth-first. This is the other half of the same mechanism and it cuts the other way: part of what looks like drainage is not drainage. Both entries are about `date_modified` being too coarse to carry the state the gate needs; neither is a reason to stop bumping, because refusing to bump leaves a page permanently red for a premise that was genuinely answered.

- **Interim mitigation, applied on all ten pages this pass:** the re-check blockquote names every flag the bump also cleared, so the record holds what the gate can no longer show. That is a convention, not an enforcement — nothing checks it and the next session will not do it unless it is written down.

- **Candidate instruction:** either (a) a re-check block must enumerate every stale flag currently on the page and say which were answered, or (b) `bin/wiki-climb` should track re-checks per pair rather than per page — a `rechecked:` frontmatter map of premise → date, so the gate clears one pair at a time and a bump for unrelated content clears nothing. (b) is the real fix and is a tool change; (a) is what a session can do today.

- **Validation, and what would settle it:** the thirty-eight/twenty-eight figures are solid — the gate run twice, diffed. What is not established is how far back this goes: **how many of the 99 remaining stale pairs are pairs that were already cleared once by an unrelated bump and re-accrued?** That needs the git history the shallow clone does not have, same blocker as the entry above. Do not promote (b) before someone has run it unshallow and confirmed the pair-level state is worth the frontmatter it costs.

- **Status:** inbox

## A mechanical rewrite over prose must mask quotations over the whole file (2026-09-05)

**Observed while writing ****`bin/wiki-crosslink unlinked --apply`****,** which inserts `[[wikilinks]]` into the body of 186 pages in one run.

**What happened.** The first cut refused to write into a quotation, a heading, a code span or an existing link, and computed that mask **one line at a time**. It then wrote a wikilink into the middle of a quoted tweet:

nothingness but at least I got the [[wiki/self/twitter|@danfrank]] handle"*

The opening `"` was two lines up. Prose in this corpus is hard-wrapped at ~78 columns, so **a quotation of more than about ten words spans lines by default** and a per-line mask sees only its tail — an unbalanced closing quote, which looks like no quote at all. The single case the guard existed for was the single case it structurally could not see.

**Why it nearly shipped.** Nothing catches it. `bin/wiki-lint` is happy, the gates are green, the diff is 432 lines of plausible-looking link insertions across 186 files, and the damage is a wikilink inside somebody's quoted words on a public site. It was found by writing a separate verifier that recomputed the quote parity from the *pre-change* bodies and diffed the results — not by reading the diff, which I had already done.

**Candidate invariant.** Any pass that edits prose mechanically must compute its protected regions over the whole file, never per line, because this corpus's line breaks fall inside its sentences and therefore inside its quotations. The same applies to a pass that *reads* prose to decide what a page contains: a regex anchored with `^`/`$` and `re.M` over hard-wrapped text is measuring lines, not statements.

**Candidate instruction.** Before a mechanical prose edit lands: write the verifier that checks the *result* against the *original* independently of the code that produced it, and run it. Over-masking is the safe direction — a missed link costs a click, an edited quotation costs the record.

**Validation.** One occurrence, caught pre-merge. Pinned by `tests/test_wiki_crosslink.py::LinkPlacement::test_never_inside_a_quotation_that_spans_lines`. **Promote on a second occurrence in a different tool** — `bin/wiki-plain`'s `audit` and `bin/wiki-lint`'s own `strip_code` are the two places most likely to carry the same assumption, and neither has been read for it. Do not promote on this alone: one bug in one function is not yet an invariant about the corpus.

- **Status:** inbox

## A module-level name in `bin/` is a public API, and the gates do not check it (2026-09-05)

**Observed while adding ****`bin/wiki-crosslink rederive`****,** a forty-line subcommand at the bottom of a 2,100-line file.

**What happened.** The new command needed to read a page's message count, so it declared `MSG_COUNT_RE` at module scope. One already existed 700 lines earlier, serving `counts`, and the new one **silently replaced it** — a stricter pattern requiring `**bold**` where the original accepted a plain or `~`-prefixed number. `counts` did not error. It just quietly stopped matching a class of page.

**Why it nearly shipped.** `bin/wiki-check` ran the whole chain and reported **all gates clean**. Every gate was green, the new command worked, and the diff looked like an addition rather than a change. Only `python3 -m unittest discover -s tests` saw it — three failures in `MessageCountCheck`, a test class for a command the diff never mentions.

**Candidate invariant.** In this repository's `bin/` tools, a module-level constant is shared surface even when the code that uses it is a thousand lines away, and Python rebinds silently. The gates check the *corpus*; nothing checks the *tools*, so a tool regression is invisible to `bin/wiki-check` by construction — which is exactly why `CLAUDE.md` lists the test suite as a separate step and not as part of the chain.

**Candidate instruction.** When adding a subcommand to an existing `bin/` tool, grep the file for every name you are about to define before defining it, and run the tests — not just `bin/wiki-check` — before committing. Reuse the existing constant where one fits; the general pattern usually already exists because somebody hit the edge cases first.

**Validation.** One occurrence, caught pre-commit by the test suite. Pinned by `tests/test_wiki_crosslink.py::RederiveQueue::test_it_reuses_the_count_regex_rather_than_shadowing_it`, which asserts there is exactly one definition.

**The corpus-wide measurement was run and it argues against promoting this.** Scanning every file in `bin/` for a module-level `NAME =` defined more than once returns **zero** — `bin/wiki-crosslink` alone declares 31 such constants and no tool currently shadows any of its own. So the hazard is real (the collision happened, and nothing but the tests saw it) and the base rate is nil: one bug in one file, introduced and caught in the same hour. **Leave it parked.** Promote on a second occurrence in a different tool, or if that count ever comes back non-zero on `main`.

## A model's recall of its own conversations is a source class, and its nouns drift (2026-09-05)

**What happened.** The operator pasted an assistant's audit of its own conversational history with him — a deliberate search for his custom-language layer, listing ~25 coined terms with provenance annotations. The document was carefully argued, explicitly warned that assistant-coined language must not be laundered into user-coined language, and closed by admitting it was running on recall rather than a corpus query.

Checked term-by-term against `raw/`, its **central term was wrong**. It filed Dan's cognitive-style self-label as *"Iterative Symbolic Architect"*: **zero occurrences** anywhere in the archive. The corpus says *"Recursive Symbolic Architect"* — 35 in the Gemini activity export, 10 in `Dan Profile.txt`, hits in four more files. Same for the AI metaphor: the audit gave *"cognitive prosthetic"*, the corpus almost always says *"recursive cognitive prosthetic"*. Four more of its coinages returned zero, and one — *"human RSS feed for cultural bullshit"* — exists in the corpus **pointed the other way**, as a model's insult aimed at Dan rather than his phrase for somebody else.

**Why it nearly shipped intact.** Nothing about the document reads as unreliable. It is better-reasoned than most `raw/` material, it is operator-endorsed, and its self-caveat makes it *look* like it has already priced in its own limits. The failure mode is narrow and specific: recall preserves the **shape** of a term and drifts on the **string** — a near-synonym gets substituted in the modifier slot. *Iterative* and *recursive* mean almost the same thing conversationally and nothing like the same thing here, where `recursive` turns out to be the load-bearing modifier across the whole lexicon and has no competitor anywhere in the corpus.

**Candidate invariant.** A model reporting on conversations it participated in is neither T0 testimony nor corpus extraction, and `EXTRACTION_SPEC.md` has no tier for it. It is reliable about *that a term exists and what it does* and unreliable about *what the term is*. Any exact string taken from such a source — a name, a coinage, a quoted phrase, a command — must be grepped against `raw/` before it enters a page, and the occurrence count recorded next to it, because **0 is informative and is not the same as "never said."**

**Candidate instruction.** When filing operator-pasted model recall: build the corroboration table first, before writing any prose. One column of counts against `raw/` reorders the entire entry — it turned an accepted inventory into a provenance audit, and the corrected term is the one the wiki now uses.

**Validation.** One occurrence, caught pre-merge, written up as `wiki/interests/language/personal-lexicon`. **Promote on a second occurrence.** The obvious place to look is the existing corpus of AI-generated self-analysis already in `raw/self/dox-md/` and `raw/self/chats/`: several of those documents quote Dan's own phrasing back at him, and nobody has checked whether the quotes survive a grep. `wiki/mind/profile/lexicon` is the nearest existing page built from a single un-verified paste. Do not promote on this alone — one drifted modifier in one document is not yet a rule about a source class.

- **Status:** inbox

## A capture path with no operation behind it is a queue that only fills (2026-09-05)

**What happened.** `lexicon/words/` is a real directory in this repository, written to from the portal, and named in `.github/workflows/notify-portal.yml` as one of the four read paths that trigger a portal sync. It is documented **nowhere else** — not in `CLAUDE.md`'s architecture section, not in the operations list, not in the tools table, not in `WORK.md`. It held exactly one file, captured 2026-08-27, `status: pending`, `## Reading` reading *"Not yet analysed."* for nine days. No session had ever looked at it, because nothing told any session it existed.

`bin/wiki-work` could not have surfaced it: the tool aggregates parked `sage/` questions, staged gap answers, stale premises, unnormalised portal edits and four named queues, and `lexicon/words/` is none of those.

**Candidate invariant.** The repository has a general shape — a capture front door, an obligation the queue reports, an operation that clears it — and this path has the first without the second or third. The *front door is the easy part*: it is one path in one workflow, and it can be built and shipped by a session that never gets round to the room behind it. Nothing in the gates detects a directory that only accumulates.

**Candidate instruction.** When adding a write path that a human or the portal can feed, add the obligation in the same change — a `bin/wiki-work` source, or at minimum a documented operation in `CLAUDE.md`. Conversely: when picking up unfamiliar work, `git ls-files -- <dir>` over the paths named in `.github/workflows/notify-portal.yml` is a cheap check for a queue nobody is draining.

**Validation.** One occurrence, nine days, one item. **Promote on a second undocumented capture path**, or on a measurement — a sweep of every directory written by the portal against what `bin/wiki-work` can see would settle whether this is a one-off or the shape of a recurring defect. It is one directory and one file; that is an observation, not yet an invariant.

- **Status:** inbox

### 2026-09-06 — When a lexical proxy is broken, the replacement is often a field a gate already checks

- **Observed during:** building `bin/wiki-claims scan` (PR #272), which needed to find pages asserting a state whose evidence had stopped

- **Surface:** any tool computing candidates over the corpus — `bin/wiki-crosslink scan`, `bin/wiki-traits mine`, `bin/psychometrics`, `bin/wiki-lexicon distinctive`

**Observation.** The obvious proxy for "this page's claim has expired" is a prose grep: `no longer`, `now defunct`, `since closed`. Measured against this corpus it returns **121 hits and is roughly all false positives** — overwhelmingly quoted tweets in which somebody *else* is no longer something (`@iamcoreybrown didn't get the memo that putting "-eezy" after words is no longer hip`). `corpus/lexical-proxy-load.md` predicts exactly this and the router surfaced it, so the rejection was cheap and the skill did its job.

What that skill does **not** say is what to reach for instead. The replacement here was **frontmatter**: `status: active` against a `date_range_end` more than two years past. That found 10 pages — every one a genuine case, no reading required to filter them — plus 80 more at `status: closed`.

**Candidate invariant.** The asymmetry is not "structured beats unstructured." It is that **`bin/wiki-lint`**** already gates ****`status`**** and the date fields**, so a session that wrote a wrong value there got told at commit time. Prose has no such gate and never did. A field under an existing gate carries the accumulated correctness of every commit that had to pass it; a regex over prose carries nothing. That is a property of *this repository's own gates*, not of data formats in general, and it is why the same move may not transfer to a corpus without them.

**Candidate instruction.** Before writing a regex over page prose to compute candidates, ask which frontmatter fields `bin/wiki-lint` validates and whether any of them is a proxy for the thing being looked for. If one is, prefer it and say in the tool why the prose version was rejected — the next session will reach for the grep otherwise, because it is the obvious thing.

**Validation.** One clean occurrence of the *positive* move; `bin/wiki-crosslink` documents the negative half (single-token name matches are ~all false positives) but replaces it with better entity matching rather than with frontmatter. **Promote on a second tool that swaps a prose proxy for a gated field**, or on a measurement — a count of which `bin/` candidate-generators read frontmatter versus prose, against their false-positive rates, would settle whether this is a pattern or one lucky fit. Do not promote earlier: a rule that says "prefer structure" is true everywhere and useful nowhere, and the gate-provenance argument is the only part with teeth.

- **Status:** inbox
