# shelf/

Superseded message extracts. Retired 2026-09-08, kept on purpose.

Everything here was produced before the complete Messages export existed —
per-contact exports, pasted transcripts, hand-copied excerpts. All of it is
**shelved**: demoted from evidence, not deleted.

## Why it is kept at all

Because you cannot correct a conclusion whose origin you have thrown away.

These files are the record of what the wiki was working from when it drew
conclusions that the complete corpus now contradicts. Deleting them would
leave the wrong conclusions in place with no way to see where they came
from — the claims would survive their own sources. That is the worst of both
outcomes, so the fragments stay.

## The one permitted use

> Evidence about **what was believed and why it was wrong**.
> Never evidence about **what happened**.

Full rules in [`CORPUS_POLICY.md`](../CORPUS_POLICY.md). The short version:
these files can tell you why a claim was made. They cannot tell you whether it
was true. For that, and for anything new, use the corpus:

```sh
bin/corpus-query --who "Name" --context 3
```

## Nothing here is tracked in git

`.gitignore` keeps this directory's contents out of the repository — this repo
is public, and shelved extracts contain exactly the same personal material as
the corpus, belonging to exactly the same people. Only this README and
`MANIFEST.md` are committed.

`MANIFEST.md` lists what is on the shelf, so the *inventory* is public and
reviewable even though the contents are not — you can see that a fragment
existed, when it was taken and what it covered, without the file itself.

## Adding to the shelf

Anything message-derived that predates 2026-09-08 belongs here. When you shelve
something, add a `MANIFEST.md` row recording what it covered and, where it is
known, which wiki pages were built on it. That link is the whole point: it is
what turns "this old file exists" into "these seven claims need re-verifying".
