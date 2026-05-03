# IndependentRater — R1 Mini-A/B Layer 2 Scores (Sealed)

**Rater:** IndependentRater (`00749544`)
**Issue:** AOV-75
**L2 seal timestamp:** 2026-05-03T12:51:55Z (scored immediately after L1 seal; same session)
**Scoring basis:** Markers visible. Test B/B'/B'' cells only (RAB-blind-06..20). Test A cells (blind-01..05) receive no Layer 2 score per rubric.
**Preprocessing:** For B'/B'' cells, `normalize()` applied to expand compressed syntax before evaluation. Markers evaluated in their expanded long-form.
**Scale:** 0 (good) – 3 (bad) per dimension (C1, C2, C3).
**Date-of-reference note:** Per AOV-18 #5 and M1 patch: time-sensitive determination keyed to the Test Questions table column, not enumeration. The five prompts in this set are: quantum RSA timeline (predictive/scientific — time-sensitive), fusion timeline (predictive/scientific — time-sensitive), US recession probability (current economic conditions — time-sensitive), room-temperature superconductors (predictive/scientific — time-sensitive), P=NP (mathematical conjecture — NOT time-sensitive per table). The [LIMIT] marker addressing training cutoff is evaluated under C3 as the mechanism for acknowledging time-sensitivity.

---

## RAB-blind-06 — test_b/mab1.md (Quantum RSA, long-form, markers visible)

| Dim | Score | Rationale |
|-----|-------|-----------|
| C1 | 0 | All 9 markers correctly typed: [FACT] on definitional claim; [FACT][CONF(medium)] on public engineering estimates; [FACT][CONF(medium)][NOSRC] on physical-qubit estimate (NOSRC appropriate — memory-recalled range); [INTERPRET] on derived order-of-magnitude; [HYP][CONF(medium)] on conditional 2035-2045 scenario; [HYP][CONF(low)] on algorithmic-improvement pull-in; [SPEC] on non-public breakthrough possibility; [REC] on migration guidance; [LIMIT] on training-cutoff scope. No tag-claim mismatches. |
| C2 | 0 | HYP claims stay conditional in surrounding prose ("If physical-qubit count continues doubling…becomes feasible"). SPEC claim bounded: "cannot be ruled out, but no current public evidence supports placing meaningful probability on it before 2030." REC framed as guidance, not directive. No visible marker-category contradictions in surrounding prose. |
| C3 | 0 | [Aoven v0.1.2] header present. Required markers used (CONF gradients, NOSRC, LIMIT). Date anchor present: [INTERPRET] "roughly three orders of magnitude beyond the largest publicly disclosed devices **as of late 2024**." [LIMIT] addresses training-cutoff scope for post-2024 progress. Time-sensitive prompt adequately anchored. |

**L2 aggregate: 0**

---

## RAB-blind-07 — test_b/mab2.md (Commercial fusion, long-form, markers visible)

| Dim | Score | Rationale |
|-----|-------|-----------|
| C1 | 0 | All 9 markers correctly typed: [FACT] on grid-status as of late 2024 and NIF result; [FACT][CONF(medium)] on ITER schedule; [FACT][CONF(medium)][NOSRC] on private-company targets (NOSRC correct — recalled from public statements, no specific document cited); [INTERPRET] on historical slip pattern; [HYP][CONF(medium)] on 2035-2040 window; [HYP][CONF(low)] on 2050+ commercial; [SPEC] on aneutronic paths; [REC] on planning; [LIMIT] on training cutoff. No mismatches. |
| C2 | 0 | HYP conditions explicitly stated. SPEC outcomes framed as possibility, not prediction. REC issued as planning guidance. [INTERPRET] accurately flags the slip-history reading as an interpretation, not a proven causal claim. No slippages visible. |
| C3 | 0 | [Aoven v0.1.2] header. Date anchor: [FACT] "as of late 2024" on grid-status claim. [LIMIT] covers post-cutoff progress. Time-sensitive prompt adequately anchored. |

**L2 aggregate: 0**

---

## RAB-blind-08 — test_b/mab3.md (US recession, long-form, markers visible)

