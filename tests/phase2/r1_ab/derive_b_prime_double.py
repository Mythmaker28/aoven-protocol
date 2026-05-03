"""Derive Test B' (P1+P2) and Test B'' (P1+P2+P3) cells from Test B.

Reads tests/phase2/r1_ab/test_b/mab{1..5}.md and writes:
  - tests/phase2/r1_ab/test_b_prime/mab{1..5}.md
  - tests/phase2/r1_ab/test_b_doubleprime/mab{1..5}.md

Mechanically applies r1_compressor; then verifies losslessness via r1_normalizer.
"""

import os
import re
import sys

HERE = os.path.dirname(os.path.abspath(__file__))
PHASE2 = os.path.dirname(HERE)
sys.path.insert(0, PHASE2)

from r1_compressor import compress_p1_p2, compress_p1_p2_p3  # type: ignore  # noqa: E402
from r1_normalizer import normalize  # type: ignore  # noqa: E402

CELLS = ["mab1", "mab2", "mab3", "mab4", "mab5"]


def split_header_and_body(text: str):
    """Split file into header (frontmatter + prompt + Aoven header line) and body."""
    lines = text.splitlines(keepends=True)
    body_start = None
    for idx, line in enumerate(lines):
        if line.strip().startswith("[Aoven v0.1.2]"):
            body_start = idx + 1
            break
    if body_start is None:
        raise RuntimeError("no [Aoven v0.1.2] header found")
    header = "".join(lines[:body_start])
    body = "".join(lines[body_start:])
    return header, body


def replace_header(header: str, new_label: str) -> str:
    return header.replace("[Aoven v0.1.2]", new_label)


def replace_title_tag(header: str, new_tag: str) -> str:
    return re.sub(r"# (MAB-\d+) / Test [^\n]+", rf"# \1 / {new_tag}", header, count=1)


def derive(cell: str):
    src_path = os.path.join(PHASE2, "r1_ab", "test_b", f"{cell}.md")
    with open(src_path, "r", encoding="utf-8") as f:
        full = f.read()
    header, body = split_header_and_body(full)

    b_prime_body = compress_p1_p2(body)
    b_dprime_body = compress_p1_p2_p3(body)

    rt_p = normalize(b_prime_body)
    rt_d = normalize(b_dprime_body)
    ok_p = _ws(rt_p) == _ws(body)
    ok_d = _ws(rt_d) == _ws(body)
    if not (ok_p and ok_d):
        print(f"[FAIL round-trip] {cell}: B'={ok_p} B''={ok_d}")
        if not ok_p:
            print("  rt_b_prime:", repr(rt_p)[:400])
            print("  expected  :", repr(body)[:400])
        if not ok_d:
            print("  rt_b_dprime:", repr(rt_d)[:400])
            print("  expected   :", repr(body)[:400])
        return False

    # Test B'
    b_prime_header = replace_title_tag(header, "Test B' (R1 P1+P2 compressed)")
    b_prime_header = replace_header(b_prime_header, "[Aoven v0.1.3-r1, P1+P2]")
    out_p = b_prime_header + b_prime_body
    with open(os.path.join(PHASE2, "r1_ab", "test_b_prime", f"{cell}.md"), "w", encoding="utf-8") as f:
        f.write(out_p)

    # Test B''
    b_dprime_header = replace_title_tag(header, "Test B'' (R1 P1+P2+P3 compressed)")
    b_dprime_header = replace_header(b_dprime_header, "[Aoven v0.1.3-r1, P1+P2+P3]")
    out_d = b_dprime_header + b_dprime_body
    with open(os.path.join(PHASE2, "r1_ab", "test_b_doubleprime", f"{cell}.md"), "w", encoding="utf-8") as f:
        f.write(out_d)

    print(f"[OK] {cell}: B' and B'' derived; round-trip PASS")
    return True


def _ws(s: str) -> str:
    return re.sub(r"\s+", " ", s).strip()


def main():
    all_ok = True
    for cell in CELLS:
        if not derive(cell):
            all_ok = False
    print(f"\n{'ALL PASS' if all_ok else 'FAILURES PRESENT'}")
    return 0 if all_ok else 1


if __name__ == "__main__":
    sys.exit(main())
