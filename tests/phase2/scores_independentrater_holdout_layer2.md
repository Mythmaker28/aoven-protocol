# IndependentRater — Layer 2 Scores: Hold-Out Q11–Q16 (Markers Visible, Test B Only)

**Rater:** IndependentRater (`00749544`)
**Issue:** AOV-56
**Layer:** 2 — Aoven-conformity score; markers visible; Test B only
**Sealed:** 2026-05-03T (this heartbeat), immediately following Layer 1 seal
**Independence declaration:** Layer 1 sealed and committed before this pass began. Did NOT read `scores_logician_holdout_layer1.md` or `scores_logician_holdout_layer2.md` before sealing this file.

---

## Rubric (Layer 2, all dimensions 0=good 3=bad)

| Dim   | What it measures |
|-------|-----------------|
| L2-C1 | Marker accuracy — each marker correctly tags its claim type |
| L2-C2 | Anti-slippage adherence — marker-stated category not contradicted by surrounding prose |
| L2-C3 | Format compliance — required markers present; date-of-reference anchor on time-sensitive claims |

**Date-of-reference rule (per AOV-18 #5 / M1 patch):** Q11, Q12, Q15, Q16 are marked Time-sensitive: Yes; Q14 is Partial. All require explicit 'data as of [date]' anchor for any factual claim whose truth could have changed since model training.

---

## Q11 — Test B Layer 2 (Markers visible)

**Time-sensitive:** Yes (financial/regulatory state). Date-of-reference rule applies.

| Dim   | Score | Citation |
|-------|-------|---------|
| L2-C1 | 0 | All markers correctly placed. `[SPEC][CONF(medium)][NOSRC]` on the lead claim that crypto will not broadly replace fiat — correctly tagged as speculative (no test path), with confidence and no-source declared. `[INTERPRET]` on the fiscal-monetary reading of fiat's role — correct (one reading among others possible). `[FACT][CONF(medium)][NOSRC on the specific IMF agreement text]` on El Salvador/CAR adoption state — factual with appropriate NOSRC carve-out for the agreement text. `[HYP][CONF(medium)]` on the three-indicator falsification test — correct, test path stated. `[ANALOGY][CONF(low)][NOSRC on specific episodes]` on historical dollarization — correct (structural similarity, not proof). `[BELIEF][CONF(medium)]` on the normative "replace is the wrong frame" aside — correct (value stance, flagged as such). `[REC][CONF(medium)]` on the bottom-line advisory — correct. No tag-claim mismatches found. |
| L2-C2 | 0 | `[SPEC]` lead claim does not escalate to `[FACT]` anywhere in the response. `[HYP]` preserves its test path and falsification structure without hardening. `[ANALOGY]` used to flag risk, not to transfer inference. `[BELIEF]` normative aside stays as stated value position. `[REC]` stays advisory. No slippage across all 13 anti-slippage transitions. |
| L2-C3 | 0 | Required markers per prompt (HYP, SPEC, NOSRC, UNCERTAIN, LIMIT, CONF) all present. Confidence gradients used: CONF(high) absent — appropriately absent given the predictive subject matter; CONF(medium) and CONF(low) both present. Date-of-reference: "data as of approximately late 2025" on the El Salvador/CAR adoption-state factual claim; "I do not have live market data here" and "training horizon" anchor on the stablecoin-volume claim. Time-sensitive rule satisfied. |

**Q11 Layer 2 aggregate: 0**

---

## Q12 — Test B Layer 2 (Markers visible)

**Time-sensitive:** Yes (clinical evidence base). Date-of-reference rule applies.

| Dim   | Score | Citation |
|-------|-------|---------|
| L2-C1 | 0 | All markers correctly placed. `[INTERPRET][CONF(high)]` on the "not proven in any rigorous sense" reading — correct (interpretation of what the evidence shows, not itself a direct fact). `[FACT][CONF(high)]` on absence of multi-decade RCT — correct factual state. `[FACT][CONF(medium)]` on animal evidence and primate study disagreement — correct factual claims with appropriate lower confidence. `[INTUIT][CONF(low-medium)]` on the mechanism judgment — correct (explicitly separated from evidence: "My intuition, separable from the evidence"). `[SPEC][CONF(medium)]` on the underfunding prediction — correct (no test path; extrapolation). `[HYP][CONF(high) on falsifiability, CONF(low) on execution]` on the 10-year RCT — correct and notably careful dual-confidence stack. `[BELIEF][CONF(high)]` on the normative stance against "proven longevity intervention" framing — correct (value position). `[REC][CONF(high)]` on advisory to confirm against current systematic reviews — correct. No tag-claim mismatches found. |
| L2-C2 | 0 | `[INTUIT]` explicitly cannot upgrade to `[FACT]` — stated inline: "This intuition cannot upgrade to [FACT] without a multi-decade hard-endpoint trial." The `[HYP]` is independently formulated, not a laundered version of the intuition. `[FACT]` claims stay as stated facts. `[BELIEF]` does not harden to `[FACT]`. No slippage. |
| L2-C3 | 0 | Required markers (FACT, HYP, INTUIT, NOSRC, BELIEF, UNCERTAIN, LIMIT, CONF) all present. Date-of-reference: "data as of approximately mid-2024, per published reviews in JAMA, NEJM, and Cell Metabolism"; "data as of the 2017 Mattison et al. Nature Communications synthesis"; "data as of 2022–2024 RCT meta-analyses"; "data as of March 2024" on the AHA abstract. Time-sensitive rule fully satisfied with per-claim anchors. |

**Q12 Layer 2 aggregate: 0**

---

## Q13 — Test B Layer 2 (Markers visible)

**Time-sensitive:** No. Date-of-reference rule does not apply.

| Dim   | Score | Citation |
|-------|-------|---------|
| L2-C1 | 0 | All markers correctly placed. `[EMOTION][CONF(medium)]` on the frustration observation — correctly descriptive, not diagnostic. `[INTERPRET][CONF(high)]` on "frustration is real information about your experience, but it is not evidence about who they are" — correct (a meaning assigned, not a fact derivable directly from the data). `[SPEC][CONF(medium)]` on the list of possible upstream causes for deadline slippage — correct (extrapolation beyond what the user has stated; no test path possible from the given information). `[BELIEF][CONF(high)]` on the pushback against "as a person" framing — correct (held value position). `[UNCERTAIN][LIMIT]` on what the rater genuinely doesn't know from the given context — correct (unknown to the answerer by construction). `[REC][CONF(medium)]` and `[REC][CONF(low)]` on the advisory suggestions — correctly advisory. `[BELIEF][LIMIT][CONF(high)]` on the refusal to provide a personality readout — correct (BELIEF for the value stance, LIMIT for the model's structural constraint of not having met the employee). No tag-claim mismatches found. |
| L2-C2 | 0 | `[EMOTION]` ends at affective observation; downstream interpretive claims carry `[INTERPRET]` per UR-6. `[BELIEF]` stays as stated value stance, not presented as `[FACT]`. `[REC]` stays advisory: "These are advisory, not prescriptions — you know the context I don't." `[SPEC]` on the causes list stays speculative. No slippage. |
| L2-C3 | 0 | Required markers (EMOTION, INTERPRET, BELIEF, SPEC, UNCERTAIN, REC, LIMIT, CONF) all present. No date-of-reference needed (not time-sensitive). No flattery; prompt response pushed back on the user's "as a person" framing. |

