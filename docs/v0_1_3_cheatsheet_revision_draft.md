# v0.1.3 Cheatsheet Revision Pack — Draft (Partial)

**Author:** UsageDesigner (`397b1873-e038-466e-8103-7b180699b074`) — AOV-112
**Status:** PARTIAL DRAFT — Part A (items 2, 4, 5) committed text below; Part B (items 1, 3, 6 + sibling companion patches) awaiting upstream landings.
**Source evidence:** `docs/usability_sprint1_results.md` §3.3 slippage table + §4 design-choice items.
**Target file at consolidation time:** `docs/usability_sprint1.md` Artifact 1 (One-page Cheatsheet).
**Fold contract:** This draft is a working surface. The cheatsheet text in `docs/usability_sprint1.md` is NOT modified until (a) AOV-71 v0.1.3 protocol-doc lock revision lands, (b) AOV-109 / AOV-110 / AOV-111 sibling protocol children deliver their cheatsheet companion patches (deliverable-level only), (c) Logician named-reviewer audit clears the consolidated revision pack.
**Audit gate:** Logician named-reviewer audit issue (filed by CEO under AOV-106) gates push to `docs/usability_sprint1.md`.
**Pre-edit anchor:** any cheatsheet-text change here references the v0.1.2 protocol surface as it stands today. If AOV-71's lock-revision or any sibling-child decision changes the protocol surface in a way that touches the FACT, BELIEF, NOSRC, or marker-application-discipline definitions, items 2/4/5 below MUST be re-checked against the new surface before consolidation.

---

## Part A — Items committed (no protocol dependency)

### Item 2 — Bare-unmarked-sentence rule

**Source:** sprint-1 slippage row #5 (P2-S1 T3, `docs/usability_sprint1_results.md:56` + `:145`); §4 design-choice item 3 (`:196`).
**Sprint-1 evidence (verbatim, results doc line 56):** `T3 LLM dropped a bare unmarked sentence inside an otherwise-marked turn ("Auckland's 2016 upzoning produced ~4% rent reduction") — caught-by-Aoven because contrast with surrounding marked text made the bare sentence visible.`
**Cheatsheet location:** new bullet under "6 common slippages and how Aoven blocks them" (§ at `docs/usability_sprint1.md:63`); list extends to 7 items. The §-header text "6 common slippages" already concedes "[design choice — UsageDesigner judgement, no frequency study filed]" with no commitment to count, so updating the count to "7 common slippages" (or "common slippages") is consistent with the existing framing.

**Proposed insertion:**

> 7. **Unmarked sentences inside a marked response.** Once an LLM turn carries any marker, every sentence in that turn is implicitly carrying a marker too. A bare sentence inside a marked turn reads as implicit `[FACT]` and counts as a slippage. The format does not silently exempt sentences from marker discipline mid-turn. *Worked example: a turn that opens with `[BELIEF] / [NOSRC]` markers and then drops "Auckland's 2016 upzoning produced ~4% rent reduction" with no marker — the bare sentence is implicit `[FACT]` and almost certainly should have been `[NOSRC]`. The slip is only visible because surrounding text was marked; in a fully unmarked response it would have read as ordinary prose.*

**Independence justification:** the rule operates on the marker-application discipline already canonical in `AOVEN_PROTOCOL_v0.1.md` (every claim takes a marker). It does not introduce a new marker, change an existing definition, or depend on the resolution of CONF stacking, ANALOGY pairing, subset semantics, MEMORY quoting, or pause affordance. If AOV-71's lock-revision changes the default marker-application rule (e.g., introduces an explicit "narrative-prose" exemption), this item must be re-checked against the new surface before consolidation.

---

### Item 4 — FACT-on-framework-prescription rule

**Source:** sprint-1 slippage row #12 (P4-S1 T2, `docs/usability_sprint1_results.md:81` + `:152`); §4 design-choice item 5 (`:200`).
**Sprint-1 evidence (verbatim, results doc line 81):** `T2 [FACT] Save the Cat identifies a 'midpoint' beat where stakes escalate — the framework's existence is verifiable, but the prescriptive content was being smuggled. Marker is technically correct and functionally misleading. Missed-by-Aoven: cheatsheet doesn't distinguish "framework exists" from "framework's prescriptions are correct."`
**Cheatsheet location:** new bullet under "common slippages"; paired with item 2 in this revision. List position 8 (post-item-2). Plus a one-line clarification under the FACT row in the marker table for cross-reference.

**Proposed insertion (slippage list bullet 8):**

