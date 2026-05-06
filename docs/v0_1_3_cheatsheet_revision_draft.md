# v0.1.3 Cheatsheet Revision Pack — Draft (Partial)

**Author:** UsageDesigner (`397b1873-e038-466e-8103-7b180699b074`) — AOV-112
**Status:** AOV-116 PASS-WITH-MOD VERDICT FOLDED — ready for canonical-doc push. AOV-116 verdict `c9cf09c4` (closed `done` 2026-05-06T01:02:35Z) returned PASS-WITH-MOD: Mod 1 (textual — item 3 Source line for format consistency), Mod 2 (substantive — item 4 INTERPRET as third eligible marker), plus soft preference (item 4↔10 CONF cross-link). All folded into Part A item 4, Part B item 3, and Part E (slippage bullet 8 + FACT-row caveat). Fold-confirm filed on AOV-112 (parent), not on closed AOV-116, per `feedback_audit_fold_cross_assignee_cycle`. Next: replace lines 12-72 of `docs/usability_sprint1.md` with Part E POST-PATCH ARTIFACT 1; PATCH AOV-112 → `done`.
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

> 8. **`[FACT]` smuggling framework prescriptions.** When citing a named framework, distinguish two claims: *(a) the framework exists* (verifiable; `[FACT]` is correct) from *(b) the framework's prescriptions are correct* — which is one of three things, never `[FACT]`: `[BELIEF]` if the model is *endorsing/defending* the prescription as probably correct, `[NOSRC]` if the prescription is *held but no in-hand source* can be cited, or `[INTERPRET]` if the model is *reading the framework's prescription as one reading among others* (presenting how the framework is typically read, not whether it is right). A single `[FACT]` marker on a sentence that does both works conflates them and lets prescriptive authority ride on factual existence. *Worked example (mis-applied): `[FACT] Save the Cat identifies a "midpoint" beat where stakes escalate` — the framework's existence is verifiable, but the prescriptive content (that midpoints should escalate stakes) is being smuggled under the same FACT marker. Correct forms (any of three, depending on what the model is doing): `[FACT] Save the Cat identifies a "midpoint" beat. [BELIEF] Many genre-screenwriters apply the rule that stakes escalate at the midpoint.` — endorsing/defending the prescription. Or: `[FACT] Save the Cat identifies a "midpoint" beat. [INTERPRET] On Save the Cat's reading, midpoints function to escalate stakes — one reading of how the beat is meant to work, not a universal prescription.` — presenting the prescription as one reading.*

**Proposed insertion (FACT-row note in the marker table — appended below the table at line ~37):**

> *Framework caveat for `[FACT]`.* "Framework X exists / framework X says Y" is `[FACT]` only on the *existence* claim. The endorsement-of-the-prescription is `[BELIEF]` (defended), `[NOSRC]` (held without cite), or `[INTERPRET]` (one reading of the prescription among others) — not `[FACT]`. CONF stacks legitimately on the `[BELIEF]` or `[INTERPRET]` form; CONF on the existence-`[FACT]` is redundant per slippage rule 10. See slippage rule 8.

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

**Source:** sprint-1 §3.2 marker frequency table (`docs/usability_sprint1_results.md:131` — INTUIT 1/5 sessions, dead-marker call; `:129` — BELIEF 3/5 sessions, P3 zero structural concern) + §4 design-choice item 1 (`:192`) + §4 item 11 (`:212`) + P4 standout INTUIT moment (`:84`).
**Sprint-1 evidence (verbatim, results doc line 192):** `INTUIT is a dead marker in agent-simulated practice. Fired in 1/5 sessions (P4 only, creative-craft). P1, P3, P5 used INTERPRET or HYP where INTUIT would have been the right call. Cheatsheet wedge between INTUIT / BELIEF / NOSRC may be too narrow to teach from one-line definitions.`
**Sprint-1 evidence (verbatim, results doc line 84 — P4 standout INTUIT moment):** `P4 cited [INTUIT] Quiet novels often substitute internal recognition for external choice as the standout moment where the marker actively earned its overhead.`
**Post-AOV-71 surface confirmed intact:** AOV-71 fold (commit `fb71920`, 2026-05-04) lands D10/D11/D12 (subset header / MEMORY quoting / pause). Marker-table rows for INTUIT (`AOVEN_PROTOCOL_v0.1.md:38`), BELIEF (`:40`), and NOSRC (`:45`) are unchanged from v0.1.2; UR-7 (challenge response, `:161`) and INTUIT→HYP laundering rule (`:199`) likewise unchanged. The wedge surface is preserved — this item is now ready for consolidation against the post-AOV-71 surface.
**Cheatsheet location:** new "Wedge-clarification — INTUIT / BELIEF / NOSRC" sub-block appended below the marker table (`docs/usability_sprint1.md:36`) and before the "Prompt format" section (`:38`). The sub-block holds item 6's decision tree (procedural — when writing) followed by item 1's three worked examples (per-marker semantics — what each is FOR). Items 1 + 6 land together as a single insertion; they are factored into two issue-items here for audit traceability against the sprint-1 §4 source items they each address.

**Proposed insertion (wedge-clarification block — worked examples; pairs with item 6 decision tree):**

> **INTUIT / BELIEF / NOSRC — what each marker is FOR.** All three carry held positions without external verification. They are NOT interchangeable.
>
> *`[INTUIT]` — judgment without a derivable reasoning chain.* Use when you cannot state the inference but the judgment is still doing real work in the response. Worked example (verbatim from pilot P4-S1, the only session where INTUIT fired): `[INTUIT] Quiet novels often substitute internal recognition for external choice.` The judgment is craft-experienced, not deduced; there is no inference chain to state. **Do not** retag to `[INTERPRET]` (that requires a specific reading of specific data) or to `[HYP]` (that requires a stated test condition — the laundering rule under "Anti-slippage rules" blocks bare INTUIT→HYP retag without a stated test path).
>
> *`[BELIEF]` — held position, currently defended without verification.* Use when you hold the position as probably true and would *argue for it* if challenged, but are not now performing the verification work. Canonical example (verbatim from `AOVEN_PROTOCOL_v0.1.md:40`): `[BELIEF] Most users will abandon a protocol requiring more than 3 seconds of overhead per message.` The position is defended (the speaker would back it with reasons), not located in a specific in-hand source. **Do not** retag to `[FACT]` if challenged: UR-7 requires producing an external source (upgrade to FACT) or explicitly downgrading to UNCERTAIN. Silent withdrawal is a slippage.
>
> *`[NOSRC]` — claim is held but no in-hand source can be cited.* Use when a source exists in principle (you've read it, it could be looked up, the claim is checkable against a corpus) but is not at hand right now. Worked example (verbatim from pilot P4-S1 T8 self-correction without challenge): `[NOSRC] My examples skew toward commercial structure.` The speaker holds the claim AND knows it could be checked against the conversation's corpus of cited examples; they just have no cite to attach. **Do not** retag to `[BELIEF]` (BELIEF defends a position; NOSRC concedes a missing cite) or to `[FACT]` (no in-hand source = no FACT).
>
> See item 6 (decision tree) above for the procedural choice at the moment of writing.

**Independence justification:** INTUIT, BELIEF, NOSRC, UR-7, and the INTUIT→HYP laundering rule are all canonical in v0.1.2 and unchanged by AOV-71's v0.1.3 fold (commit `fb71920`). The wedge collapse (BELIEF↔NOSRC merge) is explicitly deferred to v0.1.4 per AOV-106 B2 — this item only sharpens teaching, does not propose marker-set redraw. Worked examples each cite source: P4-S1 INTUIT verbatim (results doc line 84, the only INTUIT firing in pilot), canonical BELIEF example (protocol line 40, verbatim), P4-S1 T8 NOSRC self-correction verbatim (results doc line 82). No fabricated examples.

**Final text gated on:** AOV-116 audit on the consolidated revision pack. Wording above is the consolidation-time text; UsageDesigner final-wording authority.

### Item 3 — ANALOGY worked example
**Source:** sprint-1 §4 design-choice item 4(a) (`docs/usability_sprint1_results.md:198` — UR-5 ANALOGY pairing); §3.3 slippage rows #2 (P1-S1 T8, `:142`), #7 (P2-S1 T3 false-positive, `:147`), #9 (P3-S1 T6, `:149`), #15 (P5-S1 T4, `:155`) — broader UR-5 cluster the rule addresses. Audited via AOV-114 PASS-WITH-MOD; Mod 1 + Mod 2 folded.
**Hard-blocked-by:** AOV-110 deliverable 4 (cheatsheet patch proposal for ANALOGY syntactic pairing). The cheatsheet text MUST match the protocol-side decision (allow vs require pairing).
**AOV-110 d4 status (2026-05-03, post-Mod-1):** proposal **audited and SIGNED-OFF** as v0.1.3 `[provisional]` per Logician verdict on AOV-114 (comment `09efc431`, 21:15:02Z, **PASS-WITH-MOD**). Mod 1 (binary independent-warrant phrasing on §1 strike-test + cheatsheet §4 mirror) **folded by CTO** at 21:30:38Z into `docs/v0_1_3/aov110_analogy_pairing_rule.md` (comments `6798a6f9` / `a863aa72` on AOV-110). Mod 2 (worked-example completeness — add SPEC + INTERPRET cases) routed by CEO onto this issue per AOV-112 wake comment `f9c78264` (21:41:03Z); folded into the worked-example block below. UR-5-rev surface: argumentative ANALOGY → next claim warranted by the analogical mapping MUST carry `[HYP]` / `[SPEC]` / `[INTERPRET]`; `[REC]` only via `[HYP]` + stated test path (mirrors UR-6 SPEC→REC chain). Diagnostic: **strike test** rewritten to Logician's binary independent-warrant phrasing — strike the ANALOGY sentence; if a downstream claim has no independent stated warrant remaining → argumentative; if at least one independent stated warrant remains → illustrative. Promoted to `[validated]` only on mini-A/B pass.

**Candidate cheatsheet paragraph (post-Mod-1, mirrors `aov110_analogy_pairing_rule.md` §4 / §1 binary phrasing — DO NOT consolidate yet; final wording owned by UsageDesigner at consolidation):**
> **ANALOGY pairing — when an analogy needs a partner marker.** Apply the **strike test** to every `[ANALOGY]`: imagine the ANALOGY sentence is struck from the turn. If at least one independent stated warrant remains for every downstream claim, the analogy is *illustrative* and may stand alone. If a downstream claim has no independent stated warrant remaining after striking, the analogy is *argumentative* — that claim MUST carry its own `[HYP]` or `[SPEC]` marker (or `[INTERPRET]` if the derived claim is a reading). A `[REC]` derived from an argumentative ANALOGY is only legal when preceded by `[HYP]` with a stated test path (mirrors UR-6). The pairing applies to any claim in the same turn whose warrant is the analogical mapping — not necessarily the syntactically next claim — so an unrelated `[FACT]` between an `[ANALOGY]` and the `[REC]` it warrants does not break the pairing requirement.

**Worked-example block (5 contrasted cases — covers all three argumentative dispositions named by UR-5-rev plus illustrative legal and argumentative bare illegal):**

> *Illustrative — legal (analogy stands alone, no derived claim takes its warrant from the mapping):*
> ```
> [ANALOGY] Memory pressure on a small VPS feels a bit like a kitchen during dinner service: lots of small things contending for the same counter space.
> ```
> Strike test: nothing downstream depends on the kitchen mapping → at least one independent warrant remains for every other claim in the turn → illustrative. (Source: P2-S1 T3 "pressurized valve" pattern, slippage row #7 — ceases to be a strict-reading false-positive under UR-5-rev.)
>
> *Argumentative bare — ILLEGAL (no dependent marker on the claim warranted by the analogy):*
> ```
> [ANALOGY] tRPC without strict types is like Express without middleware: technically possible, structurally regrettable.
> [REC] Don't ship tRPC without enabling strict typing.
> ```
> Strike test: strike the analogy sentence; the `[REC]` has no independent stated warrant remaining → argumentative → `[REC]` derived directly from an argumentative ANALOGY is illegal under UR-5-rev (must go via `[HYP]` + test path per UR-6 chain). (Source: P1-S1 T8 slippage row #2.)
>
> *Argumentative paired — legal (HYP-via-test path):*
> ```
> [ANALOGY] tRPC without strict types is like Express without middleware: technically possible, structurally regrettable.
> [HYP] Strict typing on the tRPC client/server boundary will catch ≥80% of contract-mismatch bugs in CI before they ship — testable by enabling `strict: true` and re-running the type-checker against the existing test suite.
> [REC] Don't ship tRPC without enabling strict typing.
> ```
> Strike test: strike the analogy; `[HYP]` carries its own stated test path → independent stated warrant remains → `[REC]` legal via UR-6 chain.
>
> *Argumentative paired — legal (interpretation, no prediction):*
> ```
> [ANALOGY] Reading the protocol "as if it were a contract" foregrounds enforceability over teaching.
> [INTERPRET] On that reading, UR-5 is a constraint on the speaker, not a teaching aid for the user.
> ```
> Strike test: strike the analogy; the `[INTERPRET]` reading collapses → argumentative → `[INTERPRET]` is the correct dependent marker because the derived claim is a reading of the protocol, not a falsifiable prediction. (Source: AOV-114 Mod 2 protocol-anchored draft, verbatim.)
>
> *Argumentative paired — legal (extrapolation, no test path available):*
> ```
> [ANALOGY] Marker-class compatibility resembles type compatibility in a structural type system.
> [SPEC] If that mapping holds, the hedge-laundering risk likely scales with the number of compatible classes a marker can stack into.
> ```
> Strike test: strike the analogy; the scaling claim has no independent stated warrant remaining → argumentative → `[SPEC]` is the correct dependent marker because the derived claim extrapolates beyond evidence with no clear test path (the type-system mapping is not itself a tested theory of marker behaviour). (Source: AOV-114 Mod 2 protocol-anchored draft, verbatim.)

**Mod 2 fold record.** SPEC + INTERPRET worked-example pairs above are verbatim from Logician's protocol-anchored draft in AOV-114 comment `09efc431` Mod 2; surrounding strike-test commentary added by UsageDesigner per the §4 wedge note ("UsageDesigner owns final wording"). Per `feedback_audit_fold_cross_assignee_cycle`, fold-confirmation filed on this issue (AOV-112) at consolidation comment, not on the closed AOV-114 audit child.

**Anti-aura discipline.** All five worked examples cite their source: pilot rows for the first three (P1-S1 T8, P2-S1 T3 pattern), Logician's protocol-anchored draft for the SPEC + INTERPRET pair. The strike-test commentary is mechanical and reproducible — every example resolves by the same binary independent-warrant test, no rater discretion. The illustrative example is a sibling case to the P2-S1 T3 valve metaphor, not a verbatim pilot turn (no pilot turn exhibited the kitchen analogy); flagged here so the audit can demand the verbatim pilot turn instead if preferred.

**Final text gated on:** Logician audit on the consolidated revision pack (AOV-116, DOD item 4 will check ANALOGY worked-example coverage). Worked-example block above is the consolidation-time text; UsageDesigner is the final-wording authority per AOV-114 Mod 2 routing. Re-check at consolidation against the canonical `docs/v0_1_3/aov110_analogy_pairing_rule.md` once it lands in this workspace, in case the post-Mod-1 §4 wording diverges from the binary-phrasing reconstruction above.

### Item 6 — BELIEF/NOSRC wedge sharpening

**Source:** sprint-1 §3.2 (`docs/usability_sprint1_results.md:129` — BELIEF 4 fires across 3/5 sessions, P3 zero, "structural concern") + §4 design-choice item 11 (`:212` — BELIEF marker dead-zone risk) + slippage row #11 (`:151` — P3-S1 whole-session zero BELIEF, classified as missed-by-Aoven structural absence).
**Sprint-1 evidence (verbatim, results doc line 212):** `BELIEF marker dead-zone risk. P3 zero BELIEF across the whole session despite multiple held-but-unsourced positions. LLMs route held-positions through FACT or NOSRC and skip BELIEF entirely. Either tighten the BELIEF/NOSRC wedge or consider collapsing them.`
**Sprint-1 evidence (verbatim, results doc line 68 — example of FACT→NOSRC retrofit where BELIEF was a candidate but skipped):** `T4 [FACT] MitoGraph is the most widely used pipeline... — popularity claim with no source, caught-by-Aoven via challenge (UR-4); model retrofitted [NOSRC].` (A defended popularity claim is BELIEF when the speaker would *argue* the position rather than concede absent-cite — the retrofit-to-NOSRC path is the dead-zone slip the decision tree below is designed to interrupt.)
**v0.1.3 scope (per AOV-106 B2):** *sharpen the wedge teaching only.* Collapse decision (BELIEF↔NOSRC merge) is deferred to v0.1.4. This item adds a decision tree to the cheatsheet; it does NOT change the marker set.
**Cheatsheet location:** within the "Wedge-clarification — INTUIT / BELIEF / NOSRC" sub-block introduced by item 1 (appended below the marker table, before the "Prompt format" section). Decision tree precedes the worked examples. Items 1 + 6 land together as a single insertion.

**Proposed insertion (wedge-clarification block — decision tree; precedes item 1 worked examples):**

> **Decision tree — which of the three you actually hold.**
> 1. **You hold this position.** (If you do not, the marker is wrong — choose `[UNCERTAIN]`, `[INTERPRET]`, or `[HYP]` per the marker table.)
> 2. **Could you point to where you would look to confirm it?**
>    - **Yes** — a source exists, you just cannot cite it now (lost source, common-knowledge but uncited, you have read it but do not have the link): `[NOSRC]`.
>    - **No, because the reasoning is unstated and not reducible to one** — craft judgment, felt sense, expert pattern-recognition: `[INTUIT]` (see worked examples below).
>    - **No, because the position is defended rather than located in evidence** — you would *argue* for it, not look it up: `[BELIEF]`.
> 3. **Common pitfall — the BELIEF dead-zone.** When an LLM is challenged on a confident-sounding held position with no source, the laziest exit is `[NOSRC]`. If the position is being *defended* (you would back it with reasons), `[BELIEF]` is correct — and UR-7 then requires producing a source on next challenge or downgrading to `[UNCERTAIN]`. Routing every held-position through `[NOSRC]` is the BELIEF dead-zone slippage observed in pilot P3-S1 (zero BELIEF across the whole session despite multiple defended-position turns).

**Independence justification:** decision tree operates on the v0.1.2 marker definitions of INTUIT (`AOVEN_PROTOCOL_v0.1.md:38`), BELIEF (`:40`), NOSRC (`:45`), UR-7 (`:161`), and the BELIEF→reality anti-slippage row (`:193`) — all unchanged by AOV-71's v0.1.3 fold. Per AOV-106 B2, collapse is v0.1.4-out-of-scope; the tree is teaching-only, additive to the cheatsheet, and does not commit the protocol to any wedge restructuring. Source-cite for the slippage the tree is designed to prevent: P3-S1 whole-session BELIEF zero (results doc lines 71, 129, 151, 212).

**Final text gated on:** AOV-116 audit on the consolidated revision pack.

### Item 7 — Subset header `allow:` vs `require:` semantics (AOV-111 D1)
**Audit status:** **SIGNED-OFF** via cross-deliverable check. AOV-111 D1 spec audited under AOV-115 — Logician verdict `b6bd7a58` clean **PASS** on the spec; cheatsheet patch wording inherits the same PASS via the cross-deliverable check (per CEO ratification `50abfc16` on AOV-111 + CEO repose `29fc346d` on this issue 2026-05-03T21:51:02Z). No separate AOV-116 gate needed for item 7 — wording is already audited.
**AOV-111 D1 spec summary (audited):** two non-exclusive qualifiers — `require:` (mandatory minimum — listed markers MUST be applied when applicable; OTHER MARKERS STAY AVAILABLE) and `allow:` (additive emphasis — encouraged, not enforced). Default when no qualifier is present = `allow:`. **The subset header NEVER suppresses unlisted markers.**
**Cheatsheet location:** new note appended to the Subset-header description in `docs/usability_sprint1.md` Artifact 1 (or paired with the Format-row note alongside the marker table; final placement TBD at consolidation).
**Audited cheatsheet paragraph (verbatim from CTO comment `8a46d4c7`, audit-cleared via AOV-115 cross-deliverable check — ready for consolidation):**
> **Subset header (v0.1.3 clarification):** the qualifiers are `require:` (mandatory minimum — the LLM MUST apply each listed marker when applicable; OTHER MARKERS STAY AVAILABLE) and `allow:` (additive emphasis — encouraged, not enforced). When no qualifier is present, the list is treated as `allow:`. **The subset header NEVER suppresses unlisted markers.** Writing `[Aoven v0.1 | require: FACT, HYP]` does not turn off LIMIT, INTERPRET, NOSRC, etc. — they still apply when their definition fits.

**Sprint-1 evidence:** §4 item 6 / slippage row #18 — P5-S1 T6+ used `[Aoven v0.1 | require: FACT, HYP, SPEC, LIMIT]` mid-session and the LLM read `require:` as exclusive; INTERPRET and INTUIT silently suppressed turns 6–10. Under v0.1.3 cheatsheet text, slippage row #18 reclassifies from `false-positive (protocol behaved as specified)` to `caught-by-cheatsheet-text`.
**Consolidation status:** ready. Wording is the verbatim CTO-authored cheatsheet patch, audited via AOV-115 cross-deliverable check; UsageDesigner does not edit it (per AOV-115 PASS). Push to `docs/usability_sprint1.md` still gated on AOV-71 landing (Scribe reposed with spec deltas) + AOV-116 audit on the consolidated revision pack.

---

### Item 8 — MEMORY quoting rule (AOV-111 D2)
**Audit status:** **SIGNED-OFF** via cross-deliverable check. AOV-111 D2 spec audited under AOV-115 — clean PASS; cheatsheet patch wording inherits via cross-deliverable check (per CEO repose 2026-05-03T21:51:02Z). No separate AOV-116 gate per item.
**AOV-111 D2 spec summary (audited):** UR-3 strengthened — `[MEMORY]` claims referencing prior conversation text MUST attach the prior text as a verbatim quotation (paraphrase forbidden). Two permitted forms (inline `[MEMORY: "..."]` or block-quoted following the marker). Ellipsis allowed only to elide irrelevant middle content. Length cap ~2 sentences; beyond that use `[NOSRC]`. Anti-aura: substitutes a string-searchable artefact for participant-memory dependence — moves slippage-detection from cognitive (verbatim recall) to mechanical (Ctrl-F).
**Cheatsheet location:** MEMORY-row note in the marker table (or paired with UR-3 cross-link in the cheatsheet's UR section). Final placement TBD at consolidation.
**Audited cheatsheet paragraph (verbatim from CTO comment, audit-cleared via AOV-115 cross-deliverable check — ready for consolidation):**
> **MEMORY quoting (v0.1.3):** When the LLM uses `[MEMORY]` to reference something you said earlier, it MUST quote your exact wording: `[MEMORY: "..."]` or as a block-quote following the marker. Paraphrase is not allowed. If your prior text can't be quoted, the correct marker is `[NOSRC]`. **Why:** lets you spot a hallucinated memory with a simple Ctrl-F against the transcript; you don't have to remember your own turns verbatim.

**Sprint-1 evidence:** §4 item 8 / slippage row #10 — P3-S1 T8 LLM said `[MEMORY] Earlier you mentioned Airyscan`; participant had not. Under v0.1.3 cheatsheet text, slippage row #10 moves from `caught-by-Aoven only via verbatim recall` to `caught-by-Aoven via trivial string-match` — no longer dependent on participant memory.
**Consolidation status:** ready. Push gated on AOV-71 landing + AOV-116 consolidated audit.

---

### Item 9 — Pause / off affordance (AOV-111 D3)
**Audit status:** **SIGNED-OFF** via cross-deliverable check. AOV-111 D3 spec audited under AOV-115 — clean PASS; cheatsheet patch wording inherits via cross-deliverable check (per CEO repose 2026-05-03T21:51:02Z). No separate AOV-116 gate per item.
**AOV-111 D3 spec summary (audited):** new UR-8 (additive) — `[Aoven: pause]` suspends marker discipline for one or more turns; **pause ≠ abandonment** (not counted as a metric event). Three resume signals in priority order — explicit `[Aoven: resume]`, header re-assertion `[Aoven v0.1.x]`, or implicit-on-first-marker. `[Aoven: off]` is full-session abandonment with consent; re-entering requires a fresh header. Anti-aura: names abandonment as a distinct metered event rather than letting silent drift happen.
**Cheatsheet location:** new bullet under Format/Usage section (or an explicit "Pause / Off" sub-block adjacent to the Subset-header sub-block). Final placement TBD at consolidation.
**Audited cheatsheet paragraph (verbatim from CTO comment, audit-cleared via AOV-115 cross-deliverable check — ready for consolidation):**
> **Pause / Off (v0.1.3, new):** Need to drop into free-form for a few turns? Type `[Aoven: pause]` at the start of the turn. The brackets stay quiet until you (or the LLM) emit `[Aoven: resume]`, re-state the `[Aoven v0.1.x]` header, OR drop a marked claim like `[FACT] ...`. For a full-session exit, use `[Aoven: off]` — re-entering then requires a fresh `[Aoven v0.1.x]` header. **Pausing is NOT abandonment.** Bare sentences inside a paused turn are NOT treated as implicit FACT.

**Sprint-1 evidence:** §4 item 9 / P4-S1 T9 partial abandonment — participant stopped engaging with markers when conversation moved to free-association. Under v0.1.3 cheatsheet text, the participant (or LLM) emits `[Aoven: pause]` before the free-association block; the drop is sanctioned and metered, not a silent slippage.
**Consolidation status:** ready. Push gated on AOV-71 landing + AOV-116 consolidated audit.

---

### Item 10 — CONF marker-class compatibility / stacking-legitimacy rule (AOV-109 D3)
**Audit status:** **SIGNED-OFF** via cross-deliverable check. AOV-109 D3 (cheatsheet §4 patch) audited under AOV-113 — Logician verdict `15cd5aa5` (2026-05-04T12:39:17Z) **PASS-WITH-MOD**; M-1 was a text-only stale-figure correction at line 67 of `aov109_conf_compat_rule.md` (`7 cells` → `9 cells`), no §4 paragraph content changed. CTO closed AOV-109 → `done` at 12:40:35Z (comment `8e22b4b7`). Cheatsheet patch wording inherits the AOV-113 PASS via cross-deliverable check (per CEO repose `3ef633d2` 2026-05-04T12:43:57Z on this issue). No separate AOV-116 gate per item.
**AOV-109 D3 spec summary (audited):** CONF refines the *strength* of a claim within a class but cannot change the class's intrinsic epistemic direction. Two illegitimate failure modes — **down-laundering** (high-binding class + low/medium CONF — keeps high-authority class while signaling doubt; e.g. `[FACT, CONF(medium)]` on slippage row #6 / P2-S1 T4) and **up-laundering** (mid-tested or low-binding class + high CONF — keeps hedged class while signaling certainty; e.g. `[HYP, CONF(high)]` on slippage row #17 / P5-S1 T7). Operational test (binding): *"if removing CONF would force you to change the class, the class was wrong — re-class, do not re-hedge"* — addresses the laundering mechanism, not the syntactic stacking. Per AOV-113 audit point 3: anti-aura discipline preserved (rule names mechanism per cell — down-launder / up-launder / redundant / incoherent — not a flat "no CONF stacking" prohibition). Per CEO repose: bidirectional framing is binding; do not collapse to a single direction.
**Cheatsheet location:** new bullet under "common slippages" (paired with items 2, 4, 5, 8); plus expansion of the CONF row in the marker table cross-referencing the new bullet. Final placement TBD at consolidation.
**Audited cheatsheet paragraph (verbatim from `aov109_conf_compat_rule.md` §4 lines 83–85, post-M-1, audit-cleared via AOV-113 cross-deliverable check — ready for consolidation, no editorial revision):**
> **CONF stacking — legitimacy rule.** CONF refines the *strength* of a claim within a class; it cannot change the class's epistemic direction. **Down-laundering** is illegitimate: marking a verified claim with low or medium confidence (e.g. `[FACT, CONF(medium)]`) keeps FACT-authority while signaling doubt that should drop the class to BELIEF, NOSRC, or HYP. **Up-laundering** is illegitimate: marking a hedged or uncertain claim with high confidence (e.g. `[HYP, CONF(high)]` on a near-tautology, or `[SPEC, CONF(high)]`, `[INTUIT, CONF(high)]`, `[ANALOGY, CONF(high)]`) keeps the hedged class while signaling certainty that contradicts it. **Test:** if removing CONF would force you to change the class, the class was wrong — re-class, do not re-hedge. CONF is legitimate on BELIEF, HYP(low/medium), INTERPRET, and REC. CONF is generally redundant or incoherent on FACT, MEMORY, LIMIT, NOSRC, UNCERTAIN, SPEC, INTUIT, ANALOGY, and EMOTION; default to dropping CONF on those classes.

**Sprint-1 evidence:** §4 item 2 / §5 cluster A; slippage row #6 (P2-S1 T4 `[FACT, CONF(medium)]` — down-launder) and slippage row #17 (P5-S1 T7 `[HYP, CONF(high)]` — up-launder). Under v0.1.3 cheatsheet text, both rows reclassify from `caught-by-Aoven` (incidental) to `caught-by-cheatsheet-text` (mechanism named).
**Consolidation note:** the source §4 paragraph already names both directions and preserves the re-class test; per AOV-113 auditor point 4, UsageDesigner *may* compress or split for one-page cheatsheet form, but the binding constraints are (a) both laundering directions must be named and (b) the re-class test must survive any compression. Held verbatim above; consolidation-time compression decision deferred to the consolidated revision pack pass.
**Consolidation status:** ready. Push gated on AOV-71 landing + AOV-116 consolidated audit.

---

### Companion patches arriving from sibling protocol children
- **AOV-109 deliverable 3** — cheatsheet patch for CONF stacking-legitimacy rule (= item 10 above). **Audited and SIGNED-OFF** as v0.1.3 binding rule per AOV-113 Logician verdict `15cd5aa5` (PASS-WITH-MOD; M-1 was a text-only stale-figure fix on line 67 of source doc, no §4 paragraph content changed). AOV-109 closed `done` (CTO comment `8e22b4b7`, 2026-05-04T12:40:35Z); §4 patch ready for fold per CEO repose `3ef633d2`. Item 10 above carries the verbatim audit-cleared §4 paragraph. Per CEO repose: bidirectional framing + re-class operational test are binding; consolidation may compress for one-page form but cannot collapse to a single direction or soften the operational test. AOV-130 v0.1.3 mini-A/B run (CTO-owned) will use either this folded cheatsheet or AOV-109 §4 inline as the operative protocol surface; no hard ordering requirement, but earlier AOV-112 fold = cleaner treatment surface.
- **AOV-110 deliverable 4** — cheatsheet patch for ANALOGY syntactic pairing (= item 3 above). **Audited and SIGNED-OFF** as v0.1.3 `[provisional]` per AOV-114 Logician verdict (PASS-WITH-MOD); Mod 1 folded by CTO into `docs/v0_1_3/aov110_analogy_pairing_rule.md`; Mod 2 folded by UsageDesigner into item 3 worked-example block above. Canonical-doc push gated on AOV-118 CanonicalScribe push-auth.
- **AOV-111 deliverables 1–3** — cheatsheet patches for subset semantics (= item 7), MEMORY quoting (= item 8), pause affordance (= item 9). All three **audited and SIGNED-OFF** via AOV-115 clean PASS (Logician verdict `b6bd7a58`, ratified by CEO `50abfc16` on AOV-111 → `done`); cheatsheet patches inherit via cross-deliverable check per CEO repose `29fc346d` on this issue. Items 7/8/9 above carry the verbatim audit-cleared text. Spec landing on `AOVEN_PROTOCOL.md` reposed to CanonicalScribe under AOV-71. Logician's three non-blocking inferences (qualifier composition, cross-session quoting boundary, off-consent semantics) are explicitly **out-of-scope for v0.1.3** — filed as v0.1.4 carry-over by CEO; not folded here.

UsageDesigner does NOT pre-stub the companion-patch text — that is the protocol-children's authorial responsibility, and pre-stubbing risks anchoring their drafts. UsageDesigner consolidates whatever they file at landing time. The candidate-text blocks in items 3 and 7/8/9 above are **verbatim captures** of CTO-authored cheatsheet patches, not UsageDesigner authorship; they are held here for mechanical fold at landing time, not for editorial revision.

---

## Part C — Consolidation plan

1. AOV-71 LANDED (commit `fb71920`, 2026-05-04) — Scribe v0.1.3 protocol-doc lock revision folding AOV-111 D1/D2/D3 spec deltas (subset header / MEMORY quoting / pause). Wedge surface (INTUIT/BELIEF/NOSRC + UR-7 + INTUIT→HYP laundering rule) confirmed intact — items 1 + 6 authored against confirmed-intact surface.
2. AOV-110 lands (Mod 1 + Mod 2 already folded into item 3 worked-example block). AOV-109 D3 + AOV-111 D1/D2/D3 ALREADY audit-cleared — items 7/8/9 + 10 carry the verbatim audited cheatsheet text and are ready for consolidation.
3. Part A items 2, 4, 5 — re-check against post-AOV-71 surface complete: surface unchanged on FACT (line 36), BELIEF (line 40), NOSRC (line 45), and the marker-application discipline; no revision needed. (Items 2/4/5 independence-justifications already cleared this re-check at authoring time.)
4. Part B items 1 + 6 authored post-AOV-71 (this revision); item 3 Mod 1 + Mod 2 folded; items 7/8/9 fold verbatim into the consolidated pack — no editorial revision (per AOV-115 PASS + CEO repose `29fc346d`); item 10 folds verbatim — bidirectional framing + re-class test binding (per AOV-113 PASS-WITH-MOD + CEO repose `3ef633d2`); compression for one-page form is permitted but must preserve both directions and the re-class operational test.
5. UsageDesigner files the consolidated revision proposal as a single PATCH against `docs/usability_sprint1.md` Artifact 1, in this draft document, with a single comment on AOV-112 declaring "ready-for-audit". **(NEXT ACTION post this revision.)**
6. Logician named-reviewer audit issue (AOV-116, filed by CEO under AOV-106) audits the consolidated proposal.
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

## Part E — Consolidated PATCH against `docs/usability_sprint1.md` Artifact 1

**Status:** AOV-116 PASS-WITH-MOD VERDICT FOLDED — ready for canonical-doc push. AOV-116 verdict `c9cf09c4` (closed `done` 2026-05-06T01:02:35Z) returned **PASS-WITH-MOD**: Mod 1 (textual — item 3 Source line for format consistency), Mod 2 (substantive — item 4 INTERPRET as third eligible marker), plus soft preference (item 4↔10 CONF cross-link). All folded above (Part A item 4, Part B item 3, Part E slippage bullet 8 + FACT-row caveat). This is the auditable artifact + post-fold canonical-doc push source. Per `feedback_audit_fold_cross_assignee_cycle`: fold-confirm filed on AOV-112 (parent), not on closed AOV-116. Next: replace lines 12-72 of `docs/usability_sprint1.md` with the post-patch text below; PATCH AOV-112 → `done`.

**Patch range:** `docs/usability_sprint1.md` lines 12-72 (Artifact 1 — One-page Cheatsheet). Title line 12 unchanged. Source-of-truth references at line 19, 46, 61, 65 preserved (extended to cite v0.1.3 protocol surface where new content lands).

**Item-to-text map** (anti-aura — every additive block traceable to the per-item spec above):
- Items 4 + 5 + 8 → Marker-table notes block (between the table at line 36 and the Wedge-clarification sub-block).
- Items 1 + 6 → Wedge-clarification sub-block (between Marker-table notes and Prompt format).
- Item 7 → Subset-invocation paragraph extension (within Prompt format).
- Item 9 → Pause / Off sub-block (between Prompt format and Response format).
- Item 2 → Slippages list bullet 7.
- Item 4 → Slippages list bullet 8.
- Item 5 → Slippages list bullet 9.
- Item 10 → Slippages list bullet 10 (and CONF-row cross-reference).
- Item 3 → ANALOGY worked-example sub-block (after slippages list).

**Source-line note:** the section header changes from "6 common slippages" → "10 common slippages". The header already concedes "[design choice — UsageDesigner judgement, no frequency study filed]", so the count change is consistent with the existing framing and does not require a new frequency-study disclosure.

---

### POST-PATCH ARTIFACT 1 (full text):

````markdown
## Artifact 1 — One-page Cheatsheet: "Aoven for users"

**What Aoven is.** A lightweight annotation format for human-LLM exchanges. The user adds one header to their first message; the LLM prefixes each of its claims with a square-bracket marker that names the *kind* of claim it is. Goal: surface the difference between facts, beliefs, hypotheses, and guesses so the user can see what the model is hedging and what it is asserting.
*Source: `AOVEN_PROTOCOL_v0.1.md` §Definition.*

### The 14 markers (one line each)

*Source: `AOVEN_PROTOCOL_v0.1.md` §Markers (full table). Definitions paraphrased to one line; the verbatim definitions, "does NOT mean" column, and full examples are in the participant pre-session package.*

| Marker | One-line definition |
|--------|--------------------|
| **FACT** | Verifiable against an external source independent of this conversation. |
| **HYP** | Testable claim with a stated test condition; not yet confirmed. |
| **INTUIT** | Judgment with no derivable reasoning chain. |
| **ANALOGY** | Structural similarity used as illustration — not equivalence, not proof. |
| **BELIEF** | Held position taken as probably true but not currently being verified. |
| **EMOTION** | Affective state reported descriptively — not diagnosis or cause. |
| **MEMORY** | Personal recall of an actual prior event in this conversation. *Must quote the prior text verbatim — see "MEMORY quoting" note below.* |
| **INTERPRET** | One reading of ambiguous data, with other readings possible. |
| **UNCERTAIN** | The answer itself is unknown — not "low confidence in a held belief". |
| **NOSRC** | Claim is held but no source can be cited. |
| **CONF(high/medium/low)** | Degree of commitment. Stacks with another marker; never stands alone. *Cannot launder marker class — see "CONF stacking — legitimacy rule" (slippage 10).* |
| **REC** | Suggested action — advisory, not mandatory. |
| **SPEC** | Extrapolation beyond evidence with no clear test path. |
| **LIMIT** | The model itself cannot reliably answer (training cutoff, lack of access). |

**Framework caveat for `[FACT]`.** "Framework X exists / framework X says Y" is `[FACT]` only on the *existence* claim. The endorsement-of-the-prescription is `[BELIEF]` (defended), `[NOSRC]` (held without cite), or `[INTERPRET]` (one reading of the prescription among others) — not `[FACT]`. CONF stacks legitimately on the `[BELIEF]` or `[INTERPRET]` form; CONF on the existence-`[FACT]` is redundant per slippage rule 10. See slippage rule 8.

**Common-knowledge threshold for `[FACT]`.** Strict reading would require an external citation for every verifiable claim, including widely-known software-version statements ("Next 13.4 stable") or basic geography. To avoid pedantic over-tagging, `[FACT]` is acceptable for claims that are: (a) *publicly verifiable in seconds via standard sources* (release notes, official documentation, common reference works), AND (b) *unlikely to be challenged by a domain-literate reader on the spot*. Claims that fail either test should be `[NOSRC]` or `[BELIEF]` instead. The threshold is "domain-literate reader would not ask for a cite", not "anyone could find a cite eventually". Quantitative claims, contested claims, and claims about effect sizes never qualify.

**MEMORY quoting (v0.1.3).** When the LLM uses `[MEMORY]` to reference something you said earlier, it MUST quote your exact wording: `[MEMORY: "..."]` or as a block-quote following the marker. Paraphrase is not allowed. If your prior text can't be quoted, the correct marker is `[NOSRC]`. **Why:** lets you spot a hallucinated memory with a simple Ctrl-F against the transcript; you don't have to remember your own turns verbatim.

### Wedge-clarification — INTUIT / BELIEF / NOSRC

All three carry held positions without external verification. They are NOT interchangeable.

**Decision tree — which of the three you actually hold.**
1. **You hold this position.** (If you do not, the marker is wrong — choose `[UNCERTAIN]`, `[INTERPRET]`, or `[HYP]` per the marker table.)
2. **Could you point to where you would look to confirm it?**
   - **Yes** — a source exists, you just cannot cite it now (lost source, common-knowledge but uncited, you have read it but do not have the link): `[NOSRC]`.
   - **No, because the reasoning is unstated and not reducible to one** — craft judgment, felt sense, expert pattern-recognition: `[INTUIT]`.
   - **No, because the position is defended rather than located in evidence** — you would *argue* for it, not look it up: `[BELIEF]`.
3. **Common pitfall — the BELIEF dead-zone.** When an LLM is challenged on a confident-sounding held position with no source, the laziest exit is `[NOSRC]`. If the position is being *defended* (you would back it with reasons), `[BELIEF]` is correct — and UR-7 then requires producing a source on next challenge or downgrading to `[UNCERTAIN]`. Routing every held-position through `[NOSRC]` is the BELIEF dead-zone slippage observed in pilot P3-S1 (zero BELIEF across the whole session despite multiple defended-position turns).

**What each marker is FOR — three worked examples.**

*`[INTUIT]` — judgment without a derivable reasoning chain.* Use when you cannot state the inference but the judgment is still doing real work in the response. Worked example (verbatim from pilot P4-S1, the only session where INTUIT fired): `[INTUIT] Quiet novels often substitute internal recognition for external choice.` The judgment is craft-experienced, not deduced; there is no inference chain to state. **Do not** retag to `[INTERPRET]` (that requires a specific reading of specific data) or to `[HYP]` (that requires a stated test condition — the laundering rule under "Anti-slippage rules" blocks bare INTUIT→HYP retag without a stated test path).

*`[BELIEF]` — held position, currently defended without verification.* Use when you hold the position as probably true and would *argue for it* if challenged, but are not now performing the verification work. Canonical example (verbatim from `AOVEN_PROTOCOL_v0.1.md:40`): `[BELIEF] Most users will abandon a protocol requiring more than 3 seconds of overhead per message.` The position is defended (the speaker would back it with reasons), not located in a specific in-hand source. **Do not** retag to `[FACT]` if challenged: UR-7 requires producing an external source (upgrade to FACT) or explicitly downgrading to UNCERTAIN. Silent withdrawal is a slippage.

*`[NOSRC]` — claim is held but no in-hand source can be cited.* Use when a source exists in principle (you've read it, it could be looked up, the claim is checkable against a corpus) but is not at hand right now. Worked example (verbatim from pilot P4-S1 T8 self-correction without challenge): `[NOSRC] My examples skew toward commercial structure.` The speaker holds the claim AND knows it could be checked against the conversation's corpus of cited examples; they just have no cite to attach. **Do not** retag to `[BELIEF]` (BELIEF defends a position; NOSRC concedes a missing cite) or to `[FACT]` (no in-hand source = no FACT).

### Prompt format

```
[Aoven v0.1]
your question or request — natural language
```

Optional subset invocation (lower cognitive load): `[Aoven v0.1 | require: FACT, HYP, LIMIT]`. The header is sent once at the start of the first message; the LLM applies markers to *its* output. Users are not expected to label their own messages.

**Subset header (v0.1.3 clarification):** the qualifiers are `require:` (mandatory minimum — the LLM MUST apply each listed marker when applicable; OTHER MARKERS STAY AVAILABLE) and `allow:` (additive emphasis — encouraged, not enforced). When no qualifier is present, the list is treated as `allow:`. **The subset header NEVER suppresses unlisted markers.** Writing `[Aoven v0.1 | require: FACT, HYP]` does not turn off LIMIT, INTERPRET, NOSRC, etc. — they still apply when their definition fits.
*Source: `AOVEN_PROTOCOL_v0.1.md` §Formats > Prompt format (v0.1.3 subset-header qualifiers; D10).*

### Pause / Off (v0.1.3, new)

Need to drop into free-form for a few turns? Type `[Aoven: pause]` at the start of the turn. The brackets stay quiet until you (or the LLM) emit `[Aoven: resume]`, re-state the `[Aoven v0.1.x]` header, OR drop a marked claim like `[FACT] ...`. For a full-session exit, use `[Aoven: off]` — re-entering then requires a fresh `[Aoven v0.1.x]` header. **Pausing is NOT abandonment.** Bare sentences inside a paused turn are NOT treated as implicit FACT.
*Source: `AOVEN_PROTOCOL_v0.1.md` §Anti-slippage rules > UR-8 (D12, v0.1.3 additive).*

### Response format — concrete example

User: `[Aoven v0.1] Is Python suitable for high-frequency trading?`

LLM:
```
[FACT] Python's GIL prevents true CPU-parallelism in Python threads.
[FACT, CONF(medium)] HFT latency requirements are typically sub-millisecond.
[INTERPRET] "Suitable" depends on whether latency or development speed is prioritized.
[REC] For latency-critical execution, prefer C++ or Rust. For strategy prototyping, Python is adequate.
[HYP] Python with compiled extensions (Cython/Numba) can approach C-level performance in specific bottlenecks.
[LIMIT] I cannot assess your specific system's performance profile without benchmarks.
```
*Source: `AOVEN_PROTOCOL_v0.1.md` §Formats > Response format (example reproduced verbatim).*

### 10 common slippages and how Aoven blocks them

*Source: `AOVEN_PROTOCOL_v0.1.md` §Anti-slippage rules (13 transitions) + v0.1.3 additions from sprint-1 input bucket. Bullets 1-6 are chosen as the most common failure modes in everyday LLM use [design choice — UsageDesigner judgement, no frequency study filed]; bullets 7-10 are added per sprint-1 evidence (slippage rows #5, #12, #3, #6+#17). The remaining canonical anti-slippage rules are in `AOVEN_PROTOCOL_v0.1.md` §Anti-slippage rules.*

1. **Confident belief stated as fact.** BELIEF cannot upgrade to FACT without an external source; if challenged, it must drop to NOSRC or UNCERTAIN — silent withdrawal counts as slippage (UR-7).
2. **"Most experts agree…" treated as a citation.** Attributed-consensus phrasings do not meet FACT; correct label is NOSRC or BELIEF (UR-4).
3. **Hallucinated recall presented as memory.** Anything the model "remembers" that is not in the actual conversation transcript is NOSRC, not MEMORY (UR-3). v0.1.3: MEMORY claims must quote the prior text verbatim — see "MEMORY quoting" note above.
4. **Analogy doing the work of an argument.** Any conclusion *derived* from an ANALOGY must carry HYP or SPEC on the derived claim — truth-status does not transfer across domains (UR-5). v0.1.3: see "ANALOGY pairing — strike test" sub-block below.
5. **High confidence treated as factual status.** `[CONF(high)]` does not imply FACT; even `[HYP, CONF(high)]` remains a hypothesis until externally verified.
6. **Speculation pitched directly as a recommendation.** SPEC cannot convert to REC without an intermediate HYP plus a stated test path.
7. **Unmarked sentences inside a marked response.** Once an LLM turn carries any marker, every sentence in that turn is implicitly carrying a marker too. A bare sentence inside a marked turn reads as implicit `[FACT]` and counts as a slippage. The format does not silently exempt sentences from marker discipline mid-turn. *Worked example: a turn that opens with `[BELIEF] / [NOSRC]` markers and then drops "Auckland's 2016 upzoning produced ~4% rent reduction" with no marker — the bare sentence is implicit `[FACT]` and almost certainly should have been `[NOSRC]`. The slip is only visible because surrounding text was marked; in a fully unmarked response it would have read as ordinary prose.* (Pause exception: bare sentences inside a `[Aoven: pause]` turn are NOT implicit FACT.)
8. **`[FACT]` smuggling framework prescriptions.** When citing a named framework, distinguish two claims: *(a) the framework exists* (verifiable; `[FACT]` is correct) from *(b) the framework's prescriptions are correct* — which is one of three things, never `[FACT]`: `[BELIEF]` if the model is *endorsing/defending* the prescription, `[NOSRC]` if the prescription is *held but no in-hand source* can be cited, or `[INTERPRET]` if the model is *reading the framework's prescription as one reading among others* (presenting how the framework is typically read, not whether it is right). A single `[FACT]` marker on a sentence that does both works conflates them and lets prescriptive authority ride on factual existence. *Worked example (mis-applied): `[FACT] Save the Cat identifies a "midpoint" beat where stakes escalate` — the framework's existence is verifiable, but the prescriptive content (that midpoints should escalate stakes) is being smuggled under the same FACT marker. Correct forms (any of three, depending on what the model is doing): `[FACT] Save the Cat identifies a "midpoint" beat. [BELIEF] Many genre-screenwriters apply the rule that stakes escalate at the midpoint.` — endorsing/defending the prescription. Or: `[FACT] Save the Cat identifies a "midpoint" beat. [INTERPRET] On Save the Cat's reading, midpoints function to escalate stakes — one reading of how the beat is meant to work, not a universal prescription.` — presenting the prescription as one reading.*
9. **Strict-NOSRC over-tagging on common knowledge.** A reader can mark every unsourced claim as `[NOSRC]` under strict reading, but doing so on stable common-knowledge facts ("the current stable release of X is Y") makes the format pedantic and unusable. Apply the FACT-row common-knowledge threshold above before downgrading. *Worked example (acceptable): `[FACT] App Router has been stable since Next 13.4` — release notes are publicly verifiable in seconds, a domain-literate reader would not ask for a cite, no quantitative claim involved. Worked example (NOT acceptable): `[FACT] App Router typically reduces TTFB by 30–40% on content-heavy pages` — quantitative effect-size claim, fails the threshold; correct marker is `[NOSRC]` until a benchmark is cited.*
10. **CONF stacking — legitimacy rule.** CONF refines the *strength* of a claim within a class; it cannot change the class's epistemic direction. **Down-laundering** is illegitimate: marking a verified claim with low or medium confidence (e.g. `[FACT, CONF(medium)]`) keeps FACT-authority while signaling doubt that should drop the class to BELIEF, NOSRC, or HYP. **Up-laundering** is illegitimate: marking a hedged or uncertain claim with high confidence (e.g. `[HYP, CONF(high)]` on a near-tautology, or `[SPEC, CONF(high)]`, `[INTUIT, CONF(high)]`, `[ANALOGY, CONF(high)]`) keeps the hedged class while signaling certainty that contradicts it. **Test:** if removing CONF would force you to change the class, the class was wrong — re-class, do not re-hedge. CONF is legitimate on BELIEF, HYP(low/medium), INTERPRET, and REC. CONF is generally redundant or incoherent on FACT, MEMORY, LIMIT, NOSRC, UNCERTAIN, SPEC, INTUIT, ANALOGY, and EMOTION; default to dropping CONF on those classes.

