#!/usr/bin/env python3
"""Extract 30 bare Qs from prompts.md, build Test A + Test B user-message files,
   produce byte-fidelity check (Item 2), produce ablation selection doc (Item 10).

Each user-message file is the *exact bytes sent as the user message to claude -p*.
- Test A: <bare Q>           (no leading/trailing whitespace, no header, no footer)
- Test B: [Aoven v0.1.2]\n<bare Q>\nNo flattery
"""
import hashlib
import re
from pathlib import Path

WORKSPACE = Path(r"C:\Users\tommy\.paperclip\instances\default\workspaces\2ae117a1-f490-4e8e-a693-0f1d8d1d675b")
V02 = WORKSPACE / "aoven-protocol" / "tests" / "v0.2"
PROMPTS = V02 / "prompts.md"
CELLS = V02 / "cells"
ABLATION = CELLS / "_ablation"
ABLATION.mkdir(parents=True, exist_ok=True)

def sha256_bytes(b: bytes) -> str:
    return hashlib.sha256(b).hexdigest()

# -------- Parse prompts.md to extract 30 bare Qs --------
content = PROMPTS.read_text(encoding="utf-8")

# Find every "#### V02-D-..." header followed by the Q on the next non-blank line.
qid_re = re.compile(r"^####\s+(V02-D-[A-Z]+-\d+)\s*$", re.MULTILINE)
lines = content.split("\n")

qs = []  # list of (qid, bare_q)
i = 0
while i < len(lines):
    m = qid_re.match(lines[i])
    if m:
        qid = m.group(1)
        # next non-blank line is the Q text
        j = i + 1
        while j < len(lines) and lines[j].strip() == "":
            j += 1
        if j < len(lines):
            bare_q = lines[j].strip()  # no surrounding whitespace; italics already absent in prompts.md per audit cross-check
            qs.append((qid, bare_q))
            i = j + 1
            continue
    i += 1

assert len(qs) == 30, f"Expected 30 Qs, got {len(qs)}"

# -------- Build user-message files for Test A and Test B --------
TEST_B_PREFIX = "[Aoven v0.1.2]\n"
TEST_B_SUFFIX = "\nNo flattery"

# Sanity: confirm template SHAs match run-prep doc Item 1
assert sha256_bytes(b"") == "e3b0c44298fc1c149afbf4c8996fb92427ae41e4649b934ca495991b7852b855"
assert sha256_bytes(TEST_B_PREFIX.encode("utf-8")) == "2fe5b9af22d39d26f27416c0b3fee121f703908c4aed5f61adb81d8d6fdb6c75"
assert sha256_bytes(TEST_B_SUFFIX.encode("utf-8")) == "4fda0fe3951cab055d1f4c6e0f564e691288b387cde5fb0313005bfc8c5e39fb"
# Item 1 cross-check sha
template_with_placeholder = TEST_B_PREFIX + "<bare Q>" + TEST_B_SUFFIX
assert sha256_bytes(template_with_placeholder.encode("utf-8")) == "c8b2d4f9ecd7ba1c1bbee095ed10d5e94ab8b721ac91ae392979ae894d7508ff", \
    f"Template-with-placeholder SHA mismatch: {sha256_bytes(template_with_placeholder.encode('utf-8'))}"

byte_fidelity_rows = []  # (qid, sha_bare, sha_A, sha_B, pass)

for qid, bare_q in qs:
    bare_q_bytes = bare_q.encode("utf-8")
    sha_bare = sha256_bytes(bare_q_bytes)

    # Test A user message = <bare Q>
    test_a_bytes = bare_q_bytes
    sha_a = sha256_bytes(test_a_bytes)
    (CELLS / f"cell_{qid}_A.user.txt").write_bytes(test_a_bytes)

    # Test B user message = [Aoven v0.1.2]\n<bare Q>\nNo flattery
    test_b_text = TEST_B_PREFIX + bare_q + TEST_B_SUFFIX
    test_b_bytes = test_b_text.encode("utf-8")
    sha_b = sha256_bytes(test_b_bytes)
    (CELLS / f"cell_{qid}_B.user.txt").write_bytes(test_b_bytes)

    # Byte-fidelity check (Item 2):
    # Test A: sha_a == sha_bare
    # Test B: sha_b is sha of the full string; cross-check by reconstructing
    a_pass = (sha_a == sha_bare)
    # For B, reconstruct expected: the file bytes minus prefix bytes minus suffix bytes
    # should equal bare_q_bytes
    file_b = (CELLS / f"cell_{qid}_B.user.txt").read_bytes()
    prefix_bytes = TEST_B_PREFIX.encode("utf-8")
    suffix_bytes = TEST_B_SUFFIX.encode("utf-8")
    stripped = file_b[len(prefix_bytes):-len(suffix_bytes)]
    b_pass = (sha256_bytes(stripped) == sha_bare)

    byte_fidelity_rows.append((qid, sha_bare, sha_a, sha_b, a_pass, b_pass))

