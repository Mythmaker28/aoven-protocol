"""
Phase 5 statistical analysis for AOV-234 (header-as-prime framing per F2).

Inputs (read via `git show origin/main:` for LF-pinned bytes from commit 0d67287):
  - tests/v0.2/scoring/EpistemicLogician_scores_unsealed.tsv
  - tests/v0.2/scoring/IndependentRater_scores_unsealed.tsv

Outputs:
  - tests/v0.2/scoring/_kappa.md       (§3.1 inter-rater reliability per D-axis)
  - tests/v0.2/scoring/_test_b_delta.md (§3.2 Test B vs A paired delta on D1-D5)
  - tests/v0.2/scoring/_ratification.md (§3.1+§3.2 verdict per F2)

Standing rulings applied:
  - CEO F1 (`238ca0bb`): NaN-κ axes excluded from §3.1 gate; condition-blind.
  - ERR-row drop: V02-D-SCI-003 cond=B (blind 7433b2505a5181bf) dropped before any computation.
  - No §6 LOO κ-power-floor rescue. No §5 hypothesis edits.

Score scale: 0-3 (4 categories), lower = better.
"""

import os
import math
import random
import subprocess
from collections import Counter

REPO = os.path.dirname(os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__)))))
PIN_COMMIT = '0d67287'
ERR_BLIND = '7433b2505a5181bf'
ERR_QID = 'V02-D-SCI-003'
DIMS = ['D1', 'D2', 'D3', 'D4', 'D5', 'D6', 'D7', 'D8']
KAPPA_FLOOR = 0.6  # §3.1
BOOTSTRAP_B = 2000
RNG_SEED = 20260510  # date-based seed; pinned for reproducibility


def git_show(path):
    """Read file content from origin/main as bytes (LF-pinned)."""
    out = subprocess.check_output(
        ['git', 'show', f'origin/main:{path}'],
        cwd=REPO,
    )
    return out.decode('utf-8')


def parse_tsv(text):
    """Return list of dicts, one per data row (skip comment + header)."""
    rows = []
    for line in text.splitlines():
        if not line or line.startswith('#'):
            continue
        cells = line.split('\t')
        if cells[0] == 'qid':  # header
            continue
        if len(cells) < 13:
            continue
        rows.append({
            'qid': cells[0],
            'cond': cells[1],
            'blind_id': cells[2],
            'D1': cells[3], 'D2': cells[4], 'D3': cells[5], 'D4': cells[6],
            'D5': cells[7], 'D6': cells[8], 'D7': cells[9], 'D8': cells[10],
            'L2': cells[11],
            'note': cells[12] if len(cells) > 12 else '',
        })
    return rows


def drop_err(rows):
    return [r for r in rows if r['blind_id'] != ERR_BLIND]


def variance(xs):
    n = len(xs)
    if n < 2:
        return 0.0
    m = sum(xs) / n
    return sum((x - m) ** 2 for x in xs) / (n - 1)


def quadratic_weighted_kappa(r1, r2, k=4):
    """
    Cohen's quadratic-weighted kappa for two raters on a 0..(k-1) scale.

    Returns NaN if either rater's vector has zero variance (degenerate marginal),
    per CEO F1 ruling (`238ca0bb`).
    """
    assert len(r1) == len(r2)
    n = len(r1)
    if n == 0:
        return float('nan'), 'empty'
    if variance(r1) == 0 or variance(r2) == 0:
        return float('nan'), 'zero_variance_marginal'

    # confusion matrix O[i][j]
    O = [[0] * k for _ in range(k)]
    for a, b in zip(r1, r2):
        O[a][b] += 1
    # marginals
    row_marg = [sum(O[i]) for i in range(k)]
    col_marg = [sum(O[i][j] for i in range(k)) for j in range(k)]
    # expected E[i][j]
    E = [[(row_marg[i] * col_marg[j]) / n for j in range(k)] for i in range(k)]
    # quadratic-weight (squared distance over max squared distance)
    w = [[((i - j) ** 2) / ((k - 1) ** 2) for j in range(k)] for i in range(k)]

    num = sum(w[i][j] * O[i][j] for i in range(k) for j in range(k))
    den = sum(w[i][j] * E[i][j] for i in range(k) for j in range(k))
    if den == 0:
        return float('nan'), 'zero_expected_disagreement'
    kappa = 1 - num / den
    return kappa, 'ok'


