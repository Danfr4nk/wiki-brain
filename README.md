# Personal Wiki (v2) — second brain

A lifelong personal wiki: complete biographical history, psychological and ideological profile, and everything else about your personhood, stored as plain Markdown files. No apps, no databases, no APIs — just text files, two small scripts, and git for history. Claude (or any LLM agent) does the compilation; you just feed it material.

## The app

**To pin it in your Dock:** drag **Personal Wiki.app** onto the Dock. Click it any time to launch (or refocus) the wiki in your browser — clicking it again while it's already running just opens/reuses the tab, it never starts a second server.

Alternatively, double-click **Wiki.command** (or run `python3 app.py`). Either way, your browser opens at `http://127.0.0.1:8477` with everything in one place:

- **Wiki** — browse with collapsible domain groups and full-text search; every page has **✎ Edit** (in-place editor) and **Rename** in the toolbar. Rename updates every link and `related:` reference across the wiki automatically, and logs the operation.

- **Capture** — type facts or full stories; drag-and-drop any file to upload. Type **@** to autocomplete a wiki page reference — the note is then saved as a *correction/expansion targeting that page*, and ingestion applies it there first

- **Ingest** — the full any-LLM loop in the GUI: select an inbox item, generate the prompt pack, copy it into any chat model, paste the reply back, and apply (validated + linted, optional auto-commit)

- **Sync** — header shows branch / uncommitted / ahead-behind state; the Sync button commits, pulls --rebase, and pushes to GitHub. A red banner warns if the GitHub repo is publicly visible.

- **Intake ledger** — catalogue a finite quantity when it arrives (substance from a select box, amount, unit, when), then log each intake against it in one line. Events can be measured, estimated, or *unquantified* — "one line" is still an event and still counts toward the timing, it just never enters a gram figure. Closing a unit asks how it ended and refuses to guess at anything unaccounted for. `bin/intake` does the same from the terminal

- **Inbox** — see and manage what's waiting for ingestion

- **Export** — one click bundles the corpus for LLMs, with a download link

It's a single Python file using only the standard library — nothing to install, runs entirely on your machine, touches only this folder.

## Adding material from the terminal (optional)

The same three ways also work as CLI commands, all landing in `inbox/`:

bin/capture                     # type or paste a story; end with a "." line

bin/capture "quick fact here"   # one-liner, no prompts

bin/capture -f ~/some-file.pdf  # upload any file (or a whole folder)

bin/capture status              # see what's waiting

Or double-click `Capture.command` in Finder to open a capture window. You can also just drag files into `inbox/` yourself — same thing.

## Getting it into the wiki

Two ways — either works, both follow the same rules (`STRATEGY.md` for intent, `CLAUDE.md` for process, `STYLE_GUIDE.md` for format):

1. **Claude Code:** open it in this folder and say "ingest the inbox."

1. **Any LLM (no subscription needed):** `bin/ingest-pack` bundles an inbox item into a single prompt; paste it into any chat model (ChatGPT, Gemini, a local model), save the reply, and `bin/ingest-apply <reply>` validates and applies it. Full details in `INGEST_PROTOCOL.md`.

Either way, one item at a time: the original is filed into `raw/` (kept forever, never edited), then the relevant wiki pages are written or updated.

## Reading it

Start at `index.md` — it links to the eight domain indexes (self, timeline, people, mind, work, interests, health, places). Everything is plain Markdown; it also opens cleanly in Obsidian if you ever want a nicer reader.

## Exporting for LLMs (local)

bin/export-corpus                 # the whole compiled wiki -> exports/

bin/export-corpus --domain mind   # one domain only

bin/export-corpus --raw           # include the raw source archive (big)

Produces a single Markdown file with a table of contents and a token count, ready to paste or upload into any LLM.

## Online access for LLMs & agents

The compiled wiki is published for agents on every push to `main`:

- **Discovery:** [https://caakehorn.github.io/wiki-brain/llms.txt](https://caakehorn.github.io/wiki-brain/llms.txt)

- **Manifest:** [https://caakehorn.github.io/wiki-brain/agent/manifest.json](https://caakehorn.github.io/wiki-brain/agent/manifest.json)

- **Public mirror** (resynced hourly, useful when Pages is mid-deploy): [https://caakehorn.github.io/leviathan/data/wiki-data.json](https://caakehorn.github.io/leviathan/data/wiki-data.json) — full page text under `wikiText`, metadata and typed edges under `wikiPages.pages`.

- **Critical spine / full corpus / per-domain bundles / individual pages**

See [AGENT_ACCESS.md](http://AGENT_ACCESS.md) for the full URL table, a pasteable agent prompt, freshness rules, and privacy notes. Local preview:

bin/build-site                   # builds the static site/ (HTML wiki + agent feed), no deps

python3 -m http.server -d site 8787

## Layout

app.py     the app: capture + browse + search + export in one window

inbox/     what you've added but hasn't been processed yet

raw/       original sources, immutable archive

wiki/      the compiled knowledge (the actual second brain)

exports/   generated LLM bundles (disposable, not in git)

bin/       the tools: capture, mining, linting, export, publish

## The governing documents

Six files govern the work, in the order a new reader should meet them. Each says what it wins on when two disagree.

| **File** | **Governs** |
| --- | --- |
| `STRATEGY.md` | what this repo is for and the core loop — **read first** |
| `CLAUDE.md` | the operations: ingest, query, climb, rewrite, lint |
| `EXTRACTION_SPEC.md` | how deep to mine a source before writing — the binding constraint |
| `STYLE_GUIDE.md` | page format and the substance standard |
| `CONNECTIONS_SPEC.md` | typed edges and the claims they carry |
| `SYNTHESIS_SPEC.md` | altitude — how conclusions stack on conclusions |

Plus the working files: `BACKLOG.md` (standing work), `LLM_HANDOFF.md` (the exact resume point), `index.md` (master navigation), `log.md` (history of every operation), `queue.md` (pending ingestion), and the two machine-maintained queues `connection-queue.md` and `synthesis-queue.md`. `INGEST_RUNBOOK.md` and `INGEST_PROTOCOL.md` cover the two ingest routes; `FACTSTORY_BRIEF_TEMPLATE.md` is the source of truth for the brief shipped with hand-typed captures; `AGENT_ACCESS.md` covers online access for agents.

`DIGEST.md`, `RECENT.md` and `OPEN.md` are generated by `bin/wiki-digest` — committed, but never hand-edited.
