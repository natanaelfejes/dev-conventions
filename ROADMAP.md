# Roadmap

What is open, ordered by how much it changes the collection's standing rather than by effort. Written 2026-09-04, updated 2026-09-06 at version 0.9.0.

**This file is deliberately volatile.** When something ships it moves to `CHANGELOG.md` rather than
staying here marked done, because a roadmap that accumulates completed work stops being readable as a
list of what is left.

---

## The 1.0 gate, and nothing else substitutes for it

**Somebody who is not the author has to use this on a repository nobody here has seen.**

That is the whole gate. Three profiles now exist and **all three were derived by one person**, which
tests the document and not whether the procedure is followable. `PROFILE.md`'s seven-step derivation
was written by doing it twice; whether it survives a stranger is unknown.

Concretely, 1.0 requires:

- Two adoptions by someone else, on repositories the author has never opened.
- A written report of where the procedure was unclear or wrong.
- One install on a machine that is not the authoring machine.

**Do not bump to 1.0 for content reasons.** More sources, more files and more verification passes do
not close this. Only usage does.

## Open, and worth doing next

### 1. Read the original 2006 code review study

`WORKFLOW.md` carries a **contested headline**: whether the popular "pull requests under 400 lines"
rule misreads that study by turning a review rate into a batch size. Two independent verification
passes read its secondary sources and extracted materially different numbers, so the claim is
currently withdrawn to "no threshold from it is safe to cite".

**Reading the original book settles it**, and it is one library request. Whichever way it resolves is
publishable: either the popular rule is folklore, or this collection was wrong about it and says so.

### 2. Make it citable

`RESEARCH.md` establishes that `CITATION.cff` plus an archival-repository DOI is mature and
adoptable today, and that it satisfies the same bar artifact-evaluation tracks apply. A `CITATION.cff`
exists in this repository; **the DOI does not**.

Without a version-pinnable DOI, this collection asks consumers to pin a version while offering no
citable identifier for one. That is a rule it does not follow itself.

### 3. Reach the four sources the verification pass could not

`RESEARCH.md` has now been verified and the pass found one contradicted headline, recorded in
`CHANGELOG.md` 0.9.0. Four items it could not reach are the remainder, and each is named in the file
with a status rather than asserted:

- **Fedora and Rocky Linux** AI-contribution policies. Only secondary aggregators were seen.
- **The OpenTelemetry primary CONTRIBUTING document**, and the Linux kernel's own
  `coding-assistants.rst`, to confirm the exact trailer spec against the file rather than against
  agreeing secondary quotations.
- **The citation-difference study**, which was not located at all. Its figure is withdrawn.
- **DBLP and the publisher indexes**, to resolve the contested venue status of arXiv:2608.18167 and
  the venue fields for three preprints.

The last one needs institutional access rather than effort.

### 4. The templates were audited and one carried an unsourced claim

**Done 2026-09-06.** `templates/AGENTS.md` stated a measured finding about repository overviews as
though it measured directory trees. Recorded as error 18 and corrected by scoping.
`templates/pull_request.md` came through with one low-severity flag: a first-party observation that
reads as a general claim, acceptable once labelled.

This item is closed, and the lesson is that naming a risk on a roadmap does not retire it. These
were listed as the likeliest place an unsupported claim was sitting, for days, correctly.

### 5. Publication route

**Half done as of 2026-09-04.** The repository is on a code host, private, with a
`.claude-plugin/marketplace.json` that matches the published schema. The first one written did not
and would have failed to resolve while every local check passed.

**No longer blocked.** The clearance question is gone because the material that needed clearing is
gone: every observation drawn from a repository the author did not personally own was withdrawn from
the evidence base on 2026-09-06, deliberately and at a stated cost. The collection now rests only on
repositories its author owns and on published sources.

Note what the first publication attempt cost, because it bears on how carefully the remaining steps
should be taken: every commit carried an employer email address, which no check examined. That is
error 17, and its lesson applies directly to the withdrawal above. **Removing text in a commit does
not remove it from the repository**, so the withdrawal is only complete once history no longer
carries it.

**Sequence, in order:** confirm history is clean, then public, then an archival-repository DOI
against a tagged release, then that DOI into `CITATION.cff`.

## Known weaknesses, stated so nobody rediscovers them as news

- **The first-party base is four small repositories and one observer.** Nothing is observed at
  organisational scale, and no amount of writing fixes either the size or the single observer. Only
  somebody else's repository does.
- **Nothing has been measured against a control.** One peer-reviewed controlled experiment now exists
  on the adjacent question of downstream maintainability, which narrows this but does not close it.
- **Most 2026 sources are preprints.** That reflects the field rather than the search, and it means
  the most current claims rest on unreviewed work. Six peer-reviewed sources now exist against
  nineteen identified papers.
- **Four items are contested between verification passes.** Recorded in `EVIDENCE.md`. One of them
  undercuts a headline.
- **`RESEARCH.md` and `TOOLING.md` are single-pass.** `TOOLING.md` at least frames itself as a dated
  map rather than a finding.

## Deliberately not doing

Recorded because each has been proposed more than once:

- **Product rankings** of harnesses, models or subscriptions. See `AGENTS.md` for why.
- **Curated recommended-skill or recommended-server lists.** They would contradict `SECURITY.md`.
- **Vendor-specific mechanics.** Hook syntax and command file formats are vendor-documented.
- **Any observation drawn from a repository the author does not own.** Withdrawn entirely on
  2026-09-06 rather than de-identified further. Two reasons, and the second is the load-bearing one:
  such an observation is attributable to the author by employment however well it is rounded, and it
  is unflattering about people who did not agree to be studied. The evidence base is narrower for it
  and the narrowing is stated wherever the base is described.

## Maintenance cadence

From `SKILL.md`, restated here because a cadence nobody schedules does not happen:

- **Quarterly**: recheck the administrative facts as a unit, re-search the open gaps, recheck
  anything sitting at tier 3.
- **Faster than quarterly for `SECURITY.md`**, which cites CVEs and active campaigns and moves on a
  different clock.
- **Every edit**: trace any new number to the source's own words, and bump the version and recheck
  date.

**A stale entry in the administrative-facts section counts as a defect**, not as background. That is
the standard this collection applies to everyone else.
