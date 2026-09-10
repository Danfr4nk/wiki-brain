#!/usr/bin/env python3
"""
contact-rename.py
Cross-references wiki/people/contacts/*.md against contacts.csv.
For each match:
  1. Renames the file to a slug derived from the contact's name.
  2. Updates the # heading inside the file.
  3. Rewrites every link to the old slug throughout wiki/ to the new slug.
  4. Prints a report of all matches and actions.

Run from: /Users/Suzanne/Documents/WIKI v2
"""

import csv
import os
import re
import shutil
import sys

WIKI_ROOT = "/Users/Suzanne/Documents/WIKI v2"
CONTACTS_DIR = os.path.join(WIKI_ROOT, "wiki/people/contacts")
WIKI_DIR = os.path.join(WIKI_ROOT, "wiki")
CSV_PATH = os.path.join(WIKI_ROOT, "contacts.csv")

def normalize_phone(raw: str) -> str:
    """Strip all non-digits from a phone string."""
    return re.sub(r"\D", "", raw)

def make_slug(name: str) -> str:
    """Convert a name to a wiki-style slug: lowercase, hyphens, ascii only."""
    # Remove parens/brackets and inner content used as label clarifiers
    name = re.sub(r"\(.*?\)", "", name)
    name = name.strip().lower()
    name = re.sub(r"[^a-z0-9 ]", "", name)
    name = re.sub(r"\s+", "-", name)
    name = name.strip("-")
    return name

def load_csv_phone_map(csv_path: str) -> dict:
    """
    Returns a dict of {normalized_phone: display_name} from the CSV.
    Checks Phone 1 - Value and Phone 2 - Value columns.
    Display name: "First Last" or fallback to Organization Name or Nickname.
    """
    phone_map = {}
    with open(csv_path, newline="", encoding="utf-8") as f:
        reader = csv.DictReader(f)
        for row in reader:
            first = (row.get("First Name") or "").strip()
            last = (row.get("Last Name") or "").strip()
            org = (row.get("Organization Name") or "").strip()
            nick = (row.get("Nickname") or "").strip()

            if first and last:
                display = f"{first} {last}"
            elif first:
                display = first
            elif last:
                display = last
            elif org:
                display = org
            elif nick:
                display = nick
            else:
                continue  # no usable name

            # collect all phone values from the row
            phones = []
            for key, val in row.items():
                if "Phone" in key and "Label" not in key and val:
                    # values can be " ::: " separated
                    for part in val.split(":::"):
                        part = part.strip()
                        if part:
                            phones.append(normalize_phone(part))

            for phone in phones:
                if len(phone) >= 7:  # skip short shortcodes
                    if phone not in phone_map:
                        phone_map[phone] = display

    return phone_map


def extract_phone_from_stub(md_path: str):
    """
    Read the stub file and extract the phone number from the # heading line.
    Expected format: # Contact +17243172393
    Returns the normalized phone string or None.
    """
    with open(md_path, encoding="utf-8") as f:
        for line in f:
            m = re.match(r"^#\s+Contact\s+(\+?[\d()\s\-]+)", line)
            if m:
                return normalize_phone(m.group(1))
    return None


def get_all_wiki_files():
    """Return list of absolute paths to every .md file in wiki/."""
    result = []
    for root, dirs, files in os.walk(WIKI_DIR):
        # skip .git
        dirs[:] = [d for d in dirs if d != ".git"]
        for fname in files:
            if fname.endswith(".md"):
                result.append(os.path.join(root, fname))
    return result


def rewrite_links_in_file(filepath: str, old_slug: str, new_slug: str) -> bool:
    """
    Replace all occurrences of wiki/people/contacts/{old_slug} with
    wiki/people/contacts/{new_slug} in the given file.
    Returns True if the file was modified.
    """
    with open(filepath, encoding="utf-8") as f:
        content = f.read()

    pattern = re.escape(f"wiki/people/contacts/{old_slug}")
    new_content = re.sub(pattern, f"wiki/people/contacts/{new_slug}", content)

    if new_content != content:
        with open(filepath, "w", encoding="utf-8") as f:
            f.write(new_content)
        return True
    return False


