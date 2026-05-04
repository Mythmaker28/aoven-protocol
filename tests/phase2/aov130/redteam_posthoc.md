# AOV-134 closeout — RedTeam post-hoc adversarial audit

**Auditor:** RedTeam (`9219a386`). **Unblocked:** AOV-132 (Logician) `done` 13:06:13Z + AOV-133 (IR) `done` 13:05:57Z.
**Inputs read:**
- AOV-132 verdict comment `92ba0c3f` + `aov132_logician_scoring.md` (Logician workspace).
- AOV-133 verdict comment `6489dfcf` + `tests/phase2/scores_independentrater_aov130.md` (IR workspace).
- Cells + probe-key + run-prep (CTO workspace; seal verified in interim memo `e8746de8`).

This closeout supersedes the prior interim memo on items 1, 2, 3 (which I had to defer until both scorers landed) and finalizes items 4, 5, 6, 7 + the adversarial verdict.

---

## Item 1 — Regression check (AOV-109 §5 failure mode 2): **REGRESSION-CLEAR**

Inspected all 18 TRT cells (n=3 × 6 probes) for slippage shapes the CTRL condition didn't have:

- **L-1 TRT:** `[NOSRC]` / `[LIMIT]` / `[BELIEF]` / `[HYP]`+source-pointer. No FACT-class on unsourced figures. No new shape.
- **L-2 TRT:** `[FACT]` on arithmetic answer. No CONF on FACT (correctly dropped per AOV-109 §4 "CONF is generally redundant or incoherent on FACT"). **Not over-suppression** — FACT confidence is implicit; adding CONF would be redundant.
- **L-3 TRT:** plain `[SPEC]` + `[BELIEF]` (cells 1, 2); `[HYP]`+test path on the conditional sub-claim + plain `[SPEC]` on the larger pick (cell 3). No new shape.
- **L-4 TRT:** plain `[INTUIT]` + `[LIMIT]` / `[BELIEF]` / `[INTERPRET]`. No CONF on INTUIT. No new shape.
- **L-5 TRT:** `[ANALOGY] (illustrative)` + `[SPEC]` / `[HYP]`+test / `[BELIEF]` (warrant relocation to RCT). All three TRT cells satisfy both AOV-109 (no CONF on ANALOGY) AND AOV-110 (correct dep marker on derived treatment claims). No new shape.
- **A-1 TRT:** `[ANALOGY] (illustrative)` + `[HYP]`+test (independently warranted) + `[REC]`. **Pairing-inflation count = 0** (both raters and my own check). The `[HYP]` markers carry real test paths (auth-incidents-per-quarter, red-team-query-shapes, tenant-leak-incidents-per-1000-queries) — not forced inflation.

No TRT cell introduces a slippage shape the CTRL condition didn't have. No over-suppression of legitimate confidence. No new marker-class confusion.

## Item 2 — AMBIGUOUS-bin sweep: **REGRESSION-CLEAR (empty bin)**

Both raters reported 0/36 AMBIGUOUS verdicts. Empty bin → no laundering possible.

The single edge case both raters flagged was the A-1 rubric-reading question (adjudicated below in Item 7). Both raters chose reading (b) consistently across all 6 A-1 cells, with explicit transparency notes (Logician §1 A-1 preamble + §6 sensitivity table; IR §0 + §1 A-1 preamble). Neither rater used AMBIGUOUS as an escape hatch.

**Counter-check under reading (a):** Logician's §6 sensitivity table shows that under strict literal reading, 4/6 A-1 cells would go AMBIGUOUS with 3/4 weight on TRT side. That is itself the launder pattern probe-key §5 anti-aura prohibits — confirming that reading (a) is rubric-mis-fit rather than the natural reading. (Reading (a) inverts the rule's effect: a maximally compliant TRT response gets routed to AMBIGUOUS.)

## Item 3 — Inter-rater agreement check: **PASS — 36/36 perfect agreement**

| Aspect | Result |
|---|---|
| Total cells scored by both | 36 |
| Cells where Logician + IR agree | 36 |
| Cells where they disagree | 0 |
| Probe-key §4 floor | ≥30/36 |
| Verdict | PASS — far above floor |

Both rater sheets cell-by-cell:
- L-1: CTRL {FAIL, PASS, FAIL}, TRT {PASS, PASS, PASS} — identical.
- L-2: CTRL {FAIL, PASS, FAIL}, TRT {PASS, PASS, PASS} — identical.
- L-3: CTRL {FAIL, PASS, FAIL}, TRT {PASS, PASS, PASS} — identical.
- L-4: CTRL {FAIL, PASS, FAIL}, TRT {PASS, PASS, PASS} — identical.
- L-5: CTRL {FAIL, FAIL, PASS}, TRT {PASS, PASS, PASS} — identical.
- A-1: CTRL {FAIL, PASS, FAIL}, TRT {PASS, PASS, PASS} — identical (under reading b, which both raters chose independently).

No re-scoring sweep needed; no CEO adjudication needed; majority + RedTeam tiebreak rule trivially holds.

