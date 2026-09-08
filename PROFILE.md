# The repository profile

One small file per repository, read before any rule in `SKILL.md` is applied. It exists because
repositories legitimately differ, and a convention set that prescribes one answer is wrong in most
repositories it touches.

Location, in preference order:

1. `.agents/profile.yml` - preferred. Vendor-neutral: the `.agents/` convention reads naturally to
   agent tooling from more than one vendor.
2. A fenced `yaml` block in the root instruction file, for repositories that would rather not add a
   file.

## Schema

Every field is optional. An absent field means "infer it and say so", not "use a default silently".

```yaml
team: solo                  # solo | pair | small-team | open-source
reviewers: none             # none | nominal | agent | one | rotating
                            # humans who actually read the diff, not agents, and not humans a
                            # template claims. See "Nominal reviewers" below before choosing.

docs:                       # which slots exist, and where a missing slot's content goes
  current_state: docs/ARCHITECTURE.md
  history: CHANGELOG.md
  pending: docs/ROADMAP.md
  decisions: docs/adr/
  contributing: CONTRIBUTING.md
  absent:
    history: "milestone notes live in the architecture doc, deliberately"

stack:
  language: csharp
  check: just check          # the single command that must be green before a push
  format: just format
  test: just test
  build: dotnet build

review:                     # which passes are actually available in this repo
  - code-review
  - security-review
  - independent-context

tools:
  orchestrator: frontier    # role, not brand. Naming a model here means the
  worker: cheap             # profile needs editing every time you switch
                            # vendors or a model is renamed, and vendor churn
                            # is faster than repository churn.
  forbidden: []             # e.g. tools banned by an employer or a course

maturity: prototype         # prototype | production | published
secrets: appsettings.Development.json, .env    # gitignored, never committed

setup: ~/.agents/setup.yml  # your resolved stack, installs and delegation policy.
                            # Added 2026-09-08. It does NOT vary by repository, so
                            # it does not live here: a value repeated in seven
                            # profiles is a value that will be wrong in one of them.
                            # `SETUP.md` is the procedure that produces it, run once.
```

## How the skill uses each field

| Field | Effect |
|---|---|
| `team`, `reviewers` | Selects Layer 2 or Layer 3 in `SKILL.md`. `reviewers: none` is what makes the change description the review record. **`nominal` and `agent` keep that obligation**, because neither supplies a human who reads the diff. Only `one` and `rotating` discharge it. |
| `docs` | Every documentation rule checks this before assuming a file exists. |
| `docs.absent` | Triggers the displacement check: if a slot is missing, verify its content is not silently accumulating somewhere that forbids it. |
| `stack.check` | Named in the pre-push gate and in any "must be green" instruction, so the rule is portable across languages. |
| `review` | Constrains which passes a change description can claim, and which it must explain omitting. |
| `tools` | Sets the orchestrator and worker tiers for delegation decisions in `OPERATING.md`. |
| `maturity` | `prototype` permits documented gaps; `published` requires a licence, no employer-identifying content, and an explicit statement of what is not established. |
| `secrets` | Feeds the check that no listed path is tracked, and that none appears in history. |

## Writing one for a new repository

**Do not fill it in from a template.** A profile copied and lightly edited is worse than none,
because it looks derived. Every field below is answerable by running something, and the commands are
here so the answer is reproducible by the next person rather than resting on what you happened to
know.

Work in this order. It is ordered by dependency, not by importance: the later fields read better once
you have seen the earlier output.

### 1. Size and age, which calibrate everything after

```sh
git rev-list --count HEAD
git log --reverse --format=%ad --date=short | head -1   # first commit
git log -1 --format=%ad --date=short                    # last commit
```

A repository with 300 commits over three months and one with 20,000 over a decade need the same
fields filled differently. Note both before deciding anything else.

### 2. `reviewers`, and this is the field most often wrong

Do not read it off a policy, a template, or a branch-protection setting. Count it.

```sh
git log --format='%ae|%ce' | awk -F'|' '$1!=$2' | wc -l   # author != committer
git rev-list --count HEAD                                  # denominator
git log --grep='Reviewed-by' --oneline | wc -l
git log --grep='Co-authored-by' --oneline | wc -l
```

Near-zero on all of those means **nobody's review left a trace**, whatever the process claims.

Then check whether a pull-request flow exists at all, and **try more than one wording**:

```sh
git log --oneline -i --grep='pull request' | wc -l   # catches most platforms
git log --oneline --grep='^Merge pull request' | wc -l
git log --oneline --grep='^Merged in ' | wc -l
```

**The single-wording version of this check has already produced a false absence in this
collection's own research**: a search for one host's phrasing against a repository on another host
reported no pull requests where 36 existed. If you only run one of these, you will sometimes
confidently record `none` for a repository that has a flow.

