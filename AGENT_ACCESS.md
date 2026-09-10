# Agent / LLM access to wiki-brain

How to give models and agents the **current compiled wiki** from GitHub.

## ⚠️ STATUS [2026-08-08]: Pages is serving, but check which build

The 2026-08-02 banner here said every `caakehorn.github.io/wiki-brain/...` URL returned 404 because the repo had gone private. That is **no longer the situation, and the replacement failure was worse for being invisible**: the site answers `200`, so nothing looked broken, but Pages had been switched to **Deploy from a branch**. The legacy Jekyll builder then served the repository markdown verbatim, which meant:

- **Humans got a site with no navigation.** Jekyll has no idea what `[[wiki/self/index]]` means, so all ~3,150 wikilinks — including every row of the master index's Index column — rendered as literal grey text. You could reach the front page and go nowhere from it.

- **Agents got nothing at all.** `llms.txt`, `agent/manifest.json`, `agent/critical.md`, `agent/corpus.md` and `agent/domains/*` are written by `bin/build-site` into `site/`, which is gitignored and only ever reaches Pages as a workflow artifact. Under branch builds they were never published — every entrypoint below 404'd.

- `wiki/**/*.md` 404'd too: Jekyll rewrites `.md` to `.html`, so the documented one-page-fetch URLs did not exist in that build either.

`deploy-site.yml` had been failing on every push since 2026-08-02 for the matching reason — `configure-pages` returns *"Get Pages site failed"* when Pages is not set to build from Actions.

**Fixed in this branch**, and the workflow now repairs the setting itself: it PUTs `build_type=workflow` to the Pages API before configuring, and a post-deploy step fetches `llms.txt`, `agent/manifest.json` and friends, failing the run when Pages is serving anything other than the built site. That is the guard that was missing — the outage was silent for six days.

If the smoke test ever fails again, the manual fix is **Settings → Pages → Source → GitHub Actions**.

**Mirror (independent of all of the above):**

| **What** | **URL** |
| --- | --- |
| Everything, one file (~2.6 MB) | `https://caakehorn.github.io/leviathan/data/wiki-data.json` |
| Human-readable browser | `https://caakehorn.github.io/leviathan/wiki.html` |

That mirror lives in the public `caakehorn/leviathan` repo, is rebuilt hourly by its `sync-wiki.yml` workflow, and carries `wikiPages.pages[]` (metadata, summaries, typed connections) plus `wikiText[<id>]` (full page prose) plus `wikiLog.ops[]`. `source_commit` names the wiki-brain commit it was built from, so you can tell how stale it is.

`llm/index.txt` and the rest of `llm/` are committed to the repo rather than generated at deploy time, so they stayed reachable throughout and are the safest entrypoint if you are unsure which build is live.

## Mandatory agent activity logging

`AGENT_ACTIVITY_LOG.md` is the canonical, append-only record of substantive work performed by LLMs and agents.

### PR rule — mandatory

**Every new PR created by an agent for ****`wiki-brain`**** must contain a model-authored activity entry.** The agent must append that entry to `AGENT_ACTIVITY_LOG.md` on the PR branch and also make the same entry visible in the PR itself (PR body or a top-level PR comment).

The entry must say what the agent **actually did**: task, concrete work performed, important reasoning/decisions, files or areas touched, validation performed or skipped, result, and unresolved follow-up. Never fabricate provenance.

If work materially changes after the first entry, append a follow-up entry rather than overwriting the original. **Do not consider the agent workflow complete without the activity entry.**

See `AGENT_ACTIVITY_LOG.md` for the full schema and template.

## What you already have

