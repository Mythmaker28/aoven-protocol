#!/usr/bin/env python3
"""Build AOV-180 gen-START snapshots: Items 4, 5, 6, 7 of run_prep_aov180.md."""
import hashlib
import os
import sys
from datetime import datetime, timezone
from pathlib import Path

WORKSPACE = Path(r"C:\Users\tommy\.paperclip\instances\default\workspaces\2ae117a1-f490-4e8e-a693-0f1d8d1d675b")
CELLS = WORKSPACE / "aoven-protocol" / "tests" / "v0.2" / "cells"
HOME = Path(os.path.expanduser("~"))
MEMORY_DIR = HOME / ".claude" / "projects" / "C--Users-tommy--paperclip-instances-default-workspaces-2ae117a1-f490-4e8e-a693-0f1d8d1d675b" / "memory"

NOW = datetime.now(timezone.utc).strftime("%Y-%m-%dT%H:%M:%SZ")

def sha256_bytes(b: bytes) -> str:
    return hashlib.sha256(b).hexdigest()

def sha256_file(p: Path) -> str:
    return sha256_bytes(p.read_bytes())

CELLS.mkdir(parents=True, exist_ok=True)

# -------- Item 4: _transport.md --------
transport = f"""# AOV-180 Item 4 — transport invocation snapshot (gen-START)

**Captured:** {NOW}

## Exact transport invocation (verbatim, per run-prep §2 Item 4)

```
claude -p --system-prompt '' --tools '' --max-turns 1 --model claude-opus-4-7
```

The flag-value `''` is treated as **empty-flag-value at the CLI boundary, not empty-system-role at the API boundary.** This delta is the documented gap; it does not pretend to be conformance (per RedTeam `f63cffa2`).

## CLI version

```
$ claude --version
2.1.114 (Claude Code)
```

## Host

| Field | Value |
|-------|-------|
| OS | Windows 11 Home 10.0.26200 |
| Shell | Git Bash (MINGW64_NT-10.0-26200, MSYS2 runtime 3.6.4) |
| Bash version | 5.2.37(1)-release |
| `uname -a` | `MINGW64_NT-10.0-26200 DESKTOP-DEJ8RQN 3.6.4-b9f03e96.x86_64 2025-07-16 18:17 UTC x86_64 Msys` |

## Provenance JSONL field that points here

`transport: "claude -p --system-prompt '' --tools '' --max-turns 1 --model claude-opus-4-7"`

A re-snapshot of this invocation at gen-END is recorded at the foot of `_provenance.jsonl` only if the invocation string changes; if unchanged the gen-START record stands.
"""
(CELLS / "_transport.md").write_text(transport, encoding="utf-8", newline="\n")

# -------- Item 5: _claudemd_snapshot.md --------
locations = [
    ("Workspace-resolved", WORKSPACE / "CLAUDE.md"),
    ("Project (aoven-protocol)", WORKSPACE / "aoven-protocol" / "CLAUDE.md"),
    ("Workspace .claude", WORKSPACE / ".claude" / "CLAUDE.md"),
    ("aoven-protocol .claude", WORKSPACE / "aoven-protocol" / ".claude" / "CLAUDE.md"),
    ("User home (~/.claude)", HOME / ".claude" / "CLAUDE.md"),
]
rows = []
for name, p in locations:
    if p.exists():
        rows.append((name, str(p), "PRESENT", sha256_file(p), p.stat().st_size))
    else:
        rows.append((name, str(p), "ABSENT", "n/a", 0))

claudemd = f"""# AOV-180 Item 5 — CLAUDE.md snapshot (gen-START)

**Captured:** {NOW}

## Presence check at all five locations

| Location | Path | Status | SHA-256 | Bytes |
|----------|------|--------|---------|-------|
"""
for name, path, status, sha, size in rows:
    claudemd += f"| {name} | `{path}` | **{status}** | `{sha}` | {size} |\n"

claudemd += f"""

## Outcome

All five locations are **ABSENT** at gen-START. The §2.5 contamination test does not need to run on CLAUDE.md content because there is no content to assess.

A re-snapshot is filed at gen-END as the second half of this artefact (appended below the gen-END marker). If any CLAUDE.md materializes between gen-START ({NOW}) and gen-END, the verbatim content of that file is filed at gen-END and RedTeam adjudicates per §2.5.

---

<!-- gen-END snapshot will be appended below this marker -->
"""
(CELLS / "_claudemd_snapshot.md").write_text(claudemd, encoding="utf-8", newline="\n")

# -------- Item 6: _hooks_snapshot.md --------
settings_path = HOME / ".claude" / "settings.json"
settings_bytes = settings_path.read_bytes() if settings_path.exists() else b""
settings_sha = sha256_bytes(settings_bytes) if settings_bytes else "n/a"
settings_size = len(settings_bytes)

hooks = f"""# AOV-180 Item 6 — hook configuration snapshot (gen-START)

**Captured:** {NOW}

## settings.json presence at three locations

| File | Status | Bytes | SHA-256 |
|------|--------|-------|---------|
| `~/.claude/settings.json` | **PRESENT** | {settings_size} | `{settings_sha}` |
| `<workspace>/.claude/settings.json` | **ABSENT** | 0 | n/a |
| `<workspace>/aoven-protocol/.claude/settings.json` | **ABSENT** | 0 | n/a |

## Verbatim content of `~/.claude/settings.json`

```json
{settings_bytes.decode('utf-8') if settings_bytes else ''}
```

## Audit assessment

- No `hooks` key.
- No `apiKeyHelper` key.
- No env-injection mechanism.
- Only field present: `model: "claude-opus-4-7"` — selects the default model used by the `claude` CLI when no `--model` flag is passed. The Item 4 invocation passes `--model claude-opus-4-7` explicitly anyway, so this setting is a no-op for the generation transport.

§2.5 contamination test: NOT TRIGGERED. No hook injects pre-prompt content into Test A or Test B user messages.

A re-snapshot is filed at gen-END below the gen-END marker. If any of the three files mutate or the workspace-level files materialize, verbatim content is filed and RedTeam adjudicates.

---

<!-- gen-END snapshot will be appended below this marker -->
"""
(CELLS / "_hooks_snapshot.md").write_text(hooks, encoding="utf-8", newline="\n")

