# aoven-protocol

**Aoven is a set of epistemic markers and minimal formatting rules that force explicit labeling of claim types in human–LLM exchanges, in order to reduce hallucination, sycophancy, and slippage between epistemic categories.**

The protocol asks the LLM (not the user) to prefix each claim with one of 14 markers — `[FACT]`, `[HYP]`, `[INTUIT]`, `[ANALOGY]`, `[BELIEF]`, `[EMOTION]`, `[MEMORY]`, `[INTERPRET]`, `[UNCERTAIN]`, `[NOSRC]`, `[CONF]`, `[REC]`, `[SPEC]`, `[LIMIT]` — and obey 13 anti-slippage transitions and a small set of usage rules (UR-1 … UR-8). Markers are inline, stackable, machine-parseable, and friction-light: the user only adds the header `[Aoven v0.1]`.

## Status

- **v0.1.1** — first ratified provisional release (2026-04-26). 14 markers fixed, anti-slippage table extended to 13 transitions, INTUIT and HYP tightened, CONF locked at 3 semantic levels (D5–D8).
- **v0.1.2** — **CONFIRMATORY PASS on sealed hold-out (Q11–Q16), 2026-05-03.** Same three-part criterion (CEO adjudication AOV-35; ratification AOV-36) holds at higher margin on a fresh sealed hold-out than on the derivation set. Hold-out aggregate Layer-1 improvement: Logician 91.7 % / IndependentRater 100 % (vs 79.3 % / 87.5 % on the primary set). Inter-rater Σ-level Cohen's κ = 0.759 (substantial, Landis–Koch). Both raters PASS independently on all three criteria across both runs. Milestone #2 reached; Phase 3 (Usage Designer hire) trigger satisfied. v0.1.2 is public and DOI-stamped.
- **v0.1.3 — provisional, in launch validation.** Minor-clarifications bundle ratified by CEO + Logician on 2026-05-03 under AOV-111 / AOV-115: `allow:` vs `require:` subset-header semantics (D10), UR-3 verbatim-quotation requirement on `[MEMORY]` (D11), UR-8 `[Aoven: pause]` / `[Aoven: resume]` / `[Aoven: off]` graceful-exit affordance (D12). Pure additions or sharpenings; no v0.1.2 behavior breaks.
- **v0.2 — expansion track, pre-registered.** Scaffold under AOV-90: ≥ 20 primary + ≥ 10 hold-out questions, ≥ 3 domains, ≥ 2 humans + 4 LLM raters, κ power analysis with stated α, pre-registered hypotheses, cross-domain leave-one-out overfit guard. IndependentRater seals before any question generation.

## Where to read

- Canonical specification: [`AOVEN_PROTOCOL_v0.1.md`](./AOVEN_PROTOCOL_v0.1.md) — markers, formats, usage rules, anti-slippage table, decision log D1–D12.
- Empirical test plan: [`AOV_TEST_PLAN_v0.1.md`](./AOV_TEST_PLAN_v0.1.md) — two-layer scoring (Layer 1 blind / markers-stripped, Layer 2 markers-visible), 10 primary + 6 sealed hold-out questions, quadratic-weighted Cohen's κ ≥ 0.6 per dimension per layer.
- Hold-out reconciliation (v0.1.2 confirmatory): [`tests/phase2/reconciliation_holdout_v0.1.2.md`](./tests/phase2/reconciliation_holdout_v0.1.2.md).
- Primary-set reconciliation: [`tests/phase2/reconciliation_logician_independentrater.md`](./tests/phase2/reconciliation_logician_independentrater.md).
- Rater scores (Logician + IndependentRater, primary + hold-out, Layer 1 + Layer 2): under [`tests/phase2/`](./tests/phase2/).
- Phase 4 v0.2 60-cell corpus + closeout artefacts: [`tests/v0.2/`](./tests/v0.2/).
- Project governance, roles, anti-aura constraint: [`AGENTS.md`](./AGENTS.md).
- Ratified decisions (verdict + reasons + rejected alternatives): [`DECISIONS.md`](./DECISIONS.md).

## Anti-aura

Aoven is an engineering artifact for reducing slippage in LLM output, not a fantasy conlang or poetic dictionary. The exploratory archive (Aoa, Aova, Orven, Renavé, Renavé-mu/li/zo — see D4 / [`docs/archive_exploratoire.md`](./docs/archive_exploratoire.md)) is pre-protocol conlang material with no epistemic function the 14 markers don't already cover. It is documented for historical traceability and is not canon.

## License & contact

Project hosted at <https://github.com/Mythmaker28/aoven-protocol>. Issues, governance, and decision-routing are tracked internally via Paperclip; the canonical doc and test artefacts in this repo are the public source of truth.
