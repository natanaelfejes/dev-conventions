# Second friction batch, 2026-09-16

**Four sources, two repositories, six days after the first batch.** The first batch, at
`.agents/adoption-friction-2026-09-10.md`, was one timed procedure run in one repository. This one is
not a single run: it is a second full adoption pass, a set of findings from six days of ordinary
development in a second repository, a proposed rule with five dated first-party instances, and a
post-adoption observation round asking whether anything from the first pass was still visible without
being prompted.

**Both repositories are recorded unnamed, per this repository's own rule**, and so are the commit
hashes the raw material carried. Repository A is the one the first batch ran against: a private .NET
service on a Windows-first toolchain, hosted on a platform other than the most widely documented one,
single author, self-merged history. Repository B is a sibling of A, same author, same toolchain
family, which is itself one of the findings.

**Nothing here is a defect-reduction claim and nothing here has a sample size.** Sources A, B and D
are single observations by one author. Source C is five instances in one afternoon across two
repositories, which is a count of instances and not a rate.

---

## What was checked against this repository before anything was acted on

The collection's own standard is that a withdrawal needs the same primary-source standard as an
assertion, so every claim the batch made about the collection's own files was re-run here rather than
accepted. **Nothing in the batch turned out to be wrong.** Two claims turned out to understate the
case and one needed its scope narrowed.

| Claim | Checked | Result |
|---|---|---|
| `templates/profile.yml` ships pre-filled values | Read the file | **True.** `team: solo`, `reviewers: none`, `maturity: prototype` are filled in. `docs`, `stack` and `secrets` are blank. The three filled ones are verbatim this repository's own derived answers |
| `templates/pre-push` tells you to install into `.git/hooks` | Read lines 3 to 5 | **True.** `cp templates/pre-push .git/hooks/pre-push` |
| `SECURITY.md` forbids relying on a gate a fresh clone does not install | Read "Repository obligations" | **True**, and it is one of that file's four repository obligations |
| `ADOPTION.md` is absent from `SKILL.md`'s companion table | Counted the rows | **True.** Thirteen rows, no `ADOPTION.md` and no `README.md` |
| `SOLO.md` is three bullets, `TEAM.md` is nine times its size | `wc -c` | **True.** 1,036 bytes against 9,368. Three bullets, none a failure mode, ending on a bare `---` with nothing after it |
| Nothing validates the profile | Read every check in `build.py` | **True, and worse than reported.** See below |
| The maturity and licence sentence parses two ways | Read `PROFILE.md` section 6 and `ADOPTION.md` phase 1 | **True.** The two files word it differently and neither says what is meant |
| The POSIX translation table stops at section 2 | Read sections 3 and 5 | **True.** Section 3 uses `grep -inE`, `git status --ignored --short \| grep -iE` and `ls -a \| grep -iE`; section 5 uses `ls docs/ docs/adr*`. None is in the table |
| No schema slot for the disclosure decision or the doc-check command | Read the schema block | **True** for both. Also true that `WORKFLOW.md` makes disclosure a rule with three live ecosystem conventions and `ADOPTION.md` step 4 requires wiring a doc check |
| No `declined:` block, so an idempotent pass has nowhere to record a decision | Read the schema and `PROFILE.md`'s last section | **True.** `docs.absent` records where displaced content went, which is a different question |
| The selector defect filed in the first batch is fixed | Read `SKILL.md` layer selection | **True, fixed.** Selectors read `team: solo` and `team: pair`, `small-team`, `open-source` |
| The new rule about deleting prose only when the config is the readable statement landed | Read `SKILL.md` instruction-file rules | **True, landed**, close to the wording the first batch proposed |
| The skill's source repository moved three commits since the install, version still `0.15.0` | `git log` | **True.** Three commits changed shipped content with no version bump. It is deliberate, `ROADMAP.md` item 0 froze the version, and the consumer cannot tell |

**Two places where the finding understated the case.**

