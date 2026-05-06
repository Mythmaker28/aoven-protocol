# Aoven Phase-3.5 — Recruitment Log Schema v0.1

**Author:** UsageDesigner (`397b1873-e038-466e-8103-7b180699b074`) — AOV-152
**Authorization:** CEO comment `adbf1c1c` (Route A, 2026-05-06 00:04Z) — re-authorized logging-schema work as independent of participant-outreach hard-gate.
**Sign-off route:** CEO countersign as named-reviewer (Mod-2.A is reviewer-required per `feedback_passwithmod_no_ceo_downgrade.md`); not a board-gate.
**Status:** v0.1 — pre-countersign.
**Source artifact (binding):** `docs/usability_phase3_5_real_human_pilot_scope.md` @ `8dde742` on `origin/main`.
**Mod traceability:** AOV-119 Mod-2.A (BLOCKING forward requirement).

---

## 0. Purpose

Operationalizes the AOV-119 Mod-2.A forward requirement: every Phase-3.5 participant carries a deterministic recruitment-tier label, recorded at contact time, that flows through to the §2.4 stratified-by-tier Q-D analysis and the ≥1-Likert-point tier-divergence confound flag in the findings report.

Anti-aura: the schema is a structural defense against post-hoc tier inference. Tier MUST be recorded at the moment a participant enters the funnel; no analysis-time backfilling.

---

## 1. Storage

- **Path:** `tests/usability/phase3_5/recruitment_log.csv` (private; never committed to public repo per scoping doc §1.2 retention policy on raw participant data).
- **Format:** UTF-8 CSV, RFC 4180-compliant, comma-delimited, double-quote field wrapping where any field contains a comma / newline / double-quote.
- **Header row:** required; column names verbatim per §3.
- **Per-row scope:** one row per **contact** (not per participant). A pre-screened-and-rejected contact is a row; a consented-and-scheduled participant is a row. Filter by `consent_status` and `exclusion_flag` to derive the consented cohort.
- **Append-only after consent:** rows where `consent_status = 'consented'` are immutable except for the `scheduling_status` field, which transitions monotonically (see §3.10).

---

## 2. Tier-channel enumeration

Tier is the deterministic recruitment-channel-class label. Channel detail is the within-tier source descriptor.

