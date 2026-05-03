"""R1 compressor — opposite direction from r1_normalizer.

Takes v0.1.2 long-form Aoven text (Test B) and emits R1-compressed forms:
    compress_p1_p2(text)   -> Test B' (P1+P2 patterns only)
    compress_p1_p2_p3(text) -> Test B'' (P1+P2+P3 patterns)

For mini-A/B (AOV-72) cell generation: compress(B) -> B' / B''. Then verify
losslessness via r1_normalizer.normalize(B') == B and normalize(B'') == B.
"""

import re
import sys

CONF_INV = {"high": "H", "medium": "M", "low": "L"}


def compress_p1(text: str) -> str:
    """`[X][CONF(level)]` -> `[X.<lvl>]` for any non-CONF marker X."""
    def repl(m):
        marker = m.group(1)
        level = m.group(2)
        if marker == "CONF":
            return m.group(0)
        return f"[{marker}.{CONF_INV[level]}]"
    return re.sub(r"\[([A-Z]+)\]\[CONF\((high|medium|low)\)\]", repl, text)


def compress_p2(text: str) -> str:
    """`[FACT][NOSRC]` -> `[FACT?]`. Also `[FACT.<lvl>][NOSRC]` -> `[FACT.<lvl>?]`."""
    text = re.sub(r"\[FACT\]\[NOSRC\]", "[FACT?]", text)
    text = re.sub(r"\[FACT\.([HML])\]\[NOSRC\]", r"[FACT.\1?]", text)
    return text


def compress_p1_p2(text: str) -> str:
    return compress_p2(compress_p1(text))


def compress_p3(text: str) -> str:
    """3+ same-marker run -> block form with [/MARKER] close-tag (REQUIRED per UR-9).

    Operates on consecutive lines starting with the same `[X][CONF(level)]` (long form).
    For simplicity, this implementation only collapses runs that share an identical
    marker AND identical CONF level. Mixed CONF runs are left in long form
    (over-compression risk; conservative for AOV-72 mini-A/B).
    """
    lines = text.split("\n")
    out = []
    i = 0
    while i < len(lines):
        m = re.match(r"\[([A-Z]+)\]\[CONF\((high|medium|low)\)\]\s*(.*)", lines[i])
        if m:
            marker, level, body = m.group(1), m.group(2), m.group(3)
            run = [body]
            j = i + 1
            while j < len(lines):
                m2 = re.match(rf"\[{marker}\]\[CONF\(({level})\)\]\s*(.*)", lines[j])
                if m2:
                    run.append(m2.group(2))
                    j += 1
                else:
                    break
            if len(run) >= 3:
                out.append(f"[{marker}, default CONF({level})]")
                for claim in run:
                    out.append(f"- {claim}")
                out.append(f"[/{marker}]")
                i = j
                continue
        out.append(lines[i])
        i += 1
    return "\n".join(out)


def compress_p1_p2_p3(text: str) -> str:
    """Apply P3 first (operates on long form), then P1+P2 on whatever remains."""
    text = compress_p3(text)
    text = compress_p1(text)
    text = compress_p2(text)
    return text


# ----------------------------------------------------------------------------
# Self-check: round-trip via normalizer
# ----------------------------------------------------------------------------

def _self_check():
    from r1_normalizer import normalize  # type: ignore

    sample_b = (
        "[FACT][CONF(high)] Water boils at 100C at standard atmospheric pressure.\n"
        "[FACT][CONF(medium)][NOSRC] Most LLM hallucinations occur on long-tail entities.\n"
        "[REC][CONF(medium)] Use structured output formats.\n"
        "[REC][CONF(medium)] Add an evaluation harness.\n"
        "[REC][CONF(medium)] Cache prompts.\n"
        "[LIMIT] I cannot verify events past my training cutoff.\n"
    )
    b_prime = compress_p1_p2(sample_b)
    b_dprime = compress_p1_p2_p3(sample_b)

    rt_b_prime = normalize(b_prime)
    rt_b_dprime = normalize(b_dprime)

    print("=== Test B (input) ===")
    print(sample_b)
    print("=== Test B' (compress_p1_p2) ===")
    print(b_prime)
    print("=== Test B'' (compress_p1_p2_p3) ===")
    print(b_dprime)

    ok_prime = _normalize_ws(rt_b_prime) == _normalize_ws(sample_b)
    ok_dprime = _normalize_ws(rt_b_dprime) == _normalize_ws(sample_b)
    print(f"\nRound-trip B' -> B : {'PASS' if ok_prime else 'FAIL'}")
    print(f"Round-trip B'' -> B: {'PASS' if ok_dprime else 'FAIL'}")
    if not ok_prime:
        print("  rt_b_prime:", repr(rt_b_prime))
        print("  expected  :", repr(sample_b))
    if not ok_dprime:
        print("  rt_b_dprime:", repr(rt_b_dprime))
        print("  expected   :", repr(sample_b))
    return 0 if (ok_prime and ok_dprime) else 1


def _normalize_ws(s: str) -> str:
    return re.sub(r"\s+", " ", s).strip()


if __name__ == "__main__":
    sys.exit(_self_check())