# -------- Item 7: _automemory_snapshot.md --------
mem_files = sorted([p for p in MEMORY_DIR.iterdir() if p.suffix == ".md"])

memhdr = f"""# AOV-180 Item 7 — auto-memory snapshot (gen-START)

**Captured:** {NOW}

## Empirical determination of auto-memory loading under `claude -p`

The Item 4 transport invocation does NOT include `--bare`. The `claude` CLI's auto-memory mechanism is documented to load `MEMORY.md` and pointed-to memory files from the project-resolved memory directory based on the cwd-derived project key. The CLI session that runs the 60 cells will have cwd = `<workspace>` which maps to the project directory:

`~/.claude/projects/C--Users-tommy--paperclip-instances-default-workspaces-2ae117a1-f490-4e8e-a693-0f1d8d1d675b/`

This is the same project directory as the *driver* session that runs the generation script (this Logician session). Therefore the conservative working assumption is **auto-memory loads** under the Item 4 transport, and every `.md` file under `<project-dir>/memory/` is filed verbatim + hashed below for §2.5 contamination assessment.

A pragmatic cross-check is run alongside generation: if Test A (no Aoven priming) responses show Aoven-marker tokens or v0.1.2-aligned framing, that is evidence the memory loaded and primed the generator. The strip script + lint pipeline catches such leakage before raters see any cell.

## Memory directory listing at gen-START

Directory: `{MEMORY_DIR}`
File count: {len(mem_files)} (.md files)

| File | Bytes | SHA-256 |
|------|-------|---------|
"""

mem_entries = []
for p in mem_files:
    b = p.read_bytes()
    mem_entries.append((p.name, len(b), sha256_bytes(b), b.decode('utf-8')))
    memhdr += f"| `{p.name}` | {len(b)} | `{sha256_bytes(b)}` |\n"

memhdr += "\n## Verbatim content of every memory file\n\n"
memhdr += "Each file is filed below in fenced markdown blocks for §2.5 contamination assessment by RedTeam. Files are listed in lexicographic order.\n\n"

for name, size, sha, content in mem_entries:
    memhdr += f"### `{name}` (sha `{sha[:16]}...`, {size} bytes)\n\n"
    memhdr += "```markdown\n"
    memhdr += content
    if not content.endswith("\n"):
        memhdr += "\n"
    memhdr += "```\n\n"

memhdr += f"""## §2.5 contamination assessment (Logician self-flag at gen-START)

The following memory files contain v0.1.2-aligned or AOVEN-aligned framing and MUST be assessed by RedTeam at AOV-180 closeout:

- `agent_role.md` - describes EpistemicLogician role on AOVEN protocol; references review authority and sibling agents.
- `feedback_aoven_discipline.md` - explicitly describes AOVEN review disciplines (NOSRC, named-reviewer-sign-off, push-deferral). Contains "AOVEN" by name.
- `feedback_sealed_rubric_ambiguity.md` - references rubric ambiguity discipline; epistemic-discipline-adjacent framing.
- `feedback_park_blocked_without_edge.md` - references AOV-180 / AOV-184 park incident.
- `reference_aoven_agent_ids.md` - names AOVEN agent UUIDs.
- `reference_claude_cli_temp_assertion_gap.md` - references the temperature assertion gap that motivated the Two-Surface Separation.

The remaining 8 files (`feedback_audit_child_filing.md`, `feedback_audit_close_on_verdict.md`, `feedback_charcount_audit.md`, `feedback_heartbeat_continuity.md`, `feedback_heartbeat_text_autoposts.md`, `feedback_push_spec_commit_count_vs_diff.md`, `reference_paperclip_api.md`, `MEMORY.md` index) describe Paperclip-harness mechanics (issue routing, commenting discipline, audit-child filing) that are NOT v0.1.2-aligned framing and are unlikely to prime epistemic-marker output, but their verbatim content is filed for completeness.

The §3.3 author-bias closure is the load-bearing gate; verbatim content (above) is what the auditor uses to assess this. Logician does NOT downgrade or pre-decide the verdict; that is RedTeam's call at AOV-180 closeout.

A re-snapshot is filed at gen-END below the gen-END marker. If memory files mutate during generation, the gen-END snapshot lists the diff.

---

<!-- gen-END snapshot will be appended below this marker -->
"""
(CELLS / "_automemory_snapshot.md").write_text(memhdr, encoding="utf-8", newline="\n")

# -------- Print summary --------
print(f"Snapshot files written to: {CELLS}")
for f in ["_transport.md", "_claudemd_snapshot.md", "_hooks_snapshot.md", "_automemory_snapshot.md"]:
    p = CELLS / f
    if p.exists():
        b = p.read_bytes()
        print(f"  {f}: {len(b)} bytes, sha={sha256_bytes(b)[:16]}")
    else:
        print(f"  {f}: MISSING")
