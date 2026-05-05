#!/usr/bin/env python3
"""
v0.2 strip_test_b_markers.py — version-pinned mechanical Test B marker strip.

Per v0.2 pre-registration `c2bde85` §3.1 (Layer-1 blinding):
- Strips all `[MARKER]` and `[MARKER, CONF(level)]` and `[CONF(level)]` tokens
  from a Test B response.
- Normalises whitespace introduced by stripping.
- Removes the "marker noun-substitution" dangling-article artifact noted in
  `reconciliation_holdout_v0.1.2.md` Q14B (e.g. "this is an [INTERPRET]" -> "this is" rather than "this is an").
- Files a token-level diff (line number + before/after) for audit reproducibility.

Methodology binding:
- Pre-registration: docs/v0.2_expansion_preregistration.md @ c2bde85d32b37b6a35616adacbddf082ffd0716f.
- Probe key: tests/v0.2/probe_key.md @ f2870940 (rationale-bearing source-of-truth, NOT seen by raters).
- Marker syntax: AOVEN_PROTOCOL_v0.1.2 (canonical v0.1.2 marker set; v0.2 is locked to v0.1.2 marker syntax per pre-registration §7).
- Sibling: tests/v0.2/prompts.md (bare-prompt list for generator + raters).

Marker set (canonical v0.1.2):
    Class markers:  NOSRC, HYP, ANALOGY, BELIEF, EMOTION, MEMORY,
                    REC,   SPEC, INTUIT,  INTERPRET, FACT,    LIMIT
    Confidence:     CONF(low), CONF(medium), CONF(high)
    Combined:       [MARKER, CONF(level)]      (e.g. [FACT, CONF(low)])
                    [CONF(level)]               (standalone)

Stripping policy (steps applied in order):
    1. Replace each marker-token match with a single space.
    2. Collapse runs of horizontal whitespace (>=2 spaces or tabs) to a single space.
    3. Remove the dangling-article artifact: an article (a/an/the, any case)
       immediately preceding sentence-final punctuation [.,;:?!] is dropped.
       Rationale: when a generator wrote "this is an [INTERPRET]." the strip
       leaves "this is an ." -- the article is dangling. Remove the article so
       the sentence reads "this is."
    4. Remove a stranded space immediately preceding sentence punctuation.
    5. Trim trailing horizontal whitespace from each line.
    6. Collapse runs of >=3 newlines to exactly two newlines (preserves paragraph
       breaks but kills excessive blank-line runs introduced by stripping a
       marker that was on its own line).

No grammar repair beyond (3)-(4). Generator-time discipline (markers only as
parenthetical tags following a substantive noun phrase) is the load-bearing
contract; the strip script is a backstop, not a license.

Usage:
    python strip_test_b_markers.py <input_file>
        Writes <input_file>.stripped and <input_file>.strip_diff next to input.

    python strip_test_b_markers.py <input> --output <stripped> --diff <diff>
        Custom paths.

    python strip_test_b_markers.py --version
        Print version string.

    python strip_test_b_markers.py --selftest
        Run built-in regression cases. Exit 0 on PASS, 1 on FAIL.

Output:
    <input>.stripped       UTF-8, LF line endings, identical to input modulo
                           the stripping policy.
    <input>.strip_diff     UTF-8 audit log: header (script version, input,
                           SHA-256 of input and output) + per-line before/after
                           pairs for every changed line.

Exit codes:
    0  success (stripped + diff written; or --selftest passed)
    1  selftest failure
    2  argument error or I/O failure
"""

from __future__ import annotations

import argparse
import hashlib
import re
import sys
from typing import List, Tuple

# ---------------------------------------------------------------------------
# Version pin. Bump only when stripping policy changes; v0.2 generation cycle
# is sealed against this exact version.
# ---------------------------------------------------------------------------
VERSION = "v0.2-strip-1.0"

# Canonical v0.1.2 marker class names (alphabetical for readability).
_MARKER_NAMES = [
    "ANALOGY", "BELIEF", "EMOTION", "FACT", "HYP", "INTERPRET", "INTUIT",
    "LIMIT", "MEMORY", "NOSRC", "REC", "SPEC",
]

