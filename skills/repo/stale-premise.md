status: active scope: repo triggers:

- a staleness warning

- source_modified or synthesizes: is out of date

- bin/wiki-climb check reports a stale premise

- bin/wiki-plain check reports a stale twin sources:

- CLAUDE.md — "the four things that matter most", rule 3

- SYNTHESIS_SPEC.md

- bin/wiki-climb validated: 2026-08-30 supersedes: []

# Never clear a staleness warning by bumping the date

## Instruction

When a gate reports that a page's premise moved under it:

1. Read what actually changed in the premise — `git log -p` on the member page, not just its new date.

1. Decide whether the conclusion survives the change.

1. Write the decision down on the dependent page: the conclusion stands, is narrowed, or is retracted, and why.

1. Only then update the recorded date, as a record of the re-reading you did.

Do not touch `source_modified:`, `date_modified:` or a `synthesizes:` date before step 2 has actually happened.

## Why

The date field is not the thing being checked; it is the receipt for a check. Bumping it is the one move in this repository that corrupts the system quietly — it converts a true warning into a false all-clear, and no later gate can tell the difference, because the evidence that a re-reading was skipped is exactly the field that was overwritten.

It compounds where it is cheapest to do. A stale Reader's Digest twin cleared by a date bump is a confident, readable, wrong account of what the wiki says, served to the one reader who cannot check it against anything.

## Validation

The dependent page carries a dated line stating what moved and what happened to the conclusion. `bin/wiki-climb check` and `bin/wiki-plain check` return to 0 errors because the premise was re-read, and a reviewer reading the diff can see the reasoning, not only the changed date.

## Known limits

A premise change that is purely mechanical — a typo fix, a link repair, a reformat with no claim touched — needs the re-read but produces no prose: record that in the commit message rather than on the page.
