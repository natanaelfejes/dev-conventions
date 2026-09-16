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
derived: 2026-09-16         # the date THIS file was derived by running the commands below.
commits_at_derivation: 369  # git rev-list --count HEAD on that date.
                            # Both added 2026-09-16. They are the only fields a reader can
                            # use to tell a derived profile from a copied one, and until they
                            # existed the two were indistinguishable by construction: the
                            # template shipped pre-filled with three correct answers. Error 32.
                            # `commits_at_derivation` also dates the staleness: compare it to
                            # today's count and you know how much has happened since anyone
                            # looked.

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
  absent:                   # where a MISSING slot's content actually went. With every slot
    history: "milestone notes live in the architecture doc, deliberately"
                            # present, write `absent: {}` rather than omitting the field.
                            # An omitted field is indistinguishable from one nobody checked,
                            # which is the distinction this whole schema exists to keep.

stack:
  language: csharp
  check: just check          # the single command that must be green before a push
  format: just format
  test: just test
  build: dotnet build
  docs_check: just check-docs  # the mechanical documentation check, named separately because
                             # `DOCS.md` and `ADOPTION.md` step 4 require one and it is not
                             # always inside `check`. Added 2026-09-16: an adoption run invented
                             # this key unprompted to record the command the procedure had just
                             # told it to build, which is the definition of a missing slot.
                             # Write `docs_check: none` if there is not one yet.

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

disclosure: undecided       # assisted-by | generated-by | none | undecided
                            # Which AI-authorship trailer this repository uses. `WORKFLOW.md`
                            # makes this a rule and records that the ecosystems have NOT
                            # converged on one token, so there is a decision here and it is
                            # per-repository. `undecided` is a real value and the honest one
                            # until somebody decides: a repository with several hundred
                            # substantially agent-written commits and zero trailers of any kind
                            # has made this decision by default, and without a slot the next
                            # adoption pass raises it again as new. Count before you write it:
                            # `git log --grep='Assisted-by' --oneline | wc -l`, and the same for
                            # the other tokens. Derived, like everything else here.

maturity: prototype         # prototype | production | published

declined:                   # what was CONSIDERED and deliberately NOT done, so an idempotent
                            # pass does not re-propose it. A list of {what, when, why}.
  - what: CONTRIBUTING.md   # Added 2026-09-16. `DOCS.md` and `ADOPTION.md` step 5 propose the
    when: 2026-09-16        # same handful of commonly absent documents on every run. Without
    why: "solo repository, no second contributor exists, and this is deliberate"
                            # this block the only way to stop a third run re-proposing them was
                            # to write an instruction into the profile telling the next agent
                            # not to, which broke this file's own last section. An adoption run
                            # did exactly that, and reported that there was no other option.
                            #
                            # KEEP EACH ENTRY DESCRIPTIVE. "no second contributor exists" is a
                            # fact about the repository. "do not add one" is an instruction and
                            # belongs nowhere in this file. The difference is the whole reason
                            # this block is allowed to exist.

secrets:                    # a LIST, always, even with one entry. The first adoption run
  - config/local.json       # found three paths across two project directories, which do not
  - .env                    # read on one line, and a comma-separated scalar leaves a reader
                            # guessing whether to split on commas or iterate a sequence.
                            # With NO secret-bearing path at all, write `secrets: []`, not
                            # `secrets: none`. Added 2026-09-16, for the same reason as
                            # `absent: {}`: the empty list is the answer "checked, found
                            # nothing", and a scalar is a different shape every reader has to
                            # handle twice. This collection's own profile held the scalar
                            # until the validator was written and pointed at it.

setup: ~/.agents/setup.yml  # your resolved stack, installs and delegation policy.
                            # Write `setup: none` if that file does not exist yet, and never
                            # leave it blank: blank reads as "not applicable" and as "never
                            # checked" equally well. `none` means SETUP.md has not been run
                            # on this machine, which is a fact worth carrying.
                            # Added 2026-09-08. It does NOT vary by repository, so
                            # it does not live here: a value repeated in seven
                            # profiles is a value that will be wrong in one of them.
                            # `SETUP.md` is the procedure that produces it, run once.
