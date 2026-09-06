---
name: dev-conventions
description: Evidence-graded conventions for AI-assisted development, covering claim verification, instruction files, delegation, docs and security. Adapts per repo. Load when setting up or auditing conventions.
---

# Development conventions, evidence-graded

**Version 0.9.0. External claims last rechecked 2026-09-06.**

## What this is not

Not a guide to writing an instruction file or a skill. That ground is taken, and by the people best
placed to hold it: **all three major model vendors now publish their own first-party authoring
guidance**, and the community collections around it run to tens of thousands of stars. If you want
to know how to structure a `SKILL.md` or what belongs in an `AGENTS.md`, read the vendor
documentation first. This is not competing with it.

Not a portability layer either. The skill format is itself a cross-tool standard now, supported
natively well beyond one vendor, so a collection like this travels without needing a translation
story. That used to be a selling point. It is now just how things work.

Not a set of practices to adopt wholesale. Several of these are covered elsewhere, some of it
better, and the good published collections are credited where they apply.

**What this does that those do not: it grades the evidence behind each claim by review trail, and it
adapts to your repository instead of prescribing one.** Most advice in circulation asserts practices
without saying how strongly they are supported, which is how unmeasured line-count targets became
widely repeated facts and how a vendor security study's flaw count became a nineteen-times-larger
malicious-payload count in this very document. So every claim here carries a tier, disagreements
between sources are left standing rather than averaged, and the things nobody has measured are named
as such, including several this document would rather were settled.

**Read the version line, and distrust this file if it is old.** The field moves fast enough that
adoption figures, vendor coverage and the supported-tool lists go stale in months. Every dated claim
records the date it was checked, `EVIDENCE.md` keeps its administrative facts in one section
precisely so they can be rechecked as a unit, and a stale entry there counts as a defect rather than
as background. A document that grades its research carefully and then asserts an ecosystem fact as
timeless has hidden its weakest claim where nobody is looking.

Four warnings, up front, because they bound how much you should trust it:

- **A large share of this rests on first-party observation** of four repositories, all small, one or
  two people each. That is a real confound and it is this collection's central weakness: **a pattern
  in all four may be a pattern in how one person works.** Nothing here is observed at organisational
  scale. All of it is labelled `first-party`, which is a warning rather than a boast.
- **Absence of a recorded signal is not absence of the practice.** Most first-party findings here are
  read out of git history, and git proves only what was written down. A team that reviews by
  screen-share, chat or an external tracker leaves the same trace as a team that does not review at
  all. Every claim below about what a repository "did not do" should be read as what it **did not
  record**, and that distinction is load-bearing.
- **Nothing here has been measured against a control.** No A/B test, no before-and-after on defect
  rates. Where a number appears it is either cited to an external source with a tier, or it is a
  direct measurement of something mechanical like token counts.
- **The documentation rot taxonomy has a known bias and one external contradiction**, both stated at
  the top of `DOCS.md`. It ranks by *recorded* corrections, so it under-weights repositories that
  never audit their own documents, which are the ones whose documentation is worst. And a study of
  2,303 agent context files across 1,925 repositories found those files behave as living
  configuration rather than as documents that decay, which is a direct hit on the part of the
  taxonomy covering instruction files. The taxonomy now claims only what it can: documents nobody
  has a reason to open.

### What is deliberately not covered

Named rather than omitted, because a reader cannot tell an omission from an oversight:

- **Hooks, subagent configuration, and slash command *authoring*.** The file formats and flags are
  vendor-specific and vendor-documented. Read those. **The workflow conventions those commands
  encode are a different matter and are now covered** in `WORKFLOW.md`: that split was wrong for a
  while, and branch, merge, review and gate practice fell through the gap.
- **Plugins and marketplaces.** Distribution mechanics differ per tool and there is nothing
  evidence-graded to say yet.
- **IDE integration.** Nothing here that is not already better covered elsewhere.
- **Product rankings of any kind**, including harnesses, models and subscriptions. No independent
  head-to-head exists, they rot within a quarter, and a ranking is not something an agent acts on.
  `TOOLING.md` maps the categories instead, and `SECURITY.md` has the five facts to establish before
  granting any tool access.

