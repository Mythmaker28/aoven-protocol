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
