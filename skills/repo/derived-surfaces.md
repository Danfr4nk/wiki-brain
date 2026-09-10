status: active scope: repo triggers:

- editing a wiki page that the portal renders

- working in caakehorn/home or public/wiki

- a merged change that disappeared

- editing generated files, llm/, DIGEST.md, RECENT.md, OPEN.md, WORK.md, INDEX.md sources:

- CLAUDE.md — the portal bullet

- log.md — 2026-08-17 restore | timeline

- bin/wiki-freshness validated: 2026-08-30 supersedes: []

# Write to the source, never to the surface it generates

## Instruction

Before editing any file, establish whether it is a source or a derivation of one.

1. If the file is generated, edit the thing it is generated *from*, then rerun the generator. `DIGEST.md`, `RECENT.md`, `OPEN.md`, `wiki/meta/*`, `llm/**`, `WORK.md`, `skills/INDEX.md`, `intake/units.json` and `wiki/timeline/master-timeline.md` are all derivations.

1. If you are editing a wiki page as JSON, stop — you are in the portal repository. Pages are `wiki/**.md`, in wiki-brain.

1. Never hand-edit `public/wiki/**` in `caakehorn/home`. It is deleted and rebuilt from this repository on dispatch and hourly.

1. After a content pass, run the generators before committing. `bin/wiki-check` does this in the correct order — generate, then gate, then scan.

## Why

A derived file accepts an edit exactly as readily as a source does, and then discards it on a schedule. The failure is silent, delayed, and looks like nothing happened: on 2026-08-17 a December 2015 read pass was written into the portal's derived snapshot, merged, and deleted by the rebuild cron 39 minutes later. A second pass of the same work was written into the snapshot as well. The work was real; the surface it was written to was not the record.

The mirror image is drift: a source edited without rerunning its generator leaves the derivation stale while every gate stays green. The 2026-08-20 audit found `llm/manifest.json` eleven pages behind `wiki/` for that reason.

## Validation

`bin/wiki-freshness` compares the generated corpus against `wiki/` and names every page missing, orphaned or changed; `bin/wiki-check --check-only` answers the reviewer's question — is what is committed already consistent — without writing anything. For a portal-visible change, confirm the page is live on the site, not merely that the commit merged.

## Known limits

`wiki/**/archive/` is pinned and exempt. A generated file may be edited when the change is to the generator's *output format* and the generator is edited in the same commit — the rule is against edits the next run will silently discard, not against touching the file at all.
