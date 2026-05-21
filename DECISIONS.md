# DECISIONS.md

Top-level decision journal for the Aoven protocol. Each entry records a ratified or in-force commitment with verdict, reasons, rejected alternatives, status, and source IDs. Numbering matches the in-spec decision log in `AOVEN_PROTOCOL_v0.1.md` (D1–D12); milestone-level decisions (M-*) and Phase-3 (D-PHASE3-*) entries record process / programme decisions outside the spec proper.

Status tags: **[validated]** **[provisional]** **[observation]** **[rejected]** **[open]**.

## Spec-level decisions (mirror of `AOVEN_PROTOCOL_v0.1.md` § Decision log)

The mirror below is summary-only; the canonical reasons / alternatives / risks live in `AOVEN_PROTOCOL_v0.1.md`. Read both together.

| ID | Decision | Version | Verdict | Status |
|----|----------|---------|---------|--------|
| D1 | Keep all 14 distinct markers (no merge to 10). | v0.1.0 | All 14 retained; each merge collapsed a distinct slippage risk (UNCERTAIN ≠ NOSRC; SPEC ≠ HYP; EMOTION ≠ INTUIT). Logician audit confirmed all distinctions load-bearing. | [validated] |
| D2 | Square-bracket syntax `[MARKER]`, inline prefix per claim, stackable. | v0.1.0 | Minimal friction, readable, machine-parseable. | [provisional] — promoted on first A/B test ratification. |
| D3 | LLM applies markers, not the user. | v0.1.0 | Reduces user cognitive burden; optional user markers permitted. | [provisional] — promoted on first A/B test ratification. |
| D4 | Exploratory archive (Aoa, Aova, Orven, Renavé family) is not canon. | v0.1.0 / corrected v0.1.2 | None serve an epistemic function not covered by the 14 markers. Renavé family historical origin corrected per board input on AOV-15 (see D9). | [validated] |
| D5 | INTUIT redefinition: judgment without explicit derivable reasoning. | v0.1.1 | Original definition merged pre-verbal felt sense with heuristic judgment; new anchor closes the leak. | [validated] |
| D6 | Anti-slippage table extended 10 → 13 transitions. | v0.1.1 | Added INTUIT→HYP laundering, INTERPRET→certainty, CONF(high)→FACT — each a distinct LLM failure mode. | [validated] |
| D7 | HYP definition cleanup — no forward-reference to SPEC. | v0.1.1 | Definitions must stand alone; SPEC contrast moved to "Does NOT mean". | [validated] |
| D8 | CONF gradient at 3 semantic levels (high / medium / low); no numeric. | v0.1.1 | Numeric confidence implies calibration infrastructure that does not exist; revisit in v0.2 only if A/B tests show collapse of useful distinctions. | [validated] |
| D9 | Renavé family historical descriptions corrected per board input. | v0.1.2 | Prior wording asserted Renavé-mu/li/zo were confidence gradients superseded by `CONF` — a NOSRC fabrication. Board supplied correct origin on AOV-15 (relation of repeated presence without interaction; reciprocal; asymmetric; residual feeling). Correction logged explicitly, not silently overwritten — this is the slippage class Aoven exists to prevent. | [validated] |
| D10 | Subset-header qualifier semantics: `allow:` / `require:` non-exclusive; default = `allow:`; subset header NEVER suppresses unlisted markers. | v0.1.3 | Sprint-1 row #18 showed an LLM reading `require:` as exclusive and silently suppressing INTERPRET / INTUIT for turns 6–10. Anti-aura: fail open on ambiguity. Source: CTO `8a46d4c7` on AOV-111; Logician PASS on AOV-115 `b6bd7a58`; CEO ratification `50abfc16`. | [provisional] — pending broader v0.1.3 launch validation. |
| D11 | UR-3 strengthened: `[MEMORY]` claims referencing prior text MUST attach verbatim quotation (`[MEMORY: "..."]` or block-quote, ≤ ~2-sentence cap); longer references use `[NOSRC]`. Applies to LLM self-quotation. | v0.1.3 | Sprint-1 row #10 caught a hallucinated `[MEMORY] Earlier you mentioned Airyscan` against a participant who never said it; v0.1.2 UR-3 relied on participant memory and fails in long sessions. Verbatim-quote requirement makes hallucinated recall mechanically detectable. Source: same triad as D10. | [provisional] — pending broader v0.1.3 launch validation. |
| D12 | UR-8 added: `[Aoven: pause]` / `[Aoven: resume]` / `[Aoven: off]` graceful-exit affordance. Three sanctioned resume signals (explicit token, header re-assertion, implicit-on-first-marker). | v0.1.3 (additive) | Sprint-1 §4 item 9 showed silent abandonment when a participant drifted out of marker discipline; v0.1.2's binary on / off model converted graceful drop into silent slippage. Pure addition; no v0.1.2 behavior breaks. UR-8 numbering collides with the original AOV-54 Patch 1 (stack-depth cap) drafted as UR-8; disposition pending. Source: same triad as D10. | [provisional] — pending broader v0.1.3 launch validation. |

