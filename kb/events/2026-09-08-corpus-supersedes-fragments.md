+++
id         = "evt:2026-09-08-corpus-supersedes-fragments"
layer      = 2
type       = "event"
title      = "Complete corpus supersedes the fragment exports"
cites      = ["dat:0001-corpus-scale", "dat:0004-fragment-exports", "dat:0002-group-threads"]
confidence = "high"
importance = 5
created    = "2026-09-08"
tags       = ["corpus", "shelf", "decision"]

[when]
date = "2026-09-08"

[[edges]]
rel    = "supersedes"
target = "dat:0004-fragment-exports"

[[edges]]
rel    = "about"
target = "ent:wiki-brain"
+++

## What happened

The complete Messages export replaced every prior per-counterparty extract as
the sole admissible source of message evidence. The fragments were shelved:
demoted from evidence, retained as the record of what was believed and why.

Rules: `CORPUS_POLICY.md`. Inventory: `shelf/MANIFEST.md`.
