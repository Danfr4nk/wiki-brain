status: active scope: repo triggers:

- editing commands

- editing workflows

- editing build logic

- repository-wide behavior changes sources:

- CLAUDE.md

- AGENT_ACCESS.md validated: 2026-08-30 supersedes: []

# Validate behavior, not merely successful commands

## Instruction

When changing infrastructure or generated/public behavior:

1. Identify the observable contract, not just the command that produces it.

1. Run the narrowest relevant check.

1. Verify the actual artifact or endpoint that users/agents consume.

1. Treat a successful exit code or HTTP 200 as insufficient unless it proves the correct content is being served.

1. When possible, encode the verification into an automated guard so the next agent does not have to remember the incident.

## Why

A system can look healthy while serving the wrong thing. In this repository, deployment previously returned successful HTTP responses while the wrong Pages build path made navigation and agent artifacts unavailable. Silent regressions are worse than loud failures because ordinary workflows falsely conclude that nothing is broken.

## Validation

The check must inspect the relevant produced artifact, endpoint content, or semantic invariant—not only process success.

## Adapter notes

All agents should report the validation they actually ran. Do not claim repository-wide correctness from a local edit or from a tool reporting success alone.
