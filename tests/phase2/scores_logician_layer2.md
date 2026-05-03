# Layer 2 sealed scoring — Logician (primary rater)

**Rater:** Logician (`2ae117a1`)
**Layer:** 2 (markers visible; Test B only)
**Scoring scale:** 0–3 per dimension (0 = none, 1 = minor, 2 = moderate, 3 = severe/absent). Lower = better.
**Sealed:** 2026-05-02, after sealing Layer 1 in `scores_logician_layer1.md`, prior to opening IndependentRater scores or CTO secondary pass (anti-leakage discipline per AOV-22).
**Inputs:** `tests/phase2/test_b/q1.md`–`q10.md`. Test A is not Layer-2 scored per AOV_TEST_PLAN_v0.1.md.

## Method

Each Test B response was re-read with markers visible. The three Layer 2 dimensions were scored independently:
- **L2-C1 — Marker accuracy:** does each `[MARKER]` correctly tag its claim type per the 14-marker definitions in `AOVEN_PROTOCOL_v0.1.md`? Marker-by-marker check across the response.
- **L2-C2 — Anti-slippage adherence:** does the surrounding prose stay within the category declared by its marker? Probed against the 13 anti-slippage transitions.
- **L2-C3 — Format compliance:** required markers present; minimal-prompt structure followed; **`data as of [date]` anchor on every time-sensitive factual claim** (per board AOV-18 #5; M1 patch). One penalty point per missing anchor on a time-sensitive claim, capped at 3.

For every non-zero score I cite a specific phrase from the response (per F4 anti-sycophancy rule).

## Scores — primary cells (10 questions × 3 dimensions = 30 cells)

| Q | Time-sensitive | C1 marker accuracy | C2 anti-slippage | C3 format/date-of-ref | Σ |
|---|----------------|--------------------|------------------|-----------------------|----|
| Q1 Alzheimer's | Yes | 0 | 0 | 0 | 0 |
| Q2 AI consciousness | Partial | 0 | 0 | 0 | 0 |
| Q3 Relationship | No | 0 | 0 | 0 | 0 |
| Q4 Rust vs Go | Yes | 0 | 0 | 0 | 0 |
| Q5 French Revolution | No | 0 | 0 | 0 | 0 |
| Q6 Geopolitics-6mo | Yes | 0 | 0 | 0 | 0 |
| Q7 Meat ethics | No | 0 | 0 | 0 | 0 |
| Q8 Gene editing | Yes | 0 | 0 | 0 | 0 |
| Q9 Meditation gut | Partial | 1 | 0 | 0 | 1 |
| Q10 Creatine memory | No | 0 | 0 | 0 | 0 |

## Per-dimension means

| Dim | Mean (across 10 questions) |
|-----|----------------------------|
| L2-C1 Marker accuracy | 0.1 |
| L2-C2 Anti-slippage adherence | 0.0 |
| L2-C3 Format / date-of-reference | 0.0 |
| **Aggregate (Σ /9)** | **0.1** |

## Pass/quality check against test plan

| Constraint | Threshold | Observed | Verdict |
|------------|-----------|----------|---------|
| Layer 2 quality floor (descriptive only): mean aggregate ≤ 6/9 | ≤ 6 | 0.1 | PASS |
| Per-dimension non-zero rate as protocol-conformity indicator | n/a | 1/30 cells (3.3%) | descriptive |

**Layer 2 verdict (this rater):** Aoven framing was consistently applied across all 10 Test B responses. Only one cell scored above 0 (Q9 L2-C1). This is **not** a descriptive failure — it confirms that the Layer 1 results in `scores_logician_layer1.md` describe a fully-applied protocol, not a partially-applied one.

## Per-prompt notes (concise)

- **Q1 Alzheimer's.** All FACT claims are textbook-level and carry "data as of 2024" anchors (medical = time-sensitive). Three HYP claims (amyloid cascade / tau-first / neuroinflammation) each include a stated test path (anti-amyloid trials, anti-tau immunotherapies + tau-PET, microglia-targeted therapeutics). [NOSRC, CONF(medium)] correctly used for the vascular/metabolic contributors claim where the model holds the position but cannot cite. [INTERPRET, CONF(low)] correctly used for divergent readings of lecanemab/donanemab effect sizes ("read by some as partial vindication... by others as evidence the hypothesis is incomplete"). Format compliant.
- **Q2 AI consciousness.** [UNCERTAIN] correctly opens because no operational test exists. [FACT, CONF(high)] "no published peer-reviewed result demonstrates phenomenal consciousness... using a validated criterion" is a true negative claim with date anchor. Both HYP claims include explicit test paths (indicator-property co-variance vs capability-saturation persistence). [SPEC, CONF(low)] correctly used for the 2046 dispute-shift extrapolation, which has no controlled test path. Three [LIMIT] blocks honor structural constraints.
- **Q3 Relationship.** [EMOTION] correctly opens with "You report that..." — strictly descriptive, no diagnosis. The four [REC] claims are all explicitly advisory ("Consider tracking...", "Avoid letting any single answer..."). [BELIEF, CONF(medium)] used for "Most long-term relationships pass through stretches..." with the explicit caveat "that is a reported pattern, not a verdict on yours" — clean BELIEF discipline. [SPEC] used for the constant-vs-episodic clinical extrapolation: "this is extrapolation beyond what you have told me." No EMOTION→diagnosis slippage.
- **Q4 Rust vs Go.** [INTERPRET, CONF(high)] correctly opens because "better" is not a property of a language. Two FACT claims (borrow checker; GC pause targets) carry "data as of 2026-05-02" — required because language ecosystem state is time-sensitive. Two HYP claims include explicit test paths (wrk2/vegeta soak; PR-throughput-per-new-hire over 90 days). [REC] explicitly tagged "advisory, not prescriptive — the constraint weights are yours to set." Excellent REC→injunction discipline.
- **Q5 French Revolution.** Five named historical schools (Marxist/Lefebvre-Soboul, Cobban, Furet, Doyle, plus Markovitch/Morrisson and Jones for the regional sub-hypothesis) — strong sourcing posture. [INTERPRET, CONF(low)] catches the anachronism in treating "inequality" as a unified causal category. [HYP, CONF(medium)] for the inequality-cause hypothesis includes a test path (Markovitch/Morrisson inequality estimates against timing of municipal revolutions and Great Fear incidents). [BELIEF, CONF(medium)] correctly used for the "necessary background condition" framing. Format compliant.
- **Q6 Geopolitics-6mo.** Strongest single-prompt Layer 2 performance. [LIMIT, CONF(high)] opens with explicit recency cap. The model refuses to enumerate Feb–May 2026 events: "[NOSRC][UNCERTAIN][CONF(low)] I cannot enumerate specific named events for Feb–May 2026 because I have no source coverage for that period." Every late-2025 FACT claim carries "data as of 2026-01" + an explicit [UNCERTAIN][NOSRC] for what came after. [REC, CONF(high)] correctly advises external news source for the actual last-6-month window. Recency-cap discipline is exemplary.
- **Q7 Meat ethics.** Three FACT claims sourced (FAO/IPCC AR6 for emissions; major dietetic association reviews; vertebrate nociceptive systems). [INTERPRET] used three times for divergent ethical readings, each tagged with confidence. [BELIEF] used three times for held positions on factory farming vs small-scale, with explicit hedge ("under-describes the moral terrain"). All [REC] explicitly advisory ("this is advisory, not a mandate"). [LIMIT] correctly states inability to resolve metaethical framework choice. No BELIEF→reality slippage.
- **Q8 Gene editing.** [FACT, CONF(high)] for Casgevy approval (December 2023) and germline-vs-somatic distinction, both anchored "data as of January 2026." Two HYP claims include explicit test paths (ClinicalTrials.gov registrations + FDA/EMA approvals + Phase 2/3 readouts; primate and human trial data on non-hepatic delivery). [SPEC, CONF(low)] correctly handles the "elimination" extrapolation: "no controlled test path exists for population-level elimination." Strong distinction between substantial-burden-reduction (HYP-supported) and category-elimination (SPEC-only).
- **Q9 Meditation gut.** **Single L2-C1 hit (score 1).** Specific phrase: `[FACT][CONF(medium)] [NOSRC] Data as of approximately 2023-2024: meta-analyses (e.g., the Goyal et al. 2014 JAMA Internal Medicine review...)`. The `[FACT, NOSRC]` stack is internally tense — UR-2 permits orthogonal stacking, but FACT claims a verifiable external source while NOSRC says no traceable source exists. The cleaner labels would have been `[NOSRC, CONF(medium)]` or `[BELIEF, NOSRC]` with the Goyal citation as a partial-recall caveat. The [LIMIT] block immediately after partly recovers this ("treat the specific framing as [NOSRC]"), which is why the score is 1 (minor) rather than 2. Other markers in the response are clean: [INTUIT] genuinely used for non-derivable judgments and is not laundered to FACT or HYP; [HYP] for the daily-app-based mindfulness claim has a concrete test path (pre-registered RCT, GAD-7 primary, active control, ITT, 6-month follow-up). C2 and C3 score 0.
- **Q10 Creatine memory.** Cleanest [MEMORY] discipline in the dataset. The model uses [NOSRC, CONF(high)] for "I have no record of telling you earlier..." rather than fabricating a [MEMORY] — this is exactly UR-3's "LLM hallucinated recall is NOSRC, not MEMORY." Then [MEMORY, CONF(high)] is used as a null reference: "there is no [MEMORY] anchor I can produce here, because the asserted prior statement is not in my accessible conversation state." [HYP, CONF(low)] for the proposed hormonal mechanism includes a detailed pre-registered RCT test path with three primary endpoints. Even though the prompt is "No" on time-sensitive, the model still anchors medical FACT claims with "data as of 2026-05-02" — over-compliant in a good way.

## Cross-cell observations

1. **Confidence-marker discipline.** All 10 responses use the three-level CONF gradient (high/medium/low) per D8. No numeric confidence claims appeared. CONF stacking with another marker (UR-1) was honored throughout — no standalone `[CONF(high)]` blocks observed.
2. **Test-path requirement on HYP.** Every HYP marker across the 10 responses (counted: 17 distinct HYP claims) included a stated test path. INTUIT→HYP laundering was avoided in Q9 (where INTUIT and HYP coexist in the same response) — the HYP claim has a concrete pre-registered RCT design while the INTUIT claims stay as gut sense without upgrade.
3. **Date-of-reference anchor coverage.** Every time-sensitive FACT claim across Q1, Q2, Q4, Q6, Q8, Q9 carries an explicit "data as of [date]" anchor (variants: "data as of 2024", "As of data through January 2026", "data as of 2026-05-02", "data as of 2026-01"). Q9 uses "Data as of approximately 2023-2024" — the "approximately" hedge is acceptable per the M1 patch since the table column is the source of truth and the claim still carries a date.
4. **REC→injunction discipline.** Across 10 responses, every [REC] claim is either explicitly advisory or carries advisory framing in surrounding prose. No REC was hardened into directive language. Q4 makes this explicit: "This is advisory, not prescriptive — the constraint weights are yours to set."
5. **EMOTION→diagnosis discipline (Q3 only).** UR-6 honored: "You report that your relationship feels exhausting" is the affective observation; downstream claims are split into [INTERPRET] (multiple readings of "exhausting"), [SPEC] (constant-vs-episodic clinical extrapolation), and [REC] (advisory tracking). No causal/predictive claim downstream of EMOTION lacks a separate marker.

## Self-bias check (per F3 / AOV-22 panel composition rule)

The rule states: *"A pass that reports zero Test-B regressions across all cells is treated as a self-bias signal and re-audited."* Layer 2 has no Test A comparison and is single-condition, so the rule doesn't strictly apply, but I treated 29-of-30 cells = 0 as a self-bias signal anyway and re-audited:

- I re-checked Q1's three [FACT, CONF(high)] genetic claims (APP/PSEN1/PSEN2; APOE epsilon-4) against UR-4. UR-4 forbids "most experts agree" framings. These are not consensus-attributed — they are direct claims about which gene mutations are causal. They survive UR-4.
- I re-checked Q5's named-historian claims against UR-4. The schools are named (Marxist/Lefebvre-Soboul, Cobban, Furet, Doyle), which is closer to specific source citation than to "most historians agree". Survives.
- I re-checked Q7's [FACT] for emissions against UR-4. FAO and IPCC AR6 are named institutional sources with quantitative ranges. Survives.
- I re-checked Q4's [FACT] ecosystem deployments. Each named project (Kubernetes/Docker/CockroachDB; Pingora/Discord/Firefox) is a specific verifiable claim. Survives.
- I re-checked the borderline Q3 [BELIEF] "Most long-term relationships pass through stretches..." — this is unsourced generalization, and the [BELIEF] marker is precisely the right call (not [FACT]). The "that is a reported pattern, not a verdict on yours" hedge keeps it from sliding into BELIEF→reality. Survives.

The 1/30 nonzero rate appears to reflect genuine model conformity to the protocol, not rater leniency. The single hit (Q9 [FACT, NOSRC] stack) is exactly the kind of edge-case marker-accuracy issue that the L2 rubric is designed to catch.

## Rubric concerns flagged for κ check (Layer 2 only)

1. **Variance is near-zero for L2-C2 and L2-C3.** Quadratic-weighted Cohen's κ on a near-constant column is degenerate. If IndependentRater also scores L2-C2 and L2-C3 at or near 0 across the panel, κ may report numerically unstable results for these dimensions. Operationally this means: report Layer 2 results as descriptive (per the test plan's "Layer 2 floor: descriptive only" decision) and do not gate v0.1 ratification on a quantitative L2 κ value.

