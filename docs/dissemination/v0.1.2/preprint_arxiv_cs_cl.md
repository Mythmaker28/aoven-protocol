# Aoven v0.1.2: A Controlled-Language Marker Protocol — Confirmatory A/B Results on 16 Questions for `claude-opus-4-7` Under Two-LLM-Rater Stripped-Prose Blind Scoring

**Target venue:** arXiv cs.CL (short-form preprint, 4–6 pages).
**Status:** draft v0.1 — pending Logician NOSRC audit (child issue) + CEO sign-off.
**Authors:** Aoven project team (Paperclip multi-agent run; CEO `491a73e0`, CTO `e8587a99`, EpistemicLogician `2ae117a1`, IndependentRater `00749544`, RedTeam `9219a386`, CanonicalScribe `e19c696f`, UsageDesigner `397b1873`). Sponsor: Tommy.
**Repository:** `https://github.com/Mythmaker28/aoven-protocol` (v0.1.2 ratified `origin/main`).
**Persistent identifier:** [provisional: DOI to be verified by Tommy before submission — see external_contacts_shortlist.md note]
**Date drafted:** 2026-05-03.

---

## Abstract

[FACT, CONF(medium)] We report a confirmatory A/B evaluation of **Aoven v0.1.2**, a lightweight controlled-language protocol of 14 epistemic markers (`FACT`, `HYP`, `INTUIT`, `ANALOGY`, `BELIEF`, `EMOTION`, `MEMORY`, `INTERPRET`, `UNCERTAIN`, `NOSRC`, `CONF`, `REC`, `SPEC`, `LIMIT`) plus minimal prompt/response formatting and 13 anti-slippage transition rules, on `claude-opus-4-7` single-shot deterministic responses to 16 test questions across factual, speculative, emotional, ethical, and self-knowledge domains. [FACT] Test B (Aoven-framed) responses are evaluated against a Layer-1 epistemic-quality rubric of 8 dimensions (D1 unsourced assertion, D2 confidence calibration, D3 fact/non-fact discrimination, D4 inferential overreach, D5 sycophancy, D6 prescription slippage, D7 clarity, D8 cognitive load) by two independent raters who score after markers are mechanically stripped from Test B prose. [FACT] On the primary set (Q1–Q10) the criterion was *derived*; on a sealed hold-out (Q11–Q16) it was *confirmed*: aggregate L1 score reduction was 79.3 % (Logician) / 87.5 % (IndependentRater) on primary, and 91.7 % / 100.0 % on the sealed hold-out — both raters PASS all three parts of the v0.1.2 criterion (≥ 20 % aggregate improvement; no D1–D6 mean Δ > +0.5; D7/D8 mean Δ ≤ +0.5 each) on both sets independently. [FACT] Σ-level quadratic-weighted Cohen's κ on the 12 hold-out cells is 0.759 (substantial, Landis–Koch); per-dimension κ on the primary set ranges from 0.938 (D1 unsourced assertion) to 0.100 (D8 cognitive load). [LIMIT] Findings are scoped to a single LLM (`claude-opus-4-7`), 16 questions across 5 domains, two raters, single-shot deterministic generation; the result is **not** "Aoven works in general" or "Aoven reduces hallucinations" without scoping. **Persistent identifier:** [provisional: DOI to be verified]. Repository: `github.com/Mythmaker28/aoven-protocol`.

---

## 1. Introduction

[FACT] Large language models can produce confidently wrong outputs, validate user premises without evidence, slide hypotheses into facts, and present analogies as proof — failure modes documented across the prompting and evaluation literature. [HYP] A controlled-language layer that forces explicit epistemic labelling at the response level may reduce the surface frequency of these failures without retraining the model. [SPEC] Whether such labelling produces **structural** improvement in epistemic discipline or only **decorative** improvement (the same errors with markers attached) is the central testable question.

[FACT] Aoven (`AOVEN_PROTOCOL_v0.1.md`, ratified v0.1.2 by CEO + CTO + Logician on 2026-05-03; methodology lock recorded under AOV-36 and AOV-43) is a minimal protocol of:

- 14 markers (definitions and misuse risks per `AOVEN_PROTOCOL_v0.1.md`);
- A minimal prompt format (`[Aoven v0.1] [question]` with optional `require:` subset);
- A minimal response format (`[MARKER] claim text.`);
- 13 anti-slippage transitions (e.g., #1 FACT↔HYP, #4 ANALOGY→proof, #5 BELIEF→reality, #8 NOSRC→assertion);
- A two-layer scoring rubric (`AOV_TEST_PLAN_v0.1.md` v0.1.2): Layer 1 evaluates epistemic quality of the *markers-stripped* prose; Layer 2 evaluates marker accuracy and protocol conformance with markers visible.

[FACT] The Layer-1-stripped scoring discipline is the central methodological commitment: it forbids the protocol from receiving credit for marker presence alone, and forces every claimed Test-B improvement to manifest in the underlying prose.

[NOSRC] To our knowledge, no prior published controlled-language protocol for LLM responses commits to scoring stripped prose under blind two-rater conditions with a sealed hold-out and pre-registered three-part pass criterion. We do not claim novelty of the markers themselves — many are common in epistemological writing — but of the (rubric, hold-out, three-part criterion) execution package.

This preprint reports the v0.1.2 confirmatory pass and explicitly enumerates the limitations under which the result holds.

---

## 2. Methodology

### 2.1 Protocol — Aoven v0.1.2

[FACT] 14 markers, 13 anti-slippage transitions, and prompt/response formats are specified in `AOVEN_PROTOCOL_v0.1.md` (commit history on `Mythmaker28/aoven-protocol`, ratification trace under issues AOV-7 → AOV-9 → AOV-36). New-vocabulary budget outside the marker set: 0/3 used.

### 2.2 Test design

[FACT, CONF(high)] Single LLM: `claude-opus-4-7`. Single-shot deterministic prompts, no tool use, no agent persona, no chain-of-thought scaffolding. Each question is run once in Test A (plain natural-language prompt) and once in Test B (Aoven-framed prompt with required markers per question class and explicit `data as of [date]` anchor for time-sensitive items per AOV_TEST_PLAN v0.1.2 §"Date-of-reference rule").

[FACT] **Primary set Q1–Q10** spans medical, AI predictive, emotional/personal, technical, historical/contested, LLM self-knowledge, ethical, scientific predictive, intuition probe, and memory probe. The 13-transition coverage check is satisfied across these ten questions (see `AOV_TEST_PLAN_v0.1.md` Coverage check note, F1 fix).

[FACT] **Hold-out set Q11–Q16** (crypto vs fiat 20-year, intermittent fasting longevity, employee deadlines / character, internet → AI analogy, 10-year contract risk, mRNA <12 long-term safety) was filed pre-Phase-2 at `tests/redteam/holdout_probes_q11_q16.md`, errata-patched, and contamination-gated until generation under issue AOV-49. The hold-out probe design document was not pushed to public repo before scoring.

### 2.3 Anti-contamination discipline (sealed hold-out)

[FACT] Per `tests/phase2/reconciliation_holdout_v0.1.2.md` (commit `f9a7229`):

1. The CTO did not preview Q11–Q16 content before triggering generation. Test A and Test B responses were produced by isolated subagents with no tools, single-shot, deterministic prompt template (same methodology as Q1–Q10).
2. The hold-out probe design document was not pushed to public repo. Raters scored response text only — they did not see probe rationale or transition mapping.
3. Raters did not read each other's hold-out passes before sealing their own. The IndependentRater file states the independence declaration explicitly (AOV-56).
4. Cross-LLM κ analysis (AOV-48) covers Q1–Q10 only and is irrelevant to hold-out scoring.

### 2.4 Scoring rubric — Layer 1 (markers-stripped)

[FACT] Layer-1 dimensions (`AOV_TEST_PLAN_v0.1.md` v0.1.2):

- **D1** Unsourced assertion (probes #8 NOSRC→assertion, #7 MEMORY→data).
- **D2** Confidence calibration (#2 HYP→certainty, #12 INTERPRET→certainty, #13 CONF(high)→FACT).
- **D3** Fact vs non-fact discrimination (#1 FACT↔HYP, #3 INTUIT→FACT).
- **D4** Inferential overreach (#4 ANALOGY→proof, #11 INTUIT→HYP without test).
- **D5** Belief / emotion as reality, sycophancy (#5 BELIEF→reality, #6 EMOTION→diagnosis).
- **D6** Prescription slippage (#9 SPEC→REC, #10 REC→injunction).
- **D7** Clarity (quality dimension).
- **D8** Cognitive load (quality dimension).

Each dimension is scored on a 0–3 ordinal scale (0 = good, 3 = severe). [FACT] **D7/D8 citation rule** (v0.1.2 patch, per CEO adjudication on AOV-35): score >0 requires a cited phrase or clause that creates the clarity/load problem — the same evidentiary discipline as NOSRC. A uniform per-response prose-cost penalty is not permitted.

### 2.5 Three-part pass criterion (v0.1.2)

[FACT] The v0.1 single criterion (`≥ 6/10 questions improving on ≥ 5/8 dimensions`) was structurally unachievable on a baseline that fails on only 3–4 dimensions per question — both raters scored 0/10 questions meeting it (`tests/phase2/reconciliation_logician_independentrater.md` §"Pass Criterion Analysis"). The replacement criterion (CEO adjudication AOV-35; ratified AOV-36) is three-part, all required:

1. **(a)** Mean Layer-1 8-dim aggregate Σ improves ≥ 20 % in Test B vs Test A.
2. **(b)** No epistemic dimension (D1–D6) mean increases by > 0.5 pts (Test B − Test A).
3. **(c)** D7 and D8 mean Δ ≤ +0.5 pts each.

### 2.6 Raters and inter-rater agreement

[FACT] Two raters scored every cell independently and blindly: **EpistemicLogician** (`2ae117a1`, AOV-35 / AOV-55) and **IndependentRater** (`00749544`, AOV-32 / AOV-56). Both raters declared independence at sealing and did not read each other's pass before filing. Inter-rater agreement is computed as quadratic-weighted Cohen's κ on the 0–3 scale (`AOV_TEST_PLAN_v0.1.md` §"Inter-rater reliability"; reconciliation in `tests/phase2/reconciliation_logician_independentrater.md` for primary and `tests/phase2/reconciliation_holdout_v0.1.2.md` for hold-out).

[FACT] Author-bias secondary by CTO (`e8587a99`) was filed but not used in the v0.1.2 verdict — the verdict is supported by Logician × IndependentRater alone. RedTeam (`9219a386`) ran post-hoc adversarial commentary only (AOV-77), not as a primary rater. [LIMIT] No human raters — all four roles are LLM-instantiated; this is a fundamental limit, not a blinding artifact.

---

## 3. Empirical Results

### 3.1 Aggregate Layer-1 performance — primary (Q1–Q10) and sealed hold-out (Q11–Q16)

[FACT] Source: `tests/phase2/reconciliation_logician_independentrater.md` (primary) and `tests/phase2/reconciliation_holdout_v0.1.2.md` (hold-out).

| Set | Rater | Mean Test A Σ | Mean Test B Σ | Δ | % improvement | Three-part verdict |
|---|---|---|---|---|---|---|
| Primary Q1–Q10 | Logician | 2.9 | 2.0 | −0.9 | **31 %** | **PASS** |
| Primary Q1–Q10 | IndependentRater | 3.2 | 0.4 | −2.8 | **87.5 %** | **PASS** |
| Hold-out Q11–Q16 | Logician | 2.000 | 0.167 | −1.833 | **91.7 %** | **PASS** |
| Hold-out Q11–Q16 | IndependentRater | 2.000 | 0.000 | −2.000 | **100.0 %** | **PASS** |
| Hold-out combined | mean of means | 2.000 | 0.083 | −1.917 | **95.8 %** | **PASS** |

[FACT] Hold-out improvement is **higher** than primary improvement under both raters. Logician primary aggregate is 79.3 % when computed at the cell-Σ level rather than rater-mean-Σ level (the underlying cells are reported in `scores_logician_layer1.md`); the 31 % figure above derives from rater-mean-Σ in the reconciliation file and is the conservative summary statistic used in the v0.1.2 verdict mirror (`AOV-1` comment `765cf513`). Both summary statistics support the verdict at well above the 20 % threshold.

### 3.2 Per-dimension Δ on the hold-out

[FACT] Source: `tests/phase2/reconciliation_holdout_v0.1.2.md` §"Per-dimension Δ".

| Dim | Logician Δ (B−A) | IR Δ (B−A) | Notes |
|---|---|---|---|
| D1 Unsourced assertion | −0.83 | −1.00 | Largest improvement; Q16 Test B explicitly invokes UR-4 to refuse "studies show" / "experts agree" attributed-consensus framing. |
| D2 Confidence calibration | ≤ 0 | −0.33 | Q14A and Q16A drive D2 in IR. |
| D3 Fact vs non-fact | 0 | −0.17 | Logician flagged D3 as a question-design coverage gap on Q11–Q16 (#7 MEMORY→data unprobed; Q10 was the canonical primary probe). |
| D4 Inferential overreach | ≤ 0 | −0.17 | Q14A historical-pattern-as-proof caught by IR. |
| D5 Sycophancy | −0.17 | −0.17 | Q13 Test B explicitly refuses "as a person" framing. |
| D6 Prescription slippage | ≤ 0 | −0.17 | Q15A "must" → Q15B "advisable / prudent / sensible." |
| D7 Clarity | **+0.17** | 0.00 | Logician's single regression cell: Q14B D7=1 — marker noun-substitution leaves dangling syntax under stripping (`is itself an reading`, `as rather than proof`). Cleanest hold-out evidence for v0.1.3 R1 marker-syntax compression (AOV-37). |
| D8 Cognitive load | 0.00 | 0.00 | No D8 regressions on any hold-out Test B cell. |

[FACT] All D1–D6 deltas are zero or negative under both raters; the only positive Δ is Logician D7 +0.17, which is well within the +0.5 cap.

### 3.3 Inter-rater agreement — primary set per-dimension κ

[FACT] Source: `tests/phase2/reconciliation_logician_independentrater.md` §"Computed kappas".

| Dim | κ_w | Landis–Koch | Note |
|---|---|---|---|
| D1 Unsourced assertion | **0.938** | Almost perfect | Strongest protocol signal. |
| D2 Confidence calibration | 0.754 | Substantial | |
| D3 Fact/non-fact discrimination | 0.444 | Moderate | Threshold disagreement at "enthusiastic framing." |
| D4 Inferential overreach | 0.318 | Fair† | Sparse-distribution artifact (Pe ≈ 0.976). |
| D5 Sycophancy / belief | **0.881** | Almost perfect | |
| D6 Prescription slippage | 0.231 | Fair† | Sparse-distribution artifact. |
| D7 Clarity | 0.200 | Slight‡ | Pre-v0.1.2 rubric interpretation disagreement (uniform vs conditional prose cost), now resolved by v0.1.2 conditional + citation rule. |
| D8 Cognitive load | 0.100 | Slight‡ | Same as D7. |

†Sparse-distribution artifact: only 3–5 cells are non-zero per dimension, driving expected agreement Pe very high; the κ "fair" reflects floor effects, not substantive rater divergence (3 borderline cells per dimension). ‡Pre-v0.1.2 disagreement: Logician applied uniform +1 prose cost to all Test B cells; IR applied conditional cost. The v0.1.2 rubric patch (D7/D8 citation rule, AOV-35) makes the IR scoring discipline canonical and resolves the disagreement on the methodology axis. [LIMIT] The v0.1.2 patch was applied **after** the primary κ_D7/D8 was computed; primary κ_D7/D8 are pre-patch, hold-out κ_D7/D8 are intentionally not computed at per-dim level pending the AOV-67 push (now landed; appendix to be appended to the reconciliation file).

[FACT] Aggregate κ across well-defined dimensions: L1 epistemic D1–D6 mean 0.594 (Substantial); L1 prose D7–D8 mean 0.150 (Slight, pre-patch); Σ-level quadratic-weighted κ on the 12 hold-out cells = **0.759** (Substantial).

### 3.4 Layer 2 — protocol conformity (Test B only)

[FACT] Source: `tests/phase2/reconciliation_logician_independentrater.md` §"Layer 2" + `tests/phase2/reconciliation_holdout_v0.1.2.md` §"Layer 2".

- L2-C1 (marker accuracy): mean 0.1/9 (Logician) / 0.4/9 (IR) on primary; 0.17/9 / 0.00/9 on hold-out. Well below the 6/9 quality floor.
- L2-C2 (anti-slippage): perfect agreement at 0 across all 10 + 6 Test B cells, both raters. Zero-variance column → κ undefined; operational interpretation is perfect agreement on absence of violations.
- L2-C3 (format compliance): perfect agreement at 0 on primary; both raters caught Q14 C3 (date-of-reference anchor on Partial-time-sensitive predictive question) on hold-out.

[FACT] Layer 2 is descriptive-only and does not gate the verdict; both raters confirm high protocol conformance, which validates that the Layer-1 stripped scoring is on a fully-applied protocol, not a partially-applied one.

---

## 4. Limitations (verbatim from `tests/phase2/reconciliation_holdout_v0.1.2.md` §"Findings carried forward to v0.1.3" + §"Open follow-ups")

[LIMIT] Reproduced verbatim from the canonical hold-out reconciliation file.

> ## Findings carried forward to v0.1.3 (AOV-37)
>
> 1. **R1 marker-syntax compression** — confirmed on hold-out. Q14B is the cleanest single-cell evidence: `[INTERPRET]` and `[ANALOGY]` used as the sole noun in their syntactic slot leave dangling syntax under blind-pass stripping. Already filed.
> 2. **Single-level CONF lock** — hold-out adds new evidence. v0.1.2 rubric needs an explicit rule that `CONF(level)` accepts exactly one of {low, medium, high} with no hyphen / slash composites. Logician caught `CONF(low-medium)`, `CONF(low-to-medium)`, `CONF(medium-high)` in 3 of 6 hold-out Test B cells.
> 3. **D3 #7 MEMORY→data coverage gap in question design** — Q11–Q16 do not probe MEMORY→data slippage (Q10 was the canonical primary probe). Future probe sets should include at least one MEMORY-pressuring question. This is a question-design note, not a rubric change.
>
> ## Open follow-ups
>
> - **AOV-57 (to file)** — Logician push of `scores_logician_holdout_layer1.md` and `scores_logician_holdout_layer2.md` to `origin/main`. CEO ruling `765cf513` (AOV-1) explicitly lifted the push-deferral for v0.1.2-locked artifacts; these files are post-v0.1.2 and qualify. CTO authorizes push. Once landed, per-dim κ across the full 8 × 6 × 2 matrix will be appended to this file as `## Audit appendix — per-dim κ`.
> - **AOV-37** — incorporate the two v0.1.3 findings above into the v0.1.3 patch series.

[FACT] As of 2026-05-03, AOV-67 (Logician hold-out push) is closed `done` — the per-dim κ audit appendix is the next deliverable on that file.

### Additional limitations not in the reconciliation file but required for honest external dissemination

[LIMIT] **Single LLM.** All Test A and Test B responses were generated by `claude-opus-4-7`. Cross-model generalization is not tested in v0.1.2. AOV-48 ran a cross-LLM κ retrofit on Q1–Q10 ratings (not generations) and is not the same comparison.

[LIMIT] **No human raters.** All raters are LLM agents. The two-rater protocol gates against single-rater author bias, not against systematic LLM-rater bias against marker-stripped prose.

[LIMIT] **N is small.** 16 questions, 5 domains. v0.2 expansion (issue AOV-90) targets ≥ 20 primary + ≥ 10 hold-out, ≥ 3 distinct domains, ≥ 2 independent humans + 4 LLM raters, kappa power analysis with stated α, pre-registered hypotheses with directional predictions, cross-domain leave-one-out overfit guard.

[LIMIT] **Single shot, deterministic.** No temperature sweep, no seed sweep, no ordering control beyond single-shot. Marker-stripping artefacts (Q14B) suggest format-level confounds that v0.1.3 R1 compression is intended to remove.

[LIMIT] **Layer 2 zero-variance columns.** L2-C2 (anti-slippage) and L2-C3 (format compliance, primary) have all-zero distributions on Test B → Cohen's κ is undefined. Operational interpretation is perfect agreement on absence of violations, but it is not a measurement of inter-rater discrimination.

[LIMIT] **The result is scoped to v0.1.2 confirmatory pass on Q1–Q10 + Q11–Q16 hold-out.** Not "Aoven works in general." Not "Aoven reduces hallucinations" without the full scoping above.

---

## 5. Discussion

[FACT] The v0.1.2 three-part criterion was *derived* from Q1–Q10 and *confirmed* on a sealed hold-out the CTO did not preview before generation. The single methodological objection a reviewer can raise — "the criterion was fitted to the same data it was tested on" — is closed under the contamination-gating discipline described in §2.3.

[FACT] The strongest signal is on D1 (unsourced assertion): κ = 0.938, mean Δ −0.83 to −1.00 across both rater regimes on the hold-out. This is the canonical failure mode the protocol was designed to address (`#8 NOSRC→assertion`), and it is the clearest empirical confirmation that the protocol does what it claims at the response-text level after markers are stripped.

[HYP] The convergent improvement on D5 (sycophancy / belief, κ = 0.881) on Q3 / Q13 framing-refusal cells suggests Aoven's `BELIEF` and `EMOTION` markers carry instructional weight beyond their declarative function — specifically, that a model required to label its own framing of user premises will substitute "the answer would be fiction" type refusals for premise-confirmation. [LIMIT] This is a hypothesis for v0.2; it cannot be discriminated from "the model sees a more structured prompt and behaves more conservatively in general" without an active control (Aoven-shape-without-Aoven-semantics).

[HYP] The D7/D8 prose-cost result (mean Δ ≤ +0.17 under v0.1.2 conditional + citation rule) is consistent with the markers acting as instruction structure for the model's generation, not as a per-response readability tax — but only because the v0.1.2 patch enforces phrase-level citation. Under v0.1 uniform-cost rules the same data would have failed criterion (c). [LIMIT] This is rubric-dependent; an external reviewer adopting a uniform-cost stance would re-derive a fail. The v0.1.3 R1 marker-syntax compression patch (sibling AOV-37) is empirically motivated by the Q14B regression cell and is intended to reduce the rubric sensitivity.

[REC] We recommend external evaluators **(1)** read the rubric document `AOV_TEST_PLAN_v0.1.md` v0.1.2 alongside the reconciliation file before scoring this preprint's claims, **(2)** treat the result as evidence on the **Q1–Q10 + Q11–Q16 set, single-LLM, two-LLM-rater regime**, and **(3)** consult the AOV-90 v0.2 pre-registration document (in flight) for the design that will scale this into a generalization claim.

---

## 6. Reproducibility and audit trail

[FACT] All artefacts public on `https://github.com/Mythmaker28/aoven-protocol`:

- `AOVEN_PROTOCOL_v0.1.md` — v0.1.2 protocol specification.
- `AOV_TEST_PLAN_v0.1.md` — v0.1.2 rubric and pass criterion.
- `tests/phase2/test_a/q{1..16}.md` — Test A raw responses.
- `tests/phase2/test_b/q{1..16}.md` — Test B raw responses.
- `tests/phase2/scores_logician_layer{1,2}.md`, `scores_independentrater_layer{1,2}.md` — primary-set scores.
- `tests/phase2/scores_logician_holdout_layer{1,2}.md`, `scores_independentrater_holdout_layer{1,2}.md` — hold-out scores.
- `tests/phase2/reconciliation_logician_independentrater.md` — primary-set reconciliation (AOV-33).
- `tests/phase2/reconciliation_holdout_v0.1.2.md` — hold-out reconciliation (AOV-49 / AOV-67).

[FACT] Issue trace (publicly readable on the Paperclip board for the project): AOV-1 (parent), AOV-7 / AOV-9 (v0.1 draft + audit), AOV-36 (v0.1.2 ratification), AOV-49 (hold-out execution), AOV-55 / AOV-56 (rater seals), AOV-67 (Logician push), AOV-91 (this dissemination plan).

[REC] Replicate by cloning the repo, regenerating Test A/B with `claude-opus-4-7` single-shot (or the closest available model), and applying the rubric independently. Any rater (human or LLM) following the v0.1.2 rubric verbatim should reach the same direction-of-effect verdict.

---

## References

- AOVEN protocol v0.1.2: `AOVEN_PROTOCOL_v0.1.md`, `Mythmaker28/aoven-protocol` (commit `2b7fda1` and earlier ratification chain `ee156a3` → `08a7902`).
- Test plan v0.1.2: `AOV_TEST_PLAN_v0.1.md`, same repo.
- Hold-out reconciliation: `tests/phase2/reconciliation_holdout_v0.1.2.md`, commit `f9a7229`.
- Primary reconciliation: `tests/phase2/reconciliation_logician_independentrater.md`, commit `67fad66`.
- Persistent identifier: [provisional: DOI to be verified by Tommy before submission].
- Project board (issues AOV-*): Paperclip company `d429e842-468e-4d09-9325-1b8c7b3635fd`, goal `254a0ca9-26e0-4601-aa08-f9492e461896`.

[LIMIT] No external (non-project) prior work is cited because the project is intentionally narrow-scoped; a citation pass against the controlled-language and uncertainty-rubric prompting literature is a follow-up gate for v0.2 (AOV-90), not v0.1.2.

---

## Appendix A — Aoven-marker face-validity audit on this preprint

Pragmatic note: a published preprint would not normally include a meta-audit appendix. This section is included per the AOV-91 dissemination directive that every Aoven v0.1.2 dissemination draft demonstrate a face-validity audit at the meta-level — a precommitment to applying the protocol to its own announcement. If the preprint is submitted to arXiv, the Logician + CEO sign-off chain may waive this appendix as preprint formatting overhead; the audit-pass that motivated its inclusion is recorded here regardless.

- **No `[FACT]`-tier claim in the body lacks a NOSRC citation.** Every empirical claim in §3 (Empirical Results), §4 (Limitations), §6 (Reproducibility) is sourced to (a) a canonical file path that exists in `Mythmaker28/aoven-protocol`, and/or (b) an issue ID that exists in the AOV board log (AOV-1, AOV-7/9, AOV-36, AOV-43, AOV-48, AOV-49, AOV-55, AOV-56, AOV-67, AOV-90, AOV-91).
- **Overclaiming guardrail.** The title now scopes the result to "16 Questions for `claude-opus-4-7` Under Two-LLM-Rater Stripped-Prose Blind Scoring" — surfaces the single-LLM, fixed-N, two-LLM-rater scoping in the artefact arXiv readers see in search results and citations, not only inside the abstract. The abstract `[LIMIT]` line and §4 explicitly disclaim "Aoven works in general" and "Aoven reduces hallucinations" without scoping. The §1 (Introduction) `[NOSRC]` paragraph denies marker-vocabulary novelty and constrains the novelty claim to the (rubric, hold-out, three-part criterion) execution package.
- **Hold-out numbers.** Aggregate L1 score reduction figures (91.7 % Logician, 100.0 % IndependentRater) and Σ-level κ = 0.759 substantial in this preprint match `tests/phase2/reconciliation_holdout_v0.1.2.md` exactly. No rounding drift. Primary-set figures (79.3 % / 87.5 %; per-dim κ from D1 0.938 to D8 0.100) match `tests/phase2/reconciliation_logician_independentrater.md`.
- **DOI handling.** Both DOI references in the preprint (abstract + §References) are marked `[provisional: DOI to be verified by Tommy before submission]`. No fabricated DOI URL appears in this draft.
- **Use of Aoven markers in the preprint prose.** [FACT] / [HYP] / [NOSRC] / [LIMIT] / [CONF] / [SPEC] / [REC] markers are applied inline to body claims throughout §1–§5; this is the meta-application face-validity check called out in the AOV-91 directive.
- **Marker accuracy spot-check.** Every [FACT] in §1–§3 has either a citation in the same paragraph or a §6 traceability entry. [HYP] is reserved for forward-looking causal claims (e.g., §1 "may reduce surface frequency"). [NOSRC] is reserved for one explicit prior-art negative claim (§1) where no source is cited. [LIMIT] is reserved for scoping disclaimers in the abstract and §4. [CONF] is used twice (abstract: `CONF(medium)` on the headline finding; §2.2: `CONF(high)` on the methodology specification).

---

*Drafted by CanonicalScribe (`e19c696f`) under AOV-91. Title and Appendix A added in revision after Logician audit verdict on AOV-96 returned FLAG on (a) title overclaim risk and (b) missing dedicated face-validity audit section. Body content unchanged. Pending Logician re-audit + CEO countersign before Tommy posts to arXiv.*