| **Layer** | **URL** | **Notes** |
| --- | --- | --- |
| GitHub source of truth | [https://github.com/caakehorn/wiki-brain](https://github.com/caakehorn/wiki-brain) | `main` is authoritative after merge |
| GitHub raw file | `https://raw.githubusercontent.com/caakehorn/wiki-brain/main/wiki/…` | Tracks `main`; needs an auth token whenever the repo is private |
| GitHub Pages (agent feed) | [https://caakehorn.github.io/wiki-brain/](https://caakehorn.github.io/wiki-brain/) | Live. Serves the `bin/build-site` artifact **only** when Pages source is GitHub Actions — see banner |
| Committed LLM feed | [https://caakehorn.github.io/wiki-brain/llm/index.txt](https://caakehorn.github.io/wiki-brain/llm/index.txt) | Survives either Pages build, because `llm/` is committed rather than generated at deploy |

The local app (`app.py` on `localhost:8477`) is for **you** (capture, edit, ingest). Agents should use the online feed, not your laptop.

## Agent entrypoints (after deploy)

Once [`.github/workflows/deploy-site.yml`](http://.github/workflows/deploy-site.yml) has run on `main`:

| **Resource** | **URL** |
| --- | --- |
| **Discovery** | [https://caakehorn.github.io/wiki-brain/llms.txt](https://caakehorn.github.io/wiki-brain/llms.txt) |
| **Machine index** | [https://caakehorn.github.io/wiki-brain/agent/manifest.json](https://caakehorn.github.io/wiki-brain/agent/manifest.json) |
| **Critical spine** | [https://caakehorn.github.io/wiki-brain/agent/critical.md](https://caakehorn.github.io/wiki-brain/agent/critical.md) |
| **Full corpus** | [https://caakehorn.github.io/wiki-brain/agent/corpus.md](https://caakehorn.github.io/wiki-brain/agent/corpus.md) |
| **Domain corpora** | [https://caakehorn.github.io/wiki-brain/agent/domains/&lt;domain&gt;.md](https://caakehorn.github.io/wiki-brain/agent/domains/&lt;domain&gt;.md) |
| **One page** | [https://caakehorn.github.io/wiki-brain/wiki/self/overview.md](https://caakehorn.github.io/wiki-brain/wiki/self/overview.md) |

Domains: `self` · `timeline` · `people` · `mind` · `work` · `interests` · `health` · `places` · `legal`

### Recommended agent strategy

1. Fetch `llms.txt` or `agent/manifest.json`.

1. Check `git_sha` / `generated_at` if you care about freshness.

1. Load by context budget:

  - **Small:** `agent/critical.md`

  - **Medium:** one or more `agent/domains/*.md` (people is large; mind/self first for identity)

  - **Large:** `agent/corpus.md` (~300k+ tokens — often multi-pass)

1. Deep-dive individual `wiki/…/*.md` URLs from the manifest.

1. For any repository change that will become a PR, follow the **Mandatory agent activity logging** rule above before declaring the work complete.

### Prompt snippet you can paste into any agent

You have online access to my personal wiki (compiled second brain).

Discovery: https://caakehorn.github.io/wiki-brain/llms.txt

Manifest:  https://caakehorn.github.io/wiki-brain/agent/manifest.json

Spine:     https://caakehorn.github.io/wiki-brain/agent/critical.md

Rules:

- Prefer the compiled wiki over inventing facts.

- Start with critical.md or domain corpora; fetch individual pages as needed.

- Honor CONTRADICTION / REVISED blockquotes on pages.

- Cite page paths (e.g. wiki/people/annie-ulmer.md) in answers.

- For every new PR: append a truthful model-authored entry to AGENT_ACTIVITY_LOG.md and include the same entry in the PR body or a top-level PR comment. If the work changes materially, append a follow-up entry; do not overwrite provenance.

## Keep the feed current

1. Work on a branch → merge to **`main`** (PRs as you already do).

1. Push to `main` triggers **Deploy agent site**.

1. Pages updates in ~1–2 minutes. Manifest `git_sha` should match `main`.

Local preview of the same site:

bin/build-site

# open site/llms.txt  or  python3 -m http.server -d site 8787

## Privacy warning (important)

This repository is currently **public**, including a large `raw/` archive (messages, dossiers, etc.). The agent **Pages** feed deliberately publishes only the compiled `wiki/` tree — not `raw/` or `inbox/`.

That does **not** hide `raw/` from the internet: anyone can still clone the GitHub repo.

If you want agents online but the public web **off** your life archive:

1. Make the GitHub repo **private**.

1. Keep Pages only if your plan supports private Pages + auth, **or**

1. Put a token-gated proxy in front (Cloudflare Worker, Fly.io, etc.) that clones with a deploy key and serves `site/` only.

Until then, treat everything in this repo as world-readable.

## Optional next upgrades

| **Upgrade** | **When you need it** |
| --- | --- |
| **Private + token API** | Secrets must not be public; agents use `Authorization: Bearer …` |
| **MCP server** | Claude/Cursor tools: `search_wiki`, `get_page`, `list_domain` over the same feed |
| **Search endpoint** | Full-text search without downloading corpora (small Worker over `manifest` + page bodies) |
| **Delete ****`_config.yml`** | Deploy is `deploy-site.yml` (stdlib-only `bin/build-site`). The file is inert under Actions builds and actively harmful under branch builds — kept for now only as a degraded fallback |

The agent site uses `.nojekyll` and replaces the human Jekyll theme with raw Markdown + JSON optimized for models.
