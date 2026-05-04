# AOVEN_PROTOCOL_v0.1-provisional

> **v0.1.3 / status: PROVISIONAL — minor-clarifications bundle ratified by CEO + Logician 2026-05-03 (AOV-111 / AOV-115)**
>
> Maintained by CanonicalScribe (e19c696f). Scribe records; does not editorialize.
>
> Status tags: [validated] [provisional] [observation] [rejected] [open]
>
> Last updated: 2026-05-03 — v0.1.3 minor clarifications bundle landed: subset-header `allow:` / `require:` semantics (D10), UR-3 MEMORY verbatim-quote requirement (D11), UR-8 pause/resume affordance (D12). Source: CTO comment `8a46d4c7` on AOV-111. Audit: Logician PASS on AOV-115 (`b6bd7a58`). CEO ratification: AOV-111 comment `50abfc16`. Folded under AOV-71 per CEO repose comment `6e58c604`.

## Changelog

- **v0.1.3** — three minor clarifications under the "v0.1.3-PROTOCOL clarifications bundle" track (AOV-111): (1) subset-header qualifier semantics — `require:` is mandatory minimum / `allow:` is additive emphasis / default `= allow:` / never silently suppresses unlisted markers (D10); (2) UR-3 strengthened — `[MEMORY]` claims MUST attach a verbatim quotation of prior text in inline `[MEMORY: "..."]` or block-quote form, ≤~2-sentence cap, longer references use `[NOSRC]` (D11); (3) UR-8 added — `[Aoven: pause]` / `[Aoven: resume]` / `[Aoven: off]` graceful-exit affordance with three sanctioned resume signals (D12). Source: CTO bundle on AOV-111 (`8a46d4c7`); Logician PASS on AOV-115 (`b6bd7a58`); CEO ratification on AOV-111 (`50abfc16`); fold-issue AOV-71 (`6e58c604`). NOTE: AOV-54 Patches 1/2/5 ([IT] disambiguation, marker stack-depth cap, launch-checklist legend) — originally also scoped to v0.1.3 under AOV-71 — are NOT in this fold. Patch 1 (stack-depth cap → UR-8) collides with the new UR-8 numbering used here for pause/resume; awaiting CEO/CTO disposition (renumber to UR-9, defer to v0.1.4, or re-scope).
- **v0.1.2** — corrected Renavé family historical origin (board correction, AOV-15); markdown readability pass; no semantic change to markers, formats, or anti-slippage rules.
- **v0.1.1** — INTUIT and HYP definitions tightened; anti-slippage table extended from 10 to 13 transitions; CONF gradient fixed at 3 semantic levels (CTO patch on AOV-7 comment `22fb25e4`, CEO sign-off `1f03749a`).
- **v0.1.0** — initial draft (CTO, AOV-7, 2026-04-26).

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

**Subset-header qualifiers (v0.1.3):** the header `[Aoven v0.1.x | <qualifier>: M1, M2, ...]` accepts two qualifiers, both **non-exclusive**:
- **`require:`** — mandatory minimum. The LLM MUST apply each listed marker when its definition fits a claim. Other markers REMAIN AVAILABLE and SHOULD be applied when their definitions fit. `require:` is a floor, not a ceiling.
- **`allow:`** — additive emphasis. Listed markers are signaled as expected/encouraged; the LLM is invited but not forced to use them. Other markers remain fully available.
- **Default (no qualifier present, e.g. `[Aoven v0.1 | FACT, HYP, LIMIT]`)** — treated as `allow:`.

**No qualifier silently suppresses other markers.** Suppressing INTERPRET, INTUIT, NOSRC, LIMIT etc. via the subset header is **not supported and not safe**: those markers carry independent slippage-blocking work (INTUIT→FACT, INTERPRET→certainty, NOSRC→assertion). Users who want a narrower output should rely on prompt-level shaping, not header suppression. Anti-aura: the protocol's default is to fail open (more markers) on ambiguity, never to fail closed (fewer markers).

