# AOV-180 Item 4 — transport invocation snapshot (gen-START)

**Captured:** 2026-05-08T19:27:54Z

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
