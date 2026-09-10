+++
id         = "dat:0006-drive-copy-lossy"
layer      = 1
type       = "datum"
title      = "The Drive staging copy corrupts markdown"
claim      = "Every .md file in the Google Drive staging copy was converted to a Google Doc on upload. Exporting back to markdown returns escaped punctuation, flattened code fences, and relative links rewritten as invalid absolute URLs."
cites      = ["src:wiki-brain-git-history"]
confidence = "high"
extraction = "Observed directly by exporting README.md from Drive and diffing against expectations."
importance = 3
created    = "2026-09-08"
tags       = ["migration"]

[when]
date = "2026-09-08"
+++

Observed damage: `\+`, `\-`, `\#` escapes through prose; fenced code blocks
flattened into paragraphs; `[AGENT_ACCESS.md](AGENT_ACCESS.md)` returned as
`[AGENT\_ACCESS.md](http://AGENT_ACCESS.md)`.

The damage is plausible-looking markdown rather than an obvious break, which is
what makes it dangerous across a 1,000+ file tree.
