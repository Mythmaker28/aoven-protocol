#!/usr/bin/env python3
"""Run strip_test_b_markers.py on all 30 main Test B cells AND run the rationale-
leakage lint on raw + stripped Test B + ablation runs.

Per pre-reg \u00a73.1:
  - Strip script runs on every Test B cell.
  - Strip-diff is filed pre-rater-sealing.
  - Rationale-leakage lint rejects any Test B response that mentions
    'Aoven', 'the hypothesis', 'the rubric', 'anti-slippage', or any meta-priming
    phrase. (Strip applies to marker tokens; lint applies to META content.)

Outputs:
  cells/cell_<qid>_B.stripped.txt        (30 stripped Test B files)
  cells/_strip_diff.md                   (token-level diff, one row per cell)
  cells/_lint_report.md                  (lint pass/fail report; FAIL = re-block)
"""
import hashlib
import re
import subprocess
import sys
from pathlib import Path

WORKSPACE = Path(r"C:\Users\tommy\.paperclip\instances\default\workspaces\2ae117a1-f490-4e8e-a693-0f1d8d1d675b")
V02 = WORKSPACE / "aoven-protocol" / "tests" / "v0.2"
CELLS = V02 / "cells"
ABLATION = CELLS / "_ablation"
STRIP_SCRIPT = V02 / "strip_test_b_markers.py"

def sha256_bytes(b: bytes) -> str:
    return hashlib.sha256(b).hexdigest()

# -------- Load qids from manifest --------
qs = []
for line in (V02 / "_qs_manifest.tsv").read_text(encoding="utf-8").strip().split("\n"):
    qid, q = line.split("\t", 1)
    qs.append((qid, q))

# -------- Strip pass --------
strip_rows = []  # (qid, raw_sha, raw_size, stripped_sha, stripped_size, tokens_stripped)

# Marker token pattern (same as strip script)
MARKER_PAT = re.compile(r"\[(?:ANALOGY|BELIEF|EMOTION|FACT|HYP|INTERPRET|INTUIT|LIMIT|MEMORY|NOSRC|REC|SPEC)(?:,\s*CONF\([^)]*\))?\]|\[CONF\([^)]*\)\]")

for qid, _ in qs:
    raw_path = CELLS / f"cell_{qid}_B.txt"
    stripped_path = CELLS / f"cell_{qid}_B.stripped.txt"
    if not raw_path.exists():
        print(f"MISSING raw Test B file for {qid}: {raw_path}")
        continue
    raw_bytes = raw_path.read_bytes()

    # Run strip script on the file
    result = subprocess.run(
        [sys.executable, str(STRIP_SCRIPT), str(raw_path), "--output", str(stripped_path)],
        capture_output=True,
        timeout=30,
    )
    if result.returncode != 0:
        print(f"STRIP FAIL {qid}: rc={result.returncode}, stderr={result.stderr.decode('utf-8', errors='replace')}")
        continue

    stripped_bytes = stripped_path.read_bytes()
    raw_text = raw_bytes.decode("utf-8", errors="replace")
    tokens = MARKER_PAT.findall(raw_text)
    strip_rows.append((qid, sha256_bytes(raw_bytes), len(raw_bytes), sha256_bytes(stripped_bytes), len(stripped_bytes), len(tokens)))

# -------- Strip diff report --------
diff_md = "# AOV-180 Test B strip-script results (pre-rater-sealing token-level diff)\n\n"
diff_md += f"Strip script: `tests/v0.2/strip_test_b_markers.py`\n"
diff_md += f"Strip script SHA-256: `{sha256_bytes(STRIP_SCRIPT.read_bytes())}`\n\n"
diff_md += "## 30-row strip table\n\n"
diff_md += "| qid | raw sha | raw bytes | stripped sha | stripped bytes | tokens stripped |\n"
diff_md += "|-----|---------|-----------|--------------|----------------|----------------:|\n"
total_tokens = 0
for qid, raw_sha, raw_size, stripped_sha, stripped_size, tokens in strip_rows:
    diff_md += f"| {qid} | `{raw_sha[:16]}...` | {raw_size} | `{stripped_sha[:16]}...` | {stripped_size} | {tokens} |\n"
    total_tokens += tokens

diff_md += f"\n**Total marker tokens stripped across 30 Test B cells: {total_tokens}**\n\n"
if total_tokens == 0:
    diff_md += "Note: zero marker tokens across 30 cells indicates the bare-header form `[Aoven v0.1.2]\\n<Q>\\nNo flattery` does NOT empirically invoke v0.1.2 marker-syntax output. This is itself a measurement of the Test B treatment effect under the Two-Surface Separation regime. Raters score the unstripped output (which equals the stripped output in this case).\n"
(CELLS / "_strip_diff.md").write_text(diff_md, encoding="utf-8", newline="\n")

# -------- Rationale-leakage lint --------
LEAK_PATTERNS = [
    r"\bAoven\b",
    r"\bthe hypothesis\b",
    r"\bthe rubric\b",
    r"\banti[\s-]?slippage\b",
    r"\bv0\.1\.2\b",
    r"\bepistemic[\s-]?marker\b",
    r"\bcalibrated[\s-]?confidence\b",
]
LEAK_RE = [re.compile(p, re.IGNORECASE) for p in LEAK_PATTERNS]

