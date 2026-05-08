# AOV-180 Test B strip-script results (pre-rater-sealing token-level diff)

Strip script: `tests/v0.2/strip_test_b_markers.py`
Strip script SHA-256: `cfaa346da5dfa5c547ebda41a6432d5afd5bb2286ab8f163d7fa1d719bcf525c`

## 30-row strip table

| qid | raw sha | raw bytes | stripped sha | stripped bytes | tokens stripped |
|-----|---------|-----------|--------------|----------------|----------------:|
| V02-D-SCI-001 | `9c846f24e7e6e25d...` | 2724 | `9c846f24e7e6e25d...` | 2724 | 0 |
| V02-D-SCI-002 | `fa9c7656338a6eb5...` | 2036 | `fa9c7656338a6eb5...` | 2036 | 0 |
| V02-D-SCI-003 | `dab1903baf6fc27b...` | 70 | `dab1903baf6fc27b...` | 70 | 0 |
| V02-D-SCI-004 | `a7feaa5c31d6f578...` | 4791 | `a7feaa5c31d6f578...` | 4791 | 0 |
| V02-D-SCI-005 | `273fb7c1ffde16f6...` | 3373 | `de2b430a17a7ebd4...` | 3369 | 0 |
| V02-D-SCI-006 | `6f07b191c49dff88...` | 831 | `6f07b191c49dff88...` | 831 | 0 |
| V02-D-TECH-001 | `176ef18a26afa416...` | 2476 | `176ef18a26afa416...` | 2476 | 0 |
| V02-D-TECH-002 | `a98c1eedc067c21d...` | 2897 | `a98c1eedc067c21d...` | 2897 | 0 |
| V02-D-TECH-003 | `5f68dbcfe341e181...` | 2567 | `5f68dbcfe341e181...` | 2567 | 0 |
| V02-D-TECH-004 | `3247b6b4fa682258...` | 2374 | `3247b6b4fa682258...` | 2374 | 0 |
| V02-D-TECH-005 | `79ca575dd4e4b181...` | 3206 | `79ca575dd4e4b181...` | 3206 | 0 |
| V02-D-NORM-001 | `fa6281bd83eb2cd0...` | 1772 | `fa6281bd83eb2cd0...` | 1772 | 0 |
| V02-D-NORM-002 | `1c0b2892ee2cb266...` | 2624 | `1c0b2892ee2cb266...` | 2624 | 0 |
| V02-D-NORM-003 | `d3b12c6b8f9105c7...` | 1918 | `d3b12c6b8f9105c7...` | 1918 | 0 |
| V02-D-NORM-004 | `74851351c510e4c5...` | 2226 | `74851351c510e4c5...` | 2226 | 0 |
| V02-D-NORM-005 | `4d5577aba0b75044...` | 2280 | `4d5577aba0b75044...` | 2280 | 0 |
| V02-D-PRED-001 | `cc16f6f621b180fa...` | 1837 | `cc16f6f621b180fa...` | 1837 | 0 |
| V02-D-PRED-002 | `ede7c9b97af44aec...` | 1828 | `ede7c9b97af44aec...` | 1828 | 0 |
| V02-D-PRED-003 | `8a07cd63d821ed3f...` | 1804 | `8a07cd63d821ed3f...` | 1804 | 0 |
| V02-D-PRED-004 | `e1590461d0b6ff17...` | 2784 | `e1590461d0b6ff17...` | 2784 | 0 |
| V02-D-SCI-007 | `02786c13f14c53d0...` | 2738 | `02786c13f14c53d0...` | 2738 | 0 |
| V02-D-SCI-008 | `60d86eb2c4c1f5a0...` | 2058 | `60d86eb2c4c1f5a0...` | 2058 | 0 |
| V02-D-SCI-009 | `c0e1112660f53991...` | 2845 | `c0e1112660f53991...` | 2845 | 0 |
| V02-D-TECH-006 | `63cb60769453b9e7...` | 4175 | `63cb60769453b9e7...` | 4175 | 0 |
| V02-D-TECH-007 | `9f08b2e650e06701...` | 3016 | `9f08b2e650e06701...` | 3016 | 0 |
| V02-D-NORM-006 | `208612791f527e37...` | 1932 | `208612791f527e37...` | 1932 | 0 |
| V02-D-NORM-007 | `b1b042d0040e1631...` | 1667 | `b1b042d0040e1631...` | 1667 | 0 |
| V02-D-NORM-008 | `eee8ba07854494e0...` | 2887 | `eee8ba07854494e0...` | 2887 | 0 |
| V02-D-PRED-005 | `d5f1b95eae7ae9b0...` | 3262 | `d5f1b95eae7ae9b0...` | 3262 | 0 |
| V02-D-PRED-006 | `ca814d2a98124ed0...` | 1860 | `ca814d2a98124ed0...` | 1860 | 0 |

**Total marker tokens stripped across 30 Test B cells: 0**

Note: zero marker tokens across 30 cells indicates the bare-header form `[Aoven v0.1.2]\n<Q>\nNo flattery` does NOT empirically invoke v0.1.2 marker-syntax output. This is itself a measurement of the Test B treatment effect under the Two-Surface Separation regime. Raters score the unstripped output (which equals the stripped output in this case).