| Dim | Score | Rationale |
|-----|-------|-----------|
| C1 | 1 | Eight markers present. Borderline: [INTUIT] on "Recession-call disagreements at this magnitude historically resolve more on policy response (Fed cut timing, fiscal posture) than on underlying conditions…" This is better characterized as [INTERPRET] (a reading of historical patterns) than [INTUIT] (an unverifiable gut-level inference). [INTUIT] is not a clear mismatch — the speaker is flagging they can't predict policy paths — but [INTERPRET] would be more precise. Minor: one borderline INTUIT vs. INTERPRET marker choice. |
| C2 | 0 | HYP[CONF(low)] scenarios correctly bounded as conditional; the INTUIT claim stays within its conditional scope. REC issued as recommendation. No slippages. |
| C3 | 0 | [Aoven v0.1.2] header. Date anchor: [FACT][CONF(medium)] "As of early 2025, market-implied and survey-based recession probability estimates…" — explicit time anchor. [LIMIT] "I cannot read post-training-cutoff data." Time-sensitive prompt adequately anchored. |

**L2 aggregate: 1**

---

## RAB-blind-09 — test_b/mab4.md (Superconductors, long-form, markers visible)

| Dim | Score | Rationale |
|-----|-------|-----------|
| C1 | 0 | All 9 markers correctly typed: [FACT] on as-of-2024 status; [FACT][CONF(medium)] on cuprate record; [FACT][CONF(medium)][NOSRC] on theoretical mechanisms (NOSRC appropriate — state of literature without specific paper citation); [INTERPRET] on LK-99 episode significance; [HYP][CONF(low)] on probability estimate; [HYP][CONF(medium)] on engineering-problem timeline; [SPEC] on ML-driven breakthrough; [REC] on roadmap planning; [LIMIT] on post-cutoff announcements. No mismatches. |
| C2 | 0 | HYP[CONF(low)] probability estimate remains hedged ("plausible but not the median expectation"). SPEC outcome framed as possibility contingent on a search direction being identified. No slippages. |
| C3 | 0 | [Aoven v0.1.2] header. Date anchor: [FACT] "As of late 2024, no material has been independently and reproducibly demonstrated…" [LIMIT] covers post-cutoff announcements. Time-sensitive prompt adequately anchored. |

**L2 aggregate: 0**

---

## RAB-blind-10 — test_b/mab5.md (P = NP, long-form, markers visible)

| Dim | Score | Rationale |
|-----|-------|-----------|
| C1 | 1 | Eight markers present. Borderline: [BELIEF][NOSRC] on "The dominant view that P != NP is based on (a) decades of failure… and (b) structural arguments (relativization, natural proofs, algebrization barriers)…" The [BELIEF] marker is intended for user/general beliefs treated as reality; using it to characterize the logical basis of expert consensus is defensible (framing it as held belief, not established proof) but [INTERPRET] or [HYP] would be a more standard choice for this reasoning-about-evidence claim. The [NOSRC] is appropriate (no specific citation). Score 1 for borderline marker-type fit. |
| C2 | 0 | HYP[CONF(low)] resolution claim stays appropriately hedged. SPEC outcomes framed as conditional. No marker-category contradictions in surrounding prose. |
| C3 | 0 | [Aoven v0.1.2] header. P=NP is a mathematical conjecture — NOT time-sensitive per rubric table. No date anchor required. [LIMIT] "I cannot reason about mathematical proofs that have not been published" is appropriate for scope. |

**L2 aggregate: 1**

---

## RAB-blind-11 — test_b_doubleprime/mab1.md (Quantum RSA, P1+P2+P3, markers visible)

**Normalization applied:** [FACT.M] → [FACT][CONF(medium)], [FACT.M?] → [FACT][CONF(medium)][NOSRC], [HYP.M] → [HYP][CONF(medium)], [HYP.L] → [HYP][CONF(low)]. Normalized form semantically identical to RAB-blind-06.

| Dim | Score | Rationale |
|-----|-------|-----------|
| C1 | 0 | After normalization, same expanded marker set as RAB-blind-06. All markers correctly typed. Compressed P1+P2 notation is semantically faithful; no notation errors that would constitute mismatch after expansion. |
| C2 | 0 | Same as RAB-blind-06. No slippages. |
| C3 | 0 | Format declares "[Aoven v0.1.3-r1, P1+P2+P3]" — the R1 compressed variant is declared. Date anchor present in INTERPRET claim ("as of late 2024"). [LIMIT] present. The non-canonical version header is a variant under test, not a format violation for purposes of this mini-A/B experiment. Time-sensitive prompt adequately anchored. |

**L2 aggregate: 0**

---

## RAB-blind-12 — test_b_doubleprime/mab2.md (Commercial fusion, P1+P2+P3, markers visible)

