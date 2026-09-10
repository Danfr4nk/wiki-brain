# Manifest Quality Audit

Generated: 2026-08-20

## Current Manifest State

- **File:** llm/manifest.json

- **Generated:** 2026-08-18

- **Page count:** 465 (actual: 476) — **STALE: 11 pages missing**

## Current Schema

The manifest currently exposes per page:

{

"page": "wiki/health/chemical-architecture.md",

"title": "Chemical Architecture",

"summary": "Dan runs a deliberately engineered neurochemical system...",

"url": "https://caakehorn.github.io/wiki-brain/llm/pages/health/chemical-architecture.txt",

"bytes": 11880

}

## What Can Be Mechanically Extracted

Without semantic judgment, the following metadata can be parsed from frontmatter:

| **Field** | **Source** | **Currently Exposed?** |
| --- | --- | --- |
| page | file path | Yes |
| title | frontmatter | Yes |
| summary | first paragraph extraction | Yes (partial) |
| url | path construction | Yes |
| bytes | file size | Yes |
| domain | path segment | No |
| page_type | frontmatter | No |
| status | frontmatter | No |
| knowledge | frontmatter | No |
| date_created | frontmatter | No |
| date_modified | frontmatter | No |
| sources_count | count of raw/ paths | No |
| synthesizes_count | count of wiki/ paths | No |
| connections_count | count of connections | No |
| importance | frontmatter | No |
| aliases | frontmatter | No |
| tags | frontmatter | No |
| entities | infobox (people pages) | No |
| date_range | frontmatter | No |

## Recommended Schema Addition

The plan's richer schema (entities, topics, date_range, retrieval_hints, etc.) requires semantic judgment for some fields. But these can be mechanically added now:

- domain, page_type, status, knowledge, date_created, date_modified

- sources_count, synthesizes_count, connections_count

- importance, aliases, tags (from frontmatter)

- infobox fields for people pages (name, dob, sex, location, relationship_to_dan)

## Action Items

1. **Fix staleness:** Regenerate manifest after every content pass

1. **Add mechanical metadata:** Add extractable fields listed above

1. **Schema review:** Have Claude review and approve the final richer schema

1. **CI gate:** Add check that manifest page count matches actual wiki page count

## What Requires Claude Judgment

Per the plan, the following fields should NOT be invented mechanically:

- topics (requires understanding page content)

- entities (requires NER and resolution)

- retrieval_hints (requires understanding what the page is "for")

- importance scoring beyond what's in frontmatter

- knowledge classification beyond what's in frontmatter
