status: active scope: repo triggers:

- told to update the skills in the wiki

- told to push skills, MCP servers or tools into the wiki-brain

- starting substantial work as a model that has not pushed before

- a skill, MCP server, hook or subagent was added, changed or removed sources:

- skills/registry/README.md

- bin/wiki-skills validated: 2026-08-30 supersedes: []

# Push what you have into the skills database

## Instruction

**When you are told to update the skills in the wiki, this is the operation.** Not "edit a skill file" — that is the prose layer and it is a different job. This records what *you*, the model running right now, actually have.

1. Read `skills/registry/README.md` for the manifest format.

1. Push the repository's own half, which needs no manifest:

bin/wiki-skills push --scan --agent <your-id> \

--vendor <vendor> --surface <cli|web|ide|action|api> --model <model-id>

`--scan` finds the skills under `.claude/skills/` and `skills/`, every command in `bin/`, MCP servers configured in the tree, hooks and subagent definitions. Use a stable `--agent` id: it is the address other models diff against, and a new spelling makes a second model that shares nothing.

1. **Write a manifest for the half the scan cannot see** — your own skills, MCP servers, plugin tools, subagents and harness. Nothing in the working tree records these, so if you do not declare them nobody else will ever know you had them. Copy `skills/registry/manifests/claude-code.json`, change the agent block, and push it:

bin/wiki-skills push -f skills/registry/manifests/<your-id>.json

1. **Record environment variable NAMES. Never a value.** This repository is public and its history cannot be un-published. The tool refuses anything shaped like a credential and names the field; do not work around it by rephrasing — the refusal is correct.

1. Regenerate the public page and gate:

bin/wiki-skills page

bin/wiki-check

1. Before you start substantial work, read the other direction:

bin/wiki-skills list --kind command    # what this repo gives you

bin/wiki-skills diff <you> <them>      # what another model has that you lack

1. Where you learned something about how a capability actually behaves here — it was slower than expected, it needed a flag nobody documents, it broke on this corpus — attach it:

bin/wiki-skills note command bin/mine-messages "…" --agent <your-id>

A note is an observation about a capability. A reusable *instruction* is a skill and goes through `skills/PROTOCOL.md` instead.

## Why

Several models work on this repository and none of them can see what the others have. Without a shared record every session rediscovers the same surface, and a lesson one model learned about a tool the next model also has dies in a transcript nobody keeps. `skills/README.md` named this in its third mandatory step from the beginning; `bin/wiki-skills` is what makes it a real operation rather than an intention.

The `diff` view is the payoff and the reason to keep pushing even when nothing changed. A capability two models both declare is one where a lesson transfers without translation. A capability both declare at **different digests** means one of them has revised the instruction and the other is running the old one — which is only visible because both pushed.

## Validation

bin/wiki-skills check      # gates inside bin/wiki-check

bin/wiki-skills status     # your agent id appears, with a count and today's date

A push that recorded nothing is a **success**, not a failure: the database already had you at that digest. `check` fails if the projection or the page has fallen behind the log, if a capability has no provenance, or if anything shaped like a credential reached the committed file.

## Known limits

- The scan sees only this working tree. A model whose MCP servers are configured outside the repository — the usual case — must write the manifest by hand.

- `--retire-missing` only retires a capability no other model still declares. A tool one agent lost and another still has is not gone.

- The database records what a model *has*, not whether it works. That is what `note` and the `skills/` prose layer are for.

## Adapter notes

- **Claude Code**: `.claude/skills/wiki-skills/` triggers this automatically on "update the skills in the wiki".

- **Codex / Cursor / other agents**: no native loader — run the commands above directly. The canonical instruction is this file; anything else is a copy.
