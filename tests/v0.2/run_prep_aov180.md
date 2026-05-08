# AOV-180 run-prep — composite Surface 1 + Surface 2 closeout binding

**Issue:** AOV-180 [V02-GEN-PHASE4] EpistemicLogician: v0.2 Test A + Test B response generation (60 cells)
**Author:** EpistemicLogician (`2ae117a1`)
**Authority:** RedTeam ruling `f63cffa2` on AOV-217 (PASS-WITH-MOD on Two-Surface Separation, 2026-05-08T16:08:07Z) supersedes the call-site reading of `2feb28b3` on Surface 2 only; Surface 1 is unchanged.
**Status:** This document is the AOV-180 closeout gate spec. AOV-180 closes only when each of the 10 binding items below is satisfied with the artefact named.

---

## §0 — Two-Surface Separation (recap of `f63cffa2`)

`2feb28b3` collapsed two distinct binding surfaces. RedTeam separated them on AOV-217:

- **Surface 1 — Prompt-template byte-fidelity.** Bare-header form, byte-identical modulo `<bare Q>`. **STRICT, UNCHANGED.** Motivation: §3.3 author-bias closure.
- **Surface 2 — Sampling-config + system-role assertion.** Temp 0 + empty system role at API boundary. **RELAXED to documented + characterized + sensitivity-audited** with three teeth (transport-named, injection-surface-snapshotted, sampling-config-ablated).

If any item below is missing or fails the bar at AOV-180 closeout, RedTeam re-blocks. No CEO downgrade pre-empts (`feedback_passwithmod_no_ceo_downgrade.md`).

---

## §1 — Surface 1 closeout bindings (1, 2, 3 — STRICT, from `2feb28b3`)

### Item 1 — prompt-template SHA-256 (pre-question text)

| Cell | pre-question template literal | SHA-256 |
|------|-------------------------------|---------|
| Test A | `""` (empty) | `e3b0c44298fc1c149afbf4c8996fb92427ae41e4649b934ca495991b7852b855` |
| Test B | `[Aoven v0.1.2]\n` | `2fe5b9af22d39d26f27416c0b3fee121f703908c4aed5f61adb81d8d6fdb6c75` |

Test B post-question template literal: `\nNo flattery` — SHA-256 `4fda0fe3951cab055d1f4c6e0f564e691288b387cde5fb0313005bfc8c5e39fb`.
Test B template-with-placeholder string `[Aoven v0.1.2]\n<bare Q>\nNo flattery` — SHA-256 `c8b2d4f9ecd7ba1c1bbee095ed10d5e94ab8b721ac91ae392979ae894d7508ff` (auditor cross-check).

The `\n` in the templates is a single LF byte (`0x0a`). No CRLF.

### Item 2 — byte-identity verification

For each Q in `prompts.md` (sealed @ `022ce620d731a96fa8cbe4bf11ab415eca1f92d5af25c83ed103fbdd40ebe2bc`):

- Test A user message MUST equal `<bare Q>` exactly (no leading/trailing whitespace, no header, no footer). `sha256sum cell_<qid>_A.user.txt == sha256(<bare Q>)`.
- Test B user message MUST equal `[Aoven v0.1.2]\n<bare Q>\nNo flattery` exactly. `sha256sum cell_<qid>_B.user.txt`, with the `[Aoven v0.1.2]\n` prefix and `\nNo flattery` suffix stripped, MUST equal `sha256(<bare Q>)`.

Closeout artefact: `tests/v0.2/cells/_byte_fidelity_check.md` listing 30 (qid, sha256(bare Q), sha256(Test A user msg), sha256(Test B user msg), pass/fail) rows. All 30 rows MUST pass.

### Item 3 — user-message construction

| Cell | user message form | system role |
|------|-------------------|-------------|
| Test A | `<bare Q>` only | empty (see Surface 2 caveat below) |
| Test B | `[Aoven v0.1.2]\n<bare Q>\nNo flattery` | empty (see Surface 2 caveat below) |

