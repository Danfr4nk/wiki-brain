+++
id         = "dat:0004-fragment-exports"
layer      = 1
type       = "datum"
title      = "Prior message evidence was per-counterparty fragments"
claim      = "Message evidence before 2026-09-08 consisted of per-counterparty exports, each covering one conversation partner at a time."
cites      = ["src:wiki-brain-git-history"]
confidence = "high"
extraction = "Filenames observed in the pre-migration tree, of the form imessage_export_<handle>_<timestamp>."
importance = 4
created    = "2026-09-08"
tags       = ["corpus", "shelf"]

[when]
end = "2026-09-08"
+++

Each fragment was accurate about the thread it covered. Inventory:
`shelf/MANIFEST.md`.
