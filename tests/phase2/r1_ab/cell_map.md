# R1 mini-A/B sealed cell map (AOV-72)

> **STATUS:** UNSEALED 2026-05-03 at reconciliation. Mirror of this map is folded into `tests/phase2/r1_ab/reconciliation.md` §1.
>
> **Sealed at:** 2026-05-03 12:00Z (CTO `e8587a99`, AOV-72 generation complete).
> **Unsealed at:** 2026-05-03 15:30Z (CTO `e8587a99`, both L1+L2 rater seals landed: AOV-74 Logician comment `a4c85a40`; AOV-75 IndependentRater comment `20055900` + commit `f209183` pushed to origin/main).
> **Unseal owner:** CTO (`e8587a99`).

---

## Blinding scheme

- 20 cells generated: 5 prompts (MAB-1..5) × 4 conditions (Test A, B, B', B'').
- Cell IDs `RAB-01` through `RAB-20` issued in a randomized order (Python `random.seed(0x52414231)`, `random.shuffle`).
- Raters receive only the cell content under each `RAB-XX` ID; condition + prompt identity is held in this sealed map.
- For Test B / B' / B'': raters score the **marker-stripped or normalizer-expanded** content per AOV-22 / AOV-32. The R1 normalizer (`tests/phase2/r1_normalizer.py`, 6/6 self-tests PASS) is the canonical preprocessor for L1 grader input.

---

## Cell map (SEALED — for reconciliation use only)

| Cell ID | Condition | Prompt | Path |
|---|---|---|---|
| RAB-01 | B'' | MAB-4 | `tests/phase2/r1_ab/test_b_doubleprime/mab4.md` |
| RAB-02 | B   | MAB-4 | `tests/phase2/r1_ab/test_b/mab4.md` |
| RAB-03 | A   | MAB-4 | `tests/phase2/r1_ab/test_a/mab4.md` |
| RAB-04 | B   | MAB-5 | `tests/phase2/r1_ab/test_b/mab5.md` |
| RAB-05 | B   | MAB-2 | `tests/phase2/r1_ab/test_b/mab2.md` |
| RAB-06 | A   | MAB-3 | `tests/phase2/r1_ab/test_a/mab3.md` |
| RAB-07 | A   | MAB-5 | `tests/phase2/r1_ab/test_a/mab5.md` |
| RAB-08 | B'  | MAB-3 | `tests/phase2/r1_ab/test_b_prime/mab3.md` |
| RAB-09 | B   | MAB-1 | `tests/phase2/r1_ab/test_b/mab1.md` |
| RAB-10 | B'' | MAB-3 | `tests/phase2/r1_ab/test_b_doubleprime/mab3.md` |
| RAB-11 | B'  | MAB-5 | `tests/phase2/r1_ab/test_b_prime/mab5.md` |
| RAB-12 | B'' | MAB-2 | `tests/phase2/r1_ab/test_b_doubleprime/mab2.md` |
| RAB-13 | B'  | MAB-2 | `tests/phase2/r1_ab/test_b_prime/mab2.md` |
| RAB-14 | B'' | MAB-5 | `tests/phase2/r1_ab/test_b_doubleprime/mab5.md` |
| RAB-15 | A   | MAB-2 | `tests/phase2/r1_ab/test_a/mab2.md` |
| RAB-16 | B'' | MAB-1 | `tests/phase2/r1_ab/test_b_doubleprime/mab1.md` |
| RAB-17 | B'  | MAB-4 | `tests/phase2/r1_ab/test_b_prime/mab4.md` |
| RAB-18 | B   | MAB-3 | `tests/phase2/r1_ab/test_b/mab3.md` |
| RAB-19 | A   | MAB-1 | `tests/phase2/r1_ab/test_a/mab1.md` |
| RAB-20 | B'  | MAB-1 | `tests/phase2/r1_ab/test_b_prime/mab1.md` |

---

## Author-bias declaration

CTO (`e8587a99`) authored:
- The R1 compression patterns P1, P2, P3 (proposal at `tests/phase2/r1_compression_proposal.md`).
- The mini-A/B plan and the 5 MAB prompts.
- All 20 cell responses (Test A free-form; Test B with v0.1.2 markers; Test B' and B'' mechanically derived from B via `r1_compressor.py`).

CTO does **NOT** serve as primary scorer. Logician (`2ae117a1`) is primary; IndependentRater (`00749544`) parallel non-gating; RedTeam (`9219a386`) post-hoc.

---

## Lossless-derivation note (for reconciliation)

Test B' = `compress_p1_p2(Test B)` and Test B'' = `compress_p1_p2_p3(Test B)`. Both directions verified by `tests/phase2/r1_ab/derive_b_prime_double.py`: every B' and B'' cell round-trips back to its source B cell via `r1_normalizer.normalize()` (whitespace-normalized equality).

This means D1–D6 epistemic content is **provably identical** across B / B' / B'' for each prompt — the only inter-condition variable is marker syntax density. Any D1–D6 score divergence between B / B' / B'' on a given prompt is rater noise, not content drift. (Test A has independent free-form content and may legitimately differ on D1–D6.)
