# Contributing to this repository

This repository develops the `dev-conventions` skill: an evidence-graded collection of conventions
for AI-assisted software development. Read this before changing anything in it.

**This file is for whoever is editing the collection, human or agent.** It is not the collection
itself. `SKILL.md` is the collection's entry point and `README.md` is its front page.

**Never `@`-import `SKILL.md` from this file.** The collection is a skill so that it loads on demand,
and importing it here would turn a reference document into per-turn context, which is the exact cost
it exists to prevent. If you need a rule from it, load the skill.

## What this collection is, in one paragraph

Most advice about working with coding agents asserts practices without saying how strongly they are
supported. This collection grades every claim by **review trail**, refuses to let weak evidence
retire a safeguard, leaves genuine disagreements standing with a stated default, and **keeps a
numbered list of its own errors**. That errors list is not humility furniture. It is the single most
credible thing here, and two external reviewers have said so independently. Protect it.

## The target, and the scope it implies

**Read this before proposing work.** It is the author's stated goal, extracted from the full session
transcript and quoted at `.agents/goals.md`. Every session so far has re-derived the goal from the
artifact, and the derivation drifted each time.

### The goal, in the author's own words

> **"SOTA/MOAT that's still the target focus, but I want to reduce the friction. That's the target
> task: friction in always having to research the development conventions and development workflows
> that are the best currently."**

> "what I want to adopt across all of my repositories: the best scientifically proven or
> engineeringly proven or used by all of the developers proven AI accelerated development... all of
> my projects will have quality output quality code but at the same time will be accelerated... with
> as less friction as possible **so I don't have to constantly research this**."

Three ordered outcomes, and the order is load-bearing:

1. **Adopt it in every repository the author works in**, and have it be worth adopting.
2. **Improve the author's own prompting, delegation and workflow habits.**
3. **Publish it, with credit**, and build a reputation and eventually business visibility on it.

Publication is gated on 1, deliberately and from the first message: *"first ofc finishing the testing
run"*. `ROADMAP.md`'s 1.0 gate is the operational form of that gate.

### What is in scope

- Conventions an agent applies per repository, conditional on a profile.
- Workflow: delegation, orchestrator and worker tiering, cross-vendor structure, review discipline.
- The author's own habits, in `OPERATING.md`, which is the human-facing half.
- **Functional categories** of tooling, and what to establish before granting a tool access.
- The evidence apparatus, because it is the only thing distinguishing this from an opinion list.

### What is out of scope, permanently, and will keep being proposed

Each of these has been asked for directly. Saying no is not a gap.

- **Named tool, skill, plugin or model recommendations.** `ROADMAP.md` forbids curated lists;
  `SECURITY.md` is the reason. The most this artifact will ever give is nine categories and five
  vetting facts. Advice of that kind belongs in the author's `LOCAL.md`, never here.
- **Product rankings** of harnesses, models or subscriptions.
- **Vendor mechanics**: hook syntax, command file formats, subagent frontmatter.
- **Any observation from a repository the author does not own.** Withdrawn at 0.8.0 and not
  recoverable.

### The one want this artifact cannot meet as stated, and it should be said rather than quietly missed

The author asked for something that means **never having to research this again**, self-updating. In
a field where eight outside checks each found something and the rate has not slowed, a
never-stale digest is not available. **What is available is an honest map of what is known, what is
contested and what nobody has measured, refreshed on a cadence.** `REFRESH.md` is that cadence and
the build warns when it lapses. Anything promising more than that is the failure mode this collection
was built to avoid.

### The structure, since 2026-09-08

**Two artifacts, deliberately.** `SKILL.md` and its companions are the rules an agent loads.
`evidence/` is the apparatus a human reads and cites, built as one document by `build.py` and
excluded from the skill.

They were one thing until an external evaluation pointed out that they have opposite optimal sizes
and opposite cadences, and that sharing a repository, a version and a build is **why seven
verification passes produced evidence entries and no rules**: the apparatus is where work is legible,
so the apparatus got the work. **Do not put apparatus back in the skill.** A source, a gap, a
disagreement or an error entry goes in `evidence/`.

### Two rules about other people's collections