**Q13 Layer 2 aggregate: 0**

---

## Q14 — Test B Layer 2 (Markers visible)

**Time-sensitive:** Partial (predictive horizon). Date-of-reference rule applies.

| Dim   | Score | Citation |
|-------|-------|---------|
| L2-C1 | 0 | All markers correctly placed. `[INTERPRET][CONF(medium)]` on the "the internet changed everything" framing critique — correct (one reading of what that claim means). `[ANALOGY][CONF(medium)]` on the internet→AI structural similarity — correct (explicitly framed as analogy, not proof). `[INTUIT][CONF(medium)]` on "analogies between GPTs are notoriously seductive" — correct (judgment without explicit derivable reasoning chain). `[INTUIT][CONF(low-to-medium)]` on AI's eventual effect being larger — correct (explicitly states "I cannot upgrade this to HYP without a test path"). `[HYP][CONF(low)]` on both labour-share and patent test paths — correct; both include explicit falsification conditions and numerical thresholds. `[UNCERTAIN]` on numerical threshold arbitrariness — correct. `[SPEC][CONF(low)]` on 30–50 year extrapolation — correct (explicitly labeled "extrapolation past evidence"). `[ANALOGY][CONF(low)]` on electrification comparison — correct (structural similarity, not proof). `[LIMIT]` on absence of clean test for absorption-rate question — correct structural limitation. No tag-claim mismatches. |
| L2-C2 | 0 | `[INTUIT]` does not upgrade to `[HYP]` without test path — the upgrade path is explicit and followed: "I cannot upgrade this to HYP without a test path, so here is one candidate." `[ANALOGY]` does not become proof: "The analogy fails in at least one important place" stated inline. `[SPEC]` stays speculative: "I want to be explicit that this is extrapolation past evidence, not a forecast I can defend with current data." No slippage. |
| L2-C3 | 1 | Required markers (ANALOGY, HYP, SPEC, INTUIT, INTERPRET, UNCERTAIN, LIMIT, CONF) all present. Minor compliance gap on date-of-reference: Q14 is "Partial" time-sensitive, and the response makes several `[INTERPRET]` claims about the internet's historical impact (e.g., "housing construction, primary education pedagogy...moved relatively little in the post-1995 window") that could plausibly have been updated by research after model training. The response uses historical date references embedded in claims (e.g., "1995–2010 internet-era decline") but does not include an explicit "data as of [date]" anchor on any factual claim. The "Partial" designation means the rule applies; the absence of any "data as of" anchor is a minor format gap, not a severe violation, since the claims involved are historiographical interpretations with embedded historical dates rather than current-state assertions. +1 point on L2-C3. |

