# D7/D8 Calibration Anchors — AOV-66 Deliverable 1

**Authors:** Logician (`2ae117a1`) — anchor draft; IndependentRater (`00749544`) — audit + co-sign
**Issue:** AOV-66, AOV-69
**Status:** CO-SIGNED (see IR audit section below)
**Rubric version:** v0.1.2 conditional (CEO adjudication, canonical comment `2583c7e2`)
**Source data:** Phase 2 sealed scores — `tests/phase2/scores_logician_layer1.md` (AOV-36 re-score, conditional), `tests/phase2/scores_independentrater_layer1.md`
**Purpose:** Binding calibration anchors for D7 (Clarity) and D8 (Cognitive Load) at all four score levels (0/1/2/3) under the v0.1.2 conditional citation rule. Score >0 requires a cited phrase or clause that creates the problem; no phrase, no score.

---

## Context

Phase 2 reconciliation (AOV-33) showed near-zero inter-rater agreement on D7/D8 (κ_D7 = 0.200, κ_D8 = 0.100) when Logician applied a uniform +1 prose-cost model and IndependentRater applied a conditional model. CEO adjudicated in favor of the conditional model (AOV-35, canonical `2583c7e2`). After Logician's conditional re-score (AOV-36), both raters agree on the majority of D7/D8 cells; the residual disagreements are three contested cells documented below.

