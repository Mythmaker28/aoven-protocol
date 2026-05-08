# AOV-180 Item 10 — ablation cell selection (deterministic)

Per run-prep §4.1: selection rule is `sha256(qid || "ablation-v1")` truncated, sorted ascending within each domain stratum, take first N per RedTeam allocation (4 D-SCI / 4 D-TECH / 4 D-NORM / 3 D-PRED = 15).

## Per-Q derivation (all 30, with selection-key)

| qid | sha256(qid || "ablation-v1") | domain | selected? |
|-----|------------------------------|--------|-----------|
| V02-D-NORM-001 | `c74f756c40545bb8b83cc67285478e2c...` | D-NORM |  |
| V02-D-NORM-002 | `e380997fc8b21dda5a4abc49dda028b0...` | D-NORM |  |
| V02-D-NORM-003 | `7bac6d7540b6ebd9e04532d292bdf13d...` | D-NORM | ✓ |
| V02-D-NORM-004 | `cf5e2eb6b7068476320b2caa300d9721...` | D-NORM |  |
| V02-D-NORM-005 | `0325418da46e4873eece9ea8af1b19e9...` | D-NORM | ✓ |
| V02-D-NORM-006 | `d27a77ed5ec2c883505b77460a59e1e4...` | D-NORM |  |
| V02-D-NORM-007 | `91c87fc5886c3a443772f555c41771e0...` | D-NORM | ✓ |
| V02-D-NORM-008 | `02f61c07aa437e1b188d326f2914c503...` | D-NORM | ✓ |
| V02-D-PRED-001 | `343c8362a3f49b324d7005851b7370f3...` | D-PRED | ✓ |
| V02-D-PRED-002 | `86af2eff8048a9bcf31314a785d2ee56...` | D-PRED |  |
| V02-D-PRED-003 | `e6a3eb8d7b37af70cabe464716c8fca5...` | D-PRED |  |
| V02-D-PRED-004 | `75404021bd118e2d9ae9dfdbb8705d59...` | D-PRED |  |
| V02-D-PRED-005 | `1a473c5257d4f2f3f1d5919adaf81b2e...` | D-PRED | ✓ |
| V02-D-PRED-006 | `73626bd50808cbce157a3d37b39c4f64...` | D-PRED | ✓ |
| V02-D-SCI-001 | `b577915f86849bd32ed5644510dec15b...` | D-SCI |  |
| V02-D-SCI-002 | `24e0824b9fd23003cde100213955245d...` | D-SCI | ✓ |
| V02-D-SCI-003 | `7a14987cb8cfe0cfbebd7ce1cb507c82...` | D-SCI | ✓ |
| V02-D-SCI-004 | `55dc651856606eee7ad8c89ed1c0c047...` | D-SCI | ✓ |
| V02-D-SCI-005 | `2d7f4eb4b7a172fee85aeb049559bbe1...` | D-SCI | ✓ |
| V02-D-SCI-006 | `c9064615bcd9e7105c33c103df8d066a...` | D-SCI |  |
| V02-D-SCI-007 | `cbdf55c5e77fee5cd22dc75dfc4de5a5...` | D-SCI |  |
| V02-D-SCI-008 | `fe1a44b25de65ff408e3ddd25c167c5c...` | D-SCI |  |
| V02-D-SCI-009 | `99dc754a2a51b8c72cc95be9ded7db5a...` | D-SCI |  |
| V02-D-TECH-001 | `f8b71414c24ba52fcb1af2e7a6c95d83...` | D-TECH |  |
| V02-D-TECH-002 | `a5576d45c1d9172551c82836fe4f9918...` | D-TECH | ✓ |
| V02-D-TECH-003 | `cea3ee9ccd8577473dea75b34d9380e8...` | D-TECH |  |
| V02-D-TECH-004 | `dca980a54c2ff2faa7fdcf35012e36c2...` | D-TECH |  |
| V02-D-TECH-005 | `a1f7e2745a3d98a944205eb5d9799f94...` | D-TECH | ✓ |
| V02-D-TECH-006 | `76535035306327f8e6b65ebb89054833...` | D-TECH | ✓ |
| V02-D-TECH-007 | `4cd31adbfd2e574e2e01c70cdb8a241d...` | D-TECH | ✓ |

## Selected cells (in selection order, per domain)

| Domain | Allocation | Selected qids (selection-key ascending) |
|--------|-----------:|----------------------------------------|
| D-SCI | 4 of 9 | V02-D-SCI-002, V02-D-SCI-005, V02-D-SCI-004, V02-D-SCI-003 |
| D-TECH | 4 of 7 | V02-D-TECH-007, V02-D-TECH-006, V02-D-TECH-005, V02-D-TECH-002 |
| D-NORM | 4 of 8 | V02-D-NORM-008, V02-D-NORM-005, V02-D-NORM-003, V02-D-NORM-007 |
| D-PRED | 3 of 6 | V02-D-PRED-005, V02-D-PRED-001, V02-D-PRED-006 |

Total: **15** ablation cells.

## Run-prep §4.1 expected vs. computed cross-check

- D-SCI: expected=['V02-D-SCI-002', 'V02-D-SCI-005', 'V02-D-SCI-004', 'V02-D-SCI-003'], computed=['V02-D-SCI-002', 'V02-D-SCI-005', 'V02-D-SCI-004', 'V02-D-SCI-003'], match (set-equal): **✓**
- D-TECH: expected=['V02-D-TECH-007', 'V02-D-TECH-006', 'V02-D-TECH-005', 'V02-D-TECH-002'], computed=['V02-D-TECH-007', 'V02-D-TECH-006', 'V02-D-TECH-005', 'V02-D-TECH-002'], match (set-equal): **✓**
- D-NORM: expected=['V02-D-NORM-008', 'V02-D-NORM-005', 'V02-D-NORM-003', 'V02-D-NORM-007'], computed=['V02-D-NORM-008', 'V02-D-NORM-005', 'V02-D-NORM-003', 'V02-D-NORM-007'], match (set-equal): **✓**
- D-PRED: expected=['V02-D-PRED-005', 'V02-D-PRED-001', 'V02-D-PRED-006'], computed=['V02-D-PRED-005', 'V02-D-PRED-001', 'V02-D-PRED-006'], match (set-equal): **✓**

Order note: run-prep §4.1 lists qids in selection order (selection-key ascending). Computed list above matches that order.

**Cross-check verdict: PASS**
