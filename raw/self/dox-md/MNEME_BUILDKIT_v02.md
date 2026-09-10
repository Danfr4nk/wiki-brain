# MNEME — PERSONAL MEMORY CORPUS PLATFORM

## Full Build Kit v0.2

**Build Environment:** Google AI Studio (canvas/artifact mode) **AI Integration Model:** Option B — Gemini in-canvas (no user-supplied API key) **Revised:** April 2026

## SECTION 1 — PROJECT DEFINITION

### 1.1 Core Problem Statement

LLM users who invest significant time in AI-assisted work suffer from a chronic cold-start problem: every session begins with zero context about who they are. Current solutions treat this as a retrieval problem. It is actually an extraction and synthesis problem. Users don't know what to document, don't know how to structure it, and have no feedback on whether their efforts are working.

MNEME solves the input side. It is a structured self-knowledge extraction engine that produces a deployable, versioned exocortex artifact — a "bootloader document" — injectable into any LLM session to achieve persistent context.

### 1.2 Target User

People spending 3+ hours per week with LLMs who have already felt the cold-start pain. They've tried pasting things into system prompts. They know something is missing. They have the problem but lack the methodology.

### 1.3 Core Value Proposition

Transform unstructured personal narrative ("storytime") into a structured, layered, deployable context document — through guided extraction, contradiction surfacing, and progressive corpus visualization.

### 1.4 What This Is NOT

- Not a chat interface or journaling app

- Not a RAG/retrieval system

- Not vendor-locked to any LLM

- Not requiring user to supply or manage an API key

## SECTION 2 — CORPUS ARCHITECTURE

### 2.1 The Five Layers (Ordered by Impact-to-LLM)

Extraction follows "largest blast radius first" — life circumstances that affect the most LLM response domains get collected before narrow preferences.

**LAYER 1 — LIFE CIRCUMSTANCES** High-impact context affecting broad categories of LLM responses.

Fields: Relationship status; Dependent structure (children ages, eldercare); Living situation (urban/rural, solo/shared); Employment status + sector + seniority; Geographic anchor + mobility; Financial posture (constrained / stable / flexible — broad band only); Health context affecting daily life; Active major life transitions.

*Example LLM impact:* Vacation recommendation transforms entirely when the model knows the user is married with two children under 6.

**LAYER 2 — BIOGRAPHICAL SUBSTRATE** The formative history that explains the present state.

Fields: Geographic origin + major location arcs; Family of origin structure + cultural background; Educational path; Career arc (not just current role); Major relationship history (opt-in); Significant formative experiences (trauma-adjacent: clearly flagged opt-in); Community affiliations.

**LAYER 3 — IDEOLOGICAL + AXIOLOGICAL MAP** Core beliefs and values — ranked by conviction strength, not flat-listed.

Fields: Political orientation + specific policy positions; Ethical framework (utilitarian / deontological / virtue-based / hybrid); Religious or spiritual orientation; Non-negotiable core values; Known internal contradictions (self-reported or surfaced); Actively-updating positions vs. settled ones.

*Critical design note:* Conviction strength axis is mandatory. "I believe X" is less useful than "I hold X with high conviction and will not update without substantial evidence." The UI must capture this gradient.

**LAYER 4 — COGNITIVE STYLE PROFILE** How they think, not what they think. Cannot be accurately self-reported — must be inferred from behavioral signals within the platform.

Fields: Reasoning preference (intuitive-first / systematic-first); Uncertainty tolerance; Update triggers (what kinds of evidence change their mind); Known cognitive biases (self-reported); Response to pushback by domain; Preferred depth level per subject area.

*Note:* Fields in this layer are tagged with source: self-reported vs. platform-inferred. Inferred fields are flagged for user validation.

**LAYER 5 — STYLOMETRIC + CULTURAL SIGNATURE** How they write and what they care about aesthetically and culturally.

Fields: Writing register range (formal → casual → profane); Vocabulary density preference; Humor type (dry / absurdist / referential / none); Code-switching patterns; Music taste with anti-tastes (what they reject is as defining as preferences); Visual/aesthetic sensibility; Subcultural affiliations; Media diet (books, podcasts, film, games) with depth indicators.

## SECTION 3 — EXTRACTION METHODOLOGY

### 3.1 Storytime Mode (Primary Input)

Users type or speak freely in response to guided prompts. The platform's built-in Gemini instance processes narrative into structured layer data.

**Prompt Funneling Strategy — always large to small:**

Open questions (high extraction yield): "Tell me about your living situation right now — who's in your life day-to-day?" / "What does a typical week look like for you work-wise?" / "What's been the biggest change in your life in the last two years?"

