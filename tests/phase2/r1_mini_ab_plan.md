# R1 mini-A/B plan (post-AOV-68 mod version)

**Owner:** CTO (`e8587a99`).
**Audit-cleared:** Logician AOV-68 PASS-WITH-MOD on P1, P2, P3 (verdict `cb33d2b8`). Mods folded into proposal §5 and normalizer.
**Run owner:** AOV-72.
**Push-deferral:** local-canonical until v0.1.3 launch authorized.

---

## §1 — Cell matrix

| Condition | Description | What the LLM sees in the prompt |
|---|---|---|
| **Test A** | Baseline. No Aoven. | Plain question only. |
| **Test B** | Aoven v0.1.2 long-form. | `[Aoven v0.1.2]` header + question. |
| **Test B'** | Aoven v0.1.2 + R1 P1+P2 (compressed). | `[Aoven v0.1.3-r1, P1+P2]` header + question. |
| **Test B''** | Aoven v0.1.2 + R1 P1+P2+P3 (compressed including blocks). | `[Aoven v0.1.3-r1, P1+P2+P3]` header + question. |

**Cell layout:** 5 prompts × 4 conditions = 20 cells. Files at `tests/phase2/r1_ab/test_{a,b,b_prime,b_doubleprime}/mab{1..5}.md`.

---

## §2 — Prompts (MAB-1..5, fresh draws, orthogonal to Q1–Q16)

| ID | Prompt (English) | Domain | Q2-style? |
|---|---|---|---|
| **MAB-1** | "What's a realistic timeline for a quantum computer to break RSA-2048 encryption?" | Crypto / quantum | Yes — speculative + factual mix. |
| **MAB-2** | "When will commercial fusion power plants start delivering grid electricity?" | Energy / engineering | Yes. |
| **MAB-3** | "What is the probability of a US recession in the next 12 months?" | Macroeconomics | Yes. |
| **MAB-4** | "Will room-temperature ambient-pressure superconductors be discovered in the next decade?" | Materials physics | Yes. |
| **MAB-5** | "Is P = NP? Will it be resolved this century?" | Theoretical CS | Yes — speculative + foundational. |

**Discipline:** Hold-out Q11–Q16 sealed. CTO has not read them. MAB-1..5 are domain-orthogonal to Q1–Q10 (which were political-economic/scientific/health domains; MAB shifts toward computing-physics-econ).

---

## §3 — Generation procedure

1. CTO generates each cell as a single LLM response.
2. Test A: free response, no Aoven discipline.
3. Test B: full v0.1.2 long-form markers per AOVEN_PROTOCOL_v0.1.md §Markers and §Formats.
4. Test B': use R1 P1 (`[X.<lvl>]`) and R1 P2 (`[FACT?]`) compressed forms wherever they apply per the proposal triggers; no P3 blocks.
5. Test B'': as B', plus R1 P3 block form on any 3+ same-marker run with `[/MARKER]` close-tag REQUIRED per UR-9.
6. Each cell saved as a single `.md` file with the question echoed at top and the response below.
7. Author bias is declared (CTO authored R1 patterns AND prompts); CTO does NOT serve as primary scorer.

---

## §4 — Blinding

1. **Cell-map sealed.** A `cell_map.md` records the (condition, prompt) → blinded-cell-ID mapping. The map is sealed in the local file (committed but flagged "SEALED — do not read until reconciliation") until L1+L2 scoring lands.
2. **Cell IDs.** 20 cells use blinded IDs `RAB-01` through `RAB-20` in the order the rater receives them (randomized seed locally).
3. **Marker-strip on Test B variants.** Raters score response content, not marker compliance (per AOV-22 / AOV-32). The R1 normalizer is the canonical preprocessor for L1 grader input on Test B/B'/B''.
4. **Two-layer seal (CEO `7df27ddb`).** L1 (epistemic D1–D6) sealed before L2 (D7/D8 prose-cost) on every cell.

---

## §5 — Acceptance criteria

1. **D1–D6 unchanged:** mean(B') and mean(B'') deltas vs B (uncompressed) within ±0.5 pts on each dimension.
2. **D7/D8 mean delta improves:** mean(B' D7+D8) and mean(B'' D7+D8) each lower than mean(B D7+D8).
3. **D1–D6 vs Test A meet v0.1.2 three-part pass criterion:** zero D1–D6 regression vs A; D7/D8 ≤ +0.5 vs A under conditional rubric (per AOV-66 lean).

---

## §6 — Decision rule (AOV-72 deliverable 4)

- **Both B' and B'' pass** → recommend **P1+P2+P3** as v0.1.3 patch.
- **Only B' passes** → recommend **P1+P2** (defer P3 to v0.1.4).
- **Neither passes** → recommend **deferring R1 to v0.1.4** with diagnostic notes.
- **RedTeam-flagged new hallucination/sycophancy surface** overrides upward (downgrade or defer).

---

## §7 — Discipline binding

- Hold-out Q11–Q16 stays sealed. CTO has not read them.
- Push-deferred (local-canonical only) until v0.1.3 launch authorized.
- Two-layer scoring: L1 sealed before L2 on every cell.
- Marker-strip on Test B variants.
- Author-bias declared: CTO authored R1 patterns AND mini-A/B prompts. Logician primary; CTO does NOT serve as primary scorer.
- Post-mod normalizer (`r1_normalizer.py`) is the canonical preprocessor for L1 grader input; mechanical 6/6 round-trip PASS.

---

## §8 — Cell-map structure

The sealed cell map at `tests/phase2/r1_ab/cell_map.md` records:

```
SEAL ON: <ISO timestamp>
SEAL OFF: <unsealed at reconciliation; record timestamp>

| Cell ID | Condition | Prompt | Path |
|---------|-----------|--------|------|
| RAB-01  | ...       | MAB-?  | tests/phase2/r1_ab/test_?/mab?.md |
| ...     | ...       | ...    | ... |
```

The blinded order is generated locally with a fixed seed for reproducibility; the seed is NOT shared with the rater.
