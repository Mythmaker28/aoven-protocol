# "Show HN" submission — Aoven v0.1.2

**Channel:** Hacker News, "Show HN" tag.
**Format:** title (≤ 80 chars) + body explaining what Aoven is, what was tested, what passed, what's next.
**Status:** draft — pending Logician NOSRC audit + CEO sign-off.
**Posting actor:** Tommy (board, not delegated).

---

## Title (≤ 80 chars)

**Option A (recommended, 74 chars):**
```
Show HN: Aoven – an LLM epistemic-marker protocol scored on stripped prose
```

**Option B (56 chars):**
```
Show HN: Aoven v0.1.2 – LLMs label their own claim types
```

**Option C (74 chars):**
```
Show HN: Aoven – make an LLM tag every claim FACT, HYP, NOSRC, LIMIT, etc.
```

[FACT] Length verified by mechanical character count (Python `len()` on UTF-8 string; the en-dash `–` is U+2013, one codepoint), including the `Show HN: ` prefix that HN requires for the tag. All three options are ≤ 80 chars (HN's submission-title limit). Option A 74 / Option B 56 / Option C 74 — verified at revision after Logician audit on AOV-96 returned FLAG on prior counts (claimed 73 / 62 / 78); discrepancy was eyeball-estimation error, no posting risk on any option.

[REC] Use Option A. It states the load-bearing methodological commitment ("scored on stripped prose") in the title, which is the part that distinguishes Aoven from a marker-decoration protocol.

---

## Body

```
Aoven is a small open protocol that asks an LLM to prefix each claim with one of 14 markers — FACT, HYP, INTUIT, ANALOGY, BELIEF, EMOTION, MEMORY, INTERPRET, UNCERTAIN, NOSRC, CONF, REC, SPEC, LIMIT — plus 13 anti-slippage transition rules (don't slide HYP into FACT, don't use ANALOGY as proof, etc.). It is not a conlang and not a fine-tune. It is a prompt-and-response convention that ships as plain markdown.

What we tested in v0.1.2:

- Single LLM (claude-opus-4-7), single-shot deterministic generation.
- 16 questions across factual, speculative, emotional/personal, technical, historical, LLM-self-knowledge, ethical, and predictive domains.
- Test A: plain prompt. Test B: same question, Aoven-framed.
- Two independent LLM raters score each response on 8 epistemic-quality dimensions on a 0–3 scale. Crucially, on Test B the markers are MECHANICALLY STRIPPED before Layer-1 scoring — so the protocol cannot get credit for marker presence alone. Every claimed improvement has to manifest in the underlying prose.
- A second layer (markers visible) checks marker accuracy and protocol conformance, but does not gate the verdict.

The pass criterion (the v0.1.2 patch, after the v0.1 criterion was found structurally unachievable) is three-part:

  (a) mean Layer-1 8-dim aggregate Test B vs A improvement ≥ 20 %;
  (b) no epistemic dimension D1–D6 mean increases by > 0.5 pts;
  (c) D7 (clarity) and D8 (cognitive load) mean Δ ≤ +0.5 each, and a Δ > 0 requires a cited phrase that creates the problem (no uniform per-response prose-cost penalty).

The criterion was DERIVED on the primary set Q1–Q10. To rule out "criterion fitted to the data," we ran a sealed hold-out Q11–Q16:

- The CTO did not preview Q11–Q16 content before triggering generation.
- The hold-out probe design document was not pushed to the public repo.
- Raters did not read each other's hold-out passes before sealing their own.

Result on the hold-out: Logician 91.7 % aggregate score reduction, IndependentRater 100 %. Both raters PASS all three criteria independently. Inter-rater quadratic-weighted κ on the 12 hold-out cells = 0.759 (substantial, Landis–Koch). The hold-out outperforms the primary set under both raters, which is the cleanest signal that the criterion is not fitted to Q1–Q10 idiosyncrasies.

What I am NOT claiming:

- Not "Aoven works in general." It is one model, sixteen questions, two LLM raters.
- Not "Aoven reduces hallucinations" without scoping. The strongest signal is on D1 (unsourced assertion, κ = 0.938) and D5 (sycophancy / belief, κ = 0.881). D3, D4, D6 have lower κ that reflect sparse-distribution artefacts, not random rater divergence.
- Not "Aoven is novel." Many of the markers are common in epistemological writing. What is novel is the (rubric, sealed hold-out, three-part criterion) execution package — not the vocabulary.

What's next:

- v0.1.3 patches two findings the hold-out surfaced: marker-syntax compression so stripping doesn't leave dangling syntax (R1, AOV-37), and a single-level CONF lock (no `CONF(low-medium)` composites).
- v0.2 expansion (AOV-90, in pre-registration): ≥ 20 primary + ≥ 10 hold-out questions, ≥ 3 distinct domains, ≥ 2 independent humans + 4 LLM raters, kappa power analysis with stated α, pre-registered hypotheses with directional predictions, cross-domain leave-one-out overfit guard.
- Human raters and cross-LLM generation are the two biggest gaps; both are scoped into v0.2, neither is in v0.1.2.

Repo (everything is there — protocol, rubric, raw responses, scores, reconciliation): https://github.com/Mythmaker28/aoven-protocol

Persistent identifier: https://doi.org/10.5281/zenodo.20012818

The methodology and the verdict are the load-bearing pieces. If you find a flaw in the rubric, the contamination-gating, or the κ computation, I want to hear about it. PRs welcome on the rubric, on counter-examples to the markers, and on candidate questions that pressure dimensions we currently underprobe (the hold-out missed #7 MEMORY→data; that's a known coverage gap).
```

---

## NOSRC source citations for every empirical claim in the body

[FACT] 14 markers, 13 anti-slippage transitions, plain markdown — `AOVEN_PROTOCOL_v0.1.md` v0.1.2 §"Markers" + §"Anti-slippage transitions".
[FACT] `claude-opus-4-7`, single-shot deterministic — `AOV_TEST_PLAN_v0.1.md` v0.1.2 §"Test Structure"; `tests/phase2/reconciliation_holdout_v0.1.2.md` §"Anti-contamination discipline" point 1.
[FACT] 16 questions across listed domains — `AOV_TEST_PLAN_v0.1.md` §"Test Questions" (Q1–Q10 primary) and Q11–Q16 hold-out (`tests/phase2/test_a/q11..16.md`, `tests/phase2/test_b/q11..16.md`).
[FACT] Two independent LLM raters; Layer-1 markers stripped before scoring — `AOV_TEST_PLAN_v0.1.md` v0.1.2 §"Layer 1" (markers mechanically stripped); rater identities Logician (`2ae117a1`) and IndependentRater (`00749544`); independence declarations under AOV-55 / AOV-56.
[FACT] Three-part criterion specification — `AOV_TEST_PLAN_v0.1.md` v0.1.2 §"v0.1.2 three-part rule"; ratification AOV-36.
[FACT] D7/D8 citation rule (no uniform prose-cost penalty) — `AOV_TEST_PLAN_v0.1.md` v0.1.2 §"D7/D8 citation discipline"; CEO adjudication AOV-35.
[FACT] v0.1 criterion structurally unachievable — `tests/phase2/reconciliation_logician_independentrater.md` §"Pass Criterion Analysis".
[FACT] Anti-contamination discipline points (CTO didn't preview, probe doc not pushed, raters didn't read each other) — `tests/phase2/reconciliation_holdout_v0.1.2.md` §"Anti-contamination discipline".
[FACT] Hold-out 91.7 % / 100 %, κ = 0.759 substantial — same file §"Means and improvements" + §"Inter-rater agreement".
[FACT] Both raters PASS three-part rule independently on hold-out — same file §"v0.1.2 three-part rule applied to Q11–Q16".
[FACT] Hold-out improvement higher than primary — same file §"Means and improvements" comparison line.
[FACT] D1 κ = 0.938; D5 κ = 0.881 — `tests/phase2/reconciliation_logician_independentrater.md` §"Computed kappas".
[FACT] D3 / D4 / D6 sparse-distribution artefact — same file §"Computed kappas" footnote †.
[FACT] R1 marker-syntax compression motivated by Q14B regression — `tests/phase2/reconciliation_holdout_v0.1.2.md` §"Findings carried forward to v0.1.3" point 1.
[FACT] Single-level CONF lock evidence — same file §"Findings carried forward to v0.1.3" point 2.
[FACT] v0.2 expansion targets — AOV-1 board master directive `3222338e` (2026-05-03), reproduced in AOV-90 description.
[LIMIT] "One LLM, sixteen questions, two LLM raters" — `docs/dissemination/v0.1.2/preprint_arxiv_cs_cl.md` §4.
[LIMIT] "#7 MEMORY→data coverage gap on hold-out" — `tests/phase2/reconciliation_holdout_v0.1.2.md` §"Findings carried forward to v0.1.3" point 3.

---

## Aoven-marker face-validity audit on the body text

- The body uses **declarative-modest** register throughout. No "revolutionary," "breakthrough," "paradigm shift" — those are sycophancy-of-self vocabulary that violate Aoven's anti-aura rule.
- The "What I am NOT claiming" block is mandatory and load-bearing — do not cut it during HN-edit shrinkage.
- The phrase "If you find a flaw in the rubric, the contamination-gating, or the κ computation, I want to hear about it" is a Hacker News register move, not an Aoven discipline move; it is rhetorical, not a load-bearing claim. Acceptable to keep, fine to drop.
- The body explicitly invites adversarial PRs (counter-examples, hard questions). This is consistent with the project's RedTeam role and aligns with the anti-overclaiming rule. Keep.
- Length: the body above is ~3600 characters. HN does not have a hard limit on submission body, but bodies > 4000 chars routinely get downvoted as "wall of text." If the body needs trimming, the safe cuts are: (1) the "What's next" v0.2 bullet detail (compress to "v0.2 in pre-reg, see AOV-90"); (2) the closing PR-invitation paragraph.

---

## Posting hygiene for Tommy

- The Show HN tag is `Show HN:` exactly — HN moderators normalise the prefix, so include it.
- DOI substituted in-file (`https://doi.org/10.5281/zenodo.20012818`) per AOV-91 board direction (Cowork local-board comment `e001a922`, 2026-05-05). No further substitution required at post-time.
- Recommended posting window: weekday between 13:00 and 17:00 UTC, when HN's frontpage churn is highest. Not load-bearing on the draft, just folklore.
- Author identity: Tommy posts under his own HN account; do not delegate. The board comment chain explicitly names Tommy as the only externally-identified actor.
- If the post takes off, the comment thread is the test of NOSRC discipline. If anyone challenges a claim, every claim above has a citation in the table — answer with the citation, not with a defensive rephrase.
- If the post does not take off, do not boost it. The result is what it is: confirmatory pass on a small set, and the dissemination plan does not depend on virality.

---

*Drafted by CanonicalScribe (`e19c696f`) under AOV-91. Pending Logician NOSRC audit + CEO sign-off before Tommy posts. Title and body alternates can be selected at posting time without re-audit, provided no [FACT]-tier claim is added or modified.*
