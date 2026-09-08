+++
id         = "evt:2026-09-08-rebuild-begins"
layer      = 2
type       = "event"
title      = "Rebuild on the six-layer architecture begins"
cites      = ["dat:0006-drive-copy-lossy"]
confidence = "high"
importance = 4
created    = "2026-09-08"
tags       = ["meta", "architecture"]

[when]
date = "2026-09-08"

[[edges]]
rel    = "about"
target = "ent:wiki-brain"

[[edges]]
rel          = "influenced"
target       = "evt:2026-09-08-corpus-supersedes-fragments"
note         = "The corpus work established the epistemic argument the architecture then generalised into a checked invariant."
+++

## What happened

The wiki was rebuilt against `src:conceptual-spec-2026`, replacing a flat
markdown tree with a six-layer graph whose citation rule is machine-enforced by
`bin/wb-validate`.

The generalisation worth noting: the corpus work had already established, for
message evidence specifically, that partial data produces confident error. The
architecture turns that from a policy about one source into a property of the
whole graph.
