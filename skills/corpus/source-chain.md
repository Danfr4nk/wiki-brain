status: active scope: repo triggers:

- writing a synthesis or analytical claim from multiple wiki pages

- introducing a new number, date, causal claim, or interpretation into a T2/T3 page

- reconciling conflicting sources

- citing a transcript, profile export, web result, or derived page as evidence sources:

- SYNTHESIS_SPEC.md

- CONNECTIONS_SPEC.md

- skills/repo/stale-premise.md

- skills/corpus/vocabulary-drift.md validated: 2026-09-02 supersedes: []

# Preserve the source chain

## Instruction

When turning corpus material into an analytical claim:

1. Start from the raw or first-party evidence where available; treat derived wiki pages as reasoning surfaces, not stronger evidence merely because they are cleaner.

1. For every new number, date, causal statement, or strong interpretation, keep a traceable source path back to the evidence that actually supports it.

1. Separate what the source explicitly says from what the model infers. Do not upgrade `co-occurs` into `causes`, a transcript into direct observation, or a self-entered profile field into a machine-recorded timestamp.

1. When sources disagree, preserve the disagreement until the evidence justifies resolution. Do not make the contradiction disappear by silently choosing the cleaner source.

1. If the claim depends on a derived analysis such as a keyword count, preserve the search definition, coverage window, denominator and vocabulary assumptions so another agent can reproduce it.

1. Re-check the source chain after upstream pages move or change; a correct conclusion built on stale premises is no longer a validated conclusion.

## Why

The wiki's highest-risk errors are not usually fabricated facts; they are true-looking conclusions whose evidentiary chain has been silently weakened. Recent corpus work exposed vocabulary drift, self-entered-vs-generated timestamp conflicts, and the distinction between raw evidence and derived interpretation. The repository's synthesis and connection specifications already treat provenance and relationship type as analytical commitments. This skill turns those constraints into a repeatable agent behavior.

## Validation

For any new synthesis claim, an independent agent should be able to follow its cited source path, identify the original evidence, reproduce any stated calculation, and tell which parts are observation versus inference. Run the relevant repository checks and stale-premise checks before considering the claim settled.

## Known limits

This is not a ranking system that automatically declares one source truthful. It governs traceability and epistemic labeling. Domain-specific source rules and governing specifications remain authoritative when they are more specific.
