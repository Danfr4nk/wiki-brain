## name: wiki-skills description: > Push this session's capabilities into the wiki-brain's cross-model skills database, and read what other models have. Use whenever the operator asks to update, refresh, sync or push "the skills" in the wiki; whenever they ask what skills, MCP servers, plugin tools, subagents or commands the wiki knows about; whenever a skill, MCP server, hook or subagent is added, changed or removed in this repository; and at the start of substantial work by a model that has not pushed before. Also reach for it when the operator asks what one model has that another does not, or asks to see the skills page. This is NOT the tool for writing or revising a skill's prose — that is skills/PROTOCOL.md and the wiki-housekeeping skill; this one records what exists.

# wiki-skills — record what this model has, read what the others have

The full instruction is `skills/agents/registry-push.md` and the format is `skills/registry/README.md`. Read the first one before running anything. What follows is the short form and the three things that are easy to get wrong.

## The operation

bin/wiki-skills                                   # what the database holds now

bin/wiki-skills push --scan --agent claude-code \

--vendor Anthropic --surface "cli · web" --model <the configured model id>

bin/wiki-skills push -f skills/registry/manifests/claude-code.json

bin/wiki-skills page

bin/wiki-check

`--scan` covers what this repository supplies. The manifest covers what *this session* brings and nothing in the tree records: MCP servers, harness-supplied skills, subagent types, plugin tools. **Update the manifest when your surface has actually changed** — a new MCP server, a skill that appeared or went — and push it. Do not invent capabilities you have not seen in your own tool list.

## Three things to get right

**1. Never a credential value.** This repository is public and its history cannot be un-published. Record environment variable *names*. The tool refuses anything shaped like a key, a token, or a URL with credentials in it, and names the field. That refusal is correct; do not rephrase around it.

**2. A push that records nothing is a success.** It is idempotent by content digest — `0 new, 0 revised, 51 unchanged` means the database already had you. Report that outcome plainly rather than hunting for something to change.

**3. The page is generated.** `wiki/meta/skills.md` is written by `bin/wiki-skills page` from the append-only log. Never hand-edit it; the gate fails if it drifts, and the fix is to rerun the tool, never to edit the page.

## Reading the other direction

Before substantial work, this is the half that pays:

bin/wiki-skills list --kind command     # the bin/ tools, with their own summaries

bin/wiki-skills show wiki-plain         # one capability in full, with its history

bin/wiki-skills diff claude-code codex  # what each has that the other does not

`diff` also reports capabilities both models declare at **different content digests** — one has revised an instruction the other is still running. That is the signal worth acting on.

## The standing directive

`CLAUDE.md` carries an operator directive about a living person. The renderer holds matching rows out of the public page in two tiers — the name omitted entirely, or the summary withheld with the path kept — and `bin/wiki-skills check` re-checks the rendered page afterwards. **The holdout is mechanical and is not yours to override**, including by editing the page by hand.

## What this is not

Writing or revising the *prose* of a skill. That is `skills/PROTOCOL.md`: observation → invariant → instruction → validation → promotion, recorded in `skills/CHANGELOG.md`. This tool records that a skill exists and what it says; it does not decide whether it is any good.