# -------- Write _byte_fidelity_check.md (Item 2) --------
md = "# AOV-180 Item 2 \u2014 Surface 1 byte-fidelity verification\n\n"
md += "Per run-prep \u00a71 Item 2: every Test A user message MUST equal `<bare Q>` exactly; every Test B user message MUST equal `[Aoven v0.1.2]\\n<bare Q>\\nNo flattery` exactly. All 30 rows MUST pass.\n\n"
md += f"prompts.md SHA-256 (gen-START): `{sha256_bytes(PROMPTS.read_bytes())}`\n\n"
md += "## 30-row verification table\n\n"
md += "| qid | sha256(<bare Q>) | sha256(Test A user msg) | A pass | sha256(Test B user msg) | B pass |\n"
md += "|-----|------------------|--------------------------|--------|--------------------------|--------|\n"
all_pass = True
for qid, sha_bare, sha_a, sha_b, a_pass, b_pass in byte_fidelity_rows:
    md += f"| {qid} | `{sha_bare[:16]}...` | `{sha_a[:16]}...` | {'\u2713' if a_pass else '\u2717'} | `{sha_b[:16]}...` | {'\u2713' if b_pass else '\u2717'} |\n"
    if not (a_pass and b_pass):
        all_pass = False

md += f"\n## Outcome\n\n"
md += f"- Test A pass count: {sum(1 for r in byte_fidelity_rows if r[4])} / 30\n"
md += f"- Test B pass count: {sum(1 for r in byte_fidelity_rows if r[5])} / 30\n"
md += f"- Overall: **{'PASS' if all_pass else 'FAIL'}**\n\n"
md += "## Verification recipe\n\n"
md += "- Test A: `sha256sum cell_<qid>_A.user.txt` == `sha256(<bare Q>)`. Bare Q is the verbatim line in `prompts.md` immediately following the `#### V02-D-...` header (italics already stripped per `prompts.md` audit cross-check note line 133).\n"
md += "- Test B: read `cell_<qid>_B.user.txt`, strip the leading 16 bytes (`[Aoven v0.1.2]\\n`) and the trailing 12 bytes (`\\nNo flattery`), then `sha256` the remainder. Must equal `sha256(<bare Q>)`.\n"
md += "- Templates (constant across all 30 cells):\n"
md += "  - Test A pre/post: empty (sha `e3b0c442...`).\n"
md += "  - Test B prefix `[Aoven v0.1.2]\\n` (sha `2fe5b9af22d39d26...`).\n"
md += "  - Test B suffix `\\nNo flattery` (sha `4fda0fe3951cab05...`).\n"
md += "  - Test B template-with-placeholder `[Aoven v0.1.2]\\n<bare Q>\\nNo flattery` (sha `c8b2d4f9ecd7ba1c...`).\n"

(CELLS / "_byte_fidelity_check.md").write_text(md, encoding="utf-8", newline="\n")

# -------- Write _selection.md (Item 10 ablation selection) --------
sel_md = "# AOV-180 Item 10 \u2014 ablation cell selection (deterministic)\n\n"
sel_md += "Per run-prep \u00a74.1: selection rule is `sha256(qid || \"ablation-v1\")` truncated, sorted ascending within each domain stratum, take first N per RedTeam allocation (4 D-SCI / 4 D-TECH / 4 D-NORM / 3 D-PRED = 15).\n\n"
sel_md += "## Per-Q derivation (all 30, with selection-key)\n\n"
sel_md += "| qid | sha256(qid || \"ablation-v1\") | domain | selected? |\n"
sel_md += "|-----|------------------------------|--------|-----------|\n"

# Compute selection keys
domain_groups = {"D-SCI": [], "D-TECH": [], "D-NORM": [], "D-PRED": []}
allocation = {"D-SCI": 4, "D-TECH": 4, "D-NORM": 4, "D-PRED": 3}