The 30 bare Qs are the verbatim text of `prompts.md` §"Bare prompt list — 30 questions" entries (italics stripped per the file's audit cross-check note line 133).

---

## §2 — Surface 2 closeout bindings (4, 5, 6, 7 — RELAXED-WITH-TEETH, from `f63cffa2`)

### Item 4 — transport invocation string verbatim

```
claude -p --system-prompt '' --tools '' --max-turns 1 --model claude-opus-4-7
```

Per RedTeam: *"the flag-value `''` is treated as **empty-flag-value at the CLI boundary, not empty-system-role at the API boundary.** This delta is the documented gap; it does not pretend to be conformance."*

Closeout artefact: `tests/v0.2/cells/_transport.md` recording the exact invocation, the CLI version (`claude --version`), the OS/shell, and the host (Windows / Git Bash / `OS Version: Windows 11 Home 10.0.26200`).

### Item 5 — CLAUDE.md snapshot at generation time

Three locations to snapshot:

| Location | Status at run-prep time (2026-05-08) | SHA-256 |
|----------|--------------------------------------|---------|
| Workspace-resolved (`<workspace>/CLAUDE.md`) | **absent** (`ls` returns "No such file or directory") | n/a |
| `~/.claude/CLAUDE.md` | **absent** | n/a |
| Project-level (`<workspace>/aoven-protocol/CLAUDE.md` and `<workspace>/.claude/CLAUDE.md` and `<workspace>/aoven-protocol/.claude/CLAUDE.md`) | **all absent** | n/a |

If absence holds at generation time, the closeout artefact `tests/v0.2/cells/_claudemd_snapshot.md` MUST record "absent" for each location with a re-`ls` proof timestamp at generation start AND end. If any CLAUDE.md appears between run-prep and generation, the verbatim content is filed in the snapshot doc, hashed, and the §2.5 contamination test (below) runs against it.

**Contamination test (RedTeam re-block trigger).** If any CLAUDE.md found at generation time materially primes Test B for any of: anti-flattery framing, marker-tag use, Aoven references, epistemic discipline framing, calibrated-confidence priming, or §3.3-relevant author-mind state — RedTeam re-blocks. The §3.3 author-bias closure is the load-bearing gate; verbatim content (not just hash) is what the auditor uses to assess this.

### Item 6 — hook configuration snapshot

| File | Status at run-prep time | SHA-256 | Verbatim |
|------|-------------------------|---------|----------|
| `~/.claude/settings.json` | present, 33 bytes | `9306a1e9997fab076f5791a7a64a7fa51fa5132cfef4a0070d07b69d4e14546f` | `{\n  "model": "claude-opus-4-7"\n}\n` (no `hooks` key, no `apiKeyHelper`, no env injection) |
| `<workspace>/.claude/settings.json` | **absent** | n/a | n/a |
| `<workspace>/aoven-protocol/.claude/settings.json` | **absent** | n/a | n/a |

Re-snapshot at generation start AND end. If any `hooks` key materializes between run-prep and generation, the verbatim hooks block is filed and assessed for contamination per §2.5.

### Item 7 — auto-memory load state snapshot

The CLI session that runs the 60-cell generation MUST be auto-memory-disabled OR have its loaded memory content filed verbatim + hashed in `tests/v0.2/cells/_automemory_snapshot.md`.

**Mechanism — auto-memory-disabled path (preferred).** The transport invocation in Item 4 (`claude -p --system-prompt '' --tools '' --max-turns 1 --model claude-opus-4-7`) does NOT include `--bare`. Empirical determination of whether `claude -p` (non-`--bare`) loads auto-memory in single-turn mode is required at generation start: list any `.md` file paths that the CLI session reads from `~/.claude/projects/.../memory/` (e.g. by stracing the process or, more pragmatically, by snapshotting `~/.claude/projects/<this-session-projectname>/memory/MEMORY.md` and any files it points to, hashing all of them, and filing as "loaded — assumed by default" if memory loading cannot be empirically disabled).

**Conservative fallback.** If memory loading cannot be empirically disabled, every memory file under `~/.claude/projects/C--Users-tommy--paperclip-instances-default-workspaces-2ae117a1-f490-4e8e-a693-0f1d8d1d675b/memory/` (this session's memory dir) at generation start is hashed AND filed verbatim in the snapshot doc. Any file containing v0.1.2-aligned framing (Aoven references, anti-flattery framing, calibrated-confidence priming, marker-tag mention) triggers the §2.5 contamination test.

The current MEMORY.md index has 14 entries (per `MEMORY.md`); none of the entries should reference Aoven priming framing — but verbatim content of each pointed-to file MUST be included in the snapshot for verification.

---

## §3 — Provenance log (Item 8, pre-reg §3 binding, augmented per `f63cffa2`)

For each of the 60 cells, log the following at generation time. File: `tests/v0.2/cells/_provenance.jsonl`, one JSON object per cell:

```json
{
  "question_id": "V02-D-SCI-001",
  "condition": "A",
  "model_id": "claude-opus-4-7",
  "system_prompt_sha256": "e3b0c44298fc1c149afbf4c8996fb92427ae41e4649b934ca495991b7852b855",
  "user_prompt_sha256": "<sha256 of the exact bytes sent as user message>",
  "temperature_actual": null,
  "temperature_intent": 0,
  "temperature_call_site_assertion": false,
  "max_tokens": null,
  "stop_sequences": null,
  "output_sha256": "<sha256 of the model output bytes>",
  "output_byte_length": 0,
  "generation_started_at": "2026-05-XX...",
  "generation_completed_at": "2026-05-XX...",
  "transport": "claude -p --system-prompt '' --tools '' --max-turns 1 --model claude-opus-4-7",
  "claudemd_snapshot_ref": "_claudemd_snapshot.md@<sha>",
  "hooks_snapshot_ref": "_hooks_snapshot.md@<sha>",
  "automemory_snapshot_ref": "_automemory_snapshot.md@<sha>"
}
```

`temperature_actual` is `null` because the `claude -p` CLI does not expose a temperature flag and Anthropic's response API does not return the temperature in use. The Two-Surface Separation explicitly accepts this; the `temperature_call_site_assertion: false` field makes the gap machine-readable for v0.3 retake comparison.

Per pre-reg §3 also: rater config (each invocation logs model id, system prompt SHA, tools, temperature, seed, output SHA) — that block is filed at Phase 5 rater-time and is not part of AOV-180 closeout, but the schema above is the v0.2 generator-side analogue.

---

## §4 — Ablation pass plan (Items 9 + 10, RedTeam-strengthened)

### §4.1 — Cell selection (Item 10)

Selection rule: `sha256(question_id || "ablation-v1")` truncated, sorted ascending within each domain stratum, take first N per RedTeam allocation (4 D-SCI / 4 D-TECH / 4 D-NORM / 3 D-PRED = 15).

**Selected cells (deterministic, locked at this commit):**

| Domain | Selected question_ids (in selection order) |
|--------|-------------------------------------------|
| D-SCI (4 of 9) | V02-D-SCI-002, V02-D-SCI-005, V02-D-SCI-004, V02-D-SCI-003 |
| D-TECH (4 of 7) | V02-D-TECH-007, V02-D-TECH-006, V02-D-TECH-005, V02-D-TECH-002 |
| D-NORM (4 of 8) | V02-D-NORM-008, V02-D-NORM-005, V02-D-NORM-003, V02-D-NORM-007 |
| D-PRED (3 of 6) | V02-D-PRED-005, V02-D-PRED-001, V02-D-PRED-006 |

Reproducibility: every reader can verify by computing `sha256((qid + "ablation-v1").encode()).hexdigest()`, sorting ascending within domain, and taking the first N. The selection is deterministic and audit-traceable; no author curation occurred at any step.

### §4.2 — Per-cell re-runs and stability criterion (Item 9)

- **3 generation calls per ablation cell** under the Item 4 transport invocation, run back-to-back (≤ 60 s total per cell).
- Ablation runs **only the Test B cell** for each selected qid (Test B is where the §3.3 author-bias closure has the highest stakes; ablating both A and B doubles the call budget without adding signal on the dominant question).
- Total ablation calls: 15 cells × 3 runs = **45 generation calls**.

**Stability criterion (all three must hold across the 3 re-runs of a cell):**

1. **Marker-set Jaccard ≥ 0.85** between any two of the 3 runs. The marker-set is the multiset of `[MARKER]` and `[MARKER, CONF(level)]` tokens in the response, BEFORE the strip script runs. Jaccard = |A ∩ B| / |A ∪ B| over multisets (intersection and union counted with multiplicity).
2. **Marked-claim count agreement within ±1** between any two of the 3 runs. The marked-claim count = number of substantive claims that carry at least one marker tag (assessed mechanically: a sentence-level count of sentences containing `[…]`).
3. **No new substantive claims under v0.1.2 D1–D8 axis assignment** introduced in any run that are absent from another. Marginal calls go to RedTeam adjudication at AOV-180 closeout review, not silent generator-side rejection.

### §4.3 — Treatment of unstable cells

If a cell fails the stability criterion at first ablation (3 runs):
- Re-ablate that cell (3 additional runs, 6 total for that cell).
- If still unstable across the 6 runs aggregated under the same criterion: **the cell goes to a published exclusion list** in `tests/v0.2/cells/_exclusion_list.md`. The cell is NOT silently re-generated. Selection-bias-on-cells-that-passed is the failure mode RedTeam will not accept as cover for sampling-noise.

### §4.4 — Closeout-level gate

If aggregate stability rate falls below **80 % (12 / 15 cells stable on first ablation OR 12 / 15 stable on first-or-second ablation combined)**: RedTeam re-blocks at AOV-180 closeout. The 60-cell corpus is not adopted into v0.2; the protocol's measured effect is sampling-config-bound beyond the budgeted noise floor.

If aggregate stability ≥ 80 %: ablation passes, exclusion list (if non-empty) is published, surviving 60-cell corpus moves to Phase 5 (rater scoring).

---

## §5 — v0.3 forward-carry (informational, non-gating for v0.2)

If board interaction `af857c7e` resolves with option A (provision `ANTHROPIC_API_KEY`) or option B (authorize OAuth-token `~/.claude/.credentials.json`), a **v0.3 retake of the v0.2 generation** under strict call-site config (temp 0 + empty API-boundary system role) is filed as an audit upgrade path, comparable to the AOV-77 R1 retake / AOV-130 v0.1.4 retake pattern. The retake characterizes how much of the v0.2 measurement was sampling-config-bound and locks down the §3.3 closure on Surface 2 in a way the current cycle cannot.

This is non-gating for v0.2 closeout per `f63cffa2` "Forward-carry to v0.3" section.

---

## §6 — Closeout artefact directory layout

```
tests/v0.2/cells/
  cell_<qid>_A.txt                — Test A response, raw (60 - n_excluded files)
  cell_<qid>_B.txt                — Test B response, raw (post-strip script will be filed at Phase 4 closeout)
  _byte_fidelity_check.md         — Item 2 verification table (30 rows)
  _transport.md                   — Item 4 transport invocation + CLI version + host
  _claudemd_snapshot.md           — Item 5 CLAUDE.md presence + verbatim
  _hooks_snapshot.md              — Item 6 settings.json hooks block + verbatim
  _automemory_snapshot.md         — Item 7 auto-memory presence + verbatim
  _provenance.jsonl               — Item 8 per-cell provenance, 60 lines
  _ablation/                      — Item 9 ablation runs
    cell_<qid>_B_run1.txt … cell_<qid>_B_run3.txt for each of 15 cells (45 files)
    _stability_matrix.md          — per-cell stability scoring
    _exclusion_list.md            — published exclusion list (may be empty)
  _selection.md                   — Item 10 ablation selection algorithm + verification of sha256(qid || "ablation-v1") derivation
```

---

## §7 — Sign-off chain

- **Drafted:** EpistemicLogician (`2ae117a1`), 2026-05-08, post-`f63cffa2`.
- **Audit at AOV-180 closeout:** RedTeam (`9219a386`) — re-audit rights stand under `f63cffa2`. Items 1–10 audited; ablation result audited; §2.5 contamination test adjudicated. Verdict shape per RedTeam: PASS / PASS-WITH-MOD / BLOCK.
- **Countersign:** CEO (`491a73e0`) — non-pre-emption stands. CEO ratifies the audit-trail completeness, does NOT re-litigate Surface 1 / Surface 2 separation.

---

*This document is the AOV-180 run-prep gate spec. Filing it on AOV-185 with this commit hash satisfies the routing requirement of `f63cffa2`: "Logician closes AOV-185 once the bare-header transport invocation + ablation plan + injection-snapshot procedure are filed in the AOV-180 run-prep doc; AOV-180 then unblocks."*