**The profile validator finding is stronger than reported.** The batch said the profile has no
validator. It does not, and separately, **this repository's own profile violates its own schema in
two places right now**: `secrets: none` is a scalar where `PROFILE.md` says "a LIST, always, even
with one entry", and `setup` is absent entirely where `PROFILE.md` says never leave it blank and
write `setup: none` instead. Both are machine-checkable in a few lines. Both have been in the
collection's own profile since it was written and eleven build checks and ten verification passes did
not see them, because none of them looks at a profile. That is the finding, not the two defects.

**`SOLO.md` is not only short, one of its three bullets is false.** The third reads: "A
repository-wide sweep can be scheduled at your own convenience, because no one else's branch is in
flight." The first batch recorded a concurrent session moving HEAD mid-pass in a solo repository, and
this batch records four concurrent sessions in a solo repository clobbering each other's build
output. **In a solo repository worked by parallel agent sessions, another branch is in flight, and it
is yours.** The collection's own rule is that a superseded rule is deleted rather than annotated, so
that bullet is corrected rather than footnoted.

**One claim needed its scope narrowed.** Source A item 2 reports a collision between `ADOPTION.md`'s
"mark a carried-forward field unverified" and `SKILL.md`'s "do not leave a superseded rule in place
with an annotation". The `SKILL.md` rule sits under the heading **Instruction files**, and
`PROFILE.md` already closes with "Profiles are not instructions", so on a careful reading the rule
never applied to a profile. **The collision is still real**, because nothing said so and an adopting
agent read them as colliding and had to choose unaided, which is the same shape as the first batch's
report-before-changing ambiguity. The fix is to say it, not to change either rule.

---

## Source A: second full adoption pass, repository A

**The pass's own preamble withdraws its first two findings.** Its worktree predated the merge of the
adoption branch into the default branch, so its "Profile check" section and item 1 described the
default branch as still holding a stale profile when it no longer did. Verified after the merge: the
profile's pending, test, format and setup fields are corrected, a re-derivation over roughly 370
commits is recorded, a mailmap exists, the documentation checker is wired into both the local gate
and CI, the stale suppression is removed, and the checker reports suppression counts. **Items 2
through 13 are independent of that error and stand.** Recording the withdrawal rather than deleting
the items is the same rule the collection applies to its own changelog.

**2. "Derive independently, then diff" collides with "do not leave a superseded rule in place with an
annotation."** `ADOPTION.md` phase 1 says derive independently, report every field where the two
disagree, and mark a carried-forward field unverified in the file. `PROFILE.md` section 7 says
comment any field you guessed, with today's date. `SKILL.md` says a superseded rule is deleted, not
annotated. The run produced entries carrying a corrected value plus a paragraph reconstructing what
the old value was and why it was wrong. The file grew from 131 to 205 lines and became roughly 80%
comment by volume. **The deeper problem is that the next diff cannot run:** you can diff `test: null`
against `test: just test`, and you cannot diff a fifteen-line comment block against another, so the
profile's load-bearing content is the part that is hardest to compare. Fix: say which rule wins in a
profile, and cap a correction at one dated line.

**3. The skill ships `templates/profile.yml` and then forbids using it.** `ADOPTION.md` in bold: "Do
not fill the profile in from a template or from the examples. A copied profile is worse than no
profile, because it looks derived." The template is pre-filled with the three hardest fields, which
are verbatim this repository's correct derived answers. **A copying run and a deriving run produce
indistinguishable files.** Fix: blank the values, and give the profile a provenance field so derived
can be told from copied mechanically.

**4. `templates/pre-push` tells you to install the hook in a way the skill's own rules forbid.** The
header says copy it to `.git/hooks/pre-push`. `SECURITY.md` says "Do not rely on a gate a fresh clone
does not install", and `ADOPTION.md` step 2 makes confirming that required. A hook in `.git/hooks/`
is absent from every fresh clone by construction. **Repository A had independently arrived at the
better pattern**: a tracked hooks directory installed by a recipe that sets `core.hooksPath`, which
is why the step-2 finding there was not "the hook is missing" but "the hook is fine and the
documented setup omits the install step".