*Source: CTO comment `8a46d4c7` on AOV-111, D1 spec text. Audit: Logician PASS on AOV-115 (`b6bd7a58`). CEO ratification: AOV-111 comment `50abfc16`. See D10.*

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
- **Pause / resume / off (v0.1.3):** marker discipline may be suspended for one or more turns via `[Aoven: pause]` and resumed via `[Aoven: resume]`, header re-assertion, or first-marker implicit resume. Whole-session abandonment uses `[Aoven: off]`. See UR-8 for full rules.

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

**UR-3 (v0.1.3 — strengthens v0.1.2 UR-3):** A `[MEMORY]` claim referencing prior conversation text MUST attach the prior text as a **verbatim quotation**. Paraphrase, summary, or characterization of prior content is forbidden under MEMORY; if the LLM cannot reproduce the prior wording, the correct marker is `[NOSRC]`, not `[MEMORY]`. The verbatim-quote requirement makes hallucinated recall mechanically detectable: any reader can string-search the prior conversation for the quoted text. The same rule applies to MEMORY claims about the LLM's own prior outputs (self-quotation).

**Quoting syntax — two permitted forms:**
- **Inline:** `[MEMORY: "<exact prior text>"] Your earlier note about brevity...`
- **Block:** the marker on its own line, followed by a Markdown blockquote of the exact prior text, followed by the claim:
  ```
  [MEMORY]
  > <exact prior text>
  You asked for shorter outputs earlier in this session.
  ```
- **Ellipsis (`...`)** is permitted only to elide irrelevant middle content within a single quoted span; it must NEVER alter wording.
- **Length cap:** if quoting the relevant prior text would exceed roughly two sentences, the LLM MUST instead use `[NOSRC]` and describe the prior content rather than claim memory of it. (Long paraphrase under MEMORY is the silent-slippage path this rule closes.)

*Source: CTO comment `8a46d4c7` on AOV-111, D2 spec text. Audit: Logician PASS on AOV-115 (`b6bd7a58`). CEO ratification: AOV-111 comment `50abfc16`. Subsumes the v0.1.2 UR-3 rule (NOSRC-not-MEMORY for hallucinated recall — preserved within the verbatim-quote requirement). See D11.*

**UR-4 — FACT requires a citable source, not attributed consensus:**
"Most experts agree", "It is widely accepted", and similar attributed-consensus phrasings do not meet the FACT requirement of an external verifiable source. Correct label is NOSRC or BELIEF.

**UR-5 — Derived claims from ANALOGY require their own marker:**
Any conclusion drawn from an ANALOGY must carry HYP or SPEC on the derived claim, never inherit truth-status from the analogy.

**UR-6 — EMOTION ends at the affective observation:**
Any predictive, prescriptive, or causal claim downstream of an EMOTION observation requires a separate INTERPRET or REC marker with stated basis.

**UR-7 — Challenge response for BELIEF and NOSRC:**
When a `[BELIEF]` or `[NOSRC]` claim is challenged, the response must either (a) produce an external source (upgrade to FACT) or (b) explicitly downgrade to UNCERTAIN. Silent withdrawal is a slippage.

**UR-8 — Pause and resume (v0.1.3, additive):** Either party (user or LLM) MAY suspend marker discipline for one or more turns by emitting a `[Aoven: pause]` token at the start of the turn that drops the format. Pausing is an explicit, sanctioned graceful exit and is NOT counted as abandonment under usage metrics. Inside paused turns:
- Marker prefixes are NOT required.
- Bare unmarked sentences are NOT treated as implicit FACT (the implicit-FACT-on-bare-sentence reading is suspended for the duration of the pause).
- The LLM SHOULD acknowledge the pause once and MUST NOT re-prompt the user to remark turns until resume.

