# `reports/` — mechanical audit output

Everything in this directory is the output of a **mechanical scan**. None of it is analysis. A string match, a count, or a filename collision is a *candidate* that a reasoning pass has to confirm or reject — and the 2026-08-20 review pass found that treating matches as findings had already inflated two headline numbers by roughly an order of magnitude (`MECHANICAL_AUDIT.md` §Corrections).

**Start at **[**`MECHANICAL_AUDIT.md`**](http://MECHANICAL_AUDIT.md)**.** It carries the priority matrix and, at the bottom, a per-number verification table. Do not cite a number from this directory without checking its row there.

## Reproducibility — read before trusting a number

The audit was produced by ad-hoc scripts that **were not committed**. Most of these reports therefore cannot be regenerated, which means they are **dated snapshots, not live views**. They describe the corpus at branch commit `5355c0a` (476 pages) and go out of date with every content pass.

| **Report** | **Reproducible?** | **How** |
| --- | --- | --- |
| `MECHANICAL_AUDIT.md` | partially | numbers marked **verified** only |
| `corpus-inventory.{json,md}` | no | snapshot at `5355c0a` |
| `generated-drift.md` | **superseded** | use `bin/wiki-freshness` — deterministic, exact set difference |
| `llm-feed-audit.md` | partially | page-count claims: `bin/wiki-freshness` |
| `phantom-sources.md` | **yes** | `bin/wiki-lint` (warnings) |
| `retraction-candidates.md` | **yes** | `bin/wiki-lint` + `RETRACTED.md` |
| `duplicate-frontmatter.md` | **yes** | `bin/wiki-lint` (errors) |
| `archive-status-audit.md` | trivially | `grep -l 'status: archived' wiki/**/*.md` |
| `connection-retrofit.md`, `islands.md` | approximately | `bin/wiki-connect audit` (different tool; expect different numbers) |
| `synthesis-audit.md` | approximately | `bin/wiki-climb audit` |
| `source-coverage.md` | no | snapshot |
| `entity-candidates.md`, `entities/ENTITY_CENSUS.md` | no | **contested — the two disagree by 167** |
| `graph-candidates/top-100.{json,md}` | no | derived from `connection-queue.md` at snapshot time |
| `temporal-audit.md` | no | snapshot |
| `hygiene-results.md` | no | snapshot |
| `source-campaigns/*.md` | no | hand-assembled briefs |

**If you need a current number, run the tool.** If no tool exists, say the number is from a dated snapshot and give the date. Do not silently refresh a snapshot's prose while leaving its counts stale.

## What became enforcement

Three findings were promoted from report to gate. These *are* live:

| **Gate** | **Tool** | **Severity** |
| --- | --- | --- |
| Duplicate top-level frontmatter keys | `bin/wiki-lint` | error |
| Retracted claim asserted live | `bin/wiki-lint` + `RETRACTED.md` | error |
| Cited source is empty / header-only | `bin/wiki-lint` | warning |
| Cited source is an ambiguous bare filename | `bin/wiki-lint` | warning |
| Generated corpus out of sync with `wiki/` | `bin/wiki-freshness` | exit 1 |

Tests: `python3 -m unittest discover -s tests`.

## `source-campaigns/` — preparation, not extraction

These briefs exist to let a future session enter a source already knowing its shape: coverage window, size, existing wiki citations, candidate entities and events. **They are cheap preprocessing and must not become the source of truth.** Nothing in them establishes that an event happened, that an entity exists, or that a contradiction is real — only that a pattern matched. Read the source.