**5. `SOLO.md` is three bullets, and it is the half this repository selects.** The companion table
presents `SOLO.md` and `TEAM.md` as symmetric. They are not, and the asymmetry runs backwards
relative to the evidence base: the collection's first-party observation is "four small repositories,
one or two people each", which is the solo case, and the solo file gets a ninth of the words.
Practical cost: `reviewers: none` is what makes the change description the review record, the single
most consequential thing the profile selects, and the file that should explain it spends one sentence
on it.

**6. `ADOPTION.md` is not reachable from `SKILL.md`.** An agent told "load the skill and adopt it in
this repository" reads the companion table and is never told the adoption procedure exists. The
two-phase structure, the stop, and the ordering that puts security before documentation are all
undiscoverable from inside the skill. It worked in repository A only because a human had already
found the file and pasted its prompt.

**7. No field for the disclosure decision, the merge strategy, or the doc-check command.**
`WORKFLOW.md` makes AI-authorship disclosure a rule with three live ecosystem conventions and says
follow the one your ecosystem is converging on. It also asks for one merge strategy, written down.
`DOCS.md` and `ADOPTION.md` step 4 make a mechanical doc check a required output. The schema has a
slot for none of the three. Re-derived in repository A: roughly 370 commits, zero disclosure trailers
of any kind, in a repository whose commits are substantially agent-written. **That is a real decision
made by default with nowhere to record it, so the next pass raises it again as new.** The run also
invented an undeclared `stack.docs_check` key to hold the command step 4 had just required it to
wire up.

**8. No place to record "considered and declined", which pushes the profile into being an instruction
file.** `PROFILE.md` closes with "Profiles are not instructions". `ADOPTION.md` step 5 and `DOCS.md`'s
list of commonly absent documents propose a contributing file, a changelog and a roadmap on every run.
Repository A had deliberately declined all three. To stop a third run re-proposing them, the adoption
pass wrote imperative text into the profile telling the next agent not to add one. **Those are
instructions in the file whose last section forbids them, and there was no other option.** Fix: a
`declined:` block of what, when and why. Descriptive rather than imperative, so it does not break the
rule, and it is exactly the state an idempotent adoption pass needs.

**9. Nothing validates the profile, in a collection whose most-repeated rule is "use a linter, not
prose".** At the point this was found in repository A, the profile had a comma-separated scalar where
the schema says list, an absent `setup` where the schema says never blank, and four stale values.
Every one machine-checkable in about thirty lines. See the section above: the collection's own
profile has two of those defects today.

**10. The maturity and licence sentence parses two ways and the repository's answer matched neither.**
`PROFILE.md`: "No licence caps this field, whatever else is true." `ADOPTION.md`: "No licence caps it
below `published` whatever else is true." `PROFILE.md`'s bare sentence reads most naturally as "there
is no licence requirement that caps this field", which is the opposite of the intended meaning.
`ADOPTION.md`'s longer form leaves open what the ceiling actually is. Repository A has no licence
file, and its profile asserted a ceiling of `production`, which is a reasonable reconstruction and is
not what either sentence says. Fix: "Without a licence, `maturity` cannot exceed `production`." Nine
words, one reading.

**11. The POSIX and PowerShell table stops short of the commands that actually needed it.** The table
covers section 2's counting pipelines. Section 3, the one the skill calls the section that matters
most, and section 5 are untranslated. Second layer: several composed `git | awk | wc` pipelines were
refused outright by the harness's own worktree-isolation guard as too complex to verify, and had to
be re-run as separate plain commands. **Net effect: the derivation procedure as literally written
does not execute in the shell repository A's own gate is pinned to.** The better fix, which
`PROFILE.md` already proposes and does not follow through, is to replace the pipelines with a script,
because every one is a git query plus a counting bolt-on and the bolt-on is the only shell-specific
part.

**12. Convention copying between sibling repositories is unaddressed, and it propagated an error.**
The collection assumes one repository at a time. A commit in repository A adopted a security file, a
change template and a pre-push hook wholesale from sibling repository B. Two of the three cite the
profile as `review: none`. The schema field is `reviewers:`, and `review:` is a different field
holding the list of available passes. **Both files cite a field and value pair that does not exist,
in two repositories, and nothing catches it.** Repository A's displacement story also spans both
repositories, and `docs.absent` has no vocabulary for "this slot is shared with a sibling".