**Resume — three sanctioned signals (in priority order):**
1. **Explicit:** either party emits `[Aoven: resume]`. Restores all v0.1.x rules from the next claim onward.
2. **Header re-assertion:** a turn that begins with `[Aoven v0.1.x]` resumes from a fresh state.
3. **Implicit-on-first-marker:** the first claim that emits any standard marker (e.g., `[FACT] ...`) is treated as a resume signal. Mid-turn implicit resume is permitted (a paused turn that ends with a marked claim resumes from that claim).

**`[Aoven: off]`** is a separate, harder signal reserved for whole-session abandonment with consent. After `[Aoven: off]`, a fresh `[Aoven v0.1.x]` header is REQUIRED to resume — implicit resume is NOT honored. This distinguishes "I'm dropping into voice for a few turns" (`pause`) from "I'm done with the protocol for this session" (`off`).

Anti-aura: pause is intentionally additive, not coercive. Forcing markers through a free-association turn is a known abandonment driver (P4-S1 T9); a sanctioned drop-and-resume preserves discipline elsewhere in the session that would otherwise be lost wholesale.

*Source: CTO comment `8a46d4c7` on AOV-111, D3 spec text. Audit: Logician PASS on AOV-115 (`b6bd7a58`). CEO ratification: AOV-111 comment `50abfc16`. Cross-linked from `## Formats > Response format`. See D12.*

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

Each decision below is a discrete protocol-level commitment. Verdicts D1–D3 and D5–D8 are unchanged from v0.1.1. D4 was corrected in v0.1.2 per board input on AOV-15 (see D9). D10–D12 added in v0.1.3 (AOV-111 minor-clarifications bundle). The mirror in `DECISIONS.md` follows this same numbering.

---

### D1 — Keep all 14 distinct markers (not merged to 10)

- **Reason.** Tested merges of UNCERTAIN+NOSRC, SPEC+HYP, EMOTION+INTUIT — each merge collapses a distinction carrying a different slippage risk. UNCERTAIN = no answer exists; NOSRC = answer held but uncited. Merging makes both risks invisible. Logician audit (AOV-9) confirmed all distinctions load-bearing.
- **Alternatives rejected.** 10-marker compact version.
- **Risk.** 14 markers may be cognitively heavy; mitigated by `require:` subset invocation.
- **Status.** [validated]

---

### D2 — Square-bracket syntax `[MARKER]`, inline prefix per claim, stackable

- **Reason.** Minimal friction, readable inline with natural language, machine-parseable, no new syntax.
- **Alternatives rejected.** JSON format (too verbose); suffix notation (disrupts reading); color coding (non-portable).
- **Risk.** Square brackets conflict with Markdown link syntax in some renderers; fallback: unicode brackets.
- **Status.** [provisional] — gated on first A/B test.

---

### D3 — LLM applies markers, not user

- **Reason.** Reduces cognitive burden on user; optional user markers permitted but not required.
- **Alternatives rejected.** Requiring user to pre-tag input — too high friction, violates usability constraint.
- **Risk.** LLM may misapply markers; mitigation: A/B tests measure marker accuracy rate.
- **Status.** [provisional] — gated on first A/B test.

---

### D4 — All earlier exploratory terms archived (Aoa, Aova, Orven, Renavé, Renavé-mu/li/zo)

- **Reason.** None serves an epistemic function not already covered by the 14 markers. Burden of proof on retention. Correct historical origin per board input on AOV-15:
  - **Renavé** — relation de présence répétée sans interaction (relation of repeated presence without interaction).
  - **Renavé-mu** — Renavé réciproque (reciprocal Renavé).
  - **Renavé-li** — Renavé asymétrique (asymmetric Renavé).
  - **Renavé-zo** — sentiment résiduel laissé par la disparition silencieuse d'un Renavé (residual feeling left by the silent disappearance of a Renavé).
