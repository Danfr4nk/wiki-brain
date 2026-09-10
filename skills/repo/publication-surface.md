status: active scope: repo triggers:

- adding data files to the repository

- changing .gitignore

- deciding whether something is private

- writing to the repository from a browser or the contents API sources:

- CLAUDE.md — the intake/ bullet

- intake/README.md

- log.md — 2026-08-30 validated: 2026-08-30 supersedes: []

# Know what a commit publishes, and that .gitignore is not a privacy control

## Instruction

Before adding or tracking any file that carries personal data:

1. Establish whether the repository is public. If it is, treat every tracked byte as permanently published — git history cannot be un-published.

1. Do not reach for `.gitignore` as a privacy mechanism. It governs `git add` and nothing else; it does not touch GitHub's contents API, which is how the portal and ボスの部屋 write from a browser.

1. To make something private, make the **repository** private first, verify it, and only then decide whether ignoring the file is still wanted. That order, always.

1. Say plainly, in the file that governs the data, what the arrangement publishes. A reader must not have to infer it.

## Why

The intake ledger passed through two arrangements that each defeated its own purpose before the current one: gitignored kept the record out of reach of every session that might cite it, and sealed with AES-256-GCM kept the analysis layer from reading it too. A ledger the wiki cannot open has no reason to be here. The operator resolved it on 2026-08-30 by tracking the files in the open, knowing what that publishes.

The trap worth carrying forward is narrower and easier to repeat: `.gitignore` reads as a privacy control and is not one. A file ignored locally is still writable — and readable — through the contents API, so an ignore rule can leave a session believing data is withheld while a browser client writes it to the same public repository.

## Validation

State the repository's visibility and the file's tracked status explicitly, having checked both, rather than inferring either. A change that makes data less public is verified against the live repository before the data is treated as private.

## Known limits

This is about deliberate publication of the subject's own data, which is an operator decision and not a session's to reverse. It is not licence to add third-party personal data: the standing moratorium in `CLAUDE.md` governs there and outranks this skill.
