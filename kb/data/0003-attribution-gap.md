+++
id         = "dat:0003-attribution-gap"
layer      = 1
type       = "datum"
title      = "3,086 messages cannot be placed in any thread"
claim      = "3,086 messages (1.6% of the corpus) carry no counterparty field of any kind. They are sent messages with no chat_identifier and no destination_caller_id."
cites      = ["src:imessage-corpus-2026"]
confidence = "high"
extraction = "bin/corpus-stats; summary.json -> unattributable_to_a_thread"
importance = 4
created    = "2026-09-08"
tags       = ["corpus", "limits"]
+++

5.3% of rows arrive with no `chat_identifier`. Most are recoverable — a received
message names its sender, some sent messages carry `destination_caller_id`.
This 1.6% is the irreducible remainder.

They could be assigned by interleaving them with surrounding messages. They are
not, and that choice is the point: per-thread totals are floors rather than
exact counts, which is a smaller cost than a number that looks exact and isn't.