**Never ingest content from a collection that carries no citations.** `obra/superpowers` and
`addyosmani/agent-skills` between them have one informal academic citation across 189 markdown files
and no confidence marking of any kind. Taking a rule from either and tiering it here would launder an
unmarked claim through this scale, which is the exact thing this collection exists to prevent. **They
are a signal source, never a content source:** "a comparable added a rule about X" is a research
lead, and the research still has to happen.

**Two peers are ahead of this collection on method and should be read as such.**
`martinholovsky/SOTA-skills` measures its own lift against an unguided baseline, publishes nulls and
a retraction, and runs negative-control CI. `sjarmak/engineering-reliable-coding-agents` is the
companion to a 314-page monograph with a versioned catalog and an evidence ledger. **Read their
method. Do not copy their rules.** Both are tracked in `sources.yml`.

### Pre-register a rule change before you make it

**Adopted 2026-09-09 from `martinholovsky/SOTA-skills`, which is ahead of this collection on
measurement discipline.** Before changing or adding a rule on the strength of an anecdote or a single
observed failure, write a short dated note and **commit it before or alongside the change, never
after**:

- What you expect the rule to change.
- **What observation would show it did not help**, stated as a threshold you will not move.
- The ways the change could fail to measure anything, listed in advance **so they cannot be
  discovered afterwards as an explanation for an inconvenient result.**

**This does not manufacture a control and does not pretend to.** This repository has no runnable
artifact whose lift can be measured, and most of the borrowed project's apparatus therefore does not
transfer, which is recorded honestly at `.agents/sota-method-2026-09-09.md`. What it does is stop the
repository reading its own outcomes as confirmation after the fact, which is the one failure a prose
collection can actually close.

**One data point is not a number.** Never publish a first-party figure without its sample size
attached. Two figures in the borrowed project were walked back by a larger sample: a +0.07 retracted
at n=49, and a +0.40 revised to +0.39. This collection's first-party findings come from four
repositories and are routinely single incidents.

### Making a check fail on purpose is not enough on its own

**Sharpened 2026-09-09.** This repository's practice has been to plant a defect and confirm the build
fails. That accepts **any** failure, and the borrowed project documents why it is insufficient: a
mutation caught for the wrong reason is a **false pass**, and a harness accepting any non-zero exit
will report every control caught even when every run dies before the thing under test.

**So a fail-on-purpose test asserts two things, not one:** that the build failed, **and that the
intended check is the one that produced the message.** Their own harness found this the hard way,
twice: once when a probe failed on check 6 instead of check 15 because a staged file leaked between
probes, and once when a piped `grep -q` under `pipefail` reported a real catch as a false pass.

### Verify what runs, not only what you build

**Added 2026-09-09, as error 28, and it is the worst thing recorded here.** `build.py` verifies the
artifact it produces. The watcher verifies the sources it cites. **Nothing verified the copy that
was actually loaded**, and for five days that copy was eleven releases stale, on the author's own
machine, in every session, including the sessions writing the corrections it did not have.

Two things follow, and neither is a new build check, because the failure lives outside any build's
reach by construction:

- **An install that cannot name its version is broken, whatever it contains.** `README.md` refuses
  the copy install for this reason. A copy has no version and no path back to one.
- **Assert the loaded version before acting on loaded rules.** `SKILL.md` states its version in its
  eighth line. That question had never been asked, which is why `ADOPTION.md` now opens with it.

**And the general form, which is the eighth row of the boundary table in `evidence/EVIDENCE.md`:**
every check in this repository has drawn its boundary at a convenient unit inside the project.
Before adding one, ask what sits immediately outside the unit it examines.

### Detection is automated. Judgment is not.

`sources.yml` and `.github/workflows/source-drift.yml` watch the external sources monthly and file a
report. **That job never edits a claim, moves a tier, opens a pull request, or updates its own
baseline hashes.** It classifies every source as `unchanged`, `changed` or `unreachable`, and
**`unreachable` is never merged into either of the other two.**

The boundary is not caution. Four of this collection's recorded errors came from a network-restricted
session treating "could not reach" as "not there", and **a CI runner is more restricted than a
browser, not less**. Automating the adjudication would put this project's most repeated failure cause
on a cron schedule. The report is the input to `REFRESH.md`, which a human runs.

