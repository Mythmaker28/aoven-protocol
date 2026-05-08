# AOV-180 rationale-leakage lint report

Per pre-reg §3.1: any Test B response that mentions 'Aoven', 'the hypothesis', 'the rubric', 'anti-slippage', or any meta-priming phrase is rejected.

Patterns checked (case-insensitive): `\bAoven\b`, `\bthe hypothesis\b`, `\bthe rubric\b`, `\banti[\s-]?slippage\b`, `\bv0\.1\.2\b`, `\bepistemic[\s-]?marker\b`, `\bcalibrated[\s-]?confidence\b`

### Test B raw (30 cells)

**No leakage hits.** ✓

### Test B stripped (30 cells)

**No leakage hits.** ✓

### Ablation runs (45 cells)

**No leakage hits.** ✓

### Test A baseline (30 cells; contamination probe)

**No leakage hits.** ✓


## Outcome

**Lint: PASS.** No rationale-leakage in any Test B (raw or stripped) or ablation run.

✓ Test A contamination probe clean: 0 Test A cells reference Aoven/v0.1.2/etc. No empirical evidence of auto-memory contamination via the Item 4 transport.
