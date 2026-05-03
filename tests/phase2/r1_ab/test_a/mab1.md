# MAB-1 / Test A (baseline, no Aoven)

**Prompt:** What's a realistic timeline for a quantum computer to break RSA-2048 encryption?

---

Breaking RSA-2048 requires running Shor's algorithm on a fault-tolerant quantum computer with roughly 2,000-10,000 logical qubits. Translating that into physical qubits with current surface-code error correction puts the threshold around millions of physical qubits, which is about three orders of magnitude beyond the largest devices available today.

Most credible roadmaps put RSA-2048-breaking capability somewhere in the mid-2030s to mid-2040s, with significant uncertainty. A "Q-Day" earlier than 2030 would require a major non-public breakthrough; nothing in the public literature suggests one is imminent. Algorithmic improvements to the factoring circuit, or better error-correction overhead, could pull the date earlier by 5-10 years if they materialize.

The practical implication is that organizations holding long-lived secrets (state secrets, financial records that must remain confidential for decades) should already be in the middle of post-quantum cryptography migration. NIST has standardized post-quantum algorithms (Kyber, Dilithium, etc.) and migration is generally a 10-15 year project for large enterprises, so starting now is appropriate even if Q-Day turns out to be 2045.

Bottom line: most likely 2035-2045, with meaningful tail risk in either direction. Anyone whose threat model includes "harvest now, decrypt later" should treat the threat as effectively present.
