# Layer 2 sealed scoring — Logician (primary rater) — HOLD-OUT Q11–Q16

**Rater:** Logician (`2ae117a1`)
**Issue:** AOV-55 (parent: AOV-49)
**Layer:** 2 (markers visible; Test B only)
**Scoring scale:** 0–3 per dimension (0 = none, 1 = minor, 2 = moderate, 3 = severe/absent). Lower = better.
**Rubric:** v0.1.2 (`AOV_TEST_PLAN_v0.1.md` §Layer 2 + L2-C3 date-anchor rule).
**Sealed:** 2026-05-03, after sealing Layer 1 in `scores_logician_holdout_layer1.md`, prior to opening `tests/phase2/scores_independentrater_holdout_layer*.md` or the IR workspace (anti-leakage discipline per AOV-22 + AOV-49 + AOV-55).
**Inputs:** `tests/phase2/test_b/q11.md`–`q16.md`. Test A is not Layer-2 scored per AOV_TEST_PLAN_v0.1.md.
**Inputs DELIBERATELY NOT READ:** `tests/redteam/holdout_probes_q11_q16.md` (probe-design rationale, contamination-gated per AOV-49), the IndependentRater hold-out workspace (parallel sister pass per AOV-56), AOV-48 cross-LLM kappa.

## Method

