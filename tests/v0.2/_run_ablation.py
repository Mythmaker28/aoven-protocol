#!/usr/bin/env python3
"""Run 45 ablation cells (15 Test B Qs x 3 reruns) under same Item 4 transport.

Captures:
  cells/_ablation/cell_<qid>_B_run{1,2,3}.txt
  cells/_ablation/_provenance_ablation.jsonl
"""
import hashlib
import json
import subprocess
import time
from datetime import datetime, timezone
from pathlib import Path

WORKSPACE = Path(r"C:\Users\tommy\.paperclip\instances\default\workspaces\2ae117a1-f490-4e8e-a693-0f1d8d1d675b")
V02 = WORKSPACE / "aoven-protocol" / "tests" / "v0.2"
CELLS = V02 / "cells"
ABLATION = CELLS / "_ablation"
ABLATION.mkdir(parents=True, exist_ok=True)

CLAUDE_CMD = r"C:\Users\tommy\AppData\Roaming\npm\claude.cmd"
TRANSPORT_STRING = "claude -p --system-prompt '' --tools '' --max-turns 1 --model claude-opus-4-7"
SYSTEM_PROMPT_SHA = "e3b0c44298fc1c149afbf4c8996fb92427ae41e4649b934ca495991b7852b855"
CLAUDEMD_REF = "_claudemd_snapshot.md@ac85bca72a0062fc"
HOOKS_REF = "_hooks_snapshot.md@be31fa08e6fd8d55"
AUTOMEMORY_REF = "_automemory_snapshot.md@ff756723834e2f47"

def sha256_bytes(b: bytes) -> str:
    return hashlib.sha256(b).hexdigest()

def now_iso():
    return datetime.now(timezone.utc).strftime("%Y-%m-%dT%H:%M:%S.%fZ")

ablation_qids = (V02 / "_ablation_manifest.tsv").read_text(encoding="utf-8").strip().split("\n")
assert len(ablation_qids) == 15

provenance_path = ABLATION / "_provenance_ablation.jsonl"
log_path = V02 / "_run_ablation.log"

# Resume support
done_keys = set()
if provenance_path.exists():
    for line in provenance_path.read_text(encoding="utf-8").splitlines():
        if not line.strip():
            continue
        obj = json.loads(line)
        done_keys.add((obj["question_id"], obj["run"]))

log_f = open(log_path, "a", encoding="utf-8")
log_f.write(f"\n=== Ablation run started {now_iso()} ===\n")
log_f.write(f"Already done: {len(done_keys)} / 45\n")
log_f.flush()

prov_f = open(provenance_path, "a", encoding="utf-8")

calls = [(qid, run) for qid in ablation_qids for run in (1, 2, 3)]
assert len(calls) == 45

start_time = time.time()
for i, (qid, run) in enumerate(calls):
    if (qid, run) in done_keys:
        continue

    user_msg_file = CELLS / f"cell_{qid}_B.user.txt"
    user_msg_bytes = user_msg_file.read_bytes()
    user_prompt_sha = sha256_bytes(user_msg_bytes)

    out_file = ABLATION / f"cell_{qid}_B_run{run}.txt"

    started_at = now_iso()
    t0 = time.time()
    try:
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
        output_sha = sha256_bytes(result.stdout)

        prov = {
            "question_id": qid,
            "condition": "B",
            "run": run,
            "model_id": "claude-opus-4-7",
            "system_prompt_sha256": SYSTEM_PROMPT_SHA,
            "user_prompt_sha256": user_prompt_sha,
            "user_prompt_byte_length": len(user_msg_bytes),
            "temperature_actual": None,
            "temperature_intent": 0,
            "temperature_call_site_assertion": False,
            "output_sha256": output_sha,
            "output_byte_length": len(result.stdout),
            "generation_started_at": started_at,
            "generation_completed_at": completed_at,
            "generation_elapsed_seconds": round(elapsed, 3),
            "transport": TRANSPORT_STRING,
            "claudemd_snapshot_ref": CLAUDEMD_REF,
            "hooks_snapshot_ref": HOOKS_REF,
            "automemory_snapshot_ref": AUTOMEMORY_REF,
            "subprocess_returncode": result.returncode,
        }
        prov_f.write(json.dumps(prov, ensure_ascii=False) + "\n")
        prov_f.flush()

        msg = f"[{i+1:2d}/45] {qid} run{run}: {elapsed:5.1f}s, {len(result.stdout):5d}B, sha={output_sha[:12]}"
        print(msg)
        log_f.write(msg + "\n")
        log_f.flush()
    except Exception as e:
        msg = f"[{i+1:2d}/45] {qid} run{run}: ERROR {type(e).__name__}: {e}"
        print(msg)
        log_f.write(msg + "\n")
        log_f.flush()
        raise

total = time.time() - start_time
log_f.write(f"=== Ablation completed in {total:.1f}s ===\n")
log_f.close()
prov_f.close()
print(f"\nAblation done. Total: {total:.1f}s")
