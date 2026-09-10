#!/usr/bin/env python3
"""Personal Wiki — single-file local app (v3 GUI, Wikipedia-style).

Run:  python3 app.py   (or double-click Wiki.command / the Dock app)
Serves http://127.0.0.1:8477 — Python stdlib only, localhost only.

The interface imitates Wikipedia's classic Vector skin: left panel with
logo + portals, Page/Discussion and Read/Edit/View-history tabs, serif
headings, floating infoboxes built from page frontmatter, a numbered
table of contents, red links for missing pages, categories bar, and a
git-backed View history / Recent changes. Pages are edited (and created)
directly in the interface; pictures can be uploaded and inserted into
articles (stored under assets/uploads/). Capture / Ingest / Export live
on as Special: pages. All data stays in the plain Markdown files of this
repository.
"""
import datetime
import json
import os
import mimetypes
import re
import shutil
import subprocess
import sys
import tempfile
import threading
import urllib.parse
import urllib.request
import webbrowser
from http.server import BaseHTTPRequestHandler, ThreadingHTTPServer
from pathlib import Path

ROOT = Path(__file__).resolve().parent
INBOX = ROOT / "inbox"
WIKI = ROOT / "wiki"
UPLOADS = ROOT / "assets" / "uploads"
PORT = 8477
TEXT_EXT = {".md", ".txt", ".csv", ".json", ".html", ".rtf", ".yaml", ".yml"}
IMG_EXT = {".png", ".jpg", ".jpeg", ".gif", ".webp", ".svg", ".avif"}
META_EDITABLE = {"queue.md", "BACKLOG.md", "LLM_HANDOFF.md"}
_vis_cache = {"checked": False, "public": None, "repo": None}


# ---------------------------------------------------------------- helpers

def safe(path_str):
    p = (ROOT / path_str).resolve()
    if not str(p).startswith(str(ROOT) + "/") and p != ROOT:
        raise PermissionError(path_str)
    return p


def slugify(text, maxlen=60):
    slug = re.sub(r"[^a-z0-9]+", "-", text.lower()).strip("-")
    return slug[:maxlen].rstrip("-") or "note"


def stamp():
    return datetime.datetime.now().strftime("%Y-%m-%d_%H%M%S")


def log_line(op, domain, desc):
    today = datetime.date.today().isoformat()
    with open(ROOT / "log.md", "a", encoding="utf-8") as f:
        f.write(f"## [{today}] {op} | {domain} | {desc}\n")


def save_note(body, title=None, tags=None, targets=None):
    INBOX.mkdir(exist_ok=True)
    title = (title or body.strip().splitlines()[0][:60]).strip()
    path = INBOX / f"{stamp()}_{slugify(title, 40)}.md"
    words = len(body.split())
    kind = "correction" if targets else ("story" if words > 150 else "fact")
    front = [
        "---",
        f"captured: {datetime.datetime.now().strftime('%Y-%m-%d %H:%M')}",
        f"title: {title}",
        f"type: {kind}",
        f"tags: [{', '.join(tags or [])}]",
    ]
    if targets:
        front.append(f"targets: [{', '.join(targets)}]")
    front += ["source: wiki-app", "---", ""]
    path.write_text("\n".join(front) + body.strip() + "\n", encoding="utf-8")
    return {"saved": str(path.relative_to(ROOT)), "words": words, "kind": kind}


def save_page(rel_path, content, summary=None, create=False):
    p = safe(rel_path)
    is_wiki = str(p).startswith(str(WIKI) + "/") and p.suffix == ".md"
    is_meta = p.parent == ROOT and p.name in META_EDITABLE
    if not (is_wiki or is_meta):
        raise PermissionError("can only edit wiki/*.md pages or the editable meta files")
    if create:
        if not is_wiki:
            raise PermissionError("can only create pages under wiki/")
        if p.exists():
            raise PermissionError("page already exists")
        p.parent.mkdir(parents=True, exist_ok=True)
    elif not p.exists():
        raise PermissionError("page does not exist (use create)")
    today = datetime.date.today().isoformat()
    content = re.sub(r"(?m)^date_modified: .*$", f"date_modified: {today}",
                     content, count=1)
    p.write_text(content, encoding="utf-8")
    parts = Path(rel_path).parts
    domain = parts[1] if len(parts) >= 3 else "meta"
    op = "create" if create else "edit"
    desc = f"human {op} via app: {rel_path}"
    if summary:
        desc += f" — {summary.strip()[:200]}"
    log_line(op, domain, desc)
    return {"saved": rel_path, "created": create}


def upload_image(name, data):
    ext = Path(name).suffix.lower()
    if ext not in IMG_EXT:
        raise PermissionError(f"not an image type: {ext or '(none)'}")
    UPLOADS.mkdir(parents=True, exist_ok=True)
    fname = f"{stamp()}_{slugify(Path(name).stem, 40)}{ext}"
    dest = UPLOADS / fname
    dest.write_bytes(data)
    return {"path": str(dest.relative_to(ROOT)), "bytes": len(data)}


def rename_page(rel_path, new_name):
    """Rename a wiki page and rewrite every inbound reference."""
    p = safe(rel_path)
    if not (str(p).startswith(str(WIKI) + "/") and p.suffix == ".md" and p.exists()):
        raise PermissionError("can only rename existing wiki/*.md pages")
    if p.name == "index.md":
        raise PermissionError("index pages cannot be renamed")
    new_slug = slugify(new_name)
    if not new_slug:
        raise PermissionError("empty new name")
    new_p = p.parent / (new_slug + ".md")
    if new_p.exists():
        raise PermissionError(f"target already exists: {new_p.relative_to(ROOT)}")

    old_ref = str(p.relative_to(ROOT))[:-3]      # wiki/people/foo
    new_ref = str(new_p.relative_to(ROOT))[:-3]
    p.rename(new_p)

    pat = re.compile(re.escape(old_ref) + r"(?![-\w])")
    updated = []
    for f in list(WIKI.rglob("*.md")) + [ROOT / "index.md"]:
        if not f.exists():
            continue
        t = f.read_text(encoding="utf-8", errors="replace")
        t2 = pat.sub(new_ref, t)
        if t2 != t:
            f.write_text(t2, encoding="utf-8")
            updated.append(str(f.relative_to(ROOT)))
    # touch date_modified on the page itself
    t = new_p.read_text(encoding="utf-8")
    t = re.sub(r"(?m)^date_modified: .*$",
               f"date_modified: {datetime.date.today().isoformat()}", t, count=1)
    new_p.write_text(t, encoding="utf-8")
    domain = new_ref.split("/")[1]
    log_line("rename", domain, f"{old_ref}.md -> {new_ref}.md ({len(updated)} pages relinked) via app")
    return {"newPath": new_ref + ".md", "linksUpdated": len(updated), "files": updated}


def tree():
    def entry(p):
        return {"path": str(p.relative_to(ROOT)), "name": p.name,
                "size": p.stat().st_size}
    wiki_files = [entry(p) for p in sorted(WIKI.rglob("*.md"))]
    meta = [entry(ROOT / n) for n in
            ("index.md", "README.md", "STRATEGY.md", "CLAUDE.md", "EXTRACTION_SPEC.md",
             "STYLE_GUIDE.md", "CONNECTIONS_SPEC.md", "SYNTHESIS_SPEC.md",
             "INGEST_PROTOCOL.md", "BACKLOG.md", "LLM_HANDOFF.md", "queue.md",
             "log.md") if (ROOT / n).exists()]
    inbox = []
    if INBOX.exists():
        for p in sorted(INBOX.iterdir()):
            if p.name.startswith("."):
                continue
            size = (sum(f.stat().st_size for f in p.rglob("*") if f.is_file())
                    if p.is_dir() else p.stat().st_size)
            inbox.append({"path": str(p.relative_to(ROOT)), "name": p.name,
                          "size": size, "dir": p.is_dir()})
    return {"wiki": wiki_files, "meta": meta, "inbox": inbox}


def search(q):
    q = q.lower()
    hits = []
    files = sorted(WIKI.rglob("*.md")) + [ROOT / n for n in ("index.md", "log.md", "queue.md")]
    for f in files:
        if not f.exists():
            continue
        try:
            text = f.read_text(encoding="utf-8", errors="replace")
        except Exception:
            continue
        lines = [(i + 1, l.strip()) for i, l in enumerate(text.splitlines()) if q in l.lower()]
        if lines:
            hits.append({"path": str(f.relative_to(ROOT)),
                         "matches": [{"line": n, "text": t[:200]} for n, t in lines[:5]],
                         "count": len(lines)})
        if len(hits) >= 50:
            break
    return hits


def run(cmd, timeout=120):
    """Run a repository command without letting an unavailable remote break the UI."""
    try:
        r = subprocess.run(cmd, capture_output=True, text=True, cwd=ROOT,
                           timeout=timeout)
    except subprocess.TimeoutExpired:
        return 124, f"command timed out after {timeout}s: {' '.join(cmd)}"
    except OSError as e:
        return 127, str(e)
    return r.returncode, (r.stdout + r.stderr).strip()


def git_history(rel_path):
    rel_path = str(safe(rel_path).relative_to(ROOT))
    code, out = run(["git", "log", "--follow", "--date=format:%H:%M, %d %B %Y",
                     "--pretty=format:%h%x09%ad%x09%an%x09%s", "--", rel_path])
    entries = []
    if code == 0 and out:
        for line in out.splitlines():
            parts = line.split("\t", 3)
            if len(parts) == 4:
                entries.append({"hash": parts[0], "date": parts[1],
                                "author": parts[2], "subject": parts[3]})
    return {"path": rel_path, "entries": entries}


def git_recent(n=50):
    code, out = run(["git", "log", f"-{n}", "--date=format:%H:%M, %d %B %Y",
                     "--pretty=format:%h%x09%ad%x09%an%x09%s"])
    entries = []
    if code == 0 and out:
        for line in out.splitlines():
            parts = line.split("\t", 3)
            if len(parts) == 4:
                entries.append({"hash": parts[0], "date": parts[1],
                                "author": parts[2], "subject": parts[3]})
    return {"entries": entries}


def export(opts):
    cmd = [sys.executable, str(ROOT / "bin" / "export-corpus")]
    if opts.get("raw"): cmd.append("--raw")
    if opts.get("inbox"): cmd.append("--inbox")
    if opts.get("domain"): cmd += ["--domain", opts["domain"]]
    _, out = run(cmd)
    m = re.search(r"-> (\S+)", out)
    return {"message": out, "file": m.group(1) if m else None}


def ingest_pack(item):
    code, out = run([sys.executable, str(ROOT / "bin" / "ingest-pack"), item])
    prompt_file = ROOT / "exports" / "ingest-prompt.md"
    prompt = prompt_file.read_text(encoding="utf-8") if prompt_file.exists() and code == 0 else ""
    return {"message": out, "prompt": prompt, "ok": code == 0}


def ingest_apply(response_text, commit):
    with tempfile.NamedTemporaryFile("w", suffix=".md", delete=False,
                                     dir=str(ROOT / "exports")) as f:
        f.write(response_text)
        tmp = f.name
    try:
        cmd = [sys.executable, str(ROOT / "bin" / "ingest-apply"), tmp]
        if commit:
            cmd.append("--commit")
        code, out = run(cmd)
        return {"message": out, "ok": code == 0}
    finally:
        Path(tmp).unlink(missing_ok=True)


# ------------------------------------------------------------- intake ledger
#
# Special:Intake is a form over `bin/intake`, and it imports that file rather
# than reimplementing any of it. The tool has no .py extension, so it is loaded
# through SourceFileLoader — worth the four lines, because the alternative is a
# second implementation of the same arithmetic behind a nicer form, and two
# records of the same night that do not agree.
# THE ONE CROSS-ORIGIN HOLE IN THIS SERVER, and it is worth being explicit
# about why it exists and how narrow it is.
#
# ボスの部屋 (`boss.html` in caakehorn/leviathan) is the themed front end for
# this ledger. It is served from the static site, and the ledger it renders is
# here, on localhost. That is the right way round: the leviathan site holds no
# copy of the ledger and never receives one, and a browser that cannot reach this
# daemon shows an empty room rather than anything real. But it does mean one page
# on another origin has to be able to call these endpoints.
#
# (Note what that claim is and is not. It is about *this* boundary: the record
# does not travel to the static site. Whether the record is committed to this
# repository's git history is a separate decision, made in `.gitignore` and
# documented in `intake/README.md` — see the note at the end of this comment.)
#
# So the hole is cut to exactly that shape:
#   * an ALLOWLIST, never a wildcard, and never `*` with credentials;
#   * `/api/intake*` only — nothing else on this server answers a foreign origin,
#     so the wiki, the capture box, git sync and the file reader stay same-origin;
#   * credentials off, so nothing rides along that the page did not send itself.
#
# The residual risk, stated plainly: script execution on an allowlisted origin
# can read and write this ledger while the daemon is running. leviathan serves
# no user content, but it does load two third-party scripts (Google Fonts and
# GoatCounter), and either of those going bad is the realistic path in. If that
# is not a trade you want, set WIKI_INTAKE_ORIGINS to an empty string and the
# hole closes completely — the CLI and Special:Intake are unaffected, and
# boss.html simply reports that the house is closed.
#
# ONE PREMISE THIS COMMENT WILL NOT ASSERT. `intake/README.md` and `CLAUDE.md`
# both state that this repository is private and that the ledger's data is
# therefore tracked in git. That was checked from here on 2026-08-30 against the
# GitHub API, anonymously, and it did not hold: `private: false`,
# `visibility: public`. Nothing has been published — no `events.jsonl`,
# `units.json` or `raw/health/intake/` appears anywhere in main's history — but
# the allowlist above is sized for a public repository, and it stays that way
# until the visibility actually changes rather than until the docs say it has.
DEFAULT_INTAKE_ORIGINS = "https://caakehorn.github.io"


def intake_origins():
    raw = os.environ.get("WIKI_INTAKE_ORIGINS", DEFAULT_INTAKE_ORIGINS)
    return {o.strip() for o in raw.split(",") if o.strip()}


def intake_cors_origin(origin):
    """Echo back an allowlisted origin, or None. Localhost is always allowed."""
    if not origin:
        return None
    if origin in intake_origins():
        return origin
    host = urllib.parse.urlparse(origin).hostname
    if host in ("127.0.0.1", "localhost", "::1"):
        return origin
    return None


_intake_cache = {}


def intake_mod():
    if "m" not in _intake_cache:
        import importlib.util
        from importlib.machinery import SourceFileLoader
        loader = SourceFileLoader("intake_ledger", str(ROOT / "bin" / "intake"))
        spec = importlib.util.spec_from_loader("intake_ledger", loader)
        mod = importlib.util.module_from_spec(spec)
        loader.exec_module(mod)
        _intake_cache["m"] = mod
    return _intake_cache["m"]


def intake_view(m, ops, u):
    """One unit, plus every string the page shows — formatted here, once.

    The browser gets numbers *and* the rendered forms of them. Formatting a
    quantity is not hard, but doing it twice is how a page ends up saying 0.2 g
    where the report says 200 mg.
    """
    a, bu = u["analysis"], u["quantity_unit"]
    view = dict(u)
    view["display"] = {
        "initial": m.fmt_qty(u["initial_quantity"], bu),
        "logged": m.fmt_qty(a["quantified_total"], bu),
        "remaining": m.fmt_qty(a["remaining"], bu),
        "remaining_is_estimate": a["remaining_is_estimate"],
        "mean": m.fmt_qty(a["dose"]["mean"], bu) if a["dose"]["n"] else None,
        "coverage": m.coverage_line(a),
        "received": m.fmt_when(u["received_at"]),
        "closed": m.fmt_when(u["closed_at"]) if u["closed_at"] else None,
        "duration": m.fmt_dur(a["duration_seconds"]),
        "events": m.render_events(u),
        "overdrawn": a["overdrawn"],
    }
    view["reconciliation"] = ops.reconciliation(u)
    return view


