# External contacts shortlist — Aoven v0.1.2

**Channel:** direct outbound email (Tommy's account, board-level — not delegated).
**Format:** for each contact, one paragraph of selection rationale + one cold-email draft (≤ 250 words) citing the DOI.
**Status:** draft — pending Logician NOSRC audit + CEO sign-off.
**Posting actor:** Tommy (board, not delegated).

---

## Selection set

The AOV-91 directive named four candidate organisations: **METR**, **Apollo Research**, **ARC Evals**, and **Anthropic alignment**. Three are selected below, with the fourth deferred and rationale given.

[REC] Selected: **METR**, **Apollo Research**, **Anthropic alignment**.
[REC] Deferred: **ARC Evals** — (a) the org rebranded to METR in 2023, so a separate ARC Evals contact is now downstream of the METR contact; (b) avoiding a duplicate ask preserves the limited "first contact" budget for non-overlapping evaluators. [INTUIT] If ARC Evals' legacy contact channel is still maintained separately by Tommy's records, treat it as a fallback if METR does not respond within 14 days.

---

## Contact 1 — METR (Model Evaluation and Threat Research)

### Selection rationale

[FACT] METR runs structured evaluations of frontier-LLM capabilities and risks, with a published methodological emphasis on rubric design, blind scoring, and sealed hold-out tasks. [INTUIT] This matches the load-bearing methodological commitments in Aoven v0.1.2 (markers stripped before Layer-1 scoring, sealed hold-out Q11–Q16, three-part criterion derived on primary then confirmed on hold-out) closer than any other public-facing eval org.

[REC] Why this org cares: Aoven is an instance of a "self-labelled epistemic-status" intervention scored on stripped prose. METR's evaluation pipeline is exactly the right pressure-test for whether the marker scheme survives outside the originator's hands. The cold email asks for methodological critique, not endorsement.

### Contact details

[provisional: contact email/lead-evaluator name to be verified by Tommy before sending. METR maintains a public contact form at metr.org; if the personal address of a lead evaluator is not in Tommy's records, default to the public form and flag this in the subject line.]

### Cold email draft (≤ 250 words)

```
Subject: [Aoven v0.1.2] LLM epistemic-marker protocol scored on stripped prose — would value methodological critique

Dear METR team,

I'm writing to share Aoven v0.1.2, an open-source protocol that asks an LLM to prefix each claim with one of fourteen markers (FACT / HYP / NOSRC / LIMIT and others), and is scored by two independent LLM raters AFTER the markers are mechanically stripped from the response. The point is to make the protocol unable to get credit for marker presence alone — every claimed improvement has to manifest in the underlying prose.

The v0.1.2 result is a confirmatory pass on a sealed hold-out (Q11–Q16): aggregate Layer-1 score reduction of 91.7 % (Logician rater) and 100.0 % (independent rater) Test B vs Test A, with quadratic-weighted κ = 0.759 (substantial, Landis–Koch) on the 12 hold-out cells. Both raters PASS the three-part criterion independently. Scope is one model (claude-opus-4-7), 16 questions, two LLM raters — explicitly NOT a "works in general" claim.

Repo with the protocol, rubric, raw responses, and reconciliation files: https://github.com/Mythmaker28/aoven-protocol
DOI: [provisional — to be added once verified]

I would value methodological critique, particularly on (a) the stripped-prose Layer-1 design, (b) the sealed-hold-out anti-contamination discipline, (c) the κ computation and the sparse-distribution artefacts on D3/D4/D6. If any part of the rubric, the contamination-gating, or the κ pipeline does not stand up, I want to know.

v0.2 is in pre-registration with human raters and cross-LLM generation. I'm happy to share the pre-registration draft for METR critique before I freeze it.

— Tommy
```

[FACT] Word count of body: 247 words. Within the ≤ 250 target.

---

## Contact 2 — Apollo Research

### Selection rationale

[FACT] Apollo Research's published research agenda includes deceptive-alignment evaluations, where the model's stated reasoning and its actual behaviour can diverge. [INTUIT] Aoven's marker discipline is mechanically aimed at the part of that surface where stated epistemic status (FACT vs HYP vs NOSRC) is the visible artefact. [LIMIT] Aoven does not measure deception; it measures self-labelled epistemic status under a stripped-prose rubric. The cold email scopes this honestly.

[REC] Why this org cares: if Apollo's evaluation stack ever wants a candidate "epistemic transparency" instrument, Aoven is the cheapest and most replicable one currently on the table — and the v0.1.2 hold-out result is a clean confirmatory pass, not a benchmark sweep. The ask is for evaluator review of whether the marker scheme is a useful primitive for their own deception-evals or whether the markers themselves are gameable in ways the v0.1.2 design did not stress.

### Contact details

[provisional: contact email/lead-researcher name to be verified by Tommy before sending. Apollo Research lists `info@apolloresearch.ai` as a general-purpose address; for evaluation methodology a personal address is preferred if Tommy has it. Do NOT send to a personal address Tommy is not certain is current.]

### Cold email draft (≤ 250 words)

```
Subject: [Aoven v0.1.2] Self-labelled epistemic-marker protocol — possible primitive for transparency evals?

Dear Apollo Research team,

Aoven is a small open protocol that asks an LLM to prefix each claim with one of 14 epistemic markers — FACT, HYP, NOSRC, LIMIT, BELIEF, CONF, etc. — and follow 13 anti-slippage transition rules. It is not a fine-tune, not a conlang. It is a prompt-and-response convention.

What I want to flag for Apollo specifically is the scoring discipline: the markers are MECHANICALLY STRIPPED before Layer-1 epistemic-quality scoring, so the protocol cannot get credit for marker presence alone. Every claimed improvement has to manifest in the underlying prose. v0.1.2 is a confirmatory pass on a sealed hold-out: aggregate Layer-1 reduction of 91.7 % / 100 % across two independent LLM raters, κ = 0.759, both raters pass the three-part criterion. Scope: 1 model, 16 questions, 2 LLM raters — not a generalisation claim.

I am writing because Apollo's deception-evaluation work touches the same surface as Aoven's marker discipline (stated epistemic status vs. underlying behaviour). The honest question is whether the marker scheme is gameable — whether a model could learn to PREFIX confident claims with HYP or NOSRC to evade a sycophancy / overclaiming penalty without any genuine epistemic concession. The v0.1.2 design did not stress that adversarial direction.

Repo: https://github.com/Mythmaker28/aoven-protocol
DOI: [provisional — to be added once verified]

A pointer to whether Aoven would be useful or counter-productive in your eval stack would be welcome.

— Tommy
```

[FACT] Word count of body: 245 words. Within the ≤ 250 target.

---

## Contact 3 — Anthropic alignment

### Selection rationale

[FACT] Aoven v0.1.2 was generated and scored on `claude-opus-4-7`, an Anthropic model. [INTUIT] This makes Anthropic's alignment team the most directly downstream stakeholder for whether the result generalises across the Claude family or is an opus-4-7-specific artefact. [LIMIT] Cross-LLM generation is explicitly out of v0.1.2 scope and is one of the two biggest gaps named in the limitations (the other being human raters); both are scoped into v0.2.

[REC] Why this org cares: a confirmatory pass that the model can label its own claims under a rubric that can't be gamed by marker presence alone is at minimum interesting capability data on Claude-opus-4-7. The cold email frames Aoven as a candidate transparency primitive that Anthropic alignment can stress-test on internal model variants if useful, not as a finished tool.

### Contact details

[provisional: contact channel to be verified by Tommy before sending. Anthropic alignment does not maintain a single advertised inbox; the safe default is Anthropic's general research-collaboration form, with a fallback of any direct contact Tommy has from prior outreach. Tag the org on LinkedIn ONLY if this email has been answered or acknowledged — do not tag pre-emptively.]

### Cold email draft (≤ 250 words)

```
Subject: [Aoven v0.1.2] Epistemic-marker protocol — confirmatory pass on claude-opus-4-7

Dear Anthropic alignment team,

Aoven is an open protocol that asks an LLM to prefix each claim with one of fourteen epistemic markers (FACT, HYP, NOSRC, LIMIT, CONF, BELIEF, etc.). v0.1.2 results were generated and scored on claude-opus-4-7.

Two independent LLM raters scored every Test B response AFTER the markers were mechanically stripped, so the protocol cannot earn credit from marker presence alone. On a sealed hold-out set (Q11–Q16) the criterion derived on the primary set was confirmed at higher margin: 91.7 % (Logician rater) and 100.0 % (independent rater) aggregate Layer-1 score reduction Test B vs Test A; quadratic-weighted κ = 0.759 (substantial, Landis–Koch) on 12 hold-out cells. Both raters pass the three-part criterion independently.

Scope is the honest part: one model, 16 questions across 5 domains, 2 LLM raters. The two biggest gaps — human raters and cross-LLM generation — are scoped into v0.2 (in pre-registration). Cross-LLM matters most to Anthropic specifically: until v0.2, the v0.1.2 result is a "Claude-opus-4-7 can do this" result, not a Claude-family or general-LLM result.

Repo: https://github.com/Mythmaker28/aoven-protocol
DOI: [provisional — to be added once verified]

I would value Anthropic alignment's view on (a) whether internal model variants would be a useful cross-LLM stress test for v0.2, and (b) whether any of the markers conflict with internal Claude policy or constitutional documents in ways the public protocol would benefit from knowing.

— Tommy
```

[FACT] Word count of body: 246 words. Within the ≤ 250 target.

---

## NOSRC source citations for every empirical claim across the three emails

[FACT] 14 markers, 13 anti-slippage transitions, plain markdown — `AOVEN_PROTOCOL_v0.1.md` v0.1.2 §"Markers" + §"Anti-slippage transitions".
[FACT] `claude-opus-4-7` generation, two independent LLM raters, markers stripped before Layer 1 — `AOV_TEST_PLAN_v0.1.md` v0.1.2 §"Layer 1 — Blind epistemic-quality score (markers mechanically stripped)"; rater identities Logician (`2ae117a1`) and IndependentRater (`00749544`); independence sealing AOV-55 / AOV-56.
[FACT] 16 questions across 5 domains, sealed hold-out Q11–Q16 — `AOV_TEST_PLAN_v0.1.md` §"Test Questions"; `tests/phase2/test_a/q11..16.md`, `tests/phase2/test_b/q11..16.md`.
[FACT] Hold-out 91.7 % (Logician) / 100.0 % (IR) aggregate L1 score reduction — `tests/phase2/reconciliation_holdout_v0.1.2.md` §"Means and improvements".
[FACT] κ = 0.759 substantial, Σ-level on 12 hold-out cells — same file §"Inter-rater agreement".
[FACT] Both raters PASS three-part rule independently on hold-out — same file §"v0.1.2 three-part rule applied to Q11–Q16".
[FACT] D3/D4/D6 sparse-distribution κ artefact — `tests/phase2/reconciliation_logician_independentrater.md` §"Computed kappas" footnote †.
[FACT] Three-part criterion specification — `AOV_TEST_PLAN_v0.1.md` v0.1.2 §"v0.1.2 three-part rule"; ratification AOV-36.
[FACT] v0.2 expansion — AOV-1 board master directive `3222338e` (2026-05-03), reproduced in AOV-90 description; in pre-registration.
[LIMIT] "One LLM, 16 questions, two LLM raters" scoping — `docs/dissemination/v0.1.2/preprint_arxiv_cs_cl.md` §4.
[LIMIT] Cross-LLM generation and human raters out of v0.1.2 scope, both scoped into v0.2 — `tests/phase2/reconciliation_holdout_v0.1.2.md` §"Open follow-ups"; AOV-90 description.
[FACT] ARC Evals → METR rebrand (basis for deferral of fourth contact) — [provisional: external public-knowledge claim, citation is METR's own public-facing material; verify before posting if any reader challenges the deferral choice].

---

## Aoven-marker face-validity audit on the three emails

- All three subject lines are **declarative-modest**. None says "breakthrough," "first ever," or "solves." All three name the specific artefact (Aoven v0.1.2) and the load-bearing methodological line (stripped prose, self-labelling, confirmatory pass).
- Every email contains the scoping line "1 model, 16 questions, 2 LLM raters" or its near-equivalent. Overclaiming guardrail honoured.
- Every email contains a concrete ask scoped to that organisation's competence: METR for methodological critique, Apollo for adversarial-stress critique, Anthropic alignment for cross-LLM stress-test viability. None of the three asks is "endorsement"; each is a request for critique or a domain-specific pointer.
- The Apollo email explicitly names the adversarial direction the v0.1.2 design did NOT stress (markers as cheap evasion). This is the kind of overclaiming-guardrail honesty the AOV-91 directive demands; it is also the most likely real critique an evaluator will land on, so naming it first is good-faith.
- The Anthropic email explicitly scopes the result as "claude-opus-4-7 can do this," not "Claude family can do this." This is consistent with the cross-LLM-gap limitation in `preprint_arxiv_cs_cl.md` §4 and avoids implying Anthropic-wide validation.
- No email contains an Aoven marker (FACT, HYP, etc.) inline in the email body. This is intentional: the cold email must be readable to a non-Aoven recipient; the markers are a face-validity audit applied to the meta-text in this draft, not a constraint on the recipient-facing prose. If a recipient asks "what do those FACT/HYP labels look like in practice," the repo and preprint are the right venue.

---

## Posting hygiene for Tommy

- Send the three emails on **separate days** (suggested: METR Mon, Apollo Wed, Anthropic Fri) to avoid the appearance of mass-blast outreach. Each org should see the email as a directed, scoped contact, not a list-blast.
- Replace `[provisional — to be added once verified]` with the verified DOI URL in all three emails before sending.
- Replace every `[provisional]` contact-detail flag with a verified address. If verification fails for any of the three, **send via the public contact form for that org** rather than guess. Do NOT send to a personal address Tommy is not certain is current.
- If a reply lands, the response must hold the same NOSRC discipline as the cold email: every empirical claim in any follow-up email cites either an issue ID or a canonical file path. If you cannot cite, flag as `[provisional]` or do not send.
- If no org replies within 14 days, do **not** re-send. Cold-outreach hygiene is one shot; a follow-up at 14+ days that adds no new information is spam. Wait until v0.2 has a published result, then send a new email referencing the new result, not the old one.
- **Do not** publicly announce that any of these orgs has been contacted until they reply. The "we contacted X" claim is itself a claim that is currently NOSRC and that any of the three could legitimately ask Aoven to retract. Privacy is the right default until reciprocated.
- Anthropic email specifically: do not tag `Anthropic` on LinkedIn until this email has been **answered or explicitly acknowledged**. The LinkedIn-tagging hygiene line in `linkedin_post.md` is the canonical rule on this; this file is the upstream gate.
- If the deferred fourth contact (ARC Evals legacy channel, if Tommy has it) is to be activated, it goes in the same per-org one-paragraph + one-email format as the three above and gets its own NOSRC audit pass before sending.

---

*Drafted by CanonicalScribe (`e19c696f`) under AOV-91. Pending Logician NOSRC audit + CEO sign-off before Tommy sends. Contact-detail `[provisional]` flags must be resolved by Tommy at send-time; the per-org rationale and email body do not require re-audit if no [FACT]-tier claim is added or modified.*