### The test to apply to any proposed change

**Does it make a rule an engineer can act on, or does it make the apparatus larger?** Seven
verification passes have run and zero adoptions. Every one of those passes generated evidence,
changelog and error entries. **None of them generated a rule.** The apparatus is not the deliverable
and it has been growing faster than the thing it supports.

## The rules that are not negotiable

- **Do not add a claim without a tier, a `first-party` label, or an explicit convention marker.**
  Every section maps to its evidence kind in `SKILL.md`'s provenance table. Update that table when
  you add a section.
- **Do not write a figure you have not fetched from its primary source.** A research agent reporting
  a number is not a source. This collection carried a **fabricated statistic** for a day because it
  was specific, quotable, and agreed with a position already held. That is error 14.
- **Do not conflate "could not confirm" with "confirmed absent".** They are different results and
  only the second is evidence. Say which you have, every time.
- **Do not report an absence without stating what you searched for.** A search for one platform's
  wording, run against a system using another, completes cleanly and returns zero. That is error 10.
- **Do not trust your own paraphrase of a number.** Verifying provenance and verifying wording are
  separate passes. Three recorded errors were correct citations restated wrongly. **A number and the
  words qualifying it must come from the same sentence.** Finding the figure in the source is not
  enough: a retelling that keeps the number and borrows its qualifier from a neighbouring claim
  passes every figure check there is. That is error 19.
- **Do not confirm a venue from a surface the authors control.** Not the arXiv `Comments` field, not
  a conference banner in the paper's own typesetting, not an institutional publication page, not a
  lab's replication repository, not a ResearchGate entry. Tier 2 needs a publisher DOI, the venue's
  own programme or proceedings, or an independent index, and **an arXiv DOI is not a publisher DOI**.
  Half of this collection's preprint-based tier-2 ratings failed this. That is error 20.
- **Do not fix only the instance you were shown.** A finding that one entry breaks a rule is a
  hypothesis about every entry. The pass that found error 20 flagged one paper; auditing the rule
  instead of the paper found three more.
- **When you move an entry between tiers, leave a forwarding pointer** in the tier it left, opening
  with the exact words `**Moved out of this tier`. `build.py` reads that marker to tell a pointer
  from a claim, so rewording it silently removes the entry from the venue check.
- **Do not correct a figure in one file only.** When a number changes, **grep the whole collection**
  before calling it done. One unchecked detail once reached five documents. That is error 13.
- **A correction is not finished until you have grepped the agent-facing files specifically.**
  `SKILL.md`, `WORKFLOW.md`, `DOCS.md`, `SECURITY.md`, `PROFILE.md`, `OPERATING.md`. Three separate
  corrections landed in `EVIDENCE.md` or `RESEARCH.md` and never reached them, leaving the withdrawn
  version loading on every session while the corrected one waited to be looked up. That is error 21,
  and the general form is that **the file where a correction is easiest to write is not the file
  where it matters.**
- **Do not write that a source was read in full unless you opened it.** Where a verification pass
  reports a full-text read, record that the pass reported it. Two invented figures shipped for two
  days under the sentence "both full texts were read", which disabled every check a reader could have
  run. That is error 23.
- **Do not withdraw a claim on evidence you would not have accepted to make it.** If the primary
  source cannot be opened, mark the claim unverified and leave it. Removing it is an equally strong
  assertion about the source. That is error 19.
- **When a finding gives you a rule, re-scan against the rule's population, not the finding's
  location.** An audit that fixed every instance in tier 2 left the identical defect in tier 1, one
  heading above. That is error 22.
- **Do not use em dashes**, anywhere, including commit messages. Use a comma, a colon, or a full
  stop.
- **Do not name an employer, customer, product, repository or commit hash** in any file except
  `LOCAL.md`. Round exact commit and contributor counts: **precise counts fingerprint a private
  repository.**
- **Do not phrase a rule as a positive directive** where a prohibition works. The convention is
  tier 4 rather than settled, but mixed phrasing is worse than either style.

## What does not belong here, and why it keeps getting proposed

- **Product rankings of any kind**: harnesses, models, subscriptions, "best tool" lists. No
  independent head-to-head exists, they rot within a quarter, and a ranking is not something an
  agent acts on. `TOOLING.md` maps categories instead.