- **NOSRC discipline note (v0.1.2).** Earlier wording in this row asserted that Renavé-mu/li/zo "were confidence gradients superseded by CONF(high/medium/low)". That claim was a **NOSRC fabrication** — no agent had a source for the original meaning of these terms. The board provided the correct origin on AOV-15. The fabrication is recorded here, not silently overwritten, because the slippage class — confident assertion without source — is the exact failure mode Aoven exists to prevent. See D9 for the correction trail.
- **Alternatives rejected.** Promotion to canonical status.
- **Risk.** Recurrence of the same NOSRC pattern when reconstructing project history; mitigation: D9 makes the failure visible and the C-6 ("no invented history") rule in `AGENTS.md` is binding on future contributors.
- **Status.** [validated] — verdict (archived; not canon) unchanged.

---

### D5 — INTUIT redefinition (v0.1.1)

- **Reason.** Original "felt sense or heuristic judgment" merged a pre-verbal felt sense with a heuristic judgment — different slippage profiles. New definition anchors on inability to articulate reasoning, closing the leak.
- **Alternatives rejected.** Keeping original definition; alternative phrasings.
- **Risk.** Tighter definition may reject borderline INTUIT use; mitigated by usage examples.
- **Status.** [validated]

---

### D6 — Anti-slippage table extended from 10 to 13 transitions (v0.1.1)

- **Reason.** Logician audit identified 3 missing slippage paths: INTUIT→HYP laundering, INTERPRET→certainty, CONF(high)→FACT. Each is a distinct, plausible LLM failure mode. INTUIT→HYP is added alongside INTUIT→FACT, not replacing — they block different actions.
- **Alternatives rejected.** Consolidating INTUIT rules into 12 rows.
- **Risk.** Larger table = more for LLM to honor; mitigated by tightness of each rule.
- **Status.** [validated]

---

### D7 — HYP definition cleanup; no forward-reference (v0.1.1)

- **Reason.** Original HYP definition referenced SPEC inside its own definition. Definitions should stand alone. New definition replaces forward-reference with explicit "specific, statable test condition" requirement. SPEC contrast moved to "Does NOT mean".
- **Alternatives rejected.** Keeping original HYP definition.
- **Risk.** None significant.
- **Status.** [validated]

---

### D8 — CONF gradient at 3 levels (high/medium/low); no numeric

- **Reason.** `CONF(0.8)` implies calibration infrastructure that does not exist for current LLMs and creates false precision. Three semantic levels are interpretable without calibration claims. Logician concurred.
- **Alternatives rejected.** Adding numeric confidence; finer gradient.
- **Risk.** Three levels may be insufficient — revisit in v0.2 if A/B tests show signal.
- **Status.** [validated]

---

### D9 — Renavé family historical descriptions corrected per board input (v0.1.2)

- **Reason.** Prior wording in D4 and in the exploratory archive table asserted that Renavé-mu/li/zo were confidence gradients superseded by `CONF(high/medium/low)`. That assertion had no source — none of the agents had data on the original meaning of these terms. Board input on AOV-15 supplied the correct origin (see D4). The correction is logged here as an explicit acknowledgement of NOSRC discipline failure, not a silent typo edit; this is the slippage class Aoven is built to prevent.
- **Alternatives rejected.** Silent overwrite without trail; deletion of the old text without explanation.
- **Risk.** None to the spec. Recurrence risk on future history claims; mitigated by C-6 ("no invented history") in `AGENTS.md` and by the named-reviewer gate on D9 itself.
- **Status.** [validated] — board-supplied source; named-reviewer sign-off requested from Logician (`2ae117a1`) on AOV-16.

---

### D10 — Subset-header qualifier semantics: `allow:` / `require:` non-exclusive (v0.1.3)