Progressive narrowing toward abstract: "When you make a big decision, what does your process look like?" / "What's something you used to believe strongly that you no longer hold?" / "Describe your taste in music like you're explaining it to someone who doesn't know you at all."

**Anti-Patterns (prohibited in prompt library):** Direct "what are your values" questions (generates performative answers); Yes/no questions (no extractable narrative content); Leading questions (contaminates the data); Rapid-fire sequences (degrades response quality and user trust).

### 3.2 Adversarial Elicitation (Layers 3 + 4)

For ideological and cognitive style layers, structured challenges reveal actual positions rather than performed ones: present value-conflict scenarios and ask the user to choose; show two previously-stated positions and ask them to rank; surface a position and ask "would you update on this if X were true?"

### 3.3 Behavioral Signal Collection (Layer 4)

The platform observes interaction patterns as Layer 4 input: what sections does the user skip (low engagement / possible avoidance); what do they correct (high conviction signals); time spent per section (salience indicators); contradictions resolved vs. left open (epistemic style signal).

### 3.4 Import Modes

Paste existing documents (prior system prompts, bio pages); manual field entry for specific known facts; (Phase 3) upload and parse prior LLM chat exports.

## SECTION 4 — OUTPUT ARTIFACT SPECIFICATION

### 4.1 Bootloader Document Format

Canonical output: structured markdown with YAML frontmatter (version, generated date, coverage_score, layers_complete, last_updated), followed by sections: LIFE CIRCUMSTANCES, BIOGRAPHICAL CONTEXT, BELIEFS + VALUES, COGNITIVE STYLE, VOICE + CULTURE, DEPLOYMENT INSTRUCTIONS.

### 4.2 Component Outputs

Quick Context Card (100-word summary for fast inject); Voice Sample Block (3-5 example sentences demonstrating register); Anti-Profile (what this user is NOT — often more useful for LLM calibration than positive assertions); Layer JSONs (machine-readable per-layer exports).

### 4.3 Deployment Instructions Block

Every output includes: where to paste per LLM (system prompt / first message / custom instructions field); verification test prompts ("ask your LLM this to confirm it's using the document"); known degradation patterns (context window compression over long sessions); recommended update cadence.

## SECTION 5 — TECHNICAL ARCHITECTURE

### 5.1 Stack Philosophy

Built in Google AI Studio — the canvas/artifact environment is the IDE, using the Gemini instance built into that environment via native API call capability, no user-facing API key management required. Single-file HTML artifact first — self-contained, no build tooling, no npm. Complexity escalation path to Vite/React only if the project outgrows single-file. Local persistence only (Phase 1) — all data lives in localStorage/IndexedDB; no server, sync, or auth, treated as a feature given data sensitivity (relationships, ideology, health).

### 5.2 Frontend Stack

Phase 1 (AI Studio Canvas Artifact, Single File): Vanilla HTML5/CSS/JS, localStorage + IndexedDB native storage, Gemini via AI Studio canvas native API, Blob export, hand-coded SVG visualization, hash-based routing.

Phase 2 (Extracted App, if needed): React 18 + Vite, Tailwind CSS, Zustand state, Dexie.js storage, React Router v6, Framer Motion, markdown-it + FileSaver.js export.

### 5.3 AI Integration (In-Canvas Gemini)

AI Studio's canvas environment exposes Gemini natively via `ai.generateContent({model: "gemini-2.0-flash", contents: [...], generationConfig: {responseMimeType: "application/json"}})` — no import, no key. Call types: storytime synthesis, gap detection, contradiction detection, document compilation, next-prompt generation. All AI outputs validated client-side before storage — schema conformance check on every response; malformed outputs surface a user-visible error, never get written to storage.

### 5.4 Data Architecture

Storage schema (localStorage keys, Phase 1): mneme_layer_1 through mneme_layer_5 (per-layer structured JSON), mneme_sessions (raw storytime transcripts array), mneme_contradictions (detected conflict log), mneme_coverage (coverage score history time series), mneme_exports (saved export snapshots), mneme_settings (user preferences).

Each field stores: value, confidence level, source type, originating session, timestamp, and whether the user has explicitly validated it. Inferred fields (especially Layer 4) are visually distinguished in the UI until validated.

### 5.5 Project File Structure (Phase 1 — Single File)

`mneme.html` (entire Phase 1 app), `prompts/` (prompt library: synthesis_layer1-5.txt, gap_detection.txt, contradiction.txt, compilation.txt), `schemas/` (JSON schemas per layer), `BUILDKIT.md`.

### 5.6 Prompt Engineering Architecture