```

## Validate it, because this collection's first rule is not to do a linter's job in prose

**`templates/validate_profile.py` checks a profile against this schema.** Run it after writing one
and before trusting one:

```sh
python3 templates/validate_profile.py .agents/profile.yml
```

It reports what it examined rather than exiting quietly, it fails when it finds nothing to check, and
it takes `--self-test` to make it fail on purpose, which is the only reason to believe it when it
passes.

**Why this exists, stated plainly because it is embarrassing.** The first and most repeated rule in
`SKILL.md` is "do not put in an auto-loaded file what a linter, formatter or analyzer can enforce",
and **the one artefact every other rule in this collection depends on had no validator at all** until
2026-09-16. An adoption run found a profile with a comma-separated scalar where this file says list,
an absent `setup` where this file says never blank, and four stale values, every one of them
machine-checkable in a few lines. When that finding was checked, **this collection's own profile had
two of the same defects**, and eleven build checks and ten verification passes had not seen them,
because not one of them looks at a profile. That is error 34.

**Point it at the files that cite a profile too.** `--cite <file>` flags a citation naming a field or
value this schema does not have. That is not hypothetical: a change template and a pre-push hook,
copied wholesale between two sibling repositories, both cite `review: none`. The field is `reviewers`
and `review` is a different field holding the list of available passes, so **both files cite a field
and value pair that does not exist, in two repositories, and nothing caught it.**

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
| `stack.docs_check` | Named wherever a documentation gate is required, the same way `stack.check` is, so `DOCS.md`'s rules are portable. |
| `disclosure` | Settles which trailer a commit or change description carries, so `WORKFLOW.md`'s rule resolves to one answer here instead of three. |
| `declined` | Read before proposing anything from `DOCS.md`'s commonly-absent list or `ADOPTION.md` step 5. **A decline recorded here is answered, not open.** |
| `derived`, `commits_at_derivation` | Tell a derived profile from a copied one, and say how much has happened since anyone looked. |

## Writing one for a new repository

**Do not fill it in from a template.** A profile copied and lightly edited is worse than none,
because it looks derived. Every field below is answerable by running something, and the commands are
here so the answer is reproducible by the next person rather than resting on what you happened to
know.

Work in this order. It is ordered by dependency, not by importance: the later fields read better once
you have seen the earlier output.

**The commands below are POSIX and this was never stated.** They use `head`, `wc`, `awk` and pipes,
none of which exist in PowerShell, and the first adoption run hit this in a Windows-first repository
whose own gate is pinned to `powershell.exe`. They ran only because a Bash tool happened to be
available. **Run them in a POSIX shell, or translate as you go:**

| POSIX | PowerShell |
|---|---|
| `… \| wc -l` | `… \| Measure-Object -Line` or `(… ).Count` |
| `… \| head -1` | `… \| Select-Object -First 1` |
| `git log --format='%ae\|%ce' \| awk -F'\|' '$1!=$2' \| wc -l` | `(git log --format='%ae\|%ce' \| Where-Object { $_.Split('\|')[0] -ne $_.Split('\|')[1] }).Count` |
| `… \| grep -iE "pat"` | `… \| Select-String -Pattern "pat"` |
| `grep -inE "pat" FILE` | `Select-String -Pattern "pat" -Path FILE` |
| `ls -a \| grep -iE "pat"` | `Get-ChildItem -Force \| Where-Object Name -match "pat"` |
| `ls docs/ docs/adr* 2>/dev/null` | `Get-ChildItem docs, docs/adr* -ErrorAction SilentlyContinue` |

**The table covered section 2 only until 2026-09-16, and section 2 is not where this hurts.** A
second adoption run reported that sections 3 and 5 were untranslated, and section 3 is the one this
skill calls the section that matters most. The last three rows are those. **Net effect before the
fix: the derivation procedure as literally written did not execute in the shell that repository's own
gate is pinned to.**

**`git` itself is identical in both**, which is the point: every derivation here is a git query with
a counting pipeline bolted on, and only the bolt-on is shell-specific.

**Keep each command flat, one pipe at most, and run the counting step separately if you need it.**
The same run had several composed `git … | awk … | wc` pipelines **refused outright by its harness's
own worktree-isolation guard as too complex to verify**, and had to re-run them as separate plain
commands. A derivation that depends on composition has a second way to fail that has nothing to do
with your shell. This file has proposed replacing the pipelines with a script since it was written
and has not done it; that is recorded as open rather than claimed.

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

Then check whether a pull-request flow exists at all. **Read the host off the remote before you
choose a query, rather than trying wordings and hoping:**

```sh
git remote -v            # the host is in the URL, one command, and it costs nothing
```

Each host writes a different merge subject and **they share no anchored prefix**, so a query
written for the wrong host returns a clean, well-formed zero. Look up the one your remote names,
then run the sweep below as a safety net rather than as the primary method:

```sh
git log --oneline -i --grep='pull request' | wc -l   # catches most platforms
git log --oneline --grep='^Merge pull request' | wc -l
git log --oneline --grep='^Merged in ' | wc -l
```

**The single-wording version of this check has produced a false absence twice, once in this
collection's own research and once during a live adoption run against the rule written to prevent
it.** In the second case the most widely documented host's phrasing returned **zero** while the
host the repository was actually on returned **33**. A clean zero from a well-formed query is
indistinguishable from a genuine absence, so the failure is silent and confident.

**And the thing that would have been lost is not the flow's existence but its character.** All 33
merges carried identical author and committer identity, which makes the flow a continuous-integration
gate rather than review. Recording `none` and recording `reviewers: one` would both have been wrong,
in opposite directions. That is why this field is derived from history rather than from what the
contributing guide claims.

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

### 5. `docs`, and the five displacement targets

List what exists, not what should:

```sh
ls README.md CHANGELOG.md CONTRIBUTING.md 2>/dev/null
ls docs/ docs/adr* 2>/dev/null
```

For each of the four slots with no home, fill `absent` with **where that content actually went**, not
with the fact that it is missing. Check all five targets before concluding anything is absent:
sibling documents, commit messages, branch topology, an external tracker, and a sibling repository
where one exists.

**And a fifth target where one exists: a sibling repository.** Added 2026-09-16. Two repositories
worked by the same author, sharing a toolchain and copying conventions from each other, share
documentation slots too: a pending-work document in one carried three items explicitly carried back
from the other. `docs.absent` has no vocabulary for that, so write it in the value:
`pending: "roadmap items for this service live in the sibling service's roadmap, deliberately"`.
**A displaced slot you cannot name the destination of is not recorded, it is guessed.**

A cheap way to see whether a repository looks at its own documents at all:

```sh
git log --oneline -i --grep='doc' --grep='readme' | wc -l
```

Against the total commit count this is a rough self-audit rate. Two real repositories measured about
**21%** and about **0.03%**. That gap is not about documentation quality. It is about whether anyone
ever looks, and the low one is where documentation is worst while generating no signal at all.

### 6. `maturity`, derived last

Derived, never copied from the readme. See the section below. **Without a licence, `maturity` cannot
exceed `production`.**

**That sentence read "No licence caps this field, whatever else is true" until 2026-09-16, which says
the opposite of what it means on the most natural reading.** `ADOPTION.md` carried a longer version
that was ambiguous in a different way. An adoption run against a repository with no licence file
reconstructed a ceiling of `production`, which is correct and is not what either sentence said. A
constraint stated as the negation of a cap parses both ways. **State the bound and the value in the
same clause.**

### 7. Record your uncertainty in the file, in one line

Any field you guessed gets a comment saying so, with the date. **A profile that hides which fields
were guessed is worse than a blank one**, because the next reader cannot tell what to re-check.

**One dated line per corrected or guessed field. Not a paragraph.** A second adoption run following
`ADOPTION.md`'s derive-then-diff instruction produced multi-line comment blocks reconstructing what
each old value had been and why it was wrong, and the file grew from 131 to 205 lines and became
roughly 80% comment by volume. **The cost is not length, it is that the next diff cannot run:** you
can diff `test: null` against `test: just test`, and you cannot diff a fifteen-line comment block
against another one, so the profile's load-bearing content becomes the part that is hardest to
compare. `# 2026-09-16: was null, re-derived` is the whole obligation. If the reasoning is worth more
than a line, it belongs in the change description, which is the record of why anything changed.

