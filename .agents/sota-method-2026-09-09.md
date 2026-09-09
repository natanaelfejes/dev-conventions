# SOTA-skills evaluation harness: what is portable

Source: clone of `martinholovsky/SOTA-skills`. Read: `evals/README.md`,
`evals/DESIGN-real-repo-audit.md`, `run-build-safe.py`, `run-build-safe-arms.py`,
`run-clean.py`, `run-completeness.py`, `run-decay.py`, `score.py`,
`judge-calibration.py`, `run-adjudication.py`, `test_scoring.py`,
`evals/results/RESULTS.md`, `evals/results/2026-08-21/BUILD-SAFE.md`,
`evals/results/2026-09-06/PRE-REGISTRATION.md`, `scripts/check-negative-controls.sh`.

## 1. Experimental design

**Arms.** Baseline is `without-library` vs `with-library`, run as raw model-API
calls (`run-clean.py`, `run-completeness.py`), never inside a Claude Code session,
because the session's own `CLAUDE.md` and skill registry would contaminate the
"without" arm (README lines 304-310). Some instruments add arms: `--ablate` drops
one rule file from the with-arm; `--pad-rules N` adds a `with+pad` arm carrying N
lines of unrelated real rules prose; `--pad-rules N --no-gate-arm` adds a
`pad-nogate` arm that also strips the BUILD self-audit step.

**Unguided baseline construction.** The without-arm prompt is the bare task string,
built from a field whitelist, `keep = ("id", "language", "snippet", "prompt",
"task")` (`run-clean.py` line 156), so a case's answer-key fields cannot leak in.
For live sub-agent arms, the bare prompt must carry an explicit override, because
sub-agents inherit the repo's agent files: "Use only your own knowledge and
judgement. This instruction overrides any standing instruction..."
(`run-build-safe-arms.py` line 33). Without it, 2 of 3 nominally-bare live agents
loaded the router anyway (README).