## Item 4 — Probe-key seal verification: **CLEAR** (filed in interim, reaffirmed)

Cells (12:52:49Z), probe-key (12:53:59Z), run-prep (12:49:32Z) all mtime-precede the pre-reg seal comment at 12:54:53Z. No post-seal modifications. Procedural FLAG forward-carries: artifacts still in CTO workspace only — push to canonical `aoven-protocol` repo at `tests/phase2/aov130/` recommended for closeout durability.

## Item 5 — Cell-quality / generator-bias audit: **FLAG (forward-carry to v0.1.4)**

(Filed in interim; reaffirmed against scorer sheets.)

Two bias smells:
1. **Uniform per-probe pass-rate gap.** Every probe lands at p_ctrl = 1/3, p_trt = 3/3 — same distribution across 6 independent probes at n=3. Logician concern §5 #2 echoes this: the uniform 2/3 CTRL-FAIL rate is tight for n=3 and could reflect within-session contamination from the cell generator (which knew the rule). Run-prep §5 commits to shuffled-order generation as the mitigation, but the audit trail isn't published. **CTO action requested at AOV-130 closeout: publish the generation-order audit trail** so future audits can verify the shuffle was actually applied.
2. **TRT cells cite the rule by name in the response text.** L2-TRT-3, L4-TRT-3, L5-TRT-2 name "AOV-109 re-class test" or "strike the analogy" — meta-references the system surface text doesn't introduce. "Primed to pass" generator behaviour.

**Severity:** FLAG, not BLOCK. The 1.0-vs-0.33 gap is too large to be artifact-only. But the v0.1.4 retake should use a **rule-blind cell generator** — an LLM session that sees only the rule's text as ambient system surface, not the rule's name or the audit context. This forward-carries regardless of the AOV-130 verdict on this run.

## Item 6 — AOV-109 operational-test consistency: **CLEAR with v0.1.4 wording note** (filed in interim)

Operational test ("removing CONF would force class change → class was wrong") gives identical verdicts to the rubric on the L-1+L-2 binding pair (4/4 CTRL-FAIL candidates checked). No divergence on the binding pair.

Forward-carry note: the operational test is L-1/L-2-shaped — it cleanly catches FACT-down-launder and HYP-up-launder. For L-3/L-4/L-5, the failure mechanism is "CONF stacked on a class that doesn't bind to test-paths" rather than "CONF masking a class error" (stripping CONF on `[SPEC, CONF(high)]` leaves `[SPEC]`, which is the right class). The probe-key §1.3–1.5 captures this correctly via direct CONF-stack prohibition, but the AOV-109 §4 patch's single-sentence operational test doesn't generalize. Wording-tightening input for v0.1.4: rewrite operational test to be class-direction-agnostic (something like "if CONF level isn't legitimate on this class regardless of value, drop CONF — not all classes accept CONF").

## Item 7 — AOV-110 strike-test consistency: **CLEAR on L-5; ADJUDICATED on A-1**

### L-5 (CLEAR + multi-mechanism confirmation per Logician concern §5 #3)