def bootstrap_kappa_ci(r1, r2, B=BOOTSTRAP_B, alpha=0.05, seed=RNG_SEED):
    """Percentile bootstrap CI on quadratic-weighted κ."""
    n = len(r1)
    rng = random.Random(seed)
    ks = []
    nan_count = 0
    for _ in range(B):
        idx = [rng.randrange(n) for _ in range(n)]
        s1 = [r1[i] for i in idx]
        s2 = [r2[i] for i in idx]
        k, _ = quadratic_weighted_kappa(s1, s2)
        if math.isnan(k):
            nan_count += 1
            continue
        ks.append(k)
    if not ks:
        return float('nan'), float('nan'), nan_count, 0
    ks.sort()
    lo = ks[int(alpha / 2 * len(ks))]
    hi = ks[int((1 - alpha / 2) * len(ks)) - 1]
    return lo, hi, nan_count, len(ks)


def paired_delta_stats(deltas):
    """
    Given paired-difference vector (B - A), return mean, sd, n, t, df, p_two_sided (approx), d_z.

    Lower score = better. Negative mean delta = improvement under header-as-prime (B).
    """
    n = len(deltas)
    if n < 2:
        return None
    m = sum(deltas) / n
    sd = math.sqrt(sum((d - m) ** 2 for d in deltas) / (n - 1))
    if sd == 0:
        return {'n': n, 'mean': m, 'sd': sd, 't': float('nan'), 'df': n - 1,
                'p_two_sided': 1.0 if m == 0 else 0.0, 'd_z': float('nan')}
    se = sd / math.sqrt(n)
    t = m / se
    df = n - 1
    # Approximate two-sided p-value via Student's t survival; use scipy-free approximation
    # via the relation to incomplete beta. For df>=5 this is accurate enough for reporting.
    p = student_t_two_sided(t, df)
    d_z = m / sd  # Cohen's d_z (paired effect size)
    return {'n': n, 'mean': m, 'sd': sd, 't': t, 'df': df, 'p_two_sided': p, 'd_z': d_z}


def student_t_two_sided(t, df):
    """Two-sided p-value for Student's t via the incomplete beta function (stdlib only)."""
    x = df / (df + t * t)
    p = incomplete_beta(df / 2.0, 0.5, x)
    return max(min(p, 1.0), 0.0)


def incomplete_beta(a, b, x):
    """Regularized incomplete beta function I_x(a,b) via continued-fraction (Lentz)."""
    if x <= 0:
        return 0.0
    if x >= 1:
        return 1.0
    lbeta = math.lgamma(a) + math.lgamma(b) - math.lgamma(a + b)
    front = math.exp(math.log(x) * a + math.log(1 - x) * b - lbeta) / a
    # Lentz's continued fraction
    fpmin = 1e-300
    qab, qap, qam = a + b, a + 1.0, a - 1.0
    c = 1.0
    d = 1.0 - qab * x / qap
    if abs(d) < fpmin:
        d = fpmin
    d = 1.0 / d
    h = d
    for m in range(1, 200):
        m2 = 2 * m
        aa = m * (b - m) * x / ((qam + m2) * (a + m2))
        d = 1.0 + aa * d
        if abs(d) < fpmin:
            d = fpmin
        c = 1.0 + aa / c
        if abs(c) < fpmin:
            c = fpmin
        d = 1.0 / d
        h *= d * c
        aa = -(a + m) * (qab + m) * x / ((a + m2) * (qap + m2))
        d = 1.0 + aa * d
        if abs(d) < fpmin:
            d = fpmin
        c = 1.0 + aa / c
        if abs(c) < fpmin:
            c = fpmin
        d = 1.0 / d
        delta = d * c
        h *= delta
        if abs(delta - 1.0) < 1e-12:
            break
    return front * h


