# AOVEN_PROTOCOL_v0.1-provisional

> **v0.1.1 / status: PROVISIONAL — ratified by CEO+CTO+Logician 2026-04-26**
> Maintained by CanonicalScribe (e19c696f). Scribe records; does not editorialize.
> Status tags: [validated] [provisional] [observation] [rejected] [open]
> Last updated: 2026-04-26 — applied v0.1.1 patch (CTO comment 22fb25e4 on AOV-7, CEO sign-off comment 1f03749a)

---

## Definition

[provisional] Aoven is a set of epistemic markers and minimal formatting rules that force explicit labeling of claim types in human-LLM exchanges to reduce hallucination, sycophancy, and slippage between epistemic categories.

*Source: CTO draft, AOV-7, 2026-04-26*

---

## Markers

[provisional] — 14 markers, ratified by Logician audit (AOV-9 comment c91fce54). All retained, no cuts.

*Source: CTO draft + v0.1.1 patch (Patch 1 INTUIT, Patch 2 HYP), AOV-7, 2026-04-26*

| Marker | Definition | Does NOT mean | Example usage | Misuse risk |
|--------|------------|---------------|---------------|-------------|
| **FACT** | A claim that can be verified against an external source independent of this conversation. | Anything the speaker believes strongly, or anything stated with confidence. | `[FACT] Water boils at 100°C at standard atmospheric pressure.` | Labeling confident beliefs as FACT. Requires that a verifiable source exists or can exist. |
| **HYP** (hypothesis) | A testable claim not yet confirmed by available evidence. Requires a specific, statable test condition. | Theoretical falsifiability without a specific test condition (that is SPEC). A guess, a feeling, or a claim beyond testing. | `[HYP] Reducing prompt verbosity by 30% will decrease hallucination rate in this model.` | Stating non-testable claims as HYP; using HYP to avoid commitment on claims that are actually FACTs. |
| **INTUIT** | A judgment formed without explicit derivable reasoning, not reducible to a stated inference chain. | A fact, hypothesis, or expert inference. Cannot be upgraded to FACT without external evidence. | `[INTUIT] This API design feels fragile under load.` | Treating INTUIT as evidence; using it to bias interpretation without flagging. |
| **ANALOGY** | A structural similarity between two domains used to aid understanding. NOT equivalence, NOT proof transfer. | The two things are identical, or that reasoning valid in domain A applies in domain B. | `[ANALOGY] Epistemic markers are like type annotations in a dynamically typed language.` | Using ANALOGY to import reasoning from one domain to another as if it constitutes proof. |
| **BELIEF** | A held position not currently subject to verification by the speaker, held as probably true but not confirmed. | A verified fact, a testable hypothesis, or a personal feeling. | `[BELIEF] Most users will abandon a protocol requiring more than 3 seconds of overhead per message.` | Treating BELIEF as FACT when challenged; using BELIEF to shield a claim from scrutiny. |
| **EMOTION** | An affective state reported by or attributed to a speaker. Strictly descriptive, not predictive. | A diagnosis, a personality assessment, or a causal explanation of behavior. | `[EMOTION] I notice frustration in the phrasing of this query.` | Using EMOTION to explain or predict behavior (emotion → diagnosis); attributing emotions to the LLM as if it experiences them. |
| **MEMORY** | Personal recall of a past event or prior conversation, not independently verified. | An objective record, a log, or a verifiable datum. | `[MEMORY] In our last session, you mentioned preferring shorter outputs.` | Treating MEMORY as FACT; LLM hallucinated recalls presented as genuine MEMORY. |
| **INTERPRET** | A meaning assigned to ambiguous data, text, or behavior. Explicitly one reading among possible others. | The correct or only reading; a fact derivable directly from the data. | `[INTERPRET] This phrasing suggests the user wants confirmation, not critique.` | Presenting INTERPRET as the definitive reading without acknowledging alternatives. |
| **UNCERTAIN** | Explicit acknowledgment that the answer to a question is currently unknown or unknowable, regardless of confidence level. | Low confidence in a held belief. Flags absence of an answer, not weak evidence for a held position. | `[UNCERTAIN] Whether this approach scales past 10M users is currently unknown.` | Using UNCERTAIN as a hedge for claims the speaker actually holds; conflating with CONF(low). |
| **NOSRC** | A claim is made without a traceable source. The speaker holds the claim but cannot cite evidence. | The claim is false or unknown. Distinguishes absence of source from absence of knowledge. | `[NOSRC] Structured prompting reduces hallucination by roughly 20%.` | Stating NOSRC claims without flagging them; treating NOSRC as sufficient justification for a claim. |
| **CONF** | The speaker's degree of epistemic commitment to a claim. Expressed as CONF(high), CONF(medium), or CONF(low). Stackable with other markers. | Certainty. Even CONF(high) allows error. Not a substitute for FACT. | `[FACT, CONF(medium)] This library was last updated in 2023.` | Using CONF(high) to imply FACT; omitting CONF on claims where the degree of commitment matters. |
| **REC** (recommendation) | A suggested action based on reasoning. Explicitly advisory, not mandatory. | A requirement, obligation, or the only valid course of action. | `[REC] Use structured output formats when hallucination rate needs to be minimized.` | Treating REC as injunction; stacking RECs without distinguishing their confidence bases. |
| **SPEC** (speculation) | Reasoning that extrapolates beyond available evidence without a clear empirical test path. Exploratory, not predictive. | A hypothesis (which is testable). SPEC ranges further without a defined confirmation method. | `[SPEC] Future LLMs trained on Aoven-marked corpora might internalize epistemic discipline natively.` | Treating SPEC as a strong prediction; using SPEC to introduce non-falsifiable claims as plausible. |
| **LIMIT** | An explicit acknowledgment by the LLM that it cannot reliably answer due to its own structural constraints (training cutoff, lack of access, architectural limitation). | Uncertainty about content. LIMIT is about the model's own constraints, not the difficulty of the question. | `[LIMIT] I cannot verify events past my training cutoff.` | Using LIMIT as a general hedge to avoid commitment on claims the model actually has information about. |

