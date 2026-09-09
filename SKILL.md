---
name: dev-conventions
description: Evidence-graded conventions for AI-assisted development, where every claim is tiered by how much review it has survived and rules adapt to a per-repository profile. Covers what belongs in an instruction file versus a linter, how many reviewers agent-authored code needs and whether an agent may review its own diff, disclosing AI authorship in a commit trailer, branch and merge-gate conventions, writing commit and PR descriptions for a partly agent-written diff, documentation rot, agentic security obligations, specifying a change before delegating it, closing a session into a handoff record, and how to measure whether any of it works. Use when setting up or auditing a repository's conventions, reviewing or merging agent-authored code, deciding review or disclosure policy, writing a commit or PR description, delegating to a subagent, or checking whether a claimed best practice is actually supported by evidence.
---

# Development conventions, evidence-graded

**Version 0.14.1. External claims last rechecked 2026-09-08.**

## What this is and is not

**This is the rules half.** The evidence behind every claim, the sources, the disagreements, the open
gaps and this collection's own numbered errors are a separate document, `EVIDENCE.md`, built
as its own artifact. They were one thing until 2026-09-08. Splitting them is why this file is a third
of its former size: an agent applying a rule does not need the apparatus, and a human evaluating the
claims should not have to install a skill to read it.

**Not a guide to writing an instruction file or a skill, and not a competitor to your vendor's
workflow advice.** As of 2026-09-08 first-party guidance also covers fresh-context review, subagent
delegation, worktree isolation, context degradation and converting a prose rule into a hook. Read
your harness's page for those. **What is here is what a vendor does not say, will not say, or says
without evidence:** the strength marking, the profile conditioning, the disagreements left standing,
and the rules whose evidence points against a vendor's incentive.

**Every claim carries a tier.** Nothing here is asserted flat. Where sources disagree the
disagreement is left standing with a stated default, and the things nobody has measured are named as
such.

**Read the version line and distrust this file if it is old.** Vendor coverage, adoption figures and
tool lists go stale in months. A stale dated claim counts as a defect here, not as background.

Four warnings that bound how much you should trust it:

- **A large share rests on first-party observation** of four small repositories, one or two people
  each, all observed by one person. **A pattern across all four may be a pattern in how one person
  works.**
- **Absence of a recorded signal is not absence of the practice.** Most first-party findings are read
  out of git history, which proves only what was written down.
- **Nothing here has been measured against a control.** Where a number appears it is cited with a
  tier, or it is a direct measurement of something mechanical like token counts.
- **One finding is replicated and it undercuts the rest.** Four independent groups measured agent
  evaluation flipping outcomes between identical runs, with temperature zero providing no protection.
  Every single-run number here inherits that.

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
- **Do not re-decide what `setup.yml` already decided.** If the profile names a `setup` file, read
  it: it carries the resolved tool categories, what is installed and when it was vetted, and the
  delegation policy. Re-deciding per repository is the friction this collection exists to remove.
- **Do not proceed silently when no profile exists.** State the inferences you are making, then
  offer to write one.

## Companion files

| File | Load it when |
|---|---|
| `PROFILE.md` | Writing or reading a repo profile, including the resolved-stack block |
| `SECURITY.md` | Touching auth, secrets, CI, untrusted input, or installing a skill or MCP server |
| `SPEC.md` | About to build or delegate something large enough that getting it wrong costs a rebuild |
| `HANDOFF.md` | Closing a session whose decisions, dead ends or half-finished work outlive it |
| `OPERATING.md` | Human-facing: prompting, delegation, model and vendor selection |
| `SETUP.md` | Once, per machine rather than per repository: resolving tool categories, recording what you installed and when you vetted it, and writing the delegation policy down |
| `SOLO.md` / `TEAM.md` | Load exactly one, whichever the profile's `team` field selects |
| `MEASURING.md` | About to compare two configurations, models or prompts, or decide whether a practice earns its cost |
| `REFRESH.md` | The build warns the recheck date is over ninety days old |
| `DOCS.md` | Setting up, auditing or pruning a repository's documentation |
| `WORKFLOW.md` | Setting up branching, merging, pull request or pre-merge gate conventions |
| `TOOLING.md` | Choosing what to put around an agent, or checking for a missing category |
| `OBSERVABILITY.md` | Deciding what to record about agent work, or explaining its cost |

**`EVIDENCE.md` is not in this list and that is deliberate.** It is the apparatus: the tier scale,
every source, the disagreements, the open gaps and this collection's own numbered errors. It builds
as a separate document of roughly 27,000 words, alongside `RESEARCH.md` and `VOCABULARY.md`, and **no
agent should load it**. Open it when a rule here is challenged or you need a claim's provenance.

