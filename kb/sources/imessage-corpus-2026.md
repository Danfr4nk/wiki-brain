+++
id          = "src:imessage-corpus-2026"
layer       = 0
type        = "source"
title       = "Complete Messages export (2026-09-07)"
source_type = "message-corpus"
acquired    = "2026-09-08"
provenance  = "Apple Messages chat.db, exported whole and staged as a Google Sheet. Downloaded to corpus/messages.csv; integrity recorded in corpus/manifest.json."
reliability = "primary"
confidence  = "high"
sensitive   = true
importance  = 5
created     = "2026-09-08"
tags        = ["corpus", "authoritative"]

[when]
start = "2011-03"
end   = "2026-09"
+++

## What this is

The authoritative message record: every message in the source database, not a
per-counterparty slice of it. 45 columns, zero malformed rows on parse.

## Why it is marked sensitive

It contains the phone numbers, email addresses and private words of 498 people
who did not choose to be published. It is gitignored and excluded from every
built artifact. Derived layers may cite it; they may not reproduce it.

Governing rules: `CORPUS_POLICY.md`.
