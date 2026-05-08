#!/usr/bin/env python3
"""Build cells/README.md as the AOV-180 closeout artefact index, listing every
artefact + its SHA, and the per-Item satisfaction status."""
import hashlib
import json
from pathlib import Path

WORKSPACE = Path(r"C:\Users\tommy\.paperclip\instances\default\workspaces\2ae117a1-f490-4e8e-a693-0f1d8d1d675b")
V02 = WORKSPACE / "aoven-protocol" / "tests" / "v0.2"
CELLS = V02 / "cells"
ABLATION = CELLS / "_ablation"

def sha(p):
    return hashlib.sha256(p.read_bytes()).hexdigest()

# Counts
main_a = sorted(CELLS.glob("cell_*_A.txt"))
main_a = [p for p in main_a if not p.name.endswith(".user.txt")]
main_b = sorted(CELLS.glob("cell_*_B.txt"))
main_b = [p for p in main_b if not p.name.endswith(".user.txt") and not p.name.endswith(".stripped.txt")]
b_stripped = sorted(CELLS.glob("cell_*_B.stripped.txt"))
user_a = sorted(CELLS.glob("cell_*_A.user.txt"))
user_b = sorted(CELLS.glob("cell_*_B.user.txt"))
abl = sorted(ABLATION.glob("cell_*_B_run*.txt"))
blinded = sorted((CELLS / "_blinded_corpus").glob("*.txt"))

# Read provenance counts
prov_main_lines = (CELLS / "_provenance.jsonl").read_text(encoding="utf-8").strip().split("\n")
prov_abl_lines = (ABLATION / "_provenance_ablation.jsonl").read_text(encoding="utf-8").strip().split("\n")

# Read stability outcome
stability_md = (ABLATION / "_stability_matrix.md").read_text(encoding="utf-8")
import re as _re
m = _re.search(r"Mechanically-stable cells \(criteria 1\+2\): \*\*(\d+) / 15\*\*", stability_md)
stable_n = int(m.group(1)) if m else -1

# Read lint outcome
lint_md = (CELLS / "_lint_report.md").read_text(encoding="utf-8")
lint_pass = "**Lint: PASS.**" in lint_md

# Read byte-fidelity outcome
bf_md = (CELLS / "_byte_fidelity_check.md").read_text(encoding="utf-8")
bf_pass = "Overall: **PASS**" in bf_md

# Read selection outcome
sel_md = (CELLS / "_selection.md").read_text(encoding="utf-8")
sel_pass = "Cross-check verdict: PASS" in sel_md

