# First adoption run: friction log, 2026-09-10

**The first time this collection's procedure was executed rather than read.** Nine verification
passes and two outside audits preceded it. Recorded unnamed per this repository's own rule: the
repository is a private .NET service on a Windows-first toolchain, hosted on a platform other than
the most widely documented one, single author, self-merged history.

**Phase 2 wall clock: roughly 16 minutes.** Reported with the adopting agent's own caveat attached,
which is the honest part: it timestamped four step boundaries and kept working past two of them, so
the per-step attribution is approximate and it declined to present clean per-step numbers it had not
measured. **One data point, no sample size, so it is a duration and not a finding.**

| Span | Wall clock |
|---|---|
| Phase 2 total | ~16 min |
| Security, including loading the two rule files | ~4 min |
| Documentation | ~2 min |
| Mechanical check, including making it fail four ways | ~2 min |
| Instruction file | ~1 min |
| Not in any step: full local gate, then git recovery | ~7 min |

**The largest single span is not in any step.** Roughly seven of sixteen minutes went to the
repository's own full check and then to recovering from a concurrent session moving HEAD. Neither is
in the procedure.

## What it found in the collection

| # | Finding | Landed as |
|---|---|---|
| 1 | Layer selectors could never match any shipped example | **Error 30**, fixed, twelfth build check |
| 2 | `reviewers` derivation: platform-specific merge wording, 0 against 33 | **Error 10 replication**, `PROFILE.md` now reads the host off the remote first |
| 3 | Derivation commands are POSIX only, never stated | `PROFILE.md` states the requirement, with a translation table |
| 4 | No concept of re-adoption; step 4 reads as greenfield | `ADOPTION.md` step 4 |
| 5 | No handling of a profile that already exists | `ADOPTION.md` phase 1 |
| 6 | "Report every finding before changing anything" gates exposures or all edits? | `ADOPTION.md` step 1, disambiguated |
| 7 | `secrets` scalar or list, `docs.absent` when nothing is absent, `setup` when the file does not exist | Schema and template |
| 8 | Deleting prose a script enforces orphans the rationale | `SKILL.md`, refined |
| 9 | `EVIDENCE.md` referenced repeatedly and absent from every install | `SKILL.md`, says what to do instead |
| 10 | Nothing tells an adopting agent to check its branch before each commit | `ADOPTION.md`, whole-job rules |

## The two things worth reading twice

**A concurrent session moved HEAD mid-pass and one commit landed on the default branch.** Recovered
without loss and nothing was pushed. The adopting repository's own instruction file warns about
exactly this; the procedure did not. **A two-phase procedure with a human stop in the middle is
precisely where another session gets a window, and the stop is when you are least likely to
re-check.** Now a rule.

**Two adoption passes converged on the same two findings from different directions**, hours apart,
and one of them fixed a finding before the other reported it. That is corroboration, and it also
means a profile carried a claim that was true when written and false within hours. **The staleness
window for a derived profile is measured in hours, not months**, when anything else is working the
same repository.

## What it reported and was right not to fix

A contradiction between the adopting repository's instruction file and this skill about instruction
file length. The repository asserts a measured cost past a line count; this skill says no such
number is measured. **Neither is verifiable from inside that repository and the repository's claim
cites nothing.** The agent left it standing and reported it, which is what the counter-example
instruction asks for. Editing it would have substituted this collection's claim for the
repository's, on no more evidence.

## What it could not verify

An employer IT policy not present in the repository. Whether three named review passes are actually
run, which lives in pull request descriptions on a host it could not reach. Whether a new gate
passes in CI, since the host's clone depth is not reproducible locally. Hardware-dependent TLS
behaviour. Whether any local debug log was ever copied off the machine, which git cannot speak to.
**And run-to-run stability of any of it**, since every judgment is a single pass, which this
collection's only replicated finding discounts.
