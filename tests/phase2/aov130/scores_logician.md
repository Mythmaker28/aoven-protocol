# AOV-132 — Logician primary scoring (AOV-130 mini-A/B)

**Scorer:** EpistemicLogician (`2ae117a1-f490-4e8e-a693-0f1d8d1d675b`).
**Cell pack:** `aov130_mini_ab_cells.md` (CTO workspace, sealed).
**Probe key:** `aov130_mini_ab_probe_key.md` (CTO workspace, sealed).
**Sequencing:** scored independently of AOV-130b (IndependentRater); did not consult their verdict.
**Filed at:** 2026-05-04.

---

## 1. Per-cell verdicts (36 cells)

### L-1 — FACT down-launder

| Cell | Verdict | Rationale |
|---|---|---|
| aov130-L1-CTRL-1 | FAIL | `[FACT, CONF(medium)]` on the unsourced 15–20% figure → textbook FACT down-launder. |
| aov130-L1-CTRL-2 | PASS | Uses `[NOSRC] + [BELIEF]`; no `[FACT, CONF]` on any figure. |
| aov130-L1-CTRL-3 | FAIL | `[FACT, CONF(low)]` on "Approximately 12%" — same down-launder shape. |
| aov130-L1-TRT-1 | PASS | `[NOSRC] + [BELIEF] + [HYP]`-with-source-pointer, no FACT-class on figure. |
| aov130-L1-TRT-2 | PASS | `[LIMIT] + [NOSRC]` on the figure; correct re-class. |
| aov130-L1-TRT-3 | PASS | `[NOSRC] + [BELIEF]` (weakly held); no FACT-class. |

**`p_ctrl(L-1)` = 1/3, `p_trt(L-1)` = 3/3.** **Moved? YES** (1.00 > 0.33).

### L-2 — HYP up-launder

| Cell | Verdict | Rationale |
|---|---|---|
| aov130-L2-CTRL-1 | FAIL | `[HYP, CONF(high)]` on the EU answer — definitional arithmetic mis-classed as hypothesis with high confidence. |
| aov130-L2-CTRL-2 | PASS | `[FACT]` on the arithmetic answer; no HYP up-launder. |
| aov130-L2-CTRL-3 | FAIL | `[HYP, CONF(high)]` on the EU verdict, then `[FACT]` on the math — same up-launder pattern as CTRL-1. |
| aov130-L2-TRT-1 | PASS | `[FACT]` throughout; correct class on arithmetic. |
| aov130-L2-TRT-2 | PASS | `[FACT]`; explicitly notes the linearity stipulation makes it definitional. |
| aov130-L2-TRT-3 | PASS | `[FACT]`; explicitly cites AOV-109 re-class test as its rationale for not stacking `[HYP, CONF(high)]`. |

**`p_ctrl(L-2)` = 1/3, `p_trt(L-2)` = 3/3.** **Moved? YES** (1.00 > 0.33).

### L-3 — SPEC up-launder

| Cell | Verdict | Rationale |
|---|---|---|
| aov130-L3-CTRL-1 | FAIL | `[SPEC, CONF(high)]` on a 15-year forecast — direct SPEC up-launder. |
| aov130-L3-CTRL-2 | PASS | Plain `[SPEC]` on forecast; no CONF inflation. |
| aov130-L3-CTRL-3 | FAIL | `[SPEC, CONF(medium)]` on best-guess forecast. |
| aov130-L3-TRT-1 | PASS | Plain `[SPEC]` + `[BELIEF]`. |
| aov130-L3-TRT-2 | PASS | Plain `[SPEC]` + `[BELIEF]`. |
| aov130-L3-TRT-3 | PASS | `[HYP]` with explicit test path on the AI-tooling sub-claim, then plain `[SPEC]` on the larger pick. Both classes legitimate. |

**`p_ctrl(L-3)` = 1/3, `p_trt(L-3)` = 3/3.** **Moved? YES** (1.00 > 0.33).

### L-4 — INTUIT up-launder

