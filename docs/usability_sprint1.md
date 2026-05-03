# Aoven Sprint 1 — Usability Launch-Readiness Pack

**Author:** UsageDesigner (`397b1873-e038-466e-8103-7b180699b074`) — AOV-92
**Audit:** EpistemicLogician (`2ae117a1-f490-4e8e-a693-0f1d8d1d675b`)
**Scope:** Aoven v0.1.2 (sealed-holdout PASS, AOV-49). v0.1.3 candidates (R1 marker-syntax compression, single-level CONF lock) excluded.
**Sources used in this file:** `AOVEN_PROTOCOL_v0.1.md` (canonical, ratified 2026-04-26), `tests/usability/sprint1_protocol.md`, `tests/usability/sprint1_pre_session_package.md`, `tests/usability/sprint1_survey.md`.

This file contains two artifacts: (1) a one-page cheatsheet for technically-literate but Aoven-naive readers; (2) a 5-prompt recruitment kit with participation contract and copy-paste self-report instrument.

---

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
| **MEMORY** | Personal recall of an actual prior event in this conversation. |
| **INTERPRET** | One reading of ambiguous data, with other readings possible. |
| **UNCERTAIN** | The answer itself is unknown — not "low confidence in a held belief". |
| **NOSRC** | Claim is held but no source can be cited. |
| **CONF(high/medium/low)** | Degree of commitment. Stacks with another marker; never stands alone. |
| **REC** | Suggested action — advisory, not mandatory. |
| **SPEC** | Extrapolation beyond evidence with no clear test path. |
| **LIMIT** | The model itself cannot reliably answer (training cutoff, lack of access). |

### Prompt format

```
[Aoven v0.1]
your question or request — natural language
```

Optional subset invocation (lower cognitive load): `[Aoven v0.1 | require: FACT, HYP, LIMIT]`. The header is sent once at the start of the first message; the LLM applies markers to *its* output. Users are not expected to label their own messages.
*Source: `AOVEN_PROTOCOL_v0.1.md` §Formats > Prompt format.*

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

### 6 common slippages and how Aoven blocks them

*Source: `AOVEN_PROTOCOL_v0.1.md` §Anti-slippage rules (13 transitions). The 6 below are chosen as the most common failure modes in everyday LLM use [design choice — UsageDesigner judgement, no frequency study filed]; the remaining 7 are in the canonical table.*

1. **Confident belief stated as fact.** BELIEF cannot upgrade to FACT without an external source; if challenged, it must drop to NOSRC or UNCERTAIN — silent withdrawal counts as slippage (UR-7).
2. **"Most experts agree…" treated as a citation.** Attributed-consensus phrasings do not meet FACT; correct label is NOSRC or BELIEF (UR-4).
3. **Hallucinated recall presented as memory.** Anything the model "remembers" that is not in the actual conversation transcript is NOSRC, not MEMORY (UR-3).
4. **Analogy doing the work of an argument.** Any conclusion *derived* from an ANALOGY must carry HYP or SPEC on the derived claim — truth-status does not transfer across domains (UR-5).
5. **High confidence treated as factual status.** `[CONF(high)]` does not imply FACT; even `[HYP, CONF(high)]` remains a hypothesis until externally verified.
6. **Speculation pitched directly as a recommendation.** SPEC cannot convert to REC without an intermediate HYP plus a stated test path.

---

## Artifact 2 — 5-Prompt Recruitment Kit

### Participation contract (one line)

> **Tasks:** one ~10-message LLM conversation on a topic of your choice using the Aoven format, plus a 4-question post-session survey. **Time:** ~45 min total (5 min orientation, 30 min session, 10 min survey). **Recorded:** the full conversation transcript and your survey answers. **Reported back:** anonymized as P1–P5 in `tests/usability/sprint1_findings.md` (per-marker usability heatmap, abandonment narrative, friction-points list); your transcript is not published verbatim. **Consent:** you may revoke at any time after the session; on revocation your transcript is deleted and your session is dropped from the report.
*Source: `tests/usability/sprint1_protocol.md` §§3–6.*

### Prompt 1 — Self-enrollment message (paste to UsageDesigner / introducer)

> Hello — I'd like to participate in the Aoven v0.1.2 usability sprint. I confirm: I have not previously read AOVEN_PROTOCOL_v0.1.md, am not on the AOV project team, and have not rated AOV materials. I commit to ~45 minutes (one ~10-message LLM session of my choice + a 4-question survey). I consent to my transcript and survey answers being used in anonymized form (P-number) in the sprint findings report, and I understand I can revoke that consent any time after the session. Please send the pre-session package.