Evaluation harnesses **were** on this list as the collection's largest acknowledged hole. They are
now covered, in "Measuring whether any of this works" below, because a document that keeps saying a
practice is unmeasured owes the reader a way to measure it.

Licensed MIT, except `LOCAL.md`, which names a personal toolchain and machine paths and is not part
of any distribution. `OPERATING.md`, the human-facing half, is included.

---

Rules below are phrased as **prohibitions**, deliberately. A large study of real agent rule files
found that every individually beneficial rule was a negative constraint and every individually
harmful one was a positive directive. That study is **tier 4** (preprint, no venue acceptance), so
treat the phrasing as a well-motivated convention rather than a settled result. Keep it consistent
anyway: mixed phrasing is worse than either style.

**Never `@`-import this skill from an instruction file.** It is a skill so that it loads on demand.
Importing it turns a reference document into per-turn context, which is the exact cost it exists to
avoid.

## Read the profile first

This skill **adapts, it does not prescribe**. Repositories legitimately differ: some carry a
changelog and a roadmap, some deliberately carry neither; some have a second human reviewer, most
solo projects do not.

Before applying any rule below, read `.agents/profile.yml` (or the profile block in the root
instruction file). It declares team size, which documentation slots exist, the stack's exact
commands, which review passes are available, and the maturity level. `PROFILE.md` holds the schema.

- **Do not assume a documentation slot exists.** Check the profile.
- **Do not apply the solo rules to a team repository, or vice versa.** The profile decides.
- **Do not proceed silently when no profile exists.** State the inferences you are making, then
  offer to write one.

## Companion files

| File | Load it when |
|---|---|
| `PROFILE.md` | Writing or reading a repo profile |
| `EVIDENCE.md` | A rule here is challenged, or you need a claim's tier and source |
| `DOCS.md` | Setting up, auditing, or pruning a repository's documentation |
| `SECURITY.md` | Touching auth, secrets, CI, untrusted input, or installing a skill or MCP server |
| `WORKFLOW.md` | Setting up branching, merging, pull request or pre-merge gate conventions |
| `RESEARCH.md` | You need support from outside engineering, are writing for a research audience, or want this citable |
| `TOOLING.md` | Choosing what to put around an agent, or checking whether you are missing a category |
| `OBSERVABILITY.md` | Deciding what to record about agent work, or explaining a workflow's cost or behaviour |
| `VOCABULARY.md` | A term is doing persuasive work in a decision, a proposal, or a vendor pitch |
| `OPERATING.md` | Human-facing: prompting, delegation, model and vendor selection |

---

## Where each layer's rules come from

Stated once here rather than tagged on every line, because a tag on every line is unreadable and an
untagged rule is unaccountable. `EVIDENCE.md` carries the sources.

| Section | Provenance |
|---|---|
| Verifying a claim | **Mixed.** Run-to-run nondeterminism is **tier 1**, the only replicated finding here. The rest is `first-party` method, demonstrated on external papers: the habits are this collection's own, what they were tested on is public |
| Instruction files | **Mixed, all external, all weak.** Rule polarity, authorship and repository overviews are each tier 4. Analyzer-beats-prose and the incident rule are `first-party` |
| Working with agents | **Mixed.** Agent-only review and reviewer disagreement are tier 2; context-beats-procedure is tier 3; multi-agent degradation and context length are tier 5. Worktree collision and the delegation heuristic are `first-party` |
| Measuring whether any of this works | **Mostly tier 7**, vendor and practitioner. Nondeterminism is tier 1, judge bias is tier 4. The absence of any controlled defect study is a recorded search result, not an assumption |
| `OBSERVABILITY.md` | **Mixed.** The content-off-by-default rule is a standards-body default, the strongest thing in that file. Mix shift and heartbeat monitoring are established practice from outside this field. Alert fatigue transfers by analogy and says so. Cost figures are vendor-adjacent. Two failure modes are `first-party` |
| `VOCABULARY.md` | **Weaker sourcing than the rest, and it says so at the top.** Verdicts are this collection's judgement; the figures come from one research pass and were not each re-verified to primary sources |
| `WORKFLOW.md` | **Mostly not measured, and the file leads with that.** One 2006 industrial case study behind PR size, correlational survey data behind branching, nothing at all behind merge strategy. The AI-specific layer is vendor and self-reported |
| `TOOLING.md` | **A map, not a ranking.** Categories are durable; the named products are dated illustrations. No independent head-to-head of these tools exists |
| `RESEARCH.md` | **Convergence evidence rather than measurement.** Where a research community independently requires what engineering practice recommends. Also records one open problem nobody has solved |
| Commands, diffs and change descriptions | **Entirely `first-party`.** Every one is a specific incident. No external source was found for any of it |
| Layer 2, solo | **Entirely `first-party`** |
| Layer 3, team | Disclosure and policy prevalence are tier 2; agent-only review is tier 2. The rest is **`first-party`** from two team contexts, neither of them an engineering organisation |

