status: active scope: corpus triggers:

- counting messages or searching the iMessage dump

- a claim about how often or how much Dan writes

- measuring message length, cadence, or response time

- reaching for grep over raw/ message exports sources:

- bin/mine-messages — "Why this file exists rather than ad-hoc greps"

- bin/text-metrics — "Why turn-level rather than message-level"

- wiki/mind/profile/texting-deviance-audit.md validated: 2026-08-30 supersedes: []

# Mine the message corpus with the instruments, not with grep

## Instruction

1. To find or count messages, use `bin/mine-messages` (`stats`, `grep`, `timeline`, `battery`, `entities`). Do not use shell `grep` over the export.

1. For any claim about **length or cadence** — how much he writes, how fast he answers, how his style moved — use `bin/text-metrics`, not `mine-messages`.

1. Re-derive every number at the point you cite it. Do not copy a figure forward from another page.

1. Quote the figure with what produced it, so the next agent can re-run it.

## Why

Three properties of the dump make naive `grep` quietly wrong — it splits one message across several lines and miscounts, among others — and quietly wrong is the failure that matters, because the number still looks like evidence.

The unit error is worse, because it inverts the finding rather than blurring it. `mine-messages` counts messages, and 98% of Dan's messages are one line with a median of 6 words, so a message-level read makes him look unremarkable. The unit that corresponds to one thing said is the **turn**. Measured that way he runs 3.05x his interlocutors' words in 2026 against 1.23x in 2015–19 — the entire effect the page exists to document, invisible at the wrong unit.

## Validation

The command that produced the figure is named next to it and re-runs to the same number. A style claim cites `bin/text-metrics`; a volume or occurrence claim cites `bin/mine-messages`.

## Known limits

`bin/text-metrics` defaults to `imessage_export_deep_20260813.csv`, the only sender-tagged export reaching past 2025; a question about an earlier period may need a different source named explicitly. Neither tool may be pointed at the Annie corpus for new material — that is closed under the standing moratorium in `CLAUDE.md`, which outranks this skill.