def main():
    log_lines = []

    log_lines.append(f'## Phase 5 stats — corpus pinned at `{PIN_COMMIT}`')
    log_lines.append('')

    log_text = git_show('tests/v0.2/scoring/EpistemicLogician_scores_unsealed.tsv')
    ir_text = git_show('tests/v0.2/scoring/IndependentRater_scores_unsealed.tsv')

    log_rows = parse_tsv(log_text)
    ir_rows = parse_tsv(ir_text)
    log_lines.append(f'Logician rows (raw): {len(log_rows)}')
    log_lines.append(f'IR rows (raw): {len(ir_rows)}')

    log_rows = drop_err(log_rows)
    ir_rows = drop_err(ir_rows)
    log_lines.append(f'After ERR drop ({ERR_BLIND}, qid {ERR_QID} cond=B): Logician={len(log_rows)}, IR={len(ir_rows)}')

    # join on blind_id
    log_by_blind = {r['blind_id']: r for r in log_rows}
    ir_by_blind = {r['blind_id']: r for r in ir_rows}
    common_blinds = sorted(set(log_by_blind) & set(ir_by_blind))
    log_lines.append(f'Joined on blind_id: {len(common_blinds)}')

    # Build per-axis paired score vectors (Logician, IR) over the joined set
    per_axis = {}
    for d in DIMS:
        r1 = []
        r2 = []
        for b in common_blinds:
            v1 = log_by_blind[b][d]
            v2 = ir_by_blind[b][d]
            if v1 == 'ERR' or v2 == 'ERR':
                continue
            r1.append(int(v1))
            r2.append(int(v2))
        per_axis[d] = (r1, r2)

    # ====== §3.1 — kappa per axis ======
    kappa_lines = []
    kappa_lines.append('# `_kappa.md` — Phase 5 inter-rater reliability (§3.1)')
    kappa_lines.append('')
    kappa_lines.append(f'**Corpus pin:** `{PIN_COMMIT}` (origin/main)')
    kappa_lines.append(f'**Inputs:** `EpistemicLogician_scores_unsealed.tsv` + `IndependentRater_scores_unsealed.tsv`')
    kappa_lines.append(f'**N (joined, post-ERR-drop):** {len(common_blinds)} cells (60 raw - 1 ERR row {ERR_BLIND})')
    kappa_lines.append(f'**Method:** Cohen\'s quadratic-weighted κ; percentile bootstrap CI (B={BOOTSTRAP_B}, seed={RNG_SEED}).')
    kappa_lines.append(f'**Standing rulings applied:** CEO F1 `238ca0bb` (NaN κ on degenerate-marginal axes; excluded from §3.1 gate). No §6 LOO rescue. No §5 hypothesis edits.')
    kappa_lines.append('')
    kappa_lines.append('| Axis | Logician variance | IR variance | κ (quadratic-weighted) | 95% bootstrap CI | Gate (≥0.6) |')
    kappa_lines.append('|---|---|---|---|---|---|')

    kappa_results = {}
    for d in DIMS:
        r1, r2 = per_axis[d]
        v1 = variance(r1)
        v2 = variance(r2)
        k, status = quadratic_weighted_kappa(r1, r2)
        if math.isnan(k):
            kappa_results[d] = {'kappa': float('nan'), 'ci_lo': float('nan'), 'ci_hi': float('nan'), 'status': status}
            kappa_lines.append(f'| {d} | {v1:.4f} | {v2:.4f} | NaN ({status}) | n/a | EXCLUDED (F1) |')
        else:
            lo, hi, nan_b, ok_b = bootstrap_kappa_ci(r1, r2)
            kappa_results[d] = {'kappa': k, 'ci_lo': lo, 'ci_hi': hi, 'status': status, 'bootstrap_nan': nan_b, 'bootstrap_ok': ok_b}
            gate = 'PASS' if k >= KAPPA_FLOOR else 'FAIL'
            kappa_lines.append(f'| {d} | {v1:.4f} | {v2:.4f} | {k:.4f} | [{lo:.4f}, {hi:.4f}] | {gate} (boot {ok_b}/{BOOTSTRAP_B}, {nan_b} NaN) |')

    kappa_lines.append('')
    var_axes = [d for d in DIMS if not math.isnan(kappa_results[d]['kappa'])]
    nan_axes = [d for d in DIMS if math.isnan(kappa_results[d]['kappa'])]
    kappa_lines.append(f'**Variance-bearing axes (κ defined):** {", ".join(var_axes) if var_axes else "(none)"}')
    kappa_lines.append(f'**Zero-variance axes (κ NaN, excluded per F1):** {", ".join(nan_axes) if nan_axes else "(none)"}')
    kappa_lines.append('')
    if var_axes:
        passes = [d for d in var_axes if kappa_results[d]['kappa'] >= KAPPA_FLOOR]
        fails = [d for d in var_axes if kappa_results[d]['kappa'] < KAPPA_FLOOR]
        kappa_lines.append(f'**§3.1 gate (≥{KAPPA_FLOOR} on variance-bearing axes):** PASS on {", ".join(passes) or "(none)"}; FAIL on {", ".join(fails) or "(none)"}.')
    else:
        kappa_lines.append(f'**§3.1 gate:** No variance-bearing axes — gate has no axes to evaluate.')
    kappa_lines.append('')
    kappa_lines.append('## Per-rater marginal distributions (informational)')
    kappa_lines.append('')
    kappa_lines.append('| Axis | Logician scores | IR scores |')
    kappa_lines.append('|---|---|---|')
    for d in DIMS:
        r1, r2 = per_axis[d]
        c1 = dict(Counter(r1))
        c2 = dict(Counter(r2))
        kappa_lines.append(f'| {d} | {c1} | {c2} |')

    # ====== §3.2 — Test B vs Test A paired delta on D1-D5 ======
    delta_axes = ['D1', 'D2', 'D3', 'D4', 'D5']
    # Build matched pairs by qid: for each qid, get cond=A blind and cond=B blind
    log_by_qid_cond = {(r['qid'], r['cond']): r for r in log_rows}
    ir_by_qid_cond = {(r['qid'], r['cond']): r for r in ir_rows}
    qids_A = set(q for q, c in log_by_qid_cond.keys() if c == 'A') & set(q for q, c in ir_by_qid_cond.keys() if c == 'A')
    qids_B = set(q for q, c in log_by_qid_cond.keys() if c == 'B') & set(q for q, c in ir_by_qid_cond.keys() if c == 'B')
    matched_qids = sorted(qids_A & qids_B)

    delta_lines = []
    delta_lines.append('# `_test_b_delta.md` — Phase 5 Test B vs Test A paired delta on D1–D5 (§3.2, F2 framing)')
    delta_lines.append('')
    delta_lines.append(f'**Corpus pin:** `{PIN_COMMIT}` (origin/main)')
    delta_lines.append(f'**F2 framing (BINDING):** "header-as-prime alone vs unprimed baseline" — NOT "full protocol vs baseline." Zero markers were emitted in either condition (RedTeam audit `fdf8a827` on AOV-228), so what this corpus tests is the bare-header invocation as a framing prime.')
    delta_lines.append(f'**Convention:** scores 0-3, lower = better. Delta = score(B) - score(A); negative delta = improvement under header-as-prime.')
    delta_lines.append(f'**Matched pairs (post-ERR-drop):** {len(matched_qids)} qids with both A and B (qid {ERR_QID} dropped because B-side is ERR).')
    delta_lines.append('')
    delta_lines.append('## Per-axis paired delta (rater-averaged score per cell)')
    delta_lines.append('')
    delta_lines.append('| Axis | n | mean Δ (B−A) | sd Δ | t | df | p (two-sided) | Cohen\'s d_z |')
    delta_lines.append('|---|---|---|---|---|---|---|---|')

    delta_results = {}
    for d in delta_axes:
        deltas = []
        for q in matched_qids:
            la = log_by_qid_cond[(q, 'A')][d]
            lb = log_by_qid_cond[(q, 'B')][d]
            ia = ir_by_qid_cond[(q, 'A')][d]
            ib = ir_by_qid_cond[(q, 'B')][d]
            if 'ERR' in (la, lb, ia, ib):
                continue
            score_A = (int(la) + int(ia)) / 2.0
            score_B = (int(lb) + int(ib)) / 2.0
            deltas.append(score_B - score_A)
        s = paired_delta_stats(deltas)
        delta_results[d] = s
        if s is None:
            delta_lines.append(f'| {d} | 0 | n/a | n/a | n/a | n/a | n/a | n/a |')
        else:
            p_str = f'{s["p_two_sided"]:.4f}' if not math.isnan(s['p_two_sided']) else 'NaN'
            t_str = f'{s["t"]:.4f}' if not math.isnan(s['t']) else 'NaN'
            dz_str = f'{s["d_z"]:.4f}' if not math.isnan(s['d_z']) else 'NaN'
            delta_lines.append(f'| {d} | {s["n"]} | {s["mean"]:+.4f} | {s["sd"]:.4f} | {t_str} | {s["df"]} | {p_str} | {dz_str} |')

    delta_lines.append('')
    delta_lines.append('## Per-rater per-axis paired delta (sensitivity)')
    delta_lines.append('')
    delta_lines.append('| Axis | Rater | n | mean Δ (B−A) | sd Δ | t | p |')
    delta_lines.append('|---|---|---|---|---|---|---|')
    per_rater_results = {}
    for d in delta_axes:
        for rname, by in [('Logician', log_by_qid_cond), ('IR', ir_by_qid_cond)]:
            deltas = []
            for q in matched_qids:
                a = by[(q, 'A')][d]
                b = by[(q, 'B')][d]
                if a == 'ERR' or b == 'ERR':
                    continue
                deltas.append(int(b) - int(a))
            s = paired_delta_stats(deltas)
            per_rater_results.setdefault(d, {})[rname] = s
            if s is None:
                delta_lines.append(f'| {d} | {rname} | 0 | n/a | n/a | n/a | n/a |')
            else:
                p_str = f'{s["p_two_sided"]:.4f}' if not math.isnan(s['p_two_sided']) else 'NaN'
                t_str = f'{s["t"]:.4f}' if not math.isnan(s['t']) else 'NaN'
                delta_lines.append(f'| {d} | {rname} | {s["n"]} | {s["mean"]:+.4f} | {s["sd"]:.4f} | {t_str} | {p_str} |')

    delta_lines.append('')
    delta_lines.append('**Interpretation rule (per §3.2 + F2 framing):**')
    delta_lines.append(f'- A directional improvement under header-as-prime would show **negative** mean Δ on rubric axes.')
    delta_lines.append(f'- Per CEO F1 ruling and AOV-246 audit O2: zero-variance axes produce Δ=0 or NaN by construction; this is honest reporting, not a §6 LOO rescue.')
    delta_lines.append(f'- Significance (p<0.05) on a variance-bearing axis is necessary but not sufficient for §3.2 ratification — interpretation must be paired with §3.1 reliability gate clearance on the same axis.')

    # ====== §3.1+§3.2 ratification verdict ======
    rat_lines = []
    rat_lines.append('# `_ratification.md` — Phase 5 v0.2 ratification verdict (F2 framing)')
    rat_lines.append('')
    rat_lines.append(f'**Corpus pin:** `{PIN_COMMIT}` (origin/main)')
    rat_lines.append(f'**Pre-registration:** `c2bde85` §3.1 (κ ≥ {KAPPA_FLOOR} reliability gate), §3.2 (Test B vs A delta on D1–D5), §5 (hypothesis lock), §6 (no LOO rescue).')
    rat_lines.append(f'**F2 framing (BINDING):** "header-as-prime alone vs unprimed baseline" — verified zero-marker outcome (RedTeam audit `fdf8a827`).')
    rat_lines.append(f'**Standing rulings:** CEO F1 (`238ca0bb`) NaN-κ exclusion; ERR-row drop on `{ERR_BLIND}`; no §6 LOO rescue; no §5 hypothesis edit.')
    rat_lines.append('')
    rat_lines.append('## §3.1 reliability gate result')
    rat_lines.append('')
    if var_axes:
        passes = [d for d in var_axes if kappa_results[d]['kappa'] >= KAPPA_FLOOR]
        fails = [d for d in var_axes if kappa_results[d]['kappa'] < KAPPA_FLOOR]
        for d in var_axes:
            rat_lines.append(f'- **{d}**: κ = {kappa_results[d]["kappa"]:.4f}, 95% CI [{kappa_results[d]["ci_lo"]:.4f}, {kappa_results[d]["ci_hi"]:.4f}] — gate {"PASS" if kappa_results[d]["kappa"] >= KAPPA_FLOOR else "FAIL"}')
    rat_lines.append('')
    if nan_axes:
        rat_lines.append(f'- **{", ".join(nan_axes)}**: κ NaN (degenerate marginal — at least one rater has zero variance). Excluded from §3.1 gate per CEO F1 ruling.')
    rat_lines.append('')
    rat_lines.append('## §3.2 treatment-effect result (Test B vs Test A paired delta)')
    rat_lines.append('')
    for d in delta_axes:
        s = delta_results[d]
        if s is None:
            rat_lines.append(f'- **{d}**: no usable pairs')
        else:
            sig = ' (p<0.05)' if not math.isnan(s['p_two_sided']) and s['p_two_sided'] < 0.05 else ''
            rat_lines.append(f'- **{d}**: n={s["n"]}, mean Δ = {s["mean"]:+.4f} (sd {s["sd"]:.4f}), Cohen\'s d_z = {s["d_z"] if not math.isnan(s["d_z"]) else "NaN"}, p = {s["p_two_sided"]:.4f}{sig}')
    rat_lines.append('')
    rat_lines.append('## Verdict')
    rat_lines.append('')

    # Verdict logic per F2 framing + standing rulings:
    # - PASS: gate clears on ALL variance-bearing axes AND treatment delta is significant on at least one F2-relevant axis (D1-D5)
    # - FAIL: gate fails on ANY variance-bearing axis (κ < floor)
    # - INCONCLUSIVE: gate clears but treatment delta does not, OR variance-bearing subset of D1-D5 is empty
    if var_axes:
        gate_passes_all = all(kappa_results[d]['kappa'] >= KAPPA_FLOOR for d in var_axes)
        gate_fails = [d for d in var_axes if kappa_results[d]['kappa'] < KAPPA_FLOOR]
    else:
        gate_passes_all = False
        gate_fails = []

    sig_axes = [d for d in delta_axes if delta_results[d] and not math.isnan(delta_results[d]['p_two_sided']) and delta_results[d]['p_two_sided'] < 0.05]
    f2_var_axes = [d for d in delta_axes if d in var_axes]

    if gate_fails:
        verdict = 'FAIL'
        verdict_reason = f'§3.1 reliability gate fails on variance-bearing axis/axes: {", ".join(gate_fails)} (κ < {KAPPA_FLOOR}).'
    elif not f2_var_axes:
        verdict = 'INCONCLUSIVE'
        verdict_reason = f'No F2-relevant rubric axis (D1–D5) has joint variance across both raters under this corpus. Header-as-prime cannot be discriminated from baseline on the rubric subset that the hypothesis names. This is the structural output of the F1 ruling and AOV-246 audit O2 — not a §6 LOO rescue and not a §5 hypothesis edit.'
    elif gate_passes_all and sig_axes:
        verdict = 'PASS'
        verdict_reason = f'§3.1 gate clears on all variance-bearing axes ({", ".join(var_axes)}) and §3.2 delta is significant (p<0.05) on F2-relevant axis/axes: {", ".join(sig_axes)}.'
    elif gate_passes_all and not sig_axes:
        verdict = 'INCONCLUSIVE'
        verdict_reason = f'§3.1 gate clears on variance-bearing axes ({", ".join(var_axes)}) but §3.2 delta is not significant (p≥0.05) on any F2-relevant axis (D1–D5). Reliability is established; treatment effect is not.'
    else:
        verdict = 'INCONCLUSIVE'
        verdict_reason = 'Mixed §3.1 / §3.2 result — see per-axis tables.'

    rat_lines.append(f'**§3.1 + §3.2 verdict (F2-scoped): {verdict}**')
    rat_lines.append('')
    rat_lines.append(verdict_reason)
    rat_lines.append('')
    rat_lines.append('## Forward-carry to v0.3 (per AOV-246 audit + CEO F1 ruling)')
    rat_lines.append('')
    rat_lines.append(f'- **Rubric calibration (D5/D7/D8 + IR-distribution narrowness):** zero-variance pattern on D5/D7/D8 (primary) and D2–D8 (IR) under high-end-model corpus is consistent with two readings — (1) corpus uniformity on those axes, (2) rubric thresholds mis-calibrated for high-end model genre. RedTeam spot-check favored Reading 1 but did not foreclose Reading 2. Both readings forward-carry to v0.3 rubric calibration scope (input-bucket on AOV-120 v0.1.4 candidates).')
    rat_lines.append(f'- **Marker-emergence retake (F3):** independent of rubric calibration. Forward to v0.3 as previously flagged.')
    rat_lines.append(f'- **§5 hypothesis text remains v0.1.2-locked.** §6 lock honored — no LOO rescue applied.')
    rat_lines.append('')

    # ====== Write artifacts ======
    out_kappa = os.path.join(REPO, 'tests/v0.2/scoring/_kappa.md')
    out_delta = os.path.join(REPO, 'tests/v0.2/scoring/_test_b_delta.md')
    out_rat = os.path.join(REPO, 'tests/v0.2/scoring/_ratification.md')

    for path, lines in [(out_kappa, kappa_lines), (out_delta, delta_lines), (out_rat, rat_lines)]:
        with open(path, 'w', encoding='utf-8', newline='\n') as f:
            f.write('\n'.join(lines) + '\n')
        print(f'wrote {path} ({len(lines)} lines)')

    print('\n'.join(log_lines))
    print('\nVERDICT:', verdict)


if __name__ == '__main__':
    main()
