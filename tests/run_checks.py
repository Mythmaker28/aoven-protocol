#!/usr/bin/env python3
"""Run the repository's offline checks in a temporary copy of the working tree.

Run from the repository root:

    python3 tests/run_checks.py             # summary
    python3 tests/run_checks.py --verbose   # also print each step's output
    python3 tests/run_checks.py --keep      # keep the temporary copy

Standard library only; git must be on PATH. Nothing in the working tree is
written to. The files git lists as tracked or untracked are copied to a
temporary directory (ignored files, such as tests/v0.2/cells/_cycle_secret.txt,
are not), the steps in STEPS run there with PYTHONDONTWRITEBYTECODE=1, and the
copy is then compared with the working tree:

- a step passes when it exits with status 0;
- three steps regenerate committed files. Those files are deleted from the
  copy before the step runs, so each must be written again, and must then
  match the working tree byte for byte, or after CRLF -> LF.
  KNOWN_DIFFERENCES lists the one file that comes out differently;
- any other changed, missing or new file is a failure.

_stats.py reads its two input tables with `git show origin/main:...`. It runs
with GIT_DIR set to this repository and needs origin/main (git fetch origin
main); the runner first checks that both tables are the same at origin/main
as at the script's PIN_COMMIT.

The tests/v0.2/_*.py scripts that set WORKSPACE are never run: each expects a
fixed Windows directory, and two of them call a live model.

Exit status: 0 if every check passes, 1 otherwise.
"""

import argparse
import difflib
import hashlib
import os
import re
import subprocess
import sys
import tempfile
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
STATS = "tests/v0.2/scoring/_stats.py"
TIMEOUT = 600  # seconds, per step

# (label, arguments after the Python interpreter, files the step regenerates)
STEPS = [
    ("R1 normalizer self-tests", ["tests/phase2/r1_normalizer.py"], []),
    ("R1 compressor self-check", ["tests/phase2/r1_compressor.py"], []),
    ("Test B marker-strip self-test",
     ["tests/v0.2/strip_test_b_markers.py", "--selftest"], []),
    ("unit tests", ["-m", "unittest", "discover", "-s", "tests/unit"], []),
    ("unseal v0.2 rater scores", ["tests/v0.2/scoring/_unseal.py"],
     [f"tests/v0.2/scoring/{rater}_scores_unsealed.tsv"
      for rater in ("EpistemicLogician", "IndependentRater")]),
    ("derive Test B' and B''", ["tests/phase2/r1_ab/derive_b_prime_double.py"],
     [f"tests/phase2/r1_ab/{form}/mab{i}.md"
      for form in ("test_b_prime", "test_b_doubleprime") for i in range(1, 6)]),
    ("v0.2 statistics", [STATS],
     [f"tests/v0.2/scoring/{name}.md"
      for name in ("_kappa", "_test_b_delta", "_ratification")]),
]

# Regenerated files that differ from the committed file: sha256 of the
# committed text and of the regenerated text (line endings as LF), and what
# differs. Only this exact pair is accepted; any other content fails.
KNOWN_DIFFERENCES = {
    "tests/v0.2/scoring/_ratification.md": (
        "2fe532b8f7e438831f0864a71d2a03894e9dfb9d15848dc9b9e2bf0fb04d77e7",
        "d92105583f4fbeaa561c6199267921cba9c92ebe61398c2f5ec592c0d1b00473",
        "the committed file gives the sections 3.1 + 3.2 verdict as INCONCLUSIVE\n"
        "and sets out two readings of the D1 kappa gate (lines 10-13, 27-33);\n"
        "_stats.py writes FAIL. The committed file asks for a RedTeam audit and\n"
        "CEO ratification to pin the canonical reading (line 31).",
    ),
}


def git(*args):
    # --no-optional-locks: git status does not refresh .git/index either
    return subprocess.run(["git", "--no-optional-locks", *args], cwd=ROOT, check=True,
                          stdout=subprocess.PIPE, stderr=subprocess.PIPE).stdout