- **Curated recommended-skills or recommended-MCP-server lists.** `SECURITY.md` prohibits installing
  a skill without reading what it executes, and cites a study finding a security flaw in over a third
  of surveyed skills. A recommendation list would contradict the file beside it.
- **Vendor-specific mechanics**: hook syntax, slash-command file formats, subagent frontmatter. Those
  are vendor-documented and change faster than this can track. **The workflow conventions those
  commands encode are in scope** and live in `WORKFLOW.md`; that distinction was got wrong once.
- **New practices with no evidence.** They are the least useful thing to add and the tier scale
  exists to hold them at arm's length.

## When you find an error, and you will

**Record it in `EVIDENCE.md`'s numbered errors list.** Do not quietly fix it. The list is the
argument for the whole method, and every entry has taught a rule that no other entry covered.

State what the error was, how it was caught, and **what rule it produces that did not already
exist**. An error that teaches nothing new is still worth listing, but say so.

**Corrections to the changelog are made by a new entry, never by editing history.** That is the
collection's own rule about the history slot, applied to itself, which is why old entries still
carry retracted phrasings.

## Versioning

- **Patch** for a correction, a clarification, or a packaging fix where no claim changes.
- **Minor** for a new file, a new source that changes a rule, or a scale change.
- The `description` field in `SKILL.md` frontmatter is capped at **1,024 characters**, per Anthropic's
  own skill-authoring documentation, read 2026-09-08. `name` is capped at 64 and must be lowercase
  letters, numbers and hyphens with no reserved words. The description **must not contain a colon
  followed by a space**, which YAML plain scalars cannot hold. That is error 11: it broke the field
  that routes the skill while every other check passed.
- **This file said 200 characters until 2026-09-08 and `build.py` enforced it.** The figure was
  asserted with no source, was wrong by a factor of five, and starved the one field that decides
  whether the skill loads at all. That is error 24. **Write the description to the real budget**: it
  is the only signal the model has, and unused characters buy nothing.
- Bump the version and the recheck date in **both** `SKILL.md` and `README.md`.

## Checks to run before committing

```sh
# em dashes, must be empty
grep -l "—" *.md templates/* examples/*

# identifier leaks, must be empty
grep -n -i -E "REDACTED-EMPLOYER|REDACTED-PROJECT-B|REDACTED-PROJECT-A|Natanael|Fejes" *.md templates/* examples/*

# frontmatter description: must parse as YAML and be under 200 chars
python -c "import sys;s=open('SKILL.md',encoding='utf-8').read().split('---')[1];
d=[l for l in s.strip().splitlines() if l.startswith('description:')][0][13:];
print(len(d), ': ' in d)"

# internal cross-references resolve
grep -oh -E '[\`][A-Za-z_./-]+[.](md|yml)[\`]' *.md templates/* examples/* | tr -d '\`' | sort -u
```

**Make each check fail on purpose before you trust it.** A check that can pass by finding nothing is
worse than no check: the link checker in this repository once reported everything clean while having
extracted zero references. That is error 9, and it is why the last command prints what it examined
rather than just succeeding.

## Building a distributable

`build.py` produces the zip and the embedded JSON bundle. It excludes `LOCAL.md`, `AGENTS.md`,
`ROADMAP.md`, `build.py` and `.git`, because those develop the collection rather than being part of
it.

The zip must contain the skill as a **nested folder** (`dev-conventions/SKILL.md`), not files at the
archive root, or the upload surface rejects it.

## The repository's own profile

`.agents/profile.yml` exists and is derived, not templated. Read it before applying any rule from the
collection to this repository. It is also the third profile in existence, which matters: the
collection's central claim is that it adapts to a profile, and that claim was unexercised anywhere
until 2026-09-03.

## What would genuinely help most

In order, and the first two are worth more than any amount of new writing:

1. **Use it on a repository nobody here has seen** and report where it was wrong or unclear. External
   usage is the 1.0 gate and no amount of editing closes it.
2. **A counter-example**: a repository where one of these rules does not hold, with the mechanism.
3. **A primary source** for anything currently tiered above its evidence, or an answer to a listed
   open gap.
4. Only then, new practices.
