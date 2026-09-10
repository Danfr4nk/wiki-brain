+++
id          = "con:gitignore-is-not-protection"
layer       = 3
type        = "contradiction"
title       = "The corpus is closed in git and open on the web"
cites       = ["dat:0005-sheet-public", "dat:0001-corpus-scale"]
confidence  = "high"
importance  = 4
resolved    = false
created     = "2026-09-08"
tags        = ["privacy", "decision"]

[when]
date = "2026-09-08"
+++

## The two sides

**Closed:** `corpus/messages.csv` and `corpus/private/` are gitignored. The
repository is public and git history is permanent and searchable, so keeping the
corpus out of it is worth doing on its own terms.

**Open:** the backing sheet is shared "anyone with the link" and downloads in
full with no credentials (`dat:0005`). Anyone holding the URL has all 192,140
messages and 498 people's contact details.

## Why this is not resolved

It is not an error to correct. The exposure was raised with the operator, with
the unauthenticated download demonstrated rather than asserted, and the decision
was to leave the sharing as it is. That decision stands.

What the contradiction records is the consequence, so it stays visible: **the
gitignore is not what protects this data.** The two measures address different
exposures and only one of them is closed. Anything reasoning about the privacy
posture of this corpus should read both sides rather than the reassuring one.
