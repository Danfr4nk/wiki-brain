+++
id          = "int:fragments-silently-partial"
layer       = 3
type        = "interpretation"
title       = "The fragments failed by being silently partial, not by being wrong"
perspective = "external"
cites       = ["dat:0004-fragment-exports", "dat:0002-group-threads", "dat:0001-corpus-scale"]
confidence  = "high"
importance  = 5
created     = "2026-09-08"
tags        = ["epistemics", "shelf"]

alternatives = [
  "The fragments were simply too few, and enough of them would have been adequate — this fails to account for group threads, which no number of per-counterparty exports can represent.",
  "The conclusions were wrong for ordinary reasons (haste, motivated reasoning) and the export shape is incidental.",
]

[[edges]]
rel    = "challenges"
target = "dat:0004-fragment-exports"
+++

## The reading

Each fragment was accurate about the thread it covered. The failure was frame,
not accuracy — and a partial document is worse than a false one, because a false
document can be caught by reading it and a partial one cannot. It never
announces what it left out.

The specific mechanism: **in a fragment, absence of evidence is
indistinguishable from evidence of absence.** Read one thread in isolation and
the inferences that follow — contact stopped, a subject never came up, a period
was quiet, someone was not around — are all claims about what is *not there*. A
fragment cannot support a claim about what is not there. Only a complete record
can.

## Why this is an interpretation and not a fact

That the exports were per-counterparty is a fact (`dat:0004`). That 52 group
threads exist is a fact (`dat:0002`). That this *explains the erroneous
conclusions* is a reading of those facts, and it is recorded at L3 where it can
be challenged without disturbing the evidence underneath.

Competing explanations are recorded in `alternatives` rather than dismissed.