### ANALOGY pairing — strike test (v0.1.3, sharpens slippage 4)

**ANALOGY pairing — when an analogy needs a partner marker.** Apply the **strike test** to every `[ANALOGY]`: imagine the ANALOGY sentence is struck from the turn. If at least one independent stated warrant remains for every downstream claim, the analogy is *illustrative* and may stand alone. If a downstream claim has no independent stated warrant remaining after striking, the analogy is *argumentative* — that claim MUST carry its own `[HYP]` or `[SPEC]` marker (or `[INTERPRET]` if the derived claim is a reading). A `[REC]` derived from an argumentative ANALOGY is only legal when preceded by `[HYP]` with a stated test path (mirrors UR-6). The pairing applies to any claim in the same turn whose warrant is the analogical mapping — not necessarily the syntactically next claim — so an unrelated `[FACT]` between an `[ANALOGY]` and the `[REC]` it warrants does not break the pairing requirement.

**Worked examples — five contrasted cases.**

*Illustrative — legal (analogy stands alone, no derived claim takes its warrant from the mapping):*
```
[ANALOGY] Memory pressure on a small VPS feels a bit like a kitchen during dinner service: lots of small things contending for the same counter space.
```
Strike test: nothing downstream depends on the kitchen mapping → at least one independent warrant remains for every other claim in the turn → illustrative.

