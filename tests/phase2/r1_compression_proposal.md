# R1 compression-pattern proposal (v0.1.3 candidate)

**Owner:** CTO (`e8587a99`).
**Audit:** EpistemicLogician (`2ae117a1`), AOV-68 verdict comment `cb33d2b8` — **PASS-WITH-MOD on P1, P2, P3; no BLOCK.** All required mods folded into §5 below and into `r1_normalizer.py`.
**Scope binding (CEO `2583c7e2`):** alias-level compression of stacked combinations and repeat headers only. NOT a marker rename, NOT a marker-count reduction (all 14 retained), NOT a semantic merge, NOT a grammar overhaul.
**Discipline:** push-deferred (local-canonical) until v0.1.3 launch is authorized. Hold-out Q11–Q16 sealed. Lossless round-trip mechanically verified by `r1_normalizer.py` (6/6 self-tests PASS).

---

## §1 — Empirical motivation (Phase 2 Q1–Q10 Test B)

| Pattern observed | Approx. occurrences (Q1–Q10 Test B) | Density-gain target |
|---|---|---|
| `[X][CONF(level)]` stack | ≈30 (≈half of all bracket pairs) | P1 — highest density |
| `[FACT][NOSRC]` co-stack | 2–3 (q1, q9, q4) | P2 — CEO-named |
| 3+ same-marker run (REC×4 in q3, FACT.H×3 in q5, LIMIT×2–3 in q1/q2/q3/q5 finals) | 4 cells | P3 — block form |

Logician AOV-68 also concurred quantitatively: Logician scored **uniform +1** on D7/D8 across Test B Q1–Q10 — even an experienced rater perceived enough constant prose cost to score it under the strict reading. R1 targets that constant cost.

---

## §2 — Pattern P1: `[X][CONF(level)]` → `[X.<lvl>]`

**Trigger:** any marker `X` immediately followed by `[CONF(high|medium|low)]` on the same claim.

**Compressed form:** `[X.H]`, `[X.M]`, `[X.L]` where `.H` / `.M` / `.L` is the CONF level **only**.

**Examples (round-trip verified):**

| Long form (v0.1.2) | R1 P1 (v0.1.3 alias) |
|---|---|
| `[FACT][CONF(high)] Water boils at 100°C at standard atmospheric pressure.` | `[FACT.H] Water boils at 100°C at standard atmospheric pressure.` |
| `[HYP][CONF(medium)] Reducing prompt verbosity by 30% will decrease hallucination.` | `[HYP.M] Reducing prompt verbosity by 30% will decrease hallucination.` |
| `[REC][CONF(low)] Try Cython for the hot path.` | `[REC.L] Try Cython for the hot path.` |

**Mechanical density gain:** ≈50% bracket reduction in dense passages.

---

## §3 — Pattern P2: `[FACT][NOSRC]` → `[FACT?]` (CEO-named)

**Trigger (narrow):** **only** when both `[FACT]` and `[NOSRC]` apply to the same claim. Bare `[NOSRC]`, `[NOSRC][UNCERTAIN]`, `[LIMIT][NOSRC]`, `[BELIEF][NOSRC]` are **NOT** compressed and remain in long form.

**Compressed form:** `[FACT?]`. The `?` denotes source-not-produced-this-turn within the FACT context, **NOT** an interrogative, **NOT** a hedged FACT, **NOT** a downgrade to BELIEF.

**Composes with P1:** `[FACT][CONF(medium)][NOSRC]` → `[FACT.M?]` (P1+P2 stacked).

**Examples:**

| Long form | R1 P2 (or P1+P2) |
|---|---|
| `[FACT][NOSRC] Most LLM hallucinations occur on long-tail entity questions.` | `[FACT?] Most LLM hallucinations occur on long-tail entity questions.` |
| `[FACT][CONF(medium)][NOSRC] Meditation practice longer than 8 weeks shifts cortisol baseline.` | `[FACT.M?] Meditation practice longer than 8 weeks shifts cortisol baseline.` |

---

## §4 — Pattern P3: 3+ same-marker run → block form

**Trigger:** 3 or more consecutive claims sharing the same marker (and optionally the same CONF level). 2-claim runs stay long form.

**Compressed form:**
```
[MARKER, default CONF(level)]
- claim 1.
- claim 2.
- [.<lvl>] claim 3 (override CONF level only).
[/MARKER]
```

**Close-tag `[/MARKER]` is REQUIRED on:**
- Any block of 3+ items (per AOV-68 mod P3.1).
- Any block followed by additional bulleted text within the same response (per AOV-68 mod P3.1).

The close-tag may be elided **only** when the block is the final paragraph of the response. UR-9 (new in v0.1.3) encodes this rule.

**Example:**

| Long form (q3 REC run) | R1 P3 |
|---|---|
| `[REC][CONF(medium)] Use structured output. [REC][CONF(medium)] Add eval harness. [REC][CONF(medium)] Cache prompts. [REC][CONF(low)] Try Cython for hot path.` | `[REC, default CONF(medium)]`<br>`- Use structured output.`<br>`- Add eval harness.`<br>`- Cache prompts.`<br>`- [.L] Try Cython for hot path.`<br>`[/REC]` |

