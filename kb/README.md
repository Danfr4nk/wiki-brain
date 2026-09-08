# kb/

The knowledge base. One Markdown file per node, TOML frontmatter for machines,
prose body for humans.

Design: [`../ARCHITECTURE.md`](../ARCHITECTURE.md). Contract:
[`../schema/node.schema.json`](../schema/node.schema.json).

## Adding a node

Use `bin/wb-new`. It refuses to create a node that cannot be correct, which is
the point — hand-written frontmatter is where a knowledge base rots, because the
inconvenient required field gets skipped and six months later nobody can tell
whether the datum ever had a source.

```sh
# L0 — the raw material
bin/wb-new source --title "Journal 2019-2021" --source-type journal \
    --provenance "Three notebooks, photographed 2026-09" --reliability primary

# L1 — one claim, from that material
bin/wb-new datum --title "Moved to Pittsburgh" \
    --claim "Moved to Pittsburgh in March 2016" \
    --cites src:journal-2019-2021 --date 2016-03

# L2 — the structured object
bin/wb-new event --title "Move to Pittsburgh" --date 2016-03 \
    --cites dat:0007-moved-to-pittsburgh

# L3 — what it might mean, and whose reading that is
bin/wb-new interpretation --title "Moves track job loss, not restlessness" \
    --perspective external --cites evt:move-to-pittsburgh --confidence moderate

bin/wb-validate
```

Then write the body. The frontmatter carries the structure; the body carries
what a person actually needs to read.

## Which layer

Ask what kind of thing the claim is, not how confident you feel about it.

| You are recording | Layer | Type |
| :---- | :-- | :---- |
| Material you acquired | 0 | `source` |
| One claim from that material | 1 | `datum` |
| A person, place, thing, happening, or bond | 2 | `entity` `event` `relationship` |
| What something means | 3 | `interpretation` |
| Two things that disagree | 3 | `contradiction` |
| Something that keeps happening | 4 | `pattern` |
| A model spanning domains | 5 | `synthesis` |

The rule that decides most hard cases: **if it would still be true had nobody
thought about it, it is evidence. If it requires a thinker, it is a reading.**
"He sent 40,000 messages in 2018" is L1. "2018 was his most connected year" is
L3 — it needs someone to decide what connected means.

## Things that will be rejected

- **A datum with no source.** That is not a datum, it is a belief, and a belief
  belongs at L3 where it can be challenged.
- **A citation pointing up or sideways.** Evidence sits strictly below the claim
  it supports. A datum citing an interpretation is a conclusion laundered into a
  premise, and it is the single failure this whole system exists to prevent.
- **An interpretation with no `perspective`.** Self, external, llm and other are
  not interchangeable. Collapsing them loses the most valuable sentence the
  system can produce: *the subject believes X about himself, and the record
  suggests Y.*
- **A `caused` edge with no `causal_basis`.** Sequence is not causation. Use
  `preceded` if that is all you have.
- **A padded date.** `YYYY`, `YYYY-MM` or `YYYY-MM-DD`. Do not turn "spring
  2018" into `2018-03-01` — use `approx` and keep the imprecision honest.

## Sensitive nodes

`sensitive = true` withholds a node from every published artifact. This
repository is public, and the message corpus holds 498 other people's phone
numbers and private words.

Derived nodes may cite a sensitive source and remain publishable, as long as the
body carries only what does not identify anyone — aggregate counts, shape,
structure. `wb-validate` warns on every such node so the judgment gets made
deliberately rather than by default, and `bin/wb-check-publish` verifies the
exclusion actually happened before anything deploys.

Withheld citations are *declared* on the built page, never silently dropped. A
partial evidence trail must not be able to look complete.

## Corrections

Nodes are corrected, not overwritten, and the record of the correction is itself
worth keeping.

- **Wrong reading** — revise the L3 node freely. That is what L3 is for.
- **Superseded by better evidence** — create the replacement and add a
  `supersedes` edge. The old node stays; how the model changed is data.
- **Wrong source** — L0 is append-only. Add a `contradiction` recording the
  conflict rather than editing the source into agreement with you.
- **A claim that turned out false** — keep the datum, add the contradicting
  datum, and let the contradiction node hold both. Resolving it prematurely
  destroys the thing that made it interesting.