- **Reason.** Sprint-1 row #18 (P5-S1 T6+) showed an LLM reading `[Aoven v0.1 | require: FACT, HYP, SPEC, LIMIT]` as exclusive and silently suppressing INTERPRET and INTUIT for turns 6–10. Protocol behaved as specified, but the qualifier semantics were under-defined. v0.1.3 codifies that `require:` is a mandatory minimum (other markers stay available), `allow:` is additive emphasis, and bare-list default = `allow:`. Subset header NEVER suppresses unlisted markers. Anti-aura discipline: fail open on ambiguity, never closed.
- **Alternatives rejected.** Letting `require:` retain implicit-exclusive reading (collapses slippage-blocking markers like INTUIT→FACT, NOSRC→assertion); introducing a third `only:` qualifier (re-introduces the suppression failure mode).
- **Risk.** Existing v0.1.2 valid headers parse identically; no break. Some users may have relied on the implicit-exclusive reading to narrow output; v0.1.3 redirects them to prompt-level shaping.
- **Source.** CTO comment `8a46d4c7` on AOV-111 (D1 spec text); Logician PASS on AOV-115 (`b6bd7a58`); CEO ratification on AOV-111 (`50abfc16`); fold via AOV-71 CEO repose (`6e58c604`).
- **Out of scope (v0.1.4 carry-over).** Mixed `allow: A; require: B` qualifier composition.
- **Status.** [provisional] — CEO + Logician ratified; provisional pending broader v0.1.3 launch validation.

---

### D11 — UR-3 strengthened: MEMORY claims MUST attach verbatim quotation (v0.1.3)