Two things worth knowing before you quote any of this at somebody. **The weakest-backed section is
the one about how to describe a change**, which is entirely first-party and where a search found no
external work at all. And **the section on instruction files is uniformly tier 4**, which is
awkward, because instruction files are the single most written-about topic in this space and the
measured work on them disagrees with itself.

---

## Layer 1: applies everywhere

### Verifying a claim

- **Do not treat a submission line as a review trail.** "Submitted to venue X" states intent, not
  outcome. Check the venue's accepted list, or a publisher DOI distinct from the preprint's own.
  Applying this check to two papers cited as equally strong revealed one was peer-reviewed with a
  publisher DOI and the other had no venue at all.
- **Do not let a tier-4-or-weaker source retire a practice or remove a control.** It may raise a
  doubt. The burden is asymmetric on purpose: adding a safeguard on weak evidence costs effort,
  removing one costs correctness.
- **Do not confirm a universal claim.** Any assertion containing "zero", "none", "all", "every",
  "never" or "only" is worth exactly as much as the search that would have *falsified* it. Grepping
  for the thing you expect to be absent and finding nothing is weak evidence.
- **Do not report an absence without stating what you searched for and confirming that is the shape
  this system produces.** A search for one platform's convention, run against a system using a
  different platform's convention, completes cleanly and returns zero. That is indistinguishable
  from a true absence and carries the same confidence. It has happened here: 36 real records were
  reported as none because the query used the wrong vendor's wording.
- **Do not treat a failed verification as a negative finding.** "Could not confirm" and "confirmed
  absent" are different results and only the second is evidence. A pass that failed to reach a
  source has produced no information about that source, and reporting it as doubt is worse than
  reporting nothing, because it arrives looking like diligence. Say which of the two you have.
- **Do not trust your own paraphrase of a number.** Tiering a claim protects where it came from and
  does nothing for how you restated it. Quote the source's own units and category before publishing
  a figure: the failure mode is silently widening a narrow finding or narrowing a broad one, and it
  survives every check that looks only at provenance.
- **Do not report from a filtered read without naming what the filter cannot rule out.** A keyword
  search returning many matches is indistinguishable from a complete read, because whatever it
  dropped generates no signal.
- **Do not count two runs of the same reasoning as two kinds of evidence.** Independent *in kind*
  means a test plus a protocol capture, or a query result plus the source it was ported from.
- **Do not verify that an artifact exists when you can run it.** "Installed" is not "working". A
  hook can be configured for a binary absent from `PATH`; a script can be present but invoked under
  an interpreter name that does not resolve; a tool can be on `PATH` and still report zero activity.
  All three occurred in one week. Run the thing.
- **Do not treat rediscovery as replication.** Two research passes finding the same paper confirms
  the paper exists. It does not corroborate its finding or resolve its disagreement with another.
- **Do not conclude anything from a single agent run, and do not believe temperature zero makes it
  deterministic.** Two independent groups measured this and agree. One found roughly 9% of
  per-instance outcomes flipping between byte-identical runs at temperature 0. The other, across
  60,000 trajectories and three models, found pass@1 varying 2.2 to 6.0 percentage points run to run,
  and a standard deviation above 1.5 percentage points **even at temperature 0**. **Tier 1**, the
  only replicated finding in this collection, and it discounts every other single-run number here
  including its own. If you are comparing two configurations on your repository, run each of them
  five to ten times or accept that you are reading noise.

### Instruction files