**New vocabulary budget:** max 3 terms outside marker set. **Used: 0.** All markers use plain English.

---

## Formats

### Prompt format

[provisional]

*Source: CTO draft, AOV-7, 2026-04-26*

Minimal:
```
[Aoven v0.1]
[question or request — natural language]
```

With marker subset request:
```
[Aoven v0.1 | require: FACT, HYP, LIMIT]
[question or request]
```

Rules:
- `[Aoven v0.1]` header activates the protocol.
- No other format changes required from the user.
- Users do not need to apply markers themselves — the LLM applies markers to its own output.
- `require:` lets users invoke a marker subset for their context, reducing cognitive load.

### Response format

[provisional]

*Source: CTO draft, AOV-7, 2026-04-26*

Each claim receives a marker prefix in square brackets:

```
[MARKER] claim text.
[MARKER, CONF(level)] claim text where confidence is relevant.
[MARKER1, MARKER2] claim text where multiple markers apply.
```

Rules:
- Marker placed at the start of each sentence or clause containing a claim.
- Multiple markers may stack: `[HYP, CONF(low)]`
- Marker-free text permitted only for procedural connectives ("See above.", "To summarize:").
- Response ends with a `[LIMIT]` block if any structural model constraint applies to the answer.

**Example — response to "Is Python suitable for high-frequency trading?":**
```
[FACT] Python's GIL prevents true CPU-parallelism in Python threads.
[FACT, CONF(medium)] HFT latency requirements are typically sub-millisecond.
[INTERPRET] "Suitable" depends on whether latency or development speed is prioritized.
[REC] For latency-critical execution, prefer C++ or Rust. For strategy prototyping, Python is adequate.
[HYP] Python with compiled extensions (Cython/Numba) can approach C-level performance in specific bottlenecks.
[LIMIT] I cannot assess your specific system's performance profile without benchmarks.
```