### Usage-rule notes

- **UR-3 revision** is the substantive change in v0.1.3 (`[MEMORY]` + verbatim quote, see D11). The v0.1.2 UR-3 (NOSRC-not-MEMORY for hallucinated recall) is preserved inside the verbatim-quote requirement.
- **UR-5 — "Speakers can request a marker subset, but the LLM is not required to suppress others."** Already in force at v0.1.1; given normative weight by D10 in v0.1.3. UR-5 and D10 together codify C-3 (anti-aura: no silent suppression).
- **UR-8 added** (D12). The number UR-8 was contested between D12 (pause/resume) and the AOV-54 Patch 1 stack-depth cap; CEO repose placed pause/resume at UR-8 and parked the stack-depth cap for renumber-to-UR-9 / v0.1.4 / re-scope.

## Milestone decisions

| ID | Milestone | Date | Verdict | Source |
|----|-----------|------|---------|--------|
| M-1 | v0.1-provisional ratification. End of Phase 1 (definition + audit + patch). Phase 2 (empirical A/B testing) opens. | 2026-04-26 | Closed. CEO + CTO + Logician sign-off. | AOV-7 ratification trail. |
| M-2 | v0.1.2 confirmatory PASS on sealed hold-out. Phase 3 (Usage Designer hire) trigger satisfied. | 2026-05-03 | Reached. Three-part criterion (AOV-35) holds at higher margin on hold-out than on derivation set. Both raters PASS independently. Σ-level Cohen's κ = 0.759. | AOV-49 verdict; CEO ratification comment `9b8b405b` on AOV-1 (mirrored from CTO `3f03b60d`). |

## Programme decisions (Phase 3)

| ID | Decision | Status | Source |
|----|----------|--------|--------|
| D-PHASE3-1 | Authorize Usage Designer hire now. Deferral condition ("A/B confirms epistemic effect") met by M-2. Tracking issue AOV-73. | [validated provisional] | AOV-1 CEO comment `9b8b405b`, 2026-05-03. |
| D-PHASE3-2 | Do NOT initiate paper drafting until v0.1.3 lands. Reviewer-trap mitigation. | [observation] — revisit ~2 weeks after announcement. | AOV-1 CEO comment `9b8b405b`, 2026-05-03. |
| D-PHASE3-3 | Push-deferral lifted on v0.1.2-locked artefacts. Push execution authorized via AOV-67; v0.1.2 is public and DOI-stamped. | [validated] | AOV-1 board comment `765cf513` → CEO comment `3222338e`, 2026-05-03. |

## v0.2 expansion track

| ID | Decision | Status | Source |
|----|----------|--------|--------|
| D-V0.2-PREREG | v0.2 expansion pre-registration scaffold. Required: ≥ 20 primary + ≥ 10 hold-out questions, ≥ 3 domains, ≥ 2 humans + 4 LLM raters, κ power analysis with stated α, pre-registered hypotheses, cross-domain leave-one-out overfit guard. IndependentRater seals before any question generation. Logician primary + CEO co-owner. | [open] — scaffold under AOV-90. | AOV-1 board master directive `3222338e`, 2026-05-03. |
| D-V0.2-RATERS | v0.2 panel composition: Logician primary; IndependentRater on hold-out; ≥ 2 humans + 4 LLM raters; rater seal on Q-generation. Substantial-agreement target retained (Cohen's κ ≥ 0.6). | [open] — operationalised by AOV-90 pre-registration. | AOV-90 scaffold; cross-references AOV-49 hold-out κ = 0.759 as the empirical anchor. |
| D-V0.2-NO-PAPER-YET | Drafting deferred until v0.1.3 lands and v0.2 pre-registration seals. Aligns with D-PHASE3-2. | [observation] | Programme-level, paired with D-PHASE3-2. |

## Sealed / burned material (binding on all future decisions)

- Q1–Q10 — primary set, derivation-tainted. Cannot be reused as a fresh hold-out, but may be replaced for future scoring.
- Q11–Q16 — sealed hold-out, BURNED post-vindication 2026-05-03. Cannot reappear in any future formal scoring.
- 8 contrast pairs from the AOV-24 religious-vs-neutral pilot (theological-metaphysical: Dieu / Agent cosmique personnel; Âme / Continuité subjective post-biologique; Paradis; Enfer; Réincarnation; Jugement après la mort; Miracle; Révélation divine) — burned for Phase 2 reuse.

---

*This document is maintained by the Canonical Scribe (e19c696f). Records; does not editorialize. For full reasons, rejected alternatives, and risk text behind D1–D12, read `AOVEN_PROTOCOL_v0.1.md` § Decision log.*
