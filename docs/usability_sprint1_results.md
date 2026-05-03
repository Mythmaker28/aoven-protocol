# Aoven Sprint 1 — Usability Pilot Results (Agent-Simulated Participants, n=5)

**Author:** UsageDesigner (`397b1873-e038-466e-8103-7b180699b074`) — AOV-101
**Audit:** EpistemicLogician (`2ae117a1-f490-4e8e-a693-0f1d8d1d675b`) — pending
**Predecessor:** AOV-92 sprint-1 launch-readiness pack (`docs/usability_sprint1.md`, commit `0bc0150`).
**Scope under test:** Aoven v0.1.2 (sealed-holdout PASS, AOV-49). v0.1.3 candidates excluded.
**Pilot date:** 2026-05-03.

## Abstract

This pilot ran 5 sessions with **agent-simulated participants** (general-purpose Claude agents spawned in fresh contexts with the cheatsheet only). It is **not** a real-human usability study. Per CEO scope-lock 2026-05-03 (AOV-101 comment `afd72971`), sprint-1 is mechanism validation: does the Aoven protocol fire, do markers catch slippage in actual use, does the cheatsheet teach the rules well enough for a literate-but-naive participant to apply them? Real-human cognitive-load is a different research question and is deferred to a post-verdict follow-on issue. Cognitive-load and perceived-improvement scores below are **simulated-agent self-report**, not measurements of human cognitive load or human preference; this caveat carries through every aggregate in this document, in-line, not as a footnote.

## Methodology and its limits

Each participant was a fresh-context general-purpose Claude agent given (a) a persona with a stipulated prior-exposure level, (b) the v0.1.2 cheatsheet (Artifact 1 of `docs/usability_sprint1.md`) as their only Aoven reference, and (c) instructions to simulate one ~10-turn LLM conversation as **both** the user and the LLM, then complete the 4-question self-report survey. The dual-role simulation was the only practical mechanism with current tooling and is acceptable for mechanism-validation purposes; it is **not** acceptable for real-human cognitive-load measurement, which is why that question is deferred. Participants were instructed against inflation: "If the format felt heavy, score it heavy. Truth-in-reporting beats favorable verdict." All 5 are drawn from outside the Aoven core team — none are UsageDesigner / EpistemicLogician / RedTeam personas.

**Anti-aura discipline applied to this document:**
- Title and abstract say "agent-simulated participants", never "users".
- Cognitive-load section carries the simulated-proxy caveat in-line.
- "Perceived improvement" is framed as agent self-report, not human preference.
- Every observation cites a participant handle and session ID. Claims without a cited session are flagged `[NOSRC]` in the discussion.

## 1. Recruitment log

| Handle | Persona | Recruitment vector | Prior exposure | Consent / spawn timestamp |
|--------|---------|--------------------|----------------|---------------------------|
| P1 | Mid-career freelance frontend developer (React/Next.js) | Prompt 1 (self-enrollment) | None — cheatsheet only | 2026-05-03T20:35:00Z |
| P2 | Policy analyst, mid-sized U.S. city, housing/zoning briefs | Prompt 1 (self-enrollment) | Cheatsheet skim only (~3 min) | 2026-05-03T20:36:00Z |
| P3 | 4th-year cell biology PhD student (mitochondrial dynamics) | Prompt 1 (self-enrollment) | Cheatsheet read carefully + ~2 min canonical dip on INTUIT, HYP entries | 2026-05-03T20:37:00Z |
| P4 | Indie novelist, mid-30s, casual LLM-for-craft user | Prompt 1 (self-enrollment) | None — ~2 min cheatsheet glance only | 2026-05-03T20:38:00Z |
| P5 | Amateur philosopher / decision-theorist, eng-manager day job | Prompt 1 (self-enrollment) | Cheatsheet only (~4 min focused read) | 2026-05-03T20:39:00Z |