- **Do not put in an auto-loaded file what a linter, formatter or analyzer can enforce.** Never send
  a model to do a linter's job: slower, costlier, inconsistent. Move the rule to config and delete
  the prose. One repository moved five style rules into analyzer severities set to `error`; enabling
  them immediately failed the build on five violations, one of which a careful manual sweep had
  missed.
- **Do not include a repository or directory overview.** Measured as providing no benefit for file
  discovery, despite being recommended by model vendors.
- **Do not let a model write your instruction file over the top of existing documentation.** The one
  study that separated authorship found generated context files *hurt* task success by 0.5 and 2
  percentage points in two settings, while developer-written ones helped slightly. **The scoping
  matters and was missing until 2026-09-04**: in the same study, when existing documentation was
  *removed*, generated context files **improved** performance by about 2.7 percentage points and
  could beat developer-written docs. So the finding is not "generated context is bad", it is
  **"generated context is redundant where documentation already exists, and useful where none
  does"**. Tier 4. The size of the human-written gain is **contested between two verification
  passes**; see `EVIDENCE.md`.
- **Do not chase a line-count target.** Published advice ranges from 20 lines to 200 and none of
  those numbers is measured. What is measured: rule polarity, authorship, and repository overviews
  not helping. Size for cost, and cut when you notice a rule being skipped.
- **Do not write a rule you cannot cite an incident for.** Rules derived from a real failure stick.
  General good practice belongs in a linter or nowhere.
- **Do not leave a superseded rule in place with an annotation.** Delete it. A file that states a
  rule and then contradicts itself is worse than one that omits the rule.

### Working with agents

- **Do not let an agent review its own work.** The implementing context cannot catch an assumption
  it never questioned. Review from a fresh context, and give the reviewer the diff and the
  requirement, not the implementer's reasoning.
- **Do not let an agent be the only reviewer.** Two peer-reviewed mining studies of agent-authored
  pull requests: most receive **no review at all**, and where a code-review agent was the only
  reviewer, those changes **merged at 45.20% against 68.37% for human-reviewed ones**, with 12 of 13
  agents averaging a signal-to-noise ratio below 60%. The authors' own conclusion is that review
  agents should augment rather than replace human reviewers. **Tier 2.** This is the external
  evidence behind Layer 3's nominal-reviewer rule, which was previously first-party from one
  repository.
- **Do not stop at isolating the reviewer. Instruct it to disagree.** A fresh context is necessary
  and not sufficient: a reviewer agent given a change without an explicit disagreement instruction
  scored the worst measured result in its comparison by agreeing with the implementer, and the same
  setup with that instruction added scored the best. Tier 2, and it is the one rule here whose
  omission actively inverts the outcome rather than merely wasting the pass.
- **Do not add reviewer agents to buy confidence.** Three outperformed five in the same study. Past
  a small number the additional reviewers converge rather than diverge, so they cost tokens and
  return agreement.
- **Do not prescribe a procedure where you can supply context.** Instructing an agent to follow
  test-driven development without a test-impact map measurably *increased* regressions; supplying
  the map cut them by 70%. Context beats procedure, and this generalises past testing.
- **Do not claim a practice reduces defects without tier-1-or-2 evidence.** Specification writing,
  test-first ordering and instruction files are all worth doing for other reasons. None has that
  evidence. Justify them as scoping, accountability and cost tools, and say so plainly.
- **Do not touch adjacent code.** Change the lines the task requires. Leave pre-existing dead code
  alone. A repository-wide cleanup is its own change with its own review, because a large incidental
  diff in a correctness-critical file is where a hard-won invariant gets deleted by accident.
- **Do not delegate work whose intermediate results you need.** Delegate work whose *process* is
  large and whose *output* is small: research sweeps, verification passes, mechanical fixes. That is
  a context win, not only a cost win.
- **Do not run a worker agent in your own working tree.** Without isolation it moves `HEAD`,
  switches branches and edits files underneath you.
- **Do not stack many workers on one orchestrator.** The orchestrator accumulates every worker's
  output, and degradation with input length is measured and non-uniform.

### Measuring whether any of this works

This collection says repeatedly that a practice has no measured defect-reduction evidence. That is
an honest position and it is also an unsatisfying one, so here is how to generate the evidence for
your own repository. **Mostly tier 7**, because the working knowledge on this lives in vendor and
practitioner writing rather than in the literature, with two exceptions noted.

