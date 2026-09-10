+++
id          = "ent:wiki-brain"
layer       = 2
type        = "entity"
entity_kind = "project"
title       = "Wiki Brain"
cites       = ["dat:0004-fragment-exports"]
confidence  = "high"
importance  = 5
created     = "2026-09-08"
tags        = ["meta", "project"]

[when]
start = "2025"

[[edges]]
rel    = "about"
target = "ent:dan"
+++

## Summary

A source-grounded longitudinal knowledge graph and cognitive modeling system.
Archives raw evidence about a person and their world, transforms it into atomic
facts, events, entities, relationships, patterns and syntheses, and gives an LLM
persistent context — without collapsing evidence, interpretation and inference
into the same layer.

Projects are longitudinal entities. This one has had at least two architectures:
a plain-markdown wiki compiled by an LLM, and the layered graph specified in
`src:conceptual-spec-2026` and built here.
