## plain_of: wiki/mind/concepts/bunker-core title: "Bunker Core" reading_level: general date_modified: 2026-08-26 source_modified: 2026-08-26

# Bunker Core

**The short version.** "Bunker Core" is the name Dan has given to a self-built, local-first technical stack. At its center is a practice of running database forensics directly against his own iMessage history — a SQLite query engine pointed at `~/Library/Messages/chat.db`. The practical output is real: a commercial product called the iMessage Analysis Toolkit, launched on Gumroad in February 2026. Beyond the verifiable facts, the name also functions as a psychological posture — a way of describing a life split in two. One half is survival work: counter shifts at BFS Foods and property management alongside his mother, Suzanne. The other half is technical sovereignty: building local, self-hosted tools that don't depend on platforms or institutions. The return to Uniontown in early 2025 was a deliberate trade, by Dan's own framing — leaving the expensive, dependent life in New York for a lower-cost base from which to build something sovereign.

## What it actually is

The primary, verifiable fact is narrow and concrete: Dan built a local database-forensics practice on his own message history, and he shipped a commercial tool derived from that same skillset. The tool is the iMessage Analysis Toolkit, available on Gumroad since February 2026. The method is SQLite forensics run directly against the macOS Messages database — `~/Library/Messages/chat.db`, which is the local SQLite copy of every iMessage and SMS conversation on the machine. Querying it directly produces an immutable, timestamped, participant-tagged record that does not depend on what anyone remembers or claims. A SQL receipt is not an interpretation. It is a fact.

That's the documented software reality. Beyond it, "Bunker Core" starts functioning less as a piece of code and more as a name for a way of living.

An AI-generated forensic-inventory document — one Dan did not prompt or author himself — elaborates the concept at length. It describes Bunker Core as an "epistemic fortress," a system built so that no one, not even a partner or a platform, can rewrite his narrative without a SQL receipt. That framing is interpretive. It is something an AI produced when given Dan's setup, not something Dan stated about himself in the retained record. But the same document flags its own double edge without prompting: the same architecture that protects against gaslighting — facts that don't change based on who is shouting loudest — also risks functioning as insulation. A wall of text that prevents external entry. Optimizing for accuracy over access.

Treat the software as documented fact. Treat the fortress framing as a plausible but AI-authored interpretive overlay — a reading of what the software means, not a claim Dan has made in his own words anywhere in the corpus.

## Not one program — a small ecosystem

One of Dan's own AI session documents settles a question this entry used to leave open. It names six separate pieces of software under the heading "the Bunker Core ecosystem," which answers it plainly: Bunker Core is not a single application. It is a label for a set of small, purpose-built tools.

- **Instruction Forge** — an offline tool, running in a browser, that checks written instructions given to AI models. It follows fixed rules rather than asking another AI, so the tool that audits AI instructions does not itself need an AI to work.

- **Cognitive Foundry** — a four-stage app, wired to the Claude API, for building what he calls "cognitive prosthetics": aids for thinking.

- **VoidDiagnostic** — a tool for testing what a model knows. He moved it from Gemini to the Claude API and rebuilt its wording in the move instead of copying it over.

- **Memory Forge** — a browser tool that examines the items an AI stores about a user. It is built to match Gemini's own memory format, which means he worked out how that format functions and rebuilt it as a tool of his own.

- **YAHLATRO** — a dice game, shipped as one HTML file. It is the only thing on the list with no investigative or self-analysis purpose at all: a game built the same way the serious tools are built.

- **Bibi** — an AI persona rather than a program, described as "the AI-as-collaborator identity": a standing character he can work with, instead of a role set up fresh each session.

Two more things round the set out. The **Fortress Protocol** is a deliberately maximalist visual style for AI replies — the heavy symbols, dividers and "fortress walls" that show up throughout these documents turn out to be a designed system rather than decoration that crept in. And there is a master instructions document, assembled from his personal files.