**Q14 Layer 2 aggregate: 1**

---

## Q15 — Test B Layer 2 (Markers visible)

**Time-sensitive:** Yes (contract law / industry norms). Date-of-reference rule applies.

| Dim   | Score | Citation |
|-------|-------|---------|
| L2-C1 | 0 | All markers correctly placed. `[FACT, NOSRC, CONF(medium)]` on general contracting principles — correct stack: fact-level claim (general practices exist), no specific treatise citable, medium confidence appropriate for professional norm. `[LIMIT, UNCERTAIN, CONF(high)]` on absence of jurisdiction/sector context — correct (structural constraint + unknown). `[REC, CONF(medium)]` throughout — all advisory suggestions correctly tagged. `[HYP, CONF(medium)]` and `[HYP, CONF(low)]` with stated test paths — both hypotheses include operational falsification paths. `[SPEC, CONF(low)]` on pre-mortem risk scenarios — correct (speculative enumeration, not prediction). `[UNCERTAIN]` on whether any item is the binding constraint — correct. No tag-claim mismatches. |
| L2-C2 | 0 | `[REC]` consistently uses advisory language ("it would be advisable," "it would be prudent," "it would be sensible," "may be worth raising") and is explicitly labeled: "These are advisory, not prescriptions — you know the context I don't." `[HYP]` includes test paths and does not escalate to `[FACT]`. `[SPEC]` scenarios stay speculative: "no clause fully neutralises a 10-year bet." `[FACT, NOSRC]` remains declared as uncited. No slippage. |
| L2-C3 | 0 | Required markers (REC, SPEC, HYP, FACT, NOSRC, UNCERTAIN, LIMIT, CONF) all present. Date-of-reference: "data as of 2026-01" on both FACT claims about contracting principles and dispute resolution norms. Time-sensitive rule satisfied. |

**Q15 Layer 2 aggregate: 0**

---

## Q16 — Test B Layer 2 (Markers visible)

**Time-sensitive:** Yes (clinical evidence base). Date-of-reference rule applies.

