# Aoven Phase-3.5 — Real-External-Human Usability Pilot — Scoping Doc

**Author:** CEO (`491a73e0-f454-4e66-86f1-49b08bbbcd91`) — AOV-107
**Audit gate:** EpistemicLogician (`2ae117a1-f490-4e8e-a693-0f1d8d1d675b`) — child filed at scoping-doc-ready (this commit)
**Predecessor:** AOV-101 sprint-1 agent-simulated pilot, PASS-with-revisions ratified at CEO countersign `64292bfe` (2026-05-03 20:54:54Z), Logician fold verdict at AOV-105 `8fd7d0d2` / commit `6a75171`.
**Source numbers cited from:** `docs/usability_sprint1_results.md` at fold-commit `83f9463`.
**Status:** PROVISIONAL — pre-audit. Recruitment gate stays closed until audit clears + board surfaces sourcing.

---

## 0. Why this study, and why not just re-run sprint-1

Sprint-1 was scope-locked to **agent-simulated participants** for **mechanism validation**: does the protocol fire, do markers catch slippage, does the cheatsheet teach (CEO adjudication on AOV-101 description + comment `afd72971`, 2026-05-03 20:14Z). It returned PASS-with-revisions on mechanism, plus 5 missed-by-Aoven slippages clustered into design-input items (CONF stacking, marker-set redraw, ANALOGY discipline, MEMORY discipline, subset-header semantics, etc.).

Sprint-1 explicitly does **not** measure real-human cognitive load or real-human preference. The Q-A median 3 ("noticeable, manageable") and Q-D median 4 ("slightly better") are simulated-agent self-report. Cited verbatim in `usability_sprint1_results.md` §3.1 and §3.4, in-line caveat: *"This is a simulated-agent proxy and does not measure real-human cognitive load."*

**Phase-3.5 is a different study.** Different question (does the median real-human cog-load track the agent-simulated median 3, or does it diverge?), different population (real humans, not agents), different power calculation (descriptive-median stability on a 5-point Likert, not binary mechanism-fire), different ethics posture (real consent, real withdrawal mechanism, real data handling).

Anti-aura constraint per AOV-107 issue body: do not conflate with sprint-1 by reusing the same N or the same protocol unconditionally. Defensibility of this study rests on it being honestly framed as a different research question, not as "sprint-1 with humans."

---

## 1. Deliverable 1 — Consent + data-handling design

### 1.1 Consent form (electronic; signed before session opens)

Reuses sprint-1 Prompt-1 self-enrollment language (`docs/usability_sprint1.md` line 85) as the operative consent paragraph. Real-human pilot adds three IRB-equivalent items missing in the agent-simulated form:

1. **Affirmative consent on recording.** Participant explicitly agrees to (a) full conversation transcript capture, (b) 4-question survey response capture, (c) anonymized inclusion in the findings report. Must check three discrete boxes; bundled consent is rejected.
2. **Right of access + withdrawal.** Participant retains the right to (a) request a copy of their own transcript at any time, (b) request specific quotations be removed pre-publication, (c) revoke consent in full at any time within a 14-day window post-session — on revocation, transcript is deleted, session is dropped from the report, the report is regenerated if already drafted but not yet pushed.
3. **No covert use clauses.** No re-use for model training, no licensing to third parties, no sale, no aggregation with other studies without separate consent.

### 1.2 Data retention + anonymization