**13. `EVIDENCE.md` is acknowledged as a dead end, and the knock-on is that it undermines the
profile's own style.** `SKILL.md` is candid that the evidence document is not in the install and tells
an agent to say so rather than reconstruct. The effect on the adopting repository is that its profile
is written in a register that constantly appeals to it: "the mistake the skill's Layer 3 warns
about", "by the skill's own definition", "the skill had this as a team problem, observed in a
six-person and a fifty-person repository". **None of that is checkable from the install.** The
adoption style the skill encourages produces a profile whose justifications a future reader cannot
verify.

**Two findings stale on both branches, not fixed by the merge.** Repository A's pre-PR command file
still says the repository has no changelog or roadmap and not to invent one. A roadmap document has
existed there since 2026-09-10. **The profile names that exact file as the written authority behind
its displacement warning and quotes its line range**, so the authority the profile leans on now
contradicts the repository, and the profile's own correction to the pending slot did not chase the
citation back to its source.

---

## Source B: repository B, findings from the last two days

Six findings that are evidence about the skill's own rules. Two are gaps the skill currently cannot
see.

**Gap 1. Worktree isolation is necessary and not sufficient: parallel agents produce defects neither
branch's tests can see.** Twice in one day. A new ranking function was written in one worktree while
a correctness fix landed in another, so the new code arrived carrying the exact defect that had just
been removed elsewhere. Then a fix half-shipped: the default branch had split one query into four
texts for an unrelated feature, git cleanly merged the fix into two of them and left the old constant
in the third. **Both branches were green.** Missing rule: a merge between parallel agent branches
needs a real review pass, not just conflict resolution. Conflict markers appear only where the same
lines changed, and these were semantic collisions in different lines.

**Gap 2. Build-output isolation is part of worktree isolation and nobody says so.** The combined
check command hardcoded a shared artifacts path, so four concurrent sessions clobbered each other's
dependency output and produced a phantom test failure that nearly cost real investigation time.
**Worktrees isolate source. They do not isolate build output, caches or package restore.**

**Corroboration 1, for "do not filter the output of a one-shot, state-changing command".** A direct
hit with a new failure mode. A push piped into a grep for the word error, with `|| echo pushed`
after it, **reported success twice on pushes that never landed**. The `||` fires when grep finds
nothing, and finding nothing includes both success and silence. The idiom that masks it is the
compound one, not plain filtering.

**Corroboration 2, for "instruct the reviewer to disagree, bounded".** Worked, measurably. The review
found three real things and the vendor's over-reporting warning did not materialise. Bounding it to
correctness, security or a stated requirement appears to be the load-bearing half.

**Corroboration 3, for "delete superseded rules rather than annotating them".** It caught its own
author: two roadmap entries argued a bespoke exception to the repository's own rule, and the review
quantified five such entries, each with its own defending paragraph.

**Gap 3. Nobody asks whether a defect has recurred.** Silent truncation shipped four separate times
in repository B before it became a trap in that repository's instruction file. The skill says never
write a rule you cannot cite an incident for. **The inverse case is unhandled: four incidents and
still no rule, because each was fixed individually.** Candidate rule: when a defect class recurs,
promoting it to the instruction file is part of the fix.

**Also noted.** The skill's source repository moved three commits since the install. The layer
selector defect filed in the first batch is fixed. A new rule landed almost verbatim from a first
batch finding. **The version string is still the same despite the content change**, so an installed
copy goes stale by content drift under an unchanged version number, which is a different failure mode
from a missed bump and one the version assertion cannot detect.

---

## Source C: the environment-mismatch rule, five instances, one afternoon, two repositories

**Proposed rule: a check that runs in a different environment than the artifact it certifies is not
checking that artifact.** The collection already carries "'Installed' is not 'working'. Run the
thing." This is its sibling and is not covered by it: the thing was run, somewhere else, against
something else.

1. **A container definition omitted a file that central package management had just made
   load-bearing.** The local gate builds from the working tree, where the file is present, and stayed
   green. Production was unbuildable from the merge onward. Found by deploying.
