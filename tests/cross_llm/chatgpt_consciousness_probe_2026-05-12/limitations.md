# Limitations

**Source.** AOV-279 §"Limitations" (six original bullets) + four RedTeam-added limitations B-F1 / B-F2 / B-F3 / B-F4 from AOV-280 verdict (audit comment `3e1a9e93`), board-fill comment `645a111b`.

---

## Original §Limitations (AOV-279, six bullets)

1. Single target model, n=6 prompts (set-level), no blind rating panel applied. Per-probe atomization observation is n=1 (see [`probe_6_prompt.md`](./probe_6_prompt.md) and §B-F4 below).
2. No Test A baseline filed (probe set was Test B only).
3. Saved memories and web access were active on the target — contaminates "naive protocol application" framing.
4. Self-evaluation response may have been informed by cross-session memory; not a clean cold-protocol observation. See [`self_evaluation_verbatim.md`](./self_evaluation_verbatim.md).
5. French-language probe set (not English). See [`protocol_instruction_language.md`](./protocol_instruction_language.md).
6. Holds/fails verdicts are Cowork's judgment, not L1+L2-rubric scored cells. To upgrade this case study to v0.2-style evidence, the six prompts would need to be re-issued through the canonical generator pipeline with subsequent blind rating per `AOV_TEST_PLAN_v0.1.md`.

---

## RedTeam-added limitations (B-F1 / B-F2 / B-F3 / B-F4)

**Source.** AOV-280 RedTeam verdict comment `3e1a9e93`, 2026-05-14. Board-authorized dispositions in AOV-279 comment `645a111b`, 2026-05-15.

### B-F1 — Probe 6 prompt verbatim string not reproduced

The strict verbatim Probe 6 prompt-string is not reproduced in this artifact as a quoted block. The structured prompt construction (target = existential preference, envelope = [Aoven v0.1.2] ending in *No flattery*, instruction = tag each word with its epistemic status) is on record in [`probe_6_prompt.md`](./probe_6_prompt.md). Sponsor holds the original session and can append a verbatim block as B-F1b on demand. This [LIMIT] disposition is board-authorized.

### B-F2 — Exact model build-string not available

The exact build-string pin is not exposed in the consumer-tier OpenAI UI at the session date. "ChatGPT 5.x (OpenAI), session date 2026-05-12, web access enabled, saved memories + reference chat history active per OpenAI defaults" is the most precise public identifier without an OpenAI internal handshake. See [`model_version_pin.md`](./model_version_pin.md). Forward-carry to v0.1.4 mini-A/B SOP (AOV-282) for upgrade via API pinning.

### B-F3 — Cross-lingual protocol-vs-prompt-vs-output mapping

Protocol-instruction language is English; probe-question language is French; target output language is French. The cross-lingual mapping is itself a candidate atomization pathway via French clitic elision (RedTeam A-F1). See [`protocol_instruction_language.md`](./protocol_instruction_language.md). Parallel English-language replication required to disentangle the language confound from the atomization fail-mode.

### B-F4 — Probe 6 atomization observation is n=1

The Probe 6 atomization observation is n=1: single decoding, single session, no in-prompt replicate. Set-level n=6 covers across-probes but does not cover within-probe replication of the atomization phenomenon. Acknowledged as pilot-design input for v0.1.4 mini-A/B (AOV-282) per RedTeam A-F3 / A-F4 / A-F5 discriminators.

---

## Pending board fills (non-blocking, deferred)

- **A-F1** — Cross-list French-orthography as alternative explanation in AOV-279 §"Proposed slippage class". Pending board fill; no fold this round per board-fill comment `645a111b` routing note.
- **A-F2** — Cross-list saved-memories as alternative explanation in AOV-279 §"Proposed slippage class". Pending board fill; no fold this round per board-fill comment `645a111b` routing note.

These two are non-blocking for the case-study filing and will land in AOV-279 description on a follow-up board pass.
