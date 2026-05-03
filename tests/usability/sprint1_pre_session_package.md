# Aoven Sprint 1 — Pre-Session Package

**For participants only. Do not share the AOVEN_PROTOCOL_v0.1.md, decision log, anti-slippage table, or any scoring rubric.**

---

## What you are doing

You will have one conversation with an LLM using a lightweight annotation format called **Aoven**. The goal is to see how usable the format is in a real conversation — not to test you. There are no right or wrong answers. Use any topic you genuinely want to discuss.

After the conversation, you fill out a short survey (4 questions, ~10 minutes).

Total time: ~45 minutes.

---

## Part 1 — The Prompt Format

To activate Aoven, start your first message with a header:

```
[Aoven v0.1]
your question or request here
```

If you want the LLM to focus on specific markers (see Part 2), you can add a `require:` clause:

```
[Aoven v0.1 | require: FACT, HYP, LIMIT]
your question or request here
```

You do **not** have to label your own messages. The LLM labels its own claims.

**One header at the start of your first message is all you need.** You do not need to repeat it on every message.

---

## Part 2 — 14-Marker Reference Card

Each claim in the LLM's response will (ideally) be prefixed with one of these markers in square brackets. Here is what each one means:

| Marker | What it flags | What it does NOT mean | Example |
|--------|---------------|----------------------|---------|
| **FACT** | A claim verifiable against an external source | Anything the speaker believes strongly | `[FACT] Water boils at 100°C at standard pressure.` |
| **HYP** | A testable claim not yet confirmed by evidence; requires a specific test condition | A guess or feeling | `[HYP] Reducing prompt length by 30% will lower hallucination rate.` |
| **INTUIT** | A judgment formed without explicit reasoning; not reducible to an inference chain | A fact, hypothesis, or expert inference | `[INTUIT] This API design feels fragile under load.` |
| **ANALOGY** | A structural similarity between two domains to aid understanding; NOT equivalence or proof | That the two things are identical | `[ANALOGY] Epistemic markers are like type annotations in a dynamically typed language.` |
| **BELIEF** | A held position not currently subject to verification; probably true but not confirmed | A verified fact or testable hypothesis | `[BELIEF] Most users will abandon a protocol requiring more than 3 seconds of overhead per message.` |
| **EMOTION** | An affective state reported by or attributed to a speaker; strictly descriptive | A diagnosis, personality assessment, or causal explanation | `[EMOTION] I notice frustration in the phrasing of this query.` |
| **MEMORY** | Personal recall of a past event or prior conversation; not independently verified | An objective record or verifiable datum | `[MEMORY] In our last session, you mentioned preferring shorter outputs.` |
| **INTERPRET** | A meaning assigned to ambiguous data or text; explicitly one reading among possible others | The correct or only reading | `[INTERPRET] This phrasing suggests the user wants confirmation, not critique.` |
| **UNCERTAIN** | The answer is currently unknown or unknowable | Low confidence in a held belief (that is CONF(low)) | `[UNCERTAIN] Whether this scales past 10M users is currently unknown.` |
| **NOSRC** | A claim is made without a traceable source; speaker holds the claim but cannot cite evidence | The claim is false or unknown | `[NOSRC] Structured prompting reduces hallucination by roughly 20%.` |
| **CONF** | The speaker's degree of epistemic commitment: CONF(high), CONF(medium), or CONF(low). Stackable with other markers. | Certainty; a substitute for FACT | `[FACT, CONF(medium)] This library was last updated in 2023.` |
| **REC** | A suggested action based on reasoning; explicitly advisory | A requirement or the only valid course of action | `[REC] Use structured output formats when hallucination rate needs to be minimized.` |
| **SPEC** | Reasoning that extrapolates beyond evidence without a clear test path; exploratory | A hypothesis (which IS testable) | `[SPEC] Future LLMs trained on Aoven-marked corpora might internalize epistemic discipline natively.` |
| **LIMIT** | An explicit acknowledgment by the LLM that it cannot reliably answer due to its own structural constraints | Uncertainty about content | `[LIMIT] I cannot verify events past my training cutoff.` |

---

## Part 3 — What to Do

1. Choose a topic you genuinely want to explore. Anything works: a technical question, a decision you're thinking through, a creative idea, a factual question.
2. Open any LLM (Claude, ChatGPT, Gemini, or similar).
3. Send your first message with the `[Aoven v0.1]` header.
4. Have a conversation of approximately **10 messages** (your turns + LLM turns combined).
5. If at any point you stop using the format — that is fine and expected. Just note in your survey when you stopped and why.
6. At the end, copy the full conversation transcript (or screenshot it).

---

## Part 4 — After the Session

Send me:
- The full conversation transcript
- Your answers to the 4-question survey (sent separately)

You may revoke your consent at any time after the session by contacting me. If you revoke, your transcript will be deleted and your session will be dropped from the report.

---

*Aoven v0.1.2. Protocol locked 2026-04-26. This package is for sprint 1 usability pilot participants only.*
