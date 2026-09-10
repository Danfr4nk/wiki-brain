#!/usr/bin/env python3
"""Backfill people-page infobox classifier schema (conservative).

Sets a field ONLY when the page body / frontmatter gives a strong signal.
Never fabricates. relationship_to_dan defaults to 'unknown' when no cue.
Skips wiki/people/contacts/ (quarantine) and index.md.
"""
import re, os, glob, sys

WIKI = "wiki/people"
ROOT = os.getcwd()

def fm_parse(text):
    m = re.match(r"^---\n(.*?)\n---\n", text, re.S)
    if not m:
        return None, text
    fm = {}
    body = text[m.end():]
    for line in m.group(1).splitlines():
        kv = re.match(r"^([a-z_]+):\s*(.*)$", line)
        if kv:
            fm[kv.group(1)] = kv.group(2).strip()
    return fm, body

def get_block(text, key):
    # get a yaml block value that may be a quoted string or inline list
    m = re.search(r"^%s:\s*(.*)$" % key, text, re.M)
    return m.group(1).strip() if m else None

# relationship cues (strong -> value). Only explicit, unambiguous cues assign
# a specific value; everything else falls through to 'unknown' (never guess).
REL_PATTERNS = [
    (r"\b(wife|husband|spouse)\b", "family"),
    (r"\b(girlfriend|boyfriend)\b", "ex-partner"),
    (r"\bex[- ]?(wife|husband|girlfriend|boyfriend|partner)\b", "ex-partner"),
    (r"\b(father|mother|son|daughter|brother|sister|cousin|aunt|uncle|grandmother|grandfather)\b", "family"),
    (r"\bdealer\b|\bdrug source\b", "dealer"),
    (r"\bcoworker\b|\bco[- ]worker\b", "coworker"),
    (r"\bfriend\b", "friend"),
    (r"\bacquaintance\b", "acquaintance"),
]

def infer_relationship(body, fm):
    # Prefer explicit relationship_to_dan if present in body prose markers
    low = body.lower()
    for pat, val in REL_PATTERNS:
        if re.search(pat, low):
            return val
    # title/name based family hints
    return "unknown"

def infer_sex(body):
    # pronoun dominance over a sample; only set when clearly one-sided
    she = len(re.findall(r"\bshe\b|\bher\b|\bhers\b", body, re.I))
    he = len(re.findall(r"\bhe\b|\bhim\b|\bhis\b", body, re.I))
    # require a strong skew and a minimum count
    if she > 8 and she > he * 2:
        return "female"
    if he > 8 and he > she * 2:
        return "male"
    return None

def infer_location(body):
    low = body.lower()
    nyc = len(re.findall(r"\b(nyc|new york|brooklyn|east village|manhattan|155 virginia)\b", low))
    union = len(re.findall(r"\b(uniontown|brownsville|perry|337 saratoga)\b", low))
    if nyc > union and nyc >= 1:
        return "nyc"
    if union > nyc and union >= 1:
        return "uniontown"
    return None

def extract_handles(body):
    hs = set()
    for m in re.findall(r"\+1\*{4,}\d+", body):
        hs.add(m)
    return sorted(hs)

def infer_first_contact(fm):
    return fm.get("date_range_start")

def main():
    files = glob.glob(os.path.join(WIKI, "**", "*.md"), recursive=True)
    changed = 0
    for p in files:
        rel = os.path.relpath(p, ROOT)
        r = rel[:-3]
        if "/contacts/" in r or r.endswith("/index") or os.path.basename(p) == "index.md":
            continue
        text = open(p, encoding="utf-8", errors="replace").read()
        fm, body = fm_parse(text)
        if fm is None:
            continue
        if fm.get("domain") != "people":
            continue
        body_prose = re.sub(r"^---\n.*?\n---\n", "", text, flags=re.S)
        body_prose = re.sub(r"^#.*$", "", body_prose, flags=re.M)

        # Determine infobox existing
        ib_match = re.search(r"(infobox:\s*\n(?:[ \t]+[^-\n][^\n]*\n)*)", text)
        has_ib = ib_match is not None
        ib_lines = []
        ib_keys = set()
        if has_ib:
            block = ib_match.group(1)
            for ln in block.splitlines()[1:]:
                km = re.match(r"\s*([a-z_]+):", ln)
                if km:
                    ib_keys.add(km.group(1))
            # keep existing infobox content
            ib_lines = block.splitlines()[1:]

        # Build required + optional fields
        name = fm.get("title")
        if not name:
            name = os.path.basename(p)[:-3].replace("-", " ").title()
        else:
            name = name.strip().strip('"').strip("'")
        rel_val = "unknown"  # relationship_to_dan is NOT auto-derived (prose
                             # context is unreliable — "girlfriend" often refers
                             # to a third party). Set to 'unknown'; correct
                             # high-value pages by hand.
        sex = infer_sex(body_prose)
        loc = infer_location(body_prose)
        fc = infer_first_contact(fm)
        handles = extract_handles(body_prose)
        # known_for: first non-empty prose sentence (strip markdown)
        ko = ""
        for ln in body_prose.splitlines():
            ln = ln.strip()
            if ln and not ln.startswith("#") and not ln.startswith(">") and not ln.startswith("|") and not ln.startswith("-"):
                ko = re.sub(r"[*_`#]", "", ln)[:120]
                break

        new_fields = []
        if "name" not in ib_keys:
            new_fields.append(f'  name: "{name}"')
        if "relationship_to_dan" not in ib_keys:
            new_fields.append(f"  relationship_to_dan: {rel_val}")
        if sex and "sex" not in ib_keys:
            new_fields.append(f"  sex: {sex}")
        if loc and "location" not in ib_keys:
            new_fields.append(f"  location: {loc}")
        if fc and "first_contact" not in ib_keys:
            new_fields.append(f"  first_contact: {fc}")
        if handles and "handles" not in ib_keys:
            hs = ", ".join(f'"{h}"' for h in handles[:4])
            new_fields.append(f"  handles: [{hs}]")
        if ko and "known_for" not in ib_keys:
            new_fields.append(f'  known_for: "{ko}"')

        if not new_fields:
            continue

        if has_ib:
            # append new fields inside the existing infobox block (before its end)
            insert_at = ib_match.end()
            added = "\n" + "\n".join(new_fields)
            text = text[:insert_at].rstrip("\n") + added + "\n" + text[insert_at:]
        else:
            # insert infobox INSIDE frontmatter, before the closing ---
            fm_end = re.search(r"^---\n.*?\n---\n", text, re.S)
            if not fm_end:
                continue
            close = re.search(r"\n---\n", text[fm_end.start():], re.S)
            # position of the closing --- line
            close_pos = fm_end.start() + close.start() + 1  # after the leading \n
            ib = "infobox:\n" + "\n".join(new_fields) + "\n"
            text = text[:close_pos] + ib + text[close_pos:]

        open(p, "w", encoding="utf-8").write(text)
        changed += 1
        print(f"updated {rel}")
    print(f"\nBackfilled {changed} people pages.")

if __name__ == "__main__":
    main()