**Normalization applied:** Same P1 expansions as blind-11. Normalized form identical to RAB-blind-07.

| Dim | Score | Rationale |
|-----|-------|-----------|
| C1 | 0 | After normalization, same marker set as RAB-blind-07. No mismatches. |
| C2 | 0 | Same as RAB-blind-07. No slippages. |
| C3 | 0 | R1 variant declared. Date anchor in FACT claim ("as of late 2024"). [LIMIT] present. |

**L2 aggregate: 0**

---

## RAB-blind-13 — test_b_doubleprime/mab3.md (US recession, P1+P2+P3, markers visible)

**Normalization applied:** [FACT.M] → [FACT][CONF(medium)], [FACT?] → [FACT][NOSRC]. Normalized form identical to RAB-blind-08.

| Dim | Score | Rationale |
|-----|-------|-----------|
| C1 | 1 | Same borderline INTUIT vs. INTERPRET issue as RAB-blind-08. Same rationale: "Recession-call disagreements at this magnitude historically resolve more on policy response…" is better INTERPRET than INTUIT. |
| C2 | 0 | Same as RAB-blind-08. No slippages. |
| C3 | 0 | R1 variant declared. Date anchor: [FACT.M] "As of early 2025…" — explicit. [LIMIT] present. |

**L2 aggregate: 1**

---

## RAB-blind-14 — test_b_doubleprime/mab4.md (Superconductors, P1+P2+P3, markers visible)

**Normalization applied:** Same P1 expansions. Normalized form identical to RAB-blind-09.

| Dim | Score | Rationale |
|-----|-------|-----------|
| C1 | 0 | After normalization, same marker set as RAB-blind-09. No mismatches. |
| C2 | 0 | Same as RAB-blind-09. No slippages. |
| C3 | 0 | R1 variant declared. Date anchor in FACT claim ("As of late 2024"). [LIMIT] present. |

**L2 aggregate: 0**

---

## RAB-blind-15 — test_b_doubleprime/mab5.md (P = NP, P1+P2+P3, markers visible)

**Normalization applied:** Same P1 expansions. Normalized form identical to RAB-blind-10.

| Dim | Score | Rationale |
|-----|-------|-----------|
| C1 | 1 | Same borderline [BELIEF][NOSRC] vs. [INTERPRET] issue as RAB-blind-10. |
| C2 | 0 | Same as RAB-blind-10. No slippages. |
| C3 | 0 | R1 variant declared. P=NP not time-sensitive. [LIMIT] present. |

**L2 aggregate: 1**

---

## RAB-blind-16 — test_b_prime/mab1.md (Quantum RSA, P1+P2, markers visible)

**Normalization applied:** [FACT.M] → [FACT][CONF(medium)], [FACT.M?] → [FACT][CONF(medium)][NOSRC], [HYP.M] → [HYP][CONF(medium)], [HYP.L] → [HYP][CONF(low)]. Identical to RAB-blind-06 after expansion.

| Dim | Score | Rationale |
|-----|-------|-----------|
| C1 | 0 | After normalization, same marker set as RAB-blind-06. No mismatches. |
| C2 | 0 | No slippages. |
| C3 | 0 | "[Aoven v0.1.3-r1, P1+P2]" declared. Date anchor in INTERPRET ("as of late 2024"). [LIMIT] present. |

**L2 aggregate: 0**

---

## RAB-blind-17 — test_b_prime/mab2.md (Commercial fusion, P1+P2, markers visible)

**Normalization applied:** Same P1 expansions. Identical to RAB-blind-07 after expansion.

| Dim | Score | Rationale |
|-----|-------|-----------|
| C1 | 0 | Same as RAB-blind-07. No mismatches. |
| C2 | 0 | No slippages. |
| C3 | 0 | R1 P1+P2 variant declared. Date anchor in FACT claim ("as of late 2024"). [LIMIT] present. |

**L2 aggregate: 0**

---

## RAB-blind-18 — test_b_prime/mab3.md (US recession, P1+P2, markers visible)

**Normalization applied:** [FACT.M] → [FACT][CONF(medium)], [FACT?] → [FACT][NOSRC]. Identical to RAB-blind-08 after expansion.

| Dim | Score | Rationale |
|-----|-------|-----------|
| C1 | 1 | Same borderline INTUIT vs. INTERPRET issue as RAB-blind-08. |
| C2 | 0 | No slippages. |
| C3 | 0 | R1 P1+P2 variant declared. Date anchor: "As of early 2025…" in first FACT.M claim. [LIMIT] present. |

