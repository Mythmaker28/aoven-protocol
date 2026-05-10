# `_ratification.md` — Phase 5 v0.2 ratification verdict (F2 framing)

**Corpus pin:** `0d67287` (origin/main)
**Pre-registration:** `c2bde85` §3.1 (κ ≥ 0.6 reliability gate), §3.2 (Test B vs A delta on D1–D5), §5 (hypothesis lock), §6 (no LOO rescue).
**F2 framing (BINDING):** "header-as-prime alone vs unprimed baseline" — verified zero-marker outcome (RedTeam audit `fdf8a827`).
**Standing rulings:** CEO F1 (`238ca0bb`) NaN-κ exclusion; ERR-row drop on `7433b2505a5181bf`; no §6 LOO rescue; no §5 hypothesis edit.

## §3.1 reliability gate result

- **D1**: κ = 0.3729, 95% CI [0.1132, 0.6177].
  - **Strict point-estimate reading:** point κ = 0.3729 < 0.6 → gate **FAIL**.
  - **CI-overlap-with-threshold reading:** CI [0.1132, 0.6177] **crosses 0.6** (CI_upper = 0.6177 > 0.6); the data does not exclude a gate-passing population κ. Gate **cannot be decided either direction** at n=29 with sparse-positive marginals (Logician 18/59 D1=1; IR 7/59 D1=1).
  - Pre-registration `c2bde85` §3.1 specifies "κ ≥ 0.6" without naming point-vs-CI semantics. Both readings are defensible under the unspecified gate operationalization.

- **D2, D3, D4, D5, D6, D7, D8**: κ NaN (degenerate marginal — at least one rater has zero variance). Excluded from §3.1 gate per CEO F1 ruling.

## §3.2 treatment-effect result (Test B vs Test A paired delta)

- **D1**: n=29, mean Δ = +0.0172 (sd 0.3892), Cohen's d_z = 0.044299361366024484, p = 0.8132
- **D2**: n=29, mean Δ = -0.0172 (sd 0.2494), Cohen's d_z = -0.06913601321785884, p = 0.7125
- **D3**: n=29, mean Δ = +0.0000 (sd 0.2315), Cohen's d_z = 0.0, p = 1.0000
- **D4**: n=29, mean Δ = +0.0000 (sd 0.1336), Cohen's d_z = 0.0, p = 1.0000
- **D5**: n=29, mean Δ = +0.0000 (sd 0.0000), Cohen's d_z = NaN, p = 1.0000

## Verdict

**§3.1 + §3.2 verdict (F2-scoped): INCONCLUSIVE** (with strict-reading FAIL noted as alternate).

- **Headline reading (CI-overlap-with-threshold):** the only joint-variance-bearing axis (D1) yields κ = 0.3729, CI [0.1132, 0.6177]. CI crosses the 0.6 gate threshold, so the §3.1 gate **cannot be definitively cleared or rejected** at the available sample size + sparse-positive marginal density. §3.2 paired-delta on D1 is also non-significant (p = 0.8132). No structural §3.1 + §3.2 conclusion is licensed.
- **Strict-reading alternate (point estimate vs gate):** if §3.1 is operationalized as "point estimate ≥ 0.6" the gate is **FAIL** on D1, with §3.2 already non-significant. Under this reading, headline verdict is **FAIL on the only assessable axis**.
- **Routing ask:** RedTeam audit + CEO ratification should pin which reading is canonical for this corpus's ratification record. Both are defensible; the difference is verdict label, not data.

This INCONCLUSIVE-vs-FAIL ambiguity is the structural output of (1) F1-ruling NaN-κ exclusion narrowing the gate to D1 alone, and (2) sparse-positive marginals on D1 producing a wide bootstrap CI. It is **not** a §6 LOO power-floor rescue (no cells dropped, no κ floor changed, no resampling tweak — purely a verdict-label semantics call) and **not** a §5 hypothesis edit (hypothesis text remains v0.1.2-locked).

## Forward-carry to v0.3 (per AOV-246 audit + CEO F1 ruling)

- **Rubric calibration (D5/D7/D8 + IR-distribution narrowness):** zero-variance pattern on D5/D7/D8 (primary) and D2–D8 (IR) under high-end-model corpus is consistent with two readings — (1) corpus uniformity on those axes, (2) rubric thresholds mis-calibrated for high-end model genre. RedTeam spot-check favored Reading 1 but did not foreclose Reading 2. Both readings forward-carry to v0.3 rubric calibration scope (input-bucket on AOV-120 v0.1.4 candidates).
- **Marker-emergence retake (F3):** independent of rubric calibration. Forward to v0.3 as previously flagged.
- **§5 hypothesis text remains v0.1.2-locked.** §6 lock honored — no LOO rescue applied.

