# sage/ — questions put to the wiki from outside it

Every other operation in this repository starts with Dan: a source he captured, a gap he answered, a page he asked for. This one starts with somebody else. The portal ([`caakehorn/home`](https://github.com/caakehorn/home), `/sage`) has a question box; anyone through the door can ask something about Dan — his behaviour, his history, what the record predicts he will do — and the question lands here as a file.

**Nothing answers it automatically.** There is no model behind the box and no workflow that calls one. The question is parked, `bin/wiki-work` lists it at priority 1, and the next session working in this repository answers it properly: retrieval across `wiki/`, `bin/mine-messages` over the raw record for dated verbatim quotes, and every claim cited. That latency is the design. An answer worth putting under someone's question is one that read the corpus, and the corpus is 486 pages and 134,348 messages.

**The latency of *****answering***** is the design; the latency of *****publishing***** is not.** An answer merged here goes live on the portal's schedule — five minutes, and up to fifteen when GitHub is busy. Nothing needs nudging and nothing needs checking; just do not assume it is live the second it merges.

It was an hour until 2026-08-31. `.github/workflows/notify-portal.yml` was built to remove that wait by dispatching the moment an answer merged, because the only other nudge was the portal's own browser code, which runs when a page is edited or a question asked *from the site* — and an answer merged through a pull request has no browser behind it. On 2026-08-21 the hour put a retracted version of an answer in front of the person who asked, for forty minutes after it had been corrected. That workflow needed a cross-repository token, the token went missing on 2026-08-28 without saying so, and the schedule was turned up instead; the workflow is dormant and explains how to bring it back.

The person waiting cannot see the difference between "not answered yet" and "answered but not synced", which is the whole reason this obligation sits at priority 1 — and why five minutes is worth having over an hour even though neither is instant.

## Why these files are not in `raw/`

`raw/` is immutable. These files are not: a question arrives `pending` and becomes `answered`, and the answer is written into the same file so that what was asked and what was said back can never be separated.

The immutable artifact is produced at answer time — `raw/self/sage/<id>.md`, a capture holding the question, the answer and the sources it rested on, filed the way any other T0 material is filed. `sage/` is the working surface; `raw/` is the record; `wiki/` is what the answer eventually becomes.

## The file

One file per question, `sage/questions/<id>.md`, where the id is `<YYYY-MM-DD>_<HHMMSS>_<slug>` — sortable, unique per second, and readable.

---

id: 2026-08-21_143022_can-he-be-monogamous

asked: 2026-08-21T14:30:22Z

asker: Ally

status: pending

answered:

capture:

cites: []

---

## Question

Verbatim, as it was typed. Never edited for tone, spelling or fairness.

## Answer

Empty until a pass writes it.

| **Field** | **Meaning** |
| --- | --- |
| `id` | matches the filename stem |
| `asked` | ISO 8601 UTC, set by the portal |
| `asker` | optional; the box allows a blank, and blank reads as anonymous |
| `status` | `pending` · `answered` · `declined` |
| `answered` | date the answer landed |
| `capture` | the `raw/self/sage/` path the answer was filed to |
| `cites` | every `wiki/` and `raw/` path the answer rests on |

`declined` is a real outcome and it needs a reason in the Answer section. A question that is abusive, is about someone other than Dan, or cannot be answered from the corpus gets declined in the open rather than deleted — the portal renders it, so a question nobody wants to answer is visible as one.

## Answering

The protocol is CLAUDE.md's **ANSWER** section, and the short form is: cite everything, quote the record directly, and say where it cuts against the flattering reading. The answer is worth exactly as much as its proofs.

Sealed pages (`wiki.locks.json` in the portal repo) are out of bounds — they ship as ciphertext precisely so their contents are not readable from the site, and an answer that quotes one would publish through the back door what the seal exists to keep shut.