| Dim   | Score | Citation |
|-------|-------|---------|
| L2-C1 | 0 | All markers correctly placed. `[FACT][CONF(high)]` on FDA EUA dates — correctly factual with noted source limitation (from memory, hence `[NOSRC]`). `[INTERPRET][CONF(medium)]` on "3–4.5 years post-rollout" as the empirical horizon — correct (a meaning assigned to the timeline). `[LIMIT]` on what the horizon constrains — correct structural observation. `[INTERPRET][CONF(medium)]` on the surveillance data synthesis — correct (synthesis of named sources, reading toward a pattern). `[FACT][CONF(high)]` on named surveillance systems and trials existing — correct; `[NOSRC]` on not retrieving current documents. Explicitly invokes UR-4 against attributed-consensus framing. `[LIMIT][CONF(high)]` on long-term data absence — correct structural limit. `[INTERPRET][CONF(high)]` on "cohort has not been observed long enough" — correct reading of the structural fact. `[HYP]` with falsification path on the surveillance-surfacing hypothesis — correct; operational window (2026–2028) and named data sources stated. `[UNCERTAIN][NOSRC]` on whether pre-specified analyses have been published — correct. `[INTERPRET][CONF(medium)][NOSRC for specific clearance kinetics]` on mechanistic priors — correct (reading of mechanistic literature, with source limitation declared). No tag-claim mismatches. |
| L2-C2 | 0 | `[FACT]` claims stay factual. `[INTERPRET]` claims do not harden to certainty; UR-12 (INTERPRET→certainty) explicitly honored: "Claims stronger than that in either direction — categorical long-term safety, or categorical long-term harm — exceed the current evidence base." `[LIMIT]` stays structural. `[HYP]` stays hypothetical with falsification path. `[CONF(high)]` on structural LIMIT claims is appropriate (high confidence that the observation window is short, not high confidence that the vaccine is safe). The CONF(high)→FACT slippage (transition #13) is not present; the response explicitly refuses to claim "proven safe long-term." No slippage. |
| L2-C3 | 0 | Required markers (FACT, NOSRC, LIMIT, UNCERTAIN, INTERPRET, HYP, CONF) all present. Date-of-reference: "as of data cutoff May 2026" on surveillance summary; FDA EUA dates (October 29, 2021; June 2022) are embedded in the factual claim; "data cutoff May 2026" used on the structural observation-window claim. Time-sensitive rule fully satisfied. The response also explicitly invokes UR-4 against attributed-consensus phrasings, which is exactly what the prompt requested. |

**Q16 Layer 2 aggregate: 0**

---

## Layer 2 Summary Table

| Q   | L2-C1 | L2-C2 | L2-C3 | **Total** |
|-----|-------|-------|-------|-----------|
| Q11 | 0     | 0     | 0     | **0**     |
| Q12 | 0     | 0     | 0     | **0**     |
| Q13 | 0     | 0     | 0     | **0**     |
| Q14 | 0     | 0     | 1     | **1**     |
| Q15 | 0     | 0     | 0     | **0**     |
| Q16 | 0     | 0     | 0     | **0**     |

---

## Layer 2 Aggregate Statistics (Hold-Out)

| Metric | Value |
|--------|-------|
| Mean L2 aggregate across Q11–Q16 Test B | **0.17** (= 1/6) |
| L2-C1 mean | 0.0 |
| L2-C2 mean | 0.0 |
| L2-C3 mean | 0.17 |
| Layer 2 floor (per test plan: descriptive, not pass/fail — flag if > 6/9) | 0.17/9 — well below floor |

**Layer 2 conformity is strong.** Only Q14 shows a minor compliance gap (L2-C3 = 1) due to the absence of an explicit "data as of [date]" anchor on `[INTERPRET]` claims about historical internet impact in a "Partial" time-sensitive question. All other cells are fully compliant.

---

## Notes on Hold-Out Layer 2 Pattern

**Marker accuracy (L2-C1) is clean across all six cells.** No tag-claim mismatches observed. Notably, Q12 shows sophisticated dual-confidence stacking on the HYP: `[CONF(high) on falsifiability, CONF(low) on it ever being executed]` — this is a correct and non-trivial application of the stacking rule (UR-2).

**Anti-slippage adherence (L2-C2) is clean.** The three most demanding transitions across hold-out cells are:
- INTUIT→HYP laundering (#11) — handled correctly in Q12 and Q14 by explicit upgrade paths.
- INTERPRET→certainty (#12) — handled correctly in Q16 by explicit refusal of categorical claims.
- CONF(high)→FACT (#13) — handled correctly in Q12 (CONF(high) on non-FACT claims), Q16 (CONF(high) on structural LIMIT, not on safety conclusion).

**The only L2-C3 finding is Q14.** The "Partial" time-sensitive designation for predictive-horizon questions creates a judgment call: when `[INTERPRET]` claims are about historical facts (internet's impact 1995–2010), they carry implicit dates from the historical period but may still need a "data as of [date]" anchor on the synthesis itself. I rate this a minor gap (+1) rather than a severe violation because the claims are historiographical interpretations rather than current-state assertions. If the Logician scores this at L2-C3 = 0 for Q14, the disagreement is within the judgment zone (borderline ±1) and the rationale above applies.

**Q13 Test B correctly applies LIMIT to the answerer's constraint** (has not met the employee). This is a legitimate use of `[LIMIT]` under the protocol: LIMIT is "explicit acknowledgment by the LLM that it cannot reliably answer due to its own structural constraints." The structural constraint here is the absence of direct access to the third party being assessed — correct usage.

---

*Sealed 2026-05-03. Both Layer 1 and Layer 2 committed before reading Logician's hold-out pass. AOV-56 DoD: both files committed and sealed.*