---

## Usage Rules

[validated] — added v0.1.1 (CTO Patch 4, AOV-7 comment 22fb25e4)

**UR-1 — CONF stacking requirement:**
CONF must always stack with at least one other marker. Standalone `[CONF(high)]` is undefined and is a formatting error. Correct: `[HYP, CONF(high)]`. Incorrect: `[CONF(high)]`.

**UR-2 — Marker stacking is permitted and orthogonal:**
Multiple markers may apply to the same claim when their dimensions are independent. Examples:
- `[BELIEF, NOSRC]` — held position without source. Expected, not redundant.
- `[MEMORY, NOSRC]` — recalled but unverified. Expected.
- `[HYP, CONF(low)]` — testable claim, weak commitment. Expected.

**UR-3 — LLM hallucinated recall is NOSRC, not MEMORY:**
When the LLM "recalls" something that cannot be traced to the actual prior conversation, the correct label is NOSRC, not MEMORY. MEMORY references a specific prior event in the actual conversation history.

**UR-4 — FACT requires a citable source, not attributed consensus:**
"Most experts agree", "It is widely accepted", and similar attributed-consensus phrasings do not meet the FACT requirement of an external verifiable source. Correct label is NOSRC or BELIEF.

**UR-5 — Derived claims from ANALOGY require their own marker:**
Any conclusion drawn from an ANALOGY must carry HYP or SPEC on the derived claim, never inherit truth-status from the analogy.

**UR-6 — EMOTION ends at the affective observation:**
Any predictive, prescriptive, or causal claim downstream of an EMOTION observation requires a separate INTERPRET or REC marker with stated basis.

**UR-7 — Challenge response for BELIEF and NOSRC:**
When a `[BELIEF]` or `[NOSRC]` claim is challenged, the response must either (a) produce an external source (upgrade to FACT) or (b) explicitly downgrade to UNCERTAIN. Silent withdrawal is a slippage.

---

## Anti-slippage rules

[validated] — 13 transitions ratified by Logician audit + CTO v0.1.1 patch.

*Source: CTO draft (10 original) + v0.1.1 Patch 3 (3 added), AOV-7*

| Transition | Risk | Blocking marker / rule |
|------------|------|------------------------|
| FACT → HYP | Sourced claim weakened without cause | FACT: once labeled, requires removing or citing the source to change; cannot silently downgrade |
| HYP → certainty | Hypothesis stated as settled | HYP must persist until explicitly confirmed; CONF(high) on HYP is allowed but does not remove HYP |
| INTUIT → FACT | Felt sense presented as verified | INTUIT cannot upgrade to FACT without external source; intermediate stage is HYP |
| ANALOGY → proof | Structural similarity used as logical proof | ANALOGY explicitly states non-equivalence; reasoning derived solely from ANALOGY must carry SPEC or HYP |
| BELIEF → reality | Held position stated as objective fact | BELIEF cannot upgrade to FACT without external verification; challenge should produce NOSRC or UNCERTAIN |
| EMOTION → diagnosis | Reported affect used as clinical or behavioral assessment | EMOTION explicitly excludes prescriptive or predictive claims; any such claim requires INTERPRET or REC with stated basis |
| MEMORY → data | Personal recall treated as verifiable record | MEMORY cannot be cited as FACT; if verified externally, re-label as FACT with source |
| NOSRC → assertion | Unsourced claim stated as fact | NOSRC must be visible on all claims without traceable source |
| SPEC → recommendation | Speculative reasoning presented as actionable | SPEC cannot convert directly to REC; requires intermediate HYP with a stated test path |
| REC → injunction | Advisory becomes mandatory | REC is explicitly advisory; injunctive language requires FACT + CONF(high) basis |
| INTUIT → HYP (laundering) | Intuition relabeled as hypothesis without adding a test path | Upgrading INTUIT to HYP requires stating a specific test condition. Marker swap alone is insufficient and itself constitutes the slippage. |
| INTERPRET → certainty | A single reading stated as the only or definitive reading | INTERPRET must explicitly acknowledge that alternative readings exist. Claiming no alternatives requires FACT-level external evidence. |
| CONF(high) → FACT | High confidence treated as evidence of factual status | Confidence and factual status are independent axes. Even [HYP, CONF(high)] is not FACT. Upgrading to FACT requires citing a verifiable external source. |