def commit_exists(rev):
    return subprocess.run(["git", "rev-parse", "--verify", "--quiet", rev + "^{commit}"],
                          cwd=ROOT, stdout=subprocess.DEVNULL).returncode == 0


def lf(data):
    return data.replace(b"\r\n", b"\n")


def sha256_lf(data):
    return hashlib.sha256(lf(data)).hexdigest()


def working_tree_files():
    """Tracked and untracked files, ignored ones excluded, as {path: bytes}."""
    listing = git("ls-files", "-z", "--cached", "--others", "--exclude-standard")
    files = {}
    for name in sorted({os.fsdecode(n) for n in listing.split(b"\0") if n}):
        if (ROOT / name).is_file():  # skips files deleted from the working tree
            files[name] = (ROOT / name).read_bytes()
    return files


def check_stats_inputs():
    """Check that _stats.py, which reads origin/main, reads its pinned tables.

    Returns (problems, summary); problems is empty when the check passes.
    """
    if not commit_exists("origin/main"):
        return ["origin/main not found; run: git fetch origin main"], ""
    source = (ROOT / STATS).read_text(encoding="utf-8")
    pin = re.search(r"^PIN_COMMIT = '([0-9a-f]+)'", source, re.M)
    inputs = re.findall(r"git_show\('([^']+)'\)", source)
    if not pin or not inputs:
        return [f"PIN_COMMIT or the git_show() paths not found in {STATS}"], ""
    pin = pin.group(1)
    if not commit_exists(pin):
        return [f"PIN_COMMIT {pin} not in this clone; run: git fetch --unshallow origin"], ""
    problems = [f"{path} differs between origin/main and PIN_COMMIT {pin}"
                for path in inputs
                if git("show", f"origin/main:{path}") != git("show", f"{pin}:{path}")]
    origin_main = git("rev-parse", "--short", "origin/main").decode().strip()
    return problems, (f"its {len(inputs)} input tables are identical at origin/main"
                      f" ({origin_main}) and at PIN_COMMIT ({pin})")


def report(status, text):
    print(f"  {status:<5} {text}")


def print_diff(name, old, new, limit=40):
    lines = list(difflib.unified_diff(
        lf(old).decode("utf-8", "replace").splitlines(),
        lf(new).decode("utf-8", "replace").splitlines(),
        "working-tree/" + name, "regenerated/" + name, lineterm="", n=1))
    for line in lines[:limit]:
        print("        " + line[:160])
    if len(lines) > limit:
        print(f"        ... {len(lines) - limit} more diff lines")


def run_steps(copy, verbose):
    """Run STEPS in the copy; return the number of failed steps."""
    env = dict(os.environ, PYTHONDONTWRITEBYTECODE="1", PYTHONIOENCODING="utf-8")
    failed = 0
    print("Steps (exit status 0 = pass; last line of the step's output in quotes)")
    for label, args, outputs in STEPS:
        for name in outputs:  # a step that does not run leaves them missing
            (copy / name).unlink(missing_ok=True)
        step_env = env
        if args[0] == STATS:
            problems, summary = check_stats_inputs()
            if problems:
                failed += 1
                report("FAIL", f"{label:<30} not run")
                for problem in problems:
                    print(f"        {problem}")
                continue
            git_dir = git("rev-parse", "--absolute-git-dir").decode().strip()
            step_env = dict(env, GIT_DIR=git_dir)
        try:
            proc = subprocess.run([sys.executable, *args], cwd=copy, env=step_env,
                                  stdout=subprocess.PIPE, stderr=subprocess.STDOUT,
                                  timeout=TIMEOUT)
        except subprocess.TimeoutExpired:
            failed += 1
            report("FAIL", f"{label:<30} timed out after {TIMEOUT} s")
            continue
        output = proc.stdout.decode("utf-8", "replace")
        lines = [line.strip() for line in output.splitlines() if line.strip()]
        failed += proc.returncode != 0
        report("pass" if proc.returncode == 0 else "FAIL",
               f"{label:<30} exit {proc.returncode}  \"{lines[-1] if lines else ''}\"")
        if args[0] == STATS:
            print(f"        {summary}")
        if verbose or proc.returncode != 0:
            for line in output.splitlines():
                print("        | " + line)
    return failed