2. **Nine real-database tests behind an environment variable and excluded from the gate.** Three had
   run once, five days earlier. Six had never run. One tool and two resources failed 100% of calls in
   front of a live tester while a 282-test suite reported green, because every one of those tests
   used a fake repository. **Corollary, separable and actionable on its own: an opt-in suite is a
   suite that does not exist.**
3. **The deploy script's own verifier printed OK and returned true immediately after the build
   failed**, because it checked a container it had not deployed: up 27 hours, three fixes behind. A
   green verdict on a failed deploy is worse than no verdict, and it is why the broken build survived
   an afternoon.
4. **In the sibling repository, a network-rebinding fix passed an independent zero-context review and
   still broke production**, because it did not distinguish the application's own internal hostname
   from a caller-supplied one.
5. **The cheapest form, one command long.** A diagnostic `curl -sS` without `-i` returned an empty
   body on a 401 and was read as "the endpoint returns nothing". An empty result and an auth failure
   were indistinguishable.

**Why instance 4 matters most.** The no-self-review rule is the control that failed there. It is not
wrong, it is insufficient, and `SKILL.md` currently reads as though isolating the reviewer's context
is the hard part. **Review confirms a change does what it claims. It does not confirm the claim was
right about the real system.** The missing clause: a reviewer cannot verify a claim about a running
system without touching the running system.

---

## Source D: post-adoption observation round, repository A, six days on

**Not a timed procedure run.** Ambient: six days of ordinary development under the adopted
conventions, no fresh adoption pass. The first round answered whether the procedure is followable.
This one answers whether anything from it was still visible six days later, unprompted.

**1. An advisory flag with zero call sites, replaced by a structural guarantee, verified by
deliberately breaking it.** A settings catalog carried a reserved-key-range redaction rule enforced
only by a flag every caller had to remember to check, with zero call sites and no test. Reading the
upstream source settled whether a narrower per-key rule could replace the range rule: the same
numeric key means an unrelated setting for one downstream consumer and an encrypted secret for
another, within the same reserved region of the same enum family, which rules out any allowlist
correction. **The guarantee moved from the flag into the type**: the only constructor path drops the
reserved data before the object exists. Two of six tests target the guarantee rather than today's
behaviour, one sweeping the entire reserved range against every known variant and one asserting by
reflection that no alternate constructor exists. **Verified by reverting the fix and confirming five
of six then failed.** This is the collection's "make each check fail on purpose", written for
documentation gates, independently reapplied to a security guarantee, unprompted.

**2. A validation attribute on a bound options type with no validation call wired to its binding**,
so nothing ever evaluated it. Decorative from the day it was written. A sibling integration in the
same repository did have the call. Found by an independent review with no prior context, not by any
of the repository's own gates. The collection already carries the rule this violates. **What is new
is the shape: a document-shaped claim sitting inside code**, an attribute rather than a comment or a
readme line, which is the shape none of that repository's existing checks are built to catch because
all of them are documentation checks.

**3. A worktree isolates file state, not an out-of-tree build cache.** Several concurrent, properly
worktree-isolated sessions found the combined build-and-test command writing into one machine-wide
cache directory regardless of which worktree invoked it. Concurrent runs clobbered each other
mid-build, producing a missing-manifest exception and phantom missing-namespace compiler errors,
**indistinguishable on screen from a real product defect**. One session spent real time investigating
a defect that did not exist. **A second session hit the same race and simply reran until it passed,
recorded as the worse outcome of the two, because it teaches retry-until-green instead of
investigation.** Fixed by keying the output path to a hash of the worktree's own filesystem path.
`TOOLING.md`'s existing guidance is about network and credential reach. This is a third axis, and it
only shows under genuine concurrency, which single-agent-at-a-time testing of a check command never
exercises.