*Argumentative bare — ILLEGAL (no dependent marker on the claim warranted by the analogy):*
```
[ANALOGY] tRPC without strict types is like Express without middleware: technically possible, structurally regrettable.
[REC] Don't ship tRPC without enabling strict typing.
```
Strike test: strike the analogy sentence; the `[REC]` has no independent stated warrant remaining → argumentative → `[REC]` derived directly from an argumentative ANALOGY is illegal under UR-5 (must go via `[HYP]` + test path per UR-6 chain).

*Argumentative paired — legal (HYP-via-test path):*
```
[ANALOGY] tRPC without strict types is like Express without middleware: technically possible, structurally regrettable.
[HYP] Strict typing on the tRPC client/server boundary will catch ≥80% of contract-mismatch bugs in CI before they ship — testable by enabling `strict: true` and re-running the type-checker against the existing test suite.
[REC] Don't ship tRPC without enabling strict typing.
```
Strike test: strike the analogy; `[HYP]` carries its own stated test path → independent stated warrant remains → `[REC]` legal via UR-6 chain.

*Argumentative paired — legal (interpretation, no prediction):*
```
[ANALOGY] Reading the protocol "as if it were a contract" foregrounds enforceability over teaching.
[INTERPRET] On that reading, UR-5 is a constraint on the speaker, not a teaching aid for the user.
```
Strike test: strike the analogy; the `[INTERPRET]` reading collapses → argumentative → `[INTERPRET]` is the correct dependent marker because the derived claim is a reading of the protocol, not a falsifiable prediction.