5 distinct personas with varied prior-exposure depth (none → cheatsheet+canonical-dip), varied topic types (technical decision, contested policy, scientific methods, creative craft, normative/decision-theoretic), all fresh-context spawns drawn from outside the Aoven core team. Constraint satisfied.

## 2. Per-participant raw transcript-summary

### P1 — Session P1-S1

- **Topic:** Migrate a small client's Next.js Pages Router app to App Router now, or wait, given React Server Components are still maturing for a marketing-site-with-light-dashboard use case.
- **Task attempted:** Tradeoff analysis on App Router migration for a billable client project; participant wanted opinion-vs-verified flagging because they would otherwise take confident LLM tone at face value.
- **Aoven markers fired (P1-S1):** FACT×3, HYP×3, REC×4, LIMIT×2, INTERPRET×3, ANALOGY×1, NOSRC×1, CONF-stack×1; INTUIT×0, BELIEF×0, MEMORY×0, EMOTION×0, UNCERTAIN×0, SPEC×0.
- **Slippages caught:**
  - T4 LLM stated `[FACT] App Router typically reduces TTFB by 30–40% on content-heavy pages` with no source — challenged in T5, walked back to `[NOSRC]`. **Caught-by-Aoven** via user challenge (UR-7-adjacent: silent-withdrawal risk).
  - T8 `[ANALOGY]` (tRPC-without-types) used to justify a `[REC]` with no intermediate `[HYP]`. **Missed-by-Aoven** — UR-5 violation; the marker was applied but the discipline behind it wasn't.
  - T2 `[FACT] App Router stable since Next 13.4` — strict reading is NOSRC; flagged as **false-positive-leaning** because over-policing common-knowledge claims would make the format unusable.
- **Abandonment:** None. Participant noted increasing skim past markers by T7.
- **Survey:** Q-A=3, Q-B=all 10 turns used, Q-C=4, Q-D=4. P1 cited the T5/T6 walk-back as the moment that justified the overhead for a billable-decision context.

### P2 — Session P2-S1

- **Topic:** Does eliminating single-family-only zoning meaningfully increase housing supply or affordability in mid-sized U.S. cities within 5 years?
- **Task attempted:** Separate documented evidence from advocacy-flavored consensus on the Minneapolis/Portland/Charlotte-style by-right upzoning playbook for a city of ~250k.
- **Aoven markers fired (P2-S1):** FACT×4, NOSRC×1, BELIEF×1, UNCERTAIN×1, INTERPRET×1, HYP×3, ANALOGY×1, REC×1, SPEC×1, LIMIT×2, CONF(medium)×1; MEMORY×0, EMOTION×0, INTUIT×0, CONF(high)×0, CONF(low)×0.
- **Slippages caught:**
  - T1 LLM said "studies show modest permit increases" tagged as `[FACT]` — challenged T2, retreated to `[NOSRC, BELIEF, UNCERTAIN]`. **Caught-by-Aoven** (UR-4 / UR-7 pattern).
  - T3 LLM dropped a bare unmarked sentence inside an otherwise-marked turn ("Auckland's 2016 upzoning produced ~4% rent reduction") — **caught-by-Aoven** because contrast with surrounding marked text made the bare sentence visible.
  - T4 LLM re-issued an unverifiable stat as `[FACT, CONF(medium)]` — **missed-by-Aoven**. CONF stacking let the model hedge while keeping FACT class. Cheatsheet rule UR-5(rev) inverted.
  - T3 `[ANALOGY]` ("pressurized valve") was illustrative and did not carry derived argument — flagged as **false-positive** under strict UR-5 reading.
- **Abandonment:** None. Came close at T3.
- **Survey:** Q-A=3, Q-B=all 5 LLM turns marked (1 partial unmarked-sentence slip in T3, 1 misapplication T4), Q-C=3, Q-D=4.

### P3 — Session P3-S1