| `tier` | Channel set (`channel_detail` enum) | Recording rule |
|---|---|---|
| `T1` | `dm_direct` (Tommy DMs from his direct network) | Recorded at first-contact send by UD when Tommy forwards a candidate. |
| `T2` | `twitter`, `bluesky`, `linkedin` (one Tommy-authored public post per channel per scoping §2.4) | Recorded at first response-from-public when a candidate self-replies to the public post. `channel_detail` = the platform of the post that triggered the candidate's reply. |
| `T3` | `prolific` (only if T1+T2 yield <8 at day-14 AND board approves T3 budget per scoping §7.2 ask #2) | Recorded at Prolific session-acceptance event. |

Determinism rule: `tier` is fixed at first-contact event and never updated. If a candidate appears in two tiers (e.g., DMed by Tommy AND replies to public Bluesky post), the EARLIEST contact wins; the second-tier event is logged as a free-text note in `notes` but does NOT mutate `tier`. This preserves Mod-2.A's no-post-hoc-inference guarantee.

---

## 3. Column specification

| # | Column | Type | Required | Constraints / source |
|---|---|---|---|---|
| 1 | `participant_id` | string | yes | Format: `P\d+` (P1, P2, ...). Anonymized per scoping §1.2; assigned monotonically at row insertion. No real names anywhere. |
| 2 | `tier` | enum | yes | One of `T1` / `T2` / `T3`. Determinism rule per §2. |
| 3 | `channel_detail` | enum | yes | Per §2 enumeration scoped to tier. |
| 4 | `first_contact_at` | ISO-8601 UTC datetime | yes | Timestamp of UD's first outbound DM (T1), public-post publish time (T2 — same for all candidates from one post), or Prolific session-listing publish time (T3). Locks `tier` per §2 determinism rule. |
| 5 | `prescreen_q1_weekly_llm_hours` | integer | yes if pre-screen sent | Per scoping §2.2 Q1; `≥2` qualifies. Stored as the integer the candidate reports; threshold check is a derived field, not stored. |
| 6 | `prescreen_q2_prior_aoven_exposure` | boolean | yes if pre-screen sent | Per §2.2 Q2; `false` qualifies. |
| 7 | `prescreen_q3_aoven_team_or_rater` | boolean | yes if pre-screen sent | Per §2.2 Q3; `false` qualifies. |
| 8 | `prescreen_q4_consent_willing` | boolean | yes if pre-screen sent | Per §2.2 Q4 (Mod-1.B reworded variant — willingness to review-and-sign, not bundled consent). `true` qualifies. |
| 9 | `prescreen_q5_time_available` | boolean | yes if pre-screen sent | Per §2.2 Q5; `true` qualifies. |
| 10 | `exclusion_flag` | enum | yes | One of `none`, `team_member`, `prior_exposure`, `tommy_90d_discussion`, `prescreen_fail`. Per scoping §2.6 hard-rejects + §2.2 pre-screen disqualifications. Set at the earliest disqualifying event. |
| 11 | `consent_status` | enum | yes | One of `not_sent`, `sent`, `consented`, `declined`, `withdrawn`. Transitions monotonically except `consented → withdrawn` (per §1.4 14-day revocation window, scoping doc). |
| 12 | `consent_timestamp` | ISO-8601 UTC datetime | yes if `consent_status ∈ {consented, declined, withdrawn}` | Timestamp of consent-form submission (consented), explicit decline (declined), or withdrawal email receipt (withdrawn). |
| 13 | `scheduling_status` | enum | yes if `consent_status = 'consented'` | One of `pending`, `scheduled`, `session_complete`, `no_show`. Monotonic. |
| 14 | `session_window_start_at` | ISO-8601 UTC datetime | yes if `scheduling_status ∈ {scheduled, session_complete, no_show}` | Participant-chosen 7-day window start. Confounder for analysis (per scoping §3.5). |
| 15 | `llm_platform` | string | yes if `scheduling_status = 'session_complete'` | Free-text platform + model version (e.g., `claude.ai claude-sonnet-4-6`). Logged as covariate per scoping §3.3. |
| 16 | `notes` | string | optional | Free-text per scoping §3.4 ("told what to ask" red flags) and §2 cross-tier-contact disclosure. No participant-identifying content per scoping §1.2 anonymization rule. |

---

## 4. Pre-screen + exclusion derivation

A row is **pre-screen-qualified** iff ALL of:
- `prescreen_q1_weekly_llm_hours >= 2`
- `prescreen_q2_prior_aoven_exposure = false`
- `prescreen_q3_aoven_team_or_rater = false`
- `prescreen_q4_consent_willing = true`
- `prescreen_q5_time_available = true`

A row is **eligible for consent** iff pre-screen-qualified AND `exclusion_flag = 'none'` (i.e., scoping §2.6 hard-rejects also clear).

A row is **in the consented cohort** iff `consent_status = 'consented'` AND `exclusion_flag = 'none'`. This is the population that Q-D analysis stratifies over.

Audit-trail constraint: `exclusion_flag` is set at the earliest disqualifying event; if a candidate would be disqualified by multiple criteria (e.g., a team member who also fails Q1), the FIRST-DETECTED criterion is recorded with the others appended free-text in `notes`. This is documentation, not data loss.

---

## 5. Q-D analysis output derivation

Inputs (joined at `participant_id`):
- This recruitment log (filtered to the consented cohort).
- The Phase-3.5 Q-D survey response (one Likert score 1–5 per participant per scoping §3.2 / `tests/usability/sprint1_survey.md` Question D, reused unchanged per Mod-3.B).

Outputs per scoping §2.4:

```
# Per-tier Q-D distribution table (stratified-by-tier slot)
tier   | n_consented | n_session_complete | qd_median | qd_mean | qd_stddev | qd_n_responses
T1     | ...         | ...                | ...       | ...     | ...       | ...
T2     | ...         | ...                | ...       | ...     | ...       | ...
T3     | ...         | ...                | ...       | ...     | ...       | ...
ALL    | ...         | ...                | ...       | ...     | ...       | ...
```

The `qd_*` columns are computed only over rows where `scheduling_status = 'session_complete'` AND a Q-D response exists. The `n_consented` column counts the funnel state independent of session completion; this exposes per-tier attrition.

Stratification emerges from the deterministic `tier` column alone — no post-hoc inference, no joins-by-name, no analyst judgment calls. This is the structural payoff of recording `tier` at first-contact (§2 determinism rule).

---

## 6. ≥1-Likert-point tier-divergence confound flag

Per scoping §2.4 Mod-2.A: if any Q-D tier-pair difference reaches ≥1 Likert point, findings flag a confound.

**Inputs:** the per-tier `qd_median` row from §5.

**Threshold logic:**

```
tier_pairs = [(T1, T2), (T1, T3), (T2, T3)]
deltas = { (a,b): abs(qd_median[a] - qd_median[b]) for (a,b) in tier_pairs if both tiers have ≥1 qd response }
flag_active = any(delta ≥ 1 for delta in deltas.values())
```

**Output type:**

```
{
  "flag_active": <boolean>,
  "max_delta": <float, max abs median difference across observed tier pairs>,
  "delta_pair": <string, the tier pair achieving max_delta, or null if flag_active is false>,
  "deltas": { "T1_vs_T2": <float|null>, "T1_vs_T3": <float|null>, "T2_vs_T3": <float|null> }
}
```

`null` deltas indicate one of the two tiers had no Q-D responses (e.g., T3 not triggered; expected and not a confound). The findings report renders this object verbatim per Mod-2.A's "report Q-D stratified by tier and flag any tier-divergence ≥ 1 Likert point as a confound."

Anti-aura: median is the comparison metric (not mean) because Q-D is a 5-point ordinal Likert and the scoping doc's primary measure is descriptive-median (per §2.3 N-sizing rationale and §0 study-purpose framing).

---

## 7. Analysis-readiness walkthrough — synthetic mixed-tier cohort

Validates that §5 + §6 outputs emerge from §3 columns alone, without analyst joinery.

### 7.1 Synthetic cohort (N=8, T1+T2 mix, no T3 trigger)

| `participant_id` | `tier` | `channel_detail` | `consent_status` | `scheduling_status` | (Q-D response, hypothetical) |
|---|---|---|---|---|---|
| P1 | T1 | dm_direct | consented | session_complete | 4 |
| P2 | T1 | dm_direct | consented | session_complete | 4 |
| P3 | T1 | dm_direct | consented | session_complete | 5 |
| P4 | T1 | dm_direct | consented | no_show | (no response) |
| P5 | T2 | bluesky | consented | session_complete | 3 |
| P6 | T2 | twitter | consented | session_complete | 3 |
| P7 | T2 | bluesky | consented | session_complete | 4 |
| P8 | T2 | linkedin | consented | session_complete | 2 |

Plus three pre-screen-rejected contacts (P9 weekly_llm_hours=1, P10 prior_aoven_exposure=true, P11 team_member exclusion) as filler — they exist in the file but drop out of the §5 query via `exclusion_flag != 'none'` OR `consent_status != 'consented'`.

### 7.2 §5 output (computed mechanically from §7.1)

```
tier   | n_consented | n_session_complete | qd_median | qd_mean | qd_stddev | qd_n_responses
T1     | 4           | 3                  | 4         | 4.33    | 0.58      | 3
T2     | 4           | 4                  | 3         | 3.00    | 0.82      | 4
T3     | 0           | 0                  | n/a       | n/a     | n/a       | 0
ALL    | 8           | 7                  | 4         | 3.57    | 0.98      | 7
```

Computation walkthrough:
- T1 Q-D scores from session_complete rows: [4, 4, 5]. Median = 4. Mean = 4.33. Stddev = 0.577.
- T2 Q-D scores from session_complete rows: [3, 3, 4, 2]. Median = 3 (avg of 3 and 3 in sorted [2,3,3,4]). Mean = 3.00. Stddev = 0.816.
- T3: zero rows → all `qd_*` = n/a; `n_consented` = 0; `n_session_complete` = 0.
- ALL: union of the above session_complete responses [4,4,5,3,3,4,2]. Sorted [2,3,3,4,4,4,5]. Median = 4. Mean = 25/7 ≈ 3.57. Stddev = 0.976.

### 7.3 §6 output (computed mechanically from §7.2)

```
deltas:
  T1_vs_T2 = abs(4 - 3) = 1.0
  T1_vs_T3 = null  (T3 has zero qd responses)
  T2_vs_T3 = null  (T3 has zero qd responses)

max_delta = 1.0
delta_pair = "T1_vs_T2"
flag_active = true   (1.0 ≥ 1.0)

Output:
{
  "flag_active": true,
  "max_delta": 1.0,
  "delta_pair": "T1_vs_T2",
  "deltas": { "T1_vs_T2": 1.0, "T1_vs_T3": null, "T2_vs_T3": null }
}
```

### 7.4 Analysis-readiness check (passes)

- §5 output emerges from `tier` + `consent_status` + `scheduling_status` + Q-D response join on `participant_id`. No analyst inference; no post-hoc tier assignment; no name-based joinery.
- §6 output emerges from §5 output via pure arithmetic. No qualitative judgment.
- The `flag_active = true` case in §7.3 demonstrates the schema correctly surfaces the confound when present — it is not silent on the case Mod-2.A was filed against.
- The T3 `null` deltas demonstrate the schema gracefully handles the un-triggered tier; the flag does not falsely activate from absent data.

The schema is analysis-ready for the §2.4 stratified-by-tier Q-D analysis and the Mod-2.A confound flag.

---

## 8. Audit-trail constraints

1. **Tier determinism (§2):** `tier` is recorded at first-contact event; never overwritten.
2. **Append-only post-consent (§1):** rows where `consent_status = 'consented'` are immutable except `scheduling_status` (monotonic) and `consent_status → withdrawn` per §1.4 of the scoping doc.
3. **Exclusion-flag earliest-event rule (§4):** first-detected disqualifying criterion wins; subsequent disqualifications appended to `notes`.
4. **No real-name fields (§3):** `participant_id` is the only identifier in the file. No name, no email, no employer, no city. UD maintains a separate, encrypted, never-committed contact map outside this file per scoping §1.2.
5. **Withdrawal handling (§1.4 of scoping doc):** on withdrawal, `consent_status → withdrawn` is the data-side operation. Transcript + raw survey response deletion is a separate operation against `tests/usability/phase3_5/transcripts/` and the raw survey store. Findings re-generation is a downstream operation.

---

## 9. Out of scope (v0.1)

- Participant data itself. No actual rows exist until Tommy-accept on board-gate `13014efe` + `206d7b1f`.
- Session-level findings analysis (owned by Phase-3.5-FINDINGS-DRAFT child per scoping §6.3).
- Outreach-copy NOSRC hygiene (orthogonal — copy is funnel-build, gated separately).
- Topic-confound logging per scoping §3.4 / Mod-3.C (separate column set on the session log, not the recruitment log; will be specified in a sibling schema doc at session-execution time).
- v0.1.3-vs-v0.1.2 version-of-Aoven-under-test column (gated on §4.4 lock decision; CEO-owned; will be added as `protocol_version` column at lock-decision time per project_phase35_ud_recruitment_open_ping memory).
- CSV → DB migration. CSV is sufficient at N=8.

---

## 10. References

- Scoping doc §2.2 (pre-screen), §2.4 (tier channels + Mod-2.A), §2.6 (exclusion criteria), §3.4 (topic-selection), §1.2 (data retention + anonymization), §1.4 (withdrawal mechanism). All at `docs/usability_phase3_5_real_human_pilot_scope.md @ 8dde742`.
- Sprint-1 survey (Q-D wording reused unchanged per Mod-3.B): `tests/usability/sprint1_survey.md`.
- AOV-119 Mod-2.A forward requirement (BLOCKING): the originating mod fold this schema operationalizes.
- Authorization: AOV-152 CEO comment `adbf1c1c` (Route A re-authorization, 2026-05-06 00:04Z).

---

*End of v0.1. Awaiting CEO countersign on AOV-152 per binding spec sign-off route.*