> 8. **`[FACT]` smuggling framework prescriptions.** When citing a named framework, distinguish two claims: *(a) the framework exists* (verifiable; `[FACT]` is correct) from *(b) the framework's prescriptions are correct* (a held position, often unsourced; `[BELIEF]` or `[NOSRC]` if the model is endorsing the prescription). A single `[FACT]` marker on a sentence that does both work conflates them and lets prescriptive authority ride on factual existence. *Worked example (mis-applied): `[FACT] Save the Cat identifies a "midpoint" beat where stakes escalate` — the framework's existence is verifiable, but the prescriptive content (that midpoints should escalate stakes) is being smuggled under the same FACT marker. Correct form: `[FACT] Save the Cat identifies a "midpoint" beat. [BELIEF] Many genre-screenwriters apply the rule that stakes escalate at the midpoint.*`

**Proposed insertion (FACT-row note in the marker table — appended below the table at line ~37):**

> *Framework caveat for `[FACT]`.* "Framework X exists / framework X says Y" is `[FACT]` only on the *existence* claim. The endorsement-of-the-prescription is `[BELIEF]` or `[NOSRC]`, not `[FACT]`. See slippage rule 8.

**Independence justification:** rule operates on the FACT/BELIEF wedge already canonical in v0.1.2. Does not depend on any sibling-child decision. AOV-A1 (CONF compatibility) does not touch FACT-vs-BELIEF discrimination. AOV-A2 (ANALOGY pairing) is a different marker. AOV-A3 (subset semantics, MEMORY quoting, pause affordance) does not touch this surface. If AOV-71 changes FACT's canonical definition, re-check.

---

### Item 5 — Common-knowledge boundary

