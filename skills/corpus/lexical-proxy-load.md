status: active scope: corpus triggers:

- building a gate, filter or score on top of a regex over a corpus

- reusing another tool's pattern table for a heavier purpose than it was written for

- a measurement contradicting an established page, especially a confident one

- about to publish a number that instructs other sessions to re-read pages sources:

- bin/psychometrics — module docstring, the "I'm 99% sure" age-pattern false positive

- bin/wiki-traits — PROXY_REVIEW, and the verdict cap it implements

- tests/test_wiki_traits.py — VerdictCap, ReviewRegister

- wiki/mind/profile/trait-corpus-map.md — "The state of the instrument" validated: 2026-09-06 supersedes: []

# A lexical proxy good enough to start a conversation is not good enough to gate one

## Instruction

1. **Before a regex over a corpus is allowed to produce a verdict, read its matches.** Not a sample chosen to reassure you — `--examples N` output, in full, asking one question of each: *is this row the construct, or a string that resembles it?*

1. **Record the review where the tool can read it**, keyed to the proxy, with the string that breaks it named. A review held in a session transcript is a review the next run does not have.

1. **Cap the unreviewed.** An unreviewed proxy may not confirm a score and — this is the load-bearing half — may not contradict one. Report such a result under its own name (`unreviewed`), **never as silence**: *silent* is a finding, meaning an instrument ran and came back empty, and reusing that word for "nobody checked" claims a measurement that never happened.

1. **Exclude the broken outright rather than deleting them.** A proxy read and found broken is a finding; deleting it makes it look unwritten and invites the next session to write it again.

1. **A trait whose every proxy is broken bands as ****`no instrument`****, never ****`silent`****.** Silence implies an instrument ran and found nothing. They are different claims and collapsing them asserts a measurement that never happened.

1. **Hold reach and support patterns to the same standard.** A pattern used only for context still moves a row into a louder band and manufactures an obligation.

## Why

`bin/psychometrics` built its 23-proxy table for an exploratory sheet a human reads top to bottom, and its docstring says outright that the matches must be read before the counts are believed. `bin/wiki-traits` reused that table under a much heavier load — a filter constraining what every future synthesis may claim about registers 1, 2 and 11 of the constitution pass.

Its first run reported **`CONTRADICTED LOAD`**** on the Fe deficit**: an instruction to re-read 37 pages, 17 of them synthesis. The verdict rested on one proxy for *other-directed concern*, and every match was Dan being comforted — *"Thank you for making me feel better sweetie"*, *"those are the things you always make ME feel better about"*. The pattern caught `feel better` and could not tell who was doing the feeling.

Six of 23 proxies broke the same way once read:

| **Proxy** | **What it actually caught** |
| --- | --- |
| `altruism / other-directed concern` | Dan receiving comfort — the inverse of the construct |
| `altruism / offering help unprompted` | Transactional offers: "I'll have suz car if you need a clean getaway" |
| `sympathy / sympathy tokens` | First-person apology, not sympathy extended — right by accident |
| `assertiveness / directives` | The anti-directive: "I want you to do things however you feel most comfortable" |
| `vulnerability / overwhelm` | Idiom: "too much of a babe", "I'm done smoking cigs" |
| `impulsiveness / immediacy` | Anticipation: "can't wait to see you" |

Three reach patterns broke the same way. `left`, intended for political register, matched **"Checked, left standing"** — constitution-pass boilerplate present on every synthesis page — and inflated one trait's reach from 34 pages to 202, moving it into a cell that manufactured an obligation.

**The asymmetry is what makes the cap necessary.** Inherited from `psychometrics`: failure to corroborate is not falsification, so only an inversion is evidence against a score. That makes `INVERTED` the heaviest verdict in the system — and it is simultaneously the cheapest to manufacture, because a pattern that catches the wrong side of a conversation inverts trivially. The heaviest verdict must therefore be the hardest to reach, which is the opposite of what an unreviewed regex delivers.

## Validation

python3 -m unittest tests.test_wiki_traits -v   # VerdictCap, ReviewRegister, Traits

bin/wiki-traits review                          # the queue: 16 unreviewed, 6 broken, 1 sound

bin/psychometrics run --facet <facet> --examples 8   # how a review is actually done

`test_unreviewed_cannot_contradict` is the regression. If it is ever relaxed, the first run's false headline becomes publishable again.