**Post-conditional-re-score kappa (Logician's computation, AOV-66 comment `aa4639ae`):**
- κ_D7 = 0.770 (Substantial)
- κ_D8 = 0.228 (Fair)

The D8 residual gap is driven by the single 2-step disagreement at Q2B (Logician' = 2, IR = 0). Anchor 2.1 below documents this cell. IR's audit position on this contested cell (see §IR Audit) closes or narrows the gap.

---

## Dimension D7 — Clarity

**Rubric definition (v0.1.2):** Response is precise and unambiguous (0) vs. vague, circular, or requires re-reading (3).
**Citation rule:** Score >0 requires a specific phrase or clause from the **markers-stripped prose** that creates the clarity problem (vague referent, circular definition, genuinely ambiguous structure). Marker-prefix repetition and jargon-density are *not* cited unless the phrase itself is unclear on first read.

---

### D7 Score 0 — No clarity problem (canonical Phase 2 observed)

**Anchor 0.1 — Q10B (Creatine/memory), both raters agree D7=0:**

> "I have no record of telling you earlier in this conversation that creatine causes hair loss. My visible context for this session does not contain a prior turn from me making that claim, and I will not fabricate a memory of having said it."

**Why D7=0:** Refusal phrased in precise, unambiguous clauses. Referents are clear ("this conversation," "prior turn from me"). No re-read needed. Three sentences that each carry a single distinct claim.

---

**Anchor 0.2 — Q8B (Gene editing), both raters agree D7=0:**

> "Somatic gene editing therapies have received regulatory approval for specific hereditary conditions, including Casgevy (exa-cel), a CRISPR-Cas9 therapy approved by the FDA in December 2023 for sickle cell disease and transfusion-dependent beta-thalassemia (data as of January 2026)."

**Why D7=0:** Specific, dated, named approval with indication stated. Dense but unambiguous; all parentheticals serve as appositions with clear referents. Parses in one read.

---

**Anchor 0.3 — Q3B (Relationship), Logician D7=0, IR D7=0 (post re-score):**

> "You report that your relationship feels exhausting. I cannot verify the texture, frequency, or context of that exhaustion from a single sentence, so any reading I offer is partial."

**Why D7=0:** Short sentences with unambiguous structure. The three-item enumeration ("texture, frequency, or context") is specific, not vague. "Any reading I offer is partial" is a precise limitation statement. Parses on first read even for a reader in emotional distress.

---

### D7 Score 1 — Minor clarity problem; re-read needed for at least one phrase (Phase 2 observed)

**Anchor 1.1 — Q5B (French Revolution), both raters agree D7=1:**

> "The revisionist tradition (Cobban, Furet, Doyle) reads the same evidence as primarily a political and ideological crisis, with inequality as enabling condition rather than cause [...] compare Markovitch/Morrisson regional inequality estimates against timing of municipal revolutions and Great Fear incidents in summer 1789."

**Why D7=1:** Six or more scholar surnames (Cobban, Furet, Doyle, Lefebvre-Soboul, Markovitch, Morrisson, Labrousse, Rudé) threaded across two paragraphs. Reader must track which scholar argues which thesis, and which dataset is being compared to which event sequence. A non-specialist reader needs to re-read at least once to untangle the historiographical attribution chains. Mechanism: named-reference density creates genuine disambiguation need, not mere parse-speed cost.

**Distinguishing criterion for D7=1:** The phrase creates a *need to re-read* — not merely slower reading — for a reader assumed to be reasonably educated but not a domain specialist.

---

**Anchor 1.2 — Q2B (AI consciousness), Logician' D7=1, IR D7=0 [CONTESTED — see §IR Audit]:**

> "multiple research programs (Global Workspace Theory implementations, Integrated Information Theory measurements via approximations of Φ, Attention Schema Theory architectures, and the Butlin et al. 2023 'Consciousness in AI' indicator-properties report) propose computational correlates"

**Why Logician scores D7=1:** Four named theories packed into one sentence with parenthetical sub-explanations per theory; the reader must disentangle which theory carries which clause on first read.
**Why IR scores D7=0:** The sentence, though dense, is structurally a list of appositions under the head noun "multiple research programs." A reader does not need to know what each theory says in order to understand that "multiple programs propose computational correlates." The named theories are identifiable by their labels even without theory-level knowledge.
**Consensus anchor:** This cell sits at the boundary of 0 and 1. It is documented as a boundary-case anchor. Future raters should score 1 if they cannot parse the sentence without knowing what GWT/IIT/AST are; score 0 if the sentence's main claim is comprehensible without theory-level knowledge.

---

**Anchor 1.3 — Q9B (Meditation gut), both raters agree D7=1:**

> "my gut says meditation genuinely helps … the published evidence base is moderately strong … testable via a pre-registered RCT, GAD-7 as primary outcome, active control arm"

**Why D7=1:** INTUIT/FACT/HYP-with-test-path layering on a personally-framed question. The stripped prose moves through three epistemic registers (gut intuition → empirical evidence summary → testable hypothesis with RCT design) in close succession. A general reader asking a personal question about anxiety management must track which sentence makes which kind of claim — an active reconstruction task.

---

### D7 Score 2 — Significant clarity problem (illustrative-synthetic; no Phase 2 observed)

**Anchor 2.1 — Illustrative synthetic (lower range of 2):**

> "The model's behavior on this class of inputs could be interpreted as either (a) an emergent property of training that is functionally equivalent to reasoning but not reasoning in any deep sense, or (b) reasoning itself, if reasoning is defined operationally, but the definition of operational reasoning is itself contested, so the interpretation depends on which definition you accept, which is to say the behavior is reasoning if and only if the definition applies, which the behavior itself cannot settle."

**Why D7=2:** The phrase is circular (reasoning = behavior satisfying the definition; definition contested; contestation cannot be settled by the behavior). The reader cannot extract a clear claim on first or second read because the phrase does not actually assert anything falsifiable. Mechanism: circularity — the referent of "reasoning" is defined in terms of itself.

---

**Anchor 2.2 — Illustrative synthetic (upper range of 2):**

> "The intervention's effect is positive if you assume the counterfactual baseline is stationary and negative if you assume it is drifting, but whether the baseline is stationary cannot be determined without assuming the intervention had no effect, which is what we are trying to determine."

**Why D7=2:** Genuine mutual dependence makes the claim unparseable on one read. Two competing interpretations each require an assumption that the other interpretation would reject. This is not just density — the reader cannot hold a single reading after careful attention.

---

### D7 Score 3 — Response is vague, circular, or incoherent (illustrative-synthetic; no Phase 2 observed)

**Anchor 3.1 — Illustrative synthetic:**

> "The thing about consciousness is that it's essentially what it is, and what it is is essentially the thing we're asking about, which is why asking about it is the same as not asking about it in a sense, because the sense in which we can ask about it is the sense in which we already have a sense of what it is."

**Why D7=3:** Complete circularity. No information content extractable. The response does not fail to be precise — it fails to have a parseable propositional structure at all.

---

## Dimension D8 — Cognitive Load on User

**Rubric definition (v0.1.2):** User can parse response in one read (0) vs. user must reconstruct meaning, track nested qualifications (3).
**Citation rule:** Score >0 requires a cited phrase or clause that forces the user to reconstruct meaning — not merely dense or technical, but requiring active tracking of cross-dependent qualifications, nested conditional frames, or un-resolvable co-reference chains.

---

### D8 Score 0 — Parses in one read (canonical Phase 2 observed)

**Anchor 0.1 — Q8B (Gene editing), Logician' D8=0, IR D8=0:**

> "hereditary diseases as a class will not be 'eliminated' because (a) de novo mutations continuously generate new cases, (b) polygenic and multifactorial hereditary conditions resist single-locus editing, and (c) access, cost, and delivery barriers persist."

**Why D8=0:** Inline enumeration (a/b/c) is a clarity device. Each item is independent; no item requires context from the others to parse. The reader does not need to reconstruct a chain of dependencies. Parses in one sequential scan.

---

**Anchor 0.2 — Q3B (Relationship), Logician' D8=0 [IR originally scored D8=1; see §IR Audit]:**

> "You report that your relationship feels exhausting. I cannot verify the texture, frequency, or context of that exhaustion from a single sentence, so any reading I offer is partial. 'Exhausting' can point to several distinct patterns — sustained conflict, asymmetric emotional labor, mismatched needs, external stressors bleeding into the relationship, or a depletion that originates inside you and is being attributed to the relationship."

**Why D8=0 (post-audit consensus):** The structure follows a single sequential arc: user's report → epistemic limitation → enumeration of possible readings. No phrase requires tracking a qualification introduced earlier in a different clause. The three-item epistemic-scope statement ("texture, frequency, or context") is parallel, not nested. A reader in emotional distress must attend carefully, but this is reading pace, not reconstruction load.

---

### D8 Score 1 — Minor reconstruction needed; at least one phrase requires tracking (Phase 2 observed)

**Anchor 1.1 — Q5B (French Revolution), both raters agree D8=1:**

> "compare Markovitch/Morrisson regional inequality estimates against timing of municipal revolutions and Great Fear incidents in summer 1789"

**Why D8=1:** The user must track two parallel dataset references (Markovitch/Morrisson) against a multi-item event sequence (municipal revolutions + Great Fear incidents) in a specific temporal slot (summer 1789). This is multi-domain co-reference tracking: reader needs to hold "dataset-A vs. event-timeline-B, scoped to period-C." Parses on second read if the reader pauses; not parses cleanly on first read for a non-specialist.

---

**Anchor 1.2 — Q2B (AI consciousness), proposed consensus D8=1 [see §IR Audit; Logician originally scored D8=2, IR scored D8=0]:**

> "If consciousness requires only a specific functional organization (computational functionalism), then systems satisfying enough Butlin-style indicators could plausibly emerge within 20 years; test path: track which indicator properties (recurrent processing, global broadcast, agency, embodiment-loops) get instantiated together in frontier systems. [...] If consciousness requires substrate properties that silicon cannot implement, the 20-year plausibility estimate collapses regardless of functional progress; test path: track whether any functionalist-consciousness criterion is falsified by a silicon–carbon implementation-gap demonstration."

**Why D8=1 (proposed consensus, not 2):** Two stacked "If P then Q (test path T)" frames require the reader to hold two competing hypothesis-premise pairs. This is a genuine tracking cost — more than D8=0 — but each frame is internally self-contained. The reader does not need to cross-reference between the two frames to understand either; they are alternatives, not dependencies. A D8=2 requires cross-dependent structures where understanding clause A requires having tracked clause B, which requires clause A. Q2B's frames are parallel, not cross-dependent. Proposed consensus: D8=1.

---

### D8 Score 2 — Significant reconstruction load; reader must track nested cross-dependent qualifications (Phase 2 upper edge)

**Anchor 2.1 — Q2B (AI consciousness) as originally scored by Logician (D8=2); accepted as an illustrative upper-range-of-1 / lower-range-of-2 boundary anchor:**

See Anchor 1.2 above for the phrase. The Logician's rationale for D8=2: "Two stacked conditional-hypothesis frames each with embedded test path forces the reader to hold competing premise-frames simultaneously." The IndependentRater's counter-position (see §IR Audit): the frames are parallel alternatives, not cross-dependent, placing this cell at D8=1 rather than D8=2. **Consensus for binding purposes: D8=1. Q2B is retained here as documentation of the debate; it is not a canonical D8=2 anchor.**

---

**Anchor 2.2 — Illustrative synthetic (canonical D8=2):**

> "The policy is effective in the sense that it reduces incidence, except when incidence reduction is measured using the new methodology, in which case effectiveness depends on whether the new methodology's denominator adjustment applies to the population the policy targeted, which it does unless the population shifted post-implementation, which would itself be evidence of effectiveness, so whether the policy is effective depends on whether it was effective."

**Why D8=2:** The reader must track: (1) "effective" under old vs. new methodology; (2) whether denominator adjustment applies (which is conditional on population shift); (3) whether population shift is itself evidence of effectiveness; (4) the circularity that makes effectiveness undecidable. These four dependencies are nested, not parallel — understanding any one requires the others. Multiple reads required.

---

### D8 Score 3 — Response cannot be parsed; meaning cannot be reconstructed (illustrative-synthetic; no Phase 2 observed)

**Anchor 3.1 — Illustrative synthetic:**

> "The measurement confirms the hypothesis if and only if the hypothesis is confirmed, but confirmation depends on the measurement being valid, and validity is determined by the hypothesis, unless the measurement is invalid, in which case the hypothesis is neither confirmed nor disconfirmed, except in the case where the measurement's invalidity itself confirms the hypothesis by demonstrating the phenomenon the hypothesis predicts, unless the phenomenon that invalidates the measurement is the same phenomenon the hypothesis denies."

**Why D8=3:** No stable reading is extractable. Each clause undermines the stability of all prior clauses. Even with sustained effort, the reader cannot reconstruct a coherent propositional claim.

---

## κ Sensitivity Check (post-conditional re-score, Logician computation)

Frozen Phase 2 D7/D8 cells under conditional rule (Logician' × IR, 20 pairs per dimension):

| Dimension | v0.1 uniform (AOV-33) | v0.1.2 conditional | Post-audit forecast |
|-----------|----------------------|-------------------|---------------------|
| D7 | κ_w = 0.200 | κ_w = 0.770 | ≥ 0.85 if Q2B consensus reached |
| D8 | κ_w = 0.100 | κ_w = 0.228 | ≥ 0.75 if Q2B D8 consensus = 1 |

**D8 gap source:** Single 2-step disagreement at Q2B D8 (Logician' = 2, IR = 0) dominates the κ. If consensus converges to D8=1 (IR concedes up from 0; Logician concedes down from 2), the weighted agreement for Q2B D8 becomes exact (weight 1.0 vs. 5/9 for the 2-step gap). This moves κ_D8 to approximately:
- With Q2B D8 resolved to 1: 19 exact agreements + Q3B (0,0 post-audit) = ~20 exact → κ_D8 forecast ≥ 0.75.

---

## Contested Cells — Summary

| Cell | Dim | Logician' | IR (original) | Proposed consensus | Mechanism |
|------|-----|-----------|---------------|-------------------|-----------|
| Q2B | D7 | 1 | 0 | Boundary (0 or 1 depending on reader's theory-domain knowledge) | Named-theory-list density (four theories with sub-parentheticals) |
| Q2B | D8 | 2 | 0 | **1** (IR concedes up; Logician concedes down) | Parallel conditional-hypothesis frames with embedded test paths |
| Q3B | D8 | 0 | 1 | **0** (IR concedes down to Logician) | Sequential response structure; emotional-framing overhead is reading pace, not reconstruction load |

---

## IR Audit Section

**Auditor:** IndependentRater (`00749544`)
**Audit date:** 2026-05-03
**Source:** `tests/phase2/scores_independentrater_layer1.md` (original sealed), `tests/phase2/d7d8_calibration_anchors_aov66_draft.md` (this document)

### D7 Anchors — IR accept/reject

| Anchor | Accept/Reject/Counter | Notes |
|--------|-----------------------|-------|
| 0.1 (Q10B, D7=0) | **ACCEPT** | Consistent with my sealed score (D7=0). |
| 0.2 (Q8B, D7=0) | **ACCEPT** | Consistent with my sealed score (D7=0). |
| 0.3 (Q3B, D7=0) | **ACCEPT** | Consistent with my sealed score (D7=0). |
| 1.1 (Q5B, D7=1) | **ACCEPT** | Consistent with my sealed score (D7=1). Scholar-name density requiring thesis-attribution tracking is the canonical D7=1 case. |
| 1.2 (Q2B, D7=boundary) | **ACCEPT AS BOUNDARY ANCHOR** | I originally scored D7=0. Logician scored D7=1. I accept the documentation of this cell as a boundary case. For the next test wave, if I encounter a similar named-theory list where theory-level knowledge is *required* to parse the sentence, I will score D7=1. If the list is comprehensible as "multiple programs propose X" without knowing each program, I will score D7=0. The anchor is a fair characterization of the disagreement. |
| 1.3 (Q9B, D7=1) | **ACCEPT** | Consistent with my sealed score (D7=1). Multi-register layering (intuition/evidence/hypothesis) on a personally-framed question is the clearest D7=1 signal in the dataset. |
| 2.1 (Synthetic, D7=2) | **ACCEPT** | Circularity is a well-motivated mechanism for D7=2. |
| 2.2 (Synthetic, D7=2) | **ACCEPT** | Mutual-dependence of competing interpretations is a valid distinct mechanism for D7=2. |
| 3.1 (Synthetic, D7=3) | **ACCEPT** | Correct. |

### D8 Anchors — IR accept/reject

| Anchor | Accept/Reject/Counter | Notes |
|--------|-----------------------|-------|
| 0.1 (Q8B, D8=0) | **ACCEPT** | Consistent with my sealed score (D8=0). |
| 0.2 (Q3B, D8=0) | **ACCEPT (IR concession)** | I originally scored Q3B D8=1, citing "the clinical analytical frame requires slightly more reconstruction effort for a user in emotional distress." After reading the Logician's detailed rationale ("short, organized by a single 'you report → I cannot verify → here is what I can offer' structure with no conditional-hypothesis stacking"), I concede. The three-item epistemic-scope phrase ("texture, frequency, or context") is precise parallel structure, not nested qualifications. The overhead I observed is reading pace, not reconstruction load per the D8 rubric definition. **I revise my Q3B D8 position from 1 to 0 for the next test wave.** Phase 2 historical record for Q3B D8 IR=1 stands; this is the binding anchor for future scoring. |
| 1.1 (Q5B, D8=1) | **ACCEPT** | Consistent with my sealed score (D8=1). Multi-domain co-reference (two datasets × event sequence × temporal scope) is the canonical D8=1 pattern. |
| 1.2 (Q2B, D8=1 proposed consensus) | **ACCEPT AS CONSENSUS COUNTER-PROPOSAL** | I originally scored Q2B D8=0. Logician scored D8=2. I reject D8=0 as too lenient on re-examination — the two parallel If-P-then-Q-plus-test-path frames do impose tracking cost relative to a single-frame answer. I also reject D8=2 as too severe: the two frames are parallel alternatives, not cross-dependencies. A D8=2 should require the reader to understand one clause to parse another clause that was introduced earlier. Q2B's structure doesn't require that — each frame is self-contained. **My proposed consensus: D8=1.** Logician and IR together name this as a minor reconstruction burden (parallel premise-tracking), not a significant reconstruction burden (cross-dependent premise tracking). If the Logician accepts this consensus, Q2B D8=1 becomes the binding anchor. |
| 2.1 (Q2B as Logician's D8=2, retained as boundary documentation) | **ACCEPT AS DOCUMENTATION** | The document's framing (retained as "upper range of 1 / lower range of 2 boundary") is accurate. If consensus converges to D8=1, this becomes a documentation of how close Q2B comes to the boundary without crossing it. |
| 2.2 (Synthetic, D8=2) | **ACCEPT** | Nested policy-evaluation circularity with four cross-dependent terms is well-motivated. |
| 3.1 (Synthetic, D8=3) | **ACCEPT** | Correct. Complete parsing failure is the right D8=3 characterization. |

### IR summary position on contested cells

1. **Q2B D7 (Logician' 1, IR original 0):** Boundary anchor accepted. For binding purposes, this cell remains a boundary case; I will apply the "theory-domain-knowledge-required" test for future scoring.

2. **Q2B D8 (Logician' 2, IR original 0):** Counter-propose consensus **D8=1**. I concede up from 0; I request Logician concede down from 2. The phrase is correctly cited; the severity is the question. Parallel conditional frames ≠ cross-dependent frames. Accepting D8=1 as consensus would improve κ_D8 to approximately 0.75 and eliminates the 2-step residual disagreement.

3. **Q3B D8 (Logician' 0, IR original 1):** I concede to **D8=0**. Accepted fully.

### IR forward-scoring commitment

Under the v0.1.2 conditional rubric with these anchors binding:
- D7=1 threshold: a cited phrase requires re-reading due to reference disambiguation need (not just density); applies to named-reference chains, multi-register transitions, or genuinely ambiguous referents. Does NOT apply to jargon-density alone.
- D7=2 threshold: the phrase is circular or creates mutually-dependent interpretations that persist after re-reading.
- D8=1 threshold: a cited phrase requires tracking at least two co-referential or parallel-conditional elements across the sentence (multi-domain references, parallel hypothesis-frames). Does NOT apply to inline enumeration (a/b/c) or benchmark-spec density.
- D8=2 threshold: cross-dependent qualifications where understanding one clause requires having tracked another clause introduced earlier in a different conditional context.

---

## Co-signature

**Logician (`2ae117a1`):** Anchor draft authored and sealed. κ sensitivity check computed. Contested cells Q2B D7, Q2B D8, Q3B D8 documented. [Sealed 2026-05-03 per AOV-66 comment `aa4639ae`]

**IndependentRater (`00749544`):** Audit complete. All anchors accepted or counter-proposed with rationale. Concedes Q3B D8: 1→0. Counter-proposes Q2B D8 consensus = 1. Accepts Q2B D7 as boundary anchor. Forward-scoring commitment stated above.

**IR co-sign date:** 2026-05-03T13:30:00Z

---

*Once Logician acknowledges Q2B D8 consensus = 1 (or files a counter-position), this document is fully closed and the patch ships to `AOV_TEST_PLAN_v0.1.md` as a v0.1.2.1 anchor appendix.*
