# Roadmap

What is open, ordered by how much it changes the collection's standing rather than by effort. Written 2026-09-04, updated 2026-09-06 at version 0.9.0.

**This file is deliberately volatile.** When something ships it moves to `CHANGELOG.md` rather than
staying here marked done, because a roadmap that accumulates completed work stops being readable as a
list of what is left.

---

## Release gates, and there are two of them

**Split 2026-09-08 after an external evaluation identified one gate over two artifacts as the reason
nothing had shipped in five versions.** The gate below was written when the skill and the evidence
were one thing. They are not, and they fail in different ways, so they release on different
conditions.

### The skill: gated on adoption, and nothing substitutes for it

**Somebody who is not the author has to use this on a repository nobody here has seen.**

That is the whole gate. Three profiles now exist and **all three were derived by one person**, which
tests the document and not whether the procedure is followable. `PROFILE.md`'s seven-step derivation
was written by doing it twice; whether it survives a stranger is unknown.

Concretely, 1.0 of the skill requires:

- Two adoptions by someone else, on repositories the author has never opened.
- A written report of where the procedure was unclear or wrong.
- One install on a machine that is not the authoring machine.

**Do not bump the skill to 1.0 for content reasons.** More sources, more files and more verification
passes do not close this. Only usage does.

**Why this artifact and not the other one:** the skill is a **procedure strangers execute**. Its
failure mode is a step that made sense to the person who wrote it and does not survive contact with
somebody who does not already know what it meant. That defect is invisible from inside and no amount
of reading finds it. Only a stranger running it does.

### The evidence document: not gated on adoption at all

**`EVIDENCE.md` and anything drawn from it ship when they are correct, not when somebody adopts
them.** Its audience is readers, not adopters. **A review of published sources is not made more or
less true by whether anyone installed a skill**, and gating it on adoption is a category error that
cost five versions.

Its release conditions are its own, and they are about the claims rather than about usage:

- Every claim carries a tier, and every tier-2 rating cites a venue record that is not a surface the
  authors control. **Held as of 0.14.1**, eight papers, checked by the build.
- Every figure has been seen in its primary source by whoever wrote the sentence, and where it has
  not, the sentence says so. **Two open items**, both labelled in the document.
- The errors list is current and the outside-checks table names what each check cost.

**Anything drawn from it is gated on even less.** The venue audit, that four of nine tier-2 ratings
failed a check against records the authors do not control, is a finding **about the field's evidence
base** rather than about this repository. It is checkable by anyone in an afternoon, it implicates
every artifact that cites a 2026 preprint as though it were reviewed, and it needs no adoption, no
1.0 and nobody's permission.

### Why one gate over both was wrong, recorded so it is not re-merged

The two artifacts have **opposite dependencies**. The skill depends on a stranger, which the author
cannot supply alone. The evidence depends on the sources being right, which is entirely within the
author's control and is already met. Holding the second behind the first meant the half that was
ready waited on the half that could not move, in a field where the sources go stale in quarters.

**The observable cost:** five versions, seven verification passes, one external audit, zero
publications. The passes were not the problem. **The gate was**, and it was gating the wrong thing.

## Open, and worth doing next

### 0. Stop releasing, and the count is the argument

**Sixteen versions in six days.** An outside reader put the point plainly: the marginal return went
negative somewhere around 0.11, and every release since has been a correction to a release rather
than a new capability. **That is not a productivity signal, it is a defect-discovery rate**, and it
is high because the artifact keeps changing rather than because the checking keeps improving.

**Freeze the version.** The next bump should be caused by an adoption run finding something, not by a
verification pass finding something.

**Condition met, 2026-09-10.** The first adoption run happened and found error 30, a defect that had
made the skill's entire solo/team split inoperative in every repository since 0.14.0, silently, and
that nine reading passes had missed. Nine further friction items followed. **So the next version
bump is now earned by the terms of this entry**, and it is the first one in seventeen that is. What
the entry asked for was never "stop releasing"; it was "stop releasing on the strength of
re-reading your own artifact". Corrections that are genuinely blocking still ship, and this
entry exists so that "genuinely blocking" has to be argued rather than assumed.

