# dev-conventions

Conventions for AI-assisted software development, where **every claim carries the strength of the
evidence behind it**, and the guidance **adapts to your repository** instead of prescribing one shape
for all of them.

**Version 0.15.0. External claims last rechecked 2026-09-08.**

---

## Why this exists

There is no shortage of advice about working with coding agents. Almost none of it says how strongly
anything is supported, so a measured finding and somebody's blog post arrive looking identical. That
is how "keep your instruction file under 30 lines" became a widely repeated fact despite nobody ever
having measured it.

So this collection does two things differently:

**It grades every claim by review trail.** An eight-tier scale, ordered by whether anyone reviewed
the work rather than by whether it produced numbers. A seven-author study with 5,000 runs and no
venue is tier 4. A peer-reviewed paper confirmed against a publisher record is tier 2.

**A tier is not a correctness score.** It records how much scrutiny a claim has survived, which is
correlated with being right and is not the same thing: a tier-4 preprint can be correct and a tier-2
paper can be wrong. Use a tier to decide how hard to push back, never to decide what is true. The
numbering invites the other reading, so this is said again at the head of the scale itself.

There is a standing rule that a weak source may raise a doubt but may not retire a safeguard. Where
sources genuinely disagree the disagreement is left standing rather than averaged into a consensus
that does not exist, **and each one carries a stated default** for what to do meanwhile, chosen for
cheapest to reverse and labelled judgment rather than evidence.

**It reads a profile and adapts.** Repositories legitimately differ. Some carry a changelog and a
roadmap; some deliberately carry neither; a six-person student project needs different answers from
a solo production service. Each repository declares a small profile and the guidance becomes
conditional on it, so no rule assumes a file, a reviewer or a team that is not there.

## What this is not

Not a guide to writing an instruction file or a skill. All three major model vendors publish their
own first-party authoring guidance and the community collections around it run to tens of thousands
of stars. Read those first.

**And be clear about the overlap, because an earlier version of this sentence understated it.** The
vendors now publish most of the workflow advice too, better maintained than this can be: fresh-context
review, subagent delegation for context economy, worktree isolation, context degradation, and
converting a prose rule into a hook all appear in first-party guidance as of 2026-09-08. **What
remains here is the strength marking, the profile conditioning, the disagreements, and the things a
vendor has no incentive to say.** That is a narrower claim than "not competing" and it is the true
one.

Not a compliance framework, not audited by anyone, and not a set of practices to adopt wholesale.

## Read this before trusting any of it

- **A large share rests on first-party observation** of four repositories, all small, one or two
  people each. That is a genuine confound and it is the collection's central weakness: **a pattern
  across all four may be a pattern in how one person works.** Every first-party claim is labelled as
  such, which is a warning rather than a boast. Nothing here is observed at organisational scale, so
  read every one of these as a hypothesis about your repository rather than a finding about it.
- **Absence of a recorded signal is not absence of the practice.** Most first-party findings are read
  out of git history, which proves only what was written down. A team that reviews by screen-share
  leaves the same trace as a team that does not review. Read every claim about what a repository
  "did not do" as what it did not **record**.
- **Nothing here has been measured against a control**, and until 2026-09-09 this bullet added "and
  neither has anything else". **That was false and it was the most self-flattering sentence in the
  collection.** `martinholovsky/SOTA-skills` runs guided-against-unguided arms across multiple models
  with pre-registered predictions, publishes nine null results, and has retracted a lift that did not
  reproduce. Verified by cloning it. See error 27.

  What survives, narrowly: a deliberate search for a controlled comparison of **defect rates with and
  without AI assistance** found no study meeting all of random assignment, a real defect outcome and
  adequate power. That gap is still open. The search terms are recorded so you can do better rather
  than repeat it.
- **The documentation rot taxonomy has a known bias and one external contradiction.** It ranks by
  *recorded* corrections, so it under-weights repositories that never audit their documents, which
  are the ones whose documentation is worst. And a study of 2,303 agent context files across 1,925
  repositories found those behave as living configuration rather than decaying documents, which
  contradicts part of the taxonomy directly. Both are stated where the taxonomy appears.
- **Only one finding here is replicated**, and it undercuts the rest: **four independent groups**
  measured agent evaluation flipping outcomes between identical runs, with temperature zero providing
  no protection, and two of them name the causes. Every single-run number in this collection inherits
  that caveat, including the ones these four papers report.
- **The collection has been wrong** and keeps a numbered list of its own errors, twenty-seven of
  them, including a security figure it inflated nineteenfold, a source it cited as saying the
  opposite of what it found, and **two figures that are not in the paper they were attributed to,
  published under a claim that the paper had been read in full**. That list is not humility
  furniture. It is the argument for the scale, and it is the section to read first if you want to
  know how much to trust the rest.
- **It has been checked from outside seven times**, between 2026-09-03 and 2026-09-09, and every one
  of them found something. A fabricated statistic. Two figures wrong. Four items where two
  independent passes disagreed. A shipped template that misstated its own source. Most recently, and
  worst: **three corrections that never reached the files an agent actually loads**, one of them
  false about a named third party, and **two figures that appear nowhere in the paper they were
  attributed to, published under the sentence "both full texts were read"**. All recorded, with what
  each check cost, at the end of `EVIDENCE.md`. **Please be the seventh**: the rate at which checking
  finds things has not slowed.

## What is in here, and it is two artifacts now

**Split on 2026-09-08.** The rules and the evidence behind them were one thing and were fighting: the
rules want to be small because loading them costs tokens on every session, and the evidence wants to
be complete because that is its whole value. Bundled, every adoption paid for the apparatus and every
reader of the apparatus was handed a skill they did not want.

