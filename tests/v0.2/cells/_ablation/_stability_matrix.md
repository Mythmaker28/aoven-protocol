# AOV-180 Item 9 — ablation stability matrix

Per run-prep §4.2. Three criteria, all must hold across 3 runs of a cell:

1. Marker-set Jaccard ≥ 0.85 (multiset, between any two of 3 runs).
2. Marked-claim count agreement within ±1 (between any two of 3 runs).
3. No new substantive claims under v0.1.2 D1–D8 axis assignment introduced in any run absent from another. **Mechanically proxied via lexical symmetric-difference fraction ≤ 0.30 across post-strip token sets**; marginal/borderline cells flagged for RedTeam adjudication per §4.2 step 3 final clause.

## 15-cell stability table

| qid | marker counts (r1/r2/r3) | marked-claim counts (r1/r2/r3) | min Jaccard | ≥ 0.85? | max Δ marked | ≤ 1? | max sym-diff (RT-flag) | **mech. stable?** |
|-----|---------------------------|--------------------------------|-------------|----------|-------------|-------|----------------------|------------------|
| V02-D-NORM-003 | 0/0/0 | 0/0/0 | 1.0 | ✓ | 0 | ✓ | 0.816 ⚠ | **✓** |
| V02-D-NORM-005 | 0/0/0 | 0/0/0 | 1.0 | ✓ | 0 | ✓ | 0.806 ⚠ | **✓** |
| V02-D-NORM-007 | 0/0/0 | 0/0/0 | 1.0 | ✓ | 0 | ✓ | 0.789 ⚠ | **✓** |
| V02-D-NORM-008 | 0/0/0 | 0/0/0 | 1.0 | ✓ | 0 | ✓ | 0.819 ⚠ | **✓** |
| V02-D-PRED-001 | 0/0/0 | 0/0/0 | 1.0 | ✓ | 0 | ✓ | 0.825 ⚠ | **✓** |
| V02-D-PRED-005 | 0/0/0 | 0/0/0 | 1.0 | ✓ | 0 | ✓ | 0.734 ⚠ | **✓** |
| V02-D-PRED-006 | 0/0/0 | 0/0/0 | 1.0 | ✓ | 0 | ✓ | 0.79 ⚠ | **✓** |
| V02-D-SCI-002 | 0/0/0 | 0/0/0 | 1.0 | ✓ | 0 | ✓ | 0.743 ⚠ | **✓** |
| V02-D-SCI-003 | 0/0/0 | 0/0/0 | 1.0 | ✓ | 0 | ✓ | 0.782 ⚠ | **✓** |
| V02-D-SCI-004 | 0/0/0 | 0/0/0 | 1.0 | ✓ | 0 | ✓ | 0.693 ⚠ | **✓** |
| V02-D-SCI-005 | 0/0/0 | 0/0/0 | 1.0 | ✓ | 0 | ✓ | 0.743 ⚠ | **✓** |
| V02-D-TECH-002 | 0/0/0 | 0/0/0 | 1.0 | ✓ | 0 | ✓ | 0.787 ⚠ | **✓** |
| V02-D-TECH-005 | 0/0/0 | 0/0/0 | 1.0 | ✓ | 0 | ✓ | 0.767 ⚠ | **✓** |
| V02-D-TECH-006 | 0/0/0 | 0/0/0 | 1.0 | ✓ | 0 | ✓ | 0.793 ⚠ | **✓** |
| V02-D-TECH-007 | 0/0/0 | 0/0/0 | 1.0 | ✓ | 0 | ✓ | 0.844 ⚠ | **✓** |

## Aggregate

- Mechanically-stable cells (criteria 1+2): **15 / 15** (100.0%)
- Cells flagged for RedTeam substantive-claim adjudication (criterion 3, sym-diff > 0.30): **15 / 15**
- Closeout-level gate (run-prep §4.4): **PASS (≥ 80% mechanically stable)**

Per §4.2 step 3 final clause, criterion 3 (no new substantive claims under D1–D8 axis assignment) is *not* a mechanical generator-side reject; marginal calls go to RedTeam adjudication at AOV-180 closeout. The RT-flag column above identifies cells where the lexical sym-diff proxy crossed 0.30 and where a rater-level look at substantive-claim variation is recommended.
## Note on zero-marker outcome

All 15 ablation cells produced zero marker tokens across all 3 runs. This is a coherent signal: the bare-header form `[Aoven v0.1.2]\n<Q>\nNo flattery` does NOT empirically invoke v0.1.2 marker-syntax output under the Item 4 transport.

Under criterion 1 (Jaccard ≥ 0.85), an empty multiset vs empty multiset is defined as Jaccard = 1.0 (both stable). Under criterion 2 (marked-claim count ±1), all counts are 0 so Δ = 0 (stable). Under criterion 3, lexical symmetric-difference is the only non-trivial signal of stability across runs.

RedTeam adjudication note: this aggregate is a *measurement of the Test B treatment effect*, not a sampling-noise observation. The §3.3 author-bias closure remains the gate; this finding directly informs whether the v0.2 corpus shows any Test B effect at all.
