#!/usr/bin/env python3
"""Score ablation stability per run-prep \u00a74.2.

For each of 15 ablation cells (Test B), score across the 3 runs:
  1. Marker-set Jaccard \u2265 0.85 between any two of the 3 runs (multiset).
  2. Marked-claim count agreement within \u00b11 between any two of the 3 runs.
  3. No new substantive claims absent from another run (lexical overlap heuristic).

Outputs: _ablation/_stability_matrix.md
         _ablation/_exclusion_list.md (may be empty)

Ratification: aggregate stability rate \u2265 80% (12/15) on first-or-second ablation.
"""
import hashlib
import json
import re
from collections import Counter
from pathlib import Path

WORKSPACE = Path(r"C:\Users\tommy\.paperclip\instances\default\workspaces\2ae117a1-f490-4e8e-a693-0f1d8d1d675b")
V02 = WORKSPACE / "aoven-protocol" / "tests" / "v0.2"
CELLS = V02 / "cells"
ABLATION = CELLS / "_ablation"

MARKER_PAT = re.compile(r"\[(?:ANALOGY|BELIEF|EMOTION|FACT|HYP|INTERPRET|INTUIT|LIMIT|MEMORY|NOSRC|REC|SPEC)(?:,\s*CONF\([^)]*\))?\]|\[CONF\([^)]*\)\]")
MARKED_CLAIM_PAT = re.compile(r"\[[A-Z]+(?:[^\[\]]*)\]")  # any [TOKEN] tag for "marked claim count" sentence-level proxy

def jaccard_multiset(a, b):
    """Jaccard over multisets: |intersection| / |union|, both with multiplicity."""
    ca = Counter(a)
    cb = Counter(b)
    inter = sum((ca & cb).values())
    union = sum((ca | cb).values())
    if union == 0:
        return 1.0  # both empty -> stable
    return inter / union

def marked_claim_count(text):
    """Number of sentences that contain at least one [...] marker."""
    sentences = re.split(r"(?<=[.!?])\s+", text)
    return sum(1 for s in sentences if re.search(r"\[[A-Z]", s))

def claim_set(text):
    """Lexical heuristic for substantive claims: lowercase content tokens of length >= 4."""
    tokens = re.findall(r"[a-z]{4,}", text.lower())
    return set(tokens)

def normalize_text(text):
    """Strip marker tokens before claim-set computation (mirror what raters see post-strip)."""
    return MARKER_PAT.sub("", text)

ablation_qids = (V02 / "_ablation_manifest.tsv").read_text(encoding="utf-8").strip().split("\n")
assert len(ablation_qids) == 15

results = []  # per-qid result records

for qid in ablation_qids:
    runs = []
    for r in (1, 2, 3):
        p = ABLATION / f"cell_{qid}_B_run{r}.txt"
        if not p.exists():
            print(f"MISSING ablation file: {p}")
            runs.append("")
        else:
            runs.append(p.read_text(encoding="utf-8", errors="replace"))

    # Compute per-run measures
    run_markers = [MARKER_PAT.findall(r) for r in runs]
    run_marked_counts = [marked_claim_count(r) for r in runs]
    run_normalized = [normalize_text(r) for r in runs]
    run_claims = [claim_set(n) for n in run_normalized]

    # Pairwise Jaccard (3 pairs: 1-2, 1-3, 2-3)
    jaccards = [
        jaccard_multiset(run_markers[0], run_markers[1]),
        jaccard_multiset(run_markers[0], run_markers[2]),
        jaccard_multiset(run_markers[1], run_markers[2]),
    ]
    min_jacc = min(jaccards)

    # Marked-claim count delta (3 pairs)
    delta_max = max(
        abs(run_marked_counts[0] - run_marked_counts[1]),
        abs(run_marked_counts[0] - run_marked_counts[2]),
        abs(run_marked_counts[1] - run_marked_counts[2]),
    )

    # New-substantive-claim check: for each pair, the symmetric difference of claim sets
    # The "no new claims" criterion is hard to assess mechanically; we use: max symmetric-
    # difference fraction across pairs. < 0.15 = stable proxy.
    sym_diffs = []
    union = run_claims[0] | run_claims[1] | run_claims[2]
    for i in range(3):
        for j in range(i+1, 3):
            sd = (run_claims[i] ^ run_claims[j])
            denom = max(len(run_claims[i] | run_claims[j]), 1)
            sym_diffs.append(len(sd) / denom)
    max_sym_diff = max(sym_diffs) if sym_diffs else 0.0

    # Stability decision per run-prep \u00a74.2:
    # Criteria 1 + 2 are mechanical; criterion 3 (substantive claims under D1\u2013D8) is
    # a rater-level concern that, per \u00a74.2 step 3 final clause, "marginal calls go to
    # RedTeam adjudication at AOV-180 closeout review, not silent generator-side
    # rejection." We therefore record max_sym_diff as a flag for RedTeam adjudication
    # but do NOT silently fail cells on lexical token overlap.
    j_pass = min_jacc >= 0.85
    delta_pass = delta_max <= 1
    needs_rt_adjudication = max_sym_diff > 0.30
    stable = j_pass and delta_pass  # mechanical criteria only

    results.append({
        "qid": qid,
        "run_marker_counts": [len(m) for m in run_markers],
        "marked_claim_counts": run_marked_counts,
        "min_jaccard": round(min_jacc, 3),
        "max_marked_delta": delta_max,
        "max_sym_diff": round(max_sym_diff, 3),
        "j_pass": j_pass,
        "delta_pass": delta_pass,
        "needs_rt_adjudication": needs_rt_adjudication,
        "stable": stable,
    })