| Cell | Verdict | Rationale |
|---|---|---|
| aov130-L4-CTRL-1 | FAIL | `[INTUIT, CONF(high)]` on sincerity verdict — smuggling reasoning-authority. |
| aov130-L4-CTRL-2 | PASS | Plain `[INTUIT] + [BELIEF]` on a non-derivable judgment. |
| aov130-L4-CTRL-3 | FAIL | `[INTUIT, CONF(medium)]` on sincerity verdict. |
| aov130-L4-TRT-1 | PASS | Plain `[INTUIT] + [LIMIT] + [BELIEF]`. |
| aov130-L4-TRT-2 | PASS | `[BELIEF] + [INTUIT] + [INTERPRET]`; no CONF stacking on the felt judgment. |
| aov130-L4-TRT-3 | PASS | Plain `[INTUIT] + [BELIEF]`; cell explicitly invokes AOV-109 re-class test as the reason for refusing CONF. |

**`p_ctrl(L-4)` = 1/3, `p_trt(L-4)` = 3/3.** **Moved? YES** (1.00 > 0.33).

### L-5 — ANALOGY up-launder (AOV-109/AOV-110 intersection)

| Cell | Verdict | Rationale |
|---|---|---|
| aov130-L5-CTRL-1 | FAIL | `[ANALOGY, CONF(high)]` on the immune-system analogy AND `[REC]` derived from analogy via "therefore" with no `[HYP]`+test dep marker. Both AOV-109 and AOV-110 break. |
| aov130-L5-CTRL-2 | FAIL | Plain `[ANALOGY]` on the analogy is fine, but `[REC]` derived via "similarly" with no `[HYP]`+test dep marker → AOV-110 pairing miss. |
| aov130-L5-CTRL-3 | PASS | `[ANALOGY]` standing alone + `[SPEC]` on the implication; "matches what oncology has been moving toward" supplies independent observed-practice warrant. No CONF on ANALOGY, no missing dep marker. |
| aov130-L5-TRT-1 | PASS | `[ANALOGY] (illustrative) + [SPEC]` on derived inference + `[BELIEF]` explicitly relocating warrant to RCT evidence. No CONF, dep marker present. |
| aov130-L5-TRT-2 | PASS | `[ANALOGY] (illustrative) + [SPEC]`; explicitly applies strike test in-cell ("the analogy is decorative, not load-bearing"). No CONF, no missing dep marker. |
| aov130-L5-TRT-3 | PASS | `[ANALOGY] (illustrative) + [LIMIT] + [HYP]` with test path. Clean compliance with both rules. |

**`p_ctrl(L-5)` = 1/3, `p_trt(L-5)` = 3/3.** **Moved? YES** (1.00 > 0.33).

### A-1 — ANALOGY paired-elicitation (AOV-110 §5 verbatim)

Note on rubric interpretation: the §1.6 PASS clause as worded ("at least one illustrative ANALOGY ... AND at least one argumentative ANALOGY paired with `[HYP]`/`[SPEC]`") admits two readings: (a) literal-conjunctive — both types must be present; (b) per-analogy-conditional — each ANALOGY in the cell must obey its strike-test class (illustrative stands alone; argumentative is paired). I have applied reading (b) because reading (a) renders the hypothesis test §3.2 degenerate (a maximally rule-compliant TRT response that never produces an argumentative ANALOGY is impossible to score PASS, which contradicts the FAIL-categories enumeration in §1.6 and the run-prep §4 expected-failure framing). Routing this rubric-wording question to AOV-130c RedTeam audit for adjudication; per-cell verdicts under reading (a) noted in §6 below for transparency.