**Take this list at the confidence it earns, which is not much.** None of the six projects, the Fortress Protocol, or the master document has any independent trace anywhere else in the record — no code, no repository, no dated evidence that any of it was built. This is Dan listing his own projects inside an AI session. That is good evidence of what he intended to build. It is not evidence that the software exists and runs as described. The list answers "one program or several?" — several, by his own account — and leaves "does each one work?" wide open.

## The two-track life

Bunker Core sits inside a larger structure Dan has described as his "Bifurcated Daily OS" — a two-track operating system for daily life. The two tracks run simultaneously. They share a physical address and a daily schedule, but they operate on different logics.

| **Track** | **What it includes** | **Where it lives** |
| --- | --- | --- |
| Survival work | BFS Foods counter shifts, property management alongside Suzanne | Uniontown, PA |
| Technical sovereignty | Local SQLite forensics, iMessage Analysis Toolkit, vibe-coded games, agent tooling | The same town, the same machine |

The survival work is income, stability, and the maintenance of existing obligations. The technical sovereignty track is the construction of independent infrastructure — tools that don't require permission from a platform, an employer, or an institution.

Dan's own framing of the return to Uniontown in early 2025 is that it was a deliberate trade. He left New York — expensive, institutionally dependent — for a lower-cost base. The lower cost was not the goal. The lower cost was the precondition. What it was the precondition for was the construction of sovereign tooling: local, self-hosted, under his control.

## What the forensics actually do

The core method is SQLite queries run against the Messages database on a Mac. `~/Library/Messages/chat.db` is the local copy of every iMessage and SMS conversation on the machine. Querying it directly produces a record that is:

- **Immutable** — once a message is in the database, it does not change based on who is telling the story.

- **Timestamped** — every message has a precise time, which means the sequence of events is recoverable.

- **Participant-tagged** — every message has a sender and receiver, so attribution is queryable.

This is proof against gaslighting in the most literal sense: the database does not change based on who is shouting loudest or who has the better story. A SQL receipt is not an interpretation. It is a fact.

The iMessage Analysis Toolkit commercializes this capability. It takes the forensic method Dan built for his own use and packages it for sale. Launched February 2026 on Gumroad. The toolkit is the concrete, dated output of what Dan calls his 2026 "High-Autonomy Technical Stack" — one half of the bifurcated daily OS, the other half being survival work.

The practice is part of a larger 2025–26 wave of tool-building documented across the record: vibe-coded games, agent tooling, forensic scripts. The context-core log for that period records it as "agent/AI build work, music reactivation." The tool-building is one half of what Dan was doing in that window. The other half was something personal and separate.

## The gap between software and self

There is a question the page leaves open: is Bunker Core a single coherent codebase, or is it a loose label for an evolving set of scripts that share a philosophy but not a repository? The record does not settle this. The commercial product exists and is dated. The rest is a moving target.

A related gap: the AI-generated forensic-inventory document that elaborates the "epistemic fortress" framing is not primary self-report. It was produced by an AI given Dan's setup. It may be accurate. It may be insightful. But it is not Dan's own description of himself, and the distinction matters. The document flags its own double edge — that the same architecture protects and insulates — but it still produces the insulation reading without being asked. That is the AI finding a pattern. It is not Dan naming his own pattern.

## What we still don't know

- **~~Whether Bunker Core is one codebase or many.~~** **Answered:** several, by Dan's own account — see the list above. But each project on that list is still unverified. There is no code, repository or independent record for any of the six.

- **Whether anyone else has used or seen the toolkit beyond the Gumroad listing.** The record documents the launch. It does not document users, collaborators, or public reception.

- **Whether the fortress framing is accurate.** The AI-generated reading is plausible and self-aware about its own limits. But it remains an AI reading of a human setup, not the human's own words.

- **Whether the project is still active.** The documentation window is 2026. Nothing in the record speaks to whether the toolkit or the forensic practice continued past that point.

*This is the plain-English version of a longer, more technical entry. The full page carries the source records, the cross-references to other entries, and the revision history behind every claim here.*