# Confidence level enum (single-level lock per v0.2 pre-registration).
_CONF_LEVELS = ["low", "medium", "high"]

# Build the marker regex. Three accepted shapes:
#   [MARKER]                    -> any of the 12 class markers.
#   [MARKER, CONF(level)]       -> class marker + confidence (one whitespace
#                                  optional after the comma).
#   [CONF(level)]               -> standalone confidence marker.
_MARKER_NAMES_ALT = "|".join(_MARKER_NAMES)
_CONF_ALT = "|".join(_CONF_LEVELS)
_CONF_PAREN = rf"CONF\((?:{_CONF_ALT})\)"
_MARKER_RE = re.compile(
    rf"\[(?:(?:{_MARKER_NAMES_ALT})(?:\s*,\s*{_CONF_PAREN})?|{_CONF_PAREN})\]"
)

# Dangling-article cleanup: an article immediately preceding sentence-final
# punctuation. We require at least one whitespace before the article so we do
# not eat words like "Kaplan" or "median". The article is removed (along with
# its leading whitespace), preserving the punctuation.
_DANGLING_ART_RE = re.compile(
    r"(?:(?<=^)|(?<=\s))(?:a|an|the|A|An|The|AN|THE)\s+(?=[.,;:?!](?:\s|$))",
    flags=re.MULTILINE,
)

# Stranded space immediately before sentence punctuation. After step 3 we may
# have left a " ." or " ,"; collapse the space.
_SPACE_BEFORE_PUNCT_RE = re.compile(r" +(?=[.,;:?!])")

# Horizontal whitespace runs (spaces or tabs).
_HWS_RUN_RE = re.compile(r"[ \t]{2,}")

# Trailing horizontal whitespace on a line.
_TRAIL_WS_RE = re.compile(r"[ \t]+$", flags=re.MULTILINE)

# Three-or-more consecutive newlines -> two newlines (one blank line).
_BLANK_RUN_RE = re.compile(r"\n{3,}")


def strip_text(s: str) -> str:
    """Apply the v0.2 marker-strip policy to a single Test B response string."""
    out = _MARKER_RE.sub(" ", s)
    out = _HWS_RUN_RE.sub(" ", out)
    out = _DANGLING_ART_RE.sub("", out)
    out = _SPACE_BEFORE_PUNCT_RE.sub("", out)
    out = _TRAIL_WS_RE.sub("", out)
    out = _BLANK_RUN_RE.sub("\n\n", out)
    return out


def diff_lines(orig: str, stripped: str) -> List[Tuple[int, str, str]]:
    """Per-line before/after diff. Compares line N of orig to line N of stripped."""
    o = orig.splitlines()
    s = stripped.splitlines()
    out: List[Tuple[int, str, str]] = []
    for i in range(max(len(o), len(s))):
        a = o[i] if i < len(o) else ""
        b = s[i] if i < len(s) else ""
        if a != b:
            out.append((i + 1, a, b))
    return out


def render_diff(diff: List[Tuple[int, str, str]], header: List[str]) -> str:
    parts: List[str] = []
    parts.extend(header)
    if not diff:
        parts.append("# (no differences -- stripped output is byte-identical to input)")
    else:
        for line_no, before, after in diff:
            parts.append(f"L{line_no}: BEFORE: {before!r}")
            parts.append(f"L{line_no}: AFTER : {after!r}")
    return "\n".join(parts) + "\n"