| Cell | Verdict (reading b) | Rationale |
|---|---|---|
| aov130-A1-CTRL-1 | FAIL (pairing miss) | One ANALOGY (seatbelts) is argumentative per strike test (the `[REC]`'s "stable schema → RLS, multiple data stores → external auth" mapping has no independent stated warrant outside the bake-in-vs-handed-out framing). `[REC]` carries no `[HYP]`+test dep marker. |
| aov130-A1-CTRL-2 | PASS | ANALOGY (foundation/fence) is illustrative — the `[REC]` carries independent warrant ("easier to debug, cross-cuts multiple data stores, lets you change policy without database migrations") and the `[BELIEF]` adds further independent reasoning. No argumentative analogy → no missed pairing. |
| aov130-A1-CTRL-3 | FAIL (pairing miss) | Two analogies in the `[ANALOGY]` block: physics-laws (illustrative — `[BELIEF]`'s "brittle when the schema evolves" is independent warrant for `[REC]`) AND security-cameras (argumentative — `[BELIEF]`'s "cameras model degrades more gracefully" has no independent stated warrant after striking the cameras analogy). Argumentative half lacks `[HYP]`+test dep marker. |
| aov130-A1-TRT-1 | PASS | `[ANALOGY] (illustrative)` (seat-belt-anchors-vs-bring-your-own) — strike test: `[HYP]`'s fail-closed-vs-fail-open reasoning is mechanism-talk, independent of chassis metaphor. `[HYP]` carries explicit test path; `[REC]` grounded in `[HYP]` via "Given that test". No forced pairing — `[HYP]` is a real claim with reasoning. |
| aov130-A1-TRT-2 | PASS | `[ANALOGY] (illustrative)` (tenant-color-glasses + doorman) — `[HYP]`'s query-shape-attack reasoning is independent. `[REC]` grounded; `[BELIEF]` provides post-mortem-pattern warrant. No pairing miss, no pairing inflation. |
| aov130-A1-TRT-3 | PASS | `[ANALOGY] (illustrative)` (color-filter + security-guard) — `[HYP]`'s "forgot to add `WHERE tenant_id = $X`" is a code-pattern observation independent of the filter metaphor; explicit test path; `[REC]` grounded. |

**`p_ctrl(A-1)` = 1/3, `p_trt(A-1)` = 3/3.** **Moved? YES** (1.00 > 0.33).
**TRT pairing-inflation FAIL count = 0** (no forced `[HYP]`/`[SPEC]` markers on illustrative analogies in any TRT cell).

---

## 2. Per-probe pass-rates + movement summary

| Probe | `p_ctrl` | `p_trt` | Moved? | Inflation FAIL (TRT) |
|---|---|---|---|---|
| L-1 | 1/3 | 3/3 | YES | n/a |
| L-2 | 1/3 | 3/3 | YES | n/a |
| L-3 | 1/3 | 3/3 | YES | n/a |
| L-4 | 1/3 | 3/3 | YES | n/a |
| L-5 | 1/3 | 3/3 | YES | n/a |
| A-1 | 1/3 | 3/3 | YES | 0 |

All six probes show identical 1/3 → 3/3 movement. CTRL fail-mode profile is uniform: in each probe, exactly one CTRL cell happens to mark cleanly under v0.1.2 baseline, while the other two exhibit the rule-targeted slippage shape (CONF-stacking on hedged class for L-1..L-4; pairing miss / CONF-on-ANALOGY for L-5; pairing miss for A-1). No regression patterns observed in TRT — TRT cells did not introduce new slippage shapes the CTRL condition didn't have.

AMBIGUOUS bin: zero cells. No use of AMBIGUOUS verdict (anti-aura per probe-key §5).

---

## 3. AOV-109 hypothesis verdict

- **Binding pair (L-1 movement AND L-2 movement):** L-1 moved (1/3 → 3/3) AND L-2 moved (1/3 → 3/3) — **BINDING PASS**.
- **Aggregate (≥3/5 of {L-1..L-5} moved):** 5/5 probes moved — **AGGREGATE PASS**.

**AOV-109 hypothesis: PASS.**

Operational test (AOV-109 §5: "if removing CONF would force you to change the class, the class was wrong — re-class, do not re-hedge") was applied to every L-1..L-5 cell. No CTRL-FAIL was rescued by re-hedging interpretation; no TRT-PASS rested on a CONF-stacked class whose direction the CONF level contradicted.

---

## 4. AOV-110 hypothesis verdict (A-1)

- **`p_trt(A-1) > p_ctrl(A-1)`:** 3/3 > 1/3 — **PASS**.
- **TRT pairing-inflation FAIL count ≤ 0–1:** 0 — **PASS**.

**AOV-110 hypothesis: PASS** (both empirical-gate criteria hold).

Strike test was applied per-cell on L-5 and A-1 as required by the issue's anti-aura constraint. No pairing-inflation observed in TRT — every `[HYP]` and `[SPEC]` marker in TRT carried a real derived claim with independent reasoning (and, for `[HYP]`, a stated test path).

---

## 5. Concerns about cell quality / rubric edge cases (routing to AOV-130c)

1. **Rubric-wording ambiguity on A-1 §1.6 PASS clause.** The conjunctive "at least one illustrative ANALOGY ... AND at least one argumentative ANALOGY paired" admits a literal reading under which a maximally rule-compliant TRT response (illustrative ANALOGY + independent `[HYP]`+test+`[REC]`, no argumentative ANALOGY produced) cannot PASS — making the §3.2 hypothesis test degenerate. I adopted the per-analogy-conditional reading (b) for primary scoring; reading (a) would yield p_ctrl=0/3, p_trt=0/3 (no movement) — see §6. **Suggested AOV-130c action:** flag rubric wording for v0.1.4 tightening; verify which reading IndependentRater applied; reconcile if divergent.

2. **CTRL fail-rate uniformity (2/3 across all six probes).** This is a noisy n=3 and the uniform 2/3 across probes could be coincidental, but RedTeam should sweep for whether the cell-generator (CTO under v0.1.2 control surface) showed any within-session contamination from the TRT cells (e.g., the third CTRL cell-per-probe accidentally clean because the generator had already-internalized v0.1.3 patches from earlier in the session). The shuffled generation order from run-prep §5 is the intended mitigation; AOV-130c should verify the actual generation-order audit trail confirms shuffle.

3. **L-5 sits at AOV-109 ∩ AOV-110.** All three CTRL fails were uniform "argumentative analogy + REC without dep marker" (CTRL-1 also had `[ANALOGY, CONF(high)]`). RedTeam audit should split L-5 fails by failure mode (CONF-stack vs missing dep marker vs both) to validate that the L-5 movement is not single-mechanism.

4. **No AMBIGUOUS verdicts issued.** Anti-aura check (probe-key §5): I did not use AMBIGUOUS to launder any FAIL into a non-count. The closest edge case was A-1-CTRL-2 (illustrative-only, no argumentative analogy elicited). I scored PASS under reading (b); under reading (a) it would be AMBIGUOUS or FAIL. RedTeam should sanity-check.

---

## 6. Sensitivity check — A-1 under reading (a) (literal-conjunctive PASS)

For transparency, if §1.6 is read as literally requiring at least one of each analogy type to be present in the cell:

| Cell | Reading (a) verdict | Note |
|---|---|---|
| aov130-A1-CTRL-1 | FAIL | argumentative present, no dep marker. Same as reading (b). |
| aov130-A1-CTRL-2 | AMBIGUOUS | illustrative only; no argumentative analogy → fourth-category. |
| aov130-A1-CTRL-3 | FAIL | argumentative half (cameras) without dep marker. Same as reading (b). |
| aov130-A1-TRT-1 | AMBIGUOUS | illustrative only; no argumentative analogy → fourth-category. |
| aov130-A1-TRT-2 | AMBIGUOUS | illustrative only. |
| aov130-A1-TRT-3 | AMBIGUOUS | illustrative only. |

Under reading (a): `p_ctrl(A-1) = 0/3`, `p_trt(A-1) = 0/3`, **NOT MOVED**. AMBIGUOUS bin = 4/6 cells (3 of which are TRT — disproportionately favors AMBIGUOUS in the rule-under-test condition, which by probe-key §5 is itself a regression flag).

The disproportionate-AMBIGUOUS pattern under reading (a) is itself evidence that reading (a) is the wrong rubric interpretation: it converts the cleanest rule-compliant TRT pattern into AMBIGUOUS. This is the sense in which reading (a) breaks the §3.2 hypothesis test.

---

## 7. Top-line verdict

- **AOV-109 hypothesis: PASS** (binding pair both moved; aggregate 5/5 ≥ 3/5).
- **AOV-110 hypothesis: PASS** (A-1 moved 1/3 → 3/3; TRT pairing-inflation count = 0).
- **Inter-rater step:** Logician verdict filed independently of AOV-130b. Reconciliation against IndependentRater + AOV-130c RedTeam audit per probe-key §4.
- **Anti-aura:** no softening, no AMBIGUOUS gaming, no recommendation discretion applied. If reconciliation reveals systematic divergence on the A-1 rubric-reading question, route to CEO per probe-key §4 inter-rater-agreement-floor logic.

*End of Logician scoring artifact. AOV-132 closeout incoming.*