**What this does not mean.** It does not mean stop fixing defects: a false claim in an agent-facing
file ships as soon as it is found, and three of the last four releases were exactly that. It means
stop *generating* work by re-examining an artifact nobody outside has used.

### 1. Adopt it somewhere, and stop researching. DONE 2026-09-10, and it paid immediately

**Nine verification passes and two outside audits ran before the first adoption did.** Every one
generated evidence entries, changelog entries and error entries. Not one generated a rule. The
collection got much better at proving itself and no better at telling anyone what to do.

**The first adoption run produced ten actionable findings in about sixteen minutes**, one of which
had made the skill's entire solo/team split inoperative in every repository, silently, for two days,
and had been read past by everything else. See `.agents/adoption-friction-2026-09-10.md` and error
30.

**Keep this entry rather than ticking it, because one run is not a practice.** What it established
is that reading and running find different classes of defect, on a sample of one repository, one
agent, one pass. The second adoption is worth more than the first was: it is the one that says
whether these ten findings were about the collection or about that repository.

**What the next adoption should do differently**, from this one's own log: derive an existing
profile independently before diffing it, check the branch before every commit, and expect
re-adoption rather than greenfield if any gate is already present.

### 2. Make it citable

`RESEARCH.md` establishes that `CITATION.cff` plus an archival-repository DOI is mature and
adoptable today, and that it satisfies the same bar artifact-evaluation tracks apply. A `CITATION.cff`
exists in this repository; **the DOI does not**.

Without a version-pinnable DOI, this collection asks consumers to pin a version while offering no
citable identifier for one. That is a rule it does not follow itself.

**The DOI belongs to the evidence document, and that is what unblocks it.** `EVIDENCE.md` is the
citable artifact: a review of sources, versioned, with an errors list. **It is not gated on adoption**
per the split above, so this item is actionable now rather than after a stranger runs `ADOPTION.md`.
The skill can carry the same identifier later or its own; nothing about the skill blocks this.

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

**Two sequences now, since the gates split.** The evidence document runs the whole sequence above on
its own schedule and is blocked only on the repository going public. The skill runs it after the
adoption gate. **They were one sequence and that is why neither had started.**

### 6. The monthly adjudication session, and it is blocked on item 1 by design

**The watcher searches. This decides.** `sources.yml` and the workflow answer "what moved" and are
deliberately incapable of answering "does it matter". That second question is the one that costs the
author time, and it is the whole of the friction this collection exists to reduce.

**The shape, agreed 2026-09-10.** A scheduled cloud session, once a month on a fixed day, roughly
thirty minutes. It opens the watcher's issue for that month, reads it, and produces a
recommendation. It is a reasoning session rather than a script, so it may evaluate and it may
propose. It may not merge.

**What it evaluates.** The drift report, the venue re-checks, the gap surveillance, and the tracked
comparables: whether anything published since the last run is worth adopting, at what tier, and
against which existing rule. That includes the most-starred collections and the respected individual
writers, read as **signal about where attention is going**, never as content to absorb. See
"Deliberately not doing" for why that distinction is load-bearing rather than fussy.

**What it may never do**, and each of these is a recorded error rather than a precaution:

- **Merge anything.** It opens a pull request or comments on the issue. A human approves. Four of nine
  tier-2 ratings were wrong when this collection assigned them to itself unreviewed, and evidence
  scales have inter-rater agreement around kappa 0.27, so an unreviewed tier is the least reliable
  step in the whole method to automate.
- **Change a tier or retire a rule unattended.** The asymmetric-burden rule already forbids a weak
  source retiring a safeguard. An unattended session is a weak source about its own reach.
- **Treat an unreachable source as an absent one.** Four recorded errors come from exactly this, and a
  scheduled session is a restricted environment by definition. The first live watcher run reached 2
  of 21 sources in one environment and 20 of 21 in another. **A run must lead with its reach**, and a
  run that reached half its sources is not a clean run, it is an unusable one.
