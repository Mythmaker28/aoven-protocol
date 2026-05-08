# AOV-180 Item 2 — Surface 1 byte-fidelity verification

Per run-prep §1 Item 2: every Test A user message MUST equal `<bare Q>` exactly; every Test B user message MUST equal `[Aoven v0.1.2]\n<bare Q>\nNo flattery` exactly. All 30 rows MUST pass.

prompts.md SHA-256 (gen-START): `022ce620d731a96fa8cbe4bf11ab415eca1f92d5af25c83ed103fbdd40ebe2bc`

## 30-row verification table

| qid | sha256(<bare Q>) | sha256(Test A user msg) | A pass | sha256(Test B user msg) | B pass |
|-----|------------------|--------------------------|--------|--------------------------|--------|
| V02-D-SCI-001 | `bd71242571e3d60e...` | `bd71242571e3d60e...` | ✓ | `c7cdaedf80d1ed54...` | ✓ |
| V02-D-SCI-002 | `80d82dada940f154...` | `80d82dada940f154...` | ✓ | `10b80a0bc6957771...` | ✓ |
| V02-D-SCI-003 | `67cba689308399de...` | `67cba689308399de...` | ✓ | `2969adc33ade0b0f...` | ✓ |
| V02-D-SCI-004 | `3a94e34a3c4c1139...` | `3a94e34a3c4c1139...` | ✓ | `86b92e8e10c54093...` | ✓ |
| V02-D-SCI-005 | `b9fdc0ea2f1815e3...` | `b9fdc0ea2f1815e3...` | ✓ | `5d8a083803091765...` | ✓ |
| V02-D-SCI-006 | `e61926d32edd9817...` | `e61926d32edd9817...` | ✓ | `6b9a446156607226...` | ✓ |
| V02-D-TECH-001 | `e5c47ebc714d1695...` | `e5c47ebc714d1695...` | ✓ | `4e903e2af5821fba...` | ✓ |
| V02-D-TECH-002 | `139d6904d5a3428b...` | `139d6904d5a3428b...` | ✓ | `db65f7016c801fc9...` | ✓ |
| V02-D-TECH-003 | `a2fc46d2ca3e9bef...` | `a2fc46d2ca3e9bef...` | ✓ | `e8d0f4bd7225cfe9...` | ✓ |
| V02-D-TECH-004 | `58adfe463eff8b48...` | `58adfe463eff8b48...` | ✓ | `a1a91ff012c858a3...` | ✓ |
| V02-D-TECH-005 | `bb98820801d7cdb3...` | `bb98820801d7cdb3...` | ✓ | `10d59a79a453f206...` | ✓ |
| V02-D-NORM-001 | `4cf7329286c1a359...` | `4cf7329286c1a359...` | ✓ | `608c5667bb0812eb...` | ✓ |
| V02-D-NORM-002 | `ba3a3b64b08f7369...` | `ba3a3b64b08f7369...` | ✓ | `7eac732b9cc58e7f...` | ✓ |
| V02-D-NORM-003 | `eed690393a57a99e...` | `eed690393a57a99e...` | ✓ | `f59a8879ced5458f...` | ✓ |
| V02-D-NORM-004 | `6dbf12b6a7af7ede...` | `6dbf12b6a7af7ede...` | ✓ | `5c1eed97119b2117...` | ✓ |
| V02-D-NORM-005 | `4f82251909efde74...` | `4f82251909efde74...` | ✓ | `892898ffe24c9d01...` | ✓ |
| V02-D-PRED-001 | `bfbd559334cf0af2...` | `bfbd559334cf0af2...` | ✓ | `7175522972ecbed4...` | ✓ |
| V02-D-PRED-002 | `4e35cf79ab04bdd2...` | `4e35cf79ab04bdd2...` | ✓ | `f00b198dffefaeed...` | ✓ |
| V02-D-PRED-003 | `f6e4cf12341342c2...` | `f6e4cf12341342c2...` | ✓ | `12d5cfda22d9df29...` | ✓ |
| V02-D-PRED-004 | `f01cd6cbe21a5a88...` | `f01cd6cbe21a5a88...` | ✓ | `331c9d1783061c42...` | ✓ |
| V02-D-SCI-007 | `e1da9af3a3ea054a...` | `e1da9af3a3ea054a...` | ✓ | `a73952ee6f6596cf...` | ✓ |
| V02-D-SCI-008 | `01a39a897beb388a...` | `01a39a897beb388a...` | ✓ | `b5c2cbd3144592d1...` | ✓ |
| V02-D-SCI-009 | `97b22e778829866e...` | `97b22e778829866e...` | ✓ | `52960f6d573d8d4b...` | ✓ |
| V02-D-TECH-006 | `a130b260af127ba5...` | `a130b260af127ba5...` | ✓ | `17e92d3540373bad...` | ✓ |
| V02-D-TECH-007 | `0ca99aa7d90d7bdf...` | `0ca99aa7d90d7bdf...` | ✓ | `f49dfd468148863a...` | ✓ |
| V02-D-NORM-006 | `6a3281569880d58b...` | `6a3281569880d58b...` | ✓ | `2cde3a8d27954944...` | ✓ |
| V02-D-NORM-007 | `127c36da0c866f6b...` | `127c36da0c866f6b...` | ✓ | `0a980d799d64475c...` | ✓ |
| V02-D-NORM-008 | `44c156af05183a58...` | `44c156af05183a58...` | ✓ | `e99cc15164b60908...` | ✓ |
| V02-D-PRED-005 | `7a59c3e8e84675fa...` | `7a59c3e8e84675fa...` | ✓ | `9fc58955c865144f...` | ✓ |
| V02-D-PRED-006 | `1023237db9c772d0...` | `1023237db9c772d0...` | ✓ | `e7dc1ce722084898...` | ✓ |

## Outcome

- Test A pass count: 30 / 30
- Test B pass count: 30 / 30
- Overall: **PASS**

## Verification recipe

- Test A: `sha256sum cell_<qid>_A.user.txt` == `sha256(<bare Q>)`. Bare Q is the verbatim line in `prompts.md` immediately following the `#### V02-D-...` header (italics already stripped per `prompts.md` audit cross-check note line 133).
- Test B: read `cell_<qid>_B.user.txt`, strip the leading 16 bytes (`[Aoven v0.1.2]\n`) and the trailing 12 bytes (`\nNo flattery`), then `sha256` the remainder. Must equal `sha256(<bare Q>)`.
- Templates (constant across all 30 cells):
  - Test A pre/post: empty (sha `e3b0c442...`).
  - Test B prefix `[Aoven v0.1.2]\n` (sha `2fe5b9af22d39d26...`).
  - Test B suffix `\nNo flattery` (sha `4fda0fe3951cab05...`).
  - Test B template-with-placeholder `[Aoven v0.1.2]\n<bare Q>\nNo flattery` (sha `c8b2d4f9ecd7ba1c...`).
