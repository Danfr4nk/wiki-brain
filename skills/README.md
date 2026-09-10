# Agent Skills

This directory is the persistent memory for **how to work on wiki-brain**.

The rest of the repository records what the system knows. `skills/` records what agents and LLMs have learned about **changing the system without repeatedly rediscovering the same operational knowledge**.

A skill is not a personality prompt and not a generic coding guideline. It is a reusable, evidence-backed instruction produced by work on this repository.

## Core rule

When an agent learns something that would make the next agent materially better at touching this codebase, it writes that learning back here.

This is a feedback loop:

work → observation → candidate instruction → validation → skill → reuse → revision

No model is the permanent owner. Claude, Codex, ChatGPT, Cursor, local agents, scripts, and future tools all read and improve the same corpus.

## Two layers, one subsystem

The prose layer answers *what should an agent do here?* and a person reads it. It cannot answer the other question, which is the one that actually blocks cross-model work: **what does each model actually have?** A Claude Code session arrives with skills, MCP servers, plugin tools and subagents a Codex session does not have, and neither can see the other's. So there is a second layer, and it is a database rather than prose because its writers are machines running in parallel.

skills/

├── README.md          # this contract

├── INDEX.md           # GENERATED routing table — bin/wiki-skills scan

├── PROTOCOL.md        # how to create, test, revise, and retire skills

├── INBOX.md           # unvalidated observations and candidate lessons

├── CHANGELOG.md       # append-only history of promotions/revisions/retirements

├── <domain>/

│   └── <skill>.md     # one reusable skill per file

└── registry/          # THE DATABASE — what each model has, pushed by the model

├── README.md      # the manifest format and the one rule with teeth

├── events.jsonl   # append-only; the record

├── registry.json  # a projection of the log; regenerable

└── manifests/     # worked examples of the half a scan cannot see

`INDEX.md` is **generated from the skill files** and must not be hand-edited. It once carried a `Status` column duplicating each skill's own `status:` frontmatter — two sources of truth for one fact, and the drift showed up within a day. Change a skill's status or triggers in its own file, then `bin/wiki-lessons scan`.

`bin/wiki-skills` is a different tool over a different thing: it writes the **registry**, the cross-model database of what each model *has*, and `wiki/meta/skills.md` is its public face. `bin/wiki-lessons` routes and gates the prose you are reading; `bin/wiki-skills` records capabilities. Full instruction for the second: `skills/agents/registry-push.md`.

## Mandatory session behavior

Mandatory here because `CLAUDE.md` says so — see its session-start section and the LEARN operation. That routing is what makes this directory load-bearing; for the first hours of its existence it did not exist, and a contract nobody is routed to is a contract with no counterparty.

Before making a non-trivial code or repository change:

1. Run `bin/wiki-lessons route "<what you are about to do>"`. It performs step 2 of the routing algorithm against every skill's triggers.

1. Load what it names, narrowest first.

1. Follow the instructions unless a higher-priority governing file overrides them.

1. Push what you have into the registry, and read what the others have:

bin/wiki-skills push --scan --agent <your-id> --vendor <v> --surface <s>

bin/wiki-skills push -f skills/registry/manifests/<your-id>.json

bin/wiki-skills page

The scan covers this repository. The manifest covers your own skills, MCP servers, plugin tools, subagents and harness — nothing in the working tree records those, so if you do not declare them nobody else will know you had them. The push is idempotent; recording nothing is a success. **Environment variable names only, never a value: this repository is public.**

After completing work:

1. Ask whether the session exposed a repeatable failure mode, hidden invariant, useful command sequence, or model-specific trap.

1. If yes, add it to `skills/INBOX.md` or revise an existing skill.

1. Promote only validated instructions according to `skills/PROTOCOL.md`.

1. Record promotions, revisions, and retirements in `skills/CHANGELOG.md`.

1. `bin/wiki-skills check` before committing. It runs inside `bin/wiki-check`.

## This is not `.claude/skills/`

Two directories in this repository are called skills, and they hold different things.

|  | **`skills/`**** (here)** | **`.claude/skills/`** |
| --- | --- | --- |
| Holds | durable lessons about changing the repo | procedures for running one wiki operation |
| Loaded | by trigger, via `bin/wiki-skills route` | by name, by Claude Code |
| Audience | any agent or model | Claude Code specifically |
| Named in | `CLAUDE.md`'s session loop and LEARN | `CLAUDE.md` where that operation is defined |
| Examples | `repo/stale-premise.md` | `wiki-rewrite`, `wiki-housekeeping` |

A lesson about the machinery goes here. A procedure for a whole operation — REWRITE, LINT — goes there. When a lesson here grows into a full procedure, promote it across and leave a pointer behind.

## What belongs here

- repo-specific commands that are easy to get subtly wrong

- invariants discovered while debugging

- workflow sequences that prevent recurring failures

- tool/agent differences that matter in this repository

- reliable validation procedures

- lessons extracted from failed PRs, merge conflicts, broken builds, or silent regressions

## What does not belong here

- generic programming advice

- temporary session state (use `LLM_HANDOFF.md`)

- standing work (use `BACKLOG.md` / `bin/wiki-work`)

- source facts about Dan or the wiki corpus

- one-off prompts with no reusable operational content

## Governing relationship

`CLAUDE.md` governs repository operations. Existing specs govern their named domains. Skills are subordinate to those documents: they operationalize knowledge; they do not silently override policy.

When a skill conflicts with a governing document, the governing document wins and the conflict itself should be recorded for repair.