All synthesis prompts follow: role assignment, schema injection, few-shot examples (min 2), edge case instructions, output constraint (JSON only, no preamble/markdown fences). Prompts are version-controlled as plain text files, never modified without testing against a fixed set of example narratives first — treat prompts like code.

## SECTION 6 — FEATURE ROADMAP

**Phase 1 — MVP (Single HTML File, In-Canvas AI):** Onboarding screen; Storytime interface for Layer 1 only; Gemini synthesis of Layer 1 narrative into structured fields; Corpus view with manual field editing; Coverage indicator; Basic bootloader document export; Contradiction detection within Layer 1. Success metric: zero to deployable Layer 1 context document in under 20 minutes.

**Phase 2 — Full Layer Coverage:** Layers 2–5 extraction flows + synthesis prompts; full elicitation prompt library; cross-layer contradiction detection; coverage radar chart (all five layers); conviction strength UI (Layer 3); behavioral signal collection (Layer 4); voice sample extraction (Layer 5); anti-profile generation; component output exports; corpus version history.

**Phase 3 — Import + Advanced:** Chat log import + parsing (Claude/ChatGPT export formats); LLM-specific deployment packs; corpus diff viewer; mobile optimization; optional encrypted cloud sync.

## SECTION 7 — AI STUDIO BUILD METHODOLOGY

Core principles: Schema before everything (lock the JSON schemas before any UI/logic); one component per session (AI Studio loses fidelity on large codebases — never ask for "the whole thing" in one shot); always provide current state (paste working code at the top of each new session — AI Studio has no memory); test before extending; prompts are code (develop and version synthesis prompts in the system prompt tester before embedding); lock the interface contract first (define exact data shapes passing between components before building them); single file until it breaks (extract to multi-file only when AI Studio actually fails to handle the context, usually around 800–1000 lines).

## SECTION 8 — BUILD PROMPTING SEQUENCE

A literal sequence of discrete build sessions for AI Studio, each with a validation step: Session 0 (Schema Definition, no code — locks JSON Schema draft-07 for all five layers); Session 1 (Application Shell — single-file HTML, dark-mode-first, hash-routed nav, placeholder sections); Session 2 (Data Layer — MnemeDB object with getLayer/setLayer/updateField/getSessions/addSession/getCoverageHistory/addCoverageSnapshot/exportSnapshot/clearAll, all localStorage-backed); Session 3 (Coverage Scoring Engine — per-layer and weighted-overall completeness percentages, SVG bar indicators in header); Session 4 (Storytime Interface, no AI yet — elicitation panel, session history panel, corpus fields panel, synthesizeLayer1() stubbed); Session 5 (Synthesis Prompt Development in the AI Studio system prompt tester — validated against 4 test narratives: rich, sparse, contradictory, off-topic); Session 6 (AI Synthesis Integration — wires the validated prompt into a real `ai.generateContent` call, merges structured JSON into layer storage); Session 7 (Contradiction Detection — Gemini-driven scan for logical tensions between field values, surfaced as resolvable cards); Session 8 (Export Engine — compileBootloader() produces the full markdown document via Gemini, plus a template-only Quick Context Card requiring no AI call); Session 9 (Coverage Visualization — pure-SVG pentagon radar chart across the five layers, layer summary cards, recent activity feed); Session 10 (Polish + Edge Cases — loading/error/empty states, onboarding overlay, two-step typed-confirmation delete).

Post-Phase 1 sessions queued but undetailed: Layer 2–5 buildouts, cross-layer contradiction detection, anti-profile generator, import of existing documents, corpus version history/diff viewer, mobile optimization, extraction to Vite/React if needed.

## SECTION 9 — DESIGN (RESERVED)

Intentionally empty. Design pass follows after architecture is locked. Open questions: visual language for corpus density/coverage; storytime interaction model; contradiction-surfacing UX tone; bootloader document preview aesthetic; onboarding sequence; whether the radar chart is the right visualization for this data.

## SECTION 10 — OPEN QUESTIONS

1. Conviction strength UI (Layer 3): slider vs. categorical labels — does the compiled document actually instruct the LLM differently based on conviction level?

1. Behavioral signal granularity (Layer 4): how much skip/correction tracking is useful vs. feeling surveilled?

1. Anti-profile weight in output: too much negative-space definition can confuse LLMs.

1. Layer 4 inference transparency: how to communicate inferred-vs-self-reported clearly without undermining confidence.

1. Sensitive data communication (Layer 2): trauma-adjacent biographical content, health information, relationship history — how to communicate sensitivity without being patronizing.

1. Context window degradation: is there a smarter solution than a warning — e.g. a "compact mode" export that is half the tokens but retains the highest-impact fields?

*End of Build Kit v0.2*