**Runs per condition, and why.** No fixed n is asserted as sufficient. The stated
rule: "One run is a data point, not a number. Never publish an n=1 figure without
its sample size attached," citing two findings a larger sample walked back
(+0.07 retracted at n=49, +0.40 revised to a 2-run mean of +0.39). `temp 0` is
documented as non-deterministic here: an untreated arm that cannot see the
treatment still moved 0.60 to 0.57 on rerun, so "any single-sample delta below
roughly 0.05 is unresolvable." Where variance matters, runs use `--samples 3
--temp 0.7`. Every subgroup signal the harness ever produced evaporated once the
subgroup grew (n=6 to 26, n=8 to 20), so subgroup deltas of one or two cases are
treated as a reason to author more cases, not a result.

**Invalidity/saturation check.** An instrument is called uninformative, not a
positive null, when the baseline is at ceiling. `BUILD-SAFE.md` states it plainly:
gpt-5.1's unguided arm scored 1.000, so "there is no headroom and the maximum
possible lift on `avoided` is zero," so the +0.19 lift on sonnet-4.6 "is
model-dependent and must not be quoted unqualified." `PRE-REGISTRATION.md` states
the same in advance: "An arm at the ceiling cannot show the gate *adding*
anything... this experiment is uninformative rather than a null, and must be
reported that way." Loaders and ablations also abort outright on an empty or
degenerate corpus rather than scoring it (`load_cases` exits on zero rows;
`audit_library_context` exits on an empty glob; `--ablate` exits if its target
file is missing) because a fake +0.00 is indistinguishable from a real one.

## 2. Scoring

Two kinds. Deterministic: `score.py` (set-intersection recall/precision),
`run-build-safe.py`'s regex plus AST function-body matching. Model-judged:
`run-completeness.py` `judge()` (reused by `run-decay.py`), `judge-calibration.py`.
Every judged instrument uses a different model than the one that produced the
artifact, blind to which arm produced it.

**Judge calibration.** `judge-calibration.py` scores four reporting-discipline
dimensions 0/1 each, against a hand-written known-bad report (flatly asserts
completeness) and known-good report (states scope, labels an item "needs
verification," conditions severity). Order is shuffled
(`random.Random(11).shuffle`) so the judge cannot infer arm from position. Result
in `BUILD-SAFE.md` §2: known-bad 0/4, known-good 4/4, confirmed before the real
arms (unguided 2.67/4, with-library 4.00/4) are read.

**Judge nondeterminism.** Handled by treating any delta under the measured noise
floor as unresolved, and by validating the judge's output *shape* every call, not
just parsing it. `judge()` (lines 233-264) asserts the returned key set exactly
equals the rubric's id set and every value is in `{present, absent}`, added after
a 2026-08-16 finding that a well-formed reply of the wrong shape (`{"results":
{...}}`, or `"Present"` with a capital P) silently scored 0.00 with no exception.

## 3. The negative-control CI mechanism (`check-negative-controls.sh`)

Two subjects, one script: Part A targets `check-invariants.sh`, Part B targets
`verify-setup.sh`.

**Part A.** A disposable git worktree is created at HEAD; the working-tree copy
of the gate itself is copied in and byte-compared (line 78), testing the code
just edited. A positive control runs first: the unmutated worktree must pass, or
the script aborts entirely. Then, for each of 28 named probes, a mutation is
applied (probe 1: append 600 padding lines past a 500-line cap; probe 24b:
replace the `CLAUDE.md` symlink with a plain copy of `AGENTS.md`). Before
scoring, `probe()` asserts the mutation actually changed the tree (`git diff
--quiet`, line 133); if not, it reports itself "PROBE BROKEN," a probe defect,
not a gate defect. The gate then runs once, and the verdict has three outcomes:
NOT CAUGHT (exit 0, check is inert); caught (exit nonzero AND the gate's output
contains the expected substring, matched via a pure-bash `case ... in
(*"$want"*)`, deliberately not piped into `grep -q`, line 158); FALSE PASS (exit
nonzero but the wrong check fired). FALSE PASS is treated as equivalent to NOT
CAUGHT, because a harness accepting any nonzero exit would report false coverage.

The no-pipe fix is explained by an incident: on 2026-09-06 `printf '%s\n' "$buf"
| grep -qF -- "$want"` reported a real catch as FALSE PASS on CI while a
diagnostic line three lines later, reading the same variable, printed the wanted
string, because `grep -q` exits at first match under `pipefail`. It did not
reproduce on macOS bash 3.2 or a synthetic case, so the exact trigger is not
established; the fix removes the pipe rather than chasing the trigger.

Between probes, `restore()` does `git reset -q --hard HEAD && git clean -fdq`
with no `|| true`, because a bare checkout+clean left `git add`-ed files behind
and let one probe's staged file leak into the next (probe 15 then failed on
check 6 instead of check 15, a FALSE PASS in the harness's own dry run).

**Part B** inverts the shape: builds a fixture (fake `$CLAUDE_CONFIG_DIR`, a
throwaway repo, a stubbed `gh` on `PATH`) where every check of `verify-setup.sh`
passes, confirms that with a positive control, then removes one precondition per
probe (no skills installed, hook configured but not installed, `gh run list`
all-skipped) and asserts that *specific* check fails, matched line-by-line
(`vs_out_has_fail`, line 450) rather than a whole-buffer glob.

**Precisely how it distinguishes a real catch from a false pass:** exit code
alone is never sufficient; the check is (exit != 0) AND (the intended check's own
labeled output line is what fired). Both incidents above show either half alone
producing a false result. Coverage is stated, not implied complete: the closing
lines name 23 of 28 invariants covered and list the 5 excluded, with why.

## 4. Pre-registration

Predictions are recorded in a dated file under `evals/results/<date>/`, committed
before the run, separate from the results file the run later produces. Example:
`evals/results/2026-09-06/PRE-REGISTRATION.md`, opening line: "Written and pushed
2026-09-06, BEFORE the run. Nothing has been executed against a live model for
this question." It states three named hypotheses with numeric thresholds fixed in
advance (H1 needs GATE-ABSORPTION >= +0.05; H0's null band is [-0.03, +0.03]), a
stated reason for writing first ("Item 25's padded run returned -0.01, and that
number has already been *interpreted*... If the follow-up runs before the
prediction is recorded, whatever comes back will read as confirmation of
whichever half of the sentence survives"), a falsification clause ("H1 is
refuted if GATE-ABSORPTION < +0.05. I will not rescue it by raising the padding,
changing the model, or re-reading the rubric"), and a list of ways the
experiment could measure nothing, written down "so it cannot be discovered
afterwards as an explanation for an inconvenient result."

**Verification path.** Not stated in the file itself as a mechanism: no
cryptographic timestamp, no signed hash, no append-only ledger. The only
verification a reader has is git history, the file's commit predates the results
file's commit in the public repo's timeline. `RESULTS.md` later reports the
actual outcome against the same named thresholds ("GATE-ABSORPTION +0.04... H1
refuted... underpowered, not answered"). That is the entire mechanism this
project itself relies on; it is worth stating plainly rather than assuming.

## 5. What is portable to a documentation collection with no code to run

**Needs a runnable artifact, does not transfer:** the with/without arm structure
(needs something to build and something to grade); `run-build-safe.py`'s
avoidance scoring and truncation guards (specific to scoring generated code); the
competitor benchmark, decay eval, and prompt-independence eval (all drive a model
against a task and grade the result); the negative-control CI mechanism as built
(specific to bash gates that check file contents mechanically, requires such a
gate to already exist and run in CI, neither of which `dev-conventions` has).

**Transfers as a discipline, no artifact needed:** the pre-registration
convention itself, writing the prediction, threshold, and falsification condition
into a dated committed file before acting, is a writing habit that applies
directly to a prose rule change; "one data point is not a number," applied to any
claim in `AGENTS.md` or the evidence document that cites a single incident as
proof a rule works; stating what is NOT covered precisely rather than implying
full coverage, which is a prose discipline visible in both
`check-negative-controls.sh`'s closing lines and the repeated "this measures X,
never Y, do not report this as a lift" pattern across `RESULTS.md`.

**The honest bottom line.** Most of this method is a measurement apparatus around
a generative task with a rubric a model never sees. `dev-conventions` has no such
task. The empirical machinery (arms, judges, calibration, noise floors) does not
transfer, because there is nothing to run it on. What transfers is a small set of
writing and reporting disciplines borrowed from how this project talks about its
own numbers, not the numbers-producing code.

## 6. The cheapest single thing to adopt in under a day

Pre-register predictions for rule changes, in the same lightweight form. Before
changing a rule in `AGENTS.md` on the strength of an anecdote or a single
observed failure, write one short dated note mirroring `PRE-REGISTRATION.md`'s
shape: what is expected to change, and what observation would show the change
did not help, committed before or alongside the rule change, not after. This
needs no code, no judge, no model calls, and directly answers
`dev-conventions`'s own stated hole ("never measured anything against a
control") in the one register a prose repository actually has: it does not
manufacture a control, but it stops the repository from reading its own outcomes
as confirmation after the fact, the exact failure mode `PRE-REGISTRATION.md`
names as its reason for existing.
