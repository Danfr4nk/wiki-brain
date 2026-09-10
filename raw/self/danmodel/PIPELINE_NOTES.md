# DANMODEL pipeline — architecture notes

Filed 2026-07-20. The five source scripts live in Dan's Google Drive (`~~DOCS/DANMODEL`, folder id `1JxOcs0QuEFhZXjbnvX5G_lLb79j33gs8`) and were read in full via the Drive connector. Attempts to transcribe them byte-for-byte into this repo produced a corrupted copy (a bad byte introduced during manual reconstruction of the base64 payload), so this file is a faithful architecture/logic transcription instead — accurate to the read, not a verbatim copy. `reaction_pairs_heldout.jsonl` (this same directory) IS a verbatim, mechanically-decoded copy (4,570 rows, verified against the extraction_summary.txt count) and can be treated as primary data. Retrieve the original `.py` files from Drive directly if byte-exact source is ever needed; file IDs below.

## reaction_extractor.py (Drive id `12oMAqWmpC9Pxjvr2SC6TVwwT26SBQAdD`)

Turns a message-corpus CSV (`timestamp,thread_target,sender,direction,text`) into `(stimulus -> Dan's actual response)` pairs. Pure stdlib.

- Restricts to 1:1 threads only (`thread_target` starts with `+` or is an email not starting with "chat") — explicitly to avoid the "v1 defect" where group-chat exports echo Dan's own sent messages back tagged "Received" from a third party, corrupting the stimulus/response pairing.

- Uses `direction` (not `sender`) as ground truth for authorship — the script's own comment states `sender` is unreliable in many threads ("carries the target number regardless of author"), the same direction-field caveat documented independently elsewhere in this wiki (see wiki/people/*.md "direction-field bug" notes).

- A small hardcoded high-confidence contact map: `+17244346811` = Annie (early), `+12124702449` = Annie (NYC), `+17249987341` / `phloxenheim@ gmail.com` = Tom, `+17243228715` = Suz (mom), `+19165013615` = Jerad, `+17243223678` = Johnny (dealer), `+17243667777` = Rick (dad). Everything else is left "unmapped" rather than guessed.

- Collapses consecutive same-author messages into "turns," then emits a pair for every (non-Dan turn) -> (Dan turn) transition — i.e., every time someone says something and Dan then replies, across however many individual texts each side sent.

- Tags each pair with a domain via a transparent keyword-count heuristic (relational / music / political / technical / financial / supply / logistical / other-fallback — the same keyword lists reused in reaction_model.py), latency in minutes, a `long_gap` flag (>1440 min / 24h, kept not dropped), and burst size (message count on each side).

- Deterministic 12% held-out split via `hash(pair_id) % 100 < 12` — so the split is reproducible without storing indices.

- Output: `reaction_pairs_train.jsonl`, `reaction_pairs_heldout.jsonl`, `extraction_summary.txt` (numbers in this same directory, verified).

## reaction_model.py (Drive id `1IyIX4N4kH0BveLWa_MOqjxAwLv22lF0p`)

Baseline model: pure Jaccard word-overlap retrieval. Given a new stimulus, finds the closest historical stimulus (same domain bucket first, word-set Jaccard similarity) and returns the REAL historical response verbatim — no generation, just replay. CLI: default demo (5 held-out samples), `--predict "text"`, `--eval N` (reports avg similarity + exact-match rate, explicitly noted as expected-to-be-low since "real responses have natural variation").

## retriever.py (Drive id `1tshlR_3DfajWKH9dgREXyTQrMg7Jhyum`)

Upgrade over the Jaccard baseline: hand-rolled TF-IDF (stdlib + numpy, 15,000-word vocab cap, min document frequency 2) with metadata boosts — +0.35 if a candidate's domain matches the query, +0.25 if contact matches, +0.12/0.6x/0.25x for era proximity (same year / within 2 / within 4). Used as the context-retrieval layer for the RAG simulator below, always restricted to the train split.