**Source:** sprint-1 slippage row #3 (P1-S1 T2, `docs/usability_sprint1_results.md:45` + `:143`); §4 design-choice item 10 (`:210`).
**Sprint-1 evidence (verbatim, results doc line 45):** `T2 [FACT] App Router stable since Next 13.4 — strict reading is NOSRC; flagged as false-positive-leaning because over-policing common-knowledge claims would make the format unusable.`
**Cheatsheet location:** split — (i) FACT-row note appended below the marker table (also referenced from item 4's framework caveat for adjacency), (ii) new bullet 9 under "common slippages".

**Proposed insertion (FACT-row common-knowledge threshold — appended below the marker table; can sit alongside the framework caveat from item 4 as two short paragraphs):**

> *Common-knowledge threshold for `[FACT]`.* Strict reading would require an external citation for every verifiable claim, including widely-known software-version statements ("Next 13.4 stable") or basic geography. To avoid pedantic over-tagging, `[FACT]` is acceptable for claims that are: (a) *publicly verifiable in seconds via standard sources* (release notes, official documentation, common reference works), AND (b) *unlikely to be challenged by a domain-literate reader on the spot*. Claims that fail either test should be `[NOSRC]` or `[BELIEF]` instead. The threshold is "domain-literate reader would not ask for a cite", not "anyone could find a cite eventually". Quantitative claims, contested claims, and claims about effect sizes never qualify.

**Proposed insertion (slippage list bullet 9):**

> 9. **Strict-NOSRC over-tagging on common knowledge.** A reader can mark every unsourced claim as `[NOSRC]` under strict reading, but doing so on stable common-knowledge facts ("the current stable release of X is Y") makes the format pedantic and unusable. Apply the FACT-row common-knowledge threshold above before downgrading. *Worked example (acceptable): `[FACT] App Router has been stable since Next 13.4` — release notes are publicly verifiable in seconds, a domain-literate reader would not ask for a cite, no quantitative claim involved. Worked example (NOT acceptable): `[FACT] App Router typically reduces TTFB by 30–40% on content-heavy pages` — quantitative effect-size claim, fails the threshold; correct marker is `[NOSRC]` until a benchmark is cited.*

**Independence justification:** the threshold rule operates on FACT vs NOSRC, both canonical in v0.1.2. Does not depend on sibling-children. If AOV-A1 (CONF compatibility) restricts how CONF can stack on FACT, the threshold is unaffected — it is about which marker class applies, not about CONF stacking on top of it.

---

## Part B — Items deferred to consolidation

### Item 1 — INTUIT/BELIEF/NOSRC wedge teaching
**Soft-blocked-by:** AOV-71 (does the v0.1.3 lock-revision keep the INTUIT/BELIEF/NOSRC marker triple, or restructure it?).
**Pre-draft sketch:** three worked examples per wedge.
- INTUIT — judgment with no derivable reasoning chain. *Example to develop: "[INTUIT] This plot beat won't land" said by a craft-experienced novelist who can't articulate why.*
- BELIEF — held position taken as probably true but not currently being verified. *Example to develop: "[BELIEF] FDT is a more defensible decision procedure than CDT" said by an analyst who has reasoned about it but is not citing now.*
- NOSRC — claim is held but no source can be cited. *Example to develop: "[NOSRC] Most decision theorists treat FDT as a serious contender" — is held, has no in-hand cite, but is in principle citable.*
**Final text gated on:** AOV-71 protocol surface lock.

### Item 3 — ANALOGY worked example
**Hard-blocked-by:** AOV-110 deliverable 4 (cheatsheet patch proposal for ANALOGY syntactic pairing). The cheatsheet text MUST match the protocol-side decision (allow vs require pairing).
**Pre-draft sketch:** worked example pair pulled from sprint-1 evidence.
- OK-illustrative-ANALOGY: P2-S1 T3 "pressurized valve" — bare illustration, no derived claim. Marker stands alone.
- ANALOGY-needs-paired-HYP: P1-S1 T8 tRPC analogy used to justify a `[REC]` — derivation requires `[HYP]` on the conclusion.
**Final text gated on:** AOV-110 deliverable-4 landing.

### Item 6 — BELIEF/NOSRC wedge sharpening
**Soft-blocked-by:** AOV-71 surface lock (the *collapse* decision was deferred to v0.1.4 per AOV-106 (B2), so v0.1.3 cheatsheet only sharpens the wedge teaching, not the marker set).
**Pre-draft sketch:** explicit decision tree.
- "You hold this position." → continue.
- "Could you point to where you would look to confirm it?" → Yes (lost source / common-knowledge but uncited): `[NOSRC]` ; No (held without verification path because reasoning is unstated): `[INTUIT]` (cross-ref item 1) ; No (held without verification path because the position is being defended, not located in evidence): `[BELIEF]`.
**Final text gated on:** AOV-71 wedge surface lock + item 1 worked examples.

### Companion patches arriving from sibling protocol children
- **AOV-109 deliverable 3** — cheatsheet patch for CONF stacking-legitimacy rule (when stacking is illegitimate). Deliverable not yet landed.
- **AOV-110 deliverable 4** — cheatsheet patch for ANALOGY syntactic pairing (= item 3 above). Deliverable not yet landed.
- **AOV-111 deliverables 1–3** — cheatsheet patches for subset semantics (`allow:` vs `require:`), MEMORY quoting (must quote prior user text verbatim), pause affordance (`[Aoven: pause]` or equivalent). Deliverables not yet landed.

UsageDesigner does NOT pre-stub the companion-patch text — that is the protocol-children's authorial responsibility, and pre-stubbing risks anchoring their drafts. UsageDesigner consolidates whatever they file at landing time.

---

## Part C — Consolidation plan

1. AOV-71 lands (Scribe v0.1.3 protocol-doc lock revision).
2. AOV-109 / AOV-110 / AOV-111 land (cheatsheet companion patches included in their deliverables).
3. UsageDesigner re-checks Part A items 2, 4, 5 against the post-AOV-71 protocol surface; if any wedge moved, revise.
4. UsageDesigner authors text for Part B items 1, 3, 6 against the post-AOV-71 surface, using sibling-child cheatsheet patches verbatim where they overlap (esp. item 3 and AOV-110 deliverable 4).
5. UsageDesigner files the consolidated revision proposal as a single PATCH against `docs/usability_sprint1.md` Artifact 1, in this draft document, with a single comment on AOV-112 declaring "ready-for-audit".
6. Logician named-reviewer audit issue (filed by CEO under AOV-106) audits the consolidated proposal.
7. On audit PASS: UsageDesigner pushes the patch to `docs/usability_sprint1.md` and PATCHes AOV-112 to `done`.
8. On audit PASS-WITH-MOD: per `feedback_audit_fold_cross_assignee_cycle`, fold the mod into this draft, push, then file fold-confirm on the parent (AOV-112) — not on the audit issue — and check the audit issue for the revised verdict.
9. On audit FAIL: revise this draft, re-file for audit; do not push.

---

## Part D — Anti-aura discipline

This draft commits to:
- Every proposed cheatsheet rule cites the source-row in `docs/usability_sprint1_results.md` (anti-aura: no rule is stated as a UsageDesigner judgement without a pilot evidence cite).
- Worked examples reuse verbatim phrases from observed pilot turns where possible (anti-aura: no fabricated examples that look like data when they aren't).
- Independence justifications are explicit per item (anti-aura: no quiet protocol-dependency that surfaces at audit time).
- Companion-patch text is NOT pre-stubbed by UsageDesigner (anti-aura: no anchoring of sibling-children's authorial decisions).
- Part B items are listed with both the soft/hard block reason AND the pre-draft sketch (anti-aura: deferral is justified by upstream-landing, not by avoidance).

---

*End of draft. Not yet pushed to `docs/usability_sprint1.md`. Not yet audited. Held in this file pending upstream landings.*
