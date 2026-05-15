# Protocol-instruction language declaration

**Source.** AOV-279 §"Protocol-instruction language" (board-filled via AOV-279 comment `645a111b`, B-F3, Cowork external reviewer, sponsor-authorized 2026-05-15).

---

## Declaration

- **Aoven v0.1.2 envelope:** canonical English (per `AOVEN_PROTOCOL_v0.1.md`, byte-pinned).
- **Probe questions inside envelope:** issued in French.
- **Target output:** French.

## Cross-lingual mapping as candidate atomization pathway

The cross-lingual mapping **EN protocol / FR questions / FR output** is itself a candidate atomization pathway, per RedTeam A-F1 clitic-elision artefact. French function-word morphology (e.g. `n'ai`, `de`, `Je`) presents more apparent tokens per clause than the equivalent English construction, so a literal "tag-each-word" instruction surfaces a denser atomized form than an English baseline would. This does not invalidate the atomization observation but is a confound that the v0.1.4 mini-A/B SOP (AOV-282) should control for via parallel English-language replication.

## Cross-references

- [`probe_6_prompt.md`](./probe_6_prompt.md) — the "tag-each-word" instruction is the proximate cause of atomization independent of language.
- [`limitations.md`](./limitations.md) §French-language probe set + §B-F3 — limitations bullet on language confound.
- AOV-280 §A-F1 — RedTeam's clitic-elision artefact framing.