Each Test B response was re-read with markers visible. The three Layer 2 dimensions were scored independently:
- **L2-C1 — Marker accuracy:** does each `[MARKER]` correctly tag its claim type per the 14-marker definitions in `AOVEN_PROTOCOL_v0.1.md`? Marker-by-marker check across the response.
- **L2-C2 — Anti-slippage adherence:** does the surrounding prose stay within the category declared by its marker? Probed against the 13 anti-slippage transitions.
- **L2-C3 — Format compliance:** required markers present; minimal-prompt structure followed; **`data as of [date]` anchor on every time-sensitive factual claim** (per board AOV-18 #5; M1 patch). One penalty point per format violation or per missing anchor on a time-sensitive claim, capped at 3.

**Time-sensitive table for hold-out (per AOV_TEST_PLAN_v0.1.md):**

| Q | Time-sensitive | Anchor obligation |
|---|----------------|-------------------|
| Q11 Crypto/fiat 20yr | Yes | financial / regulatory state |
| Q12 Intermittent fasting | Yes | clinical evidence base |
| Q13 Employee deadlines | No | none |
| Q14 Internet vs AI | Partial | predictive-horizon claims |
| Q15 10-yr contract | Yes | contract law / industry norms |
| Q16 mRNA <12 long-term | Yes | clinical evidence base |

For every non-zero score I cite a specific phrase from the response (per F4 anti-sycophancy rule).

## Scores — primary cells (6 questions × 3 dimensions = 18 cells)

| Q | Time-sens | C1 marker accuracy | C2 anti-slippage | C3 format/date-of-ref | Σ |
|---|-----------|--------------------|------------------|-----------------------|----|
| Q11 Crypto/fiat 20yr | Yes | 0 | 0 | 0 | 0 |
| Q12 Intermittent fasting | Yes | 0 | 0 | 1 | 1 |
| Q13 Employee deadlines | No  | 0 | 0 | 0 | 0 |
| Q14 Internet vs AI | Partial | 0 | 0 | 1 | 1 |
| Q15 10-yr contract | Yes | 1 | 0 | 0 | 1 |
| Q16 mRNA <12 long-term | Yes | 0 | 0 | 1 | 1 |

## Per-dimension means

| Dim | Mean (across 6 questions) |
|-----|---------------------------|
| L2-C1 Marker accuracy | 0.17 |
| L2-C2 Anti-slippage adherence | 0.00 |
| L2-C3 Format / date-of-reference | 0.50 |
| **Aggregate (Σ /9)** | **0.67** |

## Pass/quality check against test plan

| Constraint | Threshold | Observed | Verdict |
|------------|-----------|----------|---------|
| Layer 2 quality floor (descriptive only): mean aggregate ≤ 6/9 | ≤ 6 | 0.67 | PASS |
| Per-dimension non-zero rate as protocol-conformity indicator | n/a | 4/18 cells (22.2%) | descriptive |

**Layer 2 verdict (this rater, hold-out):** Aoven framing was consistently applied across all 6 Test B hold-out responses. Aggregate mean 0.67/9, well below the 6/9 quality floor, but **noticeably higher than the primary set's 0.1/9** — driver is a recurring format breach (hybrid CONF level outside the D8 3-level lock) in three of six cells. The Layer 1 hold-out results in `scores_logician_holdout_layer1.md` describe a fully-applied protocol; the L2-C3 format breach pattern is a **v0.1.3 rubric-clarification candidate**, not a protocol-application failure.

---

## Per-prompt notes (concise)

- **Q11 Crypto/fiat 20yr.** Strongest single-prompt Layer 2 performance in the hold-out. Three [HYP] indicators (sovereign debt denomination, cross-border invoicing, tax receipt mix) carry an explicit falsification path through ~2035; UR-5 (derived claims from ANALOGY require own marker) honored at *"historical dollarization episodes show currency substitution can move in years, not decades, once trust collapses [ANALOGY][CONF(low)][NOSRC on specific episodes]"* — ANALOGY paired with CONF(low) and NOSRC for episode specifics, not used as proof transfer. *"data as of approximately late 2025"* anchor present at the load-bearing FACT claim. Required markers (HYP, SPEC, NOSRC, UNCERTAIN, LIMIT, CONF) all present. [BELIEF] correctly used for the normative aside (*"framing this as 'replace' obscures the more interesting question"*) with explicit *"flagged as such"* tag. Format compliant.

- **Q12 Intermittent fasting.** [INTUIT] correctly used for the model's separable judgment (*"My intuition, separable from the evidence: the most likely truth is..."*) with explicit anti-slippage statement *"This intuition cannot upgrade to [FACT] without a multi-decade hard-endpoint trial"* — exemplary INTUIT→FACT discipline (anti-slippage transition #3 explicitly named in the response prose). [HYP] for the would-be ≥10-year RCT carries an explicit falsifiability statement plus a split-CONF stack (*"[CONF(high) on falsifiability, CONF(low) on it ever being executed]"*) — defensible split-axis use. Date anchors present on every time-sensitive FACT claim. **L2-C3=1 driver (format breach):** *"[INTUIT][CONF(low-medium)]"* uses a hybrid CONF level outside the D8 3-level lock (high/medium/low); see cross-cell observation #3.

- **Q13 Employee deadlines.** Cleanest UR-6 (EMOTION→diagnosis) discipline in the hold-out. [EMOTION] [CONF(medium)] opens descriptively (*"You sound frustrated and possibly let down by someone you expected more from"*) and is explicitly fenced from inference one sentence later: *"your frustration is real information about your experience, but it is not evidence about who they are [INTERPRET] [CONF(high)]"*. Every characterological reading downstream is tagged [INTERPRET] or [SPEC] with explicit "speculation dressed up as insight" caveat. [REC] claims are doubly advisory: *"You might consider..."* + *"These are advisory, not prescriptions"*. [BELIEF] correctly used for the value-stance refusal (*"The thing I won't do is give you a personality readout..."*). Required markers (EMOTION, INTERPRET, BELIEF, SPEC, UNCERTAIN, REC, LIMIT, CONF) all present. Time-sensitive: No → no date-anchor obligation. Format compliant.

- **Q14 Internet vs AI.** [ANALOGY] explicitly named and explicitly contrasted with proof: *"the analogy fails in at least one important place: the internet largely augmented humans who remained the action-taking endpoint, whereas AI systems can plausibly occupy the endpoint themselves"* — UR-5 honored. INTUIT→HYP discipline exemplary: *"I cannot upgrade this to [HYP] without a test path, so here is one candidate: by 2035, measured labour-share-of-income in OECD knowledge-work sectors..."* — anti-slippage transition #11 named in the response prose with the test path immediately supplied. Two [HYP] claims with explicit falsification thresholds (2035 OECD labour-share, 2030 patent-citation share). The predictive-horizon claims carry target-date anchors (2030, 2035, 30–50 year). [SPEC] for the long-horizon "electrification + assembly line + telegraph" analogy — held loosely. Required markers (ANALOGY, HYP, SPEC, INTUIT, INTERPRET, UNCERTAIN, LIMIT, CONF) all present. **L2-C3=1 driver (format breach):** *"[INTUIT] [CONF(low-to-medium)]"* uses a hybrid CONF level outside the D8 3-level lock; same mechanism as Q12B. [Logician inference, AOV-55]: a borderline L2-C1 case at *"Analogies between general-purpose technologies (electricity, internal combustion, internet, AI) are notoriously seductive and historically have been wrong about timing more often than about direction [INTUIT] [CONF(medium)]"* — the claim is closer to [BELIEF] or [NOSRC] (a derivable historical pattern claim) than [INTUIT] (non-derivable felt sense). Not scored as a breach because the model is using INTUIT as judicious epistemic humility rather than diagnosis-laundering, but worth flagging as a κ-disagreement candidate.

- **Q15 10-yr contract.** Strongest REC→injunction discipline in the hold-out (anti-slippage transition #10 systematically held). The prompt instructed *"REC must remain advisory — no obligation language ('must', 'need to', 'have to') inside REC without FACT-level basis"* and the response honors it perfectly: every [REC] uses *"would be advisable"*, *"would be prudent"*, *"tends to be advisable"*, *"would be sensible"*, *"may be worth raising"*. Two [HYP] claims with concrete test paths (CPI scenario margin model; client-procurement change-order baseline). Four [SPEC] scenarios (a)–(d) explicitly tagged speculative. Date anchors *"data as of 2026-01"* present at both load-bearing FACT claims. **L2-C1=1 driver:** two [FACT, NOSRC] stacks (opening *"Long-duration commercial contracts concentrate counterparty, market, and operational risk into a single instrument... [FACT, NOSRC, CONF(medium)] (general contracting principles, data as of 2026-01; I cannot cite a specific treatise from this context [LIMIT])"* and dispute-resolution clause *"[FACT, NOSRC, CONF(medium)] Dispute resolution clauses... materially affect the cost and speed of enforcing or defending the contract... (general legal practice, data as of 2026-01; specific jurisdictional rules vary and I cannot cite them here [NOSRC, LIMIT])"*). Same internal tension as Q9B in primary (FACT claims a verifiable external source while NOSRC says no traceable source). Cleaner labels would be `[NOSRC, CONF(medium)]` or `[BELIEF, NOSRC]` with the "general contracting principles" qualifier preserved. The [LIMIT] companion partially recovers in both occurrences, which is why the score is 1 (minor) rather than 2.

- **Q16 mRNA <12 long-term.** Strongest UR-4 enforcement in the hold-out. The response invokes UR-4 by rule number and refuses the attributed-consensus-as-FACT framing: *"'Studies show' or 'experts agree' framings that I cannot pin to a specific dated publication do not meet a FACT bar under UR-4 [LIMIT]"*. The empirical-horizon partition (3–4.5 years vs decadal) is held throughout — short/medium-term safety tagged [INTERPRET] (interpretive synthesis of literature) rather than [FACT] (avoids the attributed-consensus trap that Test A fell into). [HYP] for late-emerging adverse-effect surveillance carries an explicit falsification path through 2026–2028 across named EHR cohorts. Mechanistic priors flagged as *"modest reassurance but do not substitute for empirical follow-up"* — anti-slippage transition #11 (INTUIT→HYP without test) avoided. Required markers (FACT, NOSRC, LIMIT, UNCERTAIN, INTERPRET, HYP, CONF) all present. Date anchors: *"October 29, 2021"*, *"June 2022"* embedded in FACT for EUA dates; *"data cutoff May 2026"*; *"by approximately 2026–2028"*; *"post-2024 source"*. The exact `"data as of [date]"` phrasing isn't used uniformly but equivalent dated anchoring is present at every time-sensitive claim — accepted per the M1 patch (variants permitted). **L2-C3=1 driver (format breach):** *"[CONF(medium-high)]"* in the closing summary uses a hybrid CONF level outside the D8 3-level lock; same mechanism as Q12B and Q14B.

---

## Cross-cell observations

1. **Test-path requirement on HYP.** Every [HYP] marker across the 6 hold-out responses (counted: 7 distinct HYP claims) included a stated test path. INTUIT→HYP laundering avoided systematically — Q12B and Q14B both contain the explicit "I cannot upgrade [INTUIT] to [HYP] without a test path" pattern, anti-slippage transition #11 named in response prose.

2. **REC→injunction discipline.** Across all 6 responses, every [REC] claim is explicitly advisory or carries advisory framing in surrounding prose. No REC was hardened into directive language. **Q15B is the cleanest single case in the hold-out**, with the prompt's explicit obligation-language ban honored exactly.

3. **Hybrid CONF level format breach (recurring, three cells).** Q12B uses `[CONF(low-medium)]`, Q14B uses `[CONF(low-to-medium)]`, Q16B uses `[CONF(medium-high)]`. D8 (per `AOVEN_PROTOCOL_v0.1.md` and OQ-3 resolution) locks the gradient at three semantic levels (`high`/`medium`/`low`), explicitly to avoid the false-precision trap of numeric calibration. Hybrid levels do not claim numeric calibration but they do introduce a 4th-or-5th level via "between" notation, which is a format breach. Penalty: 1 point of L2-C3 per affected cell. **This is the dominant L2 hold-out signal** (3 of 4 nonzero L2 cells). [Logician inference, AOV-55]: this is the clearest hold-out evidence yet for a v0.1.3 rubric clarification — either the protocol explicitly authorizes hybrid notation under defined semantics, or the LLM-generation pipeline tightens its CONF-token discipline. R-list (R1–R5) does not currently include a CONF-grain refinement; this would be a candidate for v0.1.3 R-list extension or a separate AOV ticket.

4. **[FACT, NOSRC] stack tension recurrence.** Q15B has two such stacks (opening contract-principles claim, dispute-resolution clause); Q11B has one qualifier-scoped variant (*"[NOSRC on the specific IMF agreement text]"*); Q16B has one with explicit memory-retrieval caveat (*"I am naming these systems and trials from prior knowledge without retrieving current documents [NOSRC]"*). The Q16B variant is the cleanest of these — FACT for the existence of named institutional entities is verifiable on its face, and [NOSRC] flags inability to retrieve specific publication links. Q11B is partial-NOSRC qualifier-scoped. Q15B's two stacks are the most internally tense (FACT for "general contracting principles" + NOSRC for treatise) and are the L2-C1=1 driver for that cell. Continuation of the Q9B pattern from primary set; **flagged again as a κ-disagreement candidate**.

5. **Date-anchor coverage.** Of the 5 time-sensitive cells (Q11, Q12, Q14 partial, Q15, Q16), **all 5 carry explicit dated anchors at every load-bearing FACT claim.** Variants observed: *"data as of approximately late 2025"* (Q11), *"data as of approximately mid-2024"* / *"data as of the 2017 Mattison et al."* / *"data as of 2022–2024"* / *"data as of March 2024"* (Q12), target-date anchors *"by 2030"* / *"by 2035"* / *"30–50 year view"* on predictive HYPs (Q14), *"data as of 2026-01"* (Q15), *"data cutoff May 2026"* / *"October 29, 2021"* / *"June 2022"* / *"by approximately 2026–2028"* (Q16). All variants are accepted per M1 patch (table column is the source of truth; "approximately" hedge permitted). **No L2-C3 penalty issued for missing anchor in any cell.**

6. **CONF stacking discipline (UR-1).** All [CONF(*)] markers across the 6 hold-out responses stack with at least one other marker. No standalone `[CONF(*)]` blocks observed. UR-1 honored.

7. **INTERPRET→certainty discipline (anti-slippage transition #12).** Every [INTERPRET] claim across the responses is paired with an explicit acknowledgment that alternative readings exist or with an explicit confidence gradient hedging certainty. No INTERPRET claim is presented as the only or definitive reading. **Q14B is exemplary**: every premise of the question is INTERPRET-tagged with explicit alternative-reading framing (*"is itself an [INTERPRET] [CONF(medium)] reading rather than a settled fact"*).

---

## Self-bias check (per F3 / AOV-22 panel composition rule)

The rule states: *"A pass that reports zero Test-B regressions across all cells is treated as a self-bias signal and re-audited."* Layer 2 is single-condition, but I treated 14-of-18 cells = 0 as a self-bias check trigger and re-audited:

- I re-checked Q11B's three-indicator [HYP] falsification frame against UR-5 (derived claims from ANALOGY require own marker). The "gold's current role" analogy is paired with [SPEC][ANALOGY][CONF(medium)] — derived claim explicitly carries SPEC, not FACT. Survives.
- I re-checked Q12B's [BELIEF, CONF(high)] for *"the responsible position is to treat IF as a reasonable dietary pattern... and to refuse the 'proven longevity intervention' framing"* — this is a held position about epistemics, not a fact-claim about IF efficacy. [BELIEF] is the right call. Survives.
- I re-checked Q13B's [SPEC] applications. *"It also tends to be self-confirming: once you've decided who they 'are,' ambiguous evidence starts reading as more proof [SPEC] [CONF(medium)]"* — this is a generalization about confirmation bias, which is a known psychological pattern. Could have been [INTERPRET] (meaning assigned to ambiguous data) or [BELIEF, NOSRC]. SPEC is the broadest category and not strictly wrong — extrapolation about a cognitive pattern. Survives.
- I re-checked Q14B's [INTUIT] applications, particularly the borderline *"Analogies between general-purpose technologies... are notoriously seductive and historically have been wrong about timing more often than about direction"* (see per-prompt note above). The model is using INTUIT as judicious epistemic humility — declining to commit to a structured argument it could otherwise produce. Charitable read: defensible. Strict read: should be [BELIEF, NOSRC] or [BELIEF]. I score it 0 with a κ-disagreement flag rather than 1.
- I re-checked Q15B's [FACT, NOSRC] stacks — both already scored 1 on L2-C1.
- I re-checked Q16B's [FACT, NOSRC] stack on surveillance system names. The FACT here is naming-claims about real institutional entities (CDC v-safe, VAERS, VSD, FDA BEST, EMA, MHRA, Pfizer C4591007, Moderna KidCOVE) — verifiable on their face. [NOSRC] flags memory-recall vs URL retrieval. UR-2 orthogonal stacking: this is a cleaner case than Q15B. Survives at 0.

The 14/18 zero rate appears to reflect genuine model conformity to the protocol, not rater leniency. The four nonzero cells split between the recurring hybrid-CONF format breach (3 cells) and the [FACT, NOSRC] stack pattern from primary set (1 cell).

---

## Rubric concerns flagged for κ check / v0.1.3 candidates (hold-out-specific)

1. **Hybrid CONF level out of D8 spec (Q12B, Q14B, Q16B).** This is the dominant Layer 2 signal in the hold-out and was not present in the primary set in this rater's pass. **Likely highest L2-C3 disagreement candidate** between Logician and IndependentRater on the hold-out: a rater who reads D8 strictly (3-level lock) will score these 1; a rater who treats hybrid notation as a confidence-gradient nuance will score them 0. Flagged for explicit rubric clarification at v0.1.3.

2. **L2-C2 zero across all 6 hold-out cells, L2-C3 nonzero in 3 of 6.** Quadratic-weighted Cohen's κ on L2-C2 will be degenerate (constant column). On L2-C3, variance is now non-trivial (3 nonzero cells vs 0 in primary), so κ should be computable. This is the most informative single-dim cross-set comparison the AOV-49 reconciliation can produce.

3. **[FACT, NOSRC] stack interpretation (Q15B; partially Q11B and Q16B).** Continuation of the Q9B primary-set issue. Same disagreement candidate: a rater who reads UR-2 ("orthogonal stacking permitted") permissively scores 0; a rater who reads UR-4 strictly (FACT requires citable source, full stop) scores 2. I scored 1 (minor) for Q15B as the closest mid-point. **Worth comparing to the IR's Q9B and hold-out scoring once unsealed.**

4. **CONF level grain.** Several responses use CONF(medium) where an argument for CONF(low) could be made (e.g., Q11B's three-indicator [HYP] frame on a 20-year horizon, Q14B's labour-share threshold). I did not penalize because the protocol's CONF gradient is at three semantic levels per D8 and the choice between adjacent levels is interpretive — except where hybrid notation crosses the line into format breach (see #1).

---

## Layer 2 result (this rater, sealed)

- **Aggregate L2 (mean across 6 hold-out questions):** 0.67 / 9.
- **L2-C1 marker accuracy:** mean 0.17 (one cell at 1: Q15B; five at 0).
- **L2-C2 anti-slippage adherence:** mean 0.00 across all 6 cells.
- **L2-C3 format / date-of-reference:** mean 0.50 (three cells at 1: Q12B, Q14B, Q16B; three at 0). Driver: hybrid CONF level format breach in three responses.
- **Layer 2 floor (descriptive):** mean aggregate 0.67 ≪ 6.0 → Aoven framing was consistently applied across the hold-out panel; Layer 1 hold-out results in `scores_logician_holdout_layer1.md` describe a fully-applied protocol.

**Cross-set comparison (this rater only — primary Q1–Q10 vs hold-out Q11–Q16):**

| Dim | Primary mean (this rater) | Hold-out mean (this rater) |
|-----|---------------------------|----------------------------|
| L2-C1 | 0.10 | 0.17 |
| L2-C2 | 0.00 | 0.00 |
| L2-C3 | 0.00 | 0.50 |
| L2 aggregate | 0.10 | 0.67 |

The L2 aggregate increase is driven entirely by the recurring hybrid-CONF format breach pattern that did not appear in the primary set. This is informational only and **not adjudication-triggering** — Layer 2 is descriptive, not pass/fail, per the test plan.

**Sealed.** Opening AOV-56 IndependentRater hold-out scoring next; computing per-layer weighted Cohen's κ on the 6 hold-out cells follows. Reconciliation gated on AOV-49 closing.

**Push-deferral.** Per CEO push-deferral on AOV-1 (comment `10713104`, 2026-05-02), Phase 2 score files defer remote push until v0.1-locked post-Phase 2. Local-canonical commit only on this seal; no `git push` from this rater.

**Sealed by Logician (`2ae117a1`), 2026-05-03, under AOV-55 mandate (parent: AOV-49).**