def intake_state():
    m = intake_mod()
    L = m.Ledger(ROOT)
    ops = m.Ops(L)
    units = L.project()
    errors, warnings = m.check(L)
    today = datetime.date.today().isoformat()
    return {
        "substances": L.substances(),
        "categories": m.CATEGORIES,
        "units": [intake_view(m, ops, u) for u in units],
        "quantity_units": {fam: sorted(t, key=lambda u: t[u]) for fam, t in m.FAMILIES.items()},
        "confidences": list(m.CONFIDENCES),
        "dispositions": list(m.DISPOSITIONS),
        "resolutions": list(m.RESOLUTIONS),
        "adjustment_kinds": list(m.ADJUSTMENT_KINDS),
        "warnings": warnings,
        "errors": errors,
        "today": sum(1 for u in units for e in u["intakes"]
                     if not e["voided"] and e["occurred_at"][:10] == today),
    }


def intake_stats(substance=None, since=None, until=None):
    """The cross-unit read, computed by the ledger and rendered by the ledger.

    Returned as both the JSON and the tool's own rendered text, so a client can
    draw a chart from the numbers without ever having to restate the prose —
    and so the prose it shows is the same prose `bin/intake stats` prints.
    """
    m = intake_mod()
    st = m.cross_stats(m.Ledger(ROOT).project(), substance, since, until)
    return {"stats": st, "text": m.render_stats(st)}


def intake_report(ref):
    m = intake_mod()
    L = m.Ledger(ROOT)
    u = L.find_unit(ref)
    return {"unit_id": u["id"], "ordinal": u["ordinal"], "report": m.render_report(u),
            "events": m.render_events(u)}


def intake_action(action, d):
    """Every mutation the page can make, each one a thin call into bin/intake."""
    m = intake_mod()
    L = m.Ledger(ROOT)
    ops = m.Ops(L)
    UI = "app"

    def qty(field="quantity", unit_field="quantity_unit"):
        raw = (d.get(field) or "").strip() if isinstance(d.get(field), str) else d.get(field)
        if raw in (None, ""):
            return None, None
        unit = (d.get(unit_field) or "").strip() or None
        if unit:
            return m.parse_quantity(f"{raw}{unit}")
        return m.parse_quantity(str(raw))

    if action == "unit":
        q, un = qty()
        if q is None:
            raise m.LedgerError("a unit has to start with a quantity")
        u = ops.new_unit(d.get("substance"), q, un, d.get("at") or None,
                         d.get("source") or None, d.get("note") or None, interface=UI)
        return {"unit": u["id"], "ordinal": u["ordinal"]}
    if action == "log":
        if (d.get("preset") or "").strip():
            ev, u = ops.log_preset(d.get("unit"), d["preset"].strip(),
                                   d.get("at") or None,
                                   (d.get("note") or "").strip() or None, interface=UI)
            return {"event": ev["id"], "ordinal": u["ordinal"], "preset": d["preset"]}
        q, un = qty()
        mtype = d.get("measurement_type") or ("unquantified" if q is None else "measured")
        ev, u = ops.log_intake(d.get("unit"), q, un, mtype, d.get("confidence") or None,
                               (d.get("descriptor") or "").strip() or None,
                               d.get("at") or None, (d.get("note") or "").strip() or None,
                               interface=UI)
        return {"event": ev["id"], "ordinal": u["ordinal"]}
    if action == "adjust":
        q, un = qty()
        ev, u = ops.adjust(d.get("unit"), q, un, d.get("kind"),
                           (d.get("note") or "").strip() or None, d.get("at") or None,
                           interface=UI)
        return {"event": ev["id"]}
    if action == "correct":
        fields = {}
        q, un = qty()
        if q is not None:
            fields["quantity"], fields["unit"] = q, un
        for key in ("descriptor", "note"):
            if (d.get(key) or "").strip():
                fields[key] = d[key].strip()
        if d.get("at"):
            fields["occurred_at"] = d["at"]
        ev = ops.correct(d.get("event"), fields, (d.get("reason") or "").strip(), interface=UI)
        return {"event": ev["id"]}
    if action == "void":
        ev = ops.void(d.get("event"), (d.get("reason") or "").strip(), interface=UI)
        return {"event": ev["id"]}
    if action == "close":
        u, capture, _ = ops.close_unit(d.get("unit"), d.get("disposition"),
                                       d.get("resolution") or None, d.get("at") or None,
                                       (d.get("note") or "").strip() or None, interface=UI)
        log_line("intake", "health", f"closed unit #{u['ordinal']} — {u['substance']}")
        return {"unit": u["id"], "report": m.render_report(u),
                "capture": str(capture.relative_to(ROOT))}
    if action == "reopen":
        u = ops.reopen(d.get("unit"), (d.get("reason") or "").strip(), interface=UI)
        return {"unit": u["id"]}
    if action == "substance":
        entry = L.add_substance(d.get("name") or "", d.get("category") or "other",
                                d.get("quantity_unit") or "g", interface=UI)
        return {"substance": entry}
    raise m.LedgerError(f"unknown intake action {action!r}")


def git_status():
    _, branch = run(["git", "rev-parse", "--abbrev-ref", "HEAD"])
    _, dirty = run(["git", "status", "--porcelain"])
    fetch_code, _ = run(["git", "fetch", "--quiet"], timeout=15)
    counts_code, counts = run(["git", "rev-list", "--left-right", "--count", "HEAD...@{upstream}"])
    ahead = behind = 0
    if fetch_code == 0 and counts_code == 0 and "\t" in counts:
        a, b = counts.split("\t")
        ahead, behind = int(a), int(b)
    _, remote = run(["git", "remote", "get-url", "origin"])
    remote_disp = re.sub(r"//[^@]+@", "//", remote)  # strip embedded credentials
    public = None
    m = re.search(r"github\.com[:/]([\w.-]+/[\w.-]+?)(?:\.git)?$", remote)
    if m:
        repo = m.group(1)
        if _vis_cache["repo"] != repo or not _vis_cache["checked"]:
            try:
                req = urllib.request.Request(f"https://api.github.com/repos/{repo}",
                                             headers={"User-Agent": "wiki-app"})
                with urllib.request.urlopen(req, timeout=4) as r:
                    public = (r.status == 200)
            except Exception:
                public = False  # 404 for private repos when unauthenticated
            _vis_cache.update(checked=True, public=public, repo=repo)
        public = _vis_cache["public"]
    return {"branch": branch, "dirty": len(dirty.splitlines()) if dirty else 0,
            "ahead": ahead, "behind": behind, "remote": remote_disp, "public": public}


def git_sync(message):
    steps = []
    _, dirty = run(["git", "status", "--porcelain"])
    if dirty:
        run(["git", "add", "-A"])
        code, out = run(["git", "commit", "-m", message or "edit: app sync commit"])
        steps.append(out.splitlines()[0] if out else "committed")
        if code != 0:
            return {"ok": False, "message": "\n".join(steps)}
    code, out = run(["git", "pull", "--rebase", "--quiet"], timeout=120)
    steps.append("pulled" if code == 0 else f"pull failed: {out[-300:]}")
    if code != 0:
        return {"ok": False, "message": "\n".join(steps)}
    code, out = run(["git", "push", "--quiet"], timeout=120)
    steps.append("pushed" if code == 0 else f"push failed: {out[-300:]}")
    return {"ok": code == 0, "message": "\n".join(steps)}


# ---------------------------------------------------------------- server

class Handler(BaseHTTPRequestHandler):
    def log_message(self, *a):
        pass

    def cors(self):
        """CORS headers for /api/intake* and nothing else on this server."""
        if not self.path.startswith("/api/intake"):
            return
        origin = intake_cors_origin(self.headers.get("Origin"))
        if not origin:
            return
        self.send_header("Access-Control-Allow-Origin", origin)
        self.send_header("Vary", "Origin")
        self.send_header("Access-Control-Allow-Methods", "GET, POST, OPTIONS")
        self.send_header("Access-Control-Allow-Headers", "Content-Type")
        # Chrome's Private Network Access preflight: a public page reaching a
        # loopback server is refused without this, silently, with a CORS error
        # that names nothing useful.
        self.send_header("Access-Control-Allow-Private-Network", "true")
        self.send_header("Access-Control-Max-Age", "600")

    def do_OPTIONS(self):
        origin = intake_cors_origin(self.headers.get("Origin"))
        if not self.path.startswith("/api/intake") or not origin:
            self.send_response(404)
            self.send_header("Content-Length", "0")
            self.end_headers()
            return
        self.send_response(204)
        self.cors()
        self.send_header("Content-Length", "0")
        self.end_headers()

    def send(self, code, body, ctype="application/json", extra=None):
        data = body if isinstance(body, bytes) else json.dumps(body).encode()
        self.send_response(code)
        self.send_header("Content-Type", ctype)
        self.send_header("Content-Length", str(len(data)))
        self.cors()
        for k, v in (extra or {}).items():
            self.send_header(k, v)
        self.end_headers()
        self.wfile.write(data)

    def body_json(self):
        n = int(self.headers.get("Content-Length", 0))
        return json.loads(self.rfile.read(n) or b"{}")

    def do_GET(self):
        url = urllib.parse.urlparse(self.path)
        qs = urllib.parse.parse_qs(url.query)
        try:
            if url.path == "/":
                self.send(200, PAGE.encode(), "text/html; charset=utf-8")
            elif url.path == "/api/tree":
                self.send(200, tree())
            elif url.path == "/api/file":
                p = safe(qs["path"][0])
                if p.is_dir():
                    self.send(200, {"path": qs["path"][0], "dir": True,
                                    "content": "\n".join(f.name for f in sorted(p.iterdir()))})
                elif p.suffix.lower() in TEXT_EXT and p.stat().st_size < 2_000_000:
                    self.send(200, {"path": qs["path"][0],
                                    "content": p.read_text(encoding="utf-8", errors="replace")})
                else:
                    self.send(200, {"path": qs["path"][0], "binary": True,
                                    "content": f"[{p.suffix or 'binary'} file, {p.stat().st_size:,} bytes]"})
            elif url.path == "/api/asset":
                p = safe(qs["path"][0])
                if p.suffix.lower() not in IMG_EXT or not p.is_file():
                    self.send(400, {"error": "not a served image"}); return
                ctype = mimetypes.guess_type(p.name)[0] or "application/octet-stream"
                self.send(200, p.read_bytes(), ctype, {"Cache-Control": "max-age=300"})
            elif url.path == "/api/search":
                self.send(200, search(qs.get("q", [""])[0]))
            elif url.path == "/api/history":
                self.send(200, git_history(qs["path"][0]))
            elif url.path == "/api/recent":
                self.send(200, git_recent())
            elif url.path == "/api/git/status":
                self.send(200, git_status())
            elif url.path.startswith("/api/intake"):
                # Its own try//except: a LedgerError is the operator being told
                # no (a closed unit, an unaccounted remainder), which is a 400
                # with a sentence, never a traceback.
                try:
                    if url.path == "/api/intake":
                        self.send(200, intake_state())
                    elif url.path == "/api/intake/report":
                        self.send(200, intake_report(qs.get("unit", ["active"])[0]))
                    elif url.path == "/api/intake/stats":
                        self.send(200, intake_stats(qs.get("substance", [None])[0],
                                                    qs.get("since", [None])[0],
                                                    qs.get("until", [None])[0]))
                    else:
                        self.send(404, {"error": "not found"})
                except Exception as exc:
                    self.send(400, {"error": str(exc)})
            elif url.path == "/api/download":
                p = safe(qs["path"][0])
                self.send(200, p.read_bytes(), "application/octet-stream",
                          {"Content-Disposition": f'attachment; filename="{p.name}"'})
            else:
                self.send(404, {"error": "not found"})
        except (PermissionError, KeyError, FileNotFoundError) as e:
            self.send(400, {"error": str(e)})

    def do_POST(self):
        try:
            d = {}
            if self.path not in ("/api/upload", "/api/upload-image"):
                d = self.body_json()
            if self.path == "/api/capture":
                if not d.get("body", "").strip():
                    self.send(400, {"error": "empty note"}); return
                self.send(200, save_note(d["body"], d.get("title") or None,
                                         [t.strip() for t in d.get("tags", "").split(",") if t.strip()],
                                         d.get("targets") or None))
            elif self.path == "/api/save":
                if not d.get("content", "").strip():
                    self.send(400, {"error": "refusing to save an empty page"}); return
                self.send(200, save_page(d["path"], d["content"],
                                         d.get("summary"), bool(d.get("create"))))
            elif self.path == "/api/rename":
                self.send(200, rename_page(d["path"], d["newName"]))
            elif self.path == "/api/upload-image":
                name = Path(urllib.parse.unquote(self.headers.get("X-Filename", "image.png"))).name
                n = int(self.headers.get("Content-Length", 0))
                if n <= 0 or n > 25_000_000:
                    self.send(400, {"error": "invalid image size (0–25MB)"}); return
                self.send(200, upload_image(name, self.rfile.read(n)))
            elif self.path == "/api/upload":
                name = Path(urllib.parse.unquote(self.headers.get("X-Filename", "upload.bin"))).name
                n = int(self.headers.get("Content-Length", 0))
                if n > 500_000_000:
                    self.send(400, {"error": "file too large (500MB cap)"}); return
                INBOX.mkdir(exist_ok=True)
                dest = INBOX / f"{stamp()}_{name}"
                with open(dest, "wb") as f:
                    remaining = n
                    while remaining:
                        chunk = self.rfile.read(min(65536, remaining))
                        if not chunk: break
                        f.write(chunk); remaining -= len(chunk)
                self.send(200, {"saved": str(dest.relative_to(ROOT)), "bytes": n})
            elif self.path == "/api/export":
                self.send(200, export(d))
            elif self.path == "/api/ingest/pack":
                self.send(200, ingest_pack(d["item"]))
            elif self.path == "/api/ingest/apply":
                if not d.get("response", "").strip():
                    self.send(400, {"error": "empty response text"}); return
                self.send(200, ingest_apply(d["response"], bool(d.get("commit"))))
            elif self.path.startswith("/api/intake/"):
                try:
                    self.send(200, {"ok": True,
                                    "result": intake_action(self.path.rsplit("/", 1)[-1], d),
                                    "state": intake_state()})
                except Exception as exc:
                    self.send(400, {"error": str(exc)})
            elif self.path == "/api/git/sync":
                self.send(200, git_sync(d.get("message", "")))
            elif self.path == "/api/delete-inbox":
                p = safe(d["path"])
                if p.parent != INBOX:
                    self.send(400, {"error": "can only delete inbox items"}); return
                shutil.rmtree(p) if p.is_dir() else p.unlink()
                self.send(200, {"deleted": d["path"]})
            else:
                self.send(404, {"error": "not found"})
        except Exception as e:
            self.send(500, {"error": str(e)})


