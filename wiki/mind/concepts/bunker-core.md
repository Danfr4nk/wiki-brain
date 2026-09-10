
---
domain: mind
page_type: concept
title: "Bunker Core"
status: active
knowledge: mixed
date_created: 2026-07-20
date_modified: 2026-08-26
sources:
  - "raw/self/dox-md/Gemini-_18.md"
  - "raw/self/dox-md/_Dan Frank's Digital Forensic Inventory .md"
  - "raw/self/dox-md/_Openclaw Agent Setup and Data .md"
  - raw/self/dox-md/MAX_PRIME.md
tags: [ai-collaboration, digital-footprint, career]
connections:
  - page: wiki/timeline/periods/2025-collapse
    type: component-of
    claim: "Bunker Core is named in Dan's own 2026 'Bifurcated Daily OS' self-description as one half of a two-track life — survival work (BFS Foods, Suzanne's property operations) alongside a self-built 'High-Autonomy Technical Stack.'"
  - page: wiki/mind/synthesis/ai-collaborative-analysis
    type: instantiates
    claim: "Local, self-hosted chat.db forensics is agent tooling that extends the same evidentiary-verification principle documented elsewhere in Dan's AI use — raw message history as proof against gaslighting, automated rather than manual."
  - page: wiki/work/tech/vibe-coding-games
    type: co-occurs
    claim: "Bunker Core, the iMessage Analysis Toolkit, and the vibe-coded games all belong to the same 2025–26 tool-building wave — the period context-core logs as 'agent/AI build work, music reactivation.'"
  - page: wiki/mind/concepts/exocortex
    type: instance-of
    claim: "Cognitive Foundry — a four-phase Claude-API app for generating 'cognitive prosthetics' — is the exocortex concept built as standalone software rather than deployed as a pasteable session config, the clearest case in the corpus of the metaphor becoming a literal build target."
  - page: wiki/work/tech/max-framework/overview
    type: parallels
    claim: "Bibi, named here as an 'agentic Max persona,' is the Max identity from that framework given a standing, buildable form rather than a per-session role — the two pages describe the same persona from software and prompt-engineering angles respectively."
---

# Bunker Core

Bunker Core is the name Dan has given to a self-built, local-first
technical stack — SQLite-based forensics run directly against his own
`~/Library/Messages/chat.db`, framed in his own notes as "Epistemic
Verification" and a "cold-data ledger." It sits alongside a Gumroad
product, the iMessage Analysis Toolkit (launched February 2026), as the
concrete, dated output of what he calls his 2026 "High-Autonomy
Technical Stack" — one half of a self-described "Bifurcated Daily OS,"
the other half being survival work: [[wiki/work/bfs-foods|BFS Foods]]
counter shifts and property management alongside his mother
[[wiki/people/suzanne-frank|Suzanne]]. In his own framing, the return to
Uniontown in early 2025 was a deliberate trade — leaving expensive,
institutionally-dependent New York life for a lower-cost base from
which to build sovereign, local tooling.

## What it is, and what it isn't

The primary, verifiable fact is narrow: a local database-forensics
practice built on his own message history, plus a shipped commercial
tool derived from the same skillset. Beyond that, "Bunker Core" starts
functioning as much as a name for a psychological posture as for a
piece of software — an AI-generated forensic-inventory document
(unprompted, not primary self-report) elaborates it at length as an
"epistemic fortress," a system built so that "no one, not even a
partner or a platform, can rewrite his narrative without a SQL
receipt." That framing is interpretive, not something Dan states about
himself in the retained corpus, and the same document flags its own
double edge without prompting: the same architecture that protects
against being gaslit — facts that don't change based on who's shouting
loudest — also risks functioning as insulation, "a wall of text that
prevents external entry," optimizing for accuracy over access. Treat
the software as documented fact and the fortress framing as a plausible
but AI-authored interpretive overlay, not a claim Dan has made in his
own words anywhere in the corpus.

## Corpus record

| Metric | Value |
|---|---|
| Named alongside | iMessage Analysis Toolkit (Gumroad, launched Feb 2026) |
| Core method | Local SQLite forensics on ~/Library/Messages/chat.db |
| Self-framing | Half of a "Bifurcated Daily OS": survival work + technical sovereignty |

## The named projects — a loose ecosystem, not one codebase

`MAX_PRIME.md` — a session-memory document, so this whole section carries
its `[MEM]` tag rather than the `[DOC]` (corpus-verified) tag most of the
document's biographical content earns — names six distinct pieces of
software under "The Bunker Core ecosystem," which settles this page's
former open question about whether Bunker Core is one program or a label
for several: it is explicitly the latter, an ecosystem of small,
purpose-built tools rather than a single application.

- **Instruction Forge** — an offline, browser-based LLM instruction
  auditor, deliberately deterministic and rule-based rather than another
  model call: no API dependency, so the audit tool for AI instructions does
  not itself depend on an AI.
- **Cognitive Foundry** — a four-phase interactive app, Claude-API-integrated,
  for generating what the source calls "cognitive prosthetics" — the
  clearest single artifact of the exocortex concept
  ([[wiki/mind/concepts/exocortex]]) built as a tool rather than used as a
  session config.
- **VoidDiagnostic** — a knowledge-diagnostic tool, migrated from Gemini to
  the Claude API with its prompt engineering rebuilt in the move rather than
  ported as-is.
- **Memory Forge** — an LLM memory-item analyzer, browser-based, explicitly
  modeled on Gemini's `user_context` schema — reverse-engineering a
  platform's own memory format into a standalone tool.
- **YAHLATRO** — a Balatro-inspired dice roguelike, shipped as a single HTML
  file. The one project in the set with no forensic or self-analysis
  function at all; a game built the same way the analysis tools are built.
- **Bibi** — named as "agentic Max persona," described as "the AI-as-collaborator
  identity" — the Max persona (see [[wiki/work/tech/max-framework/overview]])
  given a standing, buildable identity rather than a per-session role.

Two more pieces round out the ecosystem rather than being separate tools:
the **Fortress Protocol** (also called the "Alchemical Factory Fortress"),
a custom maximalist Unicode/glyph visual formatting schema for AI
responses — the heavy glyph decoration, section dividers, and fortress
walls that recur across the `dox-md/` corpus are named here as a designed
aesthetic system rather than incidental formatting — and
`DAN_FRANK_LLM_INSTRUCTIONS.md`, described as the master instruction
document synthesized from the personal data files, of which `MAX_PRIME.md`
itself is one contribution.

**Read this list at the certainty level it earns.** None of the six
projects, the Fortress Protocol, or the master-instructions document has
independent corpus verification — no code, no repository, no dated commit
— documented anywhere else `raw/` holds. This is Dan describing his own
build list inside an AI session, which is testimony about intent and
scope, not evidence the software exists as described. Treat the list as
answering "is this one codebase or several" (several, by his own account)
while leaving "does each one actually run" fully open.

**Gaps:** whether Bunker Core is a single coherent codebase or a loose
label for an evolving set of scripts is now answered above (loose label,
by Dan's own description) but each named project remains individually
unverified — no code, repository, or independent corpus record for any of
the six, or for the Fortress Protocol formatting system, beyond this one
`[MEM]`-tagged list. Any third-party involvement, collaborators, or public
release beyond the Gumroad toolkit; whether the project is still active
past its 2026 documentation window.