**The boundary is apparatus against rules, not long against short.** At 0.14.0 it was drawn on length
and four rule files ended up outside the deliverable, taking 47 prohibitions and 8,523 words with
them. Error 26.

## Where each layer's rules come from

Stated once rather than tagged on every line. `EVIDENCE.md` carries the sources.

| Section | Provenance |
|---|---|
| Verifying a claim | **Mixed.** Run-to-run nondeterminism is **tier 1**, the only multiply replicated finding here, four independent groups. The rest is `first-party` method, demonstrated on external papers: the habits are this collection's own, what they were tested on is public |
| Instruction files | **Mixed, all external, all weak.** Rule polarity, authorship and repository overviews are each tier 4. Analyzer-beats-prose and the incident rule are `first-party` |
| Working with agents | **Mixed.** Agent-only review is tier 2; reviewer disagreement was tier 2 and is **tier 4 since 2026-09-07**, when its venue turned out to be author-claimed; context-beats-procedure is tier 3; multi-agent degradation and context length are tier 5. Worktree collision and the delegation heuristic are `first-party` |
| Measuring whether any of this works | **Mostly tier 7**, vendor and practitioner. Nondeterminism is tier 1, judge bias is tier 4. The absence of any controlled defect study is a recorded search result, not an assumption |
| `OBSERVABILITY.md` | **Mixed.** The content-off-by-default rule is a standards-body default, the strongest thing in that file. Mix shift and heartbeat monitoring are established practice from outside this field. Alert fatigue transfers by analogy and says so. Cost figures are vendor-adjacent. Two failure modes are `first-party` |
| `VOCABULARY.md` | **Weaker sourcing than the rest, and it says so at the top.** Verdicts are this collection's judgement; the figures come from one research pass and were not each re-verified to primary sources |
| `WORKFLOW.md` | **Mostly not measured, and the file leads with that.** One 2006 industrial case study behind PR size, correlational survey data behind branching, nothing at all behind merge strategy. The AI-specific layer is vendor and self-reported |
| `TOOLING.md` | **A map, not a ranking.** Categories are durable; the named products are dated illustrations. No independent head-to-head of these tools exists |
| `RESEARCH.md` | **Convergence evidence rather than measurement.** Where a research community independently requires what engineering practice recommends. Also records one open problem nobody has solved |
| Commands, diffs and change descriptions | **Entirely `first-party`.** Every one is a specific incident. No external source was found for any of it |
| Layer 2, solo | **Entirely `first-party`** |
| Layer 3, team | Disclosure is tier 2 and agent-only review is tier 2, both confirmed against publisher records; policy prevalence dropped to tier 4 on 2026-09-07 when its venue could not be confirmed. The rest is **`first-party`** from two team contexts, neither of them an engineering organisation |

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
  deterministic.** **Four independent groups** measured this and agree. One found roughly 9% of
  per-instance outcomes flipping between byte-identical runs at temperature 0. A second, across
  60,000 trajectories and three models, found pass@1 varying 2.2 to 6.0 percentage points run to run,
  and a standard deviation above 1.5 percentage points **even at temperature 0**. Two more name the
  causes rather than only the effect: floating-point non-associativity, batch-size variation under
  concurrent server load, and non-deterministic kernel scheduling. One of them also reports that
  reasoning models **expose no user-configurable temperature at all**. **Tier 1**, the only
  multiply replicated finding in this collection, and it discounts every other single-run number here
  including its own. If you are comparing two configurations on your repository, run each of them
  five to ten times or accept that you are reading noise.

### Instruction files

- **Do not put in an auto-loaded file what a linter, formatter or analyzer can enforce.** Never send
  a model to do a linter's job: slower, costlier, inconsistent. Move the rule to config and delete
  the prose. One repository moved five style rules into analyzer severities set to `error`; enabling
  them immediately failed the build on five violations, one of which a careful manual sweep had
  missed.
- **Do not include a repository or directory overview.** Measured as providing no benefit for file
  discovery. **The vendors now agree**: Anthropic's current best-practices page lists "File-by-file
  descriptions of the codebase" and "Anything Claude can figure out by reading code" in its exclude
  column, read 2026-09-08. Until that date this rule said "despite being recommended by model
  vendors", which had stopped being true. See error 25.
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

**Six rules that used to be here now live in first-party vendor guidance**, checked 2026-09-08, and
carrying them here meant maintaining and rechecking advice that a vendor ships to every user of the
harness, continuously and for free. They are named rather than deleted silently, because a reader
cannot tell an omission from an oversight:

> Review from a fresh context rather than the implementing one. Use subagents to keep research out of
> your context. Run parallel sessions in isolated git worktrees. Expect performance to degrade as
> context fills. Convert a rule the agent already follows into a hook. Keep the instruction file
> short and prune it.

