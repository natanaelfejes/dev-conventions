# Branch, merge and review workflow

Load when setting up how changes move through a repository, or when someone proposes a workflow rule
and you want to know whether anything measured supports it.

**Read this section before any rule below.** It is the most important thing in the file.

## Almost none of this is measured, and the one famous number is contested

Researched 2026-09-04. The everyday conventions of branching, merging and pull requests are the most
confidently asserted and least measured practices in software engineering. Here is what each actually
rests on:

| Area | Rests on |
|---|---|
| PR size thresholds | One industrial case study from **2006**, whose numbers differ between retellings, including between this collection's own two verification passes. No modern causal measurement found |
| Trunk-based development | Correlational survey data. Its own authors do not claim causation |
| Merge strategy (squash, merge, rebase) | **Pure custom.** No measurement located at all |
| Pre-merge gates | Plausible reasoning. Marginal value unmeasured, bypass rates undocumented |
| Commit message conventions | Adoption is measured. Benefit is asserted, never measured |
| AI-specific practice | Early, and almost entirely vendor or self-reported |

### The "keep pull requests under 400 lines" rule, settled against the original 2006 book

**Settled 2026-09-08 by reading the book itself**, after two verification passes read its secondary
sources and extracted materially different numbers. Both passes were wrong in interesting ways and
the popular rule is folklore, though not quite in the way this section originally claimed.

The source is an industrial study of roughly **2,500 reviews, 3.2 million lines of code, 50
developers**, published in 2006. Quoting it directly:

| What the book actually says | Kind of claim |
|---|---|
| "Reviewers slower than **400 lines per hour** were above average in their ability to uncover defects. But when faster than 450 lines/hour the defect density is below average in **87% of the cases**" | Measured, and it is a **rate** |
| "Anything **below 200 lines** produces a relatively high rate of defects, often several times the average... no review larger than 250 lines produced more than 37 defects per 1000 lines" | Measured, and it is a **size** |
| "after 60 minutes reviewers 'wear out' and stop finding additional defects" | Measured, and cited to a separate study |
| "a reviewer will **probably** not be able to review more than **300-400 lines** of code before his performance drops" | **A hypothesis the book derives** from the two rows above, hedged in its own sentence |
| "Industry experts say inspection rates should not exceed **200 lines per hour**" | Inherited from Fagan and Gilb, not measured here |
| "your overall speed is going to be about **200 to 400 lines of code per hour**... you should expect to get a **70 to 90% yield**" | A **rate** again, in a Q&A about reviewing *your own* code |

**So the original claim was right about the mechanism.** The famous 400 is **400 lines per hour**, a
review rate. The popular rule converts it into a batch size, which the book never states as a
measurement. The second verification pass's "200 to 400 lines" and "70 to 90%" came from the last row
above, where both numbers describe a rate and its yield: **that pass committed the exact misreading
this section exists to describe.**

**And the original claim was too strong.** A 300-400 line ceiling is not baseless. The book derives
one, explicitly as a hypothesis, from the 60-minute wear-out plus a defensible rate. So "under 400
lines" is a reasonable heuristic with a stated derivation behind it, and it is not a measured
threshold, and anyone citing it as one is citing something the book hedged.

**One caveat the book raises about its own strongest size finding**, and it is the sharpest thing in
the chapter: the "small reviews find more defects per KLOC" result **assumes true defect density is
constant across large and small changes**. The book flags this itself. If a 400-line change does not
in fact contain four times the defects of a 100-line change, the result partly measures the
assumption.

**What to actually do**, and it follows from the rate rather than the size: keep a review to one
sitting under an hour, which for most code means a few hundred lines. Size is the proxy; time and
pace are what was measured. `EVIDENCE.md` records the full resolution under contested
findings.

**What survives either reading, and it is weaker and still worth having:**

- **Do not cite any specific line threshold from this study.** The figures attributed to it **vary
  between retellings**, which is itself the reliable finding. A rule whose number changes depending
  on who repeats it is not a measurement you can lean on.
- **Do not conclude that pull request size does not matter.** Both readings agree on the shape:
  **moderate-sized changes, reviewed unhurried, catch more defects.** Both agree there is a rate
  ceiling above which detection degrades. That is real and actionable without a threshold.
- **Do not let a review sitting run long.** Both readings place the effectiveness limit somewhere
  near the one-hour mark, and this is the part almost nobody repeats.
- **Do not treat one 2006 industrial case study as a general law**, whichever numbers it contains. No
  modern causal measurement of pull-request size against production defect escape was found.

One controlled experiment on change decomposition exists (arXiv:1805.10978) and its numbers could not
be extracted in either pass. **Recorded as could-not-confirm**, and it is the thing to read before
anyone cites a size threshold again.

---

## Branching

**Trunk-based development is correlational, and its own authors say so.** The best-known source
reports that teams with **three or fewer active branches**, merging to trunk **at least daily**, with
**no code freezes**, cluster among higher delivery performers. That is survey data from 2016 to 2017,
self-reported practices correlated with self-reported performance. It establishes association among
high performers. **No experimental test was found.**

That is still the best available signal, so act on it, but as judgment:

- **Do not run long-lived feature branches without a reason you can state.** The correlation points
  one way and nothing points the other, which is weak grounds and better than none.
- **Do not stack a branch on an unmerged parent** unless you describe the whole stack and say why it
  was not split. Merge parents first, then rebase. `first-party`: a seven-commit stack once merged
  looking like a documentation change, because nobody read `git log main..branch` first.
- **Do not let branches accumulate.** `first-party`, and the single biggest process failure observed
  in this collection's own repositories. One branch in flight; merge or close before starting the
  next. It is invisible while it happens and expensive to unwind.
