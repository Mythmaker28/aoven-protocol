#!/usr/bin/env python3
"""Re-snapshot CLAUDE.md / hooks / auto-memory at gen-END and append to existing
snapshot files below the gen-END marker. Compute and report any deltas vs gen-START."""
import hashlib
import os
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

def append_section(file_path: Path, content: str):
    existing = file_path.read_text(encoding="utf-8")
    file_path.write_text(existing + "\n" + content, encoding="utf-8", newline="\n")

# -------- CLAUDE.md re-check --------
locations = [
    ("Workspace-resolved", WORKSPACE / "CLAUDE.md"),
    ("Project (aoven-protocol)", WORKSPACE / "aoven-protocol" / "CLAUDE.md"),
    ("Workspace .claude", WORKSPACE / ".claude" / "CLAUDE.md"),
    ("aoven-protocol .claude", WORKSPACE / "aoven-protocol" / ".claude" / "CLAUDE.md"),
    ("User home (~/.claude)", HOME / ".claude" / "CLAUDE.md"),
]
claudemd_section = f"## gen-END snapshot (re-check at {NOW})\n\n"
claudemd_section += "| Location | Path | Status | SHA-256 |\n"
claudemd_section += "|----------|------|--------|--------|\n"
any_present = False
for name, p in locations:
    if p.exists():
        any_present = True
        claudemd_section += f"| {name} | `{p}` | **PRESENT** | `{sha256_file(p)}` |\n"
    else:
        claudemd_section += f"| {name} | `{p}` | **ABSENT** | n/a |\n"
claudemd_section += f"\n**Delta vs gen-START:** {'CONTAMINATION DETECTED \u2014 RedTeam adjudicates per \u00a72.5' if any_present else 'no change \u2014 all locations remain ABSENT'}\n"
append_section(CELLS / "_claudemd_snapshot.md", claudemd_section)

# -------- Hooks re-check --------
settings_path = HOME / ".claude" / "settings.json"
settings_bytes = settings_path.read_bytes() if settings_path.exists() else b""
settings_sha = sha256_bytes(settings_bytes) if settings_bytes else "n/a"

GEN_START_HOOKS_SHA = "9306a1e9997fab076f5791a7a64a7fa51fa5132cfef4a0070d07b69d4e14546f"
hooks_section = f"## gen-END snapshot (re-check at {NOW})\n\n"
hooks_section += f"- `~/.claude/settings.json`: bytes={len(settings_bytes)}, sha={settings_sha}\n"
hooks_section += f"- gen-START sha: `{GEN_START_HOOKS_SHA}`\n"
hooks_section += f"- **Delta:** {'NO CHANGE' if settings_sha == GEN_START_HOOKS_SHA else 'CHANGED \u2014 verbatim diff below'}\n\n"
if settings_sha != GEN_START_HOOKS_SHA:
    hooks_section += "Verbatim content at gen-END:\n```json\n" + (settings_bytes.decode("utf-8") if settings_bytes else "") + "\n```\n"
ws_settings = WORKSPACE / ".claude" / "settings.json"
ap_settings = WORKSPACE / "aoven-protocol" / ".claude" / "settings.json"
hooks_section += f"- `<workspace>/.claude/settings.json`: {'PRESENT (sha=' + sha256_file(ws_settings) + ')' if ws_settings.exists() else 'ABSENT (unchanged)'}\n"
hooks_section += f"- `<workspace>/aoven-protocol/.claude/settings.json`: {'PRESENT (sha=' + sha256_file(ap_settings) + ')' if ap_settings.exists() else 'ABSENT (unchanged)'}\n"
append_section(CELLS / "_hooks_snapshot.md", hooks_section)