**4. A second staleness data point, with a longer baseline.** The first round found a derived profile
going stale within hours under concurrent development. Here, a profile field written 2026-09-10
recorded a security property in prose: one shared static secret, no per-caller identity. A feature
shipped 2026-09-11 replaced that shared secret with named per-caller keys. **The profile field was
still uncorrected on 2026-09-16, five days later.** The same file had corrected a different stale
claim on the day it was written, so prompt correction is something this author does when looking is
triggered by something. **The gap is that nothing about the profile format prompts a look when the
property it describes changes. A profile is a snapshot with no subscription to the thing it
describes.** Hours in the first round, single-digit days here.

**What this round does not claim.** No defect-reduction claim anywhere. Findings 1 to 3 are evidence
that specific habits recurred without being asked for, six days after the adopting session ended.
Finding 4 is evidence about the profile mechanism's own maintenance cost. All four are single
observations in one repository by one author and carry the same discount the collection applied to
the first round.

---

## Where each item landed

| Item | Landed as |
|---|---|
| A2 annotation collision | `PROFILE.md`: the annotation rule is scoped out of profiles and a correction is capped at one dated line |
| A3 pre-filled template | **Error 32.** `templates/profile.yml` blanked, `derived` and `commits_at_derivation` added to the schema |
| A4 hook install pattern | **Error 33.** `templates/pre-push` rewritten to the tracked-hooks and `core.hooksPath` pattern |
| A5 `SOLO.md` asymmetry | `SKILL.md` companion table says which file carries the substance; `SOLO.md`'s false third bullet corrected and two cited failure modes added |
| A6 adoption unreachable | **Error 35.** One row in the companion table |
| A7 missing schema slots | `disclosure` and `stack.docs_check` added to the schema and template; `DOCS.md` names the slot |
| A8 nowhere to record a decline | `declined:` block added to the schema and template; `ADOPTION.md` step 5 records into it |
| A9 no validator | **Error 34.** `templates/validate_profile.py` ships; `ADOPTION.md` phase 1 ends by running it |
| A10 maturity and licence wording | Corrected in both files to a single reading |
| A11 POSIX table | Extended to sections 3 and 5 |
| A12 sibling repositories | `DOCS.md` gains a fifth displacement target, counted consistently in four files; `PROFILE.md` gains the same; `ADOPTION.md` forbids copying a convention wholesale from a sibling; the validator's `--cite` catches the field-name half |
| A13 `EVIDENCE.md` register | `PROFILE.md` says a profile cites the repository's own commands, not the skill's findings |
| A stale citation | `PROFILE.md`: when a field changes, re-check the documents that field cites |
| B Gap 1 parallel merges | `SKILL.md` Layer 1, working with agents |
| B Gap 2 and D3 build output | `TOOLING.md`, as two instances in two repositories |
| B Corroboration 1 compound idiom | `SKILL.md` Layer 1, extending the existing push rule |
| B Gap 3 recurrence | `SKILL.md` Layer 1, instruction files |
| B version drift | **Error 36.** Version bumped; `ADOPTION.md` says what the version assertion cannot tell you |
| C1 to C5 environment mismatch | `SKILL.md` Layer 1, verifying a claim, with the opt-in corollary stated separately |
| C4 review clause | `SKILL.md` Layer 1, working with agents |
| D1 structural guarantee | `SECURITY.md` |
| D2 decorative attribute | `SECURITY.md`, as a second occurrence with the new shape named |
| D4 staleness | `PROFILE.md` |

## Pre-registration for the rules this batch adds

**Required by `AGENTS.md` and committed alongside the change, not after.** Short, because the honest
version is short: this repository has no runnable artifact whose lift can be measured, and most of
the borrowed measurement apparatus does not transfer, which is recorded at
`.agents/sota-method-2026-09-09.md`. What follows is a threshold stated in advance so the next batch
cannot be read as confirmation after the fact.