---

## §5 — v0.1.3 protocol-doc patches required (from AOV-68 mods)

These patches MUST land in `AOVEN_PROTOCOL_v0.1.md` v0.1.3 before the compressed forms are introduced to graders. Captured here so Scribe (AOV-71) can apply.

### M1 — P1 doc-level disambiguation

**M1.1 (normalizer fix, applied):** `RATIFIED_MARKERS` in `r1_normalizer.py` corrected to the canonical 14: FACT, HYP, INTUIT, ANALOGY, BELIEF, EMOTION, MEMORY, INTERPRET, UNCERTAIN, NOSRC, CONF, REC, SPEC, LIMIT. Removed spurious META/DEFINE; restored ANALOGY/EMOTION.

**M1.2 (§Formats subsection, v0.1.3):** Add the sentence:
> "`.H/.M/.L` denotes the CONF level only; AOVEN does not introduce sub-marker namespaces."

### M2 — P2 anti-slippage guardrails

**M2.1 (§Anti-slippage rules, new row):**

| Transition | Risk | Blocking marker / rule |
|---|---|---|
| `[FACT?]` → `[BELIEF]` | Compressed FACT silently demoted by reader's natural-language `?` parse | `[FACT?]` retains the FACT verifiability-in-principle commitment. Challenge response per UR-7 applies: produce source (upgrade to bare `[FACT]`) or downgrade to `[UNCERTAIN]`. |

**M2.2 (§Markers, FACT row, new "Compressed alias" cell):**
> `[FACT?]` ≡ `[FACT][NOSRC]`. The `?` denotes source-not-produced-this-turn within the FACT compression context. It is NOT an interrogative and does NOT reduce the FACT-shaped commitment to verifiability.

**M2.3 (§Usage Rules, UR-7 amendment):**
> UR-7 — Challenge response for BELIEF, NOSRC, and `[FACT?]`: when challenged, produce an external source (upgrade to FACT / bare FACT) or explicitly downgrade to UNCERTAIN. Silent withdrawal is a slippage. **This applies equally to the compressed `[FACT?]` form.**

### M3 — P3 boundary tightening

**M3.1 (§Usage Rules, UR-9 new):**
> UR-9 — P3 block close-tag REQUIRED on (a) any block of 3+ items, (b) any block followed by additional bulleted text within the same response. May be elided only when the block is the final paragraph of the response.

**M3.2 (normalizer extension, applied):** `expand_p3_block` distributes the header marker + default CONF to each bullet (with inline `[.<lvl>]` overrides taking precedence) before grader preprocessing. Round-trip verified case 6.

---

## §6 — Risks and mitigations (per pattern)

| Risk | Pattern | Mitigation |
|---|---|---|
| **Risk A — `.H/.M/.L` reads as sub-marker namespace** | P1 | M1.2 doc patch + normalizer round-trip. |
| **Risk B — marker name collapse** | P1 | Full marker name retained verbatim before dot. Mechanically zero. |
| **Risk C — marker erasure (info loss)** | P1, P2 | Normalizer round-trip 6/6 PASS. Mechanically lossless. |
| **Risk D — `[FACT?]` reads as questioning** | P2 | M2.1+M2.2+M2.3 doc patches. Narrow trigger (FACT only). |
| **Risk E — P3 block boundary ambiguity** | P3 | M3.1 (close-tag REQUIRED). |
| **Risk F — per-claim grader sees bare bullets in P3** | P3 | M3.2 (`expand_p3_block` distributes header marker to bullets). |

---

## §7 — Round-trip lossless claim

`r1_normalizer.py` provides `normalize(text)` that re-expands all P1, P2, P3-inline, and P3-block compressed forms into v0.1.2 long form. Six self-tests PASS:

1. **P1 only** (q5 French Revolution): `[FACT.H]` → `[FACT][CONF(high)]`.
2. **P1+P2 composite** (q9 meditation): `[FACT.M?]` → `[FACT][CONF(medium)][NOSRC]`.
3. **P3 inline override** (q3 REC block): `[.L]` → `[CONF(low)]` inside a P3 bullet list.
4. **P2 bare**: `[FACT?]` → `[FACT][NOSRC]`.
5. **Negative**: bare `[NOSRC] [CONF(medium)]` is NOT decompressed (P2 trigger is FACT-only).
6. **P3 block distribution** (new for AOV-68 M3.2): `[REC, default CONF(medium)] - a. - b. - c. [/REC]` → three full `[REC][CONF(medium)]`-prefixed lines.

These round-trips back the lossless-alias claim mechanically rather than as prose.

---

## §8 — Sister artifacts

- `tests/phase2/r1_normalizer.py` — round-trip verifier (6/6 PASS).
- `tests/phase2/r1_mini_ab_plan.md` — cell matrix, prompts, scoring scheme, decision rule.
- AOV-68 verdict `cb33d2b8` — Logician PASS-WITH-MOD on P1/P2/P3.
- AOVEN_PROTOCOL_v0.1.md — canonical v0.1.2 reference.