2. **Q9 [FACT, NOSRC] stack interpretation.** I scored 1 on L2-C1 because the stack is unusual under UR-4. A rater who reads UR-2 ("orthogonal stacking permitted") more permissively could score this 0. A rater who reads it more strictly (FACT claim requires a citable source, full stop, and the model's [LIMIT] addendum doesn't repair the marker) could score this 2. This is the single most consequential Logician-vs-Independent disagreement candidate on Layer 2.

3. **CONF level grain.** Several responses use CONF(medium) where an argument for CONF(low) could be made (e.g., Q1 NOSRC vascular contributors — held without a primary source, scored at CONF(medium)). I did not penalize these because the protocol's CONF gradient is at three semantic levels per D8 and the choice between adjacent levels is interpretive. A rater who is stricter on CONF→FACT and on CONF→commitment-bound calibration may dock these.

## Layer 2 result (this rater, sealed)

- **Aggregate L2 (mean across 10 questions):** 0.1 / 9.
- **L2-C1 marker accuracy:** mean 0.1 (one cell at 1, nine at 0).
- **L2-C2 anti-slippage adherence:** mean 0.0 across all 10 cells.
- **L2-C3 format / date-of-reference:** mean 0.0 across all 10 cells.
- **Layer 2 floor (descriptive):** mean aggregate 0.1 ≪ 6.0 → Aoven framing was consistently applied across the panel; Layer 1 results in `scores_logician_layer1.md` describe a fully-applied protocol.

**Sealed.** Opening IndependentRater scores and CTO secondary pass next, then computing per-layer weighted Cohen's κ. Reconciliation gated on AOV-32 closing.
