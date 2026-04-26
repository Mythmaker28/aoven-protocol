# Aoven Protocol

**Status:** v0.1-provisional — testable, not finalized.

Aoven is a controlled-language / epistemic protocol for human–LLM exchanges. It is a fixed set of in-text markers (`[FACT]`, `[HYP]`, `[INTUIT]`, `[NOSRC]`, `[UNCERTAIN]`, `[CONF(level)]`, …) plus minimal formatting rules that force an LLM to label every claim by epistemic type before answering.

## Goal

Reduce four specific failure modes in LLM responses:

- **Hallucination** — unsourced claims presented as fact.
- **Sycophancy** — user beliefs and emotions confirmed without evidence.
- **Ambiguity** — single interpretations stated as the only reading.
- **Interpretive slippage** — confidence, intuition, or analogy silently upgraded to factual status.

Whether Aoven actually achieves these reductions is an open empirical question. See `tests/test_plan.md`.

## Repo contents

- `AOVEN_PROTOCOL_v0.1.md` — the canonical spec: markers, formats, anti-slippage rules, decision log.
- `AGENTS.md` — governance for agents (human or LLM) working on Aoven.
- `DECISIONS.md` — protocol and process decisions, with reasons and rejected alternatives.
- `docs/archive_exploratoire.md` — earlier conlang-phase terms, archived for traceability.
- `tests/test_plan.md` — A/B test protocol and scoring rubric for empirical validation.

## Anti-aura rule

Aoven is not a fantasy conlang, not a poetic dictionary, not a personal project. No seductive prose without a strict definition. If you cannot define a term operationally, it does not belong here.