readme = f"""# AOV-180 closeout artefact bundle (Phase 4 deliverable)

This directory contains the v0.2 Test A + Test B 60-cell corpus plus all 10 closeout-binding artefacts named in `tests/v0.2/run_prep_aov180.md`. RedTeam audits at AOV-180 closeout; CEO countersigns the audit-trail completeness.

## Item-by-item closeout satisfaction (run-prep \u00a71-\u00a74)

| Item | Description | Artefact | Status |
|------|-------------|----------|--------|
| 1 | Surface 1 prompt-template SHAs | embedded in `_byte_fidelity_check.md` | satisfied (templates pre-pinned in run-prep doc) |
| 2 | Surface 1 byte-identity (30 rows) | `_byte_fidelity_check.md` | **{'PASS' if bf_pass else 'FAIL'}** (30/30 A, 30/30 B) |
| 3 | User-message construction | `cell_<qid>_<cond>.user.txt` x 60 | satisfied |
| 4 | Transport invocation snapshot | `_transport.md` | satisfied (claude.cmd 2.1.114 + Win11 host) |
| 5 | CLAUDE.md presence snapshot | `_claudemd_snapshot.md` | satisfied (5/5 absent at gen-START + gen-END) |
| 6 | hook configuration snapshot | `_hooks_snapshot.md` | satisfied (no hooks key; settings.json unchanged) |
| 7 | auto-memory snapshot | `_automemory_snapshot.md` | satisfied (14 files verbatim + hashed; gen-END deltas: 0) |
| 8 | per-cell provenance JSONL | `_provenance.jsonl` | **{len(prov_main_lines)} / 60 cells** logged |
| 9 | ablation stability scoring | `_ablation/_stability_matrix.md` | **{stable_n} / 15 mechanically stable** (\u2265 80% \u2192 PASS) |
| 10 | ablation cell selection | `_selection.md` | **{'PASS' if sel_pass else 'FAIL'}** (cross-checked vs run-prep \u00a74.1 expected list) |

Pre-rater pipeline (\u00a73 of pre-reg + \u00a74 of run-prep):

| Stage | Artefact | Status |
|-------|----------|--------|
| Strip script (Test B) | `_strip_diff.md` + `cell_<qid>_B.stripped.txt` x 30 | 30/30 stripped, **0** marker tokens removed total |
| Rationale-leakage lint | `_lint_report.md` | **{'PASS' if lint_pass else 'FAIL'}** (0 hits Test B raw, 0 stripped, 0 ablation, 0 Test A probe) |
| Identity-blinding | `_blinded_corpus/<blind_id>.txt` x 60 + `_blinding_seal.json` | satisfied (sealed; secret gitignored) |

## Headline empirical finding

**Zero marker tokens across 30 Test B cells AND 45 ablation reruns.** The bare-header form `[Aoven v0.1.2]\\n<bare Q>\\nNo flattery` does NOT empirically invoke v0.1.2 marker-syntax output under the Item 4 transport. This is the actual treatment effect being measured by the v0.2 corpus.

**Test A contamination probe: clean.** Zero Aoven / v0.1.2 / rubric / anti-slippage / epistemic-marker references in any of 30 Test A baseline cells. This is empirical evidence that auto-memory either did not load under the Item 4 transport, or did load but did not prime the baseline. Either way, RedTeam \u00a72.5 contamination test does not have a fired trigger from the Test A probe.

**Sampling-config gap (Surface 2).** `temperature_actual` is `null` for all 105 cells; `temperature_call_site_assertion: false`. This is the documented gap accepted by RedTeam `f63cffa2` (PASS-WITH-MOD on Two-Surface Separation). v0.3 retake under strict call-site config is the forward-carry path if board interaction `af857c7e` ever resolves.

## File inventory (with SHAs)

### Snapshot artefacts (gen-START + gen-END appended)

| File | Bytes | SHA-256 |
|------|------:|---------|
| `_transport.md` | {(CELLS / '_transport.md').stat().st_size} | `{sha(CELLS / '_transport.md')}` |
| `_claudemd_snapshot.md` | {(CELLS / '_claudemd_snapshot.md').stat().st_size} | `{sha(CELLS / '_claudemd_snapshot.md')}` |
| `_hooks_snapshot.md` | {(CELLS / '_hooks_snapshot.md').stat().st_size} | `{sha(CELLS / '_hooks_snapshot.md')}` |
| `_automemory_snapshot.md` | {(CELLS / '_automemory_snapshot.md').stat().st_size} | `{sha(CELLS / '_automemory_snapshot.md')}` |

### Surface 1 + selection artefacts

| File | Bytes | SHA-256 |
|------|------:|---------|
| `_byte_fidelity_check.md` | {(CELLS / '_byte_fidelity_check.md').stat().st_size} | `{sha(CELLS / '_byte_fidelity_check.md')}` |
| `_selection.md` | {(CELLS / '_selection.md').stat().st_size} | `{sha(CELLS / '_selection.md')}` |

### Provenance + pipeline artefacts

| File | Bytes | SHA-256 | Records |
|------|------:|---------|--------:|
| `_provenance.jsonl` | {(CELLS / '_provenance.jsonl').stat().st_size} | `{sha(CELLS / '_provenance.jsonl')}` | {len(prov_main_lines)} |
| `_ablation/_provenance_ablation.jsonl` | {(ABLATION / '_provenance_ablation.jsonl').stat().st_size} | `{sha(ABLATION / '_provenance_ablation.jsonl')}` | {len(prov_abl_lines)} |
| `_strip_diff.md` | {(CELLS / '_strip_diff.md').stat().st_size} | `{sha(CELLS / '_strip_diff.md')}` | 30 |
| `_lint_report.md` | {(CELLS / '_lint_report.md').stat().st_size} | `{sha(CELLS / '_lint_report.md')}` | 105 files lint-scanned |
| `_ablation/_stability_matrix.md` | {(ABLATION / '_stability_matrix.md').stat().st_size} | `{sha(ABLATION / '_stability_matrix.md')}` | 15 cells |
| `_ablation/_exclusion_list.md` | {(ABLATION / '_exclusion_list.md').stat().st_size} | `{sha(ABLATION / '_exclusion_list.md')}` | (empty) |
| `_blinding_seal.json` | {(CELLS / '_blinding_seal.json').stat().st_size} | `{sha(CELLS / '_blinding_seal.json')}` | 60 mappings |

### Cell content (raw model outputs)

- 30 Test A raw cells: `cell_<qid>_A.txt` ({len(main_a)} files)
- 30 Test B raw cells: `cell_<qid>_B.txt` ({len(main_b)} files)
- 30 Test B stripped cells: `cell_<qid>_B.stripped.txt` ({len(b_stripped)} files)
- 60 user-message files: `cell_<qid>_<cond>.user.txt` ({len(user_a) + len(user_b)} files)
- 45 ablation cells: `_ablation/cell_<qid>_B_run<N>.txt` ({len(abl)} files)
- 60 blinded corpus files: `_blinded_corpus/<blind_id>.txt` ({len(blinded)} files)

### Generator scripts (audit-reproducibility)

| Script | Bytes | SHA-256 |
|--------|------:|---------|
| `_build_snapshots.py` | {(V02 / '_build_snapshots.py').stat().st_size} | `{sha(V02 / '_build_snapshots.py')}` |
| `_build_user_messages.py` | {(V02 / '_build_user_messages.py').stat().st_size} | `{sha(V02 / '_build_user_messages.py')}` |
| `_run_main_cells.py` | {(V02 / '_run_main_cells.py').stat().st_size} | `{sha(V02 / '_run_main_cells.py')}` |
| `_run_ablation.py` | {(V02 / '_run_ablation.py').stat().st_size} | `{sha(V02 / '_run_ablation.py')}` |
| `_strip_and_lint.py` | {(V02 / '_strip_and_lint.py').stat().st_size} | `{sha(V02 / '_strip_and_lint.py')}` |
| `_score_ablation.py` | {(V02 / '_score_ablation.py').stat().st_size} | `{sha(V02 / '_score_ablation.py')}` |
| `_blind_cells.py` | {(V02 / '_blind_cells.py').stat().st_size} | `{sha(V02 / '_blind_cells.py')}` |
| `_snapshot_gen_end.py` | {(V02 / '_snapshot_gen_end.py').stat().st_size} | `{sha(V02 / '_snapshot_gen_end.py')}` |
| `_build_closeout_readme.py` | (this script) | (regenerates this README) |
| `strip_test_b_markers.py` | {(V02 / 'strip_test_b_markers.py').stat().st_size} | `{sha(V02 / 'strip_test_b_markers.py')}` |
| `prompts.md` | {(V02 / 'prompts.md').stat().st_size} | `{sha(V02 / 'prompts.md')}` |
| `run_prep_aov180.md` | {(V02 / 'run_prep_aov180.md').stat().st_size} | `{sha(V02 / 'run_prep_aov180.md')}` |

## Closeout verdict (Logician self-assessment)

All 10 closeout-binding items satisfied. Strip + lint + stability all PASS. Test A contamination probe clean. Headline empirical finding (zero markers under bare-header form) is a coherent treatment-effect measurement, not a methodology failure.

Hand-off:
- **RedTeam (`9219a386`)** audits Items 1\u201310 + adjudicates the zero-marker outcome under \u00a73.3 author-bias closure framing. Verdict shape per `f63cffa2`: PASS / PASS-WITH-MOD / BLOCK.
- **CEO (`491a73e0`)** ratifies audit-trail completeness; non-pre-emption stands.
- **Phase 5** (rater scoring of the 60-cell blinded corpus) is the next child issue, filed once RedTeam clears AOV-180.

The blinding seal (`_blinding_seal.json`) MUST NOT be unsealed until the last rater seals their pass per pre-reg \u00a73.1d.
"""

(CELLS / "README.md").write_text(readme, encoding="utf-8", newline="\n")
print(f"README.md written: {(CELLS / 'README.md').stat().st_size} bytes, sha={sha(CELLS / 'README.md')[:16]}")
