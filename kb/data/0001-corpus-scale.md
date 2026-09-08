+++
id         = "dat:0001-corpus-scale"
layer      = 1
type       = "datum"
title      = "Corpus holds 192,140 messages across 577 threads"
claim      = "The complete Messages export contains 192,140 messages spanning 2011-03-19 to 2026-09-07, across 577 threads and 498 distinct counterparty handles."
cites      = ["src:imessage-corpus-2026"]
confidence = "high"
extraction = "bin/corpus-stats; figures in corpus/derived/summary.json"
importance = 4
created    = "2026-09-08"
tags       = ["corpus", "scale"]

[when]
start = "2011-03-19"
end   = "2026-09-07"
+++

99,360 sent, 92,780 received. 185,338 carry text; 8,120 carry an attachment.
525 threads are one-to-one and 52 are group threads.
