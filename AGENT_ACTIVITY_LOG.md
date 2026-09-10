# Agent Activity Log

A persistent, append-only ledger of substantive work performed by LLMs and agents in `wiki-brain`.

## Operating rule

Every PR created for work in this repository MUST include an **Agent Activity Log** entry before the PR is considered ready for merge. The entry is written by the model/agent that performed the work and should describe what it actually did, not merely restate the PR title.

The canonical ledger lives in this file. Each PR also carries the relevant entry in its PR body or a top-level PR comment so the local review trail and the repository-wide history stay linked.

### Required workflow

1. Agent receives a task.

1. Agent inspects the relevant wiki/repository state and identifies the work actually performed.

1. Agent makes changes on a branch.

1. Before opening or finalizing the PR, the agent appends one entry to this file on that branch.

1. Agent opens the PR with a copy of the entry, or posts the entry as a top-level PR comment if the PR already exists.

1. If the PR changes materially after review, append a follow-up entry rather than silently rewriting history.

1. On merge, the PR's entry becomes part of the permanent running ledger on `main`.

**No entry = incomplete agent workflow.**

## Entry contract

Each entry must contain:

- **Timestamp:** when the work was performed (local ISO-8601 time when available)

- **PR:** PR number, or `pending` until assigned

- **Agent/model:** the model or agent identity as reported by the executing system; do not guess

- **Task:** the user's requested objective

- **Work performed:** concrete actions taken (inspection, search, extraction, analysis, edits, tests, verification)

- **Files / areas touched:** paths or repository areas actually changed or inspected when useful

- **Reasoning summary:** brief explanation of important decisions, constraints, or rejected approaches

- **Validation:** what was checked, and what was not checked

- **Result:** what changed and the current status

- **Open questions / follow-up:** unresolved items, risks, or `None`

Do **not** fabricate tool calls, tests, confidence, sources, file reads, or results. The log is a provenance record, not a performance review.

## Standard entry template

## YYYY-MM-DD HH:MM:SS ±HH:MM — PR #<number|pending>

- **Agent/model:** <reported identity>

- **Task:** <objective>

- **Work performed:** <concrete sequence of actions>

- **Files / areas touched:** <paths / areas>

- **Reasoning summary:** <important decisions and why>

- **Validation:** <checks run; explicitly name anything not verified>

- **Result:** <what changed / status>

- **Open questions / follow-up:** <None or specific items>

## Log entries

## 2026-09-02 20:00:00 -04:00 — PR #pending

- **Agent/model:** GPT-5.6 Luna

- **Task:** Create a new wiki-brain system in which every new PR includes a model-authored description of the work performed in a running activity log.

- **Work performed:** Inspected the repository root and the existing agent-access documentation; identified the repository's agent workflow documentation as the appropriate enforcement surface; created this append-only ledger and defined the required PR/agent procedure and entry schema.

- **Files / areas touched:** `AGENT_ACTIVITY_LOG.md`; planned follow-up integration in `AGENT_ACCESS.md`.

- **Reasoning summary:** The log needs to be both repository-persistent and PR-visible. A PR comment alone would fragment history; a file alone would hide the entry from PR review. The system therefore makes the ledger canonical while requiring the same entry to accompany each PR. Follow-up entries preserve provenance when work changes after the initial entry.

- **Validation:** Confirmed the repository contains existing LLM/agent access documentation and that the new branch was created from `main`. No automated tests are applicable to this documentation-only change.

- **Result:** Established the canonical append-only activity ledger and a concrete contract for future model/agent work.

- **Open questions / follow-up:** Add the same requirement to the primary agent instructions so future agents encounter it before creating PRs.