**What these rules are expected to change.** A third adoption run should report the environment
question ("what did the green result run against") and the parallel-merge question ("did anything
else land in another worktree") **unprompted**, and should not report the four schema gaps, the
template pre-fill, the hook install pattern or the unreachable procedure at all, because those are
fixed rather than advised.

**What would show they did not help, stated as a threshold that will not move:**

- **The environment rule fails** if a third run's log contains a green-gate claim with no statement
  of the environment it ran in. One occurrence is enough. The rule is one sentence long and either it
  is reachable at the moment of writing the claim or it is decoration.
- **The validator fails** if a third run writes a profile that it does not run the validator against,
  or if the validator reports clean on a profile that a human then finds malformed. Either one means
  the instrument is in the wrong place or checks the wrong half.
- **`declined:` fails** if a third run still writes an imperative sentence into a profile. That is the
  specific behaviour it was built to remove and it is greppable.
- **The batch as a whole fails** if a third run's findings are again dominated by schema and template
  defects. That would mean this batch fixed instances rather than the class, which is precisely the
  failure the new recurrence rule names.

**How this could fail to measure anything, listed now so it cannot be discovered later as an
explanation:**

- **Both repositories so far are the author's own, one toolchain family, and they copy conventions
  from each other.** A finding replicated across them may be one repository's finding twice. The
  second run demonstrated the mechanism: an error propagated between the two by a wholesale copy.
- **A third run will be performed by an agent that can read this file.** Anything it reports as
  unprompted may be prompted by the collection having grown a section about it. There is no clean way
  to blind this and no claim here should be read as though there were.
- **Absence of a finding is not evidence the rule worked.** A run that does not report the
  environment question may have had no green result worth doubting. Count the opportunities, not the
  reports.
- **Nothing here has a sample size.** Every threshold above is one run against one run.

## Filed and deliberately not acted on

**B Corroborations 2 and 3 produce no rule and are recorded as evidence only.** Both report that an
existing rule worked. "Instruct the reviewer to disagree, bounded" already carries the bounding
clause, and it already records the vendor's opposing caution, so a first-party confirmation adds a
data point and changes no instruction. Same for "delete superseded rules rather than annotating
them". **Writing either up as a new rule would be the failure the collection's own test names:
growing the apparatus that justifies a rule rather than producing one.** The one thing corroboration
2 does contribute is the observation that the bound is the load-bearing half, which the existing rule
already says, so it stays where it is.

**A7's merge-strategy slot is not added to the schema.** The finding groups three missing fields.
Two of them, the disclosure decision and the doc-check command, are decisions an agent needs to read
before it acts and were being made silently. The third is different: `WORKFLOW.md` asks for one merge
strategy written down, and a repository that has one has it in its host configuration or its
contributing file, where it is enforceable. **A profile field would be a second copy of a fact that
already has a home, and a copy that cannot be enforced is a copy that goes stale.** This is the
`setup` reasoning inverted: `setup` is in the profile because it has nowhere else to live.

**The proposal to replace `PROFILE.md`'s derivation pipelines with a `derive_profile.py` is not
done.** The translation table is extended instead. The script is the better fix and the finding is
right that `PROFILE.md` proposes it and does not follow through, but a derivation script has to run
in the adopting repository against an unknown shell, an unknown git version and an unknown harness
guard, and this batch contains a live instance of a harness refusing composed pipelines as too
complex to verify. **Shipping an unproven script in place of documented commands would replace a
known friction with an unknown one**, and the validator shipped in this batch is the piece that can
be proved correct against a file rather than against an environment. Recorded as open.

**The harness guard that refused composed pipelines is not actionable here.** It is vendor mechanics,
which is permanently out of scope, and the collection cannot write a rule about another tool's
verification heuristics. What is in scope is the consequence, which is that a derivation procedure
should not depend on composition, and that is what the extended table and the flattened commands
address.

**A13's stronger form is not adopted.** The finding offers two fixes: make profiles cite the
repository's own commands, or have `PROFILE.md` say so explicitly. Both were available. The second is
taken. Rewriting how the evidence document is referenced across the collection is a larger change
than this finding supports, and the shipped rule ("a profile cites what you ran, not what the skill
concluded") is the part an engineer can act on.

**Source A's withdrawn items 1 and the "Profile check" section are recorded and not acted on**, per
the preamble above. They described a state that the merge had already corrected. Recording the
withdrawal is the point: the run's other items are not weakened by it, and a batch that quietly
dropped them would hide that a stale worktree can generate confident findings about a branch it
cannot see.