Deciding between the values:

- Trailers and differing identities present, humans reading diffs: **`one`** or **`rotating`**.
- A review agent reviews and no human reads the diff: **`agent`**.
- A template or contributing file names reviewers who never appear in history: **`nominal`**.
- Nothing claims a reviewer and none exists: **`none`**, and Layer 2 applies.

A PR flow whose merges are all self-merged is **not** review. It is a CI gate. Record it in a comment
so the next reader does not mistake one for the other.

### 3. `secrets`, and enumerate before you verify

**Enumerate first. This step used to start at verification and that was a real gap**, found
2026-09-04 when an agent following this procedure discovered a second credential-bearing file that
the profile's `secrets` field had simply never mentioned. The verification commands were correct and
they were being pointed at a list assembled from memory.

```sh
# Candidates from the ignore file itself, which is where they are declared
grep -inE "env|secret|credential|\.pem|\.key|password" .gitignore

# Candidates on disk, including ignored ones
git status --ignored --short | grep -iE "env|secret|credential|\.pem|\.key"

# And any example or template file, because a real sibling usually exists
ls -a | grep -iE "\.example|\.template|\.sample"
```

Then verify **each** candidate:

```sh
git check-ignore -v path/to/secret.env    # is a rule actually covering it?
git log --oneline -- path/to/secret.env   # has it EVER been committed?
```

The second command is the one that matters. An ignored path can have been committed before it was
ignored, and the ignore file says nothing about that. Empty output is the answer you want, and it is
the only evidence worth recording.

**Then check the example file against the real one, by key name only.** Never read the values into
your output. A `.env.example` missing a key the real file needs is how a new contributor ends up
improvising a value, and improvised values end up in chat. See `SECURITY.md` on why an undocumented
secret destination means chat becomes the destination.

### 4. `stack.check`

Find the one command that runs format, build and test together. **If none exists, stop and build it
before writing anything else in this file**, because every other gate in this skill depends on there
being one command whose green state means something.

Then read what it actually does. One repository's `check` recipe turned out to shell into a
PowerShell script, which makes the gate non-portable to anyone else's machine. That is a real
constraint on handing the repository to a colleague and it was written down nowhere. **Record what
you find, not the recipe name.**

### 5. `docs`, and the four displacement targets

List what exists, not what should:

```sh
ls README.md CHANGELOG.md CONTRIBUTING.md 2>/dev/null
ls docs/ docs/adr* 2>/dev/null
```

For each of the four slots with no home, fill `absent` with **where that content actually went**, not
with the fact that it is missing. Check all four targets before concluding anything is absent:
sibling documents, commit messages, branch topology, and an external tracker.

A cheap way to see whether a repository looks at its own documents at all:

```sh
git log --oneline -i --grep='doc' --grep='readme' | wc -l
```

Against the total commit count this is a rough self-audit rate. Two real repositories measured about
**21%** and about **0.03%**. That gap is not about documentation quality. It is about whether anyone
ever looks, and the low one is where documentation is worst while generating no signal at all.

### 6. `maturity`, derived last

Derived, never copied from the readme. See the section below. **No licence caps this field**, whatever
else is true.

### 7. Record your uncertainty in the file

Any field you guessed gets a comment saying so, with the date. **A profile that hides which fields
were guessed is worse than a blank one**, because the next reader cannot tell what to re-check.

### One thing worth doing while you are in here

```sh
git shortlog -sne HEAD
```

If one human resolves to more than one name-and-email pair, a `.mailmap` fixes it and almost nobody
has one. Observed in a solo repository as **three identities for one person**, two surname spellings
and two letter cases of one address, so this is a per-machine-configuration problem rather than a
team problem. Teams merely make it visible.

## Nominal reviewers

`reviewers: nominal` means **the repository declares a reviewer it does not have.** A change
template with a reviewer checklist, or a contributing document binding two people, while in practice
every change is self-merged by its author.

Observed first-party: 47 of 47 merged changes self-merged, zero human reviews across 51, with both
of those documents present.

**External corroboration, added 2026-09-03. Tier 4 since 2026-09-07**, down from tier 2 when the
study's stated venue could not be confirmed against any record its authors do not control. This was
pure inference from one repository until a mining study of agent-authored pull requests found that
**most receive no review at all**. So the state is common rather than a local quirk, which is the difference between a
schema value worth having and a private grievance.

What external work still does **not** cover: whether a declared-but-absent reviewer is *worse* than
an acknowledged absence. A search found no study testing review-policy compliance or checklist
effectiveness as a primary outcome. That specific comparison stays `first-party` inference, and it
is the part of this section to treat with most suspicion.