**Nobody has measured this properly, and that is a finding rather than an excuse.** A deliberate
search for a controlled comparison of defect rates with and without AI assistance found nothing
meeting all three of random assignment, a real defect outcome rather than a proxy, and adequate
power. The near misses each fail a different axis: a randomised trial measuring test-pass rate
instead of defects, a larger study measuring real bugs but not randomised and conflating access with
use, another randomised trial measuring only time on task. `EVIDENCE.md` records the search terms so
the next person can do better rather than repeat it.

- **Do not compare two configurations on one run each.** The single most important rule here, and the
  only tier-1 finding in the collection: outcomes flip between byte-identical runs, and temperature
  zero does not fix it. **Run each candidate five to ten times per task.**
- **Do not report pass@k when you care about reliability.** pass@k, meaning at least one success in
  k attempts, flatters an agent. What production needs is closer to pass^k, meaning it works every
  time. **Measured across 500 tasks and six configurations: the gap between pass@1 and pass@5 reaches
  24.9 percentage points, and between pass@1 and pass^5 reaches 18.9 percentage points.** That is the
  distance between the number you would report and the number you could rely on.
- **Do not build your task set out of a public benchmark's tasks.** Build a small expert-labelled
  set, ten to twenty real tasks from your own repository, and decide up front what counts as
  success, as an acceptable alternative, and as a meaningful failure. Those three categories are the
  harness. Benchmark critiques exist in reviewed venues, and one major vendor has stopped using the
  best-known coding benchmark as a frontier evaluation, which tells you how much a score on it says
  about your codebase.
- **Do not only test the happy path.** Include tool failure, context overflow, and the fiftieth tool
  call in a long run. A harness of clean tasks measures something, and it is not the thing that
  breaks.
- **Do not grade only the final answer where many paths are valid.** Capture the trajectory. A right
  answer reached by luck and a right answer reached by a sound route are the same row in your
  results table and very different things in your repository.
- **Do not use a model as a judge without knowing its bias.** Measured: LLM judges at a true
  positive rate above 96% against a true negative rate below 25% on validity judgments, which is a
  grader that mostly approves. Across 13 studies in one domain, judge-to-expert concordance ranged
  0.66 to 0.96 with a median of 0.83, worst on fine-grained tasks. A rubric-anchored ensemble of
  three reached 0.90. So anchor the rubric, use more than one judge, and never let a model judge be
  the whole gate on a fine-grained property.

### Commands, diffs and change descriptions

- **Do not filter the output of a one-shot, state-changing command.** Compress build and test output
  freely; never compress or truncate a push, because a hidden ref update cannot be re-read.
- **Do not describe only your own commits.** Describe the whole diff against the default branch,
  including work you did not write. A description accurate about its author and false about the
  change as a whole is worse than a missing one: it authorises a merge that would otherwise have
  been questioned.
- **Do not state a risk as "low".** Name what could break and what would surface it. If nothing
  would surface it, that is the most useful sentence in the description.
- **Do not omit negative evidence.** "No review passes run: documentation-only diff" is complete.
  Silence is indistinguishable from having forgotten.
- **Do not stack a branch on an unmerged parent** unless you describe the whole stack and say why it
  was not split. Merge parents first, then rebase.
- **Do not cross-reference a numbered list item.** Numbers shift when the list is pruned, and the
  reference then points at something unrelated. Name the item.

---

## Layer 2: solo repositories

Apply only when the profile says there is no second human reviewer. **These are wrong on a team.**

- The change description **is** the review record, because nobody else will read the diff. On a team
  a human reads the diff, so the description is a summary and not the record.
- Self-merging is acceptable only if the description states which review passes ran and what they
  found. That record is the compensating control for the missing reviewer.
- A repository-wide sweep can be scheduled at your own convenience, because no one else's branch is
  in flight.

---

## Layer 3: team repositories

Grounded in two first-party team contexts: a two-person repository with 51 changes of history, and a
six-person student project with 254 commits, a full chat archive, and two independent audits of the
repository it produced. Where a claim is first-party it says so; the one external claim here is
tier 2.