def compare(copy, files, verbose):
    """Compare the copy with the working tree; return the number of failures."""
    regenerated = {name for _, _, outputs in STEPS for name in outputs}
    after = {p.relative_to(copy).as_posix(): p for p in copy.rglob("*")
             if p.is_file() and "__pycache__" not in p.parts}
    failed = known = identical = 0
    print("\nFiles (copy after the steps vs working tree)")
    for name in sorted(set(files) | set(after)):
        if name not in after:
            failed += 1
            report("FAIL", f"{name}: missing" + (" (not regenerated)" if name in regenerated else ""))
            continue
        if name not in files:
            failed += 1
            report("FAIL", f"{name}: new file")
            continue
        old, new = files[name], after[name].read_bytes()
        expected = KNOWN_DIFFERENCES.get(name)
        if new == old:
            identical += 1
            if expected:
                report("note", f"{name}: identical; its KNOWN_DIFFERENCES entry is no longer needed")
        elif lf(new) == lf(old):
            identical += 1
            report("note", f"{name}: identical except for line endings (CRLF vs LF)")
        elif expected and (sha256_lf(old), sha256_lf(new)) == expected[:2]:
            known += 1
            report("known", f"{name}: regenerated content differs from the committed file;")
            for line in expected[2].splitlines():
                print(f"        {line}")
            if verbose:
                print_diff(name, old, new)
        else:
            failed += 1
            report("FAIL", f"{name}: content differs")
            if expected:
                print(f"        not the known difference (sha256 committed {sha256_lf(old)},"
                      f" regenerated {sha256_lf(new)})")
            print_diff(name, old, new)
    same = sum(1 for name in regenerated if name in files and name in after
               and lf(after[name].read_bytes()) == lf(files[name]))
    print(f"  {len(regenerated)} files regenerated by the steps, {same} match the working tree")
    print(f"  {len(set(files) | set(after))} files compared: {identical} identical,"
          f" {known} known difference(s), {failed} failure(s)")
    return failed


def run_all(copy, files, verbose):
    for name, data in files.items():
        (copy / name).parent.mkdir(parents=True, exist_ok=True)
        (copy / name).write_bytes(data)
    failed = run_steps(copy, verbose)
    failed += compare(copy, files, verbose)
    print(f"\nResult: {'PASS' if failed == 0 else 'FAIL'}"
          f" ({failed} failure(s); {len(STEPS)} steps, {len(files)} files copied)")
    return failed == 0


def main():
    parser = argparse.ArgumentParser(description=__doc__.splitlines()[0])
    parser.add_argument("--verbose", action="store_true", help="print each step's output")
    parser.add_argument("--keep", action="store_true", help="keep the temporary copy")
    options = parser.parse_args()
    if hasattr(sys.stdout, "reconfigure"):
        sys.stdout.reconfigure(errors="backslashreplace")
    try:
        files = working_tree_files()
        head = git("rev-parse", "--short", "HEAD").decode().strip()
        changed = len(git("status", "--porcelain").splitlines())
    except (OSError, subprocess.CalledProcessError) as error:
        print(f"git failed in {ROOT}: {error}")
        return 1
    print(f"Repository: {ROOT} (HEAD {head}, {changed} path(s) changed or untracked)")
    print(f"Python:     {sys.version.split()[0]} ({sys.executable})\n")
    if options.keep:
        copy = tempfile.mkdtemp(prefix="aoven-checks-")
        ok = run_all(Path(copy), files, options.verbose)
        print(f"Temporary copy kept: {copy}")
    else:
        with tempfile.TemporaryDirectory(prefix="aoven-checks-") as copy:
            ok = run_all(Path(copy), files, options.verbose)
    return 0 if ok else 1


if __name__ == "__main__":
    sys.exit(main())