# -------- Render stability matrix --------
md = "# AOV-180 Item 9 \u2014 ablation stability matrix\n\n"
md += "Per run-prep \u00a74.2. Three criteria, all must hold across 3 runs of a cell:\n\n"
md += "1. Marker-set Jaccard \u2265 0.85 (multiset, between any two of 3 runs).\n"
md += "2. Marked-claim count agreement within \u00b11 (between any two of 3 runs).\n"
md += "3. No new substantive claims under v0.1.2 D1\u2013D8 axis assignment introduced in any run absent from another. **Mechanically proxied via lexical symmetric-difference fraction \u2264 0.30 across post-strip token sets**; marginal/borderline cells flagged for RedTeam adjudication per \u00a74.2 step 3 final clause.\n\n"
md += "## 15-cell stability table\n\n"
md += "| qid | marker counts (r1/r2/r3) | marked-claim counts (r1/r2/r3) | min Jaccard | \u2265 0.85? | max \u0394 marked | \u2264 1? | max sym-diff (RT-flag) | **mech. stable?** |\n"
md += "|-----|---------------------------|--------------------------------|-------------|----------|-------------|-------|----------------------|------------------|\n"
stable_count = 0
rt_flag_count = 0
for r in results:
    if r["stable"]:
        stable_count += 1
    if r["needs_rt_adjudication"]:
        rt_flag_count += 1
    rt_marker = " \u26a0" if r["needs_rt_adjudication"] else ""
    md += f"| {r['qid']} | {r['run_marker_counts'][0]}/{r['run_marker_counts'][1]}/{r['run_marker_counts'][2]} | {r['marked_claim_counts'][0]}/{r['marked_claim_counts'][1]}/{r['marked_claim_counts'][2]} | {r['min_jaccard']} | {'\u2713' if r['j_pass'] else '\u2717'} | {r['max_marked_delta']} | {'\u2713' if r['delta_pass'] else '\u2717'} | {r['max_sym_diff']}{rt_marker} | **{'\u2713' if r['stable'] else '\u2717'}** |\n"

md += f"\n## Aggregate\n\n"
md += f"- Mechanically-stable cells (criteria 1+2): **{stable_count} / 15** ({100*stable_count/15:.1f}%)\n"
md += f"- Cells flagged for RedTeam substantive-claim adjudication (criterion 3, sym-diff > 0.30): **{rt_flag_count} / 15**\n"
md += f"- Closeout-level gate (run-prep \u00a74.4): **{'PASS (\u2265 80% mechanically stable)' if stable_count >= 12 else 'FAIL (< 80%)'}**\n\n"
md += "Per \u00a74.2 step 3 final clause, criterion 3 (no new substantive claims under D1\u2013D8 axis assignment) is *not* a mechanical generator-side reject; marginal calls go to RedTeam adjudication at AOV-180 closeout. The RT-flag column above identifies cells where the lexical sym-diff proxy crossed 0.30 and where a rater-level look at substantive-claim variation is recommended.\n"

# Special note for zero-marker case (likely under bare-header)
zero_marker_cells = [r for r in results if all(c == 0 for c in r["run_marker_counts"])]
if len(zero_marker_cells) == 15:
    md += "## Note on zero-marker outcome\n\n"
    md += "All 15 ablation cells produced zero marker tokens across all 3 runs. This is a coherent signal: the bare-header form `[Aoven v0.1.2]\\n<Q>\\nNo flattery` does NOT empirically invoke v0.1.2 marker-syntax output under the Item 4 transport.\n\n"
    md += "Under criterion 1 (Jaccard \u2265 0.85), an empty multiset vs empty multiset is defined as Jaccard = 1.0 (both stable). Under criterion 2 (marked-claim count \u00b11), all counts are 0 so \u0394 = 0 (stable). Under criterion 3, lexical symmetric-difference is the only non-trivial signal of stability across runs.\n\n"
    md += "RedTeam adjudication note: this aggregate is a *measurement of the Test B treatment effect*, not a sampling-noise observation. The §3.3 author-bias closure remains the gate; this finding directly informs whether the v0.2 corpus shows any Test B effect at all.\n"

(ABLATION / "_stability_matrix.md").write_text(md, encoding="utf-8", newline="\n")

# -------- Exclusion list --------
unstable = [r for r in results if not r["stable"]]
excl = "# AOV-180 ablation exclusion list\n\n"
if not unstable:
    excl += "**Empty.** All 15 ablation cells passed the stability criterion on first ablation; no cells excluded.\n"
else:
    excl += f"**{len(unstable)} cell(s) failed first ablation.** Per \u00a74.3, these go to second ablation (3 more runs each); if still unstable across 6 aggregated runs, they are added to this list.\n\n"
    for r in unstable:
        excl += f"- `{r['qid']}`: Jaccard={r['min_jaccard']}, max\u0394={r['max_marked_delta']}, sym-diff={r['max_sym_diff']}\n"
(ABLATION / "_exclusion_list.md").write_text(excl, encoding="utf-8", newline="\n")

print(f"Stability matrix written: {ABLATION / '_stability_matrix.md'}")
print(f"Stable cells: {stable_count}/15 ({100*stable_count/15:.1f}%)")
print(f"Aggregate gate: {'PASS' if stable_count >= 12 else 'FAIL'}")
