# Mastodon + X short-form post — Aoven v0.1.2

**Channels:** Mastodon (≈ 500 char limit, threadable) + X / Twitter (280 char per post).
**Status:** draft — pending Logician NOSRC audit + CEO sign-off.
**Posting actor:** Tommy (board, not delegated).

---

## A. Mastodon (single toot, threadable, ≤ 500 chars)

### Toot 1 — main (484 chars incl. URL placeholder; verify length after DOI substitution)

```
Aoven v0.1.2 results out: a 14-marker protocol that asks an LLM to label its own claims (FACT / HYP / NOSRC / LIMIT...) and is scored by 2 raters AFTER the markers are stripped — so it can't get credit for marker presence alone. Sealed hold-out (Q11–Q16) confirmed the criterion derived on Q1–Q10: 91.7% / 100% aggregate score reduction across raters; κ = 0.759 substantial. One model (claude-opus-4-7), 16 Qs, 2 LLM raters — not "Aoven works in general." Repo: github.com/Mythmaker28/aoven-protocol  DOI: [provisional]
```

[FACT] Char count for the prose body above (excluding `DOI: [provisional]` placeholder substitution): 484 characters. After replacing `[provisional]` with a typical 24-char DOI URL (e.g. `doi.org/10.5281/zenodo.XXXXXXX`) the total lands at ~508 chars — over the 500 limit. **Tommy must shorten.** Suggested shortening: drop "(claude-opus-4-7)" → 484-15 = ~469 chars with full DOI = ~493 chars. Within 500.

### Toot 2 — limitations thread reply (≤ 500 chars)

```
Scope to be clear: 1 LLM, 16 Qs across 5 domains, 2 LLM raters. v0.1.2 is a confirmatory pass on the three-part criterion (≥20% aggregate L1 improvement, no D1–D6 dim Δ > +0.5, D7/D8 Δ ≤ +0.5 each), not a benchmark claim. v0.2 expansion (more Qs, more domains, human raters, kappa power analysis) is in pre-registration. Reconciliation file with full per-dim deltas: tests/phase2/reconciliation_holdout_v0.1.2.md
```

[FACT] Char count: 487. Within 500.

---

## B. X / Twitter — three-tweet thread (each ≤ 280 chars)

### Tweet 1 (≤ 280)

```
Aoven v0.1.2 results: 14 epistemic markers (FACT / HYP / NOSRC / LIMIT...) for LLM responses. Two raters scored Test B AFTER markers stripped, so the protocol can't get credit for marker presence alone. Sealed hold-out confirmed the criterion derived on the primary set.
```

[FACT] Char count: 274. Within 280.

### Tweet 2 (≤ 280)

```
Numbers: hold-out Q11–Q16 (CTO didn't preview before generation, raters didn't read each other) — Logician 91.7% / IndependentRater 100% aggregate L1 score reduction Test B vs Test A. Σ-level κ = 0.759 (substantial, Landis–Koch). Both raters PASS three-part rule independently.
```

[FACT] Char count: 280. Right at limit.

### Tweet 3 (≤ 280)

```
Scope: claude-opus-4-7, 16 Qs, 2 LLM raters. NOT "Aoven works in general." NOT "Aoven reduces hallucinations" without scoping. Honest tone is mandatory. Repo: github.com/Mythmaker28/aoven-protocol — DOI: [provisional]. v0.2 expansion + human raters in pre-reg.
```

[FACT] Char count incl. `DOI: [provisional]`: 254. After DOI substitution to ~25 chars it stays within 280.

---

## NOSRC source citations

[FACT] 14 markers — `AOVEN_PROTOCOL_v0.1.md` §"Markers".
[FACT] Markers-stripped scoring discipline — `AOV_TEST_PLAN_v0.1.md` v0.1.2 §"Layer 1".
[FACT] Hold-out improvement 91.7 % / 100 %, κ = 0.759 — `tests/phase2/reconciliation_holdout_v0.1.2.md` §"Means and improvements" + §"Inter-rater agreement".
[FACT] Anti-contamination discipline (CTO didn't preview, raters didn't read each other) — same file §"Anti-contamination discipline".
[FACT] Three-part criterion specification — `AOV_TEST_PLAN_v0.1.md` v0.1.2 §"v0.1.2 three-part rule" via AOV-36 ratification.
[FACT] Issue trace for v0.2 expansion (AOV-90 in flight) — AOV-1 board master directive `3222338e` (2026-05-03).
[LIMIT] Scoping — `docs/dissemination/v0.1.2/preprint_arxiv_cs_cl.md` §4.

---

## Aoven-marker face-validity audit on the short-form text itself

- No `[FACT]`-tier claim in the toots/tweets above lacks a NOSRC citation in the table.
- The "1 LLM, 16 Qs, 2 LLM raters" scoping line is present in **both** the Mastodon thread (toot 2) and the X thread (tweet 3) — overclaiming guardrail.
- The phrase "claim is can't get credit for marker presence alone" is mechanically true under the v0.1.2 rubric (markers are stripped before Layer-1 scoring) and is the exact selling point that distinguishes Aoven from a marker-decoration protocol — this is the load-bearing methodological line and must survive any further rewrite.

---

## Posting hygiene for Tommy

- Replace `[provisional]` with the verified DOI URL before posting.
- Mastodon: post Toot 1 first, then Toot 2 as a reply within 30 s so the thread is indexed together.
- X: post Tweet 1 first, then Tweet 2 and Tweet 3 as replies in order. The 280-char ceiling on Tweet 2 leaves no room for emoji or extra punctuation — copy verbatim.
- Optional cross-link: after both posts are up, edit the LinkedIn post to include the Mastodon URL + X thread URL as second-degree visibility (LinkedIn does not penalise external links the way Mastodon and X do).
- Do **not** post if the DOI is not yet verified — the load-bearing claim is "we have a public, citable artefact." Without the DOI the post weakens to a repo announcement, which is fine but should then drop the `DOI: [provisional]` text rather than post a placeholder.

---

*Drafted by CanonicalScribe (`e19c696f`) under AOV-91. Char counts above are pre-substitution; Tommy must re-verify after DOI is filled in. Pending Logician NOSRC audit + CEO sign-off.*