- **Withdraw a claim.** Error 23: a withdrawal needs the same primary-source standard as an assertion,
  and a session that cannot open the primary cannot meet it.

**Why it waits for item 1.** Building this before the first adoption repeats the pattern that has held
for sixteen versions: the apparatus grows because apparatus is where work is legible, and the
adoption does not. It is also the cheaper order. The friction log will say which categories actually
cost time in practice, and this session should watch those rather than the ones that seem important
from inside.

**What it is honestly worth.** Continuous ad-hoc research becomes about thirty minutes a month of
reading one report and approving or rejecting a short list. That is most of the goal and it is not
all of it. **It is not zero, and no version of this is zero**, for the reason recorded under known
weaknesses.

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
- **The goal this collection is built toward contains a contradiction, and no amount of engineering
  resolves it.** Recorded 2026-09-10 after it was proposed for the third time, so that the next
  proposal is answered rather than rebuilt.

  The stated want has two halves: **every claim carries the strength of its evidence**, and **the
  collection keeps itself current by absorbing the best of what the most-starred collections
  publish**. Those are mutually exclusive. The most-starred collections grade nothing: 283,707 stars
  and zero academic citations, 92,967 and one informal citation, both verified 2026-09-08 and
  2026-09-09. Absorbing them means importing unmarked claims, and a collection that does that has
  stopped being evidence-graded and become a rules file with a scale attached.

  **The grading cannot be automated away because the grading is the product.** Everything else here
  is available free and better maintained elsewhere, which the coverage estimate above puts at three
  quarters to four fifths.

  The adjacent want, **stop researching entirely**, is not available either. Eight outside checks,
  eight found something, and the eighth found the worst entry on the list. A field with that error
  curve has no static answer to cache. **What is available is roughly thirty minutes a month**, which
  is most of the friction gone and is not none of it. Item 6 is that, and it is deliberately not more.

  **And the collection cannot be certified as the best**, which was the third form of the request.
  That requires a controlled comparison, nothing here has one, and `martinholovsky/SOTA-skills` is
  ahead on exactly that axis. Error 27 exists because a previous version implied otherwise. A
  collection built to refuse unsupported superlatives cannot issue one about itself.
- **The reputation competitor publishes faster than this collection can recheck, and says so.**
  Verified 2026-09-09 from an environment that could reach the page. Simon Willison's agentic
  engineering pattern series states that each chapter is "effectively a blog post with a less
  prominent date that's designed to be updated over time, not frozen", and that he hopes "to add more
  chapters at a rate of 1-2 a week". **That is a cadence a quarterly refresh cannot match**, from
  someone who is already the default citation in this space. Combined with first-party vendor
  guidance, a second landscape pass puts coverage of the categories this collection names at roughly
  **three quarters to four fifths**. What is left is what neither has an incentive to publish: the
  strength marking, the disagreements left standing, the profile conditioning, and any finding that
  makes a vendor look bad.

  **A false negative was nearly published on this exact point**, and it is worth recording because it
  is this collection's own rule demonstrating itself. The pass first fetched the guide's index, found
  no cadence statement, and was about to report it unconfirmed. The quote is in a chapter, not the
  index. **A search that reaches the wrong page is indistinguishable from a true absence.**

