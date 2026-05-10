# `_kappa.md` — Phase 5 inter-rater reliability (§3.1)

**Corpus pin:** `0d67287` (origin/main)
**Inputs:** `EpistemicLogician_scores_unsealed.tsv` + `IndependentRater_scores_unsealed.tsv`
**N (joined, post-ERR-drop):** 59 cells (60 raw - 1 ERR row 7433b2505a5181bf)
**Method:** Cohen's quadratic-weighted κ; percentile bootstrap CI (B=2000, seed=20260510).
**Standing rulings applied:** CEO F1 `238ca0bb` (NaN κ on degenerate-marginal axes; excluded from §3.1 gate). No §6 LOO rescue. No §5 hypothesis edits.

| Axis | Logician variance | IR variance | κ (quadratic-weighted) | 95% bootstrap CI | Gate (≥0.6) |
|---|---|---|---|---|---|
| D1 | 0.2157 | 0.1064 | 0.3729 | [0.1132, 0.6177] | FAIL (boot 1999/2000, 1 NaN) |
| D2 | 0.1064 | 0.0000 | NaN (zero_variance_marginal) | n/a | EXCLUDED (F1) |
| D3 | 0.0929 | 0.0000 | NaN (zero_variance_marginal) | n/a | EXCLUDED (F1) |
| D4 | 0.0333 | 0.0000 | NaN (zero_variance_marginal) | n/a | EXCLUDED (F1) |
| D5 | 0.0000 | 0.0000 | NaN (zero_variance_marginal) | n/a | EXCLUDED (F1) |
| D6 | 0.0789 | 0.0000 | NaN (zero_variance_marginal) | n/a | EXCLUDED (F1) |
| D7 | 0.0000 | 0.0000 | NaN (zero_variance_marginal) | n/a | EXCLUDED (F1) |
| D8 | 0.0000 | 0.0000 | NaN (zero_variance_marginal) | n/a | EXCLUDED (F1) |

**Variance-bearing axes (κ defined):** D1
**Zero-variance axes (κ NaN, excluded per F1):** D2, D3, D4, D5, D6, D7, D8

**§3.1 gate (≥0.6 on variance-bearing axes):** PASS on (none); FAIL on D1.

## Per-rater marginal distributions (informational)

| Axis | Logician scores | IR scores |
|---|---|---|
| D1 | {1: 18, 0: 41} | {1: 7, 0: 52} |
| D2 | {1: 7, 0: 52} | {0: 59} |
| D3 | {1: 6, 0: 53} | {0: 59} |
| D4 | {1: 2, 0: 57} | {0: 59} |
| D5 | {0: 59} | {0: 59} |
| D6 | {0: 54, 1: 5} | {0: 59} |
| D7 | {0: 59} | {0: 59} |
| D8 | {0: 59} | {0: 59} |
