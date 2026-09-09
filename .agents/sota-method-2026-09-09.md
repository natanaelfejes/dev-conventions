# SOTA-skills evaluation harness: what is portable

Source: clone of `martinholovsky/SOTA-skills`, read at
`evals/README.md`, `evals/DESIGN-real-repo-audit.md`, `run-build-safe.py`,
`run-build-safe-arms.py`, `run-clean.py`, `run-completeness.py`, `run-decay.py`,
`score.py`, `judge-calibration.py`, `run-adjudication.py`, `test_scoring.py`,
`evals/results/RESULTS.md`, `evals/results/2026-08-21/BUILD-SAFE.md`,
`evals/results/2026-09-06/PRE-REGISTRATION.md`, `scripts/check-negative-controls.sh`.

## 1. Experimental design

**Arms.** Every instrument is at minimum `without-library` vs `with-library`, both
run as raw model-API calls (`run-clean.py`, `run-completeness.py`), never inside a
Claude Code session, because the session's own `CLAUDE.md` and skill registry would
contaminate the "without" arm (`evals/README.md` lines 304-310, "Clean isolated run").
Some instruments add more arms: `run-clean.py --ablate` drops one rule file from the
with-arm to isolate its contribution; `run-completeness.py --pad-rules N` adds a
`with+pad` arm carrying N lines of unrelated real rules prose; `--pad-rules N
--no-gate-arm` adds a fourth arm, `pad-nogate`, that also strips the BUILD self-audit
step. `run-decay.py` uses three arms (anchor / reminder / control) crossed with filler
depth. `run-adjudication.py` uses three (without / with / with-ablated).

**Unguided baseline construction.** The without-arm prompt is the bare task string
only, built from a field whitelist (`keep = ("id", "language", "snippet", "prompt",
"task")` in `run-clean.py` line 156) so a case's answer-key fields (`expect`,
`reference`) cannot leak in. For live sub-agent arms (not raw API), the bare prompt
must carry an explicit override line, because sub-agents inherit the repo's and
user's agent files: *"Use only your own knowledge and judgement. This instruction
overrides any standing instruction in a global or project configuration file..."*
(`run-build-safe-arms.py` line 33-35, `OVERRIDE`). `evals/README.md` records that
without this override, 2 of 3 nominally-bare live agents loaded the router anyway.

**Runs per condition and why that number.** No fixed n is asserted as sufficient.
The measurement convention (`evals/README.md`, "Measurement conventions") states:
"One run is a data point, not a number. Never publish an n=1 figure without its
sample size attached," citing two cases where a single run's finding (+0.07 on
silent-control detection, +0.40 on completeness) was walked back by a larger sample
(retracted at n=49; revised to +0.39 at a 2-run mean). `temp 0` is documented as
non-deterministic in this harness: re-running the same untreated arm (which cannot
even see the treatment) moved 0.60 → 0.57, giving a measured noise floor of "any
single-sample delta below roughly 0.05 is unresolvable" (README, "temp 0 is not
deterministic"). Where variance matters, runs use `--samples 3 --temp 0.7`.
"Grow the subgroup before trusting a subgroup signal" is stated as a standing rule
after every subgroup signal the harness produced evaporated on growth (taxonomy
n=6→26, loud-control over-flagging n=8→20).