**And `SKILL.md`'s "do not leave a superseded rule in place with an annotation" does not apply
here.** That rule is about instruction files, and this file is not one, as its last section says. **A
profile is a record, and a record keeps its dated correction.** Nothing said so until 2026-09-16, and
an adopting agent read the two as colliding and had to choose unaided.

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
3. **Check the five displacement targets before concluding a slot is absent.** In a repository with
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

## A profile is a snapshot with no subscription to the thing it describes

**The maintenance cost of this mechanism, measured twice in the same repository and reported here
because it is the honest half of proposing the mechanism at all.**

- **Round one: hours.** Two adoption passes ran on one repository hours apart, converged on the same
  findings from different directions, and one fixed a finding before the other reported it. A profile
  carried a claim that was true when written and false within hours.
- **Round two: five days.** A field written 2026-09-10 recorded a security property in prose: one
  shared static secret, no per-caller identity. A feature shipped 2026-09-11 replaced that secret
  with named per-caller keys. **The field was still wrong on 2026-09-16.** The same file had a
  different stale claim corrected on the day it was written, so this is not an author who ignores
  stale claims. **Nothing about the format prompts a look when the property it describes changes.**

Three rules follow, and none of them is "re-derive it periodically", because a cadence is another
thing to remember:

- **Do not record a property in prose in a profile when a command can state it.** `secrets` names
  paths, and a path is checkable. "The auth token is one shared static secret" is a sentence about
  code, it has no checker, and the code moved. Prefer the field that a command can re-derive.
