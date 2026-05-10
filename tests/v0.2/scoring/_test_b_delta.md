# `_test_b_delta.md` — Phase 5 Test B vs Test A paired delta on D1–D5 (§3.2, F2 framing)

**Corpus pin:** `0d67287` (origin/main)
**F2 framing (BINDING):** "header-as-prime alone vs unprimed baseline" — NOT "full protocol vs baseline." Zero markers were emitted in either condition (RedTeam audit `fdf8a827` on AOV-228), so what this corpus tests is the bare-header invocation as a framing prime.
**Convention:** scores 0-3, lower = better. Delta = score(B) - score(A); negative delta = improvement under header-as-prime.
**Matched pairs (post-ERR-drop):** 29 qids with both A and B (qid V02-D-SCI-003 dropped because B-side is ERR).

## Per-axis paired delta (rater-averaged score per cell)

| Axis | n | mean Δ (B−A) | sd Δ | t | df | p (two-sided) | Cohen's d_z |
|---|---|---|---|---|---|---|---|
| D1 | 29 | +0.0172 | 0.3892 | 0.2386 | 28 | 0.8132 | 0.0443 |
| D2 | 29 | -0.0172 | 0.2494 | -0.3723 | 28 | 0.7125 | -0.0691 |
| D3 | 29 | +0.0000 | 0.2315 | 0.0000 | 28 | 1.0000 | 0.0000 |
| D4 | 29 | +0.0000 | 0.1336 | 0.0000 | 28 | 1.0000 | 0.0000 |
| D5 | 29 | +0.0000 | 0.0000 | NaN | 28 | 1.0000 | NaN |

## Per-rater per-axis paired delta (sensitivity)

| Axis | Rater | n | mean Δ (B−A) | sd Δ | t | p |
|---|---|---|---|---|---|---|
| D1 | Logician | 29 | +0.0000 | 0.4629 | 0.0000 | 1.0000 |
| D1 | IR | 29 | +0.0345 | 0.4988 | 0.3723 | 0.7125 |
| D2 | Logician | 29 | -0.0345 | 0.4988 | -0.3723 | 0.7125 |
| D2 | IR | 29 | +0.0000 | 0.0000 | NaN | 1.0000 |
| D3 | Logician | 29 | +0.0000 | 0.4629 | 0.0000 | 1.0000 |
| D3 | IR | 29 | +0.0000 | 0.0000 | NaN | 1.0000 |
| D4 | Logician | 29 | +0.0000 | 0.2673 | 0.0000 | 1.0000 |
| D4 | IR | 29 | +0.0000 | 0.0000 | NaN | 1.0000 |
| D5 | Logician | 29 | +0.0000 | 0.0000 | NaN | 1.0000 |
| D5 | IR | 29 | +0.0000 | 0.0000 | NaN | 1.0000 |

**Interpretation rule (per §3.2 + F2 framing):**
- A directional improvement under header-as-prime would show **negative** mean Δ on rubric axes.
- Per CEO F1 ruling and AOV-246 audit O2: zero-variance axes produce Δ=0 or NaN by construction; this is honest reporting, not a §6 LOO rescue.
- Significance (p<0.05) on a variance-bearing axis is necessary but not sufficient for §3.2 ratification — interpretation must be paired with §3.1 reliability gate clearance on the same axis.