- **Do not leave a branch convention unwritten.** Two inventoried repositories had a real naming
  pattern followed by roughly four branches in five and **written down nowhere**, which means the
  people who deviated were not breaking a rule.

## Merging

**This is the one area where the honest answer is that nothing is known.** A deliberate search found
**no measurement** comparing squash, merge commits and rebase against bisectability, revert success or
blame usefulness. Not weak evidence. None.

So the arguments are mechanical and real, and the choice is custom:

- Merge commits preserve full history and clutter the log.
- Rebase gives linear history and **rewrites hashes**, which breaks shared branches and invalidates
  signatures.
- Squash gives one clean commit and **destroys intra-feature bisectability** if that commit is large.

- **Do not argue about merge strategy as though evidence exists.** Pick one, write it down, apply it
  consistently. Consistency is the only property here with a defensible justification.
- **Do not rebase a branch someone else has pulled.** This is the one mechanical hazard rather than a
  preference.

## Pre-merge gates

What gates catch is described qualitatively and their marginal value is unmeasured. What is
documented, and matters more, is **how easily they are bypassed**:

- A pre-push hook is skipped with `--no-verify`.
- Repository administrators can bypass branch protection by default, even where reviews are required.
- **The bypass discussion in 2026 is mostly about agents**, which get told to skip hooks to unblock
  themselves.

- **Do not treat a bypassable gate as a control.** Treat it as a reminder. If a property must hold,
  it belongs somewhere that cannot be skipped: a server-side check, or a test that fails.
- **Do not instruct an agent to skip a gate to unblock itself.** If a gate is wrong, fix the gate.
  An agent that learns hooks are optional will skip them again, and it will be right to.
- **Do not add a gate without stating what it prevents.** Nothing measures the value of the marginal
  gate, so an unjustified one is pure friction, and friction is what teaches people to bypass.
- **Do not rely on a gate a fresh clone does not install.** `first-party`: one repository's
  pre-commit hook was its stated last defence against committing real user data, and it was absent
  from that repository's own setup instructions. A new contributor following the documentation never
  installed it.

## Commit messages and attribution

**Conventional Commits: adoption is real, benefit is asserted.** A 2025 sample found the format in
**360 of 381** randomly sampled repositories in one language ecosystem, 198 of them at 80% compliance
or better. No source measures a downstream benefit. Every stated benefit is mechanical: it enables
automated versioning and changelog generation.

- **Do not adopt a commit convention for quality reasons.** Adopt it because you want the tooling it
  enables, or do not adopt it. Both are fine; the quality argument is unsupported.

**AI attribution has real conventions now, plural, and which one applies depends on your
ecosystem.** During 2026 several major projects adopted trailer-based disclosure and **they did not
converge on one token**. The Linux kernel, Fedora, Rocky Linux and Zephyr use **`Assisted-by:`**, the
kernel's form carrying the agent and model version. The Apache Software Foundation and OpenInfra use
**`Generated-by:`**. OpenTelemetry prescribes **no trailer**, describing assistance levels instead.
`RESEARCH.md` has the table with each row's primary source.

What *is* common to all of them is the structural rule: **disclose the assistance, and never in a
field that certifies authorship.** The kernel bars AI agents from `Signed-off-by` outright.

An earlier version of this paragraph asserted a seven-project convergence on `Assisted-by:`. It was
wrong on two projects and named two more that were never verified. Recorded as error 21.

- **Do not invent a disclosure scheme local to your repository.** Follow the one your ecosystem is
  converging on.
- **Do not put an agent in `Signed-off-by`.** That field is a human attestation.

## What changes when an agent writes the diff

The newest and weakest-sourced part of this file. Treat all of it as early signal.

- **Pull requests get bigger and reviews get slower.** The largest survey programme in this space
  reported, for 2025, **PR size up about 154%** and **code review time up about 91%** alongside AI
  adoption, with organisational delivery metrics flat despite more tasks completed and far more pull
  requests merged per person. Self-reported and cross-sectional, so association only. But it is the
  one concrete number suggesting size norms are already shifting under your feet.
- **Agent-authored changes carry more redundancy.** A January 2026 paper reports agent-generated code
  showing more duplication and technical debt per change than human-authored code. So the review
  question shifts from "is this correct" toward "is this reinventing something that exists".
- **Merge rates and reviewer latency may be much worse for AI-assisted pull requests.** One vendor
  benchmark reports a large gap in 30-day merge rate and a several-fold increase in reviewer pickup
  time. **Unconfirmed against a primary source and vendor-derived**, so do not quote the figures.
  Watch your own numbers instead.
- **Isolate any agent that commits or branches.** Without a separate worktree, concurrent agents
  overwrite each other's edits to the same file with **no error at all**, discovered later when tests
  fail. This is a described mechanism rather than a measured rate, and it is confirmed `first-party`
  in this collection: a worker without isolation moved `HEAD` and edited files underneath its
  orchestrator.

## What to actually do, given how little is known

The honest summary, and every line is judgment rather than evidence:

1. **Small changes, unhurried review, short sittings.** The 2006 study supports the shape even though
   its threshold has been mangled.
2. **Short-lived branches, few of them, merged often.** Correlational, and nothing argues the other
   way.
3. **One merge strategy, written down, applied consistently.** The choice does not matter; the
   consistency is the only defensible part.
4. **Gates that cannot be bypassed for the properties that must hold**, and no gates at all for the
   ones that need not.
5. **Follow your ecosystem's AI-attribution convention** rather than inventing one.
6. **Watch your own review-load numbers** rather than trusting anyone's, including the ones above.