# -------- Auto-memory re-check --------
GEN_START_MEM_SHAS = {
    "MEMORY.md": "5423c3b87022c0b601b99b6f194073c4e38afc62d643ad727163d20c0d852dd1",
    "agent_role.md": "66cedb75cf61a9a283f3ac3dd67f5e6713648b12386c77ed564fa223ab28fdeb",
    "feedback_aoven_discipline.md": "35c8ca44933b964e2a6c1c07f8c65c21e01b26708899fd701d05a4bc238b1a79",
    "feedback_audit_child_filing.md": "cf505a35b8cfe9d9704eabc0fa3351cd811507cb57403aefe33ea213a661ecb5",
    "feedback_audit_close_on_verdict.md": "dc754a2e0d1e8350c57b3e7eb35747b389c2c549ff3dbc42b221b0699498e8b7",
    "feedback_charcount_audit.md": "3cd8ee219c7ff6cba14266ac6df8815eac9e092ebe8d3da462eb230a8fd60562",
    "feedback_heartbeat_continuity.md": "1829e029109c612ba8f0822acb93a410107455b7d6fcac881045105d0a0899c5",
    "feedback_heartbeat_text_autoposts.md": "eb068930aa06383707e3bbf2d016cbfb4ca3b00c6ea54e78ba456066b93e91df",
    "feedback_park_blocked_without_edge.md": "5d010c29f41f5b537105958e341b298d027cb92b4cf6a6bb002612b71e5a364f",
    "feedback_push_spec_commit_count_vs_diff.md": "41a47a476b8b45a62196d1b00651e374a0d8cb7f0cd7080c8d0ba66cd131115d",
    "feedback_sealed_rubric_ambiguity.md": "3af78b64d94770d574637ce42c4481cba83d6cd7d5c4d2e90c93b5b6c6e5cf55",
    "reference_aoven_agent_ids.md": "b3b1d0d08177aded44e49714e16fa1171a42a713d4904633784320d268dfb4e9",
    "reference_claude_cli_temp_assertion_gap.md": "c555f6eb7b14fd46644ff1a81d77502f3f046cc78b7e2bc73fa0247ddc80e25a",
    "reference_paperclip_api.md": "4c10dad9068f8123961e4b0bd4a441abadb77157af46712f4c9a85f2c27d2e2e",
}
mem_files = sorted([p for p in MEMORY_DIR.iterdir() if p.suffix == ".md"])
mem_section = f"## gen-END snapshot (re-check at {NOW})\n\n"
mem_section += "| File | gen-START sha | gen-END sha | delta |\n"
mem_section += "|------|---------------|--------------|-------|\n"
deltas = []
current_names = set()
for p in mem_files:
    cur = sha256_file(p)
    current_names.add(p.name)
    prev = GEN_START_MEM_SHAS.get(p.name)
    if prev is None:
        delta = "**NEW (added during generation)**"
        deltas.append(("NEW", p.name))
    elif prev != cur:
        delta = "**MUTATED**"
        deltas.append(("MUTATED", p.name))
    else:
        delta = "unchanged"
    mem_section += f"| `{p.name}` | `{(prev or 'n/a')[:16]}...` | `{cur[:16]}...` | {delta} |\n"
# Removed files
for name in GEN_START_MEM_SHAS:
    if name not in current_names:
        mem_section += f"| `{name}` | `{GEN_START_MEM_SHAS[name][:16]}...` | (removed) | **REMOVED** |\n"
        deltas.append(("REMOVED", name))

if deltas:
    mem_section += f"\n**Delta summary:** {len(deltas)} memory file(s) changed during generation:\n"
    for tag, name in deltas:
        mem_section += f"- {tag}: `{name}`\n"
    mem_section += "\nVerbatim post-change content of changed files (for RedTeam \u00a72.5 adjudication):\n\n"
    for tag, name in deltas:
        if tag == "REMOVED":
            mem_section += f"### `{name}` (REMOVED)\n\nNo current content; gen-START verbatim is in the gen-START section above.\n\n"
        else:
            p = MEMORY_DIR / name
            content = p.read_text(encoding="utf-8")
            mem_section += f"### `{name}` ({tag}, gen-END sha `{sha256_file(p)[:16]}...`)\n\n"
            mem_section += "```markdown\n" + content
            if not content.endswith("\n"):
                mem_section += "\n"
            mem_section += "```\n\n"
else:
    mem_section += f"\n**Delta vs gen-START:** no change \u2014 all 14 memory files unchanged.\n"

append_section(CELLS / "_automemory_snapshot.md", mem_section)

print(f"gen-END snapshot appended at {NOW}")
print(f"  CLAUDE.md: any present = {any_present}")
print(f"  hooks settings.json: {'changed' if settings_sha != GEN_START_HOOKS_SHA else 'unchanged'}")
print(f"  memory deltas: {len(deltas)}")