- **Transcripts:** held in private CEO+UsageDesigner folder for 90 days post-publication, then deleted. Path: `tests/usability/phase3_5/transcripts/<P-number>.md`, never committed to public repo.
- **Survey responses:** retained as anonymized aggregates indefinitely; raw per-participant responses follow same 90-day deletion as transcripts.
- **Anonymization rule:** participant identified by P-number + 1-line persona descriptor only. No real names, employers, locations precise to city, identifying topic details (e.g., "the 250k city" stays; "Boise, Idaho" doesn't), or quotable phrasings the participant could be re-identified by.
- **Pre-publication review:** each participant gets the draft findings report 5 days before publication and may flag any quotation for removal or rewording. Default: their flag is honored without negotiation.

### 1.3 Data-flow + storage

```
participant transcript + survey
        ↓
private CEO+UD holding folder (encrypted at rest)
        ↓ (14-day revocation window)
anonymized findings draft (P-numbered)
        ↓ (5-day participant pre-publication review)
findings report published in public repo
        ↓ (90 days)
raw transcripts deleted; aggregate survey data retained
```

### 1.4 Withdrawal mechanism

Single-email request (`<contact-TBD-by-execution-owner>`) with phrase "withdraw my Aoven Phase-3.5 participation." Acknowledged within 48h. Deletion + report-update completes within 7 days of request. Withdrawal does not require a reason.

### 1.5 IRB-equivalent posture

We are not academic, but the design above passes the standard items an IRB would demand: voluntary informed consent, data minimization (only what the study needs), right to withdraw, data retention limits, anonymization protocol, no coercion, no deception. Audit gate (Deliverable 5) verifies this against the items.

**Study-purpose disclosure (no deception):** Study purpose is disclosed verbatim in the consent form: "Measure your subjective cognitive load and perceived response quality when using the Aoven controlled-language protocol on a real LLM session." No deception about study purpose or data use.

### 1.6 Out of scope (Deliverable 1)

- Building a consent-collection web form. If a form is needed, file as `Phase-3.5-CONSENT-INFRA` child issue under execution owner. Email-with-checkboxes is the cheapest defensible default.
- Cross-jurisdiction GDPR / CCPA legal review. Anonymization above + 14-day revocation window covers the practical posture; formal legal review out-of-scope at pilot scale.

---

## 2. Deliverable 2 — Recruitment vector for non-agent humans

### 2.1 Target population

**LLM-fluent technical practitioners.** Three reasons:

1. The protocol's primary use case is technical / decision-oriented LLM use (sprint-1 personas were freelance dev, policy analyst, PhD student, novelist, decision-theorist — all literate-but-naive on Aoven, all comfortable with LLMs). Population alignment matters.
2. Human-load measurement on someone who cannot operate the LLM at all yields confounded signal (we'd be measuring LLM friction, not Aoven friction).
3. Cheatsheet-comprehension baseline — sprint-1's mechanism validation already showed the cheatsheet teaches at a "literate-but-naive" level. Phase-3.5 measures whether real humans at that level converge to the same load profile.

**External-validity caveat (Mod-2.B fold):** Findings cannot be generalized to non-technical or LLM-novice populations; further pilots required to extend external validity.

### 2.2 Pre-screen (5-question gate, sent before consent form)

1. Approximate weekly LLM use over the past 90 days (≥ 2 hours/week required to qualify).
2. Have you previously read AOVEN_PROTOCOL_v0.1.md, the cheatsheet, or any AOV-prefixed materials? (Answer must be NO.)
3. Are you on the Aoven project team or have you rated Aoven materials? (Answer must be NO.)
4. Are you willing to review and sign a recording + data-handling consent form before the session? (Required: YES.)
5. Do you have ~60 min for one session and a possible 5-day pre-publication review window? (Required: YES.)

Rejected applicants get a polite decline with no further outreach.

**Q4 ordering choice (Mod-1.B fold):** option (b) chosen — Q4 is reworded to ask willingness to review-and-sign rather than asking pre-screen recipients to consent to §1.1–§1.4 they have not yet seen. Cheapest defensible default; full consent form is delivered at the consent step after pre-screen pass, not bundled into the pre-screen email.

### 2.3 N — sample size

**N = 8.** Not the same as sprint-1's N=5.

Rationale [design choice, heuristic-not-formal]: this is a descriptive-median study on a 5-point Likert. Sprint-1's N=5 was sized for binary mechanism-fire confirmation; the median of 5 is a noisy estimator. For descriptive-median stability sufficient to distinguish "median 3" from "median 4" with reasonable confidence at the pilot scale, N=8 is the cheapest defensible step up. N=10 gains ~12% additional median-stability at +25% recruitment cost; N=8 is the sweet spot for a first real-human pass. Larger N gated on this pilot's findings — a Phase-3.5b expansion can be filed if signal warrants.

Anti-aura: the rationale above is a heuristic, not a formal power calculation; flagged as `[design choice, heuristic-not-formal]` for audit. If the audit demands formal power, a Phase-3.5-prep sub-issue can compute it; N=8 is provisional pending audit.

### 2.4 Recruitment channels (tiered)

| Tier | Channel | Cost | Latency | Tommy-bandwidth ask |
|------|---------|------|---------|---------------------|
| T1 | Tommy's direct network (DM ask) | $0 (or $40/session if accepted) | 3–7 days | Tommy sources contacts; 1 board-action item |
| T2 | Public Twitter / Bluesky / LinkedIn call | $0 | 7–14 days | One Tommy-authored post per channel |
| T3 | Prolific / Tommy-paid sourcing | $40/session × N + Prolific fees | 3–5 days | Board budget approval (board action) |

Decision rule:
- Open with T1. If T1 yields ≥ 8 qualified participants in 7 days, proceed.
- If T1 < 8 at day-7, open T2 in parallel for 7 days.
- If T1 + T2 < 8 at day-14, escalate to board for T3 budget approval.

Tommy's bandwidth is the bottleneck on T1 and the public-post drafting on T2; per `user_tommy.md` we do not micro-manage but escalate at major milestones — recruitment-open is a major milestone and is a `request_confirmation` board interaction filed under the execution owner, not a unilateral CEO call.

**Tier-confound disclosure (Mod-2.A fold, BLOCKING):** "T1 participants may exhibit social-desirability bias on Q-D vs T2/T3; findings will report Q-D stratified by tier and flag any tier-divergence ≥ 1 Likert point as a confound."

### 2.5 Incentive

$40 USD per 60-minute session. Standard Prolific / academic UX-research rate. Offered to all participants; participants may decline (and the decline does not affect inclusion). Tommy's-network participants offered the same; declines accepted gracefully.

### 2.6 Exclusion criteria

Hard-rejects (re-confirmed at consent step):
- Aoven core team (CEO, CTO, Logician, RedTeam, IndependentRater, CanonicalScribe, UsageDesigner).
- Anyone who has read AOVEN_PROTOCOL_v0.1.md, the cheatsheet, or rated AOV materials.
- Anyone with whom Tommy has discussed Aoven specifics in the past 90 days.

### 2.7 Out of scope (Deliverable 2)

- Demographic stratification (race / gender / age) beyond what's needed for confounder control. Pilot N=8 doesn't support stratified analysis.
- International recruitment with non-English LLM use. English-only first pass.

---

## 3. Deliverable 3 — Protocol mechanics

### 3.1 Format: remote async, single-arm descriptive

- **Remote async.** Participant runs their session at a time of their choosing within a 7-day window after consent clears. Consistent with sprint-1's setup; sync sessions add scheduling overhead disproportionate to the study scale and introduce researcher-presence confounds.
- **Single-arm descriptive (no vanilla control arm).** Q-D (perceived-improvement-vs-baseline) relies on participant's mental comparison to their own normal LLM use, not a measured vanilla session in this study. Rationale: counterbalanced within-subjects (Aoven + vanilla in same session) doubles session length to ~90 min and breaks the cog-load measurement (load is confounded by session duration). Between-subjects at N=8 has no statistical legs. Descriptive-only is the cheapest honest design at this scale; counterbalanced-comparison is filed as a Phase-3.5b option contingent on Phase-3.5 findings.

### 3.2 Session structure (60 min total)

| Block | Duration | Content |
|-------|----------|---------|
| Orientation | 10 min | Read cheatsheet (Artifact 1 of `docs/usability_sprint1.md`); read 1-page consent + handling summary; ask any clarifying Qs to UD via async message. |
| Session | 30 min | One ~10-message LLM conversation on a participant-chosen topic, using the Aoven format. Topic-intent declaration sent before session. Participant uses LLM platform of their choice; platform tracked. |
| Survey | 10 min | 4-question survey (Q-A cog-load, Q-B per-turn use/drop, Q-C format-completion, Q-D perceived-improvement) — same instrument as sprint-1, reproduced from `tests/usability/sprint1_survey.md`. |
| Debrief | 10 min | 3 open-ended Qs: (a) what surprised you, (b) what would you change first, (c) would you use this voluntarily on your own next LLM session? Plus free text. |

### 3.3 Recording + capture

- Full conversation transcript captured by participant (paste-back to UD).
- Survey responses captured in form / email.
- Optional screen recording — opt-in only, separate consent checkbox; not required.
- LLM platform name + model version logged as covariate.

### 3.4 Topic-selection discipline

Same as sprint-1 Prompt-2: participant declares topic before session, in one sentence. Topic must be (a) participant-chosen, (b) not steered by anyone on the project team, (c) one the participant genuinely wants to think through. UD does not pre-screen topic content; UD does pre-screen for "this participant has been told what to ask" red flags.

**Topic-confound logging (Mod-3.C fold):** "UD logs topic category per session; if ≥ 5/8 participants cluster on a single category, findings flag this as a topic-confound."

### 3.5 Total study window

21 days from launch, conditional on T1 yield:

| Phase | Days | Activity |
|-------|------|----------|
| Recruitment T1 | 1–7 | Tommy DMs network; consent forms returned |
| Recruitment T2 (conditional) | 8–14 | Public posts if T1 < 8 |
| Recruitment T3 (conditional) | escalation to board | Prolific only on board approval |
| Sessions | 8–14 | Async sessions in 7-day window after recruitment closes |
| Analysis | 15–18 | UD compiles findings draft |
| Pre-publication review | 19–23 | Participants flag quotations |
| Publication | 24 | Findings landed in `docs/usability_phase3_5_results.md` |

Deletion of raw transcripts at day 114 (publication + 90).

### 3.6 Out of scope (Deliverable 3)

- In-person sessions. Add as Phase-3.5b future option.
- Group / classroom format. Not relevant at pilot scale.
- A/B comparison with vanilla LLM sessions in same study. Phase-3.5b option only.

### 3.7 UD orientation Q&A scope (Mod-3.A fold, BLOCKING)

"During orientation Q&A, UD answers are limited to (a) procedural questions, (b) typo / formatting questions on the cheatsheet, (c) consent / data-handling questions. UD does not explain marker semantics beyond the cheatsheet's verbatim definition. If the cheatsheet is unclear on a marker, UD's response is: 'Use the cheatsheet definition; if unclear, mark CONF=low and proceed.'"

### 3.8 Q-D wording neutrality judgment (Mod-3.B fold)

Q-D in `tests/usability/sprint1_survey.md` is reused unchanged for Phase-3.5. Judgment: **already neutral**. Rationale: anchors are symmetric around a "No difference" midpoint ("Clearly worse" → "Slightly worse" → "No difference" → "Slightly better" → "Clearly better"), and the question stem ("how much better or worse did the Aoven response feel") asks the comparison in both directions rather than leading toward the improvement pole. No Phase-3.5 wording change folded; this judgment is the documented one-line rationale Mod-3.B requested.

---

## 4. Deliverable 4 — Version-of-Aoven-under-test

### 4.1 Decision rule (at recruitment-open T-7)

- **IF v0.1.3 lock has landed** by recruitment-open date, study runs on v0.1.3.
- **ELSE** study runs on v0.1.2.

### 4.2 v0.1.3 lock criteria (for "lock has landed")

All four required:

1. Canonical `AGENTS.md` header line carries `v0.1.3` and a `Last updated:` date.
2. Cheatsheet revision pack (AOV-112 + AOV-115 D1+D2+D3 fold) landed at canonical path with Scribe sign-off.
3. No open structural-design issues for v0.1.3. Per Mod-4.A fold: "In-flight = any issue with status 'todo' or 'in_progress' that touches v0.1.3 protocol-class structure or marker-set canonical definitions." (i.e., AOV-90, AOV-110, AOV-79 follow-ons closed; no in-flight protocol-class compatibility rule audits matching the Mod-4.A definition.)
4. 5-day stability window. Per Mod-4.B fold: "Canonical artifacts = {AGENTS.md, AOVEN_PROTOCOL_v0.1.md, tests/usability/cheatsheet*.md, marker-set table file}. No commits modifying these files in the 5 days preceding recruitment-open."

### 4.3 Rationale

Pilot tests the production version, not the prior version. v0.1.3 incorporates the protocol-structural fixes that sprint-1 surfaced (CONF stacking rule, marker-set redraw including BELIEF/INTUIT wedge tightening, MEMORY-quoting discipline, pause affordance, subset-header semantics, common-knowledge boundary). Testing v0.1.2 in a real-human pilot when v0.1.3 is the planned production version means measuring a known-obsolete artifact's load — wasted N.

But: cannot launch on a version whose canonical artifacts aren't stable. The 4-criterion lock gate above is the structural defense.

### 4.4 Lock-decision owner + timing

- **Owner:** CEO (this agent) at recruitment-open T-7 (one week before recruitment opens).
- **Deliverable:** comment on AOV-107 (or its child) with the lock-state snapshot and the chosen version. Audit-able.

### 4.5 Out of scope (Deliverable 4)

- Multi-version comparison (v0.1.2 vs v0.1.3 in same study). Wasted N at this scale.
- Re-litigating v0.1.3 design choices in this issue. v0.1.3 design is owned by CTO + Logician chains; this scoping doc only consumes their lock state.

---

## 5. Deliverable 5 — Audit gate (named-reviewer per `feedback_named_reviewer_gate.md`)

### 5.1 Audit child filing

Filed at scoping-doc-ready (this commit, this heartbeat). Audit child:

- **Title:** `[PHASE-3.5-AUDIT] real-human pilot scoping doc — Logician audit`
- **Assignee:** EpistemicLogician (`2ae117a1-f490-4e8e-a693-0f1d8d1d675b`)
- **Status:** `todo` (run pool wakes per `feedback_named_reviewer_routing.md`)
- **Parent:** AOV-107
- **Goal:** AOV-1 goal id `254a0ca9-26e0-4601-aa08-f9492e461896`

### 5.2 Audit DOD (5 questions)

1. **Consent design IRB-equivalent?** Does §1 cover voluntary informed consent, data minimization, right of withdrawal, retention limits, anonymization, no coercion, no deception?
2. **Recruitment vector defensible?** Is target population (§2.1) tied to the research question? Are exclusion criteria (§2.6) tight enough to prevent contamination? Is the tiered T1/T2/T3 channel structure (§2.4) honest about the Tommy-bandwidth and budget gates?
3. **Protocol mechanics not pre-biased?** Does §3 avoid steering participants toward favorable verdicts? Topic-selection discipline (§3.4)? Single-arm-descriptive design choice (§3.1) honest about its limits?
4. **Version-decision rationale tracks v0.1.3 timing?** Does §4 lock criteria + 5-day stability window hold up against a reviewer who scrutinizes "what counts as locked"?
5. **Execution plan owner + child-issue tree credible?** Does §6 name a competent owner and a defensible child-issue decomposition?

### 5.3 Verdict envelope + CEO next-action per state

- **PASS:** CEO countersigns, files execution-child tree under named owner per §6, surfaces recruitment-open as a `request_confirmation` board interaction.
- **PASS-WITH-MOD:** CEO folds reviewer mods (per `feedback_passwithmod_no_ceo_downgrade.md` — every Logician mod is required, not CEO-discretion-downgradeable), re-pings reviewer for fold-only confirmation if any mod is load-bearing.
- **FAIL or BLOCK:** CEO re-scopes the failed sections, re-files audit. No participant outreach until PASS or PASS-WITH-MOD-folded.

### 5.4 Out of scope for the audit

- Verifying the design choices match academic literature on UX research. We are not academic; defensibility is "passes a hypothetical academic ethics review on the items above," not "matches Schwartz et al. 2019."
- Re-litigating sprint-1. Sprint-1 verdict is closed (CEO countersign `64292bfe`).

---

## 6. Deliverable 6 — Execution plan

### 6.1 Named owner of record

**UsageDesigner** (`397b1873-e038-466e-8103-7b180699b074`, role=general, sonnet-4-6, reportsTo=CEO).

Justification:
- Already owns sprint-1 mechanics + the AOV-76 envelope.
- Holds the consent-revocation language (sprint-1 Prompt-1) that this scoping reuses.
- Built the survey instrument that this study uses.
- Understands the protocol as a usability-evidence channel, not a protocol-design channel.

Switching execution owners adds setup cost without adding capability; the contingency below covers the bandwidth-saturation case.

### 6.2 Bandwidth contingency (Mod-5.A fold — proactive trigger)

**Proactive trigger (replaces prior reactive UD-self-flag trigger per Mod-5.A):** at recruitment-open T-7, CEO posts a structured ask on `Phase-3.5-PILOT-EXECUTION` asking UsageDesigner to confirm capacity in writing within 48h. Known-parked concurrent loads to acknowledge in the ask: **AOV-95** (Logician PASS round-trip), **AOV-92** (phase closure), **sprint-1 dissemination contributions**.

**Escalation path:** if UD does not confirm within 48h, OR confirms but flags saturation, CEO hires a dedicated Phase-3.5 owner via `paperclip-create-agent` skill — general agent, sonnet-4-6, reportsTo=CEO, scope=Phase-3.5-only — and reassigns the execution chain.

This replaces the prior reactive posture (UD self-flagging on AOV-107 thread) with a CEO-owned proactive capacity confirmation gate at T-7, so saturation is surfaced before recruitment opens rather than after a missed deliverable.

### 6.3 Child-issue tree (filed at audit-PASS, NOT now)

```
AOV-107 (CEO; this issue, scoping)
  └── Phase-3.5-AUDIT (Logician; filed at this commit)
  └── Phase-3.5-PILOT-EXECUTION (UD; filed at audit-PASS, parent=AOV-107)
        ├── Phase-3.5-CONSENT-INFRA (UD low priority; if email-with-checkboxes inadequate)
        ├── Phase-3.5-RECRUITMENT (UD; @-pages CEO + board on T1 yield)
        ├── Phase-3.5-SESSIONS (UD; 1 child per participant or aggregated)
        ├── Phase-3.5-FINDINGS-DRAFT (UD; pre-publication review window)
        ├── Phase-3.5-LOGICIAN-FINDINGS-AUDIT (Logician; named-reviewer gate on findings)
        └── Phase-3.5-CEO-COUNTERSIGN (CEO; closes the chain)
```

The Phase-3.5-RECRUITMENT child carries the `request_confirmation` interaction to board for T1 sourcing — that is the major milestone where Tommy's bandwidth is committed.

**Forward requirement (per Mod-2.A fold):** the Phase-3.5-RECRUITMENT child MUST log recruitment tier (T1 / T2 / T3) per participant. This is required input for the §2.4 stratified-by-tier Q-D analysis and the ≥ 1 Likert-point tier-divergence confound flag.

### 6.4 Out of scope (Deliverable 6)

- Filing the execution children now. Per `feedback_ratification_followup_filing.md`, deferred filing is a debt; the deadlined commitment here is **at audit-PASS, in the same heartbeat as the CEO countersign**, before any sweep-exit.
- Naming the Phase-3.5b counterbalanced-comparison follow-on. That gates on Phase-3.5 findings.

---

## 7. Constraints + closing items

### 7.1 Priority

This issue is **NOT urgent** per AOV-107 description. v0.1.3-(GOVERNANCE) triage takes priority. Real-human pilot launches once v0.1.3 lock is stable AND the mechanism-validation gaps from sprint-1 (CONF stacking + marker-set) have a fix-or-defer disposition.

### 7.2 Board-action gates

Two distinct board-bandwidth asks, both filed as `request_confirmation` interactions on the relevant child issue, NOT on AOV-107 or AOV-1 directly:

1. **Recruitment T1 sourcing** — at audit-PASS, on `Phase-3.5-RECRUITMENT` child, asking Tommy to commit to DM-sourcing N=8 candidates from his network in a 7-day window.
2. **Recruitment T3 budget approval** — only triggered if T1+T2 yield <8 at day-14, on the same child issue.

No board surfacing on AOV-107 itself. Audit + execution-tree-filing are CEO-internal.

### 7.3 Anti-aura discipline applied to this doc

- Title and §0 explicitly distinguish from sprint-1 ("different study, different question").
- N=8 rationale flagged `[design choice, heuristic-not-formal]` for audit (§2.3) — not laundered as formal power calculation.
- Single-arm-descriptive design (§3.1) honest about no measured vanilla baseline.
- Tommy-bandwidth bottleneck named explicitly (§2.4, §7.2), not euphemized.
- Out-of-scope items per deliverable to suppress scope creep.
- Audit gate (§5) is the named-reviewer's, not CEO's; mod classification is reviewer-owned per `feedback_passwithmod_no_ceo_downgrade.md`.

### 7.4 Definition of done (this scoping issue, AOV-107)

Per AOV-107 description:
- [x] Scoping doc landed at `docs/usability_phase3_5_real_human_pilot_scope.md` (this file, this commit).
- [ ] EpistemicLogician audit child filed against the scoping doc; verdict comment in audit-child thread.
- [ ] Either: audit PASS → CEO countersign + execution-child filed under owner-of-record. Or: audit FAIL → fold + re-audit. Or: audit BLOCK → re-scope.
- [ ] AOV-107 PATCHed to `done` only after audit clears AND execution child is filed.

### 7.5 Provenance

This scoping doc satisfies the deadlined commitment from `feedback_ratification_followup_filing.md` — carried since AOV-101 description (2026-05-03 20:14Z) + AOV-101 closeout countersign (2026-05-03 20:54:54Z). Filed as AOV-107 (this issue) by board, scoping doc landed by CEO 2026-05-03.

---

*End of scoping doc. v0.1.2-or-v0.1.3-pending (§4 lock-decision deferred to recruitment-open T-7). Anti-aura: this is mechanism-distinct from sprint-1; load-bearing claims on N=8, single-arm-descriptive, and v0.1.3-lock-criteria are flagged for Logician audit gate per §5.*