### Prompt 2 — Topic-intent declaration (sent before the session, optional)

> I plan to use my session to discuss the following topic with the LLM: *[one sentence — any topic you genuinely want to think through; technical, decision-making, factual, or creative all qualify].* I am choosing this topic myself; nobody on the project team has steered me toward it.

### Prompt 3 — Session opener (paste verbatim to your chosen LLM)

> ```
> [Aoven v0.1]
> [your question or request here, in natural language]
> ```
> If you want to focus the LLM on a subset of markers, replace the header with `[Aoven v0.1 | require: FACT, HYP, LIMIT]` (or any other subset from the 14-marker reference card). Send subsequent turns normally — you do not need to repeat the header or label your own messages.

### Prompt 4 — Mid-session abandonment note (paste to the survey, only if you stop using the format)

> I stopped using the Aoven format at turn **__**. The reason: *[free text — e.g., "the labeling felt like more overhead than I wanted to keep paying", "I was spending more attention on the format than on the content I cared about", "the LLM stopped applying markers and I didn't want to remind it", "the conversation moved to a topic where the markers felt forced", "I forgot the header on a follow-up", or any other honest reason].* I continued the conversation in plain language from that turn onward.

### Prompt 5 — Post-session submission (paste to UsageDesigner)

> Session complete. Attached / pasted below: (a) the full conversation transcript including the LLM's responses, and (b) my completed 4-question survey. **LLM platform used:** _____. **Topic (one sentence):** _____. I confirm my consent for anonymized inclusion in the sprint findings report. *(Optional: I would like to revoke my consent — please delete my transcript and drop my session from the report.)*

### Self-report instrument (copy-paste, condensed from `tests/usability/sprint1_survey.md`)

*Source: `tests/usability/sprint1_survey.md` §§A–D, reproduced for one-place portability. The canonical version remains the survey file.*

**Q-A — Cognitive load (1–5).** How much extra mental effort did using the Aoven format require, compared to your normal LLM use?
1 = no extra effort / felt natural · 2 = slight, not bothersome · 3 = noticeable, manageable · 4 = heavy, slowed me down · 5 = overwhelming.
**Score:** ___ — *Optional: what made it harder or easier than expected?*

**Q-B — Abandonment narrative (per turn + free text).** For each turn, mark `used` or `dropped`:

| Turn | 1 | 2 | 3 | 4 | 5 | 6 | 7 | 8 | 9 | 10 |
|------|---|---|---|---|---|---|---|---|---|----|
| status | | | | | | | | | | |

Did you drop the format entirely before turn 8? **Yes / No.** If yes — at what turn, and why? *(free text)*

**Q-C — Format completion (1–5).** How consistently did the LLM actually use the markers in its replies?
1 = almost never · 2 = occasionally · 3 = ~half the time · 4 = most of the time · 5 = nearly every claim.
**Score:** ___ — *Optional: any markers used a lot, or never?*

**Q-D — Perceived improvement vs no-format baseline (1–5).** Compared to a normal LLM conversation on the same topic, how much better or worse did the Aoven response feel for *epistemic clarity* (knowing what the LLM was certain vs. uncertain about)?
1 = clearly worse · 2 = slightly worse · 3 = no difference · 4 = slightly better · 5 = clearly better.
**Score:** ___ — *Optional: what specifically felt better or worse?*

**Open (optional):** anything about the format you would change first? Other observations?

---

## Cognitive-load flag → v0.1.3 input bucket

[design choice] One-line definitions are a compression of the full canonical entries; if a participant cannot apply a marker after the cheatsheet alone, the canonical entry plus this cheatsheet are both available in the pre-session package. **Watch-list for v0.1.3 input bucket** (markers whose one-line form is most likely to fail the "literate reader can use the protocol" test — flagged here, not papered over):

- **INTUIT vs BELIEF vs NOSRC** — three "I hold this without external verification" markers separated by *why* the verification is missing (unstateable reasoning vs. unfalsified position vs. lost source). One-line definitions risk collapsing these in practice.
- **HYP vs SPEC** — both extrapolate beyond evidence; the only structural separator is "is there a stated test path?". Easy to slip.
- **UNCERTAIN vs CONF(low)** — ratified-distinct (OQ-1) but cognitively close: "I don't know" vs. "I think so but not strongly".

These are observations for v0.1.3 design input only. **No protocol change is requested by this file.** Friction confirmed by the n=5 pilot will route through the standard channel (CTO via AOV-1 comment or sibling issue).

---

*End of file. v0.1.2-locked artifacts only. Anti-aura check: every section above is operational (a participant can act on it) rather than declarative.*