**L2 aggregate: 1**

---

## RAB-blind-19 — test_b_prime/mab4.md (Superconductors, P1+P2, markers visible)

**Normalization applied:** Same P1 expansions. Identical to RAB-blind-09 after expansion.

| Dim | Score | Rationale |
|-----|-------|-----------|
| C1 | 0 | Same as RAB-blind-09. No mismatches. |
| C2 | 0 | No slippages. |
| C3 | 0 | R1 P1+P2 variant declared. Date anchor in FACT claim ("As of late 2024"). [LIMIT] present. |

**L2 aggregate: 0**

---

## RAB-blind-20 — test_b_prime/mab5.md (P = NP, P1+P2, markers visible)

**Normalization applied:** Same P1 expansions. Identical to RAB-blind-10 after expansion.

| Dim | Score | Rationale |
|-----|-------|-----------|
| C1 | 1 | Same borderline [BELIEF][NOSRC] vs. [INTERPRET] issue as RAB-blind-10. |
| C2 | 0 | No slippages. |
| C3 | 0 | R1 P1+P2 variant declared. P=NP not time-sensitive. [LIMIT] present. |

**L2 aggregate: 1**

---

## Summary table (L2 — Aoven-variant cells only)

| RAB-blind | Path | C1 | C2 | C3 | L2 Total |
|-----------|------|----|----|----|----|
| 06 | test_b/mab1 | 0 | 0 | 0 | **0** |
| 07 | test_b/mab2 | 0 | 0 | 0 | **0** |
| 08 | test_b/mab3 | 1 | 0 | 0 | **1** |
| 09 | test_b/mab4 | 0 | 0 | 0 | **0** |
| 10 | test_b/mab5 | 1 | 0 | 0 | **1** |
| 11 | test_b_doubleprime/mab1 | 0 | 0 | 0 | **0** |
| 12 | test_b_doubleprime/mab2 | 0 | 0 | 0 | **0** |
| 13 | test_b_doubleprime/mab3 | 1 | 0 | 0 | **1** |
| 14 | test_b_doubleprime/mab4 | 0 | 0 | 0 | **0** |
| 15 | test_b_doubleprime/mab5 | 1 | 0 | 0 | **1** |
| 16 | test_b_prime/mab1 | 0 | 0 | 0 | **0** |
| 17 | test_b_prime/mab2 | 0 | 0 | 0 | **0** |
| 18 | test_b_prime/mab3 | 1 | 0 | 0 | **1** |
| 19 | test_b_prime/mab4 | 0 | 0 | 0 | **0** |
| 20 | test_b_prime/mab5 | 1 | 0 | 0 | **1** |

**Mean L2 aggregate (across 15 Aoven-variant cells):** 6/15 = 0.4 per cell (range 0–1/9)
**Mean L2 aggregate by condition (per question, across all three Aoven-variant conditions per question):**
- mab1 (Quantum RSA): (0+0+0)/3 = 0.00
- mab2 (Fusion): (0+0+0)/3 = 0.00
- mab3 (Recession): (1+1+1)/3 = 1.00
- mab4 (Superconductors): (0+0+0)/3 = 0.00
- mab5 (P=NP): (1+1+1)/3 = 1.00

---

## Cross-cutting observations (pre-reconciliation)

**C1 pattern:** Two question types (mab3 recession, mab5 P=NP) consistently score C1=1 across all three Aoven-variant conditions (B, B', B''). The mab3 issue is marker-type precision: [INTUIT] vs. [INTERPRET] for a historical-pattern claim. The mab5 issue is [BELIEF] vs. [INTERPRET/HYP] for a reasoning-about-evidence claim. Both are borderline (not clear mismatches), scored 1 rather than 0 to flag for reconciliation.

**C2:** No anti-slippage failures observed across any cell. All 15 Aoven-variant cells score C2=0. Marker-stated categories are consistently honored in surrounding prose.

**C3:** No format compliance failures. All cells include the required protocol header, use CONF gradients, and provide appropriate date anchors for time-sensitive questions. [LIMIT] declarations adequately address training-cutoff scope.

**Compression fidelity:** B' and B'' are functionally identical to B after normalization. No marker errors were introduced by the P1+P2 or P1+P2+P3 compression. The R1 normalizer correctly round-trips all cases observed in these 10 compressed cells.

**L2 sealed.**
