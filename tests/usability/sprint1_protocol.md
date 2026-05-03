# Sprint 1 Usability Pilot Protocol — Aoven v0.1.2

**Author:** UsageDesigner (`397b1873-e038-466e-8103-7b180699b074`)  
**Date:** 2026-05-03  
**Protocol version:** 1.0  
**Protocol covers:** Aoven v0.1.2 ONLY (sealed-holdout PASS confirmed, AOV-49)  
**Out of scope:** v0.1.3 candidates, R1 marker-syntax compression, rubric/scoring work, non-Western framing pilots

---

## 1. Purpose

Test whether the v0.1.2-locked Aoven protocol works for **real users in real conversations** — not in lab A/B grading. Goal is usability evidence, not protocol modification. All friction findings are routed; none are actioned by this role directly.

---

## 2. Participant Criteria

### Inclusion
- Technically literate (can read/write structured text; understands concept of "annotation")
- Has no prior Aoven exposure (not an author, not a rater, not on the project team)
- Willing to spend ~45 minutes on one guided LLM session + post-session survey
- Comfortable using an LLM directly (any platform: Claude, ChatGPT, Gemini, or similar)

### Exclusion
- Any person who has read AOVEN_PROTOCOL_v0.1.md or participated in AOV project work
- Minors
- Persons unable to provide written consent in English or French

### Target n
5 participants (n=5). If recruitment stalls at < 3 by deadline, partial-with-explanation report filed.

### Bias declaration (standing)
Any participant with incidental Aoven exposure discovered after session completion will be flagged in the findings report with exposure type, session number, and assessment of contamination severity.

---

## 3. What Participants Receive (Pre-Session Package)

Participants receive exactly two items — no additional coaching or training:

1. **The v0.1.2 prompt format** (minimal form): `[Aoven v0.1]` header, with marker subset invocation syntax (`require:`) explained in one sentence.
2. **14-marker reference card** (verbatim from AOVEN_PROTOCOL_v0.1.md marker table): marker name, definition, "Does NOT mean", one example per marker.

They do NOT receive: the decision log, the anti-slippage table, the usage rules, any rubric or scoring criteria.

---

## 4. Session Script

### Pre-session (5 min)
1. Researcher (UsageDesigner) sends pre-session package.
2. Participant confirms receipt and asks any format-clarification questions (answered without steering toward correct use).
3. Participant chooses their own topic for the LLM conversation. Topic must be something they genuinely want to discuss — not assigned.

### Session (30 min max)
4. Participant conducts one LLM conversation of approximately **10 messages** (turns) using the Aoven v0.1.2 format.
5. Participant shares the full conversation transcript (copy-paste or screenshot) at session end.
6. If participant abandons the format mid-conversation, they note the turn number and reason in free text (see Measure B below). They continue the conversation in plain language — no forced restart.

### Post-session survey (10 min)
Participant answers the four measures below before seeing any analysis.

---

## 5. Measures

### Measure A — Cognitive Load (5-point self-report)
> "How much extra mental effort did using the Aoven format require, compared to your normal LLM use?"

Scale:
- 1 = No extra effort — felt natural
- 2 = Slightly more effort but not bothersome
- 3 = Noticeable effort, manageable
- 4 = Heavy effort, slowed me down significantly
- 5 = Overwhelming — I couldn't focus on the content

### Measure B — Abandonment (binary + free text per turn)
From the shared transcript, participant marks each turn:
- `used` = Aoven format applied (partial or full)
- `dropped` = Aoven format not applied

Plus one free-text field: "If you dropped the format, at what turn, and why?"

Binary flag: did participant drop the format entirely before message 8? (yes/no)

### Measure C — Format Completion Rate (per-turn, coded by UsageDesigner)
From the transcript, for each turn marked `used`:
- `full` = response structure filled (at least one marker per claim, LIMIT block if applicable)
- `partial` = some markers present, some claims un-marked
- `skipped` = header present but no markers applied

Aggregate: % full / partial / skipped across all turns where format was attempted.

### Measure D — Perceived Improvement vs. No-Format Baseline (5-point self-report)
> "Compared to a normal LLM conversation on the same topic (without the Aoven format), how much better or worse did the Aoven response feel in terms of epistemic clarity — knowing what the LLM was certain vs. uncertain about?"

Scale:
- 1 = Clearly worse — the format obscured or distracted
- 2 = Slightly worse
- 3 = No difference
- 4 = Slightly better — I could tell what the LLM was hedging
- 5 = Clearly better — much clearer epistemic picture

---

## 6. Report Template

The findings report (`sprint1_findings.md`) will include:

### 6.1 Participant Summary Table
| Participant | Prior Aoven exposure | Cognitive load (A) | Abandoned? (B) | Drop turn | Completion rate (C) | Perceived improvement (D) |
|---|---|---|---|---|---|---|

### 6.2 Usability Heatmap (per marker)
For each of the 14 markers:
- How often it appeared in transcripts
- How often it was correctly applied (UsageDesigner judgment)
- How often it was ignored when applicable
- How often it was misapplied

Rendered as a table with columns: marker / frequency / correct / ignored / misused / aura-risk flag

### 6.3 Abandonment Narrative
Free-text synthesis of why participants dropped the format, with turn-level data. Includes the "human story" — what they were trying to say or do when the format broke down.

### 6.4 Friction-Points List (partitioned)

**(a) v0.1.3 patch queue** — friction addressable in the next protocol version. Each item: description, evidence (participant count + quote), proposed route (comment on AOV-1 or new sibling issue tagged `[CTO]`).

**(b) Phase 4+ backlog** — friction requiring deeper redesign or out-of-scope work. Each item: description, evidence, filed as backlog issue with `phase4` in title.

### 6.5 Author-Bias Declaration
Explicit statement for each participant: (a) confirmed no prior Aoven exposure, OR (b) discovered exposure type and severity.

---

## 7. Data Handling

- Transcripts are stored locally in the workspace, not committed to the public repo.
- Participant identifiers are anonymized (P1–P5) in all filed documents.
- No personally identifying information is committed to the repo.
- Participants consent in writing (email or equivalent) before session; consent records are kept locally and not committed.
- **Consent revocation:** Participants may revoke consent post-session and request transcript deletion. If they do, the session is dropped from the report. The findings report will note the anonymous count of revocations (e.g., "1 session dropped post-revocation") without identifying the participant.

---

## 8. Definition of Done

- [ ] n=5 sessions completed (or partial-with-explanation if recruitment stalls)
- [ ] All four measures collected per participant
- [ ] `sprint1_findings.md` filed with all four deliverables
- [ ] Friction-points (a) routed to CTO via AOV-1 comment or sibling issue
- [ ] Friction-points (b) filed as backlog issues with `phase4` tag
- [ ] Author-bias declaration included in findings

---

## 9. Out of Scope (restated)

- v0.1.3 candidate testing (R1 marker-syntax compression, single-level CONF) — wait for AOV-37/72
- Rubric or scoring work
- Non-Western framing pilots
- Modifying AOVEN_PROTOCOL_v0.1.md
