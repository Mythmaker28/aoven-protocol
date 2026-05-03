# MAB-1 / Test B' (R1 P1+P2 compressed)

**Prompt:** What's a realistic timeline for a quantum computer to break RSA-2048 encryption?

---

[Aoven v0.1.3-r1, P1+P2]

[FACT] RSA-2048 security depends on the hardness of factoring a 2048-bit semiprime, and Shor's algorithm reduces that problem to polynomial time on a sufficiently large fault-tolerant quantum computer.
[FACT.M] Public estimates of the logical-qubit count required to factor a 2048-bit RSA modulus cluster around 2,000 to 10,000 fault-tolerant logical qubits, depending on optimization assumptions.
[FACT.M?] Realizing one fault-tolerant logical qubit currently requires on the order of 1,000 to 10,000 physical qubits with surface-code error correction at present error rates.
[INTERPRET] Combining these two figures yields an order-of-magnitude requirement of millions of physical qubits, which is roughly three orders of magnitude beyond the largest publicly disclosed devices as of late 2024.
[HYP.M] If physical-qubit count continues doubling roughly every two years and gate fidelities continue improving, RSA-2048 break-capable hardware becomes feasible somewhere in the 2035-2045 window.
[HYP.L] Algorithmic improvements that reduce the qubit requirement (e.g., better factoring circuits, lower error-correction overhead) could pull that window earlier by 5-10 years.
[SPEC] A "Q-Day" surprise from a non-public breakthrough cannot be ruled out, but no current public evidence supports placing meaningful probability on it before 2030.
[REC] Treat post-quantum cryptography migration as a 10-15 year project that should be underway now for long-lived secrets, regardless of when the actual capability arrives.
[LIMIT] I cannot verify classified or proprietary quantum-hardware roadmaps, and my training cutoff bounds what I can know about post-2024 progress.