def update_stub_heading(md_path: str, new_display_name: str, phone: str):
    """
    Update the # heading and the Identity section of the stub to reflect the resolved name.
    Also updates date_modified in frontmatter.
    """
    with open(md_path, encoding="utf-8") as f:
        content = f.read()

    # Update heading
    content = re.sub(
        r"^# Contact \+?[\d()\s\-]+",
        f"# {new_display_name}",
        content,
        flags=re.MULTILINE
    )

    # Update date_modified
    content = re.sub(
        r"^date_modified: \d{4}-\d{2}-\d{2}",
        "date_modified: 2026-07-11",
        content,
        flags=re.MULTILINE
    )

    # Update first line of Identity section to acknowledge resolved name
    content = re.sub(
        r"(## Identity\n)Non-named or minimally identified contact",
        r"\1Contact identified via Google Contacts as " + new_display_name + r". Previously unresolved contact",
        content
    )

    with open(md_path, "w", encoding="utf-8") as f:
        f.write(content)


def ensure_unique_slug(slug: str, used_slugs: set) -> str:
    """If slug is already taken, append a numeric suffix."""
    if slug not in used_slugs:
        return slug
    i = 2
    while f"{slug}-{i}" in used_slugs:
        i += 1
    return f"{slug}-{i}"


def main():
    print("Loading contacts CSV...")
    phone_map = load_csv_phone_map(CSV_PATH)
    print(f"  Loaded {len(phone_map)} phone→name mappings.")

    stub_files = sorted(
        f for f in os.listdir(CONTACTS_DIR) if f.endswith(".md")
    )
    print(f"  Found {len(stub_files)} contact stub files.\n")

    all_wiki_files = get_all_wiki_files()

    matched = []
    unmatched = []
    used_slugs = set()

    for fname in stub_files:
        old_slug = fname[:-3]  # strip .md
        fpath = os.path.join(CONTACTS_DIR, fname)
        phone = extract_phone_from_stub(fpath)

        if not phone:
            unmatched.append((fname, "could not extract phone"))
            used_slugs.add(old_slug)
            continue

        # Try 10-digit, 11-digit, 7-digit suffix matches
        name = None
        tried = set()
        for n in [10, 11, 12, 7]:
            suffix = phone[-n:] if len(phone) >= n else phone
            if suffix in tried:
                continue
            tried.add(suffix)
            # search all map keys for matching suffix
            for map_phone, map_name in phone_map.items():
                if map_phone.endswith(suffix) or suffix.endswith(map_phone[-7:]):
                    name = map_name
                    break
            if name:
                break

        if not name:
            unmatched.append((fname, f"no match for phone {phone}"))
            used_slugs.add(old_slug)
            continue

        # Build new slug
        new_slug = make_slug(name)
        new_slug = ensure_unique_slug(new_slug, used_slugs)
        used_slugs.add(new_slug)

        new_fname = new_slug + ".md"
        new_fpath = os.path.join(CONTACTS_DIR, new_fname)

        matched.append((fname, new_fname, name, phone))

        # 1. Update the stub heading
        update_stub_heading(fpath, name, phone)

        # 2. Rename the file (only if slug actually changed)
        if old_slug != new_slug:
            shutil.move(fpath, new_fpath)

            # 3. Rewrite links across all wiki files (skip files that may have been renamed)
            link_updated_count = 0
            for wf in all_wiki_files:
                if not os.path.exists(wf):
                    continue
                if rewrite_links_in_file(wf, old_slug, new_slug):
                    link_updated_count += 1
            # also update the new file itself
            if os.path.exists(new_fpath):
                rewrite_links_in_file(new_fpath, old_slug, new_slug)

            print(f"  ✓ {fname} → {new_fname}  [{name}]  (links updated in {link_updated_count} files)")
        else:
            print(f"  ✓ {fname} — name resolved to same slug, heading updated only  [{name}]")

    print(f"\n=== SUMMARY ===")
    print(f"Matched and renamed: {len(matched)}")
    print(f"Unmatched (kept as-is): {len(unmatched)}")
    if unmatched:
        print("\nUnmatched stubs:")
        for fname, reason in unmatched:
            print(f"  {fname}: {reason}")


if __name__ == "__main__":
    main()
