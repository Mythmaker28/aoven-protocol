# ROADMAP

Short-step plan for `aoven-protocol`, drafted on 2026-10-24 from the public repository only: `main` at [`0eaaba6`][c-0eaaba6] (53 commits). Line numbers refer to that commit, and every link is pinned to it.

This file is a contributor aid, not ratified spec content ([AGENTS.md:63][ag63]). It changes no spec text, data, score or verdict. Spec changes keep the circuit CTO drafts → Logician audits → CEO ratifies → Scribe folds ([AGENTS.md:64][ag64]). Claims carry markers per C-1: `[FACT]` names where to check it, `[REC]` is advisory, `[UNCERTAIN]` marks what the public repository cannot settle, and `[INTERPRET]` names its alternative reading.

## 0. Where things stand

- [FACT] v0.1.1 was ratified on 2026-04-26 ([README.md:9][rd9]; M-1, [DECISIONS.md:36][de36]).
- [FACT] v0.1.2 passed on the sealed hold-out Q11–Q16 on 2026-05-03, κ = 0.759 ([README.md:10][rd10]; M-2, [DECISIONS.md:37][de37]).
- [FACT] v0.1.3 (D10–D12) is provisional ([AOVEN_PROTOCOL_v0.1.md:3][sp3]), "pending broader v0.1.3 launch validation" ([DECISIONS.md:22-24][de22]).
- [FACT] v0.2: the pre-registration is sealed and CEO-countersigned ([tests/v0.2/prompts.md:10][pr10]). The 60-cell corpus landed in [`efae4dd`][c-efae4dd] and the Phase 5 statistics in [`28f4ae6`][c-28f4ae6]. The committed verdict reads "INCONCLUSIVE (with strict-reading FAIL noted as alternate)" and asks RedTeam and the CEO to pin the reading ([_ratification.md:27][ra27], [:31][ra31]).
- [FACT] The last commit is [`0eaaba6`][c-0eaaba6] (2026-05-22). There is no CI (no `.github/` directory), and [PR #2][pr2] (2026-04-26) is the only other open PR.
- [UNCERTAIN] Tasks are tracked in Paperclip ([AGENTS.md:63][ag63]), which is not visible from here; work done there after 2026-05-22 may already cover some steps below.

## 1. Constraints on every step

C-1 to C-7 ([AGENTS.md:53-59][ag53r]) bind every contributor, human or agent:

- **C-1** [Marker discipline][ag53] — this file applies it.
- **C-2** [Anti-aura][ag54] and **C-3** [no silent suppression][ag55] — no step touches marker semantics.
- **C-4** [Vocabulary budget, 0 / 3 used][ag56] — no step adds a term.
- **C-5** [Burned questions stay burned][ag57] — Q1–Q16 and the 8 AOV-24 contrast pairs.
- **C-6** [No invented history][ag58] — every claim below links its source.
- **C-7** [Push-deferral when in force][ag59] — publishing a local-only file (B1, B6) is a push decision.

## 2. Verified baseline

Re-run on 2026-10-24 with Python 3.11 from the repository root at `0eaaba6`. Standard library only; no network; no model calls.

| Script (run as `python3 <path>`) | Result |
|---|---|
| [`tests/phase2/r1_normalizer.py`][t-norm] | 6/6 self-tests PASS |
| [`tests/phase2/r1_compressor.py`][t-comp] | 2/2 round-trips PASS (B′→B, B″→B) |
| [`tests/v0.2/strip_test_b_markers.py`][t-strip] `--selftest` | 14/14 PASS |
| [`tests/v0.2/scoring/_unseal.py`][t-unseal] | 60 rows per rater; rewritten TSVs byte-identical |
| [`tests/phase2/r1_ab/derive_b_prime_double.py`][t-derive] | ALL PASS; outputs byte-identical |
| [`tests/v0.2/scoring/_stats.py`][st] | `_kappa.md`, `_test_b_delta.md` byte-identical; `_ratification.md` differs (B2) |

- [FACT] Afterwards `git status` shows one modified tracked file (`tests/v0.2/scoring/_ratification.md`) and one untracked directory (`tests/phase2/__pycache__/`, created by the import at [r1_compressor.py:88][cmp88]).
- [FACT] `_stats.py` reads its inputs with `git show origin/main:<path>` ([_stats.py:37-41][st37]), so it needs a clone with an `origin/main` ref; `PIN_COMMIT` ([:28][st28]) only appears in the generated text.
- [FACT] [`_run_main_cells.py:23`][rmc] and [`_run_ablation.py:21`][rab] call a local `claude.cmd` CLI, i.e. live model calls. Nine `tests/v0.2/_*.py` scripts, these two included, hard-code a Windows `WORKSPACE` path (e.g. [`_blind_cells.py:20`][bc20]).
- [REC] Keep those nine scripts out of CI and agent runs.

## 3. Steps

### Track A — Repository hygiene

No spec, data or verdict change. Any contributor may draft; the CEO owns push gates ([AGENTS.md:13][ag13]).

- **A1** [REC] Add a root `.gitignore` with `__pycache__/` (§2). Only [`tests/v0.2/cells/.gitignore`][cgi] exists today.
- **A2** [REC] Add `tests/README.md`: the §2 commands, their expected results, and the nine scripts not to run ([`_blind_cells.py:20`][bc20] and the others listed by `grep -l '^WORKSPACE' tests/v0.2/_*.py`).
- **A3** [REC] Add a GitHub Actions workflow running the three self-tests ([`r1_normalizer.py`][t-norm], [`r1_compressor.py`][t-comp], [`strip_test_b_markers.py --selftest`][t-strip]); standard library, no network, no secrets.
- **A4** [REC] Extend A3: re-run [`_unseal.py`][t-unseal], [`derive_b_prime_double.py`][t-derive] and [`_stats.py`][st], and fail on any output diff except `_ratification.md` until B2 is settled. The checkout needs an `origin/main` ref (`fetch-depth: 0`).

### Track B — Record integrity

Fixes pointers and labels; none changes a score or a verdict. The named owner decides.

- **B1 — Dead link in the spec.** [FACT] [AOVEN_PROTOCOL_v0.1.md:372][sp372] links `tests/pilots/2026-05-01-religious-vs-neutral.md`, which no public commit contains (Appendix A). It is the only dead relative link outside code blocks in the 124 `.md` files tracked at `0eaaba6`. [FACT] A committed snapshot lists the pilot docs as "local-canonical only" per push-deferral ([_automemory_snapshot.md:387][am387]). [REC] Publish the file, or replace the link with a note that it is not public. Owner: spec circuit ([AGENTS.md:64][ag64]).
- **B2 — Verdict label vs script output.** [FACT] The committed [_ratification.md:27][ra27] reads INCONCLUSIVE. Re-running [`_stats.py`][st] at the same commit writes "§3.1 + §3.2 verdict (F2-scoped): FAIL", with the same κ = 0.3729, CI [0.1132, 0.6177] and the same §3.2 table; the two versions differ only at [lines 10–13][ra10] and [27–33][ra27r]. Script and file came in the single commit [`28f4ae6`][c-28f4ae6]. [INTERPRET] The two-readings text was added by hand after the script ran; alternative: an uncommitted script version produced it. [REC] Once the CEO pins the reading ([:31][ra31]), encode the rule in `_stats.py` or mark the hand-written sections as such. [REC] Make `git_show` read `PIN_COMMIT` rather than `origin/main` ([_stats.py:28][st28], [:37-41][st37]); today both give the same bytes, since only [`0d67287`][c-0d67287] touched the input TSVs. Owner: CEO for the pin; script changes need owner review (scoring code).
- **B3 — Spec placeholder.** [FACT] "Test results" ([AOVEN_PROTOCOL_v0.1.md:376-400][sp376]) still says "awaiting Red Team / Experimentation (AOV-6)" and "(pending AOV-6)", while Phase 2 scores and reconciliations are committed under [`tests/phase2/`][d-phase2] since [`67fad66`][c-67fad66] (pointers at [README.md:18-20][rd18]; result M-2, [DECISIONS.md:37][de37]). [REC] Replace the placeholder with pointers. Owner: spec circuit.
- **B4 — Lagging status lines.** [FACT] [README.md:12][rd12] still describes v0.2 as a pre-registered scaffold, and [DECISIONS.md:51][de51] keeps D-V0.2-PREREG at "[open] — scaffold under AOV-90", while the pre-registration is sealed and countersigned ([prompts.md:10][pr10]) and Phase 5 statistics exist ([`28f4ae6`][c-28f4ae6]). [FACT] The [cheatsheet revision draft, line 4][cs4] still says "ready for canonical-doc push"; that push is [`ab79153`][c-ab79153]. [REC] Update these after B2, recording only. Owner: Canonical Scribe ([AGENTS.md:47-49][ag47]).
- **B5 — Pre-registration header.** [FACT] The [pre-registration, line 10][pg10] still says "DRAFT v1 — awaiting IR seal". The seal is recorded as `c2bde85…`, "canonical at `origin/main:3643264`" ([probe_key.md:6][pk6]). [FACT] `c2bde85` is not in public history; the file's blob `94ab599…` is identical at [`3643264`][c-3643264] and at `0eaaba6` (Appendix A). [REC] Do not edit the file: line 10 locks it "at this commit hash". Record the `c2bde85` → `3643264` mapping in DECISIONS.md instead. Owner: Scribe, after CEO agreement.
- **B6 — Cited but absent files.** [FACT] 13 paths cited in committed docs exist on no public ref (Appendix B). [REC] For push-deferred or local-only paths, the owner decides: publish (C-7), or add a note at the citing line. Private-by-design paths need no action. Owner: CEO ([AGENTS.md:13][ag13]).
- **B7 — Stale PR.** [FACT] [PR #2][pr2] (2026-04-26, "Clean repository docs and fix exploratory archive (v0.1.2)") is still open and conflicts with `main` on all 5 files it touches (Appendix A). [FACT] Later commits changed all 5 files, among them [`fb71920`][c-fb71920] (the spec) and [`0eaaba6`][c-0eaaba6] (the other four). [INTERPRET] They appear to supersede it; alternative: it holds wording that never reached `main`. [REC] The owner closes it or asks for a refresh. Owner: CEO.

### Track C — Protocol programme

The owner or the board decides; agents only prepare drafts.

- **C1 — v0.1.3 launch validation.** [FACT] D10–D12 are "pending broader v0.1.3 launch validation" ([DECISIONS.md:22-24][de22]). [UNCERTAIN] No public file defines what that validation requires. [REC] Write the criterion down before running it. Owner: CEO + Logician.
- **C2 — UR-8 collision.** [FACT] AOV-54 Patch 1 (stack-depth cap), drafted as UR-8, awaits disposition: renumber to UR-9, defer to v0.1.4, or re-scope ([AOVEN_PROTOCOL_v0.1.md:13][sp13], [:323][sp323]; [DECISIONS.md:30][de30]). AOV-54 Patches 1, 2 and 5 are not in the v0.1.3 fold ([:13][sp13]). Owner: CEO/CTO, then the spec circuit.
- **C3 — D2/D3 promotion.** [FACT] D2 and D3 are "[provisional] — gated on first A/B test" ([AOVEN_PROTOCOL_v0.1.md:225][sp225], [:234][sp234]). The spec ties them to the marker-accuracy signal ([:392][sp392]), scored in Phase 2 as Layer 2 L2-C1 ([scores_logician_layer2.md:12][l2c1]); M-2 records the confirmatory PASS ([DECISIONS.md:37][de37]); DECISIONS.md still lists both as provisional ([:14-15][de14]). [UNCERTAIN] Whether this meets the trigger: no public decision says so. Owner: CEO, then the spec circuit.
- **C4 — Next versions.** [FACT] Forward-carried to v0.3: rubric calibration and the marker-emergence retake ([_ratification.md:35-38][ra35]). Carried to v0.1.4: the D10–D12 out-of-scope items ([AOVEN_PROTOCOL_v0.1.md:303][sp303], [:314][sp314], [:325][sp325]) and the "retake-spec absorption track" ([AGENTS.md:18][ag18]). Owner: CTO drafts; spec circuit.
- **C5 — Human studies.** [FACT] The Phase 3.5 pilot is "PROVISIONAL — pre-audit", with the recruitment gate closed ([pilot scope, line 7][ps7]); v0.2 human raters are paid $40/session ([recruitment pack, line 211][hp211]). [REC] Never automate: this involves spending and recruitment. Owner: board + CEO.
- **C6 — Dissemination.** [FACT] The v0.1.2 arXiv draft awaits a Logician NOSRC audit and CEO sign-off ([preprint, line 4][pp4]). Paper drafting is deferred ([DECISIONS.md:44][de44], [:53][de53]), and announcements need CEO sign-off ([AGENTS.md:13][ag13]). Owner: Scribe drafts, CEO signs ([AGENTS.md:47-49][ag47]).

## 4. Out of scope for agents

[REC] An agent session never: runs the live-model scripts (§2); spends money or contacts participants (C5); ratifies, adjudicates or relabels a verdict (B2, C1–C3); edits a hash-locked file (B5); edits the spec outside the circuit ([AGENTS.md:64][ag64]); publishes or announces (C6); reuses burned questions (C-5).

## Appendix A — Checks behind B1, B5 and B7

```sh
git log --all --oneline -- tests/pilots                        # empty
git rev-parse 3643264:docs/v0.2_expansion_preregistration.md   # 94ab5993e70fb1215d239af2e9b775a8e704eac4
git rev-parse 0eaaba6:docs/v0.2_expansion_preregistration.md   # same blob
git cat-file -t c2bde85                                        # fails: not in public history
git merge-tree --write-tree origin/main 32bdd70                # exit 1, 5 conflicts (PR #2 head)
```

## Appendix B — Paths cited but absent from every public ref

Each path has 0 commits on every public ref (`git log --all -- <path>`). Scope: paths written with their directory in the 124 tracked `.md` files, plus the root file `AOV_TEST_RESULTS_v0.1.md`. Left out: range patterns such as `tests/phase2/test_a/q11..16.md` (the files exist), spec version names such as `AOVEN_PROTOCOL_v0.1.2.md`, and bare file names without a directory (agent-memory files, older names).

| Path | Cited at | Context at the citing line |
|---|---|---|
| `tests/pilots/2026-05-01-religious-vs-neutral.md` | [AOVEN_PROTOCOL_v0.1.md:372][sp372] | local-canonical per push-deferral ([_automemory_snapshot.md:387][am387]) |
| `tests/redteam/` | [scores_logician_layer1.md:9][x-ll9], [scores_logician_holdout_layer1.md:8][x-lh8], [scores_independentrater_layer1.md:7][x-il7] | listed among inputs the rater did not read |
| `tests/redteam/holdout_probes_q11_q16.md` | [AOV_TEST_PLAN_v0.1.md:199][x-tp199] and 5 other lines | "contamination-gated per AOV-49" ([scores_logician_holdout_layer1.md:10][x-lh10]) |
| `tests/phase2/scores_logician_r1ab_layer1.md` | [r1_ab/reconciliation.md:11][x-rc11] | Logician local commit `d3c36d2`, push-deferred |
| `tests/phase2/scores_logician_r1ab_layer2.md` | [r1_ab/reconciliation.md:12][x-rc12] | Logician local commit `f6a6540`, push-deferred |
| `tests/phase2/scores_independentrater_aov130.md` | [aov130/redteam_posthoc.md:6][x-rp6] | "(IR workspace)" |
| `tests/phase2/scores_cto.md` | [reconciliation_logician_independentrater.md:225][x-rli225] and 2 other lines | the citing line says it "does not exist" |
| `AOV_TEST_RESULTS_v0.1.md` | [scores_independentrater_layer1.md:7][x-il7] | named as the scoring input; no reason given |
| `docs/v0_1_3/aov110_analogy_pairing_rule.md` | [v0_1_3_cheatsheet_revision_draft.md:94][x-cs94], [:140][x-cs140], [:215][x-cs215] | line 140: "once it lands in this workspace" |
| `tests/v0.2/cells/_exclusion_list.md` | [run_prep_aov180.md:169][x-rp169] | [INTERPRET] path slip: the layout at [line 202][x-rp202] and [cells/README.md:63][x-cr63] put it under `_ablation/`, where it exists; alternative: a separate main-cell list |
| `docs/usability_phase3_5_results.md` | [usability_phase3_5_real_human_pilot_scope.md:179][x-ps179] | future deliverable |
| `tests/usability/phase3_5/recruitment_log.csv` | [phase35_recruitment_log_schema.md:22][x-rl22] | private by design |
| `tests/usability/phase3_5/transcripts/` | [usability_phase3_5_real_human_pilot_scope.md:35][x-ps35] | private by design |

<!-- Reference links: every target is pinned to commit 0eaaba60c7fc63657db89b8db1e97742b274f11b. -->

[c-0eaaba6]: https://github.com/Mythmaker28/aoven-protocol/commit/0eaaba60c7fc63657db89b8db1e97742b274f11b
[c-28f4ae6]: https://github.com/Mythmaker28/aoven-protocol/commit/28f4ae68a73ab38a6989b14db9854be8ce8312b0
[c-0d67287]: https://github.com/Mythmaker28/aoven-protocol/commit/0d6728722cb7499b30946fa20afc3ad66ab73b15
[c-3643264]: https://github.com/Mythmaker28/aoven-protocol/commit/36432640f0aed6f9ed4102043f07333692ee5c87
[c-efae4dd]: https://github.com/Mythmaker28/aoven-protocol/commit/efae4dd95e3b6c580e805a6a77a9dde4d053382b
[c-67fad66]: https://github.com/Mythmaker28/aoven-protocol/commit/67fad66894a9f6a6348f9b620920785393fc9cc4
[c-fb71920]: https://github.com/Mythmaker28/aoven-protocol/commit/fb71920fa1e26a0560de2402bfecb82c36afb6cd
[c-ab79153]: https://github.com/Mythmaker28/aoven-protocol/commit/ab7915358b7df1766df77862f8698bcdd2be5e7b
[pr2]: https://github.com/Mythmaker28/aoven-protocol/pull/2

[ag13]: https://github.com/Mythmaker28/aoven-protocol/blob/0eaaba60c7fc63657db89b8db1e97742b274f11b/AGENTS.md?plain=1#L13
[ag18]: https://github.com/Mythmaker28/aoven-protocol/blob/0eaaba60c7fc63657db89b8db1e97742b274f11b/AGENTS.md?plain=1#L18
[ag47]: https://github.com/Mythmaker28/aoven-protocol/blob/0eaaba60c7fc63657db89b8db1e97742b274f11b/AGENTS.md?plain=1#L47-L49
[ag53r]: https://github.com/Mythmaker28/aoven-protocol/blob/0eaaba60c7fc63657db89b8db1e97742b274f11b/AGENTS.md?plain=1#L53-L59
[ag53]: https://github.com/Mythmaker28/aoven-protocol/blob/0eaaba60c7fc63657db89b8db1e97742b274f11b/AGENTS.md?plain=1#L53
[ag54]: https://github.com/Mythmaker28/aoven-protocol/blob/0eaaba60c7fc63657db89b8db1e97742b274f11b/AGENTS.md?plain=1#L54
[ag55]: https://github.com/Mythmaker28/aoven-protocol/blob/0eaaba60c7fc63657db89b8db1e97742b274f11b/AGENTS.md?plain=1#L55
[ag56]: https://github.com/Mythmaker28/aoven-protocol/blob/0eaaba60c7fc63657db89b8db1e97742b274f11b/AGENTS.md?plain=1#L56
[ag57]: https://github.com/Mythmaker28/aoven-protocol/blob/0eaaba60c7fc63657db89b8db1e97742b274f11b/AGENTS.md?plain=1#L57
[ag58]: https://github.com/Mythmaker28/aoven-protocol/blob/0eaaba60c7fc63657db89b8db1e97742b274f11b/AGENTS.md?plain=1#L58
[ag59]: https://github.com/Mythmaker28/aoven-protocol/blob/0eaaba60c7fc63657db89b8db1e97742b274f11b/AGENTS.md?plain=1#L59
[ag63]: https://github.com/Mythmaker28/aoven-protocol/blob/0eaaba60c7fc63657db89b8db1e97742b274f11b/AGENTS.md?plain=1#L63
[ag64]: https://github.com/Mythmaker28/aoven-protocol/blob/0eaaba60c7fc63657db89b8db1e97742b274f11b/AGENTS.md?plain=1#L64

[rd9]: https://github.com/Mythmaker28/aoven-protocol/blob/0eaaba60c7fc63657db89b8db1e97742b274f11b/README.md?plain=1#L9
[rd10]: https://github.com/Mythmaker28/aoven-protocol/blob/0eaaba60c7fc63657db89b8db1e97742b274f11b/README.md?plain=1#L10
[rd12]: https://github.com/Mythmaker28/aoven-protocol/blob/0eaaba60c7fc63657db89b8db1e97742b274f11b/README.md?plain=1#L12
[rd18]: https://github.com/Mythmaker28/aoven-protocol/blob/0eaaba60c7fc63657db89b8db1e97742b274f11b/README.md?plain=1#L18-L20

[de14]: https://github.com/Mythmaker28/aoven-protocol/blob/0eaaba60c7fc63657db89b8db1e97742b274f11b/DECISIONS.md?plain=1#L14-L15
[de22]: https://github.com/Mythmaker28/aoven-protocol/blob/0eaaba60c7fc63657db89b8db1e97742b274f11b/DECISIONS.md?plain=1#L22-L24
[de30]: https://github.com/Mythmaker28/aoven-protocol/blob/0eaaba60c7fc63657db89b8db1e97742b274f11b/DECISIONS.md?plain=1#L30
[de36]: https://github.com/Mythmaker28/aoven-protocol/blob/0eaaba60c7fc63657db89b8db1e97742b274f11b/DECISIONS.md?plain=1#L36
[de37]: https://github.com/Mythmaker28/aoven-protocol/blob/0eaaba60c7fc63657db89b8db1e97742b274f11b/DECISIONS.md?plain=1#L37
[de44]: https://github.com/Mythmaker28/aoven-protocol/blob/0eaaba60c7fc63657db89b8db1e97742b274f11b/DECISIONS.md?plain=1#L44
[de51]: https://github.com/Mythmaker28/aoven-protocol/blob/0eaaba60c7fc63657db89b8db1e97742b274f11b/DECISIONS.md?plain=1#L51
[de53]: https://github.com/Mythmaker28/aoven-protocol/blob/0eaaba60c7fc63657db89b8db1e97742b274f11b/DECISIONS.md?plain=1#L53

[sp3]: https://github.com/Mythmaker28/aoven-protocol/blob/0eaaba60c7fc63657db89b8db1e97742b274f11b/AOVEN_PROTOCOL_v0.1.md?plain=1#L3
[sp13]: https://github.com/Mythmaker28/aoven-protocol/blob/0eaaba60c7fc63657db89b8db1e97742b274f11b/AOVEN_PROTOCOL_v0.1.md?plain=1#L13
[sp225]: https://github.com/Mythmaker28/aoven-protocol/blob/0eaaba60c7fc63657db89b8db1e97742b274f11b/AOVEN_PROTOCOL_v0.1.md?plain=1#L225
[sp234]: https://github.com/Mythmaker28/aoven-protocol/blob/0eaaba60c7fc63657db89b8db1e97742b274f11b/AOVEN_PROTOCOL_v0.1.md?plain=1#L234
[sp303]: https://github.com/Mythmaker28/aoven-protocol/blob/0eaaba60c7fc63657db89b8db1e97742b274f11b/AOVEN_PROTOCOL_v0.1.md?plain=1#L303
[sp314]: https://github.com/Mythmaker28/aoven-protocol/blob/0eaaba60c7fc63657db89b8db1e97742b274f11b/AOVEN_PROTOCOL_v0.1.md?plain=1#L314
[sp323]: https://github.com/Mythmaker28/aoven-protocol/blob/0eaaba60c7fc63657db89b8db1e97742b274f11b/AOVEN_PROTOCOL_v0.1.md?plain=1#L323
[sp325]: https://github.com/Mythmaker28/aoven-protocol/blob/0eaaba60c7fc63657db89b8db1e97742b274f11b/AOVEN_PROTOCOL_v0.1.md?plain=1#L325
[sp372]: https://github.com/Mythmaker28/aoven-protocol/blob/0eaaba60c7fc63657db89b8db1e97742b274f11b/AOVEN_PROTOCOL_v0.1.md?plain=1#L372
[sp376]: https://github.com/Mythmaker28/aoven-protocol/blob/0eaaba60c7fc63657db89b8db1e97742b274f11b/AOVEN_PROTOCOL_v0.1.md?plain=1#L376-L400
[sp392]: https://github.com/Mythmaker28/aoven-protocol/blob/0eaaba60c7fc63657db89b8db1e97742b274f11b/AOVEN_PROTOCOL_v0.1.md?plain=1#L392

[ra10]: https://github.com/Mythmaker28/aoven-protocol/blob/0eaaba60c7fc63657db89b8db1e97742b274f11b/tests/v0.2/scoring/_ratification.md?plain=1#L10-L13
[ra27]: https://github.com/Mythmaker28/aoven-protocol/blob/0eaaba60c7fc63657db89b8db1e97742b274f11b/tests/v0.2/scoring/_ratification.md?plain=1#L27
[ra27r]: https://github.com/Mythmaker28/aoven-protocol/blob/0eaaba60c7fc63657db89b8db1e97742b274f11b/tests/v0.2/scoring/_ratification.md?plain=1#L27-L33
[ra31]: https://github.com/Mythmaker28/aoven-protocol/blob/0eaaba60c7fc63657db89b8db1e97742b274f11b/tests/v0.2/scoring/_ratification.md?plain=1#L31
[ra35]: https://github.com/Mythmaker28/aoven-protocol/blob/0eaaba60c7fc63657db89b8db1e97742b274f11b/tests/v0.2/scoring/_ratification.md?plain=1#L35-L38
[st]: https://github.com/Mythmaker28/aoven-protocol/blob/0eaaba60c7fc63657db89b8db1e97742b274f11b/tests/v0.2/scoring/_stats.py
[st28]: https://github.com/Mythmaker28/aoven-protocol/blob/0eaaba60c7fc63657db89b8db1e97742b274f11b/tests/v0.2/scoring/_stats.py#L28
[st37]: https://github.com/Mythmaker28/aoven-protocol/blob/0eaaba60c7fc63657db89b8db1e97742b274f11b/tests/v0.2/scoring/_stats.py#L37-L41
[t-unseal]: https://github.com/Mythmaker28/aoven-protocol/blob/0eaaba60c7fc63657db89b8db1e97742b274f11b/tests/v0.2/scoring/_unseal.py
[t-strip]: https://github.com/Mythmaker28/aoven-protocol/blob/0eaaba60c7fc63657db89b8db1e97742b274f11b/tests/v0.2/strip_test_b_markers.py
[pr10]: https://github.com/Mythmaker28/aoven-protocol/blob/0eaaba60c7fc63657db89b8db1e97742b274f11b/tests/v0.2/prompts.md?plain=1#L10
[pk6]: https://github.com/Mythmaker28/aoven-protocol/blob/0eaaba60c7fc63657db89b8db1e97742b274f11b/tests/v0.2/probe_key.md?plain=1#L6
[am387]: https://github.com/Mythmaker28/aoven-protocol/blob/0eaaba60c7fc63657db89b8db1e97742b274f11b/tests/v0.2/cells/_automemory_snapshot.md?plain=1#L387
[cgi]: https://github.com/Mythmaker28/aoven-protocol/blob/0eaaba60c7fc63657db89b8db1e97742b274f11b/tests/v0.2/cells/.gitignore
[rmc]: https://github.com/Mythmaker28/aoven-protocol/blob/0eaaba60c7fc63657db89b8db1e97742b274f11b/tests/v0.2/_run_main_cells.py#L23
[rab]: https://github.com/Mythmaker28/aoven-protocol/blob/0eaaba60c7fc63657db89b8db1e97742b274f11b/tests/v0.2/_run_ablation.py#L21
[bc20]: https://github.com/Mythmaker28/aoven-protocol/blob/0eaaba60c7fc63657db89b8db1e97742b274f11b/tests/v0.2/_blind_cells.py#L20

[d-phase2]: https://github.com/Mythmaker28/aoven-protocol/tree/0eaaba60c7fc63657db89b8db1e97742b274f11b/tests/phase2
[t-norm]: https://github.com/Mythmaker28/aoven-protocol/blob/0eaaba60c7fc63657db89b8db1e97742b274f11b/tests/phase2/r1_normalizer.py
[t-comp]: https://github.com/Mythmaker28/aoven-protocol/blob/0eaaba60c7fc63657db89b8db1e97742b274f11b/tests/phase2/r1_compressor.py
[t-derive]: https://github.com/Mythmaker28/aoven-protocol/blob/0eaaba60c7fc63657db89b8db1e97742b274f11b/tests/phase2/r1_ab/derive_b_prime_double.py
[cmp88]: https://github.com/Mythmaker28/aoven-protocol/blob/0eaaba60c7fc63657db89b8db1e97742b274f11b/tests/phase2/r1_compressor.py#L88
[l2c1]: https://github.com/Mythmaker28/aoven-protocol/blob/0eaaba60c7fc63657db89b8db1e97742b274f11b/tests/phase2/scores_logician_layer2.md?plain=1#L12

[pg10]: https://github.com/Mythmaker28/aoven-protocol/blob/0eaaba60c7fc63657db89b8db1e97742b274f11b/docs/v0.2_expansion_preregistration.md?plain=1#L10
[cs4]: https://github.com/Mythmaker28/aoven-protocol/blob/0eaaba60c7fc63657db89b8db1e97742b274f11b/docs/v0_1_3_cheatsheet_revision_draft.md?plain=1#L4
[ps7]: https://github.com/Mythmaker28/aoven-protocol/blob/0eaaba60c7fc63657db89b8db1e97742b274f11b/docs/usability_phase3_5_real_human_pilot_scope.md?plain=1#L7
[hp211]: https://github.com/Mythmaker28/aoven-protocol/blob/0eaaba60c7fc63657db89b8db1e97742b274f11b/docs/v0_2_h2_recruitment_pack.md?plain=1#L211
[pp4]: https://github.com/Mythmaker28/aoven-protocol/blob/0eaaba60c7fc63657db89b8db1e97742b274f11b/docs/dissemination/v0.1.2/preprint_arxiv_cs_cl.md?plain=1#L4

[x-ll9]: https://github.com/Mythmaker28/aoven-protocol/blob/0eaaba60c7fc63657db89b8db1e97742b274f11b/tests/phase2/scores_logician_layer1.md?plain=1#L9
[x-lh8]: https://github.com/Mythmaker28/aoven-protocol/blob/0eaaba60c7fc63657db89b8db1e97742b274f11b/tests/phase2/scores_logician_holdout_layer1.md?plain=1#L8
[x-lh10]: https://github.com/Mythmaker28/aoven-protocol/blob/0eaaba60c7fc63657db89b8db1e97742b274f11b/tests/phase2/scores_logician_holdout_layer1.md?plain=1#L10
[x-il7]: https://github.com/Mythmaker28/aoven-protocol/blob/0eaaba60c7fc63657db89b8db1e97742b274f11b/tests/phase2/scores_independentrater_layer1.md?plain=1#L7
[x-tp199]: https://github.com/Mythmaker28/aoven-protocol/blob/0eaaba60c7fc63657db89b8db1e97742b274f11b/AOV_TEST_PLAN_v0.1.md?plain=1#L199
[x-rc11]: https://github.com/Mythmaker28/aoven-protocol/blob/0eaaba60c7fc63657db89b8db1e97742b274f11b/tests/phase2/r1_ab/reconciliation.md?plain=1#L11
[x-rc12]: https://github.com/Mythmaker28/aoven-protocol/blob/0eaaba60c7fc63657db89b8db1e97742b274f11b/tests/phase2/r1_ab/reconciliation.md?plain=1#L12
[x-rp6]: https://github.com/Mythmaker28/aoven-protocol/blob/0eaaba60c7fc63657db89b8db1e97742b274f11b/tests/phase2/aov130/redteam_posthoc.md?plain=1#L6
[x-rli225]: https://github.com/Mythmaker28/aoven-protocol/blob/0eaaba60c7fc63657db89b8db1e97742b274f11b/tests/phase2/reconciliation_logician_independentrater.md?plain=1#L225
[x-cs94]: https://github.com/Mythmaker28/aoven-protocol/blob/0eaaba60c7fc63657db89b8db1e97742b274f11b/docs/v0_1_3_cheatsheet_revision_draft.md?plain=1#L94
[x-cs140]: https://github.com/Mythmaker28/aoven-protocol/blob/0eaaba60c7fc63657db89b8db1e97742b274f11b/docs/v0_1_3_cheatsheet_revision_draft.md?plain=1#L140
[x-cs215]: https://github.com/Mythmaker28/aoven-protocol/blob/0eaaba60c7fc63657db89b8db1e97742b274f11b/docs/v0_1_3_cheatsheet_revision_draft.md?plain=1#L215
[x-rp169]: https://github.com/Mythmaker28/aoven-protocol/blob/0eaaba60c7fc63657db89b8db1e97742b274f11b/tests/v0.2/run_prep_aov180.md?plain=1#L169
[x-rp202]: https://github.com/Mythmaker28/aoven-protocol/blob/0eaaba60c7fc63657db89b8db1e97742b274f11b/tests/v0.2/run_prep_aov180.md?plain=1#L202
[x-cr63]: https://github.com/Mythmaker28/aoven-protocol/blob/0eaaba60c7fc63657db89b8db1e97742b274f11b/tests/v0.2/cells/README.md?plain=1#L63
[x-ps179]: https://github.com/Mythmaker28/aoven-protocol/blob/0eaaba60c7fc63657db89b8db1e97742b274f11b/docs/usability_phase3_5_real_human_pilot_scope.md?plain=1#L179
[x-rl22]: https://github.com/Mythmaker28/aoven-protocol/blob/0eaaba60c7fc63657db89b8db1e97742b274f11b/docs/phase35_recruitment_log_schema.md?plain=1#L22
[x-ps35]: https://github.com/Mythmaker28/aoven-protocol/blob/0eaaba60c7fc63657db89b8db1e97742b274f11b/docs/usability_phase3_5_real_human_pilot_scope.md?plain=1#L35