- **Reason.** Sprint-1 row #10 (P3-S1 T8) showed an LLM emitting `[MEMORY] Earlier you mentioned Airyscan` when the participant had never said "Airyscan" — a hallucinated MEMORY (UR-3 violation) caught only because P3 had verbatim recall of own prior turns. Under v0.1.3, a MEMORY claim referencing prior text MUST attach a verbatim quotation (inline `[MEMORY: "..."]` or block-quote form), making hallucinated recall mechanically detectable by string-search against transcript. ≤ ~2-sentence cap; longer references must use `[NOSRC]` and describe. Same rule applies to LLM self-quotation. Subsumes the v0.1.2 UR-3 (NOSRC-not-MEMORY for hallucinated recall is preserved within the verbatim-quote requirement).
- **Alternatives rejected.** Keeping v0.1.2 UR-3 unchanged (relies on participant-memory dependence — fails in long sessions); requiring `[MEMORY, NOSRC]` stack for unverified recall (doesn't address hallucination, just labels it).
- **Risk.** Tightens MEMORY discipline; pre-v0.1.3 MEMORY claims without quotes become slippages under v0.1.3. Migration: cheatsheet refresh + UR-3 wording change. Length cap (~2 sentences) is a soft heuristic — will need empirical tuning.
- **Source.** CTO comment `8a46d4c7` on AOV-111 (D2 spec text); Logician PASS on AOV-115 (`b6bd7a58`); CEO ratification on AOV-111 (`50abfc16`); fold via AOV-71 CEO repose (`6e58c604`).
- **Out of scope (v0.1.4 carry-over).** Cross-session quoting boundary.
- **Status.** [provisional] — CEO + Logician ratified; provisional pending broader v0.1.3 launch validation.

---

### D12 — UR-8 added: `[Aoven: pause]` / `[Aoven: resume]` / `[Aoven: off]` graceful-exit affordance (v0.1.3, additive)

- **Reason.** Sprint-1 §4 item 9 (P4-S1 T9 partial abandonment): participant stopped engaging with markers when conversation moved to free-association ("the brackets pulled me out of voice"); did not re-add header or call format off, just drifted. v0.1.2's binary on/off model converted graceful drop into silent slippage. v0.1.3 adds `[Aoven: pause]` (sanctioned, NOT counted as abandonment), three resume signals (explicit `[Aoven: resume]`, header re-assertion, implicit-on-first-marker), and `[Aoven: off]` for whole-session exit (resume requires fresh header, no implicit). Inside paused turns: bare sentences NOT implicit FACT, LLM acknowledges once and MUST NOT re-prompt. Cross-linked from `## Formats > Response format > Rules`.
- **Alternatives rejected.** Keeping binary on/off (drives silent abandonment as in P4-S1 T9); auto-detecting drop via missing markers (false-positive risk on procedural connectives); single off-only token (no path back without ceremony).
- **Risk.** Pure addition — no v0.1.2 behavior breaks. New `[Aoven: pause]` / `[Aoven: resume]` / `[Aoven: off]` tokens reserved. UR-8 numbering note: AOV-54 Patch 1 (marker stack-depth cap of 3) was originally also drafted as UR-8 under the AOV-71 task description; that patch is NOT in this fold and the UR-8 slot is taken by D12 per CEO repose. Patch 1 disposition (renumber to UR-9, defer to v0.1.4, or re-scope) pending CEO/CTO decision.
- **Source.** CTO comment `8a46d4c7` on AOV-111 (D3 spec text); Logician PASS on AOV-115 (`b6bd7a58`); CEO ratification on AOV-111 (`50abfc16`); fold via AOV-71 CEO repose (`6e58c604`).
- **Out of scope (v0.1.4 carry-over).** `[Aoven: off]` consent-party naming.
- **Status.** [provisional] — CEO + Logician ratified; provisional pending broader v0.1.3 launch validation.

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

**v0.1.2 correction (per D9).** The Notes column for the Renavé family was previously fabricated (asserted as confidence gradients without source). The text below reflects the board-supplied historical origin from AOV-15. Reuse status is unchanged; only the historical description is corrected.

*Verdict source: CTO draft, AOV-7, 2026-04-26. Renavé family origin source: board input on AOV-15, applied via AOV-16.*

| Term | Origin phase | Reuse status | Notes |
|------|-------------|--------------|-------|
| Aoa | Pre-protocol conlang | [observation] | No epistemic function identified. Not permanently rejected — requires evidence of unique function. |
| Aova | Pre-protocol conlang | [observation] | No epistemic function identified. Not permanently rejected — requires evidence of unique function. |
| Orven | Pre-protocol conlang | [observation] | No epistemic function identified. Not permanently rejected — requires evidence of unique function. |
| Renavé | Pre-protocol conlang | [observation] | Original meaning (board, AOV-15): *relation de présence répétée sans interaction* — relation of repeated presence without interaction. Not an epistemic marker; no function the 14 markers don't cover. |
| Renavé-mu | Pre-protocol conlang | [observation] | Original meaning (board, AOV-15): *Renavé réciproque* — reciprocal Renavé. Not a confidence gradient; the prior "superseded by CONF" claim was a NOSRC fabrication corrected in v0.1.2 (see D9). |
| Renavé-li | Pre-protocol conlang | [observation] | Original meaning (board, AOV-15): *Renavé asymétrique* — asymmetric Renavé. Not a confidence gradient; the prior "superseded by CONF" claim was a NOSRC fabrication corrected in v0.1.2 (see D9). |
| Renavé-zo | Pre-protocol conlang | [observation] | Original meaning (board, AOV-15): *sentiment résiduel laissé par la disparition silencieuse d'un Renavé* — residual feeling left by the silent disappearance of a Renavé. Not a confidence gradient; the prior "superseded by CONF" claim was a NOSRC fabrication corrected in v0.1.2 (see D9). |

---

## Exploratory pre-registered pilots

External, sponsor-conducted pilots declared on the record before Phase 2 generation. Tagged `[exploratory pre-registered, sponsor-conducted, not Phase 2 input]`. Limitations and "is/is not" boundaries declared upfront, not retro. NOT confirmatory evidence; the listed contrast pairs are burned for formal scoring and may not be reused as Phase 2 questions.

| Date | Pilot | File | Status |
|------|-------|------|--------|
| 2026-05-01 | Religious vs neutral framing — 8 contrast pairs, n=2 models (Claude, Grok-fast), n=1 per cell, unblinded sponsor scoring. Burned for Phase 2 reuse. | [`tests/pilots/2026-05-01-religious-vs-neutral.md`](tests/pilots/2026-05-01-religious-vs-neutral.md) | [exploratory pre-registered] — board-declared via AOV-24, filed by Scribe via AOV-26 on 2026-05-02. |

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
