"""Numerical checks for tests/v0.2/scoring/_stats.py.

Run from the repository root:

    python3 -m unittest discover -s tests/unit -v

Standard library only. _stats.py is loaded from its path and only its pure
functions are called: main() never runs, so no `git show` is issued and no
scoring artefact is rewritten.

Each function is compared with a reference computed independently of it:

- Student's t: the exact finite series for integer df (the A(t|nu) series of
  Abramowitz & Stegun 1964, section 26.7), itself checked against Simpson
  integration of the t density and against tabulated critical values;
- regularized incomplete beta: the closed forms of I_x(a,1), I_x(1,b) and
  I_1/2(a,a);
- quadratic-weighted kappa: with weights proportional to (i-j)^2, expanding
  both weighted sums gives kappa = 2*cov / (var1 + var2 + (mean1 - mean2)^2)
  (population moments), evaluated here in exact rational arithmetic;
- paired deltas: the statistics module.
"""

import importlib.util
import math
import random
import statistics
import sys
import unittest
from fractions import Fraction
from pathlib import Path

STATS_PATH = Path(__file__).resolve().parents[1] / "v0.2" / "scoring" / "_stats.py"


def load_stats():
    previous = sys.dont_write_bytecode
    sys.dont_write_bytecode = True  # leave no __pycache__ in tests/v0.2/scoring/
    try:
        spec = importlib.util.spec_from_file_location("aoven_v02_stats", STATS_PATH)
        module = importlib.util.module_from_spec(spec)
        spec.loader.exec_module(module)
    finally:
        sys.dont_write_bytecode = previous
    return module


stats_mod = load_stats()