- **Tie the re-read to the change, not to the calendar.** The moment a change alters something the
  profile describes is the only moment anyone is looking. **A change that falsifies a profile field
  is not finished until the field is corrected**, the same way a change that falsifies a comment is
  not finished.
- **When a field changes, re-check the documents that field cites, and the documents that cite the
  field.** Found 2026-09-16: a profile named a specific file as the written authority behind its
  displacement warning and quoted its line range, and that file had since been contradicted by the
  repository. The profile's own correction to the affected slot **did not chase the citation back to
  its source**, so the authority the profile leaned on now disagreed with it. This is error 21's
  shape, a correction landing in one file and not the file that matters, inside a single profile.
- **Record `commits_at_derivation`** so the next reader can measure the gap instead of guessing at
  it. It costs one command.

## Cite what you ran, not what this skill concluded

**A profile justifies its values with the repository's own output.** `git log --grep=… | wc -l`
returning 33 is a citation. "The mistake the skill's Layer 3 warns about" is not, and neither is "by
the skill's own definition" or a reference to a finding observed in somebody else's repository.

The reason is mechanical rather than stylistic. `EVIDENCE.md` is **not in your install**, by design,
and `SKILL.md` says so. **So a profile written in that register produces justifications a future
reader of that repository cannot check**, which is the same defect the profile exists to prevent
elsewhere. Observed 2026-09-16 in a profile written by an adoption pass, and the style came from the
skill rather than from the author.

Where you genuinely need the skill's reasoning, name the rule and let the reader load the skill.
**Do not restate the evidence, because you do not have it.**

## Profiles are not instructions

This file describes a repository. It carries no rules of its own, and nothing in it overrides
`SKILL.md`. A profile that starts telling an agent what to do has become a second instruction file,
which is the thing the sizing rules exist to prevent.

**The `declined:` block exists because this rule was under real pressure and losing.** An adoption
pass that keeps being told to propose the same three documents, in a repository that has deliberately
refused all three, has exactly one way to stop the next pass re-proposing them: write an instruction
into this file. One did, and reported that there was no other option. **A decline is a fact about the
repository, so it gets a descriptive slot**, and the rule holds. Check the wording of every entry you
add: "no second contributor exists" is a fact, "do not add one" is an instruction.
