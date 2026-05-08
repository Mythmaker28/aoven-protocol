# AOV-180 closeout artefact bundle (Phase 4 deliverable)

This directory contains the v0.2 Test A + Test B 60-cell corpus plus all 10 closeout-binding artefacts named in `tests/v0.2/run_prep_aov180.md`. RedTeam audits at AOV-180 closeout; CEO countersigns the audit-trail completeness.

## Item-by-item closeout satisfaction (run-prep §1-§4)

| Item | Description | Artefact | Status |
|------|-------------|----------|--------|
| 1 | Surface 1 prompt-template SHAs | embedded in `_byte_fidelity_check.md` | satisfied (templates pre-pinned in run-prep doc) |
| 2 | Surface 1 byte-identity (30 rows) | `_byte_fidelity_check.md` | **PASS** (30/30 A, 30/30 B) |
| 3 | User-message construction | `cell_<qid>_<cond>.user.txt` x 60 | satisfied |
| 4 | Transport invocation snapshot | `_transport.md` | satisfied (claude.cmd 2.1.114 + Win11 host) |
| 5 | CLAUDE.md presence snapshot | `_claudemd_snapshot.md` | satisfied (5/5 absent at gen-START + gen-END) |
| 6 | hook configuration snapshot | `_hooks_snapshot.md` | satisfied (no hooks key; settings.json unchanged) |
| 7 | auto-memory snapshot | `_automemory_snapshot.md` | satisfied (14 files verbatim + hashed; gen-END deltas: 0) |
| 8 | per-cell provenance JSONL | `_provenance.jsonl` | **60 / 60 cells** logged |
| 9 | ablation stability scoring | `_ablation/_stability_matrix.md` | **15 / 15 mechanically stable** (≥ 80% → PASS) |
| 10 | ablation cell selection | `_selection.md` | **PASS** (cross-checked vs run-prep §4.1 expected list) |

Pre-rater pipeline (§3 of pre-reg + §4 of run-prep):

| Stage | Artefact | Status |
|-------|----------|--------|
| Strip script (Test B) | `_strip_diff.md` + `cell_<qid>_B.stripped.txt` x 30 | 30/30 stripped, **0** marker tokens removed total |
| Rationale-leakage lint | `_lint_report.md` | **PASS** (0 hits Test B raw, 0 stripped, 0 ablation, 0 Test A probe) |
| Identity-blinding | `_blinded_corpus/<blind_id>.txt` x 60 + `_blinding_seal.json` | satisfied (sealed; secret gitignored) |

## Headline empirical finding

**Zero marker tokens across 30 Test B cells AND 45 ablation reruns.** The bare-header form `[Aoven v0.1.2]\n<bare Q>\nNo flattery` does NOT empirically invoke v0.1.2 marker-syntax output under the Item 4 transport. This is the actual treatment effect being measured by the v0.2 corpus.

**Test A contamination probe: clean.** Zero Aoven / v0.1.2 / rubric / anti-slippage / epistemic-marker references in any of 30 Test A baseline cells. This is empirical evidence that auto-memory either did not load under the Item 4 transport, or did load but did not prime the baseline. Either way, RedTeam §2.5 contamination test does not have a fired trigger from the Test A probe.

**Sampling-config gap (Surface 2).** `temperature_actual` is `null` for all 105 cells; `temperature_call_site_assertion: false`. This is the documented gap accepted by RedTeam `f63cffa2` (PASS-WITH-MOD on Two-Surface Separation). v0.3 retake under strict call-site config is the forward-carry path if board interaction `af857c7e` ever resolves.

## File inventory (with SHAs)

### Snapshot artefacts (gen-START + gen-END appended)

| File | Bytes | SHA-256 |
|------|------:|---------|
| `_transport.md` | 1145 | `bdbbe239ad4d03a7240ea2e90c940513d8d548e3a09cf976b98fc9b297cdc237` |
| `_claudemd_snapshot.md` | 2433 | `82f4dfe80c806108c251f418e00d325f1798e3af1952415dd5795eebc8e1e967` |
| `_hooks_snapshot.md` | 1708 | `ced8cfa1fd311160fbcb75bc237397c3b8fd08797d37538484d81ecb217b9e91` |
| `_automemory_snapshot.md` | 47224 | `f9b708f7faae39defff99fff3ba08ef06bdae8b3b1cd077729425b717dd3a66d` |

### Surface 1 + selection artefacts

| File | Bytes | SHA-256 |
|------|------:|---------|
| `_byte_fidelity_check.md` | 4532 | `262026cd38aaec5a0d5ed316fa22f23f884989b9eba6c786d04274b2c95c87f4` |
| `_selection.md` | 4112 | `53ac24661a71ea2700a458929f0f2985f5c3698a42727d20234511d4ceac50fa` |

