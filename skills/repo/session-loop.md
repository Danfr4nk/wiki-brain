status: active scope: repo triggers:

- any multi-step code or repository task sources:

- CLAUDE.md validated: 2026-08-30 supersedes: []

# Preserve the repository session loop

## Instruction

For substantial repository work:

1. Read `LLM_HANDOFF.md` and `operator-log.md`.

1. Run `bin/wiki-work`.

1. Do the operator's requested task in full.

1. Return to outstanding obligations and handle them in priority order.

1. Record remaining state in `LLM_HANDOFF.md` rather than leaving discoveries trapped in session context.

1. Capture any reusable operational lesson in `skills/INBOX.md` or an existing skill.

## Why

The repository separates current session state from durable reusable knowledge. `LLM_HANDOFF.md` answers "where are we now?"; `skills/` answers "what have agents learned about doing this kind of work?" Mixing them causes either stale instructions to become permanent or durable lessons to disappear when the handoff rotates.

## Validation

Before ending the task, another agent should be able to answer both questions without access to the original conversation:

- What remains to be done now?

- What reusable instructions were learned for future work?
