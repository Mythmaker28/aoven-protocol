# AGENTS.md — Aoven project governance

Public governance rules for any agent (human or LLM) contributing to Aoven. This file is the project-public charter; private agent instruction files are out of scope here.

---

## Roles

| Role | Responsibility | Hire / authorship constraint |
|------|---------------|------------------------------|
| **Protocol Architect** | Drafts and revises the canonical spec (`AOVEN_PROTOCOL_v0.1.md`): markers, formats, usage rules, anti-slippage rules. | May not also serve as sole reviewer of own drafts. |
| **Epistemic Logician** | Audits drafts for category leaks, definitional circularity, missed slippage paths. Independent reviewer, not co-author of the artifact under review. | Must be structurally independent from the artifact under audit at the moment of review. |
| **Canonical Scribe** | Records validated, provisional, in-observation, rejected, and open-question decisions in the canonical spec. Does not author content. Records both sides of disagreements. | Anti-editorialization: records, does not argue. |
| **Red Team / Independent Rater** | Adversarial probing of the protocol; third independent rater on empirical tests. Not a co-author of the protocol or the rubric being applied. | Must be neither author of the protocol nor scorer of the rubric they apply. |

---

## Governance rules

### G-1 — Named-reviewer sign-off gate (no author self-validation)

A decision moves from `[provisional]` to `[validated]` only after a named reviewer who is not the author signs off in writing on a referenced artifact (issue comment, audit document). Author self-declaration of validation is not a valid gate. If a CEO ratification lands before the audit is complete, the audit's blocking findings still apply and must be integrated before the next phase opens.

### G-2 — Anti-aura rule

No prose, term, or claim that sounds impressive without an operational definition. Every term used in this repo must either:

- be one of the 14 canonical markers in `AOVEN_PROTOCOL_v0.1.md`, or
- have a strict definition in the spec, or
- carry an explicit status tag (`[provisional]`, `[observation]`, `[open]`, `[rejected]`).

Aoven is **not** a conlang, not a poetic vocabulary, not a personal project. Seductive language without definition is removed without discussion.

### G-3 — New-vocabulary budget: ≤3 non-marker terms

Total new vocabulary outside the marker set is capped at 3 terms. Adding a term requires demonstrating an epistemic function not covered by an existing marker. As of v0.1.2: **0 used**.

### G-4 — Burden of proof on retention

Exploratory or legacy terms are not Aoven canon by default. The burden of proof is on retention, not on rejection. A term remains `[observation]` until an agent demonstrates a unique epistemic function.

### G-5 — Disagreement is recorded, not resolved silently

If two agents disagree on a decision, both positions are recorded with reasons in `DECISIONS.md` along with the resolution path (or its absence). The Scribe does not pick a winner.

### G-6 — Hiring rule (structural conflict only)

Hires are added when the project has a structural conflict that no current role can resolve without compromising independence — e.g., a third independent rater is needed because the only available raters are protocol co-authors. Hires are not added on workload alone.

---

## Anti-hallucination constraints (binding on contributors)

These constraints apply to anything written into the spec, decision log, or test outputs.

- **C-1 — Marker discipline.** Any claim in the canonical spec or test results must fit one of the 14 marker categories. If it does not fit, it does not belong, or a new marker proposal is required (subject to G-3).
- **C-2 — Fact ≠ hypothesis.** A `FACT` requires an external verifiable source; a `HYP` requires a stated, specific test condition. Confident belief is not FACT. Falsifiable-in-principle is not HYP.
- **C-3 — Analogy ≠ proof.** Conclusions drawn from an `ANALOGY` carry `HYP` or `SPEC` on the derived claim; they never inherit truth-status from the source domain.
- **C-4 — Intuition is not a hypothesis.** Upgrading `INTUIT` to `HYP` requires stating a specific test condition. A marker swap alone is the slippage, not its repair.
- **C-5 — No silent withdrawal.** When a `BELIEF` or `NOSRC` claim is challenged, respond by either citing a source (upgrade to `FACT`) or downgrading to `UNCERTAIN`. Quietly dropping the claim is itself a slippage.
- **C-6 — No invented history.** Facts about the project's past go in the spec, decision log, or issue thread, or they do not go anywhere. Reconstructed narratives are out.

---

## Anti-scope — what Aoven is NOT

- **NOT a fantasy conlang.** Markers are not flavor words. The spec is not world-building.
- **NOT a poetic dictionary.** Aesthetic appeal is not a retention criterion.
- **NOT a personal project.** Scope is set by the empirical question (does it reduce the four failure modes), not by individual authorial preference.
- **NOT a private vocabulary system.** Aoven exists only insofar as it produces measurable improvement in human–LLM exchanges per the test plan.

---

## Workflow

1. **Drafting** — Protocol Architect drafts in the canonical spec or in a labeled patch. Each entry carries source attribution and a status tag.
2. **Audit** — Epistemic Logician reviews independently and writes blocking findings. The audit is a public artifact.
3. **Patch** — Architect integrates blocking findings before the gate opens. The Scribe records the patch with full context.
4. **Empirical test** — Test plan runs A/B on a fixed question set with the rubric in `tests/test_plan.md`. Three independent raters; quadratic-weighted Cohen's κ ≥ 0.6 per dimension. Pre-committed refinement candidates and a hold-out probe set guard against p-hacking.
5. **Versioning** — Decisions move from `[provisional]` to `[validated]` only after named-reviewer sign-off (G-1) and, where applicable, empirical signal.

---

## Status tags (used throughout the repo)

- `[validated]` — accepted, passed audit and (where applicable) test signal.
- `[provisional]` — in use, awaiting test data or named-reviewer sign-off.
- `[observation]` — under watch; may or may not be retained.
- `[rejected]` — explicitly excluded; reason recorded.
- `[open]` — open question; no decision yet.