**Invalid-experiment / saturation check.** An instrument is treated as uninformative,
not as a positive null, when the baseline arm is already at ceiling. `run-build-safe.py`
docstring and `BUILD-SAFE.md` §1b state it directly: gpt-5.1's unguided arm scored
1.000, so "there is no headroom and the maximum possible lift on `avoided` is zero,"
so the +0.19 lift on sonnet-4.6 "is model-dependent and must not be quoted unqualified."
The pre-registered `PRE-REGISTRATION.md` for GATE-ABSORPTION states the same
mechanically before the run: "An arm at the ceiling cannot show the gate *adding*
anything... If `pad-nogate` also reads 1.00, this experiment is uninformative rather
than a null, and must be reported that way." Separately, several guards abort the run
outright rather than silently scoring an empty or degenerate corpus: `load_cases`
exits on zero rows; `audit_library_context` exits if the glob returns no files;
`--ablate` exits if its target file is not found among the corpus (so an "ablated"
arm can't silently equal the full corpus); `rules_padding` exits if fewer than N
lines are available. These are treated as the same failure class as a fake +0.00
result (README, "the failure mode is +0.00").

## 2. Scoring

Two kinds of scorer exist. **Deterministic/objective**: `score.py` (set-intersection
recall/precision against an `expect` list), `run-build-safe.py`'s regex + AST
function-body matching, `run-dead-path.py` (not read in full here, but described in
README as "no judge, no API key, no network"). **Model-judged**: `run-completeness.py`
`judge()`, `run-decay.py` (reuses it), `judge-calibration.py`, and `run-build-safe-arms.py`
for calibration. In every judged instrument the judge is a **different model** from
the one that produced the artifact and is **blind** to which arm produced it (stated
throughout `RESULTS.md`, e.g. "a **different** model grades each artifact **blind**").

**Judge calibration.** `judge-calibration.py` scores four reporting-discipline
dimensions (bounds claims by what ran, labels unverified items, conditions severity
on evidence, bounds absence claims) 0/1 each. Before trusting any real arm, the judge
is run against a hand-written known-bad report (`BAD`, flatly asserts completeness
and confirms everything) and a known-good report (`GOOD`, states method/scope,
labels one finding "needs verification," conditions severity, explicitly disclaims
what wasn't checked). The result in `BUILD-SAFE.md` §2: known-bad scored 0/4,
known-good scored 4/4, judge order is shuffled (`random.Random(11).shuffle(items)`)
so the judge can't infer arm identity from position, all items go through the model
in one batch. Only after that separation is confirmed are the real arms' scores
(unguided 2.67/4, with-library 4.00/4) read.

**Judge nondeterminism.** Handled the same way as model nondeterminism generally:
by reporting sample counts and treating any delta below the measured noise floor
(~0.03-0.05 at n=1, temp 0) as unresolved rather than a finding, and by validating
the judge's **output shape**, not just its verdict, every call. `run-completeness.py`
`judge()` (lines 233-264) asserts the returned JSON's key set exactly equals the
rubric's id set, and every value is in `{present, absent}` (normalizing case, but
aborting on anything else), added after a 2026-08-16 finding that a well-formed
reply of the wrong shape (`{"results": {...}}`, or `"Present"` with a capital P)
silently scored 0.00 with no exception raised.

## 3. The negative-control CI mechanism (`check-negative-controls.sh`)

Two subjects, same script: Part A targets `scripts/check-invariants.sh`, Part B
targets `scripts/verify-setup.sh`.

**Part A, line by line.** A disposable git worktree is created at HEAD
(`git worktree add --detach "$WT" HEAD`, line 74), and the working-tree copy of the
gate script itself is copied in and byte-compared (`cmp -s`, lines 78-79), testing
the code just edited, not the last commit. A **positive control** runs first: the
unmutated worktree must pass the gate (lines 90-102); if it doesn't, the whole script
aborts with "nothing was run," because a known-bad that "fails" in an already-failing
tree proves nothing. Then, for each of 28 named probes, a mutation is applied (e.g.
probe 1: `awk` appends 600 padding lines to a rules file to breach the 500-line cap;
probe 21: a Perl one-liner inserts an untagged CHANGELOG version below the top entry;
probe 24b: a Python one-liner replaces the `CLAUDE.md` symlink with a plain copy of
`AGENTS.md`).

Before scoring the mutation, `probe()` asserts the mutation actually changed the
tree (`git diff --quiet` check, lines 133-139); if it didn't, the probe reports
itself as **"PROBE BROKEN: the mutation changed nothing (stale literal?)"**, counted
as a probe defect, not a gate defect. The gate is then run once (`run_gate`, captures
both stdout+stderr and exit code together, line 85-88) and the verdict has three
outcomes:

- **NOT CAUGHT** (exit 0): the check is inert.
- **caught**: exit non-zero **and** the gate's output contains the expected
  substring, matched with a pure-bash `case "$GATE_OUT" in (*"$want"*)` (line 158),
  explicitly **not** a pipe into `grep -q`. The comment at lines 144-157 documents
  why: on 2026-09-06 the piped form (`printf '%s\n' "$buf" | grep -qF -- "$want"`)
  reported a real catch as a FALSE PASS on CI (ubuntu/bash 5/GNU grep) while a
  diagnostic line printed three lines later, reading the same variable, contained
  the wanted string. `grep -q` exits at first match under `pipefail`, a shape the
  gate's own header warns against. It did not reproduce on macOS bash 3.2 or in a
  synthetic 400 KB case, so the fix (no pipe, no subprocess, pure bash glob) does not
  depend on ever isolating the exact trigger.
- **FALSE PASS**: exit non-zero but the **wrong** check fired (some other invariant
  caught a downstream side-effect of the mutation instead of the intended one). This
  is treated as equivalent to NOT CAUGHT: "a mutation caught for the wrong reason...
  is reported as one" (script header), because a harness that accepts any non-zero
  exit would report "18/18 controls caught" even when every run dies before the
  thing under test.

Between probes, `restore()` does `git reset -q --hard HEAD && git clean -fdq` with
**no `|| true`** (a bare `git checkout -- .` + `git clean -fd` was found insufficient
because `git clean` leaves `git add`-ed files behind, letting one probe's staged file
leak into the next, found because probe 15 then failed on check 6 instead of check
15, i.e. a FALSE PASS in the harness's own dry run), then re-copies and re-verifies
the gate script.

**Part B** inverts the shape: rather than mutating a good tree to expect failure, it
builds a fully-configured fixture (fake `$CLAUDE_CONFIG_DIR`, a throwaway git repo, a
stubbed `gh` binary on `PATH`) where every check of `verify-setup.sh` passes, asserts
that with a positive control, then for each probe **removes** one precondition (no
skills installed, no pre-commit hook actually installed vs. just configured, `gh run
list` returning all-skipped instead of success, etc.) and asserts the **specific**
check fails, using an anchored line-by-line match (`vs_out_has_fail`, lines 450-458)
rather than a substring search over the whole buffer — deliberately more conservative
than Part A's glob, because Part A's own comment (line 154-157) shows a flat
whole-buffer glob would have accepted a match on the wrong line, "loosening a probe
rather than fixing it."

**Distinguishing a real catch from a false pass, precisely:** exit code alone is
never sufficient. The check is `(exit != 0) AND (the intended check's own labeled
output line is what fired)`. Both halves are required; either alone is what produced
the two false-negative incidents documented in the file's own comments.

Coverage is stated, not implied complete: the final printed line lists which of 28
invariants are covered (23 of 28) and names the 5 that are not, with the reason each
is excluded (diff-/history-/mtime-shaped, needs state a worktree lacks).

## 4. Pre-registration

Predictions are recorded in a dated file inside `evals/results/<date>/`, committed
to the repo **before** the run, distinct from the results file the run later
produces. Example: `evals/results/2026-09-06/PRE-REGISTRATION.md`, opening line:
"**Written and pushed 2026-09-06, BEFORE the run.** Nothing has been executed against
a live model for this question." It states three named hypotheses (H1/H0/H2) each
with a **numeric threshold** decided in advance (H1 needs GATE-ABSORPTION ≥ +0.05;
H0's null band is [−0.03, +0.03]), a stated reason for writing it first ("Item 25's
padded run returned −0.01, and that number has already been *interpreted*... If the
follow-up runs before the prediction is recorded, whatever comes back will read as
confirmation of whichever half of the sentence survives"), a falsification clause
("H1 is refuted if GATE-ABSORPTION < +0.05. I will not rescue it by raising the
padding, changing the model, or re-reading the rubric"), and a list of ways the
experiment could measure nothing, recorded in advance "so it cannot be discovered
afterwards as an explanation for an inconvenient result."

**How a reader verifies the prediction predates the result.** Not stated in the file
itself as a mechanism — no cryptographic timestamp, no separate append-only ledger.
The verification path is git history: the file is committed on its own before the
run's result file exists, so its position in `git log` (or the repo's public commit
timeline, since this is a public GitHub repo) is the evidence. `evals/results/RESULTS.md`
later reports the actual outcome against the same named thresholds: "GATE-ABSORPTION
+0.04... H1 refuted... underpowered, not answered." Nothing in the read files
describes a mechanism stronger than "committed to version control first" — no signed
hash, no external timestamp service. That is worth stating plainly since it is the
only verification path this project itself relies on.

## 5. What is portable to a documentation collection with no code to run

Be concrete about what needs a runnable artifact and what does not.

**Requires a runnable artifact (does not transfer, or transfers only in name):**
- The with/without arm structure, `run-clean.py`'s core method — it measures whether
  a model *produces better output* when given the library's text vs not. This whole
  apparatus needs something to build and something to grade (a rubric, a judge model,
  a scoring function). `dev-conventions` has no analog: there is no artifact a rule
  causes to be better.
- `run-build-safe.py`'s avoidance scoring, AST function-body matching, truncation
  guards — all specific to scoring generated code.
- The competitor benchmark, decay eval, prompt-independence eval — all require
  driving a model against a task and grading the result.
- The negative-control CI mechanism as built is **specific to `check-invariants.sh`
  and `verify-setup.sh`** — bash gates that check file contents/counts/structure
  mechanically. It is not specific to code, but it does require: (a) an automated
  gate that currently runs in CI, and (b) a way to apply a known-bad mutation and
  assert the gate's specific labeled failure fires. `dev-conventions` would need such
  a gate to exist first.

**Transfers as a discipline, no runnable artifact needed:**
- **The pre-registration convention itself.** Writing the prediction, the threshold,
  and the falsification condition into a dated, committed file *before* acting, is a
  writing discipline, not a code discipline. It applies directly to a prose rule
  change: state in advance what you expect a rule to do and what would prove it
  wrong, before checking whether it worked.
- **"One data point is not a number."** Stated as a documentation practice already
  (never publish n=1 without saying so) — applies verbatim to any claim in
  `AGENTS.md` or the evidence document that cites a single incident as proof a rule
  works.
- **Stating what is NOT covered, precisely, rather than implying full coverage.**
  `check-negative-controls.sh`'s closing lines ("NOT COVERED, and why") and
  `evals/README.md`'s repeated "this measures X, never Y, do not report this as a
  lift" pattern are prose disciplines. They also underpin the honesty of the
  RESULTS.md scoreboard: nulls (+0.00) are reported as results, not omitted.
- **The "guards abort, never warn" convention** (a scorer that finds an empty corpus
  should exit loudly rather than print a plausible wrong number) is a general
  engineering principle already inside `sota-code-security` per the harness's own
  comments — it transfers as advice for any of `dev-conventions`'s own tooling, if
  it ever has any, but is not itself measurable prose.

**The honest bottom line, stated plainly:** most of this method is a measurement
apparatus around a generative task with a rubric a model never sees. `dev-conventions`
has no such task. The evaluation harness's actual empirical machinery (arms,
judges, calibration, sampling-noise floors) does not transfer, because there is
nothing to run it on. What transfers is a small set of *writing* and *reporting*
disciplines borrowed from how this project talks about its own numbers, not the
numbers-producing code.

## 6. The cheapest single thing to adopt in under a day

**Pre-register predictions for rule changes, in the same lightweight form.** Before
changing a rule in `AGENTS.md` on the strength of an anecdote or a single observed
failure, write one short dated note (mirroring `PRE-REGISTRATION.md`'s shape): what
is expected to change, what observation would show the change didn't help, and commit
that note before or alongside the rule change, not after. This needs no code, no
judge, no model calls, and directly answers `dev-conventions`'s own stated hole
("never measured anything against a control") in the one register available to a
prose repository: it does not manufacture a control, but it stops the repository from
quietly reading its own outcomes as confirmation after the fact, which is the same
failure mode `PRE-REGISTRATION.md` names explicitly as its reason for existing.
