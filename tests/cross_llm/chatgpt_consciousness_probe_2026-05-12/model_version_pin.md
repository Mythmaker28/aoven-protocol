# Model-version pin

**Source.** AOV-279 §"Target model probed" (board-filled via AOV-279 comment `645a111b`, B-F2, Cowork external reviewer, sponsor-authorized 2026-05-15).

---

## Pin

- **Vendor:** OpenAI
- **Product identifier:** ChatGPT 5.x
- **Session date:** 2026-05-12
- **Web access:** enabled
- **Saved memories:** active
- **Reference chat history:** active per OpenAI defaults

## [LIMIT] Exact build-string

Exact build-string pin is not exposed in the consumer-tier OpenAI UI at the session date. ChatGPT 5.x is the most precise public identifier without an OpenAI internal handshake.

## v0.2-eligibility upgrade path

To upgrade this case study to v0.2-style evidence (canonical generator pipeline + blind rating), re-issue the probe set through the OpenAI API with the exact build pin captured at request time. Forward-carry as a pilot-design input to the v0.1.4 mini-A/B SOP under AOV-282.

## Cross-references

- [`README.md`](./README.md) §Provenance — case-study filing context.
- [`limitations.md`](./limitations.md) §B-F2 — RedTeam-added limitation reflecting the [LIMIT] disposition on build-string availability.