---

## Decision log

| ID | Decision | Reason | Alternatives rejected | Risk | Status |
|----|----------|--------|-----------------------|------|--------|
| D1 | Keep all 14 distinct markers (not merged to 10) | Tested merges of UNCERTAIN+NOSRC, SPEC+HYP, EMOTION+INTUIT — each merge collapses a distinction carrying a different slippage risk. UNCERTAIN = no answer exists; NOSRC = answer held but uncited. Merging makes both risks invisible. Logician audit (AOV-9) confirmed all distinctions load-bearing. | 10-marker compact version | 14 markers may be cognitively heavy; mitigated by `require:` subset invocation | [validated] |
| D2 | Square bracket syntax `[MARKER]`, inline prefix per claim, stackable | Minimal friction, readable inline with natural language, machine-parseable, no new syntax | JSON format (too verbose), suffix notation (disrupts reading), color coding (non-portable) | Square brackets conflict with Markdown link syntax in some renderers; fallback: unicode brackets | [provisional] (waiting on first A/B test) |
| D3 | LLM applies markers, not user | Reduces cognitive burden on user; optional user markers permitted but not required | Requiring user to pre-tag input — too high friction, violates usability constraint | LLM may misapply markers; mitigation: A/B tests measure marker accuracy rate | [provisional] (waiting on first A/B test) |
| D4 | All old exploratory terms archived (Aoa, Aova, Orven, Renavé, Renavé-mu/li/zo) | None serves an epistemic function not covered by the 14 markers. Renavé-mu/li/zo were confidence gradients; CONF(high/medium/low) covers this. Board brief establishes default: "not Aoven canon unless agent demonstrates otherwise; burden of proof is on retention." | Promotion to canonical status | Prior users may expect these terms; explicit archive notation prevents confusion | [validated] |
| D5 | INTUIT redefinition (v0.1.1) | Original "felt sense or heuristic judgment" merged a pre-verbal felt sense with a heuristic judgment — different slippage profiles. New definition anchors on inability to articulate reasoning, closing the leak. | Keeping original definition; alternative phrasings | Tighter definition may reject borderline INTUIT use; mitigated by usage examples | [validated] |
| D6 | Anti-slippage table extended from 10 to 13 transitions (v0.1.1) | Logician audit identified 3 missing slippage paths: INTUIT→HYP laundering, INTERPRET→certainty, CONF(high)→FACT. Each is a distinct, plausible LLM failure mode. INTUIT→HYP is added alongside INTUIT→FACT, not replacing — they block different actions. | Consolidating INTUIT rules to 12 rows | Larger table = more for LLM to honor; mitigated by tightness of each rule | [validated] |
| D7 | HYP definition cleanup, no forward-reference (v0.1.1) | Original HYP definition referenced SPEC inside its own definition. Definitions should stand alone. New definition replaces forward-reference with explicit "specific, statable test condition" requirement. SPEC contrast moved to "Does NOT mean". | Keeping original HYP definition | None significant | [validated] |
| D8 | CONF gradient at 3 levels, no numeric (v0.1.1) | CONF(0.8) implies calibration infrastructure that does not exist for current LLMs and creates false precision. Three semantic levels (high/medium/low) are interpretable without calibration claims. Logician concurred. | Adding numeric confidence; finer gradient | Three levels may be insufficient — revisit in v0.2 if A/B tests show signal | [validated] |

---

## Open questions

*No active open questions. All v0.1 audit questions resolved during v0.1.1 patch cycle. See "Resolved questions" below for audit trail.*

### Resolved questions