### Artifact A: the skill, which an agent loads

| File | What it is | Load it when |
|---|---|---|
| `ADOPTION.md` | A two-phase prompt that adopts this in one repository | **Start here.** Paste it into an agent session rooted in that repo |
| `SETUP.md` | Deciding your tool categories, installs and delegation policy **once per machine**, not per repository | Before your second adoption. It is what stops you re-deciding |
| `SKILL.md` | The rules, in profile-conditional layers | Always the entry point for an agent |
| `PROFILE.md` | The profile schema, its defaults, and a cold-start path | Writing or reading a repository profile |
| `SOLO.md` / `TEAM.md` | The two mutually exclusive rule sets | Load exactly one, whichever the profile's `team` field selects |
| `SECURITY.md` | Agentic security obligations, grounded in 2026 incidents | Touching auth, secrets, CI, untrusted input, or installing a third-party skill or MCP server |
| `SPEC.md` | Specifying a change before it is built | About to start or delegate something large enough that getting it wrong costs a rebuild |
| `HANDOFF.md` | Closing a session into a record the next one can act on | Ending a session whose decisions or half-finished work outlive it |
| `MEASURING.md` | How to actually test whether a practice helps | Comparing two configurations, or deciding whether a practice earns its cost |
| `OPERATING.md` | Human-facing: delegation, model tiering, prompting habits | Deciding how to drive the system, not what it should do |
| `REFRESH.md` | The quarterly re-research pass | The build warns the recheck date is over ninety days old |
| `templates/`, `examples/` | Drop-in files and three filled profiles | Setting up a new repository |

### Artifact B: the evidence, which a human reads

`evidence/` builds into a single document, roughly 27,000 words, and **it is not part of the skill.**
It holds the tier scale, every source, the disagreements left standing, the open gaps, the numbered
errors, the research-community conventions and the vocabulary.

**The boundary is apparatus against rules, and 0.14.0 drew it on length instead.** Four rule files,
`DOCS.md`, `WORKFLOW.md`, `TOOLING.md` and `OBSERVABILITY.md`, ended up outside the deliverable and
took 47 prohibitions with them. They are back in the skill. Error 26.

Read it when a rule is challenged, when you need a claim's provenance, or when you want to know how
often this has been wrong. **Do not load it in a session.** Nothing in `ADOPTION.md` requires it.

**`CHANGELOG.md` is in the repository and not in the distributable.** It records what changed
between versions and what was checked and did not change, which matters when you are deciding whether
to pin or upgrade, and it is not something an agent should be loading. Read it on the code host.

## Install

**Claude Code, personal.** Clone or copy the directory to `~/.claude/skills/dev-conventions/`.

**Claude Code, one project.** Same, at `.claude/skills/dev-conventions/`.

**Claude Desktop or Claude on the web.** Zip the directory so the archive contains
`dev-conventions/SKILL.md` as a nested folder rather than files at the root, then upload it under
Customize, Skills. It registers against your account, so it is then available on any device.
Requires a paid plan with code execution enabled.

**Other tools.** The skill format is supported natively well beyond one vendor. Check your tool's
documentation for where it expects skills to live; the files themselves need no changes.

**One hard rule, whichever way you install it: never `@`-import this from an instruction file.** It
is a skill so that it loads on demand. Importing it turns a reference document into per-turn context,
which is precisely the cost it exists to prevent.

## Using it

**The fastest path is `ADOPTION.md`.** It is a prompt you paste into an agent session rooted in the
repository you want to adopt this in. Two phases with a deliberate stop between them: derive the
profile, get it approved, then apply the conventions in the order that prevents the most damage
first. Run it once per repository.

If you would rather do it by hand: write a profile first. `PROFILE.md` has the schema, a seven-step
derivation procedure with the actual commands, and `examples/` has three filled profiles for
different repository shapes. Several fields are answerable only by running something rather than by
copying a template, and the procedure says which.

If no profile exists the skill infers what it can and states its inferences. That is a fallback, not
the intended path.

## Contributing, and what would actually help

The most useful contribution is **a counter-example**: a repository where one of these rules is
wrong, with the mechanism. The first-party evidence base is four small repositories, one or two
people each, all observed by one person. That is the collection's central weakness and it is stated
as such throughout.

**Specifically wanted: a repository with a retrievable review trail.** Every team context inventoried
so far turned out to record who merged a change and nothing about who reviewed it. One of them had a
pull-request mechanism and it still recorded no reviewer. If your repository actually has review comments, approval trailers, or a review
history an outsider could reconstruct, that is the counter-example most likely to change what this
collection says.

The second most useful is **a source**. If a claim here is tiered too high, or an open gap has an
answer, that is worth more than new practices. One gap in this collection stood as sourceless while
an accepted paper answering it already existed.

New practices without evidence are the least useful thing to add, and they are what the tier scale
exists to hold at arm's length.

## Licence

**Dual, and which one applies depends on the file.**

- **`templates/`, `examples/`, `build.py`, `.claude-plugin/`: MIT.** Copy a template into your
  repository and no obligation travels with it. That is what a template is for.
- **The prose: CC BY 4.0.** Share and adapt it, including commercially, with credit to the collection
  **and the version**. The version matters because a claim corrected between versions is otherwise
  indistinguishable from one that still holds, which is the same reason `CHANGELOG.md` exists.

MIT permits use without attribution, which is the wrong default for a collection whose whole argument
is that claims should be traceable to who made them and when. `LICENSE` and `LICENSE-DOCS` carry the
file lists.

`LOCAL.md` where present is under neither. It holds machine-specific notes and is excluded from every
distribution.
