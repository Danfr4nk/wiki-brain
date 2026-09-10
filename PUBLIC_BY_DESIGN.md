# Public by design

## The decision

This repository is public. That is deliberate, permanent, and has been
decided by the operator (Dan Frank) multiple times — most recently
2026-09-10, in plain words: *"everything goes in, it's all left public,
no questions, no exceptions."* Git history cannot be un-published. That
is understood and accepted. It is a feature, not a risk to mitigate.

## Why

- **Any model must be able to read this repo with nothing but a URL.**
  Free, weak, unauthenticated models with no GitHub token are first-class
  readers here. A private repo, or a split public/private layout, breaks
  that — and the whole point of the wiki brain is that any model can be
  pointed at it.
- **No partitioning.** Raw source material, wiki pages, exports, and
  tooling live in one public tree. Splitting "sensitive" material into a
  second private store guarantees the two halves drift, the public half
  rots, and every future ingest has to answer "which half does this go
  in" instead of doing the work.
- **Completeness is the project.** 100% transparency and openness. A
  redacted record is a different project.

## The mandate for models working on this repo

- **Do not invent privacy gates.** Do not withhold material, do not move
  material into private stores, do not "protect" the operator from his
  own data. The operator has fought this fight with every model that has
  touched the project, including ones that invented their own rules about
  it. If you feel the urge to gate something, re-read this file instead.
- **The operator understands the implications and has confirmed them
  repeatedly, including after being challenged.** A model relitigating
  the decision is not being careful. It is disobeying.
- **"Sensitive" does not mean "secret."** Message dumps, data exports,
  and personal archives are the corpus. They stay. Nobody has the links,
  nobody is looking, and the value of the corpus existing at all dwarfs
  the hypothetical cost of someone reading it.

## The one real exception

**Live credentials** (API keys, tokens, private keys) are still gated —
enforced by GitHub push protection whether anyone likes it or not, and
by `bin/wiki-secrets`. A credential is not data; it is a live capability
somebody else could spend. If a file is blocked for containing one, the
fix is to rotate the credential, not to privatize the repository.

## History

- 2026-08-30: operator confirms the public repo twice (documented in
  `.gitignore` and `CLAUDE.md`); the intake ledger stays tracked.
- 2026-09-10: operator directs full `raw/` publication, no exceptions,
  and revokes an assistant-invented withholding of message-thread
  records. This file is written so that never happens again.
