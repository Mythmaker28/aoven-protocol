"""R1 compression normalizer — re-expand P1, P2, P3 forms to v0.1.2 long form.

Mechanical round-trip verifier for AOV-37/AOV-68/AOV-72.
Mods folded in per AOV-68 verdict cb33d2b8:
    - RATIFIED_MARKERS = canonical 14 from AOVEN_PROTOCOL_v0.1.md §Markers.
    - expand_p3_block distributes header marker + default CONF to each bullet.

Run as a script: `python tests/phase2/r1_normalizer.py` -> 6/6 PASS expected.
"""

import re
import sys

RATIFIED_MARKERS = {
    "FACT", "HYP", "INTUIT", "ANALOGY", "BELIEF", "EMOTION", "MEMORY",
    "INTERPRET", "UNCERTAIN", "NOSRC", "CONF", "REC", "SPEC", "LIMIT",
}

CONF_MAP = {"H": "high", "M": "medium", "L": "low"}


def expand_p1(text: str) -> str:
    """`[X.<lvl>]` -> `[X][CONF(level)]`. Also handles `[X.<lvl>?]` (P1+P2 stacked)."""
    def repl(m):
        marker = m.group(1)
        lvl = m.group(2)
        q = m.group(3) or ""
        if marker not in RATIFIED_MARKERS or marker == "CONF":
            return m.group(0)
        long = f"[{marker}][CONF({CONF_MAP[lvl]})]"
        if q == "?":
            if marker == "FACT":
                long += "[NOSRC]"
            else:
                return m.group(0)
        return long
    return re.sub(r"\[([A-Z]+)\.([HML])(\??)\]", repl, text)


def expand_p2(text: str) -> str:
    """`[FACT?]` -> `[FACT][NOSRC]`. Trigger is FACT-only (narrow)."""
    return re.sub(r"\[FACT\?\]", "[FACT][NOSRC]", text)


def expand_p3_inline(text: str) -> str:
    """`[.<lvl>]` -> `[CONF(level)]` (used inside a P3 bullet to override block default)."""
    def repl(m):
        return f"[CONF({CONF_MAP[m.group(1)]})]"
    return re.sub(r"\[\.([HML])\]", repl, text)


def expand_p3_block(text: str) -> str:
    """Distribute P3 block header (marker + default CONF) to each bullet.

    Block form:
        [MARKER, default CONF(level)]
        - claim 1
        - claim 2
        - [CONF(other)] claim 3
        [/MARKER]

    Becomes (each bullet gets the header marker + CONF, inline overrides win):
        [MARKER][CONF(level)] claim 1
        [MARKER][CONF(level)] claim 2
        [MARKER][CONF(other)] claim 3
    """
    pattern = re.compile(
        r"\[([A-Z]+),\s*default\s+CONF\(([a-z]+)\)\]\s*\n"
        r"((?:\s*-\s*.*\n)+)"
        r"\[/\1\]",
        re.MULTILINE,
    )

    def repl(m):
        marker = m.group(1)
        default_conf = m.group(2)
        bullets_block = m.group(3)
        out_lines = []
        for line in bullets_block.splitlines():
            stripped = line.lstrip().lstrip("-").strip()
            if not stripped:
                continue
            override_match = re.match(r"\[CONF\(([a-z]+)\)\]\s*(.*)", stripped)
            if override_match:
                conf = override_match.group(1)
                rest = override_match.group(2)
            else:
                conf = default_conf
                rest = stripped
            out_lines.append(f"[{marker}][CONF({conf})] {rest}")
        return "\n".join(out_lines)

    return pattern.sub(repl, text)


def normalize(text: str) -> str:
    """Apply all R1 expansions in order. Lossless on the canonical R1 forms."""
    text = expand_p3_inline(text)
    text = expand_p3_block(text)
    text = expand_p1(text)
    text = expand_p2(text)
    return text


# ----------------------------------------------------------------------------
# Self-tests (6/6 expected PASS per AOV-68 mod-applied version)
# ----------------------------------------------------------------------------

CASES = [
    (
        "P1 only — q5 French Revolution",
        "[FACT.H] The French Revolution began in 1789. [FACT.M] The Bastille was stormed on July 14.",
        "[FACT][CONF(high)] The French Revolution began in 1789. [FACT][CONF(medium)] The Bastille was stormed on July 14.",
    ),
    (
        "P1+P2 composite — q9 meditation",
        "[FACT.M?] Meditation longer than 8 weeks shifts cortisol baseline.",
        "[FACT][CONF(medium)][NOSRC] Meditation longer than 8 weeks shifts cortisol baseline.",
    ),
    (
        "P3 inline override — bullet [.L] -> [CONF(low)]",
        "[.L] try Cython for the hot path.",
        "[CONF(low)] try Cython for the hot path.",
    ),
    (
        "P2 bare — [FACT?] -> [FACT][NOSRC]",
        "[FACT?] Most LLM hallucinations occur on long-tail entities.",
        "[FACT][NOSRC] Most LLM hallucinations occur on long-tail entities.",
    ),
    (
        "Negative — bare [NOSRC][CONF(medium)] is NOT decompressed",
        "[NOSRC][CONF(medium)] Held position without source.",
        "[NOSRC][CONF(medium)] Held position without source.",
    ),
    (
        "P3 block distribution — header propagated to every bullet (AOV-68 M3.2)",
        (
            "[REC, default CONF(medium)]\n"
            "- Use structured output formats.\n"
            "- Add an evaluation harness.\n"
            "- [CONF(low)] Try Cython for the hot path.\n"
            "[/REC]"
        ),
        (
            "[REC][CONF(medium)] Use structured output formats.\n"
            "[REC][CONF(medium)] Add an evaluation harness.\n"
            "[REC][CONF(low)] Try Cython for the hot path."
        ),
    ),
]


def run_self_tests() -> int:
    passes = 0
    for name, src, expected in CASES:
        got = normalize(src)
        ok = got.strip() == expected.strip()
        status = "PASS" if ok else "FAIL"
        print(f"[{status}] {name}")
        if not ok:
            print("  expected:", repr(expected))
            print("  got     :", repr(got))
        else:
            passes += 1
    total = len(CASES)
    print(f"\n{passes}/{total} self-tests PASS")
    return 0 if passes == total else 1


if __name__ == "__main__":
    sys.exit(run_self_tests())