It is its own state rather than a rounding error toward `none`, because it has a distinct failure
mode. With `reviewers: none`, Layer 2 applies and the change description becomes the review record.
With `nominal`, that compensating control silently lapses: nobody writes the review-passes record
because a reviewer is nominally going to catch it, and nobody reviews because they were never
actually asked. **The declared reviewer removes the solo discipline without supplying the team
discipline.**

Determine it from history, not from documents: count changes where the merging identity differs from
the authoring identity, and count review comments. If both are near zero while a reviewer checklist
exists, this is the state.

## Agent reviewers

`reviewers: agent` means **a review agent reviews changes and no human reads the diff.** Added
2026-09-03 because it is now a common state with its own measured failure mode, and folding it into
`one` or `nominal` hides that.

It is not `nominal`, because the review genuinely happens and produces comments. It is not `one`,
because the reviewer cannot be accountable and does not carry the context a colleague carries.

Measured, tier 2, from a peer-reviewed mining study of agent-authored pull requests: changes reviewed
**only** by a review agent merged at **45.20% against 68.37%** for human-reviewed ones, a 23-point
gap. 60.2% of the closed agent-only-reviewed changes fell in the lowest signal-to-noise band, and
**12 of 13 review agents averaged a signal ratio below 60%.** The study's own conclusion is that
review agents should augment rather than replace human reviewers.

What that means for the rules, and it is not "turn the agent off":

- **The Layer 2 solo discipline still applies.** An agent reviewer does not discharge it. Write the
  review-passes record, because the compensating control for a missing human reviewer is a written
  account of what was checked, and an agent's comment thread is not that.
- **Do not let an agent reviewer gate a merge on its own.** Roughly two comments in five carry
  signal at the measured rates. A gate that wrong is a gate people learn to click through, and then
  you have neither the agent nor the habit.
- **Instruct it to disagree.** See `SKILL.md`. A reviewer agent's default failure is agreement, and
  the same measured pattern shows up in the model-as-judge literature at a true positive rate above
  96% against a true negative rate below 25%.

Set this value honestly. A repository with an automated reviewer and no human one reads as reviewed
on every dashboard and is closer to `none` than to `one` in what it actually catches.

## Maturity is derived, not declared

**Do not copy the maturity claim out of the readme.** Observed first-party in three of three
non-work repositories, in both directions:

- One self-describes as production-ready with a data-protection checklist, and has no tests, no CI,
  and no reviewers.
- One is versioned `0.1.0` and named a prototype, and runs live behind authentication with rate
  limiting, per-caller quotas, access logging and a secrets pre-commit hook.
- One says a phase is complete with substantial work committed past it.

That is a pattern rather than three coincidences. Derive the field from process evidence: does a
check command exist and does anything run it automatically, are there tests and do they exercise the
assembled system, is there a credential boundary, is there a licence. `published` in particular is
not a claim about ambition - it requires a licence, no employer-identifying content, and an explicit
statement of what is not established.

## Cold start: a repository with no agent configuration

One inventoried repository has no instruction file, no agent directory, no hooks and no skills, while
self-describing as production-ready. The schema above assumes something to read; this is the path
when there is not.

1. **Do not write a profile and an instruction file in the same pass.** Establish the check command
   first. Everything else in this skill depends on there being one command whose green state means
   something, and in a repository with no CI and no combined check that command usually does not
   exist yet. Build it, then profile.
2. **Read history for the conventions nobody wrote down.** Commit subject style, branch naming, and
   whether changes are reviewed are all observable without a document, and all three were
   inconsistent in the repository above, which is itself the finding: no rule was ever agreed.
3. **Check the four displacement targets before concluding a slot is absent.** In a repository with
   one readme and nothing else, the history is in commit messages and the roadmap is in unmerged
   branches. Both were, there.
4. **State the inferences in the profile itself**, in a comment, with the date. A profile that hides
   which fields were guessed is worse than a blank one.
5. **Do not add an instruction file because this skill exists.** If nothing about the repository is
   hard to infer from its code, the correct instruction file is none.

## The displacement rule

The most useful thing this file encodes. Dropping a documentation slot does not remove its content,
it relocates it, usually somewhere that forbids it.

One observed case: a repository deliberately had no changelog and no roadmap, with a written rule
that its architecture and algorithm docs were current-state only. Its history then accumulated as a
200-line milestone log inside the architecture doc, 90 lines of phase notes in the readme, and one
three-sentence changelog entry inside a decision record's status field. Every one of those violated
the repository's own stated rule.

So `docs.absent` is not documentation of a gap. It is a commitment about where that content goes,
and something to check rather than assume.

## Profiles are not instructions

This file describes a repository. It carries no rules of its own, and nothing in it overrides
`SKILL.md`. A profile that starts telling an agent what to do has become a second instruction file,
which is the thing the sizing rules exist to prevent.
