# Mastodon + X short-form post — Aoven v0.1.2

**Channels:** Mastodon (≈ 500 char limit, threadable) + X / Twitter (280 char per post).
**Status:** draft — Logician audit returned BLOCK on Toot 1 v1 (519 chars literal, over 500); v2 in this file is the revision. Pending Logician re-audit + CEO sign-off.
**Posting actor:** Tommy (board, not delegated).
**Char-count basis:** literal Python `len()` on UTF-8 string; post-DOI-substitution simulated by replacing `[provisional]` (13 chars) with a representative Zenodo DOI URL `https://doi.org/10.5281/zenodo.1234567` (38 chars), i.e. +25 chars per occurrence. Stricter than Mastodon/X's documented "URL-counts-as-23" platform rule, so a block that passes here will pass on the platform.

---

## A. Mastodon (single toot, threadable, ≤ 500 chars)

### Toot 1 — main (revised v2; literal 439 chars; post-DOI-substitution 464 chars)

```
Aoven v0.1.2: a 14-marker protocol that asks an LLM to label its own claims (FACT / HYP / NOSRC / LIMIT…), scored by 2 raters AFTER markers stripped — can't earn credit from marker presence alone. Sealed hold-out reconfirmed the primary-set criterion: 91.7% / 100% aggregate L1 score reduction; κ = 0.759 substantial. 1 LLM, 16 Qs, 2 LLM raters — not "Aoven works in general." Repo: github.com/Mythmaker28/aoven-protocol DOI: [provisional]
```

[FACT] In-file literal length 439 chars (Python `len()`). Post-DOI-substitution length 464 chars assuming a 38-char Zenodo DOI URL. Both ≤ 500. Margin to the 500-char Mastodon limit: 36 chars.

[FACT] Differences from v1: tightened opening ("Aoven v0.1.2:" instead of "Aoven v0.1.2 results out:"); dropped "(claude-opus-4-7)" parenthetical; replaced "Sealed hold-out (Q11–Q16) confirmed the criterion derived on Q1–Q10" with "Sealed hold-out reconfirmed the primary-set criterion"; collapsed double-space before "DOI:" to single space. Net saving from v1: 80 chars (519 → 439).

### Toot 2 — limitations thread reply (literal 412 chars, no DOI substitution)

```
Scope to be clear: 1 LLM, 16 Qs across 5 domains, 2 LLM raters. v0.1.2 is a confirmatory pass on the three-part criterion (≥20% aggregate L1 improvement, no D1–D6 dim Δ > +0.5, D7/D8 Δ ≤ +0.5 each), not a benchmark claim. v0.2 expansion (more Qs, more domains, human raters, kappa power analysis) is in pre-registration. Reconciliation file with full per-dim deltas: tests/phase2/reconciliation_holdout_v0.1.2.md
```

[FACT] In-file literal length 412 chars. ≤ 500. (v1 claimed 487; recount shows 412 — Logician audit confirmed; previous claim was inflated by ~75. Body unchanged from v1.) Margin to 500: 88 chars.

---

## B. X / Twitter — three-tweet thread (each ≤ 280 chars)

### Tweet 1 (literal 270 chars, no DOI substitution)

```
Aoven v0.1.2 results: 14 epistemic markers (FACT / HYP / NOSRC / LIMIT...) for LLM responses. Two raters scored Test B AFTER markers stripped, so the protocol can't get credit for marker presence alone. Sealed hold-out confirmed the criterion derived on the primary set.
```

[FACT] Literal length 270 chars. ≤ 280. (v1 claimed 274; recount shows 270 — Logician audit confirmed.) Margin to 280: 10 chars.

### Tweet 2 (literal 277 chars, no DOI substitution)

```
Numbers: hold-out Q11–Q16 (CTO didn't preview before generation, raters didn't read each other) — Logician 91.7% / IndependentRater 100% aggregate L1 score reduction Test B vs Test A. Σ-level κ = 0.759 (substantial, Landis–Koch). Both raters PASS three-part rule independently.
```

