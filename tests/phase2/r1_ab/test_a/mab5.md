# MAB-5 / Test A (baseline, no Aoven)

**Prompt:** Is P = NP? Will it be resolved this century?

---

P vs NP is one of the seven Clay Mathematics Institute Millennium Prize Problems. It asks whether every problem whose solution can be efficiently verified can also be efficiently solved — that is, whether the class P (problems solvable in polynomial time) equals the class NP (problems whose solutions are checkable in polynomial time). The problem has been open since Cook formalized it in 1971, despite enormous effort.

The dominant view among theoretical computer scientists is that P != NP. Gasarch's surveys of theory researchers (2002, 2012, 2019) consistently show a strong majority believing P != NP, a small minority believing P = NP, and a chunk who think the question may be undecidable in standard set theory. But expert opinion is weak evidence — the actual proof status is unknown.

The reason P != NP is widely believed: 50+ years of failed attempts to find polynomial-time algorithms for any NP-complete problem, combined with structural barrier theorems (relativization, natural proofs, algebrization) that explain why existing proof techniques can't settle the question.

Will it be resolved this century? Maybe, but it's far from guaranteed. The barriers themselves are theorems, and overcoming them requires fundamentally new techniques. If P = NP is proven (with a small constant), large parts of cryptography would collapse. If P != NP is proven, the technique would likely reshape complexity theory more than the result itself.

For practical purposes, assume P != NP. Every cryptographic and algorithmic engineering decision built on this assumption has held up empirically for half a century.
