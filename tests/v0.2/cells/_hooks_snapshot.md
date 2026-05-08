# AOV-180 Item 6 — hook configuration snapshot (gen-START)

**Captured:** 2026-05-08T19:27:54Z

## settings.json presence at three locations

| File | Status | Bytes | SHA-256 |
|------|--------|-------|---------|
| `~/.claude/settings.json` | **PRESENT** | 33 | `9306a1e9997fab076f5791a7a64a7fa51fa5132cfef4a0070d07b69d4e14546f` |
| `<workspace>/.claude/settings.json` | **ABSENT** | 0 | n/a |
| `<workspace>/aoven-protocol/.claude/settings.json` | **ABSENT** | 0 | n/a |

## Verbatim content of `~/.claude/settings.json`

```json
{
  "model": "claude-opus-4-7"
}

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

## gen-END snapshot (re-check at 2026-05-08T20:18:40Z)

- `~/.claude/settings.json`: bytes=33, sha=9306a1e9997fab076f5791a7a64a7fa51fa5132cfef4a0070d07b69d4e14546f
- gen-START sha: `9306a1e9997fab076f5791a7a64a7fa51fa5132cfef4a0070d07b69d4e14546f`
- **Delta:** NO CHANGE

- `<workspace>/.claude/settings.json`: ABSENT (unchanged)
- `<workspace>/aoven-protocol/.claude/settings.json`: ABSENT (unchanged)