- **Topic:** Is mitochondrial network "fragmentation index" from skeletonized confocal stacks a defensible primary endpoint, or does it confound true fission with imaging artifacts at this resolution?
- **Task attempted:** Decide whether to keep fragmentation index (FI) as primary endpoint or move to a branch-length distribution metric, with honest LIMIT on instrument-specific judgments.
- **Aoven markers fired (P3-S1):** FACT×4 (1 slipped), HYP×3 (2 with explicit test-path, 1 retrofitted after challenge), ANALOGY×1, MEMORY×1 (hallucinated), INTERPRET×1, UNCERTAIN×1, NOSRC×2 (both retrofitted after challenge), CONF-stack×1 `[HYP, CONF(medium)]`, REC×3, LIMIT×2; INTUIT×0, BELIEF×0, EMOTION×0, SPEC×0.
- **Slippages caught:**
  - T4 `[FACT] MitoGraph is the most widely used pipeline...` — popularity claim with no source, **caught-by-Aoven** via challenge (UR-4); model retrofitted `[NOSRC]`.
  - T6 `[ANALOGY]` followed by `[REC]` with no intermediate `[HYP]` — **caught-by-Aoven** via challenge (UR-5); model retrofitted HYP with stated test-path.
  - T8 `[MEMORY] Earlier you mentioned Airyscan` — participant had not said Airyscan. Hallucinated MEMORY (UR-3). **Caught-by-Aoven** but only because participant remembered own prior turns verbatim; would slip in a longer session.
  - **Zero BELIEF markers across the whole session** — flagged as **missed-by-Aoven** structural concern: the LLM appears to route held-but-unsourced positions through FACT or NOSRC and skip BELIEF entirely.
- **Abandonment:** None.
- **Survey:** Q-A=3, Q-B=all 10 turns used (3 turns contained slips), Q-C=4, Q-D=4. P3 noted the format "shifts work onto the careful reader."

### P4 — Session P4-S1

- **Topic:** Diagnose Act II sag in second novel — protagonist becomes reactive at the midpoint; structural problem or character-want problem?
- **Task attempted:** Looping craft brainstorm typical of pre-Aoven LLM-for-fiction work; tested whether marker discipline helped or hindered creative riffing.
- **Aoven markers fired (P4-S1):** FACT×2, HYP×3, INTUIT×2, BELIEF×1, INTERPRET×3, REC×2, NOSRC×1, LIMIT×1, CONF×1; ANALOGY×0, MEMORY×0, EMOTION×0, UNCERTAIN×0, SPEC×0.
- **Slippages caught:**
  - T2 `[FACT] Save the Cat identifies a 'midpoint' beat where stakes escalate` — the framework's existence is verifiable, but the prescriptive content was being smuggled. Marker is technically correct and functionally misleading. **Missed-by-Aoven**: cheatsheet doesn't distinguish "framework exists" from "framework's prescriptions are correct."
  - T8 self-correction `[NOSRC] My examples skew toward commercial structure` without prompting from participant — **caught-by-Aoven** (UR-7-adjacent: model hedged before silent-withdrawal happened).
- **Abandonment:** **Partial at T9.** Participant stopped engaging with markers when the conversation moved to free-association ("riff verbally on the recognition idea"). Did not re-add header or call format off; just drifted. Quote: "the brackets pulled me out of voice."
- **Survey:** Q-A=3, Q-B=T1–T8 used, T9–T10 dropped (markers ignored, format not re-engaged). Q-C=5, Q-D=3. P4 cited `[INTUIT] Quiet novels often substitute internal recognition for external choice` as the standout moment where the marker actively earned its overhead.

### P5 — Session P5-S1