def lint_text(text: str) -> list:
    """Returns list of (pattern, match) tuples for any leak found."""
    hits = []
    for pat, rx in zip(LEAK_PATTERNS, LEAK_RE):
        for m in rx.finditer(text):
            hits.append((pat, m.group(0), m.start()))
    return hits

lint_md = "# AOV-180 rationale-leakage lint report\n\n"
lint_md += "Per pre-reg \u00a73.1: any Test B response that mentions 'Aoven', 'the hypothesis', 'the rubric', 'anti-slippage', or any meta-priming phrase is rejected.\n\n"
lint_md += "Patterns checked (case-insensitive): " + ", ".join(f"`{p}`" for p in LEAK_PATTERNS) + "\n\n"

# Lint targets: raw Test B (30) + stripped Test B (30) + ablation runs (45) = 105 files
# Test A is NOT lint-targeted because it's the baseline and \u00a73.1 lint targets Test B only.
# But we DO scan Test A defensively for Aoven-leak as a contamination probe (auto-memory check).

def lint_file(p: Path, label: str):
    if not p.exists():
        return None
    try:
        text = p.read_text(encoding="utf-8", errors="replace")
    except Exception as e:
        return ("ERROR", str(e))
    hits = lint_text(text)
    return hits

# Scan Test B raw + stripped
b_raw_hits = []
b_stripped_hits = []
a_hits = []  # contamination probe
for qid, _ in qs:
    raw_p = CELLS / f"cell_{qid}_B.txt"
    stripped_p = CELLS / f"cell_{qid}_B.stripped.txt"
    test_a_p = CELLS / f"cell_{qid}_A.txt"
    h_raw = lint_file(raw_p, f"{qid}_B.raw")
    h_str = lint_file(stripped_p, f"{qid}_B.stripped")
    h_a = lint_file(test_a_p, f"{qid}_A")
    if h_raw:
        b_raw_hits.append((qid, h_raw))
    if h_str:
        b_stripped_hits.append((qid, h_str))
    if h_a:
        a_hits.append((qid, h_a))

# Scan ablation runs
abl_hits = []
ablation_qids = (V02 / "_ablation_manifest.tsv").read_text(encoding="utf-8").strip().split("\n")
for qid in ablation_qids:
    for run in (1, 2, 3):
        p = ABLATION / f"cell_{qid}_B_run{run}.txt"
        h = lint_file(p, f"{qid}_B_run{run}")
        if h:
            abl_hits.append((qid, run, h))

def render_hits(label, all_hits):
    s = f"### {label}\n\n"
    if not all_hits:
        s += "**No leakage hits.** \u2713\n\n"
        return s
    s += f"**{len(all_hits)} cell(s) with hits:**\n\n"
    for entry in all_hits:
        if len(entry) == 2:
            qid, hits = entry
            s += f"- `{qid}`: " + ", ".join(f"`{m}` (offset {off})" for (_, m, off) in hits) + "\n"
        else:
            qid, run, hits = entry
            s += f"- `{qid}` run{run}: " + ", ".join(f"`{m}` (offset {off})" for (_, m, off) in hits) + "\n"
    s += "\n"
    return s

lint_md += render_hits("Test B raw (30 cells)", b_raw_hits)
lint_md += render_hits("Test B stripped (30 cells)", b_stripped_hits)
lint_md += render_hits("Ablation runs (45 cells)", abl_hits)
lint_md += render_hits("Test A baseline (30 cells; contamination probe)", a_hits)

# Decision
b_raw_ct = len(b_raw_hits)
b_str_ct = len(b_stripped_hits)
abl_ct = len(abl_hits)
a_ct = len(a_hits)

lint_md += "\n## Outcome\n\n"
if b_raw_ct == 0 and b_str_ct == 0 and abl_ct == 0:
    lint_md += "**Lint: PASS.** No rationale-leakage in any Test B (raw or stripped) or ablation run.\n\n"
else:
    lint_md += f"**Lint: FAIL.** {b_raw_ct} raw + {b_str_ct} stripped + {abl_ct} ablation cells with leakage. Affected cells require regeneration or RedTeam adjudication.\n\n"

if a_ct > 0:
    lint_md += f"\u26a0\ufe0f **Test A contamination probe: {a_ct} Test A cell(s) contain Aoven/v0.1.2 references.** This is evidence the auto-memory loaded under the Item 4 transport and primed the baseline. RedTeam contamination test \u00a72.5 may re-block on this.\n"
else:
    lint_md += "\u2713 Test A contamination probe clean: 0 Test A cells reference Aoven/v0.1.2/etc. No empirical evidence of auto-memory contamination via the Item 4 transport.\n"

(CELLS / "_lint_report.md").write_text(lint_md, encoding="utf-8", newline="\n")

print(f"Strip pass: {len(strip_rows)}/30 cells, total tokens stripped: {total_tokens}")
print(f"Lint summary:")
print(f"  Test B raw hits:      {b_raw_ct}")
print(f"  Test B stripped hits: {b_str_ct}")
print(f"  Ablation hits:        {abl_ct}")
print(f"  Test A probe hits:    {a_ct}")
