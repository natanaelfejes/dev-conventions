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

### 1. Adopt it somewhere, and stop researching

**This is now the only item that matters and it has been the only item that matters for five
versions.** Six verification passes and one external audit have run. Zero adoptions. Every one of
those passes generated evidence entries, changelog entries and error entries, and not one of them
generated a rule. The collection has got much better at proving itself and no better at telling
anyone what to do.

The 1.0 gate below says the same thing in stronger terms. This entry exists because the gate is easy
to read as a distant milestone, and the actual instruction is immediate: **run `ADOPTION.md` against
a repository, in anger, and record where it was wrong.**

### 2. Make it citable

`RESEARCH.md` establishes that `CITATION.cff` plus an archival-repository DOI is mature and
adoptable today, and that it satisfies the same bar artifact-evaluation tracks apply. A `CITATION.cff`
exists in this repository; **the DOI does not**.

Without a version-pinnable DOI, this collection asks consumers to pin a version while offering no
citable identifier for one. That is a rule it does not follow itself.

### 3. Reach the sources no pass could reach

**Mostly closed 2026-09-08**, when the sources were downloaded by hand and read. What that produced
is in `CHANGELOG.md` 0.12.0: three tier restorations, the 2006 book settled, two invented figures
found, and one withdrawal reversed.

**What that leaves, and it is the useful residue:**

- **The citation-difference study** was located at 0.10.0 and this entry went on asking for it. A
  stale request on a roadmap costs somebody an afternoon.
- **DBLP remains unreachable** behind an anti-bot interstitial, from every environment tried. It has
  not mattered yet, because venue programmes and OpenReview answered every question DBLP would have.
- **The lesson is about the environment rather than the sources.** Four of this collection's recorded
  errors trace to a network-restricted session treating "could not reach" as a result: three
  downgrades that were wrong, and one withdrawal that was wrong. **A blocked network is not a
  finding**, and the fix is not a better search, it is a human with a browser.

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
  the most current claims rest on unreviewed work. **Eight papers now carry a confirmed venue record
  against roughly thirty identified**, and three of those eight are in the lightest categories their
  venues run: a workshop poster, a vision-track short paper and a short-paper talk.
- **Four items are contested between verification passes.** Recorded in `EVIDENCE.md`. One of them
  undercuts a headline.
- **`TOOLING.md`, `OBSERVABILITY.md`, `DOCS.md` and `VOCABULARY.md` are single-pass**, and only two
  of them say so. `RESEARCH.md` is no longer single-pass and states its verification prominently,
  which is the model the other four should follow. `TOOLING.md` frames itself as a dated map, which
  is not the same as saying its claims were never checked against primary sources.
  **`OBSERVABILITY.md` has no file-level sourcing statement at all**, unlike every other rule file.

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