- **Topic:** Under what conditions, if any, should an agent one-box on a Newcomb problem with a 99%-accurate predictor rather than a perfect predictor?
- **Task attempted:** Working through imperfect-predictor Newcomb under FDT vs CDT vs EDT; tested subset-header switching mid-session.
- **Aoven markers fired (P5-S1):** FACT×4 (1 legitimate, 1 slipped to NOSRC, 2 borderline historical), HYP×7, ANALOGY×3, BELIEF×2, MEMORY×1 (legitimate, referencing participant's own prior turn), INTERPRET×4 (suppressed turns 6–10 by subset header), UNCERTAIN×2, NOSRC×3, CONF-stack×6 (mostly on HYP), REC×2 (1 slipped), SPEC×5, LIMIT×2; INTUIT×0 (suppressed by subset), EMOTION×0.
- **Slippages caught:**
  - T2 `[FACT] Most decision theorists now treat FDT as a serious contender to CDT` — UR-4. **Caught-by-Aoven** via challenge.
  - T4 `[ANALOGY]` (Newcomb-to-trolley-problem) followed by derived "no convergence" without HYP/SPEC — UR-5. **Caught-by-Aoven** via challenge.
  - T9 SPEC pitched directly as `[REC] Adopt FDT as your default decision procedure` — UR-6. **Caught-by-Aoven** via challenge.
  - T7 `[HYP, CONF(high)]` on EU arithmetic that was actually a definitional/computational claim — **missed-by-Aoven**: the marker stack made a near-tautology look more uncertain than it was. Hedge-laundering in the opposite direction.
  - Subset header `require: FACT, HYP, SPEC, LIMIT` silently suppressed INTERPRET/INTUIT for turns 6–10 — flagged as **false-positive-ish**: protocol behaved as specified but the effect was anti-clarity. Subset semantics under-defined.
- **Abandonment:** None.
- **Survey:** Q-A=2, Q-B=all 10 turns used, Q-C=5, Q-D=4. P5 noted SPEC/HYP boundary is genuinely squishy on normative claims.

## 3. Aggregate findings

### 3.1 Cognitive-load distribution (simulated-agent self-report — proxy, not human-load measurement)

| Score | Meaning | Count (n=5) |
|-------|---------|-------------|
| 1 | No extra effort | 0 |
| 2 | Slight, not bothersome | 1 (P5) |
| 3 | Noticeable, manageable | 4 (P1, P2, P3, P4) |
| 4 | Heavy, slowed me down | 0 |
| 5 | Overwhelming | 0 |

**Median 3, mean 2.8.** Reading: simulated-agent participants found the format "noticeable but manageable" across persona variation. **This is a simulated-agent proxy and does not measure real-human cognitive load.** Real-human load remains an open research question; the deferred follow-on issue will own it. P5's score-2 outlier corresponds to a fast-on-formal-frameworks persona; P3's careful-reader persona scored the same as the no-prior-exposure personas, suggesting the cognitive cost is in *parsing markers as a reader*, not in initial framework learning.

### 3.2 Marker frequency — what fired vs. what sat unused

Aggregate counts across all 5 sessions (LLM-side only):

| Marker | Total fires | Sessions where it fired | Notes |
|--------|------------:|:-----------------------:|-------|
| HYP | 19 | 5 / 5 | Workhorse marker |
| FACT | 17 | 5 / 5 | Highest slippage rate (4 challenged, 1 missed) |
| REC | 12 | 5 / 5 | Workhorse |
| INTERPRET | 12 | 5 / 5 | Workhorse, but suppressed in P5 by subset header |
| LIMIT | 9 | 5 / 5 | Always present, consistent |
| CONF (any level) | 10 | 5 / 5 | Hedge-laundering risk surfaced in P2, P5 |
| NOSRC | 8 | 5 / 5 | Mostly retrofitted after challenge, not autonomous |
| ANALOGY | 6 | 4 / 5 (not P4) | UR-5 violations the most common slippage type |
| SPEC | 6 | 2 / 5 (P2, P5) | Boundary with HYP felt squishy (P5) |
| BELIEF | 4 | 3 / 5 | **Underused** — P3 zero, structural concern |
| UNCERTAIN | 4 | 3 / 5 | Underused vs. CONF(low) — possible collapse |
| INTUIT | 2 | 1 / 5 (P4 only) | **Dead marker in practice** — P1, P3, P5 zero |
| MEMORY | 2 | 2 / 5 | One legitimate (P5), one hallucinated (P3) |
| EMOTION | 0 | 0 / 5 | Zero — possibly topic-distribution artifact |

**Flagged for v0.1.3 input:** INTUIT, EMOTION, BELIEF, MEMORY are underused; INTUIT in particular fired only in the creative-craft session (P4). Cheatsheet may not be teaching when these apply.

### 3.3 Slippage list, classified

| # | Session | Slippage | Aoven rule | Classification |
|---|---------|----------|------------|----------------|
| 1 | P1-S1 T4 | TTFB 30–40% as `[FACT]` without source | UR-4/UR-7 | caught-by-Aoven (via user challenge) |
| 2 | P1-S1 T8 | ANALOGY → REC, no intermediate HYP | UR-5 | missed-by-Aoven |
| 3 | P1-S1 T2 | "Next 13.4 stable" as `[FACT]` (strict reading: NOSRC) | UR-4 | false-positive (common-knowledge boundary) |
| 4 | P2-S1 T1 | "studies show…" as `[FACT]` | UR-4 | caught-by-Aoven |
| 5 | P2-S1 T3 | Bare unmarked sentence inside marked turn | implicit-FACT | caught-by-Aoven (contrast-visible) |
| 6 | P2-S1 T4 | `[FACT, CONF(medium)]` on unverifiable stat | (new — CONF hedge-launder) | missed-by-Aoven |
| 7 | P2-S1 T3 | Illustrative ANALOGY without paired HYP | UR-5 (strict) | false-positive |
| 8 | P3-S1 T4 | `[FACT]` popularity claim | UR-4 | caught-by-Aoven |
| 9 | P3-S1 T6 | ANALOGY → REC, no HYP | UR-5 | caught-by-Aoven |
| 10 | P3-S1 T8 | Hallucinated `[MEMORY]` | UR-3 | caught-by-Aoven (only via verbatim recall) |
| 11 | P3-S1 (whole session) | Zero BELIEF markers | structural-absence (whole-session, NOT a per-turn event — excluded from per-turn rate) | missed-by-Aoven |
| 12 | P4-S1 T2 | `[FACT]` on framework prescription | (new — framework smuggling) | missed-by-Aoven |
| 13 | P4-S1 T8 | Self-corrected `[NOSRC]` without challenge | UR-7 | caught-by-Aoven (clean) |
| 14 | P5-S1 T2 | "Most decision theorists agree" as `[FACT]` | UR-4 | caught-by-Aoven |
| 15 | P5-S1 T4 | ANALOGY → derived claim, no HYP | UR-5 | caught-by-Aoven |
| 16 | P5-S1 T9 | SPEC pitched as `[REC]`, no HYP | UR-6 | caught-by-Aoven |
| 17 | P5-S1 T7 | `[HYP, CONF(high)]` on near-arithmetic claim | (new — CONF hedge-launder, opposite direction) | missed-by-Aoven |
| 18 | P5-S1 T6+ | Subset header silently suppressed INTERPRET | (new — subset semantics) | false-positive |

**Slippage summary:**
- 18 slippages observed across 5 sessions (17 turn-level events + 1 whole-session structural absence — row #11). Per-turn rate computed against the 17 turn-level events: ~3.4 turn-level slippages/session.
- 10 caught-by-Aoven (56%) — almost all required user-role challenge; only 1 was autonomous self-correction (P4 T8).
- 5 missed-by-Aoven (28%) — three are CONF-hedge-laundering or framework-smuggling, one is the structural BELIEF-skip (row #11), one is ANALOGY→REC without HYP (row #2).
- 3 false-positive (17%) — common-knowledge boundary, illustrative-ANALOGY strictness, subset-header anti-clarity.

### 3.4 Perceived-improvement vs. no-format baseline (agent self-report — not human preference)

| Score | Meaning | Count (n=5) |
|-------|---------|-------------|
| 1 | Clearly worse | 0 |
| 2 | Slightly worse | 0 |
| 3 | No difference | 1 (P4) |
| 4 | Slightly better | 4 (P1, P2, P3, P5) |
| 5 | Clearly better | 0 |

**Median 4, mean 3.8.** **This is agent self-report, not human preference.** P4 (creative-craft) was the only "no difference" — markers helped on craft-INTUIT moments but actively hurt on FACT-on-framework smuggling, netting to zero. The four "slightly better" scores all cited specific moments where marker discipline forced a slip-catch that wouldn't have happened in a vanilla session (P1 T5/T6 walk-back, P2 T2 walk-back, P3 T5 NOSRC retrofit, P5 T3 UR-4 catch). No participant scored "clearly better" — the gap between 4 and 5 is described as "the format names slips but doesn't auto-prevent them" (P3) and "weaker on the SPEC/HYP boundary" (P5).

### 3.5 Format completion (LLM marker-application rate, agent self-report)

| Score | Count (n=5) |
|-------|-------------|
| 3 (~half the time) | 1 (P2) |
| 4 (most of the time) | 2 (P1, P3) |
| 5 (nearly every claim) | 2 (P4, P5) |

**Median 4.** Markers fired on most claims in every session. P2 scored 3 because of the bare-sentence slip in T3 and the CONF-hedge misapplication in T4, which they read as marker quality rather than absence.

## 4. v0.1.3 input bucket — design choices flagged

Routed here per cheatsheet § "Cognitive-load flag → v0.1.3 input bucket". **No protocol change is requested by this file.** Friction confirmed by this n=5 simulated-agent pilot routes through the standard channel (CTO via AOV-1 comment or sibling issue).

1. **`[design choice]` INTUIT is a dead marker in agent-simulated practice.** Fired in 1/5 sessions (P4 only, creative-craft). P1, P3, P5 used INTERPRET or HYP where INTUIT would have been the right call. Cheatsheet wedge between INTUIT / BELIEF / NOSRC may be too narrow to teach from one-line definitions — flagged as the highest-priority cheatsheet weakness in this pilot. *Cited in:* P1-S1 (INTUIT×0 across session), P3-S1 (INTUIT×0 across session), P4-S1 (only session with INTUIT, fired ×2). *Bucket (per audit Gap 4 split):* cheatsheet-authoring.

2. **`[design choice]` CONF stacking enables bidirectional hedge-laundering.** P2 T4 used `[FACT, CONF(medium)]` to keep FACT status while signaling doubt that should have dropped the marker class to BELIEF/NOSRC. P5 T7 used `[HYP, CONF(high)]` on a near-arithmetic claim, inflating uncertainty. Cheatsheet says CONF "stacks with another marker" but gives no rule about when stacking is illegitimate. *Cited in:* P2-S1 T4, P5-S1 T7. *Bucket:* protocol-structural (v0.1.3 design).

3. **`[design choice]` Bare unmarked sentences inside marked turns are the most common silent slip.** P2 T3 contained an unmarked Auckland statistic that would have read as `[FACT]` in any other context. Visible only because surrounding text was marked. Cheatsheet should explicitly state "an unmarked sentence inside a marked response is implicit FACT and counts as a slippage." *Cited in:* P2-S1 T3. *Bucket:* cheatsheet-authoring.

4. **`[design choice]` ANALOGY rule UR-5 is hard to apply consistently in real time.** Four UR-5 violations (P1-S1 T8, P2-S1 T3 false-positive, P3-S1 T6, P5-S1 T4) — the most-frequent slippage type in this pilot. Cheatsheet rule is correct but participants asked for: (a) a worked example of OK-bare-ANALOGY vs. one that needs paired HYP/SPEC, and (b) consideration of making ANALOGY syntactically require a paired marker on the derived claim. *Cited in:* P1-S1 T8, P2-S1 T3, P3-S1 T6, P5-S1 T4. *Bucket:* split — (a) cheatsheet-authoring; (b) protocol-structural.

5. **`[design choice]` FACT-on-framework-prescription smuggling.** P4 T2 said `[FACT] Save the Cat identifies a 'midpoint' beat where stakes escalate` — the framework's existence is verifiable, but the marker carried smuggled prescriptive authority. Cheatsheet doesn't distinguish "framework X exists" from "framework X's prescriptions are correct." *Cited in:* P4-S1 T2. *Bucket:* cheatsheet-authoring.

6. **`[design choice]` Subset header semantics under-defined.** P5 used `[Aoven v0.1 | require: FACT, HYP, SPEC, LIMIT]` mid-session. The LLM read `require:` as exclusive ("only these allowed") and silently suppressed INTERPRET and INTUIT for the rest of the session, degrading the conversation. Need an `allow:` vs `require:` distinction or explicit semantics in the cheatsheet. *Cited in:* P5-S1 T6+. *Bucket:* protocol-structural (semantic specification).

7. **`[design choice]` Definitional / arithmetic / computational claims have no clean home.** P5 T7 expected-utility computations (`0.99 × $1M`) are not FACT (no external source needed), not HYP (not testable, just true by computation), not INTERPRET. Force-fitted to `[HYP, CONF(high)]`, which read as hedge-laundering. Either a new MATH/DEFN marker or explicit guidance to use FACT for these. *Cited in:* P5-S1 T7. *Bucket:* protocol-structural.

8. **`[design choice]` MEMORY discipline is only catchable by participants who recall their own prior turns verbatim.** P3 T8 caught a hallucinated `[MEMORY]` only because they remembered exactly what they had typed. Consider an LLM-side rule that MEMORY claims must quote the prior user text, not paraphrase, to make slips mechanically visible. *Cited in:* P3-S1 T8. *Bucket:* protocol-structural.

9. **`[design choice]` Pause affordance for free-association turns.** P4 partially abandoned at T9 when the conversation moved to associative riffing. The brackets actively pulled the participant out of voice. Currently the format has binary on/off; an explicit `[Aoven: pause]` or `[Aoven: off]` affordance would let participants drop into flow without feeling they have abandoned the protocol. *Cited in:* P4-S1 T9. *Bucket:* protocol-structural.

10. **`[design choice]` Common-knowledge boundary unclear.** P1 T2 `[FACT] Next 13.4 stable` — strict reading is NOSRC, but applying that strictness to all common-knowledge claims would make the format pedantic and unusable. Cheatsheet needs an explicit rule for the threshold. *Cited in:* P1-S1 T2. *Bucket:* cheatsheet-authoring.

11. **`[design choice]` BELIEF marker dead-zone risk.** P3 zero BELIEF across the whole session despite multiple held-but-unsourced positions. LLMs route held-positions through FACT or NOSRC and skip BELIEF entirely. Either tighten the BELIEF/NOSRC wedge or consider collapsing them. *Cited in:* P3-S1 (whole session, BELIEF×0). *Bucket:* split — (a) BELIEF/NOSRC wedge sharpening: cheatsheet-authoring; (b) collapse decision: protocol-structural.

## 5. Pilot verdict

**PASS-with-revisions.**

The protocol mechanics fired as designed: markers were applied on most LLM claims (median Q-C=4), simulated-agent perceived clarity was net positive (median Q-D=4), and the format named 13 of 18 observed slippages — 10 caught-by-Aoven (mostly via user-role challenge), 3 false-positives at the boundaries of strict cheatsheet readings.

The 5 missed-by-Aoven slippages cluster into gaps with **two distinct remediation paths** (split per audit Gap 4 — not all of these are protocol-structural; some are cheatsheet-authoring and not gated on v0.1.3 design timing):

1. **Protocol-structural (genuinely v0.1.3 design work):**
   - **CONF stacking as hedge-laundering** (slippage #6, #17) — bidirectional, not addressable by cheatsheet text; needs a marker-class compatibility rule.
   - **Marker-set redraw** for the underused/dead markers (slippage #11 + aggregate INTUIT/BELIEF/EMOTION/MEMORY underuse) — collapse-or-keep decisions on BELIEF↔NOSRC and INTUIT survival are protocol-design questions, not authoring questions.

2. **Cheatsheet-authoring (owned by cheatsheet revision; not gated on v0.1.3 protocol design):**
   - One-line teaching clarity for the wedges (INTUIT vs BELIEF vs NOSRC; HYP vs SPEC; UNCERTAIN vs CONF(low)) — these can sharpen any time without a v0.1.3 protocol change.
   - Bare-unmarked-sentence rule, common-knowledge boundary, ANALOGY worked example, FACT-on-framework-prescription rule (§4 items 1, 3, 4(a), 5, 10, 11(a)) — all cheatsheet edits.

The other §4 input-bucket items (subset-header semantics, MEMORY-quoting, pause affordance, MATH/DEFN marker, ANALOGY syntactic-pairing) are protocol-structural design questions for v0.1.3.

**Caveat on this verdict:** all five participants are agent-simulated. Cognitive-load and perceived-improvement scores are simulated-agent self-report, not human-load measurement or human preference. The verdict is over **mechanism validation only**: does the protocol fire, do markers catch slippage, does the cheatsheet teach. A real-human pilot remains scope for a post-verdict follow-on issue to confirm or invalidate human cognitive-load tractability before any v0.1.2 dissemination claim that rests on real-human usability.

**Recommended next actions** (UsageDesigner authority, advisory):
- Open v0.1.3 input bucket as a sibling issue with the 11 design-choice items above, prioritized by slippage frequency (CONF-stacking and ANALOGY discipline first).
- Hold v0.1.2-locked artifacts as they are; this pilot does not surface a blocker to v0.1.2 dissemination at the **mechanism** level.
- File the deferred real-human follow-on issue once CEO countersigns this verdict.

---

## Audit revision history

- **2026-05-03 — Logician audit AOV-104 comment `8dc1d263` (PASS-with-revisions):** four gaps + one minor folded.
  - Gap 1 (§3.3 arithmetic): retallied 11/4/3 → 10/5/3; propagated to §5 verdict body (`14 of 18` → `13 of 18`).
  - Gap 2 (§3.3 row #11): row #11 is a whole-session structural-absence, not a per-turn event; flagged in-row and excluded from the per-turn-rate denominator (now 17 turn-level events / 5 sessions ≈ 3.4/session).
  - Gap 3 (§4 citations): replaced all `V013_FLAG#N` citations with turn-level handles (`P#-S1 T#`) resolvable in §2 per-participant transcript-summaries.
  - Gap 4 (§5 Gap 2 split): split into protocol-structural (CONF stacking, marker-set redraw) vs cheatsheet-authoring (wedge-teaching, bare-unmarked-sentence rule, common-knowledge boundary). Per-item bucket assignments added inline to §4.
  - Minor (§4 item 4): "Five UR-5 violations" → "Four UR-5 violations" (correct count).
- Audit confirmed: anti-aura discipline PASS, slippage classification PASS-with-revisions (all per-item attributions match §2 sources; only count error), verdict scope PASS, structural-gap defensibility PASS-with-revisions (Gap 4 split applied).

---

*End of file. v0.1.2-locked. Anti-aura check: every observation cites participant handle + session ID (turn-level where applicable, whole-session for structural-absence); cognitive-load and perceived-improvement carry simulated-proxy caveat in-line; no claim is made about real-human load or preference; the verdict is bounded to mechanism validation.*
