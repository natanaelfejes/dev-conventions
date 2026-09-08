# Team repositories

**Load this when the profile says `team: 2` or more.** Split out of `SKILL.md` on 2026-09-08: this
and `SOLO.md` are mutually exclusive by the profile's own rule, and both were loading on every
session.

**Provenance: mixed.** Disclosure is tier 2 and agent-only review is tier 2, both confirmed against
publisher records. Policy prevalence is tier 2 on a vision-track short paper. The rest is
`first-party` from two team contexts, neither of them an engineering organisation, and that is a
small and unrepresentative base for advice about teams.

Grounded in two first-party team contexts: a two-person repository with 51 changes of history, and a
six-person student project with 254 commits, a full chat archive, and two independent audits of the
repository it produced. Where a claim is first-party it says so; the external claims here are tier 2
and tier 4, and which is which is stated at each one.

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
- **Do not invent your own disclosure convention, and do not assume there is one to copy.** There
  are **two camps and an abstainer**, verified project by project against each project's own page:
  the Linux kernel, Fedora, Rocky Linux and Zephyr use **`Assisted-by:`**; the Apache Software
  Foundation and OpenInfra use **`Generated-by:`**; OpenTelemetry prescribes **no trailer at all**
  and describes assistance levels instead. **Tier 5, vendor and project self-reported**, each
  confirmed against a primary page. `RESEARCH.md` carries the table and the verification status of
  every row.

  What is genuinely converged is the **structure**, not the token: disclose the assistance, and never
  in a field that certifies authorship. The kernel states that AI agents **MUST NOT** add
  `Signed-off-by`, and Zephyr gives the reason, that only a human can certify the DCO.

  **So copy your own ecosystem's convention and check which camp it is in.** An earlier version of
  this rule said seven projects had converged on `Assisted-by:`. That was wrong about the Apache
  Software Foundation and wrong about OpenTelemetry, and it named two projects nobody here had
  verified. See error 21.
- **Do not assume the project has no position.** A survey of 1,000 repositories found 118 carrying an
  explicit AI policy, and of those, **78% permit AI contributions, 51% require disclosure and 74%
  require a human in the loop**. Tier 4: recorded as accepted at a reviewed venue until 2026-09-07,
  when no venue record could be found for it. So the common case is still no
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

