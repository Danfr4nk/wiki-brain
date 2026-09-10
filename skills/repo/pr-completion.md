status: active scope: repo triggers:

- asked to commit repository work

- asked to open or update a pull request

- completing a multi-file repository change

- a task touches generated or derived surfaces sources:

- skills/repo/session-loop.md

- skills/repo/change-safety.md

- skills/repo/derived-surfaces.md

- skills/README.md validated: 2026-09-02 supersedes: []

# Complete the change, not merely the write

## Instruction

Before calling a repository task complete:

1. Identify the canonical source files and every generated or derived surface the change can affect.

1. Inspect the final diff, not just the individual writes. Confirm that the diff contains the intended change and no accidental collateral edits.

1. Run the repository gate (`bin/wiki-check`) after regeneration of every derived surface that the change touches.

1. Verify the target branch, PR base, changed-file set, and resulting repository state. A successful write or API response is not completion evidence.

1. If the repository has an agent/PR activity mechanism, record what the model actually did and discovered rather than only repeating the user's request.

1. Only then report the work as complete; if validation cannot be run, state exactly which validation remains outstanding.

## Why

Repository work can succeed at the write layer while failing at the system layer: a generated twin can remain stale, a browser/API write can land on the wrong branch, or a successful command can leave the intended artifact absent. The session loop already requires a gate, but making final-state verification an explicit completion condition prevents the common failure of treating "the tool said success" as "the repository is correct." This is especially important as multiple agents work concurrently and PRs become the durable handoff between sessions.

## Validation

Run `bin/wiki-check` and inspect the final branch diff before opening or declaring a PR complete. For a PR, confirm the PR's base/head and changed files through the repository interface and ensure the expected artifact is present on the head branch.

## Known limits

This does not replace domain-specific validation or the derived-surface skill. It is the final completion gate across them. If the repository's activity-log mechanism is absent, do not invent one; record the discovery as a candidate lesson instead.