**Read your harness's own best-practices page for those.** What stays below is what a vendor does not
say, will not say, or says without evidence.

- **Do not let an agent be the only reviewer.** A mining study of agent-authored pull requests found
  that where a code-review agent was the only reviewer, those changes **merged at 45.20% against
  68.37% for human-reviewed ones**, with 12 of 13 agents averaging a signal-to-noise ratio below 60%.
  The authors' own conclusion is that review agents should augment rather than replace human
  reviewers. **Tier 2**, confirmed against a publisher record. No vendor says this, and the incentive
  runs the other way.
- **Do not stop at isolating the reviewer. Instruct it to disagree, and bound what it reports.** A
  reviewer agent given a change without an explicit disagreement instruction scored the worst
  measured result in its comparison by agreeing with the implementer; the same setup with the
  instruction scored the best. **Tier 2**, ICML 2026 DL4C poster.

  **This one has a live first-party caution against it**, and both are true. Anthropic's
  best-practices page warns that "a reviewer prompted to find gaps will usually report some, even
  when the work is sound", leading to over-engineering. The study measures under-reporting; the
  vendor warns about over-reporting. **Do both: tell the reviewer to disagree, and to flag only gaps
  affecting correctness or the stated requirements.** Judgment, not evidence.
- **Do not add reviewer agents to buy confidence.** Three outperformed five in the same study. Past a
  small number the additional reviewers converge rather than diverge, so they cost tokens and return
  agreement.
- **Do not prescribe a procedure where you can supply context.** Instructing an agent to follow
  test-driven development without a test-impact map measurably *increased* regressions; supplying
  the map cut them by 70%. **Tier 3.** Context beats procedure, and this generalises past testing.
- **Do not claim a practice reduces defects without tier-1-or-2 evidence.** Specification writing,
  test-first ordering and instruction files are all worth doing for other reasons. None has that
  evidence. Justify them as scoping, accountability and cost tools, and say so plainly. This is the
  rule the rest of this collection exists to support.
- **Do not touch adjacent code.** Change the lines the task requires. Leave pre-existing dead code
  alone. A repository-wide cleanup is its own change with its own review, because a large incidental
  diff in a correctness-critical file is where a hard-won invariant gets deleted by accident.
  `first-party`, from a specific incident.

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

## Layer 2 and Layer 3: load the one the profile selects

**These are mutually exclusive and neither is loaded by default.**

- **`team: 1` in the profile, load `SOLO.md`.** What replaces a reviewer when there is none, what a
  solo repository records instead of a process, and the failure modes of working alone with an agent.
- **`team: 2` or more, load `TEAM.md`.** Disclosure, review that exists on paper only, process that
  exists only as an agreement, decision records, and ownership.

**Do not load both, and do not apply one to the other's repository.** Until 2026-09-08 both were
inline here, which meant every session in every repository read roughly a hundred lines that applied
to at most half of them.

## When a rule here conflicts with published advice

Check the tier before changing the rule. Vendor documentation and independently measured outcomes
are not guaranteed to agree, and where they diverge the independent measurement carries more weight
for a production workflow.

**One live instance, added 2026-09-08.** Anthropic's best-practices page cautions, verbatim: *"A
reviewer prompted to find gaps will usually report some, even when the work is sound, because that is
what it was asked to do. Chasing every finding leads to over-engineering."* This document says
**instruct the reviewer to disagree**, on a tier-4 source. Both can be true: the vendor is warning
about over-reporting, the study measured under-reporting. **Default: keep the disagreement
instruction and bound it.** Tell the reviewer to disagree, and to flag only gaps affecting
correctness or the stated requirements. Judgment, not evidence, and it is recorded in `EVIDENCE.md`
under disagreements left standing.

**One standing instance:** practitioner guides advise writing constraints as positive directives, and
the largest study of real rule files measured the opposite.

**And one that expired.** This section used to cite repository overviews as a case of vendors
recommending what measurement contradicts. The vendor's published position now agrees with the
measurement. A conflict claim about a third party is a dated claim, and this one went stale in the
agent-facing file while the recheck date read zero days old. Error 25.

`EVIDENCE.md` carries the tier scale, every source, and what remains unverified.

---

## Keeping this current

**The cadence is enforced, not promised.** `build.py` reads the recheck date from this file's header,
warns at 90 days and fails the build at 180. `REFRESH.md` is the pass itself: what to recheck, in
what order, which vendor pages to open by URL, and the rules that do not relax because it is routine.

**On every edit:** trace any number you add back to the source's own words as a pass separate from
tiering it, and bump the version and the recheck date. Three of this collection's recorded errors
were paraphrase drift with correct provenance, so the citation check does not catch them.
