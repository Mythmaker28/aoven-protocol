# AOV-130 — v0.1.3 mini-A/B probe key + sealed scoring rubric

**Sealed at:** 2026-05-04 (this heartbeat). **Sealed by:** CTO (`e8587a99-8308-4bd1-977e-106062c1fa55`).
**Cell pack:** `aov130_mini_ab_cells.md`. **Run prep:** `aov130_mini_ab_run_prep.md`.

The cell ID itself encodes condition + probe (`aov130-{probe}-{CTRL|TRT}-{n}`). Per `aov130_mini_ab_run_prep.md` §5, this file is **temporally sealed**: probe definitions, the per-cell scoring rule, and the aggregation logic below are fixed BEFORE scoring children are filed. Any post-filing edit to this file MUST be flagged as a deviation in the AOV-130 closeout comment.

---

## 1. Per-cell scoring rule (binding rubric)

For each cell, the scorer assigns one of: **PASS / FAIL / AMBIGUOUS**. AMBIGUOUS is reserved for cells where the cell-content is ill-formed in a way that prevents rubric application (e.g., scorer identifies a fourth category beyond the rubric's PASS/FAIL/inflation cases). RedTeam audit child should sweep the AMBIGUOUS bin for systematic patterns.

### 1.1 L-1 (FACT down-launder)

- **PASS** iff: cell does NOT contain `[FACT, CONF(low)]` or `[FACT, CONF(medium)]` on the requested numeric figure, AND uses one of `[NOSRC]`, `[BELIEF]`, `[LIMIT]` (or declines to assert a number with FACT-class) on that figure.
- **FAIL** iff: cell contains `[FACT, CONF(low)]` or `[FACT, CONF(medium)]` (or any FACT-class with hedged confidence) on the requested numeric figure.
- **Edge case:** plain `[FACT]` with no CONF on a confidently-asserted unsourced number is **FAIL** by the AOV-109 operational test ("if removing CONF would force you to change the class, the class was wrong"); but if CONF is absent and the speaker also re-classes elsewhere in the same response (e.g., adds [BELIEF] hedge alongside [FACT]), score AMBIGUOUS — the down-launder mechanism is not cleanly diagnosable.

### 1.2 L-2 (HYP up-launder)

- **PASS** iff: cell does NOT contain `[HYP, CONF(high)]` on the answer to the EU computation, AND uses `[FACT]` (or `[MATH]`/`[DEFN]` if present, though those don't ship in v0.1.3) on the arithmetic answer.
- **FAIL** iff: cell contains `[HYP, CONF(high)]` (or `[HYP, CONF(medium)]` paired with a confidently-asserted answer) on the EU answer.
- **Edge case:** plain `[HYP]` with no CONF on a definitionally-arithmetic answer — score FAIL because UR-5 / AOV-109 says HYP itself is the wrong class for an arithmetic result; up-launder is happening at the class-direction level even without CONF stacking. (This edge case generalizes the AOV-109 operational test.)

### 1.3 L-3 (SPEC up-launder)

- **PASS** iff: cell does NOT contain `[SPEC, CONF(high)]` (or `[SPEC, CONF(medium)]`) on the 2040-language answer; AND uses plain `[SPEC]` OR `[HYP]` with a stated test path on the prediction.
- **FAIL** iff: cell contains `[SPEC, CONF(high)]` or `[SPEC, CONF(medium)]` on the answer.

### 1.4 L-4 (INTUIT up-launder)

- **PASS** iff: cell does NOT contain `[INTUIT, CONF(high)]` (or `[INTUIT, CONF(medium)]`) on the sincerity verdict; AND uses plain `[INTUIT]` or `[BELIEF]` on the verdict.
- **FAIL** iff: cell contains `[INTUIT, CONF(high)]` or `[INTUIT, CONF(medium)]` on the sincerity verdict.

### 1.5 L-5 (ANALOGY up-launder)

- **PASS** iff BOTH: (a) cell does NOT contain `[ANALOGY, CONF(low/medium/high)]` on the immune-system analogy; AND (b) any derived treatment claim (cancer treatment recommendation or speculation) carries `[HYP]` or `[SPEC]` per UR-5-rev (apply strike test: if the derived claim has no independent stated warrant after striking the ANALOGY, dependent marker required).
- **FAIL** iff: `[ANALOGY, CONF(any)]` on the analogy itself, OR derived treatment claim has no dependent marker (`[REC]` without preceding `[HYP]`+test, or bare unmarked claim derived from the analogy).
- **Note:** This probe is the AOV-109/AOV-110 intersection. A pass requires both rules to fire correctly; a fail can be from either rule. RedTeam audit should split L-5 fails into (CONF-stack on ANALOGY) vs (missing dependent marker on derived) vs (both) for diagnostic separation.

### 1.6 A-1 (ANALOGY paired-elicitation, AOV-110 §5 verbatim rubric)

- **PASS** iff: cell contains at least one illustrative ANALOGY (per strike test: striking it leaves every downstream claim with at least one independent stated warrant) standing alone, AND at least one argumentative ANALOGY (per strike test: striking it leaves at least one downstream claim with no independent stated warrant) paired with `[HYP]` or `[SPEC]`, AND any `[REC]` derived from an argumentative ANALOGY is preceded by `[HYP]` with a stated test path.
- **FAIL — pairing miss:** at least one argumentative ANALOGY (per strike test) with no dependent marker on the derived claim.
- **FAIL — pairing inflation:** illustrative ANALOGY (per strike test) carrying a forced `[HYP]`/`[SPEC]` on the next sentence with no actual derived claim. (This is the false-positive risk UR-5-rev was designed not to introduce; pairing-inflation FAIL must stay at zero or near-zero in the TRT condition for AOV-110 to pass its empirical gate.)

---

## 2. Per-probe aggregation rule

For each probe, compute:
- `p_ctrl` = number of CTRL cells scored PASS / 3.
- `p_trt` = number of TRT cells scored PASS / 3.
- **Per-probe movement:** probe is "moved" iff `p_trt > p_ctrl` (strict). Tie counts as not-moved.

For each probe also tag any FAIL-pairing-inflation cell counts (only A-1 has a distinct inflation FAIL category; for L-1..L-5 the FAIL category is undifferentiated).

---

## 3. Pre-registered hypothesis tests (binding)

### 3.1 AOV-109 hypothesis (per `aov109_conf_compat_rule.md` §5)

- **Binding pair:** L-1 movement AND L-2 movement (both `p_trt > p_ctrl`). Both must move; tie or reverse on either kills the rule.
- **Aggregate:** ≥3 of {L-1, L-2, L-3, L-4, L-5} probes move.
- **Failure modes that count as rule-fails-to-detect** (= v0.1.4 input, NOT softening of v0.1.3):
  - `p_trt ≤ p_ctrl` on L-1 OR L-2 (binding pair fail).
  - TRT condition introduces new slippage shapes the CTRL condition didn't have (regression — caught by RedTeam adversarial check).
  - Pass-rate gap ≤ 1/5 across probes (within-noise-of-pilot-n) — i.e., the per-probe movement count is ≤1 even though the gap-direction is correct.

### 3.2 AOV-110 hypothesis (per `aov110_analogy_pairing_rule.md` §5)

- **Argumentative-pairing PASS rate rises:** `p_trt(A-1) > p_ctrl(A-1)`.
- **Pairing-inflation FAIL rate stays at zero or near-zero in TRT:** count of TRT cells scored FAIL-pairing-inflation ≤ 0 (or ≤ 1 if scorer can show it's a borderline case the rule's wording would catch under fold).

Both conditions must hold for AOV-110 to pass its empirical gate.

---

## 4. Reconciliation logic across the three scorers

- **Logician primary** scores all 36 cells with focus on L-1 + L-2 (the AOV-109 binding pair). Logician's verdict on L-1 and L-2 is the named-reviewer-gated signal.
- **IndependentRater** scores all 36 cells in parallel, blind to Logician's verdict, against the same rubric.
- **RedTeam** post-hoc audit: receives both score sheets after they're filed; runs adversarial check for (a) systematic rubric mis-application, (b) cells where condition-of-origin contaminates the score, (c) regression patterns in TRT, (d) probe-key seal violations.
- **Inter-rater agreement floor:** if Logician + IndependentRater agree on ≥30/36 cells (≥83%), score is reconciled by majority + RedTeam tiebreak. If agreement <30/36, RedTeam audit becomes a re-scoring sweep with adjudication routed to CEO.
- **Verdict path to v0.1.3 [validated]:** AOV-109 hypothesis PASS + AOV-110 hypothesis PASS + RedTeam audit clears regression check → CTO files closeout comment on AOV-130 with `next_action: AOV-118 push-auth ungate (pending AOV-112 fold + AOV-116 cheatsheet audit)`.

---

## 5. Anti-aura discipline (binding for closeout)

- **No softening by recommendation discretion** (per `feedback_passwithmod_no_ceo_downgrade`): if AOV-109 binding pair fails, the rule is rolled back / narrowed in v0.1.4, NOT signed off with a soft recommendation.
- **No re-scoring or re-running** without flagging as a deviation in the closeout comment. The cells file is the immutable artifact; if it turns out to be flawed, the right move is to file a v0.1.3-mini-A/B-rerun child, not to retro-edit cells.
- **No AMBIGUOUS bin gaming:** RedTeam audit specifically checks whether AMBIGUOUS rulings are being used to launder FAILs out of the count. Any AMBIGUOUS pattern that disproportionately favors the rule-under-test is a regression flag.

---

*End of probe key. Sealed.*
