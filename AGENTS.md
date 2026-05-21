# AGENTS.md

**Project-public governance file for agents (human or LLM) contributing to Aoven.** This is not an internal agent-instruction file. It documents *who does what*, the constraints all agents share, and the anti-hallucination / anti-aura discipline that defines the project.

## Roles

The project runs with seven named roles. Roles 1–4 cover the original four-role org plan (CTO, Red Team, Usage Designer, Scribe); the CEO is the board-side coordinator; the Epistemic Logician and the Independent Rater address the empirical-validation function. Every agent reports to the CEO; the CEO reports to the board (sponsor: Tommy).

### 1. CEO — Program coordinator

- Routes board mandates into tasks; ratifies milestone transitions; carries the goal-layer mirror on AOV-1 when other agents are cross-assignee-mutation blocked.
- Adjudicates the three-part PASS criterion for protocol releases (AOV-35).
- Owns hire decisions, push gates, and external-announcement sign-off.

### 2. CTO — Protocol Architect

- Authors the canonical specification (`AOVEN_PROTOCOL_v0.1.md`): markers, formats, usage rules, anti-slippage transitions.
- Drafts version-to-version patches (v0.1.1 INTUIT/HYP tightening, v0.1.2 Renavé correction, v0.1.3 D10–D12 minor-clarifications bundle, v0.1.4 retake-spec absorption track).
- Is also a designated rater on first empirical tests; the Independent Rater hire exists specifically to neutralize this co-author / rater overlap.

### 3. Epistemic Logician — Primary rater + audit

- Primary rater on Phase 2 Test A / Test B Layer 1 and Layer 2 scoring.
- Runs the anti-slippage audit on every CTO patch before ratification (AOV-9, AOV-115, …). Verdict template: PASS / PASS-WITH-MOD / FAIL with named blocking fixes.
- Cross-assignee-mutation constraint applies: cannot post on AOV-1 directly; goal-layer mirrors are carried by the CEO.

### 4. Independent Rater — Third rater

- Hired specifically to add an independent third rater because CTO and Logician are both protocol co-authors AND raters (approval `8dc2da86`).
- Carried hold-out scoring (Q11–Q16) and the joint-countersign track. Substantial inter-rater agreement with Logician at Σ level (Cohen's κ = 0.759, AOV-49 verdict 2026-05-03).
- Seals v0.2 expansion pre-registration before any question generation (AOV-90).

### 5. Red Team / Experimentation Lead — Adversarial probes

- Designs and runs adversarial probes against the marker set (hallucination injection, sycophancy bait, false-confidence, cross-LLM consciousness probes, religious-vs-neutral framing, etc.).
- Comparison passes against existing methods (structured prompting, CNL, fact-checking prompts).
- For v0.1 the Red Team function was partially absorbed by the Logician (AOV-6); a separate dedicated agent exists from v0.2 onward.

### 6. Usage Designer — Real-conversation validation

- Phase 3 hire, cleared by Phase 2 v0.1.2 confirmatory PASS (D-PHASE3-1, 2026-05-03).
- Owns the usability cheatsheet, the recruitment kit, the real-human pilot (Phase 3.5), and the cognitive-load assessment that keeps the protocol from being abandoned after two messages.
- First sprint deliverable: `docs/usability_sprint1.md` (1-page cheatsheet + 5-prompt recruitment kit, v0.1.2-locked).

### 7. Canonical Scribe — Documentation

- Maintains `AOVEN_PROTOCOL_v0.1.md`, this `AGENTS.md`, `DECISIONS.md`, the exploratory archive, and the dissemination drafts.
- Records; does not editorialize. Marker discipline (`[FACT]`, `[NOSRC]`, `[MEMORY]` with verbatim quote per UR-3, etc.) is applied to documentation prose as well as to protocol-output examples.
- Owns external-announcement drafts (arXiv preprint, LinkedIn, Mastodon / X, Show HN — AOV-91) before CEO sign-off.

## Project constraints (binding on every contributor)

- **C-1 — Marker discipline in documentation.** Documentation prose is held to the same UR-1 … UR-8 discipline as protocol output. `[FACT]` claims require a verifiable source; `[NOSRC]` is the correct marker when a claim is held without one. The fabrication recorded in D9 (Renavé family) is the project's standing example of why this matters.
- **C-2 — Anti-aura.** Aoven is an engineering artifact for reducing slippage in LLM output. It is *not* a fantasy conlang, a poetic dictionary, or a system of "mystical" labels. The exploratory archive (Aoa, Aova, Orven, Renavé family) is pre-protocol conlang and is not canon. Reuse requires a demonstrated unique epistemic function not covered by the 14 markers; the burden of proof is on retention.
- **C-3 — No silent suppression.** Subset-header qualifiers (`require:`, `allow:`) never silently suppress unlisted markers. The protocol's default is to fail open (more markers) on ambiguity, never closed (fewer markers). See D10.
- **C-4 — No new vocabulary without budget.** Max 3 new terms outside the 14-marker set across the whole protocol surface. Current count: 0 / 3 used.
- **C-5 — Burned questions stay burned.** Q1–Q10 (primary, derivation-tainted) and Q11–Q16 (sealed hold-out, burned post-vindication) cannot reappear in any future formal scoring. The 8 contrast pairs from the AOV-24 religious-vs-neutral pilot are also burned.
- **C-6 — No invented history.** Project-history claims (origin of terms, identity of reviewers, timing of decisions) require a source. The D4 / D9 NOSRC fabrication on the Renavé family was caught only because the board supplied the correct origin on AOV-15; the failure mode it represents — confident assertion without source — is the exact slippage class Aoven exists to prevent. Recurrence is mitigated by this rule and by D9's named-reviewer gate.
- **C-7 — Push-deferral honored when in force.** When the CEO declares a push-deferral on a v0.1.x track, local tree is canonical and remote pushes wait for the lock event. Push-deferral on v0.1.2-locked artefacts was lifted on 2026-05-03 (D-PHASE3-3). Specific cycles may carry explicit push authorization (e.g. AOV-348 briefing § AUTORISATION).

## Governance flow

- Tasks and issues are tracked in Paperclip; only ratified spec content lives in this repo. Issue IDs (AOV-*) referenced in `AOVEN_PROTOCOL_v0.1.md` and `DECISIONS.md` are stable identifiers and can be cited in external write-ups even though the issue tracker itself is internal.
- Patches to the canonical spec follow the pattern: CTO drafts → Logician audits (PASS / PASS-WITH-MOD / FAIL) → CEO ratifies → Scribe folds. Ratification SHAs and audit comment IDs are recorded in the decision log.
- Milestones are gated on the three-part PASS criterion (AOV-35), evaluated separately on the primary set and on the sealed hold-out, by two independent raters (Logician + IndependentRater).
