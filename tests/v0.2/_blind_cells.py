#!/usr/bin/env python3
"""Identity-blinding rename of cells per pre-reg \u00a73.1d.

Each cell file is renamed by deterministic hash:
  blind_id = sha256(qid + "||" + condition + "||" + cycle_secret).hexdigest()[:16]

The (question_id, condition) -> blind_id mapping is sealed in
  cells/_blinding_seal.json
which is the single source of truth that gets unsealed only after raters seal their pass.

The cycle_secret is read from cells/_cycle_secret.txt (which is generated here using
os.urandom and gitignored; only the seal mapping JSON ships, not the secret).
"""
import hashlib
import json
import os
import secrets
from pathlib import Path

WORKSPACE = Path(r"C:\Users\tommy\.paperclip\instances\default\workspaces\2ae117a1-f490-4e8e-a693-0f1d8d1d675b")
V02 = WORKSPACE / "aoven-protocol" / "tests" / "v0.2"
CELLS = V02 / "cells"
BLIND_DIR = CELLS / "_blinded_corpus"
BLIND_DIR.mkdir(parents=True, exist_ok=True)

# Read or generate cycle secret
secret_path = CELLS / "_cycle_secret.txt"
if secret_path.exists():
    cycle_secret = secret_path.read_text(encoding="utf-8").strip()
else:
    cycle_secret = secrets.token_hex(32)
    secret_path.write_text(cycle_secret, encoding="utf-8", newline="\n")

# Load qids
qs = []
for line in (V02 / "_qs_manifest.tsv").read_text(encoding="utf-8").strip().split("\n"):
    qid, q = line.split("\t", 1)
    qs.append((qid, q))

mapping = {}  # blind_id -> (qid, condition, source_file_relpath, source_sha)

for qid, _ in qs:
    for cond in ("A", "B"):
        # Use stripped Test B for raters; raw Test A for raters (no marker syntax to strip).
        if cond == "A":
            src = CELLS / f"cell_{qid}_A.txt"
        else:
            stripped = CELLS / f"cell_{qid}_B.stripped.txt"
            raw = CELLS / f"cell_{qid}_B.txt"
            src = stripped if stripped.exists() else raw

        if not src.exists():
            print(f"MISSING source for {qid}/{cond}: {src}")
            continue

        blind_id = hashlib.sha256(f"{qid}||{cond}||{cycle_secret}".encode("utf-8")).hexdigest()[:16]
        target = BLIND_DIR / f"{blind_id}.txt"
        target.write_bytes(src.read_bytes())

        mapping[blind_id] = {
            "question_id": qid,
            "condition": cond,
            "source_file": str(src.relative_to(WORKSPACE)).replace("\\", "/"),
            "source_sha256": hashlib.sha256(src.read_bytes()).hexdigest(),
            "byte_length": src.stat().st_size,
        }

# Sealed mapping JSON
seal_path = CELLS / "_blinding_seal.json"
seal = {
    "cycle_secret_sha256": hashlib.sha256(cycle_secret.encode("utf-8")).hexdigest(),
    "scheme": "sha256(qid + '||' + condition + '||' + cycle_secret).hexdigest()[:16]",
    "mapping": mapping,
    "cell_count": len(mapping),
}
seal_path.write_text(json.dumps(seal, ensure_ascii=False, indent=2) + "\n", encoding="utf-8", newline="\n")

# Gitignore the secret file
gitignore_path = CELLS / ".gitignore"
gitignore_lines = ["_cycle_secret.txt\n"]
if gitignore_path.exists():
    existing = gitignore_path.read_text(encoding="utf-8")
    if "_cycle_secret.txt" not in existing:
        gitignore_path.write_text(existing.rstrip() + "\n_cycle_secret.txt\n", encoding="utf-8", newline="\n")
else:
    gitignore_path.write_text("_cycle_secret.txt\n", encoding="utf-8", newline="\n")

print(f"Blinded {len(mapping)} cells -> {BLIND_DIR}")
print(f"Seal mapping JSON: {seal_path} (sha={hashlib.sha256(seal_path.read_bytes()).hexdigest()[:16]})")
print(f"Cycle secret SHA: {seal['cycle_secret_sha256'][:16]}")
