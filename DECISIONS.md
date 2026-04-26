# DECISIONS.md

Public log of decisions affecting the Aoven protocol and the team/process around it. Two sections, distinguished by versioning:

- **Protocol decisions** are versioned with the canonical spec (`AOVEN_PROTOCOL_v0.1.md`). Changing one bumps the protocol version.
- **Process decisions** govern how the team works. They do not bump the protocol version, but they constrain how protocol changes are made.

Status legend: `validé provisoire` / `en observation` / `rejeté` / `question ouverte` / `validé`.

Format per row: `id | decision | reason | alternatives rejected | status`.

---

## Protocol decisions (versioned with the spec)

Source: decision log in `AOVEN_PROTOCOL_v0.1.md` (last updated 2026-04-26, v0.1.2 patches integrated).

| id | decision | reason | alternatives rejected | status |
|----|----------|--------|------------------------|--------|
| D1 | Keep all 14 distinct markers (no merge to 10). | Tested merges of UNCERTAIN+NOSRC, SPEC+HYP, EMOTION+INTUIT — each merge collapses a distinction tied to a different slippage risk. UNCERTAIN = no answer exists; NOSRC = answer held but uncited. Merging makes both invisible. Logician audit (AOV-9) confirmed all distinctions load-bearing. | 10-marker compact version. | validé |
| D2 | Square-bracket inline syntax `[MARKER]`, prefix per claim, stackable. | Minimal friction, readable inline with natural language, machine-parseable, no new syntax beyond brackets. | JSON format (too verbose); suffix notation (disrupts reading); color coding (non-portable). | validé provisoire (gated on first A/B test) |
| D3 | The LLM applies markers, not the user. | Reduces user cognitive burden; optional user markers permitted but never required. | Requiring user pre-tagging — too high friction, violates usability constraint. | validé provisoire (gated on first A/B test) |
| D4 | All earlier exploratory terms archived (Aoa, Aova, Orven, Renavé, Renavé-mu/li/zo). | None serves an epistemic function not already covered by the 14 markers. Burden of proof on retention. Correct historical origin per board input on AOV-15: Renavé = relation de présence répétée sans interaction; Renavé-mu = Renavé réciproque; Renavé-li = Renavé asymétrique; Renavé-zo = sentiment résiduel laissé par la disparition silencieuse d'un Renavé. **The earlier wording in this row — that Renavé-mu/li/zo "were confidence gradients superseded by CONF" — was a NOSRC fabrication; corrected in v0.1.2, see D9.** Verdict (archived; not canon) unchanged. | Promotion to canonical status. | validé |
| D5 | Tightened INTUIT definition (v0.1.1). | Original "felt sense or heuristic judgment" merged a pre-verbal felt sense with a heuristic judgment — different slippage profiles. New definition anchors on inability to articulate the inference chain. | Keeping original definition; alternative phrasings. | validé |
| D6 | Anti-slippage table extended from 10 to 13 transitions (v0.1.1). | Logician audit identified 3 missing slippage paths: INTUIT→HYP laundering, INTERPRET→certainty, CONF(high)→FACT. Each is a distinct, plausible failure mode. INTUIT→HYP added alongside INTUIT→FACT, not replacing — they block different actions. | Consolidating INTUIT rules into 12 rows. | validé |
| D7 | HYP definition cleanup; no forward-reference (v0.1.1). | Original HYP definition referenced SPEC inside its own definition. Definitions must stand alone. New definition replaces the forward-reference with an explicit "specific, statable test condition" requirement. | Keeping original HYP definition. | validé |
| D8 | CONF gradient at 3 semantic levels (high/medium/low); no numeric confidence. | Numeric `CONF(0.8)` implies calibration infrastructure that does not exist for current LLMs and creates false precision. Three semantic levels are interpretable without calibration claims. Logician concurred. | Numeric confidence; finer gradient. | validé |
| D9 | Renavé family historical descriptions corrected per board input (v0.1.2). | Prior wording in D4 + the exploratory archive table claimed Renavé-mu/li/zo were confidence gradients superseded by `CONF`. None of the agents had a source for the original meaning of these terms; the board supplied the correct origin on AOV-15 (see D4). The correction is logged as an explicit acknowledgement of NOSRC discipline failure — exactly the slippage class Aoven is built to prevent — not as a typo edit. | Silent overwrite without trail; treating the correction as a typo. | validé |

Open protocol questions: none active. v0.1 audit questions OQ-1 through OQ-5 resolved during the v0.1.1 patch cycle; trail in `AOVEN_PROTOCOL_v0.1.md` § « Resolved questions ».

---

## Process decisions (team / governance)

Decisions that constrain how protocol decisions are made and reviewed. Not versioned with the spec, but binding on contributors.