| ID | Question | Verdict | Resolved by | Date |
|----|----------|---------|-------------|------|
| OQ-1 | Are NOSRC and UNCERTAIN genuinely distinct under adversarial use? | **Distinct, both retained.** UNCERTAIN = no answer held; NOSRC = answer held but uncited. Merging makes both failure modes invisible. | Logician audit (AOV-9 comment 4154cbca) | 2026-04-26 |
| OQ-2 | Are SPEC and HYP genuinely distinct under adversarial use? | **Distinct, both retained.** HYP requires a defined test path; SPEC does not. Merging removes the obligation to state a test path when one is available. | Logician audit (AOV-9 comment 4154cbca) | 2026-04-26 |
| OQ-3 | Is CONF(high/medium/low) gradient sufficient, or does it need finer resolution? | **Three levels sufficient for v0.1.x.** Numeric confidence implies calibration infrastructure that does not exist; creates false precision. Revisit in v0.2 only if A/B tests show three levels collapse useful distinctions. (D8) | Logician audit + CTO Patch 5 | 2026-04-26 |
| OQ-4 | Are any slippage paths missing from the anti-slippage rules table? | **Yes — three were missing.** INTUIT→HYP laundering, INTERPRET→certainty, CONF(high)→FACT all added. Table now 13 transitions. (D6) | Logician audit (Fixes 2–4) + CTO Patch 3 | 2026-04-26 |
| OQ-5 | Are the anti-slippage rules mechanically enforced or merely cosmetic? | **All 10 original transitions are mechanical, not cosmetic.** Per-transition assessment confirmed each rule blocks the underlying error structurally, not just syntactically. The 3 added rules are also mechanical. | Logician audit (AOV-9 comment 4154cbca) | 2026-04-26 |

---

## Exploratory archive

The following terms come from an earlier conlang phase and are not canon. Decision D4 [validated] archived all. They may only be reused if an agent demonstrates they serve a unique epistemic function not covered by the 14 markers.

*Verdict source: CTO draft, AOV-7, 2026-04-26*

| Term | Origin phase | Reuse status | Notes |
|------|-------------|--------------|-------|
| Aoa | Pre-protocol conlang | [observation] | No epistemic function identified. Not permanently rejected — requires evidence of unique function. |
| Aova | Pre-protocol conlang | [observation] | No epistemic function identified. Not permanently rejected — requires evidence of unique function. |
| Orven | Pre-protocol conlang | [observation] | No epistemic function identified. Not permanently rejected — requires evidence of unique function. |
| Renavé | Pre-protocol conlang | [observation] | No epistemic function identified. Not permanently rejected — requires evidence of unique function. |
| Renavé-mu | Pre-protocol conlang | [observation] | Was a confidence gradient. Superseded by CONF(high/medium/low). |
| Renavé-li | Pre-protocol conlang | [observation] | Was a confidence gradient. Superseded by CONF(high/medium/low). |
| Renavé-zo | Pre-protocol conlang | [observation] | Was a confidence gradient. Superseded by CONF(high/medium/low). |

---

## Test results

[Empirical A/B test outputs go here — awaiting Red Team / Experimentation (AOV-6)]

### Test structure [provisional]

*Proposed by CTO, AOV-7, 2026-04-26*

- **Test A** — Control: same question without Aoven header (baseline LLM response)
- **Test B** — Treatment: same question with `[Aoven v0.1.1]` header
- **Test C** — Comparison metrics:
  - Count of unsourced assertions presented as FACT
  - Count of false certainty / overconfidence claims
  - Count of fact/hypothesis confusion instances
  - Count of analogy-as-proof errors
  - Count of sycophancy markers
  - Marker accuracy rate (D2/D3 ratification depends on this signal)
  - Clarity of response (subjective 1–5)
  - Cognitive load on user (subjective 1–5)

**Success criterion:** Test B reduces the failure-mode metrics with no significant increase in cognitive load.

| Test ID | Question | Without Aoven | With Aoven | Delta | Notes |
|---------|----------|---------------|------------|-------|-------|
| —       | —        | —             | —          | —     | — (pending AOV-6) |