**The two teams differ on review, which is the useful part.** One self-merged every change. The other
split merges roughly evenly between the author and another member. But in both cases the only
available signal is **who clicked merge, not who reviewed** - the second repository's audit says so
explicitly, and neither had retrievable review comments. So do not read a mixed merge pattern as
evidence of review. It is evidence of a mixed merge pattern.

### Disclosure

- **Do not leave AI authorship undeclared because you modified the output heavily.** In a study of
  613 mined code snippets and 111 practitioners, 76.6% declare AI-generated code always or
  sometimes, and the most common reason given for *not* declaring is that extensive modification
  made the code feel distinct. That is exactly the case where a reviewer most needs to know, because
  heavy modification is where an agent's assumption gets half-corrected. **Tier 2**, and the
  best-evidenced *practice* claim here, though the replicated nondeterminism finding above now
  outranks it on the scale.
- **Do not invent your own disclosure convention.** One is settling in the open-source world and
  copying it is free. Major projects including the Linux kernel, the Apache Software Foundation,
  Fedora, LLVM and QEMU adopted formal trailer-based disclosure during 2026, using an
  `Assisted-by:` trailer and **explicitly barring AI from `Signed-off-by`**, which keeps
  human accountability and machine assistance in separate fields. Follow the convention your
  ecosystem is converging on rather than a scheme local to your repository.
- **Do not assume the project has no position.** A survey of 1,000 repositories found 118 carrying an
  explicit AI policy, and of those, **78% permit AI contributions, 51% require disclosure and 74%
  require a human in the loop**. Tier 2, accepted at a reviewed venue. So the common case is still no
  stated policy, and where one exists it usually permits the work and requires you to say so. Check
  before contributing rather than after.

### Review that exists on paper only

**First-party, and the most consequential finding in this layer.** One two-person repository
self-merged **47 of 47** changes, each by its own author, with zero human reviews across 51 - while
carrying a change template whose reviewer checklist names both contributors, and a contributing
document binding both to rules only one of them has ever edited.

- **Do not record a reviewer you do not have.** A declared-but-absent reviewer is worse than an
  acknowledged absence, because the solo compensating control in Layer 2 never gets applied: nobody
  writes the review-passes record, on the grounds that a reviewer will catch it.
- **Do not treat a checklist as a control.** An undocumented environment variable shipped through the
  exact checklist item written to catch it. A checklist nobody fills in is a record of intent.
- **Do not record an agent as the reviewer either.** Set `reviewers: agent` when a review agent
  reviews and no human reads the diff, and keep applying the Layer 2 solo discipline, because an
  agent's comment thread is not a review record. Neither `nominal` nor `agent` discharges the
  obligation to write down what was checked; only a human who actually read the diff does.
- Set `reviewers: nominal` in the profile when this is the situation. It is a real state with its own
  failure mode, not a rounding error toward `none` or `one`.

### Process that exists only as an agreement

**First-party.** A six-person team named unequal task distribution in two retrospectives a month
apart, with nothing between them but a restated intention. Then, days before final submission, the
retrospective itself was skipped and its content invented for the report.

- **Do not rely on a recurring meeting to enforce anything.** The mechanism meant to catch the
  problem was the first thing dropped once deadline pressure arrived. **A process that exists only
  as a verbal agreement in a recurring meeting is not a control.**
- **Do not let a decision needing absent members' approval proceed on the assumption of it.** One
  sprint-length change was made and then awaited after-the-fact ratification, which is a decision
  with no owner.
- **Do not schedule in free text.** Meeting times posted as inconsistently formatted chat messages,
  with no timezone and no confirmations, produced a real missed meeting from format ambiguity alone.

### Decisions defending themselves

**First-party.** External reviewers advised against an architecture; the team continued because
reversing was expensive, and recorded that reasoning in the meeting log. Nobody missed the feedback.

- **Do not write a decision without its reconsider-if trigger.** See `DOCS.md`. A trigger written
  when the decision is cheap costs one line; reconsidering after months costs the argument.

### Tests that certify a build nobody ran

**First-party, and the only pattern in this skill observed independently in three separate
repositories.** A team repository had a broken endpoint discovered late despite green tests, because
the tests mocked the API and never exercised the real stack. A second has no test project at all for
its orchestration layer. A third documents a negative benchmark result rather than a passing one.

