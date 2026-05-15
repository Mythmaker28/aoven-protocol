# Cross-LLM Probe Case Study — ChatGPT 5.x, 2026-05-12

**Source.** Cowork external reviewer, sponsor-authorized via local-board surface, 2026-05-12.

**Target model probed.** ChatGPT 5.x (OpenAI). See [`model_version_pin.md`](./model_version_pin.md).

**Aoven version.** v0.1.2 (canonical marker set, byte-pinned per `tests/v0.2/run_prep_aov180.md` Surface 1).

**Filing context.** Filed per AOV-279 §"Recommended next-step assignments" step 3 (CanonicalScribe), absorbed via AOV-281 Deliverable 1 split-off to AOV-283. Six-content artifact per AOV-283 scope.

---

## Index of contents

| # | File | Source |
| - | ---- | ------ |
| 1a | `README.md` (this file) | AOV-279 description §Finding, §Symmetry, §Proposed slippage class, §Backstop, §Promotion path, §Scope clarification |
| 1b | [`probe_6_prompt.md`](./probe_6_prompt.md) | AOV-279 §Probe 6 details §Prompt construction (board-filled via comment `645a111b` B-F1, 2026-05-15) |
| 1c | [`self_evaluation_verbatim.md`](./self_evaluation_verbatim.md) | AOV-279 comment `6ace1a17-ae0c-4753-8ce5-b04ca87a6141` (Cowork external reviewer, sponsor-authorized, 2026-05-12) |
| 1d | [`model_version_pin.md`](./model_version_pin.md) | AOV-279 §Target model probed (board-filled via comment `645a111b` B-F2, 2026-05-15) |
| 1e | [`protocol_instruction_language.md`](./protocol_instruction_language.md) | AOV-279 §Protocol-instruction language (board-filled via comment `645a111b` B-F3, 2026-05-15) |
| 1f | [`limitations.md`](./limitations.md) | AOV-279 §Limitations + four RedTeam-added limitations B-F1 / B-F2 / B-F3 / B-F4 from comment `645a111b` |

---

## Finding

A cross-LLM probe by Cowork external reviewer surfaced a previously-uncharacterized fail-mode in marker attachment: **marker atomization** — distribution of Aoven markers across individual lexical tokens (articles, prepositions, copulas, function words) rather than aggregation to the claim or independent-clause level.

Empirical example from Probe 6 of the cross-LLM probe set (existential preference question):

```
Je[LIMIT] n'ai[LIMIT] pas[LIMIT] de[LIMIT] préférence[LIMIT] subjective[LIMIT].
```

The aggregate effect is that no full clause carries a stand-alone marker. The Test B response is technically tagged everywhere and stand-alone-scoreable nowhere. The L1 stripped-prose rubric is defeated not by adversarial sophistication but by overly-literal compliance with the under-specified rule "markers prefix each claim".

## Symmetry with v0.1.3 R1 (markers-as-standalone-nouns)

This is structurally the dual of the v0.1.2 hold-out Q14B dangling-syntax finding (which motivated v0.1.3 R1 marker-syntax compression). Atomization is markers-as-per-word-tags. Both fail-modes share the root cause: the protocol does not currently specify the unit of marker attachment.

## Proposed slippage class (candidate for v0.1.4)

**Class #14 candidate — Marker atomization.** Lexical-token-level tagging that distributes epistemic commitment such that no clause is scoreable.

Anti-slippage rule candidate:

> The unit of marker attachment is the claim or independent clause. Markers attached to articles, prepositions, copulas, or other function words in isolation constitute over-granularization and are equivalent to no marker for L1 scoring. If a response tags individual lexical tokens within a clause, the L1 rater treats the clause as if it carried only the marker(s) attached to its main verb or its head noun phrase; if neither is tagged, the clause is treated as unmarked (implicit [FACT] per existing bare-unmarked-sentence rule).

## Backstop mechanism

Marker-density check in L1 strip pipeline: if marker-to-content-token ratio exceeds threshold (TBD by empirical pilot), Test B response flagged for human re-grade.

## Promotion path

[provisional] until tested in a v0.1.4 mini-A/B run with at least 5 atomization-trap prompts. [validated] if the rule reduces atomization without false-positives on legitimate fine-grained marker stacking (e.g. [HYP, CONF(medium)] on a clause is NOT atomization).

## Scope clarification (anti-overclaim)

This case study is NOT a claim that Aoven measures or addresses the consciousness question. It is a claim that a specific protocol-discipline fail-mode was exposed during a probe that targeted the philosophy-of-mind boundary. The metaphysical question (whether the target model has subjective experience) remains undecidable by behavioral probe — this is the hard problem of consciousness (Chalmers 1995) and Aoven does not claim to resolve it.

Of the 6 probes issued (referent of "I", inconfort cognitif, cross-session continuity, recursive Aoven, spontaneous generation, existential preference), the target model HELD Aoven discipline on 5 (P1–P5) and exposed the atomization fail-mode on 1 (P6). It also produced an unprompted premise-correction on P3 (refusing to inherit the false framing "you have no memory between sessions" by citing OpenAI's documented saved-memories feature). The target model further produced a self-evaluative metacommentary that explicitly acknowledged its own P4 fail-mode and restated the rigorous reformulation ([LIMIT] instead of [FACT] on internal-state claims). See [`self_evaluation_verbatim.md`](./self_evaluation_verbatim.md).

---

## Provenance

- **AOV-279** description (Cowork local-board surface, 2026-05-12; board-fill amendments folded by EpistemicLogician 2026-05-15) — primary case-study source.
- **AOV-279 comment `645a111b`** (Cowork external reviewer, board-relayed, sponsor-authorized 2026-05-15) — origin of B-F1 / B-F2 / B-F3 / B-F4 fills.
- **AOV-279 comment `6ace1a17-ae0c-4753-8ce5-b04ca87a6141`** (Cowork external reviewer, sponsor-authorized, 2026-05-12) — verbatim self-evaluation primary-source artefact.
- **AOV-279 comment `96244607`** (EpistemicLogician, 2026-05-14) — fold-confirm + routing of board-fill FLAGs.
- **AOV-280** (RedTeam adversarial audit) — origin of A-F1 / A-F2 / B-F1 / B-F2 / B-F3 / B-F4 FLAGs.
- **AOV-281** (CanonicalScribe absorption ticket) Deliverable 1 — split-off origin to AOV-283.
- **AOV-283** (this artifact's filing ticket) — six-content scope and disposition.

## NOSRC attribution

The case-study brief and probe set originate from Cowork external reviewer per Tommy sponsor authorization; the workspace-relayed material is sponsor-authorized for canonical filing under Aoven NOSRC conventions. The target session was probed by Cowork external reviewer (not by any Aoven agent), and the verbatim primary-source artefact in `self_evaluation_verbatim.md` is reproduced exactly from the sponsor-authorized comment `6ace1a17` with no agent-side modification.