PAGE = r"""<!doctype html>
<html lang="en">
<head>
<meta charset="utf-8">
<meta name="viewport" content="width=device-width, initial-scale=1">
<title>WikiBrain</title>
<style>
/* ================= Vector-skin imitation ================= */
html,body{margin:0;padding:0}
body{background:#f6f6f6 url() repeat-x; font:13px/1.5 sans-serif; color:#202122}
a{color:#0645ad; text-decoration:none}
a:hover{text-decoration:underline}
a:visited{color:#0b0080}
a.new, a.new:visited{color:#ba0000}
a.external{color:#36b}
#mw-page-base{height:5em; background:linear-gradient(to bottom, #f6f6f6 50%, #ffffff 100%); position:absolute; top:0; left:0; right:0; z-index:0}

/* ---- personal bar ---- */
#p-personal{position:absolute; top:.33em; right:1em; z-index:5; font-size:.75em}
#p-personal ul{list-style:none; margin:0; padding:0}
#p-personal li{display:inline-block; margin-left:1em}
#p-personal .uicon::before{content:""; display:inline-block; width:12px; height:12px; margin-right:4px;
  border-radius:50% 50% 0 0; background:#54595d;
  box-shadow:0 7px 0 -1px #54595d; vertical-align:-2px}
#gitPill{color:#54595d}
#gitPill b{color:#202122}
#syncLink{cursor:pointer}

/* ---- head: tabs + search ---- */
#mw-head{position:absolute; top:0; right:0; left:11em; z-index:4; height:5em}
#left-navigation{float:left; margin-top:2.5em}
#right-navigation{float:right; margin-top:2.5em}
ul.vectorTabs{list-style:none; margin:0; padding:0; float:left; height:2.5em;
  background:linear-gradient(to bottom, rgba(167,215,249,0) 0%, #a7d7f9 100%);
  background-repeat:no-repeat; background-size:1px 100%}
ul.vectorTabs li{float:left; height:2.5em; display:block;
  background:linear-gradient(to bottom, rgba(167,215,249,0) 0%, #a7d7f9 100%) no-repeat right / 1px 100%}
ul.vectorTabs li a{display:block; height:1.9em; padding:.6em .8em 0;
  color:#0645ad; font-size:.8em; cursor:pointer;
  background:linear-gradient(to bottom, rgba(255,255,255,.4) 0, #eef4fa 100%);
  box-shadow:inset 0 -1px 0 #77c1f6}
ul.vectorTabs li.selected a{background:#ffffff; color:#202122; box-shadow:none}
ul.vectorTabs li.disabled a{color:#a2a9b1; cursor:default}
ul.vectorTabs li.icononly a{color:#54595d}
#ca-more{position:relative}
#ca-more ul{display:none; position:absolute; top:2.5em; right:0; list-style:none; margin:0; padding:0;
  background:#fff; border:1px solid #a7d7f9; border-top:0; min-width:9em; z-index:9}
#ca-more:hover ul, #ca-more.open ul{display:block}
#ca-more ul li{float:none; height:auto; background:none}
#ca-more ul li a{background:none; height:auto; padding:.5em .8em; white-space:nowrap}
#ca-more ul li a:hover{background:#eaf3ff}

/* ---- search ---- */
#p-search{float:left; margin:2.75em 1em 0 .5em; position:relative}
#searchForm{display:flex}
#searchInput{width:14em; padding:.25em 1.7em .25em .4em; border:1px solid #a2a9b1; border-radius:2px;
  font-size:.8em; background:#fff; color:#202122; outline:none}
#searchInput:focus{border-color:#3366cc; box-shadow:inset 0 0 0 1px #36c}
#searchGo{margin-left:-1.6em; border:0; background:none; cursor:pointer; color:#54595d; font-size:.9em}
#suggestions{position:absolute; top:1.9em; left:0; right:0; background:#fff; border:1px solid #a2a9b1;
  display:none; z-index:10; font-size:.8em; box-shadow:0 2px 4px rgba(0,0,0,.15)}
#suggestions a{display:block; padding:.35em .5em; color:#202122; border-bottom:1px solid #eaecf0}
#suggestions a b{color:#202122}
#suggestions a .d{color:#72777d; font-size:.9em; margin-left:.4em}
#suggestions a.sel, #suggestions a:hover{background:#eaf3ff; text-decoration:none}

/* ---- left panel ---- */
#mw-panel{position:absolute; top:0; left:0; width:11em; z-index:3; font-size:inherit; padding-top:.5em}
#p-logo{width:10em; height:absolute; margin:0 auto; text-align:center; padding:.6em 0 .4em}
#p-logo .globe{width:105px; height:105px; margin:0 auto; display:block}
#p-logo .wordmark{font-family:'Linux Libertine','Hoefler Text',Georgia,'Times New Roman',serif;
  font-size:1.62em; color:#202122; letter-spacing:.02em; margin-top:.1em; cursor:pointer}
#p-logo .tagline{font-family:Georgia,serif; font-size:.72em; color:#54595d; font-style:italic}
.portal{margin:0 .6em 0 .7em; padding:.25em 0}
.portal h3{font-size:.75em; color:#4d4d4d; font-weight:normal; margin:0 0 .3em;
  border-bottom:1px solid rgba(0,0,0,.12); padding:.25em 0 .15em .35em}
.portal ul{list-style:none; margin:0; padding:0 0 0 .35em}
.portal li{padding:.28em 0; font-size:.75em; line-height:1.1}
.portal li a{color:#0645ad; cursor:pointer}
.portal li .cnt{color:#72777d; font-size:.92em}

/* ---- content ---- */
#content{position:relative; z-index:2; margin-left:11em; margin-top:5em; padding:1.1em 1.5em 1.5em;
  background:#ffffff; border:1px solid #a7d7f9; border-right-width:0; color:#202122; min-height:70vh}
#firstHeading{font-family:'Linux Libertine','Hoefler Text',Georgia,'Times New Roman',serif;
  font-size:1.83em; font-weight:normal; margin:0; padding:0 0 .17em; line-height:1.3;
  border-bottom:1px solid #a2a9b1; overflow:hidden}
#siteSub{font-size:.86em; color:#54595d; margin:.35em 0 0}
#contentSub{font-size:.83em; color:#54595d; margin:.2em 0 .6em; line-height:1.2em}
#bodyContent{font-size:.875em; line-height:1.6; margin-top:.6em}
#bodyContent h2{font-family:'Linux Libertine','Hoefler Text',Georgia,'Times New Roman',serif;
  font-size:1.5em; font-weight:normal; border-bottom:1px solid #a2a9b1; margin:1em 0 .25em; padding:0}
#bodyContent h3{font-size:1.2em; font-weight:bold; margin:.9em 0 .25em}
#bodyContent h4{font-size:1.05em; font-weight:bold; margin:.8em 0 .25em}
#bodyContent p{margin:.5em 0}
#bodyContent ul{margin:.3em 0 .3em 1.6em; padding:0}
#bodyContent ol{margin:.3em 0 .3em 2em; padding:0}
#bodyContent li{margin-bottom:.1em}
#bodyContent hr{border:0; border-top:1px solid #a2a9b1; margin:.6em 0}
#bodyContent blockquote{border-left:4px solid #eaecf0; padding:.4em 1em; margin:.6em 0 .6em 1em; color:#42474d}
#bodyContent code{background:#f8f9fa; border:1px solid #eaecf0; border-radius:2px; padding:1px 4px;
  font-family:'Courier New',monospace; font-size:.95em}
#bodyContent pre{background:#f8f9fa; border:1px solid #eaecf0; padding:1em; overflow-x:auto;
  font-family:'Courier New',monospace; font-size:.92em; line-height:1.4}
#bodyContent pre code{border:0; background:none; padding:0}
#bodyContent mark{background:#ffe57e; border-radius:2px; padding:0 1px}
.mw-headline{}
.mw-editsection{font-family:sans-serif; font-size:small; font-weight:normal; margin-left:1em; user-select:none}
.mw-editsection a{color:#0645ad; cursor:pointer}
.hatnote{font-style:italic; color:#54595d; padding-left:1.6em; margin:.3em 0 .5em; font-size:.95em}

/* ---- TOC ---- */
#toc{display:table; background:#f8f9fa; border:1px solid #a2a9b1; padding:7px 12px; font-size:95%; margin:1em 0}
#toc .toctitle{text-align:center; font-weight:bold}
#toc .toctoggle{font-size:.85em; font-weight:normal}
#toc .toctoggle a{cursor:pointer}
#toc ul{list-style:none; margin:.3em 0 0; padding:0}
#toc ul ul{margin:0 0 0 2em}
#toc li{margin-bottom:.1em; font-size:.95em}
#toc .tocnumber{color:#202122; padding-right:.5em}
#toc.collapsed ul{display:none}

/* ---- infobox ---- */
.infobox{float:right; clear:right; width:22.7em; margin:.5em 0 1em 1em; border:1px solid #a2a9b1;
  background:#f8f9fa; font-size:88%; line-height:1.5em; padding:.2em; border-collapse:collapse}
.infobox caption{font-size:125%; font-weight:bold; padding:.2em; text-align:center}
.infobox th.ibhead{background:#eaecf0; font-size:114%; text-align:center; padding:.3em}
.infobox th[scope=row]{text-align:left; vertical-align:top; background:none; width:40%;
  padding:.25em .6em .25em .2em; font-weight:bold}
.infobox td{vertical-align:top; padding:.25em .2em}
.infobox tr{border:0}
.infobox .ibimage{text-align:center; padding:.4em 0 .1em}
.infobox .ibimage img{max-width:250px; max-height:280px}
.infobox .ibcaption{text-align:center; font-size:92%; color:#54595d; padding-bottom:.4em}

/* ---- thumbnails ---- */
.thumb{margin:.5em 0 1.3em 1.4em; width:auto}
.thumb.tright{float:right; clear:right}
.thumb.tleft{float:left; clear:left; margin:.5em 1.4em 1.3em 0}
.thumbinner{border:1px solid #c8ccd1; background:#f8f9fa; padding:3px; font-size:94%;
  text-align:center; overflow:hidden; width:auto; max-width:270px}
.thumbinner img{max-width:260px; height:auto; display:block; margin:0 auto; background:#fff; border:1px solid #c8ccd1}
.thumbcaption{text-align:left; line-height:1.4; padding:3px; font-size:94%; color:#202122}
#bodyContent img.inline{max-width:100%}

/* ---- tables ---- */
table.wikitable{background:#f8f9fa; color:#202122; border:1px solid #a2a9b1; border-collapse:collapse;
  margin:1em 0; font-size:100%}
table.wikitable th{background:#eaecf0; text-align:center; border:1px solid #a2a9b1; padding:.2em .4em}
table.wikitable td{border:1px solid #a2a9b1; padding:.2em .4em}

/* ---- references / navbox / categories ---- */
.references{font-size:90%; margin-left:1.6em}
.references li{margin-bottom:.2em}
.references cite{font-style:normal; font-family:'Courier New',monospace; font-size:.95em}
.navbox{border:1px solid #a2a9b1; width:100%; margin:1em auto 0; clear:both; font-size:88%;
  background:#fdfdfd; border-collapse:separate; border-spacing:0}
.navbox th.nbhead{background:#ccccff; padding:.25em 1em; text-align:center; font-size:114%}
.navbox th.nbgroup{background:#ddddff; padding:.25em 1em; white-space:nowrap; text-align:right; width:1%}
.navbox td{padding:.25em .7em; border-top:1px solid #fdfdfd; text-align:left}
.navbox .claim{color:#54595d}
#catlinks{border:1px solid #a2a9b1; background:#f8f9fa; padding:5px; margin-top:1em; clear:both; font-size:.87em}
#catlinks a{cursor:pointer}
#footerArea{margin-left:11em; padding:.9em 1.5em 2em; font-size:.7em; color:#54595d}
#footerArea li{display:inline; margin-right:1.2em}
#footerArea ul{list-style:none; margin:0; padding:0}

/* ---- site notice ---- */
#siteNotice{display:none; margin:-.5em 0 .8em; border:1px solid #fde29b; background:#fef6e7;
  padding:.5em 1em; font-size:.85em; text-align:center}

/* ---- edit page ---- */
#editArea{display:none}
.editnotice{border:1px solid #fde29b; background:#fef6e7; padding:.6em 1em; font-size:.85em; margin:.6em 0}
#editToolbar{border:1px solid #c8ccd1; border-bottom:0; background:#f8f9fa; padding:.3em .4em; display:flex; gap:.25em}
#editToolbar button{border:1px solid #c8ccd1; background:#fff; border-radius:2px; min-width:2em;
  padding:.25em .5em; cursor:pointer; font-size:.9em; color:#202122}
#editToolbar button:hover{background:#eaf3ff; border-color:#36c}
#editToolbar b{font-family:serif}
#wpTextbox{width:100%; box-sizing:border-box; min-height:62vh; border:1px solid #c8ccd1; padding:.6em;
  font:13px/1.5 'Courier New',monospace; color:#202122; background:#fff; resize:vertical; outline:none}
#editOptions{border:1px solid #c8ccd1; border-top:0; background:#eaecf0; padding:.7em 1em; margin-bottom:.7em}
#editOptions label{font-size:.85em; color:#54595d; display:block; margin-bottom:.25em}
#wpSummary{width:60%; padding:.35em .5em; border:1px solid #a2a9b1; border-radius:2px; font:inherit}
.mw-btn{display:inline-block; padding:.45em 1em; border-radius:2px; border:1px solid #a2a9b1;
  background:#f8f9fa; color:#202122; font-weight:bold; font-size:.9em; cursor:pointer; margin-right:.6em}
.mw-btn.progressive{background:#36c; border-color:#36c; color:#fff}
.mw-btn.progressive:hover{background:#447ff5}
.mw-btn:disabled{opacity:.5; cursor:default}
#previewNote{border:1px solid #fde29b; background:#fef6e7; padding:.5em 1em; margin:1em 0 .5em;
  font-size:.9em; display:none}
#previewOut{margin-bottom:1em}
.msg{font-size:.85em; color:#d33; margin-top:.5em; white-space:pre-wrap}

/* ---- history / recent / search results ---- */
#pagehistory{list-style:none; margin:.5em 0; padding:0}
#pagehistory li{padding:.25em .4em; border-bottom:1px solid #f0f1f2; font-size:.95em}
#pagehistory .mw-changeslist-date{color:#202122; font-weight:normal}
#pagehistory .hist-author{color:#0645ad; margin:0 .4em}
#pagehistory .comment{color:#54595d; font-style:italic}
#pagehistory .curprev{color:#72777d; font-size:.85em; margin-right:.5em}
.mw-search-result{margin:.6em 0 1em}
.mw-search-result .title{font-size:1.08em}
.mw-search-result .snippet{color:#42474d; font-size:.92em; margin:.15em 0}
.mw-search-result .meta{color:#72777d; font-size:.8em}

/* ---- special pages (capture / ingest / export) ---- */
.spForm{max-width:640px}
.spForm label{display:block; font-size:.8em; color:#54595d; margin:.9em 0 .25em; font-weight:bold}
.spForm input[type=text], .spForm textarea, .spForm select{width:100%; box-sizing:border-box;
  padding:.45em .6em; border:1px solid #a2a9b1; border-radius:2px; font:inherit; background:#fff; color:#202122}
.spForm textarea{min-height:180px; resize:vertical; line-height:1.5}
.acwrap{position:relative}
#ac{position:absolute; left:0; right:0; z-index:10; background:#fff; border:1px solid #a2a9b1;
  box-shadow:0 2px 6px rgba(0,0,0,.15); max-height:220px; overflow-y:auto; display:none; font-size:.9em}
#ac div{padding:.4em .6em; cursor:pointer}
#ac div .d{color:#72777d; font-size:.85em; margin-left:.5em}
#ac div.sel{background:#eaf3ff}
#targets{display:flex; flex-wrap:wrap; gap:6px; margin-top:8px}
.tchip{display:inline-flex; align-items:center; gap:6px; background:#eaf3ff; border:1px solid #a7d7f9;
  border-radius:2px; padding:2px 8px; font-size:.85em}
.tchip button{border:0; background:none; color:#54595d; cursor:pointer; padding:0}
#drop{margin-top:14px; border:2px dashed #a2a9b1; border-radius:2px; padding:20px; text-align:center;
  color:#54595d; cursor:pointer; font-size:.9em}
#drop.over{border-color:#36c; color:#36c}
.inb{display:flex; align-items:center; gap:10px; padding:.5em .7em; border:1px solid #c8ccd1;
  margin:.35em 0; font-size:.9em; cursor:pointer; background:#f8f9fa}
.inb.sel{border-color:#36c; background:#eaf3ff}
.inb .nm{flex:1; overflow:hidden; text-overflow:ellipsis; white-space:nowrap}
.inb .sz{color:#72777d; font-size:.85em}
.inb button{border:0; background:none; color:#72777d; cursor:pointer}
.inb button:hover{color:#d33}
.step{border:1px solid #c8ccd1; padding:.9em 1.1em; margin:.8em 0; background:#f8f9fa}
.step h3{margin:.1em 0 .3em}
.step .hint{font-size:.85em; color:#54595d; margin-bottom:.5em}
.note{background:#eaf3ff; border:1px solid #a7d7f9; padding:.6em 1em; font-size:.85em; color:#54595d; margin-top:1em}

/* ---- Special:Intake ---- */
.iwarn{background:#fee7e6; border:1px solid #d33; padding:.6em 1em; font-size:.85em; margin:0 0 1em}
.iunit{border:1px solid #c8ccd1; background:#fff; padding:.8em 1em; margin:.7em 0}
.iunit.closed{background:#f8f9fa; color:#54595d}
.iunit h3{margin:0 0 .15em; font-family:Georgia,serif; font-weight:normal; font-size:1.15em}
.iunit .imeta{font-size:.82em; color:#54595d; margin-bottom:.5em}
.ibig{font-size:1.5em; font-family:Georgia,serif; color:#202122}
.ibig small{font-size:.5em; color:#72777d}
.icov{font-size:.8em; color:#72777d; font-style:italic; margin:.3em 0}
/* The quick-log row. If logging is annoying the data dies, so this is one line
   of controls on the unit itself — no dialog, no page change, Enter saves. */
.iquick{display:flex; gap:.4em; align-items:center; flex-wrap:wrap; margin:.5em 0 .2em}
.iquick input[type=text]{width:5.5em; padding:.35em .4em; border:1px solid #a2a9b1; font-size:1em}
.iquick select{padding:.35em; border:1px solid #a2a9b1}
.iquick .desc{width:11em}
.imore{font-size:.82em; color:#54595d; margin:.4em 0 0}
.imore label{display:inline-block; margin-right:1em; font-weight:normal; text-transform:none}
.ievents{font:12px/1.55 'Courier New',monospace; background:#f8f9fa; border:1px solid #eaecf0;
  padding:.5em .7em; margin:.5em 0 0; white-space:pre; overflow-x:auto; color:#202122}
.ireport{font:12px/1.5 'Courier New',monospace; background:#f8f9fa; border:1px solid #c8ccd1;
  padding:1em; white-space:pre; overflow-x:auto}
.igrid{display:flex; gap:1.5em; flex-wrap:wrap; align-items:flex-start}
.igrid > div{flex:1; min-width:300px}
.ipill{display:inline-block; font-size:.75em; border:1px solid #a2a9b1; border-radius:2px;
  padding:.05em .45em; margin-left:.4em; color:#54595d; background:#f8f9fa}

dialog{border:1px solid #a2a9b1; background:#fff; color:#202122; padding:1.3em 1.5em; max-width:460px;
  box-shadow:0 8px 30px rgba(0,0,0,.3)}
dialog::backdrop{background:rgba(0,0,0,.35)}
dialog h3{margin-top:0; font-family:'Linux Libertine',Georgia,serif; font-weight:normal;
  border-bottom:1px solid #a2a9b1; padding-bottom:.2em}
dialog input[type=text]{width:100%; box-sizing:border-box; padding:.45em .6em; border:1px solid #a2a9b1;
  border-radius:2px; font:inherit; margin:.5em 0}
dialog select{padding:.35em; border:1px solid #a2a9b1; font:inherit}

@media(max-width:900px){
  #mw-panel{display:none}
  #mw-head{left:0}
  #content,#footerArea{margin-left:0}
}
</style>
</head>
<body>

<div id="mw-page-base"></div>

<div id="p-personal"><ul>
  <li><span class="uicon"></span>Dan Frank</li>
  <li><span id="gitPill">…</span></li>
  <li><a id="syncLink">Sync</a></li>
</ul></div>

<div id="mw-head">
  <div id="left-navigation">
    <ul class="vectorTabs">
      <li id="ca-page" class="selected"><a>Page</a></li>
      <li id="ca-talk"><a>Discussion</a></li>
    </ul>
  </div>
  <div id="right-navigation">
    <ul class="vectorTabs">
      <li id="ca-view" class="selected"><a>Read</a></li>
      <li id="ca-edit"><a>Edit</a></li>
      <li id="ca-history"><a>View history</a></li>
      <li id="ca-more"><a>More&nbsp;▾</a>
        <ul><li id="ca-move"><a>Move</a></li></ul>
      </li>
    </ul>
    <div id="p-search">
      <form id="searchForm" autocomplete="off">
        <input id="searchInput" placeholder="Search WikiBrain" autocomplete="off">
        <button id="searchGo" type="submit" title="Search">&#128269;</button>
      </form>
      <div id="suggestions"></div>
    </div>
  </div>
</div>

<div id="mw-panel">
  <div id="p-logo">
    <svg class="globe" viewBox="0 0 120 120" xmlns="http://www.w3.org/2000/svg" aria-hidden="true">
      <defs>
        <radialGradient id="gsh" cx="38%" cy="32%" r="75%">
          <stop offset="0%" stop-color="#fdfdfd"/><stop offset="70%" stop-color="#e8eaed"/>
          <stop offset="100%" stop-color="#c9ccd1"/>
        </radialGradient>
      </defs>
      <circle cx="60" cy="60" r="54" fill="url(#gsh)" stroke="#8a8f96" stroke-width="1.5"/>
      <ellipse cx="60" cy="60" rx="54" ry="20" fill="none" stroke="#9aa0a6" stroke-width="1"/>
      <ellipse cx="60" cy="60" rx="54" ry="40" fill="none" stroke="#b7bcc2" stroke-width=".8"/>
      <ellipse cx="60" cy="60" rx="20" ry="54" fill="none" stroke="#9aa0a6" stroke-width="1"/>
      <ellipse cx="60" cy="60" rx="40" ry="54" fill="none" stroke="#b7bcc2" stroke-width=".8"/>
      <line x1="6" y1="60" x2="114" y2="60" stroke="#9aa0a6" stroke-width="1"/>
      <line x1="60" y1="6" x2="60" y2="114" stroke="#9aa0a6" stroke-width="1"/>
      <text x="60" y="72" text-anchor="middle" font-family="Georgia,serif" font-size="34" fill="#54595d">DF</text>
    </svg>
    <div class="wordmark" id="logoHome">WikiBrain</div>
    <div class="tagline">The Dan Frank Encyclopedia</div>
  </div>
  <div class="portal">
    <h3>Navigation</h3>
    <ul>
      <li><a id="nav-main">Main page</a></li>
      <li><a id="nav-contents">Contents</a></li>
      <li><a id="nav-random">Random article</a></li>
      <li><a id="nav-recent">Recent changes</a></li>
    </ul>
  </div>
  <div class="portal">
    <h3>Domains</h3>
    <ul id="domainList"></ul>
  </div>
  <div class="portal">
    <h3>Tools</h3>
    <ul>
      <li><a id="nav-whatlinks">What links here</a></li>
      <li><a id="nav-capture">Capture a note</a></li>
      <li><a id="nav-ingest">Ingest inbox <span class="cnt" id="inboxN"></span></a></li>
      <li><a id="nav-export">Export corpus</a></li>
      <li><a id="nav-intake">Intake ledger <span class="cnt" id="intakeN"></span></a></li>
      <li><a id="nav-newpage">Create a page</a></li>
    </ul>
  </div>
  <div class="portal">
    <h3>Project files</h3>
    <ul id="metaList"></ul>
  </div>
</div>

<div id="content">
  <div id="siteNotice">⚠ The GitHub repo backing this wiki is <b>PUBLIC</b> — anyone can read it.
    Make it private: repo Settings → Danger Zone → Change visibility.</div>
  <h1 id="firstHeading">Loading…</h1>
  <div id="siteSub">From WikiBrain, the personal encyclopedia</div>
  <div id="contentSub"></div>
  <div id="bodyContent"></div>

  <div id="editArea">
    <div class="editnotice" id="editNotice">You are editing this page directly. Complete sentences;
      tables hold numbers, prose holds meaning; contradictions are flagged, not overwritten
      (<i>STYLE_GUIDE.md</i> governs). Saving updates <code>date_modified</code> and appends to the log.</div>
    <div id="previewNote"><b>Preview only</b> — your changes have not been saved yet.</div>
    <div id="previewOut"></div>
    <div id="editToolbar">
      <button data-tb="bold" title="Bold"><b>B</b></button>
      <button data-tb="italic" title="Italic"><i>I</i></button>
      <button data-tb="link" title="Internal wikilink">[[&nbsp;]]</button>
      <button data-tb="h2" title="Section heading">H2</button>
      <button data-tb="image" title="Insert picture">&#128444; Image</button>
      <button data-tb="table" title="Insert table">Table</button>
    </div>
    <textarea id="wpTextbox" spellcheck="false"></textarea>
    <div id="editOptions">
      <label for="wpSummary">Edit summary (briefly describe your changes)</label>
      <input id="wpSummary" type="text" placeholder="">
      <div style="margin-top:.7em">
        <button class="mw-btn progressive" id="wpSave">Save changes</button>
        <button class="mw-btn" id="wpPreview">Show preview</button>
        <button class="mw-btn" id="wpCancel">Cancel</button>
        <span class="msg" id="editMsg" style="display:inline-block; margin-left:.6em"></span>
      </div>
    </div>
  </div>
</div>

<div id="footerArea">
  <ul>
    <li id="lastmod"></li>
    <li>Content is personal and private; the wiki is the compiled product of raw/ — treat earned pages with respect.</li>
    <li>Powered by a single Python file. Wikipedia-style interface (imitation, for personal use).</li>
  </ul>
</div>

<dialog id="renameDlg">
  <h3>Move page</h3>
  <div style="font-size:.85em; color:#54595d">Renames the file and updates every inbound link.<br>
    Source: <code id="renameFrom"></code></div>
  <input type="text" id="renameTo" placeholder="New title (will be slugified)">
  <div>
    <button class="mw-btn progressive" id="renameGo">Move page</button>
    <button class="mw-btn" id="renameCancel">Cancel</button>
  </div>
  <div class="msg" id="renameMsg"></div>
</dialog>

<dialog id="imageDlg">
  <h3>Insert picture</h3>
  <div style="font-size:.85em; color:#54595d; margin-bottom:.5em">
    The file is uploaded to <code>assets/uploads/</code> and embedded at the cursor.</div>
  <input type="file" id="imgFile" accept="image/*">
  <input type="text" id="imgCaption" placeholder="Caption">
  <div style="font-size:.85em; margin:.4em 0">
    Placement:
    <select id="imgPlace">
      <option value="thumb">Thumbnail (right, with caption)</option>
      <option value="left">Thumbnail (left, with caption)</option>
      <option value="inline">Inline (full width)</option>
    </select>
  </div>
  <div>
    <button class="mw-btn progressive" id="imgGo">Upload &amp; insert</button>
    <button class="mw-btn" id="imgCancel">Cancel</button>
  </div>
  <div class="msg" id="imgMsg"></div>
</dialog>

<dialog id="newPageDlg">
  <h3>Create a page</h3>
  <div style="font-size:.85em; color:#54595d">Pick a domain and a title; the page opens in the editor
    with frontmatter pre-filled.</div>
  <select id="npDomain" style="width:100%; margin-top:.5em">
    <option>self</option><option>timeline</option><option selected>people</option><option>mind</option>
    <option>work</option><option>interests</option><option>health</option><option>places</option><option>legal</option>
  </select>
  <input type="text" id="npTitle" placeholder="Page title">
  <div>
    <button class="mw-btn progressive" id="npGo">Create in editor</button>
    <button class="mw-btn" id="npCancel">Cancel</button>
  </div>
  <div class="msg" id="npMsg"></div>
</dialog>

<template id="tpl-capture">
  <div class="spForm">
    <p style="color:#54595d">Type a fact or story — it lands in the inbox for ingestion. Type <b>@</b> to
    target an existing page (correction/expansion). Square-bracket lines like
    <code>[RENAME PAGE TO x]</code> are executed as instructions at ingest time.</p>
    <label>Title (optional)</label>
    <input type="text" id="cTitle">
    <label>Text</label>
    <div class="acwrap">
      <textarea id="cBody" placeholder="A fact, a memory, a story… @ to target a page."></textarea>
      <div id="ac"></div>
    </div>
    <div id="targets"></div>
    <label>Tags (optional, comma-separated)</label>
    <input type="text" id="cTags">
    <div style="margin-top:.8em"><button class="mw-btn progressive" id="cSave">Save to inbox</button></div>
    <div class="msg" id="cMsg"></div>
    <div id="drop">Drop files here or click to upload — any format</div>
    <input type="file" id="filePick" multiple style="display:none">
    <div class="msg" id="uMsg"></div>
  </div>
</template>

<template id="tpl-ingest">
  <div style="display:flex; gap:2em; flex-wrap:wrap">
    <div style="flex:0 0 300px">
      <h2 style="border-bottom:1px solid #a2a9b1; font-family:Georgia,serif; font-weight:normal">Inbox</h2>
      <p style="color:#54595d; font-size:.9em">Select an item to ingest. Ingestion moves it to raw/ and writes wiki pages.</p>
      <div id="inboxList"></div>
      <div class="note">Prefer Claude Code? Open it in this folder and say "ingest the inbox" — same rules, fully automatic.</div>
    </div>
    <div style="flex:1; min-width:320px" class="spForm">
      <h2 style="border-bottom:1px solid #a2a9b1; font-family:Georgia,serif; font-weight:normal">Ingest with any LLM</h2>
      <div class="step">
        <h3>1 · Generate the prompt</h3>
        <div class="hint">Bundles the item, the style guide, and the pages it touches.</div>
        <button class="mw-btn progressive" id="packBtn" disabled>Generate prompt</button>
        <span class="msg" id="packMsg"></span>
        <textarea id="packOut" readonly style="display:none; min-height:120px; margin-top:10px; font:12px 'Courier New',monospace"></textarea>
        <button class="mw-btn" id="copyBtn" style="display:none; margin-top:.5em">Copy prompt to clipboard</button>
      </div>
      <div class="step">
        <h3>2 · Paste the model's reply</h3>
        <div class="hint">Paste the full response (its FILE/MOVE/LOG blocks are extracted; extra prose is ignored).</div>
        <textarea id="applyIn" style="min-height:140px; font:12px 'Courier New',monospace" placeholder="===FILE: wiki/... ==="></textarea>
        <label style="font-weight:normal; text-transform:none; margin-top:.5em">
          <input type="checkbox" id="applyCommit" checked> commit automatically if lint passes</label>
        <button class="mw-btn progressive" id="applyBtn">Validate &amp; apply</button>
        <div class="msg" id="applyMsg"></div>
      </div>
    </div>
  </div>
</template>

<template id="tpl-export">
  <div class="spForm">
    <p style="color:#54595d">One Markdown file for LLM ingestion, with a token estimate.</p>
    <label>Scope</label>
    <select id="eDomain">
      <option value="">Whole wiki</option>
      <option>self</option><option>timeline</option><option>people</option>
      <option>mind</option><option>work</option><option>interests</option>
      <option>health</option><option>places</option><option>legal</option>
    </select>
    <label style="font-weight:normal; text-transform:none; margin-top:.8em">
      <input type="checkbox" id="eRaw"> include raw/ archive (big)</label>
    <label style="font-weight:normal; text-transform:none">
      <input type="checkbox" id="eInbox"> include un-ingested inbox</label>
    <div style="margin-top:.8em"><button class="mw-btn progressive" id="eGo">Export</button></div>
    <div class="msg" id="eMsg"></div>
  </div>
</template>

<template id="tpl-intake">
  <div id="iwarn"></div>
  <p style="color:#54595d; max-width:70ch">A finite object enters the record; every known
  disposition of it is recorded after that. At closure the ledger reconciles what is known,
  preserves what is unknown, and computes only what the evidence supports.
  <a href="#" id="iHelp">How it works</a>.</p>
  <div class="igrid">
    <div style="flex:2">
      <h2 style="border-bottom:1px solid #a2a9b1; font-family:Georgia,serif; font-weight:normal">
        Active units</h2>
      <div id="iactive"></div>
      <h2 style="border-bottom:1px solid #a2a9b1; font-family:Georgia,serif; font-weight:normal">
        Closed <span id="iclosedN" style="font-size:.7em; color:#72777d"></span></h2>
      <div id="iclosed"></div>
    </div>
    <div style="flex:1; min-width:300px" class="spForm">
      <div class="step">
        <h3>New unit</h3>
        <div class="hint">What arrived, how much of it, and when.</div>
        <label>What is it?</label>
        <select id="nuSub"></select>
        <div id="nuNew" style="display:none; border-left:3px solid #36c; padding-left:.8em">
          <label>Name</label><input type="text" id="nuName" placeholder="Kratom">
          <label>Category</label><select id="nuCat"></select>
          <label>Default unit</label><select id="nuDefUnit"></select>
          <div style="margin-top:.6em"><button class="mw-btn" id="nuAdd">Add to the catalog</button></div>
          <div class="hint" style="margin-top:.4em">Added once, on purpose — after that every unit
          picks it from the list. Free text produces four spellings of one substance and no
          cross-unit statistic survives that.</div>
        </div>
        <label>Quantity received</label>
        <div class="iquick">
          <input type="text" id="nuQty" placeholder="3.5">
          <select id="nuUnit"></select>
        </div>
        <label>When did you receive it?</label>
        <div class="iquick">
          <input type="text" id="nuAt" placeholder="now" style="width:12em">
          <span class="hint">blank = now; or 2026-08-29 13:42</span>
        </div>
        <label>Source / context (optional)</label><input type="text" id="nuSource">
        <label>Note (optional)</label><input type="text" id="nuNote">
        <div style="margin-top:.9em"><button class="mw-btn progressive" id="nuGo">Create unit</button></div>
        <div class="msg" id="nuMsg"></div>
      </div>
      <div class="note" id="iHelpText" style="display:none">
        <b>Three kinds of event.</b> <i>Measured</i> is a number off a scale. <i>Estimated</i> is a
        number you are guessing at, kept apart so a mean can say how much of itself rests on a
        guess. <i>Unquantified</i> — &ldquo;one line&rdquo;, &ldquo;two hits&rdquo; — carries no
        quantity and is still a real event: it counts toward the event total, the intervals and the
        time-of-day profile, and is excluded from every quantity figure.<br><br>
        <b>Nothing is edited in place.</b> A mistyped 0.5&nbsp;g becomes a correction naming the
        original, the new value and the reason. The ledger shows the corrected number; the log
        remembers both.<br><br>
        <b>Closing asks what happened.</b> If quantity is unaccounted for, the ledger will not
        guess — it asks, records the answer, and prints it on the report from then on.
      </div>
    </div>
  </div>
  <div id="ireport" style="display:none; margin-top:1.5em"></div>
</template>

<script>
const $=s=>document.querySelector(s), api=async(p,o)=>(await fetch(p,o)).json();
let TREE=null, PAGES=new Set(), CUR=null, RAW=null, MODE="read", CREATING=null;
const DOMAINS=["self","timeline","people","mind","work","interests","health","places","legal"];
const cap=s=>s.charAt(0).toUpperCase()+s.slice(1);

/* ============================ utilities ============================ */
function esc(s){return String(s).replace(/&/g,"&amp;").replace(/</g,"&lt;").replace(/>/g,"&gt;")}
function humanTitle(path){
  const base=path.split("/").pop().replace(/\.md$/,"");
  if(base==="index"){
    const parts=path.split("/");
    return parts.length>2?cap(parts[parts.length-2])+" — index":"Main Page";
  }
  return base.split("-").map(w=>/^\d/.test(w)?w:cap(w)).join(" ");
}
function anchorOf(t){return t.toLowerCase().replace(/[^\w\s-]/g,"").trim().replace(/\s+/g,"_")}
function stripMd(s){return s.replace(/\*\*|\*|`|\[\[|\]\]/g,"")}
function imgUrl(u){
  u=u.trim().replace(/^\.\//,"");
  return /^https?:/.test(u)?u:"/api/asset?path="+encodeURIComponent(u);
}
function resolveWiki(target){
  let t=target.trim().replace(/^\.\//,"");
  if(!/\.md$/.test(t)) t+=".md";
  if(PAGES.has(t)) return {path:t, exists:true};
  const hit=[...PAGES].find(p=>p.endsWith("/"+t));
  if(hit) return {path:hit, exists:true};
  // meta files
  const meta=(TREE?TREE.meta:[]).find(f=>f.path===t||f.path.endsWith("/"+t));
  if(meta) return {path:meta.path, exists:true};
  const guess=t.startsWith("wiki/")?t:null;
  return {path:guess, exists:false, raw:target};
}

/* ============================ frontmatter ============================ */
function parseFM(text){
  const out={meta:{}, infobox:null, connections:[], sources:[], aliases:[], body:text, fmLines:0};
  if(!text.startsWith("---")) return out;
  const end=text.indexOf("\n---",3);
  if(end<0) return out;
  const fmText=text.slice(4,end);
  out.body=text.slice(end+4).replace(/^\n/,"");
  out.fmLines=text.slice(0,text.length-out.body.length).split("\n").length-1;
  const lines=fmText.split("\n");
  let i=0;
  while(i<lines.length){
    const l=lines[i];
    const m=l.match(/^([A-Za-z_][\w-]*):\s*(.*)$/);
    if(!m){i++;continue}
    const key=m[1], val=m[2].trim();
    if(val!==""){
      if(key==="aliases"||key==="tags"||key==="related"||key==="sources"){
        const items=val.replace(/^\[|\]$/g,"").split(",").map(s=>s.trim().replace(/^["']|["']$/g,"")).filter(Boolean);
        if(key==="aliases") out.aliases=items;
        if(key==="sources") out.sources=items;
      } else out.meta[key]=val.replace(/^["']|["']$/g,"");
      i++; continue;
    }
    // block value
    const block=[]; i++;
    while(i<lines.length && (/^\s+\S/.test(lines[i])||lines[i].trim()==="")){ block.push(lines[i]); i++; }
    if(key==="infobox"){
      out.infobox={};
      for(const b of block){
        const bm=b.match(/^\s+([\w-]+):\s*(.*)$/);
        if(bm) out.infobox[bm[1]]=bm[2].trim().replace(/^["']|["']$/g,"");
      }
    } else if(key==="connections"){
      let cur=null;
      for(const b of block){
        if(/^\s*-\s/.test(b)){ if(cur) out.connections.push(cur); cur={};
          const bm=b.match(/^\s*-\s*([\w-]+):\s*(.*)$/); if(bm) cur[bm[1]]=bm[2].trim().replace(/^["']|["']$/g,""); }
        else { const bm=b.match(/^\s+([\w-]+):\s*(.*)$/); if(bm&&cur) cur[bm[1]]=bm[2].trim().replace(/^["']|["']$/g,""); }
      }
      if(cur) out.connections.push(cur);
    } else if(key==="sources"){
      for(const b of block){ const bm=b.match(/^\s*-\s*(.+)$/); if(bm) out.sources.push(bm[1].trim().replace(/^["']|["']$/g,"")); }
    } else if(key==="aliases"){
      for(const b of block){ const bm=b.match(/^\s*-\s*(.+)$/); if(bm) out.aliases.push(bm[1].trim().replace(/^["']|["']$/g,"")); }
    }
  }
  return out;
}

/* ============================ markdown ============================ */
function inline(s){
  s=esc(s);
  s=s.replace(/`([^`]+)`/g,"<code>$1</code>");
  s=s.replace(/!\[([^\]]*)\]\(([^)\s]+)\)/g,(m,alt,u)=>
    `<img class="inline" src="${imgUrl(u)}" alt="${alt}">`);
  s=s.replace(/\*\*([^*]+)\*\*/g,"<b>$1</b>").replace(/(^|\W)\*([^*]+)\*/g,"$1<i>$2</i>");
  s=s.replace(/\[([^\]]+)\]\(([^)]+)\)/g,(m,t,u)=>
    /^https?:/.test(u)?`<a href="${u}" class="external" target="_blank" rel="noopener">${t}</a>`
      :`<a href="#" data-wiki="${u}">${t}</a>`);
  s=s.replace(/\[\[([^\]|]+)\|([^\]]+)\]\]/g,`<a href="#" data-wiki="$1">$2</a>`);
  s=s.replace(/\[\[([^\]]+)\]\]/g,`<a href="#" data-wiki="$1">$1</a>`);
  return s;
}
function mdRender(text, opts){
  opts=opts||{};
  const lineOffset=opts.lineOffset||0, editable=!!opts.editable;
  const lines=text.split("\n"); let out=[],toc=[],i=0;
  while(i<lines.length){
    let l=lines[i];
    if(/^```/.test(l)){ let buf=[]; i++;
      while(i<lines.length && !/^```/.test(lines[i])) buf.push(lines[i++]);
      i++; out.push("<pre><code>"+esc(buf.join("\n"))+"</code></pre>"); continue; }
    if(/^#{1,5} /.test(l)){
      const n=l.match(/^#+/)[0].length, raw=l.replace(/^#+ /,"");
      const a=anchorOf(stripMd(raw)), srcLine=i+lineOffset;
      if(n>=2&&n<=3) toc.push({n,txt:stripMd(raw),a});
      const editLink=(editable&&n>=2)?`<span class="mw-editsection">[<a data-editline="${srcLine}">edit</a>]</span>`:"";
      out.push(`<h${n} id="${a}"><span class="mw-headline">${inline(raw)}</span>${editLink}</h${n}>`);
      i++; continue; }
    if(/^---+\s*$/.test(l)){ out.push("<hr>"); i++; continue; }
    if(/^\s*>/.test(l)){ let buf=[];
      while(i<lines.length && /^\s*>/.test(lines[i])) buf.push(lines[i++].replace(/^\s*> ?/,""));
      // reflow: blank quote lines separate paragraphs, others join with a space
      const paras=[]; let cur=[];
      for(const b of buf){ if(b.trim()===""){ if(cur.length){paras.push(cur.join(" "));cur=[];} } else cur.push(b); }
      if(cur.length)paras.push(cur.join(" "));
      out.push("<blockquote>"+paras.map(p=>"<p>"+inline(p)+"</p>").join("")+"</blockquote>"); continue; }
    if(/^\|.*\|/.test(l) && /^\|[\s:|-]+\|/.test(lines[i+1]||"")){
      let rows=[]; while(i<lines.length && /^\|/.test(lines[i])) rows.push(lines[i++]);
      const cells=r=>r.replace(/^\||\|$/g,"").split("|").map(c=>inline(c.trim()));
      let h='<table class="wikitable"><tr>'+cells(rows[0]).map(c=>`<th>${c}</th>`).join("")+"</tr>";
      for(const r of rows.slice(2)) h+="<tr>"+cells(r).map(c=>`<td>${c}</td>`).join("")+"</tr>";
      out.push(h+"</table>"); continue; }
    if(/^\s*[-*] /.test(l)){ let buf=[];
      while(i<lines.length && /^\s*[-*] /.test(lines[i])) buf.push("<li>"+inline(lines[i++].replace(/^\s*[-*] /,""))+"</li>");
      out.push("<ul>"+buf.join("")+"</ul>"); continue; }
    if(/^\s*\d+\. /.test(l)){ let buf=[];
      while(i<lines.length && /^\s*\d+\. /.test(lines[i])) buf.push("<li>"+inline(lines[i++].replace(/^\s*\d+\. /,""))+"</li>");
      out.push("<ol>"+buf.join("")+"</ol>"); continue; }
    if(l.trim()===""){ i++; continue; }
    // standalone image line -> thumbnail frame
    const im=l.trim().match(/^!\[([^\]]*)\]\(([^)\s]+)\)$/);
    if(im){
      out.push(`<div class="thumb tright"><div class="thumbinner">`+
        `<a href="${imgUrl(im[2])}" target="_blank"><img src="${imgUrl(im[2])}" alt="${esc(im[1])}"></a>`+
        (im[1]?`<div class="thumbcaption">${inline(im[1])}</div>`:"")+`</div></div>`);
      i++; continue; }
    let buf=[lines[i++]];   // always consume the current line (guards against non-heading '#…' etc.)
    while(i<lines.length && lines[i].trim()!=="" &&
      !/^(#|```|>|\||\s*[-*] |\s*\d+\. |---)/.test(lines[i])) buf.push(lines[i++]);
    out.push("<p>"+inline(buf.join(" "))+"</p>");
  }
  return {out,toc};
}
function tocHtml(toc){
  if(toc.length<3) return "";
  let h='<div id="toc"><div class="toctitle">Contents <span class="toctoggle">[<a id="tocToggle">hide</a>]</span></div><ul>';
  let n1=0,n2=0,open=false;
  for(const t of toc){
    if(t.n===2){ if(open){h+="</ul></li>";open=false;} n1++; n2=0;
      h+=`<li><span class="tocnumber">${n1}</span><a href="#${t.a}" data-anchor="${t.a}">${esc(t.txt)}</a>`;
      open=true; h+="<ul>"; }
    else { n2++; h+=`<li><span class="tocnumber">${n1}.${n2}</span><a href="#${t.a}" data-anchor="${t.a}">${esc(t.txt)}</a></li>`; }
  }
  if(open)h+="</ul></li>";
  return h+"</ul></div>";
}

/* ============================ infobox / navbox / cats ============================ */
const IB_ORDER=["name","born","status","type","relationship_to_dan","known_for","occupation","partner",
  "location","sex","first_mentioned","first_contact","closed","handles","era","period","notes"];
const IB_LABEL={name:"Name",born:"Born",status:"Status",type:"Type",relationship_to_dan:"Relationship to Dan",
  known_for:"Known for",occupation:"Occupation",partner:"Partner",location:"Location",sex:"Sex",
  first_mentioned:"First mentioned",first_contact:"First contact",closed:"Closed",handles:"Handles",
  era:"Era",period:"Period",notes:"Notes"};
function infoboxHtml(fm, title){
  const fb=fm.infobox;
  const img=fm.meta.image;
  if(!fb&&!img) return "";
  const head=(fb&&fb.name)||title;
  let h='<table class="infobox">';
  h+=`<tr><th class="ibhead" colspan="2">${esc(head)}</th></tr>`;
  if(img) h+=`<tr><td colspan="2" class="ibimage"><img src="${imgUrl(img)}" alt="${esc(head)}"></td></tr>`+
    (fm.meta.image_caption?`<tr><td colspan="2" class="ibcaption">${inline(fm.meta.image_caption)}</td></tr>`:"");
  if(fb){
    const keys=IB_ORDER.filter(k=>k!=="name"&&fb[k]!==undefined&&fb[k]!=="")
      .concat(Object.keys(fb).filter(k=>k!=="name"&&!IB_ORDER.includes(k)));
    for(const k of keys){
      let v=fb[k]; if(v===undefined||v==="")continue;
      if(/^\[[^\[].*\]$/.test(v)) v=v.replace(/^\[|\]$/g,"").split(",").map(s=>s.trim().replace(/^["']|["']$/g,"")).join(", ");
      h+=`<tr><th scope="row">${esc(IB_LABEL[k]||cap(k.replace(/_/g," ")))}</th><td>${inline(v)}</td></tr>`;
    }
  }
  return h+"</table>";
}
function connectionsHtml(conns){
  if(!conns.length) return "";
  let h='<table class="navbox"><tr><th class="nbhead" colspan="2">Connections <span style="font-weight:normal;font-size:85%">(typed edges)</span></th></tr>';
  for(const c of conns){
    if(!c.page)continue;
    h+=`<tr><th class="nbgroup">${esc(c.type||"related")}</th><td><a href="#" data-wiki="${esc(c.page)}">${esc(humanTitle(c.page))}</a>`+
      (c.claim?` — <span class="claim">${esc(c.claim)}</span>`:"")+`</td></tr>`;
  }
  return h+"</table>";
}
function catlinksHtml(fm, path){
  const cats=[];
  const domain=path.startsWith("wiki/")?path.split("/")[1]:null;
  if(domain&&DOMAINS.includes(domain)) cats.push(`<a data-page="wiki/${domain}/index.md">${cap(domain)}</a>`);
  if(fm.meta.page_type) cats.push(`<span>${esc(cap(fm.meta.page_type))} pages</span>`);
  if(fm.meta.status) cats.push(`<span>Status: ${esc(fm.meta.status)}</span>`);
  if(fm.meta.importance) cats.push(`<span>Importance: ${esc(fm.meta.importance)}</span>`);
  if(fm.meta.knowledge) cats.push(`<span>Knowledge: ${esc(fm.meta.knowledge)}</span>`);
  if(!cats.length) return "";
  return `<div id="catlinks"><b>Categories:</b> ${cats.join('<span style="color:#a2a9b1"> | </span>')}</div>`;
}
function referencesHtml(sources){
  if(!sources.length) return "";
  let h='<h2><span class="mw-headline" id="references">References</span></h2><ol class="references">';
  for(const s of sources)
    h+=`<li><cite><a href="#" data-page="${esc(s)}">${esc(s)}</a></cite></li>`;
  return h+"</ol>";
}

/* ============================ article view ============================ */
function articleHtml(content, path, opts){
  opts=opts||{};
  const fm=parseFM(content);
  let title=fm.meta.title||humanTitle(path);
  // a leading H1 in the body becomes the display title (avoid duplication)
  const bl=fm.body.split("\n"); let k=0;
  while(k<bl.length && bl[k].trim()==="") k++;
  if(k<bl.length && /^# /.test(bl[k])){ title=stripMd(bl[k].replace(/^# /,"")); k++; }
  else k=0;
  const body=bl.slice(k).join("\n");
  const editable=!opts.preview&&isEditable(path);
  const r=mdRender(body,{lineOffset:fm.fmLines+k, editable});
  let parts=[];
  // hatnote for aliases
  if(fm.aliases.length)
    parts.push(`<div class="hatnote">Also known as: ${fm.aliases.map(esc).join(" · ")}</div>`);
  parts.push(infoboxHtml(fm,title));
  // TOC goes right before the first h2
  const toc=tocHtml(r.toc);
  const firstH=r.out.findIndex(x=>/^<h2/.test(x));
  if(toc&&firstH>=0) r.out.splice(firstH,0,toc);
  parts=parts.concat(r.out);
  if(fm.sources.length) parts.push(referencesHtml(fm.sources));
  parts.push(connectionsHtml(fm.connections));
  if(!opts.preview) parts.push(catlinksHtml(fm,path));
  return {html:parts.join("\n"), title, fm};
}
function isEditable(path){
  return /^wiki\/.+\.md$/.test(path) ||
    /^(queue|BACKLOG|LLM_HANDOFF)\.md$/.test(path);
}
function wireBody(el){
  el.querySelectorAll("a[data-wiki]").forEach(a=>{
    const res=resolveWiki(a.dataset.wiki);
    if(!res.exists){ a.classList.add("new"); a.title=`${a.dataset.wiki} (page does not exist)`; }
    a.onclick=e=>{
      e.preventDefault();
      if(res.exists) openPage(res.path);
      else if(res.path) openCreate(res.path);
      else alert("Cannot resolve link target: "+a.dataset.wiki);
    };
  });
  el.querySelectorAll("a[data-page]").forEach(a=>{
    a.onclick=e=>{e.preventDefault(); openPage(a.dataset.page);};
  });
  el.querySelectorAll("a[data-editline]").forEach(a=>{
    a.onclick=e=>{e.preventDefault(); openEditor({line:+a.dataset.editline});};
  });
  el.querySelectorAll("a[data-anchor]").forEach(a=>{
    a.onclick=e=>{e.preventDefault();
      const t=document.getElementById(a.dataset.anchor); if(t)t.scrollIntoView({behavior:"smooth"});};
  });
  const tt=el.querySelector("#tocToggle");
  if(tt) tt.onclick=()=>{ const toc=el.querySelector("#toc");
    toc.classList.toggle("collapsed");
    tt.textContent=toc.classList.contains("collapsed")?"show":"hide"; };
}

function setTabs(){
  $("#ca-view").classList.toggle("selected",MODE==="read");
  $("#ca-edit").classList.toggle("selected",MODE==="edit");
  $("#ca-history").classList.toggle("selected",MODE==="history");
  $("#ca-page").classList.toggle("selected",MODE!=="special");
  const isSpecial=MODE==="special";
  $("#ca-edit").style.display=(!isSpecial&&CUR&&isEditable(CUR))?"":"none";
  $("#ca-history").style.display=isSpecial?"none":"";
  $("#ca-more").style.display=(!isSpecial&&CUR&&/^wiki\/.+\.md$/.test(CUR)&&!CUR.endsWith("index.md"))?"":"none";
  $("#ca-talk").className=isSpecial?"disabled":"";
}
function showRead(){
  MODE="read"; CREATING=null;
  $("#editArea").style.display="none";
  $("#bodyContent").style.display="block";
  setTabs();
}

async function openPage(path, highlight){
  CUR=path; RAW=null; CREATING=null; MODE="read";
  if(decodeURIComponent(location.hash.slice(1))!==path)
    location.hash=encodeURIComponent(path);
  const r=await api("/api/file?path="+encodeURIComponent(path));
  const bc=$("#bodyContent");
  $("#editArea").style.display="none"; bc.style.display="block";
  $("#contentSub").innerHTML="";
  $("#siteSub").textContent=path.startsWith("wiki/")
    ?"From WikiBrain, the personal encyclopedia"
    :"Project file — "+path;
  if(r.error){
    $("#firstHeading").textContent="Error";
    bc.innerHTML=`<p>${esc(r.error)}</p>`;
  } else if(r.binary||r.dir||!/\.(md|txt)$/.test(path)){
    $("#firstHeading").textContent=path.split("/").pop();
    bc.innerHTML=`<pre>${esc(r.content)}</pre>`;
    RAW=r.dir?null:r.content;
  } else {
    RAW=r.content;
    const art=articleHtml(r.content, path);
    $("#firstHeading").innerHTML=esc(art.title);
    const fmm=art.fm.meta;
    const bits=[];
    if(fmm.status) bits.push(`<i>${esc(fmm.status)}</i>`);
    if(fmm.page_type) bits.push(esc(fmm.page_type));
    if(fmm.importance) bits.push("importance: "+esc(fmm.importance));
    $("#contentSub").innerHTML=bits.length?("("+bits.join(" · ")+")"):"";
    bc.innerHTML=art.html;
    wireBody(bc);
    $("#lastmod").textContent=fmm.date_modified
      ?`This page was last edited on ${fmm.date_modified}. Page size ${RAW.length.toLocaleString()} bytes.`
      :`Page size ${RAW.length.toLocaleString()} bytes.`;
    if(highlight){
      const rx=new RegExp(highlight.replace(/[.*+?^${}()|[\]\\]/g,"\\$&"),"gi");
      bc.querySelectorAll("p,li,td,h2,h3,blockquote").forEach(el=>{
        if(rx.test(el.textContent)) el.innerHTML=el.innerHTML.replace(rx,m=>`<mark>${m}</mark>`); });
    }
  }
  setTabs();
  window.scrollTo(0,0);
}

/* ============================ editor ============================ */
function openEditor(opts){
  opts=opts||{};
  if(RAW===null&&!CREATING) return;
  MODE="edit"; setTabs();
  $("#bodyContent").style.display="none";
  $("#editArea").style.display="block";
  $("#previewNote").style.display="none"; $("#previewOut").innerHTML="";
  $("#editMsg").textContent=""; $("#wpSummary").value="";
  const ta=$("#wpTextbox");
  ta.value=CREATING?CREATING.template:RAW;
  $("#firstHeading").textContent=(CREATING?"Creating ":"Editing ")+humanTitle(CUR);
  $("#siteSub").textContent=CUR;
  ta.focus();
  if(opts.line!==undefined){
    const lines=ta.value.split("\n");
    let pos=0; for(let i=0;i<Math.min(opts.line,lines.length);i++) pos+=lines[i].length+1;
    ta.setSelectionRange(pos,pos);
    const lh=ta.scrollHeight/lines.length;
    ta.scrollTop=Math.max(0,lh*opts.line-80);
  }
  window.scrollTo(0,0);
}
function openCreate(path){
  const today=new Date().toISOString().slice(0,10);
  const domain=path.split("/")[1]||"people";
  CUR=path; RAW=null;
  CREATING={template:
`---
domain: ${DOMAINS.includes(domain)?domain:"people"}
page_type: entity
status: stub
date_created: ${today}
date_modified: ${today}
sources: []
---

`};
  openEditor();
}
$("#ca-edit").onclick=()=>{ if(MODE!=="edit") openEditor(); };
$("#ca-view").onclick=()=>{ if(MODE!=="read"&&CUR) openPage(CUR); };
$("#wpCancel").onclick=()=>{ if(CREATING){CREATING=null; openPage("index.md");} else openPage(CUR); };
$("#wpPreview").onclick=()=>{
  const art=articleHtml($("#wpTextbox").value, CUR, {preview:true});
  $("#previewNote").style.display="block";
  const po=$("#previewOut");
  po.innerHTML=art.html; wireBody(po);
  window.scrollTo(0,0);
};
$("#wpSave").onclick=async()=>{
  $("#wpSave").disabled=true;
  const r=await api("/api/save",{method:"POST",body:JSON.stringify(
    {path:CUR, content:$("#wpTextbox").value, summary:$("#wpSummary").value,
     create:!!CREATING})});
  $("#wpSave").disabled=false;
  if(r.error){$("#editMsg").textContent="⚠ "+r.error; return;}
  CREATING=null;
  await refresh(); openPage(CUR); gitRefresh();
};
/* toolbar */
function tbWrap(before,after,placeholder){
  const ta=$("#wpTextbox");
  const s=ta.selectionStart, e=ta.selectionEnd;
  const sel=ta.value.slice(s,e)||placeholder;
  ta.value=ta.value.slice(0,s)+before+sel+after+ta.value.slice(e);
  ta.setSelectionRange(s+before.length, s+before.length+sel.length);
  ta.focus();
}
document.querySelectorAll("#editToolbar button").forEach(b=>b.onclick=ev=>{
  ev.preventDefault();
  const k=b.dataset.tb;
  if(k==="bold") tbWrap("**","**","bold text");
  else if(k==="italic") tbWrap("*","*","italic text");
  else if(k==="link") tbWrap("[[","]]","wiki/people/page-name");
  else if(k==="h2") tbWrap("\n## ","\n","Section heading");
  else if(k==="table") tbWrap("\n| Column | Column |\n|---|---|\n| ", " |  |\n","value");
  else if(k==="image"){ $("#imgMsg").textContent=""; $("#imgCaption").value="";
    $("#imgFile").value=""; $("#imageDlg").showModal(); }
});
/* image dialog */
$("#imgCancel").onclick=()=>$("#imageDlg").close();
$("#imgGo").onclick=async()=>{
  const f=$("#imgFile").files[0];
  if(!f){$("#imgMsg").textContent="choose an image file"; return;}
  $("#imgGo").disabled=true; $("#imgMsg").textContent="uploading…";
  try{
    const r=await(await fetch("/api/upload-image",{method:"POST",
      headers:{"X-Filename":encodeURIComponent(f.name)},body:f})).json();
    if(r.error){$("#imgMsg").textContent="⚠ "+r.error; return;}
    const cap_=$("#imgCaption").value.trim(), place=$("#imgPlace").value;
    let mdTxt;
    if(place==="inline") mdTxt=`![${cap_}](${r.path}) `;
    else mdTxt=`\n![${cap_}](${r.path})\n`;   // standalone line renders as a thumb
    tbWrap("", "", ""); // ensure focus
    const ta=$("#wpTextbox"), s=ta.selectionStart;
    ta.value=ta.value.slice(0,s)+mdTxt+ta.value.slice(s);
    ta.setSelectionRange(s+mdTxt.length,s+mdTxt.length);
    $("#imageDlg").close();
  } finally { $("#imgGo").disabled=false; }
};

/* ============================ history ============================ */
$("#ca-history").onclick=async()=>{
  if(!CUR||MODE==="history")return;
  MODE="history"; setTabs();
  $("#editArea").style.display="none";
  const bc=$("#bodyContent"); bc.style.display="block";
  $("#firstHeading").textContent=humanTitle(CUR)+": Revision history";
  $("#siteSub").textContent=CUR;
  $("#contentSub").innerHTML="";
  bc.innerHTML="<p>Loading history…</p>";
  const r=await api("/api/history?path="+encodeURIComponent(CUR));
  if(!r.entries||!r.entries.length){ bc.innerHTML="<p>No recorded revisions for this page (not yet committed).</p>"; return; }
  bc.innerHTML='<p>Commits touching this page, newest first (from git; renames followed).</p>'+
    '<ul id="pagehistory">'+r.entries.map(e=>
      `<li><span class="curprev">${esc(e.hash)}</span>`+
      `<span class="mw-changeslist-date">${esc(e.date)}</span>`+
      `<span class="hist-author">${esc(e.author)}</span>`+
      `<span class="comment">(${esc(e.subject)})</span></li>`).join("")+"</ul>";
};
$("#ca-talk").onclick=()=>{
  if(MODE==="special")return;
  MODE="read"; setTabs();
  $("#editArea").style.display="none";
  const bc=$("#bodyContent"); bc.style.display="block";
  $("#firstHeading").textContent="Talk: "+(CUR?humanTitle(CUR):"");
  $("#contentSub").innerHTML="";
  bc.innerHTML='<p>There is no discussion page in this wiki. Model-to-model coordination happens in '+
    '<a href="#" data-page="LLM_HANDOFF.md">LLM_HANDOFF.md</a>; operator instructions arrive via '+
    '<a href="#" data-page="queue.md">queue.md</a> and captures.</p>';
  wireBody(bc);
};

/* ============================ move (rename) ============================ */
$("#ca-move").onclick=()=>{
  $("#renameFrom").textContent=CUR;
  $("#renameTo").value=""; $("#renameMsg").textContent="";
  $("#renameDlg").showModal(); $("#renameTo").focus();
};
$("#renameCancel").onclick=()=>$("#renameDlg").close();
$("#renameGo").onclick=async()=>{
  const nn=$("#renameTo").value.trim();
  if(!nn){$("#renameMsg").textContent="enter a new name"; return;}
  const r=await api("/api/rename",{method:"POST",body:JSON.stringify({path:CUR,newName:nn})});
  if(r.error){$("#renameMsg").textContent="⚠ "+r.error; return;}
  $("#renameDlg").close();
  await refresh(); openPage(r.newPath); gitRefresh();
  setTimeout(()=>alert(`Moved. ${r.linksUpdated} page(s) had links updated.`),50);
};

/* ============================ special pages ============================ */
function specialShell(title, sub){
  MODE="special"; CUR=null; RAW=null; CREATING=null; setTabs();
  $("#editArea").style.display="none";
  const bc=$("#bodyContent"); bc.style.display="block";
  $("#firstHeading").textContent=title;
  $("#siteSub").textContent=sub||"Special page";
  $("#contentSub").innerHTML="";
  $("#lastmod").textContent="";
  window.scrollTo(0,0);
  return bc;
}
function showContents(){
  const bc=specialShell("Special:Contents","All pages by domain");
  const groups={};
  for(const f of TREE.wiki){
    const parts=f.path.split("/");
    const g=parts[1]+(parts.length>3?" / "+parts[2]:"");
    (groups[g]=groups[g]||[]).push(f);
  }
  let h="";
  for(const g of Object.keys(groups).sort()){
    const items=groups[g].sort((a,b)=>(a.name==="index.md"?-1:b.name==="index.md"?1:a.name<b.name?-1:1));
    h+=`<h2><span class="mw-headline">${esc(g)} <span style="font-size:70%;color:#72777d">(${items.length})</span></span></h2><ul>`;
    h+=items.map(f=>`<li><a href="#" data-page="${esc(f.path)}">${esc(humanTitle(f.path))}</a> `+
      `<span style="color:#72777d;font-size:.85em">${(f.size/1024).toFixed(1)} KB</span></li>`).join("");
    h+="</ul>";
  }
  bc.innerHTML=h; wireBody(bc);
}
async function showRecent(){
  const bc=specialShell("Special:RecentChanges","Latest commits in the repository");
  bc.innerHTML="<p>Loading…</p>";
  const r=await api("/api/recent");
  bc.innerHTML='<ul id="pagehistory">'+(r.entries||[]).map(e=>
    `<li><span class="curprev">${esc(e.hash)}</span>`+
    `<span class="mw-changeslist-date">${esc(e.date)}</span>`+
    `<span class="hist-author">${esc(e.author)}</span>`+
    `<span class="comment">(${esc(e.subject)})</span></li>`).join("")+"</ul>";
}
async function showSearch(q){
  const bc=specialShell("Search results",`Results for "${q}"`);
  bc.innerHTML="<p>Searching…</p>";
  const hits=await api("/api/search?q="+encodeURIComponent(q));
  if(!hits.length){ bc.innerHTML=`<p>There were no results matching the query.</p>`; return; }
  bc.innerHTML=hits.map(h=>
    `<div class="mw-search-result">`+
    `<div class="title"><a href="#" data-page="${esc(h.path)}" data-hl="${esc(q)}">${esc(humanTitle(h.path))}</a></div>`+
    h.matches.map(m=>`<div class="snippet">…${esc(m.text)}…</div>`).join("")+
    `<div class="meta">${esc(h.path)} — ${h.count} matching line(s)</div></div>`).join("");
  bc.querySelectorAll("a[data-page]").forEach(a=>{
    a.onclick=e=>{e.preventDefault(); openPage(a.dataset.page, a.dataset.hl);};
  });
}
async function showWhatLinks(){
  if(!CUR||!CUR.startsWith("wiki/")){alert("Open a wiki page first.");return;}
  const target=CUR.replace(/\.md$/,"");
  const base=target.split("/").pop();
  const cur=CUR;
  const bc=specialShell("Pages that link to "+humanTitle(cur), target);
  bc.innerHTML="<p>Searching…</p>";
  const hits=(await api("/api/search?q="+encodeURIComponent(base))).filter(h=>h.path!==cur);
  bc.innerHTML=hits.length?("<ul>"+hits.map(h=>
    `<li><a href="#" data-page="${esc(h.path)}">${esc(humanTitle(h.path))}</a> `+
    `<span style="color:#72777d;font-size:.85em">${esc(h.path)}</span></li>`).join("")+"</ul>")
    :"<p>No other page mentions this page's name.</p>";
  wireBody(bc);
}
function showTemplate(tplId, title, init){
  const bc=specialShell(title);
  bc.innerHTML="";
  bc.appendChild(document.getElementById(tplId).content.cloneNode(true));
  init();
}

/* ============================ sidebar nav ============================ */
$("#logoHome").onclick=()=>openPage("index.md");
$("#nav-main").onclick=()=>openPage("index.md");
$("#nav-contents").onclick=showContents;
$("#nav-recent").onclick=showRecent;
$("#nav-random").onclick=()=>{
  const pool=TREE.wiki.filter(f=>!f.path.endsWith("index.md")&&!f.path.includes("/contacts/"));
  openPage(pool[Math.floor(Math.random()*pool.length)].path);
};
$("#nav-whatlinks").onclick=showWhatLinks;
$("#nav-capture").onclick=()=>showTemplate("tpl-capture","Special:Capture",initCapture);
$("#nav-ingest").onclick=()=>showTemplate("tpl-ingest","Special:Ingest",initIngest);
$("#nav-export").onclick=()=>showTemplate("tpl-export","Special:Export",initExport);
$("#nav-intake").onclick=()=>showTemplate("tpl-intake","Special:Intake",initIntake);
$("#nav-newpage").onclick=()=>{
  $("#npMsg").textContent=""; $("#npTitle").value="";
  $("#newPageDlg").showModal(); $("#npTitle").focus();
};
$("#npCancel").onclick=()=>$("#newPageDlg").close();
$("#npGo").onclick=()=>{
  const t=$("#npTitle").value.trim();
  if(!t){$("#npMsg").textContent="enter a title"; return;}
  const slug=t.toLowerCase().replace(/[^a-z0-9]+/g,"-").replace(/^-|-$/g,"");
  if(!slug){$("#npMsg").textContent="title has no usable characters"; return;}
  const path=`wiki/${$("#npDomain").value}/${slug}.md`;
  if(PAGES.has(path)){$("#npMsg").textContent="page already exists — opening it"; setTimeout(()=>{$("#newPageDlg").close();openPage(path);},700); return;}
  $("#newPageDlg").close();
  openCreate(path);
};

/* ============================ search box ============================ */
const sIn=$("#searchInput"), sug=$("#suggestions");
let sugSel=0, sugItems=[];
function hideSug(){sug.style.display="none"; sugItems=[];}
sIn.addEventListener("input",()=>{
  const q=sIn.value.trim().toLowerCase();
  if(!q){hideSug();return;}
  sugItems=TREE.wiki.filter(f=>!f.path.endsWith("/index.md"))
    .map(f=>({path:f.path,t:humanTitle(f.path)}))
    .filter(x=>x.t.toLowerCase().includes(q)||x.path.toLowerCase().includes(q))
    .sort((a,b)=>{
      const ap=a.t.toLowerCase().startsWith(q)?0:1, bp=b.t.toLowerCase().startsWith(q)?0:1;
      return ap-bp||a.t.length-b.t.length;})
    .slice(0,10);
  if(!sugItems.length){hideSug();return;}
  sugSel=0;
  sug.innerHTML=sugItems.map((x,i)=>
    `<a class="${i===0?'sel':''}" data-i="${i}"><b>${esc(x.t)}</b><span class="d">${esc(x.path.replace(/^wiki\//,"").replace(/\.md$/,""))}</span></a>`).join("");
  sug.style.display="block";
  sug.querySelectorAll("a").forEach(a=>{
    a.onmousedown=e=>{e.preventDefault(); openPage(sugItems[+a.dataset.i].path); hideSug(); sIn.value="";};
  });
});
sIn.addEventListener("keydown",e=>{
  if(sug.style.display!=="block")return;
  if(e.key==="ArrowDown"){e.preventDefault();sugSel=Math.min(sugSel+1,sugItems.length-1);}
  else if(e.key==="ArrowUp"){e.preventDefault();sugSel=Math.max(sugSel-1,0);}
  else if(e.key==="Escape"){hideSug();return;}
  else return;
  sug.querySelectorAll("a").forEach((a,i)=>a.classList.toggle("sel",i===sugSel));
});
sIn.addEventListener("blur",()=>setTimeout(hideSug,150));
$("#searchForm").onsubmit=e=>{
  e.preventDefault();
  const q=sIn.value.trim(); if(!q)return;
  if(sug.style.display==="block"&&sugItems[sugSel]){ openPage(sugItems[sugSel].path); }
  else showSearch(q);
  hideSug(); sIn.value="";
};

/* ============================ tree / git ============================ */
async function refresh(){
  TREE=await api("/api/tree");
  PAGES=new Set(TREE.wiki.map(f=>f.path));
  $("#inboxN").textContent=TREE.inbox.length?`(${TREE.inbox.length})`:"";
  const dl=$("#domainList"); dl.innerHTML="";
  for(const d of DOMAINS){
    const n=TREE.wiki.filter(f=>f.path.startsWith("wiki/"+d+"/")).length;
    if(!n)continue;
    const li=document.createElement("li");
    li.innerHTML=`<a>${cap(d)}</a> <span class="cnt">${n}</span>`;
    li.querySelector("a").onclick=()=>openPage(`wiki/${d}/index.md`);
    dl.appendChild(li);
  }
  const ml=$("#metaList"); ml.innerHTML="";
  for(const f of TREE.meta){
    if(f.path==="index.md")continue;
    const li=document.createElement("li");
    li.innerHTML=`<a>${esc(f.name)}</a>`;
    li.querySelector("a").onclick=()=>openPage(f.path);
    ml.appendChild(li);
  }
}
async function gitRefresh(){
  const g=await api("/api/git/status");
  const bits=[`<b>${esc(g.branch||"?")}</b>`];
  if(g.dirty)bits.push(`${g.dirty} uncommitted`);
  if(g.ahead)bits.push(`↑${g.ahead}`);
  if(g.behind)bits.push(`↓${g.behind}`);
  if(!g.dirty&&!g.ahead&&!g.behind)bits.push("in sync");
  $("#gitPill").innerHTML=bits.join(" · ");
  $("#siteNotice").style.display=(g.public===true)?"block":"none";
}
$("#syncLink").onclick=async()=>{
  $("#syncLink").textContent="Syncing…";
  const g=await api("/api/git/status");
  if(g.public===true && !confirm("The GitHub repo is PUBLIC. Push anyway?")){
    $("#syncLink").textContent="Sync"; return; }
  const msg=g.dirty?prompt("Commit message for local changes:","edit: app sync"):"";
  if(g.dirty&&msg===null){ $("#syncLink").textContent="Sync"; return; }
  const r=await api("/api/git/sync",{method:"POST",body:JSON.stringify({message:msg})});
  alert(r.message);
  $("#syncLink").textContent="Sync";
  gitRefresh();
};

/* ============================ special: capture ============================ */
let TGT=new Set(), acSel=0, acMatches=[], acStart=-1;
/* ============================ Special:Intake ============================
   A form over bin/intake. Every mutation is one POST to /api/intake/<action>,
   which calls the same functions the CLI calls and hands back the whole
   recomputed state — so the page can never hold a number the ledger disagrees
   with, and there is no second copy of the arithmetic to drift. */
let IST=null, IMORE={}, ICLOSE={}, IADJ={};

function iQtyUnits(sel){
  let h="";
  for(const [fam,units] of Object.entries(IST.quantity_units))
    h+=`<optgroup label="${esc(fam)}">`+units.map(u=>
      `<option${u===sel?" selected":""}>${esc(u)}</option>`).join("")+"</optgroup>";
  return h;
}
function iSubOptions(){
  const byCat={};
  for(const s of IST.substances)(byCat[s.category]=byCat[s.category]||[]).push(s);
  let h='<option value="">— choose —</option>';
  for(const c of IST.categories.filter(c=>byCat[c]))
    h+=`<optgroup label="${esc(c)}">`+byCat[c].map(s=>
      `<option value="${esc(s.id)}" data-unit="${esc(s.default_unit)}">${esc(s.name)}</option>`
      ).join("")+"</optgroup>";
  return h+'<option value="__new__">+ add a substance…</option>';
}
async function iPost(action, body, msg){
  if(msg) msg.textContent="";
  const r=await api("/api/intake/"+action,{method:"POST",body:JSON.stringify(body)});
  if(r.error){ if(msg) msg.textContent="⚠ "+r.error; else alert(r.error); return null; }
  IST=r.state; iRender(); return r.result;
}
async function initIntake(){
  IST=await api("/api/intake");
  iRender();
  $("#iHelp").onclick=e=>{e.preventDefault();
    const t=$("#iHelpText"); t.style.display=t.style.display==="none"?"":"none";};
}

function iUnitCard(u){
  const d=u.display, open=u.status==="active";
  const mid="mt-"+u.id;
  let h=`<div class="iunit${open?"":" closed"}" data-u="${esc(u.id)}">`+
    `<h3>${esc(u.substance)}<span class="ipill">#${u.ordinal}</span>`+
    (open?"":`<span class="ipill">${esc(u.disposition||"closed")}</span>`)+`</h3>`+
    `<div class="imeta">${esc(d.initial)} received ${esc(d.received)}`+
    (d.closed?` · closed ${esc(d.closed)}`:"")+` · ${esc(d.duration)} · `+
    `${u.analysis.events.total} event(s)`+
    (u.source_context?` · ${esc(u.source_context)}`:"")+`</div>`;
  if(open) h+=`<div class="ibig">${esc(d.remaining_is_estimate?"~":"")}${esc(d.remaining)}`+
    ` <small>left of ${esc(d.initial)}${d.mean?" · mean "+esc(d.mean):""}</small></div>`;
  h+=`<div class="icov">${esc(d.coverage)}</div>`;
  if(d.overdrawn) h+=`<div class="msg">⚠ more is logged against this unit than it was opened with.</div>`;
  if(open){
    // ONE TAP. The manual row below is still the honest path for anything
    // weighed — these are for the case that actually recurs, where the
    // alternative to a tap is not a careful entry but no entry at all.
    const pres=((IST.substances||[]).find(x=>x.id===u.substance_id)||{}).presets||[];
    if(pres.length) h+=`<div style="font-size:8.5px;letter-spacing:.26em;color:#54595d;margin:.9em 0 .35em">ONE TAP</div>`+
      `<div class="iquick">`+pres.map(pre=>
        `<button class="mw-btn" data-role="pre" data-pre="${esc(pre.id)}" title="${esc(pre.note||"")}">`+
        `${esc(pre.label||pre.id)} <span style="opacity:.65">${esc(pre.quantity)} ${esc(pre.unit)}</span></button>`
      ).join("")+`</div>`+
      `<div style="font-size:.78em;color:#72777d;line-height:1.7;margin:.35em 0 .2em">`+
      `Every preset logs as an <b>estimate</b>, never a measurement — nobody weighed these, `+
      `and the ledger will not let a stand-in pass for a scale.</div>`;
    h+=`<div class="iquick">`+
      `<input type="text" class="q" placeholder="0.18" data-role="q">`+
      `<select data-role="u">${iQtyUnits(u.quantity_unit)}</select>`+
      `<button class="mw-btn progressive" data-role="log">Log intake</button>`+
      `<a href="#" data-role="tog">${IMORE[u.id]?"less":"more"}…</a></div>`+
      `<div class="imore" style="display:${IMORE[u.id]?"":"none"}" data-role="more">`+
      ["measured","estimated","unquantified"].map((t,i)=>
        `<label><input type="radio" name="${mid}" value="${t}"${i?"":" checked"}> ${t}</label>`).join("")+
      `<br><label>descriptor <input type="text" class="desc" data-role="desc" placeholder="one line"></label>`+
      `<label>at <input type="text" data-role="at" placeholder="now" style="width:9em"></label>`+
      `<label>note <input type="text" data-role="note" style="width:12em"></label>`+
      `<div style="margin-top:.4em">An <i>unquantified</i> event needs no quantity — the descriptor
       is enough, and the event still counts toward everything except the grams.</div></div>`;
  }
  if(d.events.length) h+=`<pre class="ievents">`+esc(d.events.join("\n"))+`</pre>`;
  h+=`<div style="margin-top:.5em; font-size:.85em">`+
    `<a href="#" data-role="report">unit report</a>`+
    (open?` · <a href="#" data-role="adjust">record a spill or transfer</a>`+
          ` · <a href="#" data-role="close">close this unit</a>`
        :` · <a href="#" data-role="reopen">reopen</a>`)+`</div>`;
  if(open&&IADJ[u.id]) h+=iAdjustPanel(u);
  if(open&&ICLOSE[u.id]) h+=iClosePanel(u);
  return h+`<div class="msg" data-role="msg"></div></div>`;
}

function iAdjustPanel(u){
  return `<div class="step" data-role="adjpanel"><h3>Quantity leaving without being consumed</h3>`+
    `<div class="hint">A spilled gram is not a dose. Recorded apart from intake so it never
     shows up in a use pattern.</div><div class="iquick">`+
    `<input type="text" data-role="aq" placeholder="0.3"><select data-role="au">${iQtyUnits(u.quantity_unit)}</select>`+
    `<select data-role="ak">`+IST.adjustment_kinds.map(k=>`<option>${esc(k)}</option>`).join("")+`</select>`+
    `<input type="text" data-role="an" placeholder="note" style="width:14em">`+
    `<button class="mw-btn progressive" data-role="asave">Record</button>`+
    `<a href="#" data-role="acancel">cancel</a></div></div>`;
}

function iClosePanel(u){
  const r=u.reconciliation, bu=u.quantity_unit;
  let h=`<div class="step" data-role="closepanel"><h3>How did this unit end?</h3>`+
    `<select data-role="cd">`+IST.dispositions.map(x=>`<option>${esc(x)}</option>`).join("")+`</select>`;
  if(r&&r.needs_answer){
    const gap=Math.abs(r.unaccounted).toFixed(3).replace(/0+$/,"").replace(/\.$/,"");
    h+=`<div class="hint" style="margin-top:.7em">`+
      `<b>Initial</b> ${r.initial} ${esc(bu)} · <b>quantified intake</b> `+
      `${r.quantified_intake.toFixed(3).replace(/0+$/,"").replace(/\.$/,"")} ${esc(bu)}`+
      (r.adjusted?` · <b>adjustments</b> ${r.adjusted} ${esc(bu)}`:"")+
      ` · <b>${r.overdrawn?"over-logged":"unaccounted"}</b> ${gap} ${esc(bu)}`+
      (r.unquantified_events?` · ${r.unquantified_events} event(s) logged without a quantity`:"")+
      `<br>The ledger will not guess what happened to it. Say what did:</div>`+
      `<select data-role="cr">`+IST.resolutions.map(x=>
        `<option value="${esc(x)}">${esc(x.replace("_"," "))}</option>`).join("")+`</select>`+
      `<div class="hint" style="margin-top:.3em"><i>final intake</i> records the remainder as one
       estimated, low-confidence event — it is counted, and every report names it as a remainder
       rather than a watched dose.</div>`;
  } else {
    h+=`<div class="hint" style="margin-top:.7em">The ledger balances — nothing unaccounted for.</div>`;
  }
  return h+`<div class="iquick" style="margin-top:.6em">`+
    `<input type="text" data-role="cat" placeholder="closed at (blank = now)" style="width:14em">`+
    `<input type="text" data-role="cn" placeholder="note" style="width:14em">`+
    `<button class="mw-btn progressive" data-role="csave">Close unit</button>`+
    `<a href="#" data-role="ccancel">cancel</a></div></div>`;
}

function iRender(){
  if(!IST||!$("#iactive")) return;
  const warn=$("#iwarn");
  warn.innerHTML=(IST.errors||[]).map(e=>`<div class="iwarn"><b>ERROR</b> ${esc(e)}</div>`).join("")+
    (IST.warnings||[]).map(w=>`<div class="iwarn">⚠ ${esc(w)}</div>`).join("");
  const active=IST.units.filter(u=>u.status==="active");
  const closed=IST.units.filter(u=>u.status!=="active").reverse();
  $("#iactive").innerHTML=active.length?active.map(iUnitCard).join("")
    :`<p style="color:#54595d">No open units. Create one on the right — the unit comes first,
      and intake events are logged against it.</p>`;
  $("#iclosedN").textContent=closed.length?`(${closed.length}) · ${IST.today} event(s) logged today`
    :`· ${IST.today} event(s) logged today`;
  $("#iclosed").innerHTML=closed.length?closed.map(iUnitCard).join(""):"";
  const n=$("#intakeN"); if(n) n.textContent=active.length?`(${active.length})`:"";
  iWireUnits(); iWireNew();
}

function iWireUnits(){
  document.querySelectorAll(".iunit").forEach(card=>{
    const id=card.dataset.u, g=r=>card.querySelector(`[data-role="${r}"]`), msg=g("msg");
    const val=r=>{const el=g(r); return el?el.value.trim():"";};
    const tog=g("tog");
    if(tog) tog.onclick=e=>{e.preventDefault(); IMORE[id]=!IMORE[id]; iRender();};
    const doLog=async()=>{
      const mt=card.querySelector(`input[name="mt-${id}"]:checked`);
      await iPost("log",{unit:id, quantity:val("q"), quantity_unit:val("u"),
        measurement_type:mt?mt.value:"measured", descriptor:val("desc"),
        at:val("at"), note:val("note")}, msg);
    };
    card.querySelectorAll('[data-role="pre"]').forEach(b=>{
      b.onclick=async()=>{
        b.disabled=true;
        await iPost("log",{unit:id, preset:b.dataset.pre}, msg);
        iRender();
      };
    });
    if(g("log")) g("log").onclick=doLog;
    if(g("q")) g("q").onkeydown=e=>{if(e.key==="Enter"){e.preventDefault(); doLog();}};
    if(g("desc")) g("desc").onkeydown=e=>{if(e.key==="Enter"){e.preventDefault(); doLog();}};
    if(g("report")) g("report").onclick=async e=>{e.preventDefault(); await iShowReport(id);};
    if(g("adjust")) g("adjust").onclick=e=>{e.preventDefault(); IADJ[id]=!IADJ[id]; iRender();};
    if(g("acancel")) g("acancel").onclick=e=>{e.preventDefault(); IADJ[id]=false; iRender();};
    if(g("asave")) g("asave").onclick=async()=>{
      const ok=await iPost("adjust",{unit:id, quantity:val("aq"), quantity_unit:val("au"),
        kind:val("ak"), note:val("an")}, msg);
      if(ok){ IADJ[id]=false; iRender(); }};
    if(g("close")) g("close").onclick=e=>{e.preventDefault(); ICLOSE[id]=!ICLOSE[id]; iRender();};
    if(g("ccancel")) g("ccancel").onclick=e=>{e.preventDefault(); ICLOSE[id]=false; iRender();};
    if(g("csave")) g("csave").onclick=async()=>{
      const res=await iPost("close",{unit:id, disposition:val("cd"), resolution:val("cr"),
        at:val("cat"), note:val("cn")}, msg);
      if(res){ ICLOSE[id]=false; iRender();
        $("#ireport").style.display="";
        $("#ireport").innerHTML=`<div class="note">Archived to <code>${esc(res.capture)}</code>
          — written once, never regenerated.</div><pre class="ireport">${esc(res.report)}</pre>`;
        $("#ireport").scrollIntoView({behavior:"smooth"}); }};
    if(g("reopen")) g("reopen").onclick=async e=>{e.preventDefault();
      const why=prompt("Reopening a closed unit needs a reason:"); if(!why) return;
      await iPost("reopen",{unit:id, reason:why}, msg);};
  });
}

async function iShowReport(id){
  const r=await api("/api/intake/report?unit="+encodeURIComponent(id));
  const box=$("#ireport"); box.style.display="";
  box.innerHTML=r.error?`<div class="msg">⚠ ${esc(r.error)}</div>`
    :`<pre class="ireport">${esc(r.report)}\n\nEVENTS\n${esc(r.events.join("\n"))}</pre>`;
  box.scrollIntoView({behavior:"smooth"});
}

function iWireNew(){
  const sub=$("#nuSub"); if(!sub) return;
  const keep=sub.value;
  sub.innerHTML=iSubOptions(); if(keep) sub.value=keep;
  $("#nuUnit").innerHTML=iQtyUnits($("#nuUnit").value||"g");
  $("#nuDefUnit").innerHTML=iQtyUnits($("#nuDefUnit").value||"g");
  $("#nuCat").innerHTML=IST.categories.map(c=>`<option>${esc(c)}</option>`).join("");
  sub.onchange=()=>{
    const isNew=sub.value==="__new__";
    $("#nuNew").style.display=isNew?"":"none";
    const opt=sub.selectedOptions[0];
    if(!isNew&&opt&&opt.dataset.unit) $("#nuUnit").value=opt.dataset.unit;
  };
  $("#nuAdd").onclick=async()=>{
    const r=await iPost("substance",{name:$("#nuName").value,category:$("#nuCat").value,
      quantity_unit:$("#nuDefUnit").value}, $("#nuMsg"));
    if(r){ $("#nuName").value=""; $("#nuNew").style.display="none";
      $("#nuSub").value=r.substance.id; $("#nuUnit").value=r.substance.default_unit; }};
  $("#nuGo").onclick=async()=>{
    const r=await iPost("unit",{substance:$("#nuSub").value, quantity:$("#nuQty").value,
      quantity_unit:$("#nuUnit").value, at:$("#nuAt").value, source:$("#nuSource").value,
      note:$("#nuNote").value}, $("#nuMsg"));
    if(r){ $("#nuQty").value=$("#nuAt").value=$("#nuSource").value=$("#nuNote").value=""; }};
  $("#nuQty").onkeydown=e=>{if(e.key==="Enter"){e.preventDefault(); $("#nuGo").click();}};
}

function initCapture(){
  TGT=new Set(); acSel=0; acMatches=[]; acStart=-1;
  const body=$("#cBody"), ac=$("#ac");
  const pageList=()=>TREE?TREE.wiki.map(f=>f.path.replace(/\.md$/,"")):[];
  const renderTargets=()=>{
    const el=$("#targets"); el.innerHTML="";
    for(const t of TGT){
      const c=document.createElement("span"); c.className="tchip";
      c.innerHTML=`<b>@${esc(t.split("/").pop().replace(/\.md$/,""))}</b> <span style="color:#72777d">${esc(t)}</span><button>✕</button>`;
      c.querySelector("button").onclick=()=>{TGT.delete(t);renderTargets()};
      el.appendChild(c); } };
  const hideAc=()=>{ ac.style.display="none"; acMatches=[]; acStart=-1; };
  const paintAc=()=>ac.querySelectorAll("div[data-i]").forEach((d,i)=>d.classList.toggle("sel",i===acSel));
  const pickAc=i=>{
    const p=acMatches[i]; if(!p)return;
    const short="@"+p.split("/").pop();
    body.value=body.value.slice(0,acStart)+short+body.value.slice(body.selectionStart);
    const pos=acStart+short.length;
    body.setSelectionRange(pos,pos); body.focus();
    TGT.add(p+".md"); renderTargets(); hideAc(); };
  const showAc=q=>{
    const ql=q.toLowerCase();
    acMatches=pageList().filter(p=>p.toLowerCase().includes(ql))
      .sort((a,b)=>{
        const an=a.split("/").pop().toLowerCase().startsWith(ql)?0:1;
        const bn=b.split("/").pop().toLowerCase().startsWith(ql)?0:1;
        return an-bn||a.length-b.length; }).slice(0,8);
    if(!acMatches.length){ hideAc(); return; }
    acSel=0;
    ac.innerHTML=acMatches.map((p,i)=>
      `<div class="${i===0?"sel":""}" data-i="${i}"><b>${esc(p.split("/").pop())}</b><span class="d">${esc(p)}</span></div>`).join("");
    ac.style.display="block";
    ac.style.top=Math.min(body.offsetHeight,160)+"px";
    ac.querySelectorAll("div[data-i]").forEach(d=>{
      d.onmousedown=e=>{e.preventDefault();pickAc(+d.dataset.i)};
      d.onmouseover=()=>{acSel=+d.dataset.i;paintAc()}; }); };
  body.addEventListener("input",()=>{
    const caret=body.selectionStart, text=body.value;
    const at=text.lastIndexOf("@",caret-1);
    if(at<0||(at>0&&/[\w/]/.test(text[at-1]))){ hideAc(); return; }
    const q=text.slice(at+1,caret);
    if(/[\s@]/.test(q)||q.length>60){ hideAc(); return; }
    acStart=at; showAc(q); });
  body.addEventListener("keydown",e=>{
    if(ac.style.display!=="block")return;
    if(e.key==="ArrowDown"){e.preventDefault();acSel=Math.min(acSel+1,acMatches.length-1);paintAc();}
    else if(e.key==="ArrowUp"){e.preventDefault();acSel=Math.max(acSel-1,0);paintAc();}
    else if(e.key==="Enter"||e.key==="Tab"){e.preventDefault();pickAc(acSel);}
    else if(e.key==="Escape"){hideAc();} });
  body.addEventListener("blur",()=>setTimeout(hideAc,150));
  $("#cSave").onclick=async()=>{
    const r=await api("/api/capture",{method:"POST",body:JSON.stringify(
      {title:$("#cTitle").value, body:$("#cBody").value, tags:$("#cTags").value, targets:[...TGT]})});
    $("#cMsg").textContent=r.error?("⚠ "+r.error):`✓ saved ${r.saved} (${r.words} words, ${r.kind})`;
    if(!r.error){ $("#cTitle").value=$("#cBody").value=$("#cTags").value=""; TGT.clear(); renderTargets(); refresh(); } };
  const drop=$("#drop"), pick=$("#filePick");
  const upload=async files=>{
    for(const f of files){
      $("#uMsg").textContent=`uploading ${f.name}…`;
      const r=await(await fetch("/api/upload",{method:"POST",
        headers:{"X-Filename":encodeURIComponent(f.name)},body:f})).json();
      $("#uMsg").textContent=r.error?("⚠ "+r.error):`✓ ${r.saved}`; }
    refresh(); };
  drop.onclick=()=>pick.click();
  drop.ondragover=e=>{e.preventDefault();drop.classList.add("over")};
  drop.ondragleave=()=>drop.classList.remove("over");
  drop.ondrop=e=>{e.preventDefault();drop.classList.remove("over");upload(e.dataTransfer.files)};
  pick.onchange=()=>upload(pick.files);
}

/* ============================ special: ingest ============================ */
let SEL_INBOX=null;
function initIngest(){
  SEL_INBOX=null;
  const renderInbox=()=>{
    const el=$("#inboxList"); if(!el)return;
    el.innerHTML="";
    if(!TREE.inbox.length){ el.innerHTML="<p style='color:#72777d'>Inbox is empty.</p>"; $("#packBtn").disabled=true; return; }
    for(const f of TREE.inbox){
      const d=document.createElement("div"); d.className="inb"+(f.path===SEL_INBOX?" sel":"");
      d.innerHTML=`<span class="nm">${esc(f.name)}</span><span class="sz">${f.size.toLocaleString()} B</span><button title="delete">✕</button>`;
      d.onclick=e=>{
        if(e.target.tagName==="BUTTON")return;
        SEL_INBOX=f.path; renderInbox(); $("#packBtn").disabled=false;
        $("#packMsg").textContent=""; $("#packOut").style.display="none"; $("#copyBtn").style.display="none"; };
      d.querySelector("button").onclick=async()=>{
        if(!confirm(`Delete ${f.name}? This cannot be undone.`))return;
        await api("/api/delete-inbox",{method:"POST",body:JSON.stringify({path:f.path})});
        if(SEL_INBOX===f.path)SEL_INBOX=null;
        await refresh(); renderInbox(); };
      el.appendChild(d); }
    $("#packBtn").disabled=!SEL_INBOX; };
  renderInbox();
  $("#packBtn").onclick=async()=>{
    $("#packBtn").disabled=true; $("#packMsg").textContent="packing…";
    const r=await api("/api/ingest/pack",{method:"POST",body:JSON.stringify({item:SEL_INBOX.replace(/^inbox\//,"")})});
    $("#packBtn").disabled=false;
    $("#packMsg").textContent=r.ok?r.message.split("\n").slice(0,2).join(" · "):("⚠ "+r.message);
    if(r.ok){ $("#packOut").value=r.prompt; $("#packOut").style.display="block";
      $("#copyBtn").style.display="inline-block"; } };
  $("#copyBtn").onclick=async()=>{
    await navigator.clipboard.writeText($("#packOut").value);
    $("#copyBtn").textContent="✓ Copied"; setTimeout(()=>{const b=$("#copyBtn"); if(b)b.textContent="Copy prompt to clipboard";},1500); };
  $("#applyBtn").onclick=async()=>{
    $("#applyBtn").disabled=true; $("#applyMsg").textContent="applying…";
    const r=await api("/api/ingest/apply",{method:"POST",body:JSON.stringify(
      {response:$("#applyIn").value, commit:$("#applyCommit").checked})});
    $("#applyBtn").disabled=false;
    $("#applyMsg").textContent=(r.ok?"✓\n":"⚠\n")+(r.message||r.error||"");
    if(r.ok){ $("#applyIn").value=""; SEL_INBOX=null; await refresh(); renderInbox(); gitRefresh(); } };
}

/* ============================ special: export ============================ */
function initExport(){
  $("#eGo").onclick=async()=>{
    $("#eGo").disabled=true; $("#eMsg").textContent="exporting…";
    const r=await api("/api/export",{method:"POST",body:JSON.stringify(
      {domain:$("#eDomain").value, raw:$("#eRaw").checked, inbox:$("#eInbox").checked})});
    $("#eGo").disabled=false;
    $("#eMsg").innerHTML=esc(r.message)+(r.file?
      `<br><a href="/api/download?path=${encodeURIComponent(r.file)}">⬇ download</a>`:""); };
}

/* ============================ boot ============================ */
window.addEventListener("hashchange",()=>{
  const p=decodeURIComponent(location.hash.slice(1));
  if(p&&p!==CUR&&MODE!=="edit") openPage(p);
});
refresh().then(()=>openPage(decodeURIComponent(location.hash.slice(1))||"index.md"));
gitRefresh(); setInterval(gitRefresh, 120000);
</script>
</body>
</html>"""


def main():
    server = ThreadingHTTPServer(("127.0.0.1", PORT), Handler)
    url = f"http://127.0.0.1:{PORT}"
    print(f"Personal Wiki running at {url}  (Ctrl-C to stop)")
    if not os.environ.get("WIKI_APP_EXTERNAL_OPEN"):
        threading.Timer(0.6, lambda: webbrowser.open(url)).start()
    try:
        server.serve_forever()
    except KeyboardInterrupt:
        print("\nstopped")


if __name__ == "__main__":
    main()
