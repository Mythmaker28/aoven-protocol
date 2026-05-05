# LinkedIn announcement — Aoven v0.1.2

**Channel:** LinkedIn (Tommy's account, board-level — not delegated).
**Format:** single paragraph, professional register, no jargon, links to DOI + repo.
**Status:** draft — pending Logician NOSRC audit + CEO sign-off.

---

## Post (single paragraph, ~110 words, professional register)

I'm sharing the v0.1.2 results for Aoven, a small open-source protocol that asks an LLM to label its own claims with markers like "fact," "hypothesis," "intuition," "no source," "limit." The point is to make the model's epistemic status visible at the response level — not to teach it new facts. We tested it on `claude-opus-4-7` across 16 questions in factual, speculative, ethical, and self-knowledge domains, with two independent raters scoring the responses **after markers were stripped**, so the protocol cannot get credit for marker presence alone. On a sealed hold-out set the criterion the rubric was originally derived against was confirmed at higher margin (91.7 % and 100 % aggregate score reduction across raters; substantial inter-rater κ = 0.759). It is one model, sixteen questions, two LLM raters — not "Aoven works in general." Repo and full reconciliation file: github.com/Mythmaker28/aoven-protocol. Persistent identifier: https://doi.org/10.5281/zenodo.20012818.

---

## NOSRC source citations for every empirical claim above

[FACT] 14 markers — `AOVEN_PROTOCOL_v0.1.md` §"Markers" (commit history on `Mythmaker28/aoven-protocol`).
[FACT] `claude-opus-4-7`, 16 questions across 5 domains — `AOV_TEST_PLAN_v0.1.md` §"Test Questions"; `tests/phase2/reconciliation_holdout_v0.1.2.md` §"Aggregate L1 results".
[FACT] Two independent raters, scoring stripped prose — `AOV_TEST_PLAN_v0.1.md` v0.1.2 §"Layer 1 — Blind epistemic-quality score (markers mechanically stripped)"; AOV-55 / AOV-56 sealing comments.
[FACT] Hold-out 91.7 % (Logician) / 100.0 % (IR) aggregate L1 score reduction — `tests/phase2/reconciliation_holdout_v0.1.2.md` §"Means and improvements".
[FACT] κ = 0.759 substantial Σ-level on 12 hold-out cells — same file, §"Inter-rater agreement".
[FACT] Criterion derived on Q1–Q10, confirmed on sealed Q11–Q16 — AOV-36 (ratification), AOV-49 (hold-out execution), AOV-67 (push), AOV-1 mirror comments `765cf513` (provisional) and `9b8b405b` (confirmatory).
[LIMIT] "One model, sixteen questions, two LLM raters" — same file §"Findings carried forward to v0.1.3" + the canonical scoping in the preprint draft (`docs/dissemination/v0.1.2/preprint_arxiv_cs_cl.md` §4).

---

## Aoven-marker face-validity audit on the post text itself

The single-paragraph post above contains no claim that does not have a NOSRC citation in the table above. It does not say "Aoven reduces hallucinations" without scoping; it says "make the model's epistemic status visible at the response level." It does not say "Aoven works in general"; it says "It is one model, sixteen questions, two LLM raters." The single quasi-claim of novelty ("small open-source protocol") is a description of the artefact, not an empirical claim, and is verifiable directly from the repo.

---

## Posting hygiene notes for Tommy

- Tommy is the only externally-identified actor; outbound posting is not delegated (per AOV-91 directive).
- DOI substituted in-file per AOV-91 board direction (Cowork local-board comment `e001a922`, 2026-05-05): concept DOI `https://doi.org/10.5281/zenodo.20012818` (Zenodo, sponsor-confirmed retrievable 2026-05-04). No further substitution required at post-time.
- Suggested character of post: declarative-modest. The result is a confirmatory pass on a small set, not a benchmark sweep. Match register accordingly.
- Suggested LinkedIn tagging: tag `arXiv` if the preprint has been accepted; tag `Anthropic` only if the cold email to Anthropic alignment (see `external_contacts_shortlist.md`) has been answered or acknowledged. Do not tag organisations that have not engaged.
- Do not post on a Friday after 16:00 local time — engagement halves over the weekend (industry NOSRC heuristic; not load-bearing on this draft).

---

*Drafted by CanonicalScribe (`e19c696f`) under AOV-91. Pending Logician NOSRC audit + CEO sign-off before Tommy posts.*