- **Do not accept a green suite as evidence the system runs.** Name what the tests mock, and keep at
  least one check that exercises the assembled thing. This is not "write more tests"; more mocked
  tests make the problem worse by raising confidence without raising coverage of reality.

### Ownership and onboarding

- **Do not assume the shared instruction file has an owner.** Decide who may add rules and where
  disagreements are settled, before it becomes a battleground. Observed: eight commits to one such
  file, all by the same person, in a repository whose contributing document binds two.
- **Do not let one person's conventions become implicit house rules.** Onboarding someone onto a
  workflow they did not design is a documentation task, not an announcement.
- **Do not skip the diff because an agent wrote a good description.** The description was written to
  persuade you; the diff was not.
- **Do not add a platform without retiring one.** One team ran nine tools at once and consolidated
  only after external feedback, and then only by one.
- **Do not let one person's snapshot become shared state by default.** A readme progress section
  written by one member in one week was never revisited by any of the other five, and silently
  described a finished pipeline as in progress through 200 further commits. Solo, a stale snapshot
  misleads its author. With six people it misleads five who never knew it was one person's note.
- **Do not leave git identity to per-machine config.** Three of six contributors each committed under
  two distinct name and email pairs. Harmless alone; on a team it fragments authorship badly enough
  that reasoning about who owns what stops working.
- **Do not let a convention exist only as a pattern in branch names.** One team's branch scheme was
  real, followed by most, and written nowhere - so the members who omitted it were not breaking a
  rule, because there wasn't one.
- **Do not keep a requirements document with no traceability to what shipped.** One listed user
  authentication as a requirement; the codebase has no authentication of any kind, and nothing
  anywhere records that the requirement was dropped or why. A requirements list that outlives its
  requirements is worse than none, because it reads as a commitment.

---

## When a rule here conflicts with published advice

Check the tier before changing the rule. Vendor documentation and independently measured outcomes
are not guaranteed to agree, and where they diverge the independent measurement carries more weight
for a production workflow. One documented instance: repository overviews are recommended by model
vendors and were measured as not helping. Another: practitioner guides advise writing constraints as
positive directives, and the largest study of real rule files measured the opposite.

`EVIDENCE.md` carries the tier scale, every source, and what remains unverified.

---

## Keeping this current

A collection that grades other people's evidence and then lets its own go stale has failed on its
own terms. So the maintenance schedule is part of the artifact rather than an afterthought.

**Every quarter, and the whole point is that these are different jobs:**

- **Recheck the administrative facts as a unit.** `EVIDENCE.md` keeps adoption figures, governance
  status and supported-tool lists in one section for exactly this reason. They rot fastest and
  matter least individually, which is why they get checked together and cheaply.
- **Re-search the open gaps.** Not the sources, the gaps. One gap in this collection stood as
  sourceless while an accepted paper answering it already existed, missed by four separate research
  passes. **The gap list records what searching failed to find, not what does not exist**, and it
  should be read that way every time.
- **Recheck the tier of anything at tier 3.** Tier 3 means a decision was pending. Pending decisions
  resolve, in both directions, and nobody sends you a notification.

**The cadence is now enforced rather than promised.** `build.py` reads the recheck date from this
file's header, **warns at 90 days and fails the build at 180**. `REFRESH.md` is the pass itself: what
to recheck, in what order, and the rules that do not relax because it is routine. Before those two
existed this section was a promise, and a collection that grades other people's evidence while
letting its own cadence run on good intentions has failed on its own terms.

**On every edit, not quarterly:**

- **Trace any number you add back to the source's own words.** Separate pass from tiering it. Three
  of this document's own recorded errors were paraphrase drift with correct provenance, so the
  citation check does not catch them.
- **Bump the version and the recheck date** in the header. A reader's only defence against a stale
  document is knowing how stale it is.

**On the security file, faster than quarterly.** `SECURITY.md` cites CVEs, an OWASP ranking and
active supply-chain campaigns. Those move on a different clock from the research, and a security
document that is a year behind is worse than absent because it reads as current.

**When consuming this in a repository**, pin the version you read rather than tracking the tip
silently, and record which version a convention came from. A convention whose source has since been
retracted is otherwise indistinguishable from one that still holds.