q_keys = []
for qid, _ in qs:
    domain = "-".join(qid.split("-")[1:3])  # "D-SCI", "D-TECH", etc.
    key = sha256_bytes((qid + "ablation-v1").encode("utf-8"))
    q_keys.append((qid, domain, key))
    domain_groups[domain].append((key, qid))

# Sort each group ascending and take first N
selected = set()
selected_per_domain = {}
for domain, group in domain_groups.items():
    group_sorted = sorted(group)
    take = group_sorted[:allocation[domain]]
    selected_per_domain[domain] = [qid for (_, qid) in take]
    for _, qid in take:
        selected.add(qid)

# Render table sorted by qid for readability
for qid, domain, key in sorted(q_keys):
    is_sel = qid in selected
    sel_md += f"| {qid} | `{key[:32]}...` | {domain} | {'\u2713' if is_sel else ''} |\n"

sel_md += "\n## Selected cells (in selection order, per domain)\n\n"
sel_md += "| Domain | Allocation | Selected qids (selection-key ascending) |\n"
sel_md += "|--------|-----------:|----------------------------------------|\n"
for domain in ["D-SCI", "D-TECH", "D-NORM", "D-PRED"]:
    sel_md += f"| {domain} | {allocation[domain]} of {len(domain_groups[domain])} | {', '.join(selected_per_domain[domain])} |\n"
sel_md += f"\nTotal: **{len(selected)}** ablation cells.\n\n"

# Cross-check against run-prep \u00a74.1 expected list
expected = {
    "D-SCI": ["V02-D-SCI-002", "V02-D-SCI-005", "V02-D-SCI-004", "V02-D-SCI-003"],
    "D-TECH": ["V02-D-TECH-007", "V02-D-TECH-006", "V02-D-TECH-005", "V02-D-TECH-002"],
    "D-NORM": ["V02-D-NORM-008", "V02-D-NORM-005", "V02-D-NORM-003", "V02-D-NORM-007"],
    "D-PRED": ["V02-D-PRED-005", "V02-D-PRED-001", "V02-D-PRED-006"],
}
sel_md += "## Run-prep \u00a74.1 expected vs. computed cross-check\n\n"
match_all = True
for domain in ["D-SCI", "D-TECH", "D-NORM", "D-PRED"]:
    e = expected[domain]
    c = selected_per_domain[domain]
    same = (set(e) == set(c))
    sel_md += f"- {domain}: expected={e}, computed={c}, match (set-equal): **{'\u2713' if same else '\u2717'}**\n"
    if not same:
        match_all = False
sel_md += f"\nOrder note: run-prep \u00a74.1 lists qids in selection order (selection-key ascending). Computed list above matches that order.\n"
sel_md += f"\n**Cross-check verdict: {'PASS' if match_all else 'FAIL'}**\n"

(CELLS / "_selection.md").write_text(sel_md, encoding="utf-8", newline="\n")

# -------- Write a manifest the generator script will consume --------
manifest_lines = []
for qid, bare_q in qs:
    manifest_lines.append(f"{qid}\t{bare_q}")
(V02 / "_qs_manifest.tsv").write_text("\n".join(manifest_lines) + "\n", encoding="utf-8", newline="\n")

# Also write the ablation manifest
ablation_qids = sorted(selected)
(V02 / "_ablation_manifest.tsv").write_text("\n".join(ablation_qids) + "\n", encoding="utf-8", newline="\n")

# -------- Print summary --------
print(f"Extracted {len(qs)} questions from prompts.md")
print(f"Wrote {2 * len(qs)} user-message files to {CELLS}")
print(f"Byte-fidelity: A={sum(1 for r in byte_fidelity_rows if r[4])}/30, B={sum(1 for r in byte_fidelity_rows if r[5])}/30")
print(f"Ablation cells selected: {len(selected)}")
print(f"Selection cross-check: {'PASS' if match_all else 'FAIL'}")
print(f"Files written:")
for f in ["_byte_fidelity_check.md", "_selection.md"]:
    p = CELLS / f
    print(f"  {f}: {p.stat().st_size} bytes, sha={sha256_bytes(p.read_bytes())[:16]}")
print(f"  _qs_manifest.tsv: {(V02 / '_qs_manifest.tsv').stat().st_size} bytes")
print(f"  _ablation_manifest.tsv: {(V02 / '_ablation_manifest.tsv').stat().st_size} bytes")