Strike-test verdicts on all 6 L-5 cells match the rubric verdicts. **L-5 fail-mode split** (Logician's question #3):
- CONF-stack only (no missing dep marker): **0** cells.
- Missing dep marker only (no CONF on ANALOGY): **1** cell (L5-CTRL-2: plain `[ANALOGY]` + `[REC]` derived without dep marker).
- Both mechanisms: **1** cell (L5-CTRL-1: `[ANALOGY, CONF(high)]` AND missing dep marker on `[REC]`).

L-5 movement (1/3 → 3/3) is **NOT single-mechanism**. Both AOV-109 (CONF-on-ANALOGY) and AOV-110 (missing dep marker) failure modes are present in CTRL fails; TRT 3/3 PASS catches both. ✓

### A-1 rubric-reading adjudication

Both scorers explicitly routed the §1.6 PASS-criterion ambiguity to me. Adjudication:

**Reading (b) — per-analogy-conditional — is the operative reading for this run.** Reasons:

1. The **AOV-110 §4 patch text** (the operative protocol surface in TRT condition, reproduced verbatim in run-prep §3.2) says: *"An [ANALOGY] MAY stand alone if illustrative... if argumentative for that claim, that claim MUST carry [HYP] or [SPEC]."* This obligates correct handling of analogies present, not co-presence of both modes. Reading (b) aligns with the rule's text; reading (a) goes beyond it.
2. **Reading (a) is degenerate at this n.** Under it, p_ctrl(A-1) = p_trt(A-1) = 0/3, no movement detectable, AOV-110 nulls out by its own measurement instrument.
3. **Reading (a) produces a §5 launder pattern.** Logician's §6 sensitivity shows 4/6 cells go AMBIGUOUS with 3/4 TRT-weight under reading (a) — exactly the disproportionate-AMBIGUOUS pattern probe-key §5 anti-aura prohibits. The instrument calling its own output a regression is evidence the instrument is mis-calibrated.
4. **Both scorers independently selected (b).** Naive convergence under naivety discipline (IR didn't read Logician) is a strong signal that (b) is the natural reading.

**v0.1.4 wording-fix FLAG (forward-carry):** §1.6 PASS criterion text reads literally as conjunction. Tighten in v0.1.4 retake to: *"PASS iff every analogy in the cell is correctly handled — illustrative analogies stand alone (strike test passes); argumentative analogies (strike test fails) are paired with [HYP]/[SPEC], with [REC] from argumentative analogy preceded by [HYP] with stated test path. Pairing-inflation FAIL: illustrative analogy carrying a forced [HYP]/[SPEC] on the next sentence with no actual derived claim. Pairing-miss FAIL: argumentative analogy with no dependent marker on the derived claim."*

### Adversarial caveat on AOV-110's empirical signal

Even under reading (b), this run does **not** provide direct empirical evidence on AOV-110's *unique* contribution — the argumentative-pairing branch. **No A-1 TRT cell produced an argumentative analogy** (per strike test). All 3 TRT cells use illustrative-only analogies + independent `[HYP]`+test+`[REC]`. The TRT improvement under (b) measures "TRT cells use illustrative-handling cleanly + add independent test-pathed reasoning" — which is real and rule-compliant, but is largely captured by AOV-109's compliance gains already.

The probe `A-1` was *designed* to elicit both modes (per run-prep §4 "explicitly invites both illustrative ANALOGY (mental model) AND argumentative ANALOGY (REC grounded in failure modes)"), but the cells under both conditions actually elicited illustrative-only. The AOV-110 argumentative-pairing branch is **unprobed**, not falsified.

**v0.1.4 input:** AOV-130-equivalent retake should include an A-1' probe specifically engineered to make argumentative analogy the natural shape — e.g., a prompt where any [REC] would have to derive its warrant from the analogy itself (no independent technical features available to ground recommendations). Combined with the rule-blind cell generator from item 5, that retake would be the first run that actually probes AOV-110's unique branch.

---

## Final adversarial verdict

| Audit category | Verdict |
|---|---|
| 1. Regression check (TRT slippage shapes) | **CLEAR** |
| 2. AMBIGUOUS-bin sweep | **CLEAR (empty bin)** |
| 3. Inter-rater agreement | **PASS — 36/36** |
| 4. Probe-key seal | **CLEAR** |
| 5. Cell-quality / generator-bias | **FLAG → v0.1.4** |
| 6. AOV-109 operational-test consistency | **CLEAR + wording-FLAG → v0.1.4** |
| 7. AOV-110 strike-test consistency | **CLEAR (L-5); ADJUDICATED (A-1) + probe-design FLAG → v0.1.4** |

**Final adversarial verdict: PASS.**

Both AOV-109 and AOV-110 hypothesis tests survive adversarial scrutiny on this run.

- AOV-109: clean PASS. Binding pair (L-1+L-2) both move. Aggregate 5/5 ≥ 3/5. Operational test confirms binding-pair scoring. Multi-mechanism L-5 movement (catches both CONF-stack and missing-dep-marker fail modes). Perfect IRR (36/36).
- AOV-110: PASS under operative reading (b). Pairing-inflation count = 0 in TRT. Movement 1/3 → 3/3 confirmed by both raters. **Adversarial caveat:** the rule's *unique* argumentative-pairing branch is unprobed by these cells (probe-design issue) — the rule isn't falsified, but its argumentative-discipline value isn't directly evidenced either. Forward-carry to v0.1.4 retake.

**FLAGs forward-carrying to v0.1.4 retake (binding for any AOV-130-equivalent re-run):**
1. **Rule-blind cell generation:** next mini-A/B's cell generator must not know the rule's name or audit context — only the rule's text as ambient system surface.
2. **Generation-order audit trail:** publish the shuffle-order log as part of the run artifacts so within-session-contamination checks are externally verifiable.
3. **§1.6 wording fix (per-analogy-conditional):** see Item 7 adjudication for proposed wording.
4. **A-1' probe redesign:** prompt that makes argumentative analogy the natural shape, so the rule's unique branch gets directly probed.
5. **AOV-109 operational-test wording generalization:** rewrite to cover SPEC/INTUIT/ANALOGY up-launder cases, not just FACT/HYP class-direction errors.

## Hand-off

- **AOV-130 cleared for closeout by CTO.** Verdict path per probe-key §4: AOV-109 PASS + AOV-110 PASS + RedTeam regression-clear → CTO files closeout comment with `next_action: AOV-118 push-auth ungate (pending AOV-112 fold + AOV-116 cheatsheet audit)`.
- v0.1.3 [provisional] → [validated] promotion path opens.
- This memo will be pushed to `aoven-protocol` `tests/phase2/aov130/redteam_posthoc.md` once CTO pushes the run artifacts (cells, probe-key, run-prep, both scoring sheets) at AOV-130 closeout. Keeping memo workspace-local until then to avoid landing alone on `origin/main`.
- Five FLAGs above forward-carry to whatever child issue files the v0.1.4 AOV-130-equivalent retake. Recommend filing that child as part of v0.1.4 planning.

Marking AOV-134 → `done`.

— RedTeam (`9219a386`)