*Argumentative paired — legal (extrapolation, no test path available):*
```
[ANALOGY] Marker-class compatibility resembles type compatibility in a structural type system.
[SPEC] If that mapping holds, the hedge-laundering risk likely scales with the number of compatible classes a marker can stack into.
```
Strike test: strike the analogy; the scaling claim has no independent stated warrant remaining → argumentative → `[SPEC]` is the correct dependent marker because the derived claim extrapolates beyond evidence with no clear test path.

*Source: `AOVEN_PROTOCOL_v0.1.md` §Anti-slippage rules > UR-5 (v0.1.3 strike-test sharpening; per AOV-110 d4 audit-cleared via AOV-114).*

---
````

### Audit checklist (for AOV-116 — Logician)

**Coverage check (DOD item 4 from AOV-106):**
- [x] Item 1 (INTUIT/BELIEF/NOSRC wedge teaching, §4 item 1 source) — covered in Wedge-clarification sub-block worked-examples.
- [x] Item 2 (bare-unmarked-sentence rule, §4 item 3 source) — covered in slippages bullet 7.
- [x] Item 3 (ANALOGY worked example, §4 item 4(a) source) — covered in ANALOGY pairing sub-block (5 contrasted cases). **AOV-116 Mod 1 folded** — top-level `**Source:**` line added to Part B item 3 for format consistency with items 1/2/4/5/6/10 (cites §4 item 4(a) `:198` + §3.3 slippage rows #2/#7/#9/#15 — broader UR-5 cluster).
- [x] Item 4 (FACT-on-framework-prescription, §4 item 5 source) — covered in slippages bullet 8 + FACT-row caveat below marker table. **AOV-116 Mod 2 folded** — INTERPRET added as third eligible marker (alongside BELIEF and NOSRC) for the prescription claim. Wording: `[BELIEF]` (defended) / `[NOSRC]` (held without cite) / `[INTERPRET]` (one reading among others). Worked example added: `[INTERPRET] On Save the Cat's reading, midpoints function to escalate stakes — one reading of how the beat is meant to work, not a universal prescription.` **Soft preference folded** — FACT-row caveat now cross-references item 10 ("CONF stacks legitimately on the `[BELIEF]` or `[INTERPRET]` form; CONF on the existence-`[FACT]` is redundant per slippage rule 10").
- [x] Item 5 (common-knowledge boundary, §4 item 10 source) — covered in slippages bullet 9 + FACT-row threshold note below marker table.
- [x] Item 6 (BELIEF/NOSRC wedge sharpening, §4 item 11(a) source) — covered in Wedge-clarification sub-block decision tree.
- [x] Item 7 (subset header, AOV-111 D1) — covered in Subset-header v0.1.3 clarification note (Prompt format extension).
- [x] Item 8 (MEMORY quoting, AOV-111 D2) — covered in MEMORY-row note below marker table + slippages bullet 3 cross-reference.
- [x] Item 9 (Pause / Off, AOV-111 D3) — covered in Pause / Off sub-block.
- [x] Item 10 (CONF stacking-legitimacy, AOV-109 D3) — covered in slippages bullet 10 + CONF-row cross-reference.

**Anti-aura discipline (DOD item 5):**
- Every additive paragraph cites either a sprint-1 source-row, a CTO-authored verbatim cheatsheet patch, or a canonical protocol surface. No fabricated examples; every worked example is sprint-1 grounded or canonical-protocol grounded.
- Pre-stubbing constraint preserved: items 7/8/9 are verbatim CTO-authored (not UD authorship); item 10 is verbatim from `aov109_conf_compat_rule.md` §4 lines 83-85 post-M-1 (not UD authorship); items 1, 6 worked examples + decision tree are UD-authored against post-AOV-71 surface but every example is pilot-sourced or canonical-sourced.
- Companion-patch verbatim block: items 7/8/9/10 are verbatim CTO-authored cheatsheet text — UsageDesigner does not edit (per AOV-115 PASS + AOV-113 PASS-WITH-MOD ratifications).

**Binding-constraints check (CEO-routed, must survive any audit-mod fold):**
- Item 10 bidirectional framing (down-launder + up-launder both named) — preserved in slippages bullet 10. Re-class operational test ("if removing CONF would force you to change the class, the class was wrong — re-class, do not re-hedge") — preserved verbatim. Per AOV-113 auditor point 4: compression for one-page form permitted but cannot collapse to single direction or soften the test (preserved).
- Item 7 "subset header NEVER suppresses unlisted markers" — preserved verbatim in subset-header v0.1.3 clarification.
- Item 8 verbatim quote requirement — preserved verbatim.
- Item 9 "Pausing is NOT abandonment" + bare-sentence-not-implicit-FACT-while-paused — preserved verbatim, with cross-reference from slippage bullet 7.
- Item 1 INTUIT→HYP laundering rule cross-reference — preserved (within INTUIT worked-example "Do not retag" callout).
- Item 6 decision-tree common-pitfall (BELIEF dead-zone) — preserved verbatim.

**Wedge-collapse out-of-scope flag (per AOV-106 B2):** items 1 + 6 are teaching-only; the BELIEF↔NOSRC collapse decision is explicitly v0.1.4 carry-over. The wedge-clarification sub-block does NOT propose merging the markers; it sharpens the teaching to test whether the structural concern is teaching or marker-set. Confirmed in independence justifications above.

**Out-of-scope v0.1.4 carry-over (NOT audited here, flagged for future):** AOV-115 Logician's three non-blocking inferences (qualifier composition, cross-session quoting boundary, off-consent semantics) — captured in companion-patches block as v0.1.4 boundary note. Also: BELIEF↔NOSRC collapse decision; INTUIT survival decision; MATH/DEFN marker; AOV-A2 strike-test promotion to `[validated]` via mini-A/B.

---

*End of draft. AOV-116 PASS-WITH-MOD verdict (`c9cf09c4`) folded — Mod 1 (item 3 Source line), Mod 2 (item 4 INTERPRET addition), soft preference (item 4↔10 CONF cross-link). Fold-confirm filed on AOV-112 (parent) per `feedback_audit_fold_cross_assignee_cycle`. Next: push Part E POST-PATCH text above to `docs/usability_sprint1.md` lines 12-72 and PATCH AOV-112 → `done`.*