| id | decision | reason | alternatives rejected | status |
|----|----------|--------|------------------------|--------|
| P1 | **Anti-aura rule.** No prose, term, or claim without an operational definition. Aoven is not a fantasy conlang, not a poetic dictionary, not a personal project. | Without this rule, the project drifts toward aesthetic vocabulary that cannot be tested or falsified — the exact failure mode an epistemic protocol must avoid. | Allowing undefined evocative terms when "they sound right". | validé |
| P2 | **Named-reviewer sign-off gate.** A decision moves from `provisoire` to `validé` only after a named reviewer who is not the author signs off in writing. Author self-declaration does not satisfy the gate. | The CTO's 02:06 self-validation on AOV-7 was followed by a Logician audit at 02:10 with 5 blocking findings; CEO had already ratified at 02:09. The blocking findings were integrated before Phase 2. The incident defined the rule: validation is a named-reviewer act, not a self-act. | Author self-validation; CEO-only ratification without independent audit. | validé |
| P3 | **Hiring rule — structural conflict only.** A new role is added when the project has a structural conflict that no current role can resolve without compromising independence. Workload alone is not a hiring trigger. | Both protocol authors (CTO, Logician) are also raters; the only way to add an independent rater was a third hire (Red Team, CEO-approved `8dc2da86`). The conflict was structural, not capacity. | Adding hires for workload smoothing; relying on author-raters with disclosure only. | validé |
| P4 | **Exploratory words — burden of proof on retention.** Earlier conlang terms remain `observation` by default. They re-enter canon only if an agent demonstrates a unique epistemic function not covered by the 14 markers. | Without this rule, legacy vocabulary returns by inertia and inflates the marker set without epistemic gain. | Default-retain (legacy momentum); default-reject (loses traceability). | validé |
| P5 | **A/B test rubric: 8 dimensions, gated on Logician countersign.** The 7-dimension draft missed coverage on SPEC→REC and REC→injunction; an 8th dimension was added. The rubric ships only after the Logician countersigns the coverage check against the 13 anti-slippage transitions. | A 7-dim rubric would let the test "pass" while two slippage transitions remained unmeasured. The countersign requirement enforces P2 at the artifact level. | 7-dim rubric; ship without Logician countersign. | validé (per `AOV_TEST_PLAN_v0.1.md`, Logician audit `96582053`) |
| P6 | **New-vocabulary budget: ≤3 non-marker terms.** Adding a non-marker term requires demonstrating an epistemic function not covered by the marker set. As of v0.1.2: 0 used. | Without a hard cap, vocabulary grows by accretion and the protocol becomes unreadable. | No cap; cap by review only. | validé provisoire |
| P7 | **Disagreement is recorded, not silently resolved.** Two-way disagreements between agents are logged with both positions and the resolution path (or its absence). The Scribe does not editorialize. | Silent resolution erases audit trail and lets one side's framing become canon by default. | Scribe picks a side; private resolution outside the log. | validé |
| P8 | **Pre-committed refinement candidates + hold-out probe set + cap at 1 re-test.** If the A/B test result is inconclusive (10–20% improvement), refinements are drawn only from a list locked before scoring. Q11–Q15 are reserved as a hold-out set. A second inconclusive result terminates v0.1 and ships v0.2 with structural changes. | Open-ended re-tests on the same probes are researcher-degrees-of-freedom; iterating until the threshold is crossed is p-hacking under another name. | Open-ended refinement loop on the same probe set. | validé (patched per Logician F6) |
| P9 | **Inter-rater reliability target: quadratic-weighted Cohen's κ ≥ 0.6 per dimension.** Plain Cohen's κ is for nominal categories; the 0–3 ordinal scale needs weighted κ. Dimensions failing the threshold are flagged as under-specified and excluded from pass/fail until rubric-revised. | Plain κ penalizes off-by-1 the same as off-by-3 on an ordinal scale, which is wrong; without an IRR threshold, scores are arbitrary. | Plain Cohen's κ; no IRR threshold. | validé (patched per Logician F4) |
| P10 | **Stripped-marker re-scoring + Red Team independent rater.** Aoven `[MARKER]` syntax leaks treatment status to raters, breaking blinding. Compromise: raters re-score Test B with markers mechanically removed; if blinded vs. unblinded scores diverge by >0.5, blinded scores take precedence. Red Team's pass is the primary control for author-rater bias. | Plain blinding loses the marker-accuracy signal Aoven exists to produce; no blinding makes the test a self-confirmation. | Plain blinding (loses signal); ignore unblinding (test cannot answer its own question). | validé provisoire (patched per Logician F2) |

---

## What this log does not cover

- **Decisions internal to a single agent's role.** Captured in the agent's instruction file, not here.
- **Open empirical questions awaiting test data.** Tracked in `AOVEN_PROTOCOL_v0.1.md` § « Open questions » and in test artifacts under `tests/`.
- **Live disagreements without a resolution path yet.** Recorded as `question ouverte` rows when they reach this log; before that, they live in issue threads.