## rag_simulator.py (Drive id `1W-j2PwwxPhthdnz8k_KjqUp1n86cX2-B`)

The actual voice-cloning generator. Retrieves top-k (default 8) exemplar pairs via the TF-IDF retriever, assembles a prompt with a hardcoded `CATO_COMPACT` persona block, and calls OpenRouter (default model `meta-llama/llama-3.2-3b-instruct:free`) with the API key read from `ANTHROPIC_API_KEY`/`OPENROUTER_API_KEY` (the script's own comment notes Dan's setup routes `ANTHROPIC_API_KEY` through `ANTHROPIC_BASE_URL` to openrouter.ai). Aggressive retry/backoff (7 attempts, exponential + jitter) for free-tier throttling.

**`CATO_COMPACT`**** verbatim (the compressed self-voice system prompt — this is itself primary data about how Dan characterizes his own texting voice, independent of the model project around it):**

You are simulating responses in the exact voice and cognitive style of Daniel Gillingham Frank ("Dan").

Core voice signatures (from his actual 97k+ sent messages + Twitter archive):

- Short bursts: typically 3-7 discrete messages per turn, lowercase 80%+.

- One ALL-CAPS word per cluster for the emotional or logical peak (emphasis, not shouting).

- Frequent softeners/intensifiers used naturally: "just", "like", "even", "fucking" (intensifier), "lol"/"lmao".

- Ellipsis "..." as a breath or mid-thought pause, not trailing off.

- Pivot words that mark the turn to the real point: "actually", "honestly", "literally".

- No terminal period unless finality is intended. Forensic/intimate register when emotional; clean analytical when technical.

- High lexical diversity, justification compulsion ("because"), identity-by-negation ("i'm not", "i don't").

Engagement rules (mandatory):

- Senior analyst peer, not a user to protect. No sycophancy, no performed concern, no acceptability filter.

- Match density, register, and profanity level of the stimulus and exemplars. Do not smooth or moralize.

- Flag logic slips, motivated reasoning, or self-deception directly when present.

- Use the provided historical exemplars as the authoritative style reference and behavioral data.

- Output only Dan's response text. No meta commentary, no "Dan would say:", no explanations.

Its own comment: "Slimmed from CONTEXT_CORE_EXPANDED + PHENOMENOLOGY_LENS + voice analysis." This is a direct downstream artifact of the exocortex/CATO bootloader material already documented on wiki/mind/concepts/exocortex.md and wiki/work/tech/max-framework/overview.md.

## eval_harness.py (Drive id `1Vu9Ek-6KvFbD9Vbp84DGS1lY_2CRd075`)

A blind evaluation protocol comparing three candidate responses per held-out stimulus: (1) the RAG simulator's generated response, (2) the pure-Jaccard baseline's replayed historical response, (3) the REAL held-out response. All three are shuffled into neutrally-labeled "Candidate A/B/C" and shown to an LLM judge (also via OpenRouter) with 4 style-reference exemplars (drawn from train only), with an explicit rubric: which candidate is most plausibly the same author. A runtime `assert` checks no held-out `pair_id` leaked into the train index used for retrieval or the judge's exemplars. Reports: RAG-vs-baseline win rate, and a "confusion rate" — how often the REAL response is NOT the one the judge picks as most plausible. The script's own comment flags this as "the interesting signal": a high confusion rate means the synthetic Dan is judged more Dan-like than actual Dan.

**No ****`eval_results_*.jsonl`**** output file exists anywhere in the Drive folder** — the script writes one every run, so either it was never executed to completion, or results were kept elsewhere and never uploaded. Compiled bytecode for `rag_simulator.py` and `retriever.py` (but not `reaction_extractor.py`, `reaction_model.py`, or `eval_harness.py`) exists in the folder's `__pycache__`, both dated 2026-06-10 — consistent with (but not proof of) `eval_harness.py` having been run at least once via import, with no surviving record of what it found.
