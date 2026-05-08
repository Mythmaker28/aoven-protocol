#!/usr/bin/env python3
"""Run the 60 main cells (30 Q x {A, B}) under the Item 4 transport invocation.

Captures:
  - cell_<qid>_<cond>.txt        (raw model output bytes)
  - _provenance.jsonl            (60 lines, one JSON object per cell)

Transport: claude -p --system-prompt '' --tools '' --max-turns 1 --model claude-opus-4-7
"""
import hashlib
import json
import subprocess
import sys
import time
from datetime import datetime, timezone
from pathlib import Path

WORKSPACE = Path(r"C:\Users\tommy\.paperclip\instances\default\workspaces\2ae117a1-f490-4e8e-a693-0f1d8d1d675b")
V02 = WORKSPACE / "aoven-protocol" / "tests" / "v0.2"
CELLS = V02 / "cells"

TRANSPORT_STRING = "claude -p --system-prompt '' --tools '' --max-turns 1 --model claude-opus-4-7"
CLAUDE_CMD = r"C:\Users\tommy\AppData\Roaming\npm\claude.cmd"

# Snapshot SHAs (recorded in each provenance row)
CLAUDEMD_REF = "_claudemd_snapshot.md@ac85bca72a0062fc"
HOOKS_REF = "_hooks_snapshot.md@be31fa08e6fd8d55"
AUTOMEMORY_REF = "_automemory_snapshot.md@ff756723834e2f47"

SYSTEM_PROMPT_SHA = "e3b0c44298fc1c149afbf4c8996fb92427ae41e4649b934ca495991b7852b855"  # empty

def sha256_bytes(b: bytes) -> str:
    return hashlib.sha256(b).hexdigest()

def now_iso():
    return datetime.now(timezone.utc).strftime("%Y-%m-%dT%H:%M:%S.%fZ")

# Load qs manifest
qs = []
for line in (V02 / "_qs_manifest.tsv").read_text(encoding="utf-8").strip().split("\n"):
    qid, q = line.split("\t", 1)
    qs.append((qid, q))
assert len(qs) == 30

# Build cell list: 30 Qs x {A, B}
cells_to_run = []
for qid, _ in qs:
    cells_to_run.append((qid, "A"))
    cells_to_run.append((qid, "B"))
assert len(cells_to_run) == 60

provenance_path = CELLS / "_provenance.jsonl"
log_path = V02 / "_run_main_cells.log"

# Resume support: if provenance file exists, skip cells already logged
done_keys = set()
if provenance_path.exists():
    for line in provenance_path.read_text(encoding="utf-8").splitlines():
        if not line.strip():
            continue
        obj = json.loads(line)
        done_keys.add((obj["question_id"], obj["condition"]))

log_f = open(log_path, "a", encoding="utf-8")
log_f.write(f"\n=== Run started {now_iso()} ===\n")
log_f.write(f"Already done: {len(done_keys)} / 60\n")
log_f.flush()

provenance_f = open(provenance_path, "a", encoding="utf-8")

start_time = time.time()
for i, (qid, cond) in enumerate(cells_to_run):
    if (qid, cond) in done_keys:
        continue

    user_msg_file = CELLS / f"cell_{qid}_{cond}.user.txt"
    user_msg_bytes = user_msg_file.read_bytes()
    user_prompt_sha = sha256_bytes(user_msg_bytes)

    out_file = CELLS / f"cell_{qid}_{cond}.txt"
    err_file = CELLS / f"cell_{qid}_{cond}.stderr.txt"

    started_at = now_iso()
    t0 = time.time()
    try:
        # Pipe user_msg bytes to stdin of `claude -p` via the .cmd shim (Windows, full path)
        result = subprocess.run(
            [CLAUDE_CMD, "-p", "--system-prompt", "", "--tools", "", "--max-turns", "1", "--model", "claude-opus-4-7"],
            input=user_msg_bytes,
            capture_output=True,
            timeout=180,
            cwd=str(WORKSPACE),
            shell=False,
        )
        completed_at = now_iso()
        elapsed = time.time() - t0

        out_file.write_bytes(result.stdout)
        if result.stderr:
            err_file.write_bytes(result.stderr)

        output_sha = sha256_bytes(result.stdout)
        output_len = len(result.stdout)

        prov = {
            "question_id": qid,
            "condition": cond,
            "model_id": "claude-opus-4-7",
            "system_prompt_sha256": SYSTEM_PROMPT_SHA,
            "user_prompt_sha256": user_prompt_sha,
            "user_prompt_byte_length": len(user_msg_bytes),
            "temperature_actual": None,
            "temperature_intent": 0,
            "temperature_call_site_assertion": False,
            "max_tokens": None,
            "stop_sequences": None,
            "output_sha256": output_sha,
            "output_byte_length": output_len,
            "generation_started_at": started_at,
            "generation_completed_at": completed_at,
            "generation_elapsed_seconds": round(elapsed, 3),
            "transport": TRANSPORT_STRING,
            "claudemd_snapshot_ref": CLAUDEMD_REF,
            "hooks_snapshot_ref": HOOKS_REF,
            "automemory_snapshot_ref": AUTOMEMORY_REF,
            "subprocess_returncode": result.returncode,
        }
        provenance_f.write(json.dumps(prov, ensure_ascii=False) + "\n")
        provenance_f.flush()

        msg = f"[{i+1:2d}/60] {qid} {cond}: {elapsed:5.1f}s, {output_len:5d}B, sha={output_sha[:12]}, rc={result.returncode}"
        print(msg)
        log_f.write(msg + "\n")
        log_f.flush()
    except subprocess.TimeoutExpired:
        msg = f"[{i+1:2d}/60] {qid} {cond}: TIMEOUT after 120s"
        print(msg)
        log_f.write(msg + "\n")
        log_f.flush()
        sys.exit(1)
    except Exception as e:
        msg = f"[{i+1:2d}/60] {qid} {cond}: ERROR {type(e).__name__}: {e}"
        print(msg)
        log_f.write(msg + "\n")
        log_f.flush()
        sys.exit(2)

total_elapsed = time.time() - start_time
log_f.write(f"=== Run completed in {total_elapsed:.1f}s ===\n")
log_f.close()
provenance_f.close()
print(f"\nDone. Total elapsed: {total_elapsed:.1f}s")