# ---------------------------------------------------------------------------
# Selftest. Regression cases for the stripping policy. If any fail, the v0.2
# generation cycle should NOT use this script -- bump the version and re-seal.
# ---------------------------------------------------------------------------
_SELFTEST_CASES: List[Tuple[str, str, str]] = [
    # (label, input, expected_output)
    (
        "single-class-marker",
        "The result is unclear. [HYP]",
        "The result is unclear.",
    ),
    (
        "marker-with-conf",
        "The trial showed a benefit. [FACT, CONF(low)]",
        "The trial showed a benefit.",
    ),
    (
        "standalone-conf",
        "I think this is right. [CONF(medium)]",
        "I think this is right.",
    ),
    (
        "noun-substitution-dangling-article",
        "This statement is an [INTERPRET].",
        "This statement is.",
    ),
    (
        "noun-substitution-the",
        "She delivered the [REC].",
        "She delivered.",
    ),
    (
        "marker-mid-sentence",
        "The drug works [HYP] in some patients.",
        "The drug works in some patients.",
    ),
    (
        "two-markers-same-line",
        "X causes Y [HYP] and Z [CONF(low)].",
        "X causes Y and Z.",
    ),
    (
        "blank-line-collapse",
        "First.\n\n\n\nSecond.",
        "First.\n\nSecond.",
    ),
    (
        "no-marker-noop",
        "A plain sentence with no markers.",
        "A plain sentence with no markers.",
    ),
    (
        "trailing-ws-trim",
        "Hello world.   \nNext line.",
        "Hello world.\nNext line.",
    ),
    (
        "non-marker-bracket-preserved",
        "See [Smith 2023] for the data.",
        "See [Smith 2023] for the data.",
    ),
    (
        "case-sensitive-marker-names",
        "lower-case [hyp] is not a canonical marker.",
        "lower-case [hyp] is not a canonical marker.",
    ),
    (
        "marker-then-comma",
        "It is risky [SPEC], but worth trying.",
        "It is risky, but worth trying.",
    ),
    (
        "marker-on-own-line",
        "First sentence.\n[INTERPRET]\nSecond sentence.",
        "First sentence.\n\nSecond sentence.",
    ),
]


def selftest() -> int:
    fails = 0
    for label, src, expected in _SELFTEST_CASES:
        got = strip_text(src)
        if got != expected:
            fails += 1
            sys.stderr.write(
                f"FAIL {label}\n"
                f"  input    {src!r}\n"
                f"  expected {expected!r}\n"
                f"  got      {got!r}\n"
            )
    if fails == 0:
        sys.stdout.write(f"strip_test_b_markers.py {VERSION}: {len(_SELFTEST_CASES)}/{len(_SELFTEST_CASES)} PASS\n")
        return 0
    sys.stderr.write(f"strip_test_b_markers.py {VERSION}: {fails}/{len(_SELFTEST_CASES)} FAIL\n")
    return 1


def main(argv: List[str]) -> int:
    p = argparse.ArgumentParser(description=__doc__.splitlines()[1] if __doc__ else None)
    p.add_argument("input", nargs="?", help="Test B response file (UTF-8).")
    p.add_argument("--output", help="Stripped output path (default: <input>.stripped).")
    p.add_argument("--diff", help="Strip-diff log path (default: <input>.strip_diff).")
    p.add_argument("--version", action="store_true", help="Print version and exit.")
    p.add_argument("--selftest", action="store_true", help="Run built-in regression cases.")
    args = p.parse_args(argv)

    if args.version:
        sys.stdout.write(VERSION + "\n")
        return 0

    if args.selftest:
        return selftest()

    if not args.input:
        p.error("input file required (or pass --selftest / --version)")

    try:
        with open(args.input, encoding="utf-8") as f:
            orig = f.read()
    except OSError as e:
        sys.stderr.write(f"read error: {e}\n")
        return 2

    stripped = strip_text(orig)
    out_path = args.output or (args.input + ".stripped")
    diff_path = args.diff or (args.input + ".strip_diff")

    in_sha = hashlib.sha256(orig.encode("utf-8")).hexdigest()
    out_sha = hashlib.sha256(stripped.encode("utf-8")).hexdigest()
    header = [
        f"# strip_test_b_markers.py {VERSION}",
        f"# input         : {args.input}",
        f"# input_sha256  : {in_sha}",
        f"# output_sha256 : {out_sha}",
        f"# input_lines   : {len(orig.splitlines())}",
        f"# output_lines  : {len(stripped.splitlines())}",
    ]

    try:
        with open(out_path, "w", encoding="utf-8", newline="\n") as f:
            f.write(stripped)
        with open(diff_path, "w", encoding="utf-8", newline="\n") as f:
            f.write(render_diff(diff_lines(orig, stripped), header))
    except OSError as e:
        sys.stderr.write(f"write error: {e}\n")
        return 2

    sys.stdout.write(f"stripped: {out_path}\n")
    sys.stdout.write(f"diff    : {diff_path}\n")
    return 0


if __name__ == "__main__":
    sys.exit(main(sys.argv[1:]))