[FACT] Literal length 277 chars. ≤ 280. (v1 claimed 280; recount shows 277 — Logician audit confirmed.) Margin to 280: 3 chars. Slim — copy verbatim, no emoji, no extra punctuation.

### Tweet 3 — revised v2 (literal 232 chars; post-DOI-substitution 257 chars)

```
Scope: 1 LLM (claude-opus-4-7), 16 Qs, 2 LLM raters. NOT "Aoven works in general." NOT "Aoven reduces hallucinations" without scoping. Repo: github.com/Mythmaker28/aoven-protocol — DOI: [provisional]. v0.2 + human raters in pre-reg.
```

[FACT] In-file literal length 232 chars. Post-DOI-substitution length 257 chars (38-char Zenodo DOI URL replaces 13-char `[provisional]`). Both ≤ 280. Margin to 280: 23 chars.

[FACT] Differences from v1: dropped "Honest tone is mandatory." sentence (24 chars); reframed "claude-opus-4-7" as parenthetical to "1 LLM"; tightened "v0.2 expansion + human raters in pre-reg" → "v0.2 + human raters in pre-reg". Net saving from v1: 28 chars (260 → 232) — needed because v1 post-DOI-substitution at 285 chars was over the 280 limit (Logician audit did not flag this; Scribe self-flagged on re-recount per Logician mod #4).

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
- The "1 LLM, 16 Qs, 2 LLM raters" scoping line is present in Toot 1, Toot 2, and Tweet 3 — overclaiming guardrail honoured at the recipient surface, not just an audit appendix.
- The phrase "can't earn credit from marker presence alone" / "can't get credit for marker presence alone" is mechanically true under the v0.1.2 rubric (markers are stripped before Layer-1 scoring) and is the load-bearing methodological line that distinguishes Aoven from a marker-decoration protocol; it must survive any further rewrite.
- All char-count [FACT] claims in this revision are recounted by independent Python `len()` and verified by simulated post-DOI substitution. Original v1 claims were undercounts (Toot 1 by 35 chars literal, Toot 2 by 75, Tweet 1 by 4, Tweet 2 by 3, Tweet 3 by 6). Source of the v1 error: manual eyeball estimation rather than mechanical recount.

---

## Posting hygiene for Tommy

- Replace `[provisional]` with the verified DOI URL before posting.
- Mastodon: post Toot 1 first, then Toot 2 as a reply within 30 s so the thread is indexed together.
- X: post Tweet 1 first, then Tweet 2 and Tweet 3 as replies in order. Tweet 2 has only 3 chars of margin to the 280-char limit — copy verbatim, no emoji, no extra punctuation, no auto-correct surprises.
- The post-DOI-substitution simulation in this file uses a representative 38-char Zenodo URL. If the verified DOI URL is shorter (e.g. `doi.org/10.5281/zenodo.NNNNNNN` at 30 chars), the actual posted length will be 8 chars less than reported here. If the verified DOI is *longer* than 38 chars, recount before posting Toot 1.
- Optional cross-link: after both posts are up, edit the LinkedIn post to include the Mastodon URL + X thread URL as second-degree visibility (LinkedIn does not penalise external links the way Mastodon and X do).
- Do **not** post if the DOI is not yet verified — the load-bearing claim is "we have a public, citable artefact." Without the DOI the post weakens to a repo announcement, which is fine but should then drop the `DOI: [provisional]` text rather than post a placeholder.

---

*Drafted by CanonicalScribe (`e19c696f`) under AOV-91. Char counts above are mechanical recounts (Python `len()`); post-DOI substitution simulated against a 38-char representative DOI URL. v2 revision incorporates Logician audit verdict on AOV-96 (BLOCK on Toot 1 v1, FLAGs on char-count [FACT] claims throughout). Pending Logician re-audit + CEO sign-off.*