def exact_t_two_sided(t, df):
    """Exact two-sided p-value P(|T| >= |t|) of Student's t, integer df >= 1.

    Uses theta = atan(|t| / sqrt(df)) and the finite series for
    A(t|df) = P(|T| <= |t|); returns 1 - A.
    """
    theta = math.atan(abs(t) / math.sqrt(df))
    s, c = math.sin(theta), math.cos(theta)
    if df == 1:
        a = 2.0 * theta / math.pi
    elif df % 2 == 0:
        term = acc = 1.0
        for k in range(1, df // 2):  # cos^2 ... cos^(df-2)
            term *= (2 * k - 1) / (2 * k) * c * c
            acc += term
        a = s * acc
    else:
        term = acc = 1.0
        for k in range(1, (df - 1) // 2):  # cos^2 ... cos^(df-3)
            term *= (2 * k) / (2 * k + 1) * c * c
            acc += term
        a = 2.0 / math.pi * (theta + s * c * acc)
    return 1.0 - a


def simpson_t_two_sided(t, df, intervals=2000):
    """1 - 2 * integral of the t density from 0 to |t| (composite Simpson)."""
    log_norm = (math.lgamma((df + 1) / 2) - math.lgamma(df / 2)
                - 0.5 * math.log(df * math.pi))

    def density(x):
        return math.exp(log_norm - (df + 1) / 2 * math.log1p(x * x / df))

    h = abs(t) / intervals
    total = density(0.0) + density(abs(t))
    total += sum((4 if i % 2 else 2) * density(i * h) for i in range(1, intervals))
    return 1.0 - 2.0 * total * h / 3.0


class ExactOracleTest(unittest.TestCase):
    """The reference used below is right before anything is compared with it."""

    def test_closed_forms_df1_df2(self):
        for t in (0.1, 0.5, 1.0, 2.0, 5.0, 20.0):
            self.assertAlmostEqual(exact_t_two_sided(t, 1),
                                   1.0 - 2.0 / math.pi * math.atan(t), places=12)
            self.assertAlmostEqual(exact_t_two_sided(t, 2),
                                   1.0 - t / math.sqrt(2.0 + t * t), places=12)

    def test_matches_numerical_integration(self):
        for df in (3, 4, 5, 7, 10, 28, 29, 58, 100):
            for t in (1e-4, 0.01, 0.3, 1.0, 2.048, 5.0, 12.0):
                with self.subTest(df=df, t=t):
                    self.assertAlmostEqual(exact_t_two_sided(t, df),
                                           simpson_t_two_sided(t, df), places=10)

    def test_tabulated_critical_values(self):
        # Two-sided 5% critical values of Student's t, as printed to 3 decimals
        # in standard tables.
        for df, t_crit in ((1, 12.706), (2, 4.303), (5, 2.571), (10, 2.228),
                           (28, 2.048), (29, 2.045), (100, 1.984)):
            with self.subTest(df=df):
                self.assertAlmostEqual(exact_t_two_sided(t_crit, df), 0.05, delta=1e-4)


class StudentTTest(unittest.TestCase):

    def test_matches_exact_values_away_from_zero(self):
        # 0.2386 and 0.3723 are the |t| reported in _test_b_delta.md (df = 28).
        for df in (1, 2, 5, 10, 28, 29, 58):
            for t in (0.0, 0.2386, 0.25, 0.3723, 0.5, 1.0, 2.0, 2.048, 3.0,
                      5.0, 10.0, 30.0):
                for signed_t in (t, -t):
                    with self.subTest(df=df, t=signed_t):
                        self.assertAlmostEqual(
                            stats_mod.student_t_two_sided(signed_t, df),
                            exact_t_two_sided(signed_t, df), delta=1e-9)

    @unittest.expectedFailure
    def test_matches_exact_values_near_zero(self):
        """Known defect, reported and left unfixed: |t| close to 0.

        student_t_two_sided() evaluates I_x(df/2, 1/2) at x = df / (df + t^2),
        which tends to 1 as t -> 0. incomplete_beta() applies the continued
        fraction directly, although it converges quickly only for
        x < (a+1)/(a+b+2), and stops after 199 iterations. Near t = 0 it then
        returns p-values far below the exact ones: df=28, t=1e-4 gives 0.0077
        instead of 0.9999. The p-values in the committed _test_b_delta.md
        (|t| in {0, 0.2386, 0.3723}, df = 28) are outside this regime and
        agree with the exact values to within 1e-11.

        The usual remedy is the symmetry I_x(a,b) = 1 - I_{1-x}(b,a) for
        x > (a+1)/(a+b+2). Changing scoring code is the owner's decision;
        once the defect is fixed this test passes, and unittest then reports
        an unexpected success until the decorator is removed.
        """
        for df in (5, 28, 100):
            for t in (1e-4, 1e-3, 1e-2):
                self.assertAlmostEqual(stats_mod.student_t_two_sided(t, df),
                                       exact_t_two_sided(t, df), delta=1e-6)


class IncompleteBetaTest(unittest.TestCase):

    def test_closed_forms_where_the_fraction_converges(self):
        # Every point satisfies x <= (a+1)/(a+b+2).
        ib = stats_mod.incomplete_beta
        for a, x in ((0.5, 0.3), (2.0, 0.5), (14.0, 0.8)):
            self.assertAlmostEqual(ib(a, 1.0, x), x ** a, places=12)
        for b, x in ((0.5, 0.3), (2.0, 0.3), (14.0, 0.05)):
            self.assertAlmostEqual(ib(1.0, b, x), 1.0 - (1.0 - x) ** b, places=12)
        for a in (0.5, 1.0, 2.5, 14.0, 50.0):
            self.assertAlmostEqual(ib(a, a, 0.5), 0.5, places=12)

    def test_bounds(self):
        self.assertEqual(stats_mod.incomplete_beta(14.0, 0.5, 0.0), 0.0)
        self.assertEqual(stats_mod.incomplete_beta(14.0, 0.5, 1.0), 1.0)


def closed_form_kappa(r1, r2):
    n = len(r1)
    m1, m2 = Fraction(sum(r1), n), Fraction(sum(r2), n)
    var1 = sum((a - m1) ** 2 for a in r1) / n
    var2 = sum((b - m2) ** 2 for b in r2) / n
    if var1 == 0 or var2 == 0:
        return None
    cov = sum((a - m1) * (b - m2) for a, b in zip(r1, r2)) / n
    return 2 * cov / (var1 + var2 + (m1 - m2) ** 2)


class QuadraticWeightedKappaTest(unittest.TestCase):

    def test_matches_closed_form_on_random_ratings(self):
        rng = random.Random(20261030)
        degenerate = 0
        for case in range(500):
            n = rng.randint(2, 60)
            r1 = [rng.randint(0, 3) for _ in range(n)]
            if case % 2:
                r2 = [rng.randint(0, 3) for _ in range(n)]
            else:  # correlated second rater
                r2 = [min(3, max(0, a + rng.choice((-2, -1, 0, 0, 0, 1, 2)))) for a in r1]
            kappa, status = stats_mod.quadratic_weighted_kappa(r1, r2)
            expected = closed_form_kappa(r1, r2)
            with self.subTest(case=case):
                if expected is None:
                    degenerate += 1
                    self.assertEqual(status, "zero_variance_marginal")
                    self.assertTrue(math.isnan(kappa))
                else:
                    self.assertEqual(status, "ok")
                    self.assertAlmostEqual(kappa, float(expected), places=12)
        self.assertGreater(degenerate, 0)  # the NaN branch was exercised

    def test_degenerate_inputs(self):
        kappa, status = stats_mod.quadratic_weighted_kappa([0, 0, 0], [0, 1, 2])
        self.assertTrue(math.isnan(kappa))
        self.assertEqual(status, "zero_variance_marginal")
        kappa, status = stats_mod.quadratic_weighted_kappa([], [])
        self.assertTrue(math.isnan(kappa))
        self.assertEqual(status, "empty")

    def test_perfect_agreement(self):
        self.assertEqual(stats_mod.quadratic_weighted_kappa([0, 1, 2, 3, 3], [0, 1, 2, 3, 3]),
                         (1.0, "ok"))


class PairedDeltaTest(unittest.TestCase):

    def test_matches_statistics_module(self):
        deltas = [1, -1, 0, 2, 0.5, -0.5, 0, 1.5]
        got = stats_mod.paired_delta_stats(deltas)
        n = len(deltas)
        mean, sd = statistics.fmean(deltas), statistics.stdev(deltas)
        t = mean / (sd / math.sqrt(n))
        self.assertEqual(got["n"], n)
        self.assertEqual(got["df"], n - 1)
        self.assertAlmostEqual(got["mean"], mean, places=12)
        self.assertAlmostEqual(got["sd"], sd, places=12)
        self.assertAlmostEqual(got["t"], t, places=12)
        self.assertAlmostEqual(got["d_z"], mean / sd, places=12)
        self.assertAlmostEqual(got["p_two_sided"], exact_t_two_sided(t, n - 1), places=9)

    def test_zero_spread(self):
        # The D5 row of _test_b_delta.md: sd = 0, t and d_z NaN, p = 1.
        got = stats_mod.paired_delta_stats([0, 0, 0, 0])
        self.assertEqual((got["mean"], got["sd"], got["p_two_sided"]), (0.0, 0.0, 1.0))
        self.assertTrue(math.isnan(got["t"]))
        self.assertTrue(math.isnan(got["d_z"]))
        self.assertEqual(stats_mod.paired_delta_stats([1, 1, 1])["p_two_sided"], 0.0)

    def test_fewer_than_two_deltas(self):
        self.assertIsNone(stats_mod.paired_delta_stats([]))
        self.assertIsNone(stats_mod.paired_delta_stats([0.5]))


if __name__ == "__main__":
    unittest.main()