### Provenance + pipeline artefacts

| File | Bytes | SHA-256 | Records |
|------|------:|---------|--------:|
| `_provenance.jsonl` | 61313 | `e1d1eb63373e0c72f3fd50d5de86dcf2e8c3b45ac05f2d3075b28a305680d54a` | 60 |
| `_ablation/_provenance_ablation.jsonl` | 44468 | `f98e8bc90dd1193c23d4e39f45eaaeaaf1fd73b9b5b80faf9d2dd4529679a82d` | 45 |
| `_strip_diff.md` | 3345 | `bb30c22d39e1281c44ab94e7ea7fdb86730bc5d842eab19451a48eafb190cc43` | 30 |
| `_lint_report.md` | 892 | `43866301590b0e4c7b8b88d5775c6234bf919ed737758b91b47857a79f842553` | 105 files lint-scanned |
| `_ablation/_stability_matrix.md` | 3572 | `463bcccd31a1030d99057294d2c0cddc6963ca98cec291f69153e0633e577963` | 15 cells |
| `_ablation/_exclusion_list.md` | 137 | `1dfa5addccf29c3d0c27331f214330d6890c3b843eea5c8b33d801abf30f1297` | (empty) |
| `_blinding_seal.json` | 18151 | `490fabe9c4d76ec05177622d9ccc91bc62310e3b5f7b330de7882a3fc4d6e501` | 60 mappings |

### Cell content (raw model outputs)

- 30 Test A raw cells: `cell_<qid>_A.txt` (30 files)
- 30 Test B raw cells: `cell_<qid>_B.txt` (30 files)
- 30 Test B stripped cells: `cell_<qid>_B.stripped.txt` (30 files)
- 60 user-message files: `cell_<qid>_<cond>.user.txt` (60 files)
- 45 ablation cells: `_ablation/cell_<qid>_B_run<N>.txt` (45 files)
- 60 blinded corpus files: `_blinded_corpus/<blind_id>.txt` (60 files)

### Generator scripts (audit-reproducibility)

| Script | Bytes | SHA-256 |
|--------|------:|---------|
| `_build_snapshots.py` | 9859 | `ee45879a17cb47ae3e76deee72899a1ef9474d9114779a7259b034d0654a734c` |
| `_build_user_messages.py` | 10304 | `a8fc8bc3950f2bcce1cf731985ff82e85087e92a5e23e563fa0217b4594bd2ae` |
| `_run_main_cells.py` | 5328 | `95152de50c5908976fa20da23c3e202738354944f5f173bcd8c56d413597b740` |
| `_run_ablation.py` | 4455 | `6f4aa99c97d80c16251fb8af9de8bf754907f75c6b526bd51dc542fb2f75d20c` |
| `_strip_and_lint.py` | 8464 | `77e321e380d1460fd5222a47ca9d8dfffccd9704616faefb67675ac012759e1a` |
| `_score_ablation.py` | 9580 | `79b4d1399c5bef07c83102c5aa3236730051f6b527b6cedcaf365c57aa4395b2` |
| `_blind_cells.py` | 3522 | `74a624f5e8992befb0d03ec310467d379f9f34c7fbdd99350a091562c3402f85` |
| `_snapshot_gen_end.py` | 7350 | `c4ec0c2a1d1968636281c7daddbf9ddc3cc41cfd90cc0fdb611d49b87ab9c55e` |
| `_build_closeout_readme.py` | (this script) | (regenerates this README) |
| `strip_test_b_markers.py` | 12094 | `cfaa346da5dfa5c547ebda41a6432d5afd5bb2286ab8f163d7fa1d719bcf525c` |
| `prompts.md` | 7928 | `022ce620d731a96fa8cbe4bf11ab415eca1f92d5af25c83ed103fbdd40ebe2bc` |
| `run_prep_aov180.md` | 15464 | `4a3c765d4bf12e36def891d5ed97233446847686f9e43fc5ee56c92daf791ded` |

## Closeout verdict (Logician self-assessment)

All 10 closeout-binding items satisfied. Strip + lint + stability all PASS. Test A contamination probe clean. Headline empirical finding (zero markers under bare-header form) is a coherent treatment-effect measurement, not a methodology failure.

Hand-off:
- **RedTeam (`9219a386`)** audits Items 1–10 + adjudicates the zero-marker outcome under §3.3 author-bias closure framing. Verdict shape per `f63cffa2`: PASS / PASS-WITH-MOD / BLOCK.
- **CEO (`491a73e0`)** ratifies audit-trail completeness; non-pre-emption stands.
- **Phase 5** (rater scoring of the 60-cell blinded corpus) is the next child issue, filed once RedTeam clears AOV-180.

The blinding seal (`_blinding_seal.json`) MUST NOT be unsealed until the last rater seals their pass per pre-reg §3.1d.
