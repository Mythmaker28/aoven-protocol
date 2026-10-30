"""Round-trip checks for the R1 compressor and normalizer (tests/phase2/).

Run from the repository root:

    python3 -m unittest discover -s tests/unit -v

Standard library only. r1_compressor.py and r1_normalizer.py are loaded
from their paths; nothing is written to the repository. Neither script is
modified: they implement the R1 forms audited under AOV-68.

Property under test: normalize(compress(text)) == text, byte for byte, for
the P1+P2 path (Test B') and the P1+P2+P3 path (Test B'').
"""

import importlib.util
import random
import sys
import unittest
from pathlib import Path

PHASE2 = Path(__file__).resolve().parents[1] / "phase2"
R1_AB = PHASE2 / "r1_ab"
CELLS = ["mab1", "mab2", "mab3", "mab4", "mab5"]


def load(name):
    previous = sys.dont_write_bytecode
    sys.dont_write_bytecode = True  # leave no __pycache__ in tests/phase2/
    try:
        spec = importlib.util.spec_from_file_location("aoven_" + name, PHASE2 / (name + ".py"))
        module = importlib.util.module_from_spec(spec)
        spec.loader.exec_module(module)
    finally:
        sys.dont_write_bytecode = previous
    return module


compressor = load("r1_compressor")
normalizer = load("r1_normalizer")

MARKERS = sorted(normalizer.RATIFIED_MARKERS - {"CONF"})
LEVELS = ["high", "medium", "low"]
WORDS = "water boils at standard pressure use structured output cache prompts".split()


def random_text(rng, stacked):
    """Long-form text: marker lines, blank and plain lines, same-marker runs.

    With stacked=True, some lines carry a third marker right after the CONF
    tag (`[X][CONF(level)][NOSRC] claim`).
    """
    lines = []
    for _ in range(rng.randint(1, 12)):
        marker, level = rng.choice(MARKERS), rng.choice(LEVELS)
        claim = " ".join(rng.choice(WORDS) for _ in range(rng.randint(1, 6))).capitalize() + "."
        if rng.random() < 0.2:  # run of 2-5 lines with the same marker and level
            lines += [f"[{marker}][CONF({level})] Item {j}." for j in range(rng.randint(2, 5))]
            continue
        k = rng.random()
        if k < 0.45:
            lines.append(f"[{marker}][CONF({level})] {claim}")
        elif k < 0.60 and stacked:
            lines.append(f"[{rng.choice(('FACT', marker))}][CONF({level})][NOSRC] {claim}")
        elif k < 0.70:
            lines.append(f"[{marker}] {claim}")
        elif k < 0.78:
            lines.append(f"[FACT][NOSRC] {claim}")
        elif k < 0.85:
            lines.append("")
        else:
            lines.append(claim)
    return "\n".join(lines) + ("\n" if rng.random() < 0.5 else "")


def body_after(path, label):
    """Text after the version-header line, split as derive_b_prime_double.py does."""
    lines = path.read_text(encoding="utf-8").splitlines(keepends=True)
    start = next(i for i, line in enumerate(lines) if line.strip().startswith(label))
    return "".join(lines[start + 1:])


class CommittedCorpusTest(unittest.TestCase):
    """The committed Test B' and Test B'' cells (AOV-72) follow from Test B."""

    def test_derived_cells_match_and_round_trip(self):
        for cell in CELLS:
            with self.subTest(cell=cell):
                b = body_after(R1_AB / "test_b" / f"{cell}.md", "[Aoven v0.1.2]")
                b_prime = body_after(R1_AB / "test_b_prime" / f"{cell}.md",
                                     "[Aoven v0.1.3-r1, P1+P2]")
                b_dprime = body_after(R1_AB / "test_b_doubleprime" / f"{cell}.md",
                                      "[Aoven v0.1.3-r1, P1+P2+P3]")
                self.assertNotEqual(b_prime, b)
                self.assertEqual(compressor.compress_p1_p2(b), b_prime)
                self.assertEqual(compressor.compress_p1_p2_p3(b), b_dprime)
                self.assertEqual(normalizer.normalize(b_prime), b)
                self.assertEqual(normalizer.normalize(b_dprime), b)


class RandomTextTest(unittest.TestCase):

    def test_p1_p2_round_trip(self):
        rng = random.Random(20261030)
        for case in range(2000):
            text = random_text(rng, stacked=True)
            with self.subTest(case=case):
                self.assertEqual(normalizer.normalize(compressor.compress_p1_p2(text)), text)

    def test_p1_p2_p3_round_trip_without_stacked_markers(self):
        rng = random.Random(20261031)
        blocks = 0
        for case in range(2000):
            text = random_text(rng, stacked=False)
            compressed = compressor.compress_p1_p2_p3(text)
            blocks += compressed.count(", default CONF(")
            with self.subTest(case=case):
                self.assertEqual(normalizer.normalize(compressed), text)
        self.assertGreater(blocks, 0)  # the P3 block form was exercised


class KnownP3GapsTest(unittest.TestCase):
    """Inputs on which the P3 round trip is not exact; reported, left unfixed.

    MAB-1..5 contain no run that P3 compresses (tests/phase2/r1_ab/
    reconciliation.md), so no committed cell is affected. Whether to change
    the R1 scripts is the owner's decision. If they change, these tests pass
    and unittest reports an unexpected success until the decorator is removed.
    """

    @unittest.expectedFailure
    def test_stacked_marker_inside_a_run(self):
        """A third marker in a 3+ run comes back with an extra space.

        compress_p3 matches `[X][CONF(level)]` as a prefix, so the line
        `[FACT][CONF(medium)][NOSRC] b.` joins the run as the bullet
        `- [NOSRC] b.`, and expand_p3_block re-emits it as
        `[FACT][CONF(medium)] [NOSRC] b.`. Markers and their order survive and
        NOSRC stays on its own claim; only the spacing differs, which the
        compressor's own whitespace-collapsing check (_normalize_ws) counts
        as a failure.
        """
        text = ("[FACT][CONF(medium)] a.\n"
                "[FACT][CONF(medium)][NOSRC] b.\n"
                "[FACT][CONF(medium)] c.\n")
        round_trip = normalizer.normalize(compressor.compress_p1_p2_p3(text))
        self.assertEqual(compressor._normalize_ws(round_trip), compressor._normalize_ws(text))

    @unittest.expectedFailure
    def test_marker_only_lines_inside_a_run(self):
        """A run of 3+ marker-only lines (no claim text) is dropped.

        The compressor emits empty bullets (`- `); expand_p3_block skips empty
        bullets, so the three `[REC][CONF(medium)]` lines below disappear.
        """
        text = "x\n[REC][CONF(medium)]\n[REC][CONF(medium)]\n[REC][CONF(medium)]\ny\n"
        round_trip = normalizer.normalize(compressor.compress_p1_p2_p3(text))
        self.assertEqual(compressor._normalize_ws(round_trip), compressor._normalize_ws(text))


if __name__ == "__main__":
    unittest.main()
