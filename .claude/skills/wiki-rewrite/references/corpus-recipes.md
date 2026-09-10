# Corpus recipes — where things live and how to read them without getting a wrong answer

Companion to `SKILL.md`. Read the section for a source type before writing greps against it. Several of these formats fail *silently* — they hand you a plausible wrong number rather than an error — and each trap below has already produced a false claim that reached a wiki page.

## Contents

1. Map of raw/

1. Source tiers

1. The iMessage dump

1. Per-thread CSV exports

1. Identity: resolving who a handle belongs to

1. Facebook Messenger threads

1. [The Gchat / Gmail archive](#the-gchat--gmail-archive)

1. The GEDCOM family tree

1. Google and YouTube activity exports

1. Reading lists

1. Opening sweep

## Map of raw/

raw/self/context-core/CONTEXT_CORE_EXPANDED.md   curated, authoritative, self-flagging — CHECK FIRST

raw/self/dox-scan/       message dumps, per-platform analyses, Gemini overflow (.txt)

raw/self/dox-md/         Gemini/ChatGPT sessions, AI profile artifacts (.md)

raw/self/message-csv/    per-thread and bulk iMessage exports

raw/self/facebook/       full Facebook takeout (messages, address book, posts, searches)

raw/self/ancestry/       GEDCOM family tree

raw/self/google-drive-export/, raw/self/favorites/   Goodreads, FAVS masterlist

raw/self/gemini-activity/, raw/self/youtube-watch-history/, raw/self/twitter/

raw/self/captures/       operator-typed notes filed from inbox/

raw/people/, raw/legal/, raw/interests/, raw/mind/, raw/tech/, raw/music/

`CONTEXT_CORE_EXPANDED.md` is curated and internally cross-checked, and it flags its own gaps. For any self/mind/timeline question, read it before searching the wider corpus, and treat other sources as supplementary or corrective to it rather than co-equal — unless they carry a specific dated correction it lacks. Its residency table alone settles most date disputes.

## Source tiers

**Primary** — records of what happened: the message dump and per-thread CSVs, the GEDCOM, `contacts.csv` and the Facebook address book, the Gchat archive, Goodreads/YouTube/Twitter/Facebook takeouts.

**AI-secondary** — a model reasoning about the corpus: everything under `dox-md/` that is a Gemini or ChatGPT session, `THE_DAN_FRANK_BOOTLOADER.md`, `THE_DAN_FRANK_MANUAL.md`, `CATO_*`, `DANSYNTH.txt`, `dansynth-scrape-*`.

The distinction is not that AI-secondary is worthless — it is often the only place a memory or a self-assessment is recorded, and **the operator's own words inside a session are primary testimony**, including his corrections of the model. What is not evidence is the model's factual assertions. These files confabulate specifics with total confidence: invented deed lookups, invented publication chronologies, probability estimates that wander four orders of magnitude between sessions. When you keep one, attribute it on the page.

`DANSYNTH.txt` is a special case worth knowing: it is heavily stylised AI output wrapped around real operator statements. The glyph noise is worthless; the `# you asked` blocks are first-person primary source and contain some of the sharpest geographic and relational statements in the corpus.

## The iMessage dump

`raw/self/dox-scan/all_imessages_complete_dump.txt` — the **only** message source with trustworthy direction. Pipe-delimited:

YYYY-MM-DD HH:MM:SS|Sent|Received|handle|handle|text|attachment|service|4 numeric flags

Three traps, all documented in `EXTRACTION_SPEC.md`, all of which have produced false measurements:

1. **Records span multiple lines.** A record starts with a `TS|Sent|…` header; everything until the next header belongs to it. Line-based `grep` splits one message into several, miscounts, and cannot show you a whole message.

1. **Curly apostrophes outnumber straight ones 28,904 to 19,978** in Dan's sent text. A pattern written `i'm` misses most of its own matches.

1. **Counting without reading.** The count is the cheap part; the message that explains the count is the finding.

Use the instrument:

bin/mine-messages stats

bin/mine-messages grep '<pattern>' --dir Sent --from 2017-01-01 --to 2018-12-31

bin/mine-messages timeline '<pattern>'

bin/mine-messages entities        # capitalised names with no wiki page

For a handle-scoped count, import it rather than grepping:

import importlib.machinery, importlib.util

loader = importlib.machinery.SourceFileLoader('mm', 'bin/mine-messages')

spec = importlib.util.spec_from_loader('mm', loader)

mm = importlib.util.module_from_spec(spec); loader.exec_module(mm)

recs = [r for r in mm.records() if '<digits>' in r['handle']]

from collections import Counter

print(len(recs), Counter(r['dir'] for r in recs))

print(min(r['date'] for r in recs), max(r['date'] for r in recs))

Record keys are `date`, `time`, `dir`, `handle`, `text`.

**Coverage gaps:** 2022 and 2026 are absent from this dump entirely. Anything about the terminal phase, the June 2026 closure or the July 2026 re-contact lives only in `raw/self/message-csv/`.

## Per-thread CSV exports

`raw/self/message-csv/` holds named exports, usually `imessage_<digits>_both_all_now.csv`, with header `timestamp,target,direction,text,associated_message_type,cache_has_attachments,service,textSource`. These are reverse-chronological and two-sided where the filename says `both`.

**`MASTER_MESSAGES_DB_DUMP.csv`**** marks nearly everything ****`Received`****.** Any page built on it will describe a one-sided thread that is not one-sided. This is the single most common false claim in the wiki's people pages, and the tell is a page reporting a suspiciously round "all received (export artifact)".

Line count minus one is a safe message count for these files only because they are single-line-per-record — unlike the dump.

## Identity: resolving who a handle belongs to

Do this before writing a person page. Two independent exports:

grep -i "<name>" contacts.csv | cut -c1-200                 # Google Contacts

python3 -c "

import re, html

d = open('raw/self/facebook/facebook-ihatedanfrank/other_personal_information/your_address_books.html',

encoding='utf-8', errors='replace').read()

L = [x.strip() for x in re.sub('<[^>]+>', '\n', html.unescape(d)).split('\n')]

for i, l in enumerate(L):

if '<surname>' in l: print(L[i:i+6])

"

**Agreement across both exports is an identification. A single Google Contacts record is not** — Google merges records aggressively, so one contact card can carry numbers belonging to two different people. The Facebook address book has not been merged and is the tiebreaker.

Worked example, which is why this section exists: handle `+18439903264` was attributed to Zach Harshman for months. Google Contacts carried it on a card named "Zach Clingan" *and* on a bare "Zach" card — the signature of a merge. The Facebook address book, which never saw the 843 number, independently gave Clingan the same 413 number and gave Harshman a completely disjoint set. Neither Harshman number appears in the message dump at all. The page was about the wrong person, and the real Harshman already had his own page.

When the identification is an inference rather than a signature, **show the chain on the page** and keep it in Gaps.

## Facebook Messenger threads

`raw/self/facebook/facebook-ihatedanfrank/messages/inbox/<name>_<hash>/message_1.html`. Note the takeout contains a duplicated nested tree (`facebook-ihatedanfrank/facebook-ihatedanfrank/…`); either path works, but do not count a thread twice.

In the HTML, each message is a `_3-95 _a6-g` div containing, **in this order**, sender (`_a6-h _a6-i`), body (`_a6-p`), then timestamp (`_a72d`). An earlier session's notes recorded body-before-sender and were wrong. Messages appear **newest first**, so read a thread bottom-up for conversation order. `d.count('_3-95 _a6-g')` is a reliable message count for the thread.

For quick reads, strip tags and scan:

import re, html

d = open(path, encoding='utf-8', errors='replace').read()

L = [x.strip() for x in re.sub('<[^>]+>', '\n', html.unescape(d)).split('\n') if x.strip()]

for i, l in enumerate(L):

if '<term>' in l.lower(): print(L[max(0,i-6):i+4])

The plain-text scrapes under `dox-scan/` (e.g. `dan tom 2010 2022.txt`) are a different format: **reverse-chronological**, and each record is `timestamp → sender → blank → text`. Read bottom-up to get conversation order, and be careful attributing lines that share a timestamp.

## The Gchat / Gmail archive

`raw/self/dox-scan/gmail_bodies.txt` — the largest under-read source in the repository. Blocks separated by a long `─` rule, each headed `From: / To: / Date: / Subject: Chat with <name>`, with the transcript below as `me:` and `<name>:` lines.

d = open('raw/self/dox-scan/gmail_bodies.txt', encoding='utf-8', errors='replace').read()

blocks = [b for b in d.split('─'*56) if '<their-address>' in b]

Two things to know. **Most blocks are undated** — in the reference pass only 43 of 495 carried a `Date:` header, so the archive's true span is usually unknown and should be reported as a sample range, not a span. And the content is almost entirely mundane, which is exactly its value: it is the only *daily* record of 2010–2013 in the corpus, written while things were happening rather than reconstructed afterwards by one participant during an argument about something else. It is where private vocabulary, household logistics and undramatised relationship texture live.

## The GEDCOM family tree

`raw/self/ancestry/extracted/Daniel Frank family tree.txt`. Records start at column 0 with `0 @I…@ INDI` (individual) or `0 @F…@ FAM` (family). Levels are leading integers. To walk it:

lines = open(path, encoding='utf-8', errors='replace').read().split('\n')

starts = {l.split()[1]: i for i, l in enumerate(lines) if l.startswith('0 @')}

def block(tag, n=400):

i = starts[tag]; out = [lines[i]]

for l in lines[i+1:i+n]:

if l.startswith('0 '): break

out.append(l)

return out

`FAM` records give `HUSB` / `WIFE` / `CHIL` pointers and `MARR` with `DATE` and `PLAC`; `INDI` records give `NAME`, `SEX`, `BIRT`, `DEAT`, `BURI`, repeated `RESI` (dated residences), `FAMC` (parents) and `FAMS` (spouse families).

Two cautions. **`PLAC`**** under a ****`DEAT`**** is a burial place as often as a death place** — a previous pass asserted a death location the record did not contain. And Ancestry attaches sources loosely, so a citation's publication date may not match the event date; report both rather than picking one.

The tree is worth searching even when the subject is not a relative: it carries dated residences and place names that pin down addresses, and in the reference pass a single `PLAC Belmont Circle` line moved a house's documented history back by a decade and revealed that a family's arrival there was a return from Florida.

## Google and YouTube activity exports

`raw/self/gemini-activity/Gemini Activity.html`, `raw/self/youtube-watch-history/*.html`, `raw/self/facebook/**/search/your_search_history.html`. All large, all tag-soup. Strip tags and window around the match:

import re, html

d = open(path, encoding='utf-8', errors='replace').read()

for m in re.finditer(r'.{600}<term>.{400}', d, re.S):

s = re.sub(r'\s+', ' ', html.unescape(re.sub('<[^>]+>', ' | ', m.group(0))))

print(s, '\n---')

Timestamps sit a few fields after the item title, so a window is more reliable than a line grep. These exports are excellent for dating an interest precisely — and for catching a story that says "autoplay" when the record shows two related videos watched two minutes apart at one in the morning, which is a search.

## Reading lists

`raw/self/google-drive-export/goodreads_library_export.md` (markdown table) and `raw/self/favorites/FAVS MASTERLIST.csv`. The Goodreads columns of interest are title, author, **My Rating**, average rating, publisher, **year published**, **date read** and shelves.

The trap: **the shelving date is not the publication year**, and the shelf tags often contain a year that is the shelving year. A page once dated a 2017 novel to 2022 on that basis. Cross-check the `year published` column, and check whether a book the wiki says was read actually appears in the export at all — in the reference pass, the novel an entire page was built around was not in either file.

## Opening sweep

For a person, place or thing you are about to rewrite:

SUBJECT="<name>"

grep -ril "$SUBJECT" raw/ | head -40                  # every source that mentions it

grep -rln "<page-slug>" wiki/ *.md                    # inbound links

grep -rn -A2 "page: wiki/<domain>/<slug>" wiki/       # existing inverse edges

grep -i "$SUBJECT" contacts.csv | cut -c1-200         # identity, if a person

bin/wiki-search "$SUBJECT"                            # what the wiki already says

Then read `CONTEXT_CORE_EXPANDED.md` for the subject before anything else in `raw/`, and go from there.