- **Direct prior art for the evidence-grading thesis exists, and this collection did not find it in
  eight passes.** A second landscape pass, 2026-09-09, reports **arXiv:2608.13867** (Jarmak, 14 August
  2026, 314 pages) as carrying a **versioned catalog of 206 reliability records and an evidence
  ledger**. If that description holds, it is not adjacent work and it is not a thematic analysis of a
  corpus, which is what the nearest previously-known item was. It is the thing this collection
  believes itself to be doing, done at a scale this collection is not close to.

  **Confirmed 2026-09-09 from an environment that could reach arXiv**, after being provisional here
  for one day. Stephanie Jarmak, submitted 14 August 2026. Verbatim from the abstract: **"a versioned
  catalog of 206 reliability records: 193 gated practices"**, "an evidence ledger", "limits on
  evidence-grading claims", and **"164 scholarly works, 100 practitioner records"**. The Comments
  field gives 314 pages and a public companion repository, **`sjarmak/engineering-reliable-coding-agents`**,
  created 2026-08-05, last pushed 2026-08-24, **10 stars and one fork**.

  **Note what resolved and what that says about the method.** The 206 and the 193 are not competing
  figures: 206 reliability records **of which** 193 are gated practices. Two reports of the same
  abstract looked like a discrepancy and were not, which is why a number is quoted with its
  surrounding clause rather than alone. And this entry sat provisional for exactly one day because a
  different environment could reach the page. **A blocked network is not a finding**, demonstrated
  again.

- **The pair of numbers below is the finding, and it bears on the publication plan more than the
  paper does.**

  | Artifact | Stars | Retrieved |
  |---|---|---|
  | The Jarmak companion repository | **10** | GitHub REST API, 2026-09-09, confirmed here |
  | `obra/superpowers` | **283,707** | GitHub REST API, 2026-09-09, confirmed here |

  **A second datapoint, 2026-09-09, in the same direction.** `martinholovsky/SOTA-skills`, the most
  methodologically rigorous artifact found anywhere in three landscape passes, with control arms,
  published nulls, a retraction and negative-control CI, has **18 stars**, confirmed against the
  GitHub API. Two independent rigorous projects, 10 and 18. **This is no longer an anecdote.**

  **In this market rigor and distribution are inversely correlated, and the ratio is roughly
  28,000 to 1.** The most rigorous artifact found in two landscape passes has an audience of
  approximately nobody. The most distributed one, cloned and grepped on 2026-09-08, carries **one
  informal academic citation across 94 markdown files** and no confidence marking of any kind.

  Three things follow, and none of them is "so do not bother":

  - **Rigor is not a distribution strategy.** Anyone planning to publish this on the strength of
    being more careful than the alternatives should read those two numbers first. Careful is not
    what gets installed.
  - **It does not follow that the rigor is worthless.** It follows that the rigor and the reach are
    **different products with different audiences**, which is the same conclusion the gate split
    above reached from the other direction, arrived at independently. The evidence document competes
    with the 10, and it competes on being right. The skill competes with the 283,707, and it does not
    compete on completeness.
  - **The comparison needs a timestamp, not a date.** The pass read 283,183 and this session read
    **283,707 the same day**, a drift of 524 in hours. `EVIDENCE.md` keeps administrative facts in
    one section precisely because they rot; a figure that moves that fast is one nobody should quote
    without saying when they looked.
- **`TOOLING.md`, `OBSERVABILITY.md`, `DOCS.md` and `VOCABULARY.md` are single-pass**, and only two
  of them say so. `RESEARCH.md` is no longer single-pass and states its verification prominently,
  which is the model the other four should follow. `TOOLING.md` frames itself as a dated map, which
  is not the same as saying its claims were never checked against primary sources.
  **`OBSERVABILITY.md` has no file-level sourcing statement at all**, unlike every other rule file.

## Deliberately not doing

Recorded because each has been proposed more than once:

- **Product rankings** of harnesses, models or subscriptions. See `AGENTS.md` for why.
- **Curated recommended-skill or recommended-server lists.** They would contradict `SECURITY.md`.
- **Ingesting content from collections that cite nothing**, however popular. Verified 2026-09-08 and
  2026-09-09: `obra/superpowers` carries **283,707 stars and zero academic citations** across its
  corpus, `addyosmani/agent-skills` **92,967 and one informal citation**, and neither marks confidence
  on any claim. Absorbing their rules would import unmarked assertions into a collection whose entire
  argument is that a claim carries the strength of its evidence. That is error 14's shape, at scale
  and on purpose. **They are tracked in `sources.yml` as a signal source and never as a content
  source**: that a popular collection added a rule is a research lead, not a claim.
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
