# Evidence

Every claim in this skill, with its tier, its source, and what could not be verified. Read this when
a rule is challenged. **Compiled 2026-09-01, venue checks completed 2026-09-02.**

## The tier scale

> **A tier is not a correctness score, and the numbering will mislead you if you let it.** It records
> **how much scrutiny a claim has survived**, which is correlated with being right and is not the
> same thing. A tier-4 preprint can be correct; a tier-2 paper can be wrong, because peer review
> catches method errors rather than all errors. A lower number means *more people have checked*,
> never *more true*.
>
> The warning is here because numbering does rhetorical work no disclaimer undoes: a reader who skims
> reads "tier 2" as "truer than tier 4" whatever the surrounding prose says. **Use a tier to decide
> how hard to push back on a claim, not to decide whether it is true.** Added 2026-09-03 after an
> external review named exactly this failure.

Ordered by **review trail**, not by whether numbers exist. That ordering is the point: a
seven-author study with public code and 5,000 runs and a single-author self-published preprint both
produce numbers, and collapsing them into one "measured" bucket is what let a weak source be used to
retire a practice.

| Tier | Name | Means |
|---|---|---|
| 1 | Replicated | Independent groups, consistent direction. **States its review status separately**, see below |
| 2 | Reviewed | Peer-reviewed and accepted, confirmed against the venue or a publisher DOI |
| 3 | Under review | Multi-author, public code or data, submitted to a reviewed venue, decision not confirmed |
| 4 | Preprint | Methodology and numbers exist, no review trail, possibly self-published |
| 5 | Vendor-disclosed | A company's own instrumentation or security research, evaluation not independently published |
| 6 | Analyst-forecast | A research firm's survey-based projection. A forecast, not an observed outcome |
| 7 | Practitioner judgment | Named, credible individual, no comparison arm |
| 8 | Unverifiable | Circulates, no primary source traceable |

### A tier is a rater's judgment, not a property of the source

**Added 2026-09-06, and it is the sharpest external criticism this scale has received.** A
verification pass went looking for what is known about evidence hierarchies *as instruments*, in the
one field that has run the experiment for three decades. The finding bears directly on this scale.

**Grading schemes have measurably poor inter-rater reliability.** An early GRADE working-group
reliability test found agreement among raters across twelve outcomes at only "fair", kappa around
0.27, ranging from **worse than chance for four outcomes** up to 0.82 for one. A separate study
applying GRADE in practice found reliability from "slight" (kappa 0.18 for precision) to "almost
perfect" (0.84 for consistency), with overall quality-of-evidence agreement "slight" in one review
and "moderate" in another.

Those are trained people, applying a mature and heavily documented scheme, to the same evidence, and
disagreeing at rates that are themselves only fair. **This scale is younger, less documented, and has
been applied by one person.** There is no reason to think it does better and every reason to think
it does worse.

What follows from that, and what does not:

- **A tier is a judgment made by whoever assigned it, with known disagreement between raters.** It is
  not a measured attribute of the source. The scale header already says a tier is not a correctness
  score; this is the stronger and better-sourced version of the same warning, and it was missing.
- **Two people applying this scale to the same paper will sometimes differ, and neither is
  necessarily wrong.** If you disagree with a tier here, that is an ordinary outcome rather than a
  bug report, though it is still worth raising.
- **It strengthens the asymmetric-burden rule rather than weakening it.** If grades are noisy, a rule
  that forbids acting on a weak grade to *remove* a safeguard is doing more work, not less.
- **It does not invalidate the scale.** The critique literature's own conclusion is that hierarchies
  are useful and oversold, not that they are useless. Related known criticisms, which apply here too:
  hierarchies conflate study design with study quality, and they systematically under-rate
  observational evidence in domains where randomisation is infeasible, which is exactly this domain.

**One further finding worth recording because it explains an absence.** Evidence-based software
engineering launched as a movement in 2004 and its systematic-review half took hold while its
grading-and-appraisal half largely did not. Its own retrospectives cite missing infrastructure, the
cost of systematic reviews, and vulnerability to experimenter bias. So a practitioner collection
attempting evidence grading in this field is not filling an obvious gap that everybody missed; it is
attempting something the field tried and mostly abandoned. That is a reason for humility about the
instrument, not a reason to drop it.

**Tier 1 is not simply tier 2 plus a replication, and treating it that way was a defect in this
scale.** Corrected 2026-09-03 when the first tier-1 entry turned out to be two independent preprints.
Replication and review are orthogonal: one says other people got the same answer, the other says
reviewers scrutinised the method. Neither implies the other, and for deciding whether to act on a
finding, convergence is usually the more informative of the two. So a tier-1 entry always names its
review status rather than leaving it inferred from the number 1.

### The closest thing to this collection is not a paper, it is a live repository, and it measures

**Found 2026-09-09 in a third landscape pass, missed by the two before it, and verified here by
cloning the repository rather than reading its README.** `martinholovsky/SOTA-skills`, created
2026-06-17, pushed the day it was checked, CC BY 4.0, **18 stars**. 385 markdown files, roughly
795,000 words, which is fourteen times this collection's corpus.

**What it has that this collection does not, all confirmed in the clone:**

- **Control arms.** Guided against unguided, on multiple models, with saturation checks that
  discard an experiment when the arms fail to separate. This collection grades other people's
  published evidence. That repository **generates its own**.
- **Nine published null results**, sitting on the same scoreboard as the positive ones, including
  one that says the audit half of its own library adds nothing a good model does not already do. The
  count was **corrected upward from seven**, in public, for understating it.
- **A retraction.** An early +0.07 on inert-control detection did not reproduce when the sample grew
  from 15 to 49 cases. Withdrawn, documented, not quietly dropped.
- **Pre-registered predictions**, recorded before the experiments ran, with the wrong ones published.
- **Negative-control CI.** `scripts/check-negative-controls.sh` injects a known-bad per invariant
  into a disposable worktree and **requires the intended check to be the one that complains**; a
  non-zero exit for any other reason is reported as a false pass rather than a catch. This
  collection makes its checks fail on purpose by hand, once, when it remembers. That repository
  automated it and verifies that the *right* check fired.
- **A `LAST-VERIFIED` stamp with an invariant preventing a dishonest bump**: it cannot move without a
  sweep-shaped diff or a changelog entry naming it. This collection's recheck date is bumped by
  whoever edits the header.

**Where this collection is still different, stated narrowly because the honest margin is narrow.**
SOTA-skills measures **its own library's effect on model output**. This collection grades **the
field's published claims by review trail** and records where sources disagree, where nobody has
measured, and where it was itself wrong. Those are different instruments. Its scoreboard cannot tell
you that a paper's venue was never confirmed; this document's tier scale cannot tell you whether a
rule changes what a model writes.

**A fourth independent corroboration of the tier-1 nondeterminism finding, and this one comes with a
usable number.** Its harness records that temperature 0 is not deterministic in practice: re-running
an **untreated** arm, which cannot even see the treatment, moved 0.60 to 0.57. From that it derives a
working noise floor and states it as a rule: **any single-sample delta below roughly 0.05 is
unresolvable.** That is the first figure this document holds that tells a practitioner *how big a
difference has to be* before a single run means anything, rather than only that single runs are
unreliable. Organisation-disclosed, one harness, one project, so tier 5.

**How this entry was verified, because the pass that surfaced it has a defect worth recording.** The
repository was **cloned and grepped**, not read from its README, and the two facts most load-bearing
here, the negative-control script and the `LAST-VERIFIED` invariant, are visible only in the clone.
The research pass that surfaced it carried **a broken footnote apparatus**: footnote numbers resolved
to unrelated sources, including a citation for an arXiv policy that resolved to a medical evidence
handbook. Its inline URLs were mostly correct, so the work was recoverable, but **anyone verifying it
by footnote number lands on the wrong document.** Nothing from that pass entered this collection
without independent retrieval, and the general rule stands: **a research pass locates a thing, it
never supplies the number.**

**Self-interest flag, since this collection insists on them:** the repository's homepage is a company
site, so the measurements are published by a party with a commercial interest in the library
performing well. Its own headline is nevertheless hedged as "small pilot, 3x, two models, one task"
and it reports the stricter measure alongside the flattering one, which is more than most parties
with that interest do.

**It does not close open gap 4**, and it says so itself: baseline-dependent, small pilot, and on one
model the unguided arm already scores 1.00 so the lift is +0.00.

### The nearest published thing to this scale, and how it differs

**Added 2026-09-08 after an external evaluation went looking for prior art.** arXiv:2605.11027, De La
Cruz, "From Code-Centric to Intent-Centric Software Engineering", PDF read 2026-09-08. A reflexive
thematic analysis of this field's public discourse and peer-reviewed evidence, organised through a
corpus register, a codebook, a coding matrix, a theme-to-source traceability table, **a DOI and
reference audit**, and a stated reproducibility protocol. Its corpus deliberately mixes peer-reviewed
literature, benchmarks, talks, essays, product announcements and social-media discourse.

**So somebody has stratified this field's sources by kind, in an academic register, and published
it.** That is worth stating plainly rather than letting the differentiation claim stand unqualified.

**And something closer may exist.** A second landscape pass on 2026-09-09 reports **arXiv:2608.13867**
(Jarmak, 314 pages) as carrying a versioned catalog of **206 reliability records** and an evidence
ledger, which would be direct prior art rather than adjacent work. **Not confirmed here**: arXiv is
unreachable from every environment used on this project and the companion repository was not named.
Recorded in `ROADMAP.md` under known weaknesses with its verification status. **If it holds, the
differentiation claim in this section is too strong and this document should be the one to say so.**

**Two differences, and they are real rather than defensive.** It classifies **sources in a corpus** in
order to derive themes about where the profession is going. This collection grades **claims attached
to rules an engineer applies**, and the tier travels with the rule to the point of use. And its
output is a thematic account; this document's output is a prohibition with a tier on it, a stated
default where sources disagree, and a numbered list of the times it was wrong.

**Where it is ahead of this collection:** it is peer-reviewable, it has an explicit codebook and
reproducibility protocol, and its DOI audit is a formalised version of what this document only
started doing at 0.10.1, after awarding tier 2 four times on surfaces the authors controlled.

### What counts as confirming a venue, and what does not

**Added 2026-09-07.** Tier 2 requires the venue or a publisher DOI. In practice the thing nearest to
hand is a preprint's own metadata, and it does not qualify:

- **An arXiv `Comments` field is supplied by the submitting author and is not verified by arXiv or by
  any publisher.** "Accepted at X" there is the author's claim. It is usually true and it is not a
  venue record, so on its own it supports **tier 4 with a note**, not tier 2.
- The same applies to an author's institutional publication page, a lab's replication repository, and
  a ResearchGate entry. All three are author-controlled surfaces. Finding the claim on more of them
  raises confidence and does not change who is asserting it.
- **What does qualify:** a publisher record with a DOI, the venue's own published programme or
  proceedings, or an independent bibliographic index such as DBLP.

All nine papers this document had rated tier 2 were audited against this on 2026-09-07. **Five held
and four moved to tier 4**, one of which had never claimed a venue at all and had been tiered on the
quality of its method. Recorded at error 20. `build.py` now counts records against papers on
every build, so an entry naming two papers must cite two records.

One trap worth naming separately: **an arXiv DOI is not a publisher DOI.** Every arXiv paper has one,
of the form `10.48550/arXiv.NNNN.NNNNN`, and its existence says only that the preprint exists.

### First-party observation is a separate axis, not a tier

The scale above grades **external** claims: things someone else published, which a reader can go and
check. A large share of this skill rests on something different - direct observation of the
repositories and teams it came from.

That is **not tier 1, and it is not tier 8 either.** It is a different kind of thing:

- **Strong for the case it came from.** A rule derived from a failure in your own repository is the
  best possible evidence about your own repository.
- **Unfalsifiable by an outside reader.** Nobody can check it. A stranger reading "47 of 47 changes
  self-merged" has to take it on trust or discard it.
- **Not automatically generalisable.** Repositories worked on by one or two people share confounds.
  A pattern across all of them may be a pattern in how one person works.

**Two numbers are hiding inside every first-party claim here, and conflating them is the easiest way
to over-read this document.** Added 2026-09-03 after an external review flagged it:

- **The observations within a case.** "47 of 47 merged changes self-merged, zero human reviews
  across 51" rests on every change in that repository's history. Within that repository the finding
  is not thin at all.
- **The cases themselves.** That same claim rests on **one repository**. As a statement about
  repositories in general it is a single case study and nothing more.

So read a first-party number as **strong about its own case, weak about yours**, and notice which
question you are asking. A dramatic figure with a large internal N still generalises no further than
the handful of repositories it came from. Where a claim states a count of independent contexts, that
count is the number that bounds generalisation.

Everything of this kind is labelled **`first-party`** wherever it appears, and the label is a
warning to the reader rather than a boast. Where a first-party pattern appears in genuinely
independent contexts it says how many, because that is the only strengthening available without
external work: the mocked-tests-certifying-a-broken-build pattern is stated as three independent
repositories for exactly this reason.

**Do not promote a first-party observation to a tier by repetition.** Observing it again in the same
hands is not independent.

### The two standing rules

**Asymmetric burden.** A tier-4-or-weaker source may raise a doubt about a practice. It may **not**
retire a practice, remove a control, or downgrade a standing recommendation. Adding a safeguard on
weak evidence costs effort; removing one costs correctness. Any revision that uses a tier-4-or-weaker
source to justify *stopping* something must say so explicitly and flag it for a stronger check.

**Check the artifact, not the claim about the artifact.** A paper's own "submitted to venue X" line
states intent, not outcome; check the accepted list or a publisher DOI distinct from the preprint's.
This generalises well past citations, and it is the single highest-yield habit in this document:

- A tool's hook was configured and the binary it invoked was not on `PATH`. The hook failed silently
  on every call and the savings were zero.
- A tool believed installed was not installed at all; three name variants and three data directories
  came back empty.
- A tool was installed, its script present and executable, and it still could not run: the skill
  invoked `python3`, which resolved to a shim rather than the real interpreter.

All three were "verified installed" by someone who had checked that a file or command existed.
**Run the thing.**

**Rediscovery is not replication.** Two research passes finding the same paper confirms the paper
exists and says what it claims. It does not corroborate the finding, and it does not resolve a
disagreement between that paper and another.

---

## Sources

### Tier 1, Replicated

**Run-to-run nondeterminism in agent evaluation, and it discounts everything else here.**

**Upgraded 2026-09-06 from two groups to four.** A verification pass found a third and fourth
independent measurement, and both name the mechanism rather than only the effect:

- **arXiv:2602.16666**, "Towards a Science of AI Agent Reliability", runs each agent-benchmark
  combination **K=5 times at temperature 0** so that any observed variance is attributable to
  non-sampling sources, and attributes it to **floating-point non-associativity, batch-size variation
  from concurrent server load, and non-deterministic kernel scheduling**. It also notes that
  reasoning models **do not expose a user-configurable temperature parameter**, which answers a
  question this collection had explicitly listed as open.
- **arXiv:2608.08239**, "The Replay Gap", calls batching- and kernel-induced nondeterminism at
  temperature 0 **an experimental floor in the agentic setting**, and finds it **differs sharply
  across quantization stacks**.
- Supporting rather than independent: arXiv:2604.12147 repeats runs three times and reports a
  pairwise McNemar test showing statistically significant differences across runs; arXiv:2408.04667
  quantifies temperature-0 instability generally.

These are independent by group, by data and by method: different scaffolds, different benchmarks,
different variance-attribution approaches. **So the finding is now multiply replicated rather than
merely replicated**, and the causes are named rather than inferred. Everything in this collection
that rests on a single run inherits a larger caveat than before, not a smaller one.

The two original sources, different methods, different scale, same direction:

- **arXiv:2607.09691**, single author, SWE-bench Verified, N=70 multi-file instances, affiliated with
  a small consultancy. The finding that matters and is uncontested: **re-running one arm at
  temperature 0 flips 6 of 70 per-instance outcomes, roughly 9%**, which the paper itself calls a
  noise floor bounding "ours and others'" small differences.

  **One detail is contested between two independent verification passes and is therefore not
  asserted here.** An earlier version of this entry read the 25-of-70 and 23-of-70 figures as two
  runs of the same arm. A second pass reports them as **two different experimental arms**
  (keep-and-drop at 25 of 70, structured-signature at 23 of 70, with a null result between them at
  p=0.754), which would make the earlier reading a conflation of arms with runs. **See the contested
  findings section below**: this collection does not have a direct read settling it, so the flip
  count stands and the 25-versus-23 framing is withdrawn.
- **arXiv:2602.07150**, Bjarnason, Silva & Monperrus (KTH). **Preprint. An acceptance at the ICLR
  2026 Workshop on Agents in the Wild is claimed by the paper's own front matter and has not been
  confirmed against any record its authors do not control.**

  **This entry said "published, confirmed 2026-09-04 from the paper's own front matter" until
  2026-09-08.** A front-matter banner is exactly the surface error 20 disqualified, and it is the
  surface arXiv:2605.02273 was moved down to tier 4 for. The 0.10.1 audit that established the rule
  was scoped to tier 2 and never looked one section above it, so the identical defect survived the
  audit that existed to find it. Searches of the workshop's accepted-paper listing and of
  bibliographic indexes did not reach a record. **"Could not confirm", not "confirmed absent"**:
  other papers carry that banner, so the workshop is real. Recorded as error 21.

  **60,000 trajectories** over **500 SWE-bench Verified tasks**, six configurations (three models
  across two scaffolds), **ten runs per configuration** at multiple temperatures. **pass@1 varies 2.2
  to 6.0 percentage points run-to-run**, with standard deviations **up to 1.8pp** and exceeding 1.5pp
  **even at temperature 0**. Concrete example: one configuration at temperature 0 scored 22.3% with a
  standard deviation of 1.8 and a range of 19.8 to 25.2.

  **And a figure this collection should have been quoting all along**: the gap between pass@1 and
  pass@5 reaches **24.9 percentage points**, and between pass@1 and pass^5 reaches **18.9 percentage
  points**. That is the size of the lie a single run tells you, and it is the strongest available
  justification for the pass^k rule in `SKILL.md`.

  **One sub-claim retracted 2026-09-04.** An earlier version of this entry added that the
  interquartile range at temperature 0 was comparable to or wider than at temperature 0.7. A direct
  read of the paper found only standard deviation and min-max ranges, no interquartile comparison.
  **Unconfirmed rather than contradicted**, and removed because it was doing rhetorical work the
  paper does not support. The finding that matters, that temperature 0 does not buy determinism,
  stands on the standard-deviation figure alone.

The second finding is the one to remember: **setting temperature to zero does not make agent
evaluation deterministic.** Anyone comparing two configurations on a single run, on their own
repository, is very likely reading noise.

**This entry forced a correction to the scale itself, which is worth more than the finding.** When
it was written, both papers were believed to be preprints with no venue: the scale is ordered by
review trail, so it could not express "two independent groups agree, neither peer-reviewed", and it
was quietly treating tier 1 as tier 2 plus replication. That was wrong and the fix stands.

**The premise then changed twice and this paragraph tracked only the first change**, which is how the
section came to say "confirmed workshop-accepted" in one place and "both preprints" in another, four
paragraphs apart, for two days. Both statements shipped. `SKILL.md` forbids exactly this: a file that
states a rule and then contradicts itself is worse than one that omits the rule.

> **Replication and review are orthogonal axes.** Tier 1 records that independent groups converged.
> Tier 2 records that reviewers accepted the work. Neither implies the other. Two independent
> preprints agreeing is genuinely stronger on the dimension that matters most for acting on a
> finding, and genuinely weaker on method scrutiny.

So a tier-1 entry now **states its review status explicitly** rather than implying one. This pair is
**tier 1, both preprints**, one of them carrying an author-claimed workshop acceptance this document
has not confirmed. Read that as: the effect is probably real, the exact numbers have not been through
review.

**And the finding no longer rests on this pair alone**, which is what makes the unconfirmed venue
survivable: two further independent groups measured the same effect and named its causes, recorded
above. A venue record would add method scrutiny to one paper. It would not change the replication
count, and the replication count is what this tier is for.

Everything else in this document that rests on a single benchmark run inherits this caveat, including
the compression result below, which comes from one of these two papers.

### Tier 2, Reviewed

**AI-generated code carries more of two specific defect classes, and the aggregate direction is
contested.** Cotroneo, Improta & Liguori, arXiv:2508.21634. **Published at the 36th IEEE
International Symposium on Software Reliability Engineering (ISSRE) 2025**, IEEE Xplore document
11229706, **DOI 10.1109/ISSRE66568.2025.00035**, pages 252-263. **Upgraded from tier 4**, where it
sat as a preprint for two days because the first verification pass did not reach its acceptance line.

> **The confirmation route was corrected on 2026-09-07 and the tier survived it.** The upgrade
> originally rested on the arXiv **Comments** field, which is **author-supplied and not checked by
> any publisher**, so it is an author's claim of acceptance rather than a venue record and does not
> meet this scale's own tier-2 bar. A third pass flagged exactly that. Rechecking found the
> publisher record above, so the entry is now confirmed the way the scale requires rather than the
> way it happened to be confirmed first. **Route recorded because the outcome does not justify it:**
> had the DOI not existed, this belonged back at tier 4.

Over **500,000 code samples** across Python and Java, comparing human-written GitHub functions with
output from three model families. Defects via Pylint and PMD mapped to ODC; security via Semgrep
mapped to CWE. Reports AI-generated code as more prone to **unused constructs and hardcoded debugging
artefacts**, as triggering **more high-risk CWE categories** including command injection and
hardcoded secrets, and as **shorter**, using fewer tokens and fewer lines on average.

> **Contested at the aggregate by arXiv:2603.27130** (Mao, Duan, Tang, Wang & Zhang, Indiana
> University Bloomington and NTU), a large-scale measurement of AI-assisted code in real-world
> repositories, still a preprint.
>
> **This block was rewritten on 2026-09-08 against the preprint's own PDF, and three of the numbers
> it previously carried were wrong.** The version before this one said both full texts had been read
> on 2026-09-06. They had not. Recorded as error 23, and read the numbers below as the corrected
> ones rather than as an update.
>
> **What the preprint actually reports**, quoted from its section on code security and defects:
>
> - **Overall CodeQL alert density: AI 10.04 against human 13.56 per KLOC.** AI-generated code
>   triggers *fewer* alerts, "in each type of alerts and each level of severity" with one exception.
> - **That exception is high-risk alerts, and there the two are similar: 0.514 against 0.52.** Not
>   elevated. The previous version of this entry reported this row as AI 0.934 against human 0.464,
>   which is not in the paper, and it reversed the direction of the finding it names.
> - **A second table showing AI at 12.81 against human 11.58 does not exist.** Those numbers appear
>   nowhere in the paper.
> - **Human-written code contains more hardcoded secrets**, passwords, API keys, tokens and private
>   keys, which is a direct contradiction of one of the ISSRE paper's two named defect classes rather
>   than an aggregate disagreement.
> - Its own summary: *"AI-generated code shows lower overall defect density, but security differences
>   are language-dependent."* For high-risk alerts, **C, C#, JavaScript and Ruby** are higher in
>   AI-generated code; **C++, Java and Python** show the opposite; TypeScript is similar.
>
> **The methodological differences stand and still matter:**
>
> - **Different populations.** ISSRE studies prompt-generated functions from a docstring. The
>   preprint studies AI-assisted code **found in the wild**, matched against human code from the same
>   repositories.
> - **Different instruments.** Pylint, PMD and Semgrep against CodeQL.
> - **Both find the same dominant CWE categories**, CWE-563 and CWE-561, unused or ineffective code
>   constructs. That is genuine convergence on the *mechanism*, and it is on the defect class the
>   ISSRE paper names first.
>
> **What the corrected reading changes.** The previous conclusion, "both find elevated high-risk
> patterns in AI-generated code in at least one cut", was resting on a figure that is not in the
> paper. It survives only in the weak form: **in four of eight languages** the preprint finds
> high-risk alerts higher in AI-generated code, and in three it finds the opposite. At the aggregate
> the preprint finds AI code *safer* by alert density and *cleaner* on hardcoded secrets. **So the
> disagreement is wider than this document claimed, not narrower.**
>
> **Default, unchanged, and now doing more work than before:** keep checking AI-generated code for
> the two named defect classes. They are cheap to find and cheap to remove, and the asymmetric-burden
> rule holds: a contesting source may raise a doubt about a safeguard and may not retire it. **Note
> what that rule is now protecting.** The safeguard survives a source that contradicts it more
> strongly than this document previously admitted, which is the rule working rather than the rule
> being convenient. If you work in C, C# or JavaScript the preprint is on the safeguard's side
> anyway.
>
> **Neither study measures whether human review catches any of this at normal rates.** Both count
> analyzer alerts. That question remains open, is gap 10, and is the one a practitioner actually
> needs answered.

**Self-declaration of AI-generated code.** Kashif, Liang & Tahir, arXiv:2504.16485. Published as
**ACM Transactions on Software Engineering and Methodology, vol. 35 no. 7, pp. 1-37, July 2026**.
Confirmed 2026-09-02 against the **Crossref registrar record** for `10.1145/3771937`, which carries
volume, issue and pagination, so this is final publication rather than acceptance alone. Note what
the earlier basis was worth: the publisher DOI printed on the arXiv listing is an author-entered
field, so on its own it was still the paper's own claim about itself. The registrar record is what
makes this tier 2. Method: 613 mined code snippets plus a survey of 111
practitioners. Findings: 76.6% self-declare AI-generated code always or sometimes, 23.4% never;
declaration is motivated by traceability for later review and debugging, and by ethics;
non-declaration is motivated by extensive modification making the code feel distinct, and by
disclosure feeling like overhead.

This is **the best-evidenced source in the skill**, and it went unused by four separate research
passes before being found. Worth remembering when a research chain reports convergence.

**Re-verified 2026-09-02 by a second direct fetch of the registrar record**, because an independent
check that same day reported the volume, issue and DOI as *unconfirmed*. Both fetches were of the
same record; the second one reached it and the first of the two attempts did not. Title, journal,
volume 35, issue 7, pages 1-37, July 2026, and all three authors match.

This produced a rule worth having on its own:

> **A failed verification is not a negative finding.** "Could not confirm" and "confirmed absent"
> are different results, and only the second one is evidence. Treating the first as the second
> would have downgraded the strongest source in this collection on the strength of one pass not
> reaching a URL.

The asymmetric-burden rule already covers weak evidence retiring a practice. This covers the
adjacent case: **absent evidence retiring a practice**, which is easier to miss because it arrives
looking like diligence.

**The OWASP ranking.** The GenAI Security Project's **2026 LLM Top 10, published 2026-08-04, keeps
prompt injection at number one**, and a separate 2026 Top 10 for agentic applications now exists
alongside it. Confirmed 2026-09-02. This is the basis for treating prompt injection as the primary
production failure mode rather than a secondary concern, and the separate agentic list is worth
reading directly since this collection does not reproduce it.

**Vulnerability disclosures.** Treated as tier 2 because a CVE is an independently verified
disclosure rather than a vendor's self-report. **Vendors named**, unlike the first-party examples
elsewhere in this collection: a CVE is public record, and "an agentic IDE" gives a reader nothing to
check or patch against. Both mechanisms verified against the CVE records 2026-09-04.
CVE-2026-22708 against **Cursor**: shell built-ins such as `export`, `unset` and `alias` bypass the
terminal allowlist, letting an attacker poison the shell environment so that a later *trusted*,
allowlisted command such as `git` executes a malicious payload. **The allowlist was never the thing
that mattered**, which is the whole lesson.
CVE-2025-59532 against **Codex CLI**: the agent trusted a **model-generated `cwd`** as the sandbox's
writable root, so the model's own output redefined the boundary meant to contain it.

**Adversarial review, and how many reviewers.** Qiu & Gill, arXiv:2608.18167. **ICML 2026 Workshop
on Deep Learning for Code, accepted as a Poster**, confirmed 2026-09-08 against the **OpenReview
record**: submission 123, published 16 June 2026, listed under the workshop's own venue on a platform
the authors do not control. **Restored to tier 2** after one day at tier 4: it was downgraded on
2026-09-07 when its only evidence of acceptance was the arXiv `Comments` field and no record could be
reached from a network-restricted environment. The record existed. See error 20 and the note on
"could not confirm" that follows it.

**The tier carries a weight this scale does not currently express**, and it is stated here rather
than hidden: a workshop **poster** is peer-reviewed and accepted, which is what tier 2 requires, and
it is among the lightest review trails a venue offers. Read it as tier 2 at the bottom of tier 2.

Findings, and all three are directly load-bearing here:

- A **three-agent** adversarial review (main, reviewer, critic) outperformed a **five-agent**
  baseline on LiveCodeBench. More reviewers is not better, and this is the only measured statement
  available on the question.
- On SWE-PRBench, naive adversarial review exposed a **false-consensus failure mode**, agents
  converging on agreement without sufficient evidence.
- **A single prompt iteration adding explicit disagreement** produced the highest F1 among tested
  methods.

The authors' own summary: cooperative code review "requires that disagreement be minimal, structured,
and evidence-grounded". So isolating the reviewer's context is necessary and not sufficient. The
reviewer also has to be told to disagree, because a reviewer that merely lacks the implementer's
reasoning will still converge on its conclusion. This closes open gap 2.

**Who actually reviews AI-authored changes, and how well.** Chowdhury et al., **arXiv:2604.03196,
MSR 2026, DOI 10.1145/3793302.3793614.** Added 2026-09-03. From 19,450 pull requests: 3,109 in a
commented-review state, 98 closed reviewed only by a code-review agent, 13 such agents studied.
**Agent-only-reviewed pull requests merged at 45.20% against 68.37% for human-only, a 23.17 point
gap.** 60.2% of the closed agent-only pull requests fell in the 0 to 30% signal-to-noise band, and 12
of the 13 agents averaged a signal ratio below 60%. The authors' conclusion, quoted: code review
agents "should augment rather than replace human reviewers".

This is the external evidence the team layer previously lacked entirely, and it lands on the same
conclusion the first-party self-merge observation reached from one repository.

**How humans review AI-generated pull requests.** Duma, Wróblewski, Bobińska, Winiarska & Przymus,
arXiv:2605.02273. **EASE 2026, Short Papers and Emerging Results track**, confirmed 2026-09-08
against the conference's own research-papers programme, scheduled as a ten-minute talk. **Restored to
tier 2** after one day at tier 4, same cause and same correction as the entry above.

Most AI-generated pull requests **receive no review at all**, and where they are reviewed, the review
is dominated by AI agents rather than humans. Human-authored pull requests are more likely to attract
human-only review and direct human feedback. **Sample size could not be extracted from the available
text**, which is worth stating because the finding is qualitative without it.

**Two weights on this one, both stated because the tier number expresses neither**: it is a short
paper in an emerging-results track, and it uses the same public dataset as arXiv:2604.03196 above, so
the pair is related rather than independent.

**AI-contribution policy prevalence.** Hora & Robbes, arXiv:2605.16706, "AI Policy, Disclosure, and
Human in the Loop: How Are Contribution Guidelines Adapting to GenAI?". **ICSME 2026, Visions and
Emerging Results track**, confirmed 2026-09-08 against the conference's own programme, scheduled as a
ten-minute short paper on 16 September 2026. **Restored to tier 2** after one day at tier 4, same
cause and same correction as the two entries above.

1,000 GitHub repositories surveyed, **118 carrying an explicit AI policy**: of those, 78% permit AI
contributions, **51% require disclosure**, and 74% require a human in the loop.

Note carefully what this is and is not. It measures **project policy prevalence**, a different unit
from the self-declaration *rate* among practitioners in arXiv:2504.16485. So it corroborates that
disclosure norms exist and are being formalised. **It does not replicate the 76.6% figure**, and the
disclosure claim therefore stays tier 2 single-study rather than moving toward replicated. It is also
a vision-track short paper, which is the light end of tier 2.

**Documentation inconsistency is measurably harmful. Two papers, and they were conflated here until
2026-09-04.**

- **Wen et al., ICPC 2019**, DOI 10.1109/ICPC.2019.00019. The large-scale mining study: **1.3 billion
  AST-level changes across 1,500 systems**. Its finding is about timing, not magnitude: an
  inconsistency's bug-introducing impact is **highest immediately after it is introduced and decays
  over time**. That is a more useful finding than the one previously attributed to it, and it argues
  for catching drift early rather than auditing periodically.
- **Radmanesh, Imani, Ahmed & Moshirpour**, arXiv:2409.10781, "Investigating the Impact of Code
  Comment Inconsistency on Bug Introducing". **This is where the 1.5x figure comes from**:
  inconsistent changes are "around 1.5 times more likely to lead to a bug-introducing commit than
  consistent changes".

The earlier version of this entry credited the 1.5x figure to Wen et al. It is not in that paper. See
error 12.

This is the first external support for the documentation rot taxonomy's core mechanism, which was
otherwise entirely first-party. It is also seven years older than everything else here, which is
itself informative: the problem is not new and the agentic framing did not create it.

**Benchmark scores transfer poorly to real repositories.** "What's in a Benchmark? The Case of
SWE-Bench in Automated Program Repair", **ACM ICSE-SEIP 2026, DOI 10.1145/3786583.3786904**.
Existence and peer-reviewed status confirmed; **the full text could not be retrieved, so no number
from it is quoted here.** Recorded at tier 2 for its existence and used only to support the general
claim that benchmark critiques exist in reviewed venues.

Figures circulating alongside it, and deliberately **not** adopted as claims: roughly a third of
successful patches said to contain solution leakage in issue text, a quarter said to pass on weak
tests, and a vendor audit reporting that 59.4% of one model's apparent failures were harness flaws.
Each is plausible, none was verified to a primary source in this pass, and all three are the sort of
figure this document has previously restated wrongly. **Treat as unverified until fetched.**

**AI assistance speeds the writing and does not improve what comes after. A controlled experiment,
and the strongest study in this collection on the question that matters most.** Borg et al., "Echoes
of AI: Investigating the Downstream Effects of AI Assistants on Software Maintainability",
arXiv:2507.00788, **published in Empirical Software Engineering**, volume 31 issue 6, **DOI
10.1007/s10664-026-10889-1**. Added 2026-09-04; publisher record cited from 2026-09-07, having stood
for three days on the journal name alone.

**It is also the only preregistered study in this collection.** It went through the **Registered
Reports track of ICSME**, which reviews the design before the results exist and issues in-principle
acceptance on the protocol. That is a stronger guarantee than ordinary peer review against the
failure mode this document worries about most, because a preregistered design cannot be reshaped
after the numbers come in.

Two-phase design, **151 participants, roughly 95% professionals**:

- **Phase 1.** Participants add a feature to a Java web application, with or without AI assistance.
  Result: **30.7% median reduction in completion time**, and an estimated **55.9% speedup** for
  habitual AI users. A large, real effect on the writing.
- **Phase 2, and this is the point.** *Different* participants, randomly assigned, then evolve those
  solutions **without** AI assistance. Result: **no significant differences** in subsequent evolution
  time or code quality. A Bayesian analysis concludes any speed or quality improvement was **"at most
  small and highly uncertain"**.

**Why this is the most important entry added in this pass.** It is a peer-reviewed controlled
experiment that separates the phase AI helps from the phase that inherits the consequences, and it
finds the benefit does not carry. That is a stronger design than anything else here on downstream
effects, and it is the closest existing work to the controlled defect-rate study this collection
keeps saying does not exist. **It does not close that gap**, because maintainability and evolution
time are not defect rates, but it narrows it considerably.

Affiliations include a commercial code-analysis company alongside academic co-authors, so **vendor
involvement is present**, and the direction of the finding is not the flattering one for that
vendor's market, which is worth noting in both directions.

**Moved out of this tier 2026-09-07: developers are wrong about their own speedup**,
arXiv:2507.09089. **Now at tier 4**, below, and this one was not a misread venue record. **It never
claimed a venue at all.** It was placed at tier 2 because it is a randomised controlled trial with a
clean design, which is grading by method quality, and this scale is explicitly ordered by review
trail rather than by method quality. That substitution is the specific failure the scale exists to
prevent, committed by the scale's own author. Error 20.

### Tier 3, Under review

**Test-impact context beats test-first procedure.** Alonso, Yovine & Braberman, arXiv:2603.17973,
March 2026. Multi-author, public code and data, states submission to a reviewed venue's data and
benchmark track. Checked: it does not appear on that venue's accepted-papers list, so tier 3 rather
than tier 2. Findings: supplying a graph-based test-impact map cut regressions by 70%, from 6.08% to
1.82%; imposing test-driven development as a procedural instruction *without* that context raised
regressions to 9.94%, worse than no intervention.

This is the source for "context beats procedure", the most actionable finding in the skill.

### Tier 4, Preprint

**Code health predicts whether an LLM can refactor a file without breaking it.** Borg, Hagatulah,
Tornhill & Söderberg, arXiv:2601.02200, "Code for Machines, Not Just Humans: Quantifying
AI-Friendliness with Code Health Metrics". PDF read 2026-09-08. **5,000 Python files** from
competitive programming, LLM-based refactoring, finding a meaningful association between **Code
Health**, a maintainability metric calibrated for human comprehension, and **semantic preservation
after AI refactoring**. The authors' conclusion: human-friendly code is also more compatible with AI
tooling, and Code Health can indicate where AI intervention is lower risk.

**Tier 4 and not tier 2, and the reason is this document's own rule.** The paper is reported at FORGE
2026 with an ACM DOI. **The preprint's own ACM reference block carries a placeholder DOI**, not a
real one, and no venue record was opened here. Under error 20's rule an acceptance is not confirmed
from a surface the authors control. **Upgrade on sight of the ACM record or the conference
programme.**

**What it does and does not do for open gap 4.** It is the closest thing found to evidence that a
code property affects AI outcomes, and it is **not** the controlled defect study gap 4 asks for:
non-randomised, a competitive-programming corpus rather than fielded software, and the outcome is
refactoring-preservation rather than defects that reach anyone. Gap 4 stays open and now names this
paper, because a gap that does not name the nearest thing to an answer misleads about how empty it
is.

**Rule polarity.** Zhang, Wang, Cui, Qiu, Li, Zhu & He, arXiv:2604.11088, April 2026, revised May
2026. 679 real rule files, 25,532 rules, 5,000+ agent runs on a frontier model against a standard
benchmark. Findings: random rule files improved performance as much as expert-curated ones, both
+13.8pp on a discriminative subset; every individually beneficial rule was a negative constraint,
every individually harmful one a positive directive; gains were largely content-independent,
consistent with context priming rather than instruction-following.

**Checked directly: no journal reference, no venue, no acceptance comment. Tier 4 despite seven
authors and 5,000 runs.** This document originally cited it as tier 3, which was an overstatement of
exactly the kind the scale exists to catch. The prohibition-phrasing convention survives because
choosing a phrasing style does not retire a practice, so the asymmetric-burden rule does not apply.
But it is a convention, not a settled result.

**Specification writing and defect rates.** Single author, self-published preprint, version 3, with
public code. 119 repositories, 100,247 pull requests, within-author fixed effects and defect tracing.
Finding: no association between specification presence or quality and defect outcomes across all
robustness checks.

Note carefully what this does and does not support. The claim it challenges was never measured
either: specification-driven development's defect-reduction benefit is vendor methodology, tier 5 at
best. So the honest statement does not depend on this preprint being right: **nobody has produced
tier-1-or-2 evidence that specifications reduce defects, including the one person who tested it.** If
the methodology holds, there is a tier-4 null. If it does not, there is still no support for the
original claim.

This source was once used to instruct a downgrade of specification practice from "do this" to
"contested". That is precisely what the asymmetric-burden rule forbids, and it is the reason the rule
is written down.

### Tier 4, venue checked and none found

Four studies of agent instruction files, **checked 2026-09-02: no journal reference, no venue and no
acceptance comment on any of the four**. Tier 4 is now a confirmed floor rather than an open
question:

- arXiv:2602.11988, Gloaguen et al. - context files did not generally improve task success while
  raising inference cost **over 20% on average**. **Authorship did matter, and this document
  previously stated the opposite.** Corrected 2026-09-02: LLM-generated context files *hurt*
  performance by 0.5% and 2% in two settings, while developer-written files gained **+2.4% on
  average**. Corrected 2026-09-04 from "roughly 4%", which overstated it by more than half; see
  error 12. Cost rose 20% in one setting and 23% in the other, so "over 20%" is precise for one and
  borderline for the other. The aggregate
  null conceals two effects pointing in opposite directions, and the practical reading is that a
  generated instruction file is worse than no instruction file. The paper also distinguishes by
  content type: instructions are well followed by agents, and **repository overviews specifically
  did not help**, contradicting vendor guidance. Five authors, v1 February 2026, v2 June 2026.

  Note for anyone citing the 4-point figure: it is internal to this paper. An earlier reading of
  the research chain treated it as a separate rebuttal by a different author, which would have made
  two sources out of one.

  **A nuance found 2026-09-04 that narrows the rule built on this paper, and it matters.** When
  existing documentation is **removed** from the repository, LLM-generated context files **improve**
  performance by about **2.7 percentage points** and can outperform developer-written docs. So the
  finding is not "generated context is bad". It is **"generated context is redundant when
  documentation already exists, and helpful when it does not"**. The rule in `SKILL.md` is scoped
  accordingly: do not generate one *over the top of existing documentation*.

  Design detail worth having: two benchmarks, one of 300 tasks across popular repositories and a
  purpose-built one of 138 issues across twelve **less-popular** repositories that have
  developer-written context files. The human-context gain is reported on the second. Affiliations:
  a university group **and a commercial company**, so vendor involvement is present.
- arXiv:2601.20404 - instruction-file presence cut median wall-clock time **28.64%** and median
  output tokens **16.58%**. **Correctness was explicitly not measured**, and the authors say so. Six
  authors, five pages, two agents.
- arXiv:2607.27250, Khatri - a with/without context-file comparison across two frontier agents,
  **17 real tasks from 3 repositories, 288 evaluated runs with gold-test evaluation**. The PDF was
  read 2026-09-08 and it states a **bounded null** rather than merely a non-significant result:
  context strategy does not measurably move correctness, **bounded to within 10 percentage points on
  one agent and 15 on the other via equivalence testing**. Failure triage attributes failures to
  implementation skill, feature design, pattern selection and exact wiring, **not to missing
  repository knowledge**, and a manipulation probe found the real context file could not convert a
  near-miss failure into a pass on either agent. It also reports that borderline task difficulty is
  **agent-specific**, which it offers as the reason single-agent studies reach contradictory
  conclusions. **Single author, independent researcher**; releases all code and data.

  **A bounded null is a stronger result than a non-finding and it is the strongest thing available
  on this question.** It does not say context files are useless. It says that on these tasks the
  correctness effect, if any, is smaller than the band, which is wide. Read alongside arXiv:2601.20404
  above, which measured a large wall-clock and token saving and explicitly did not measure
  correctness, the two are consistent: the case for a context file is time and tokens, not
  correctness.
- arXiv:2607.09691 - rendering an unread file remainder as signatures resolved no more issues than
  deleting it outright (N=70, exact McNemar p=0.75). **Single author**, but pre-registered hypotheses
  with the nulls published, which is stronger method discipline than the tier alone implies. Two
  further findings from it bear on this document's own open gaps, below.

### Tier 4, added 2026-09-03

**Review load, not defect rate, is what AI throughput actually moves.** arXiv:2607.01904, He,
Vasilescu et al. Enterprise field study, **802 developers, 196,212 pull requests**, January 2024 to
April 2026, staggered difference-in-differences. Throughput reached **2.09 times baseline**,
**per-reviewer load roughly doubled**, automated review overtook human review, and **merge and revert
rates held steady**.

The last clause is the interesting one and it cuts against alarmism: on this study's defect proxy,
nothing got worse. What changed was who and what does the reviewing, and how much of it there is.
Preprint, large N, enterprise data.

**Compression on a real code-editing workload, second data point.** arXiv:2601.16746, SWE-Pruner.
On SWE-bench Verified, **23 to 54% token reduction on agent tasks while improving success rates**,
using a small neural line-skimmer. Method is entirely different from arXiv:2607.09691's
representation ablation, so this is a second data point on the same question rather than a
replication. Both point the same way: compression on coding workloads is not the loss it is on
summarisation workloads.

**Code structure does affect agent success, and the first non-opinion evidence for it.**
arXiv:2605.06445, "Constraint Decay", Dente, Satriani & Papotti. 80 greenfield plus 20 feature
tasks across **8 web frameworks**. Capable configurations **lose 30 points on average in assertion
pass rates** moving from baseline to fully specified tasks, with **data-layer and ORM defects as the
dominant failure mode**, and worse results in convention-heavy frameworks than in minimal ones.
Single group, no replication found.

Worth noting because it is unusual: this **supports** a practitioner claim already in this document
(plain queries over ORMs, less magic over more), which had been sitting at tier 7 with no measured
backing. The direction now has one study behind it.

**Two competing reconciliations of the instruction-file disagreement, neither a replication.**
arXiv:2606.20512, Shepard & Albrecht, attributes the conflict to step-budget and iterative-refinement
differences (33.0% against 28.3% resolve rate). arXiv:2607.27250, Khatri, attributes it to
agent-specific task-difficulty bands (Spearman 0.75) across 288 runs, 17 tasks, 3 repositories and 2
agents, concluding that context strategy "does not measurably move correctness on either agent",
bounded to 15 points or less by equivalence testing. **Two different explanations of the same
disagreement is not a resolution of it**, and the disagreement below stays open.

**Model reviewers have a measured agreeableness bias.** arXiv:2510.11822 reports LLM judges at a
**true positive rate above 96% against a true negative rate below 25%** on validity judgments, which
is a machine that mostly says yes. arXiv:2605.25273, a scoping review of 13 studies in one domain,
found judge-to-expert concordance ranging **0.66 to 0.96, median 0.83**, worst on fine-grained
tasks, with a three-judge rubric-anchored ensemble reaching 0.90.

Both corroborate the mechanism behind the adversarial-review finding below: a reviewer agent's
default failure is agreement, so the disagreement instruction is doing real work rather than
decorating the prompt.

**Agent context files behave unlike documentation.** arXiv:2511.12884, "Agent READMEs". **2,303
context files across 1,925 repositories.** They function as **living configuration rather than
documentation**: frequent small edits rather than decay. Content skews to functional matters, tests
at 75.9% and architecture at 68.1%, while **security appears in 14.8% and performance in 14.5%**.

This one **contradicts a claim in this collection** and is recorded as such in the disagreements
below.

**Venue rechecks, 2026-09-03, closed against the PDFs 2026-09-08.** arXiv:2604.11088 and
arXiv:2607.09691: **confirmed preprint-only**, no venue or journal field present at all rather than
merely unreached. arXiv:2603.17973: the v2 PDF carries **no acceptance line and no publisher block**,
so **tier 3 stands unchanged** on its stated submission. arXiv:2607.27250: the outstanding "could not
confirm" from 2026-09-03 is now **confirmed preprint-only** from the PDF, single author, independent
researcher, July 2026. arXiv:2511.12884: the ISBN hint that suggested proceedings publication is not
borne out by the PDF, so it **stays tier 4**.

**Three of those four were "could not confirm" and all three resolved the way the weaker reading
predicted, which is worth noticing rather than celebrating.** It is one small sample and the base
rate on the tier-2 audit ran the other way: there, three of four unconfirmable acceptances turned out
to be real. **"Could not confirm" carries no direction.** That is the whole reason it is not a
finding.

### Tier 4, moved down from tier 2 and stayed down

**One entry.** Four were moved down on 2026-09-07 when a rule was added that an author-controlled
surface cannot confirm a venue. **Three of those four were restored to tier 2 on 2026-09-08** once
the venue records were fetched by hand: an OpenReview record, a conference programme, and a second
conference programme. They are back in tier 2 above, each naming its record and its track.

**The one that stayed down never claimed a venue at all**, and that is the difference. The other
three were "could not confirm" from a network-restricted environment. This one was a category error.

**Developers are wrong about their own speedup, and wrong in the confident direction.** Becker, Rush,
Barnes & Rein, arXiv:2507.09089, a randomised controlled trial from a non-commercial research
organisation, July 2025. **Preprint, no venue claimed.** Added 2026-09-04 at tier 2, which was simply
wrong: nothing about it was ever peer-reviewed, and it was graded on the strength of its design.

**16 experienced open-source developers, 246 tasks**, in mature repositories they had worked in for
around five years, with tasks randomly assigned to allow or disallow AI tooling.

- They **forecast** AI tools would make them **24% faster**.
- Afterwards they **believed** they had been **20% faster**.
- Measured, they were **19% slower**, with a confidence interval from **+2% to +39%** slower.

Small N, expert developers, familiar codebases, so it does not generalise to every setting. But the
gap between believed and measured is the finding, and it is the empirical backing for the
`OPERATING.md` rule about holding performance opinions loosely. **You cannot introspect your own
throughput**, and this is the study to cite when somebody reports that an agent made them much
faster.

**The tier drop does not weaken that rule**, on the asymmetric-burden rule: the rule it supports is
"believe your own speed estimate less", and a lower tier is not an argument for believing it more.
This is the clearest case in the collection of a finding whose usefulness is independent of its
review trail, which is exactly why the two are graded separately.

### Tier 5, Vendor-disclosed

**A five-run controlled comparison of an instruction file, and it demonstrates this collection's
tier-1 rule rather than merely citing it.** Griffiths, Agentic AI Foundation blog, 22 July 2026, read
in full 2026-09-08. Two identical clones of a real VS Code extension, one with a twelve-line
`AGENTS.md` and one without, same agent, same prompt, same starting commit, **five runs per
condition**.

**The finding that matters most is the one about method.** The author's first attempt, one run per
condition, reported the `AGENTS.md` run as **44% slower and 41% more expensive for identical
output**, and says of it: *"Clean numbers. Wrong conclusion."* Running five and taking the median
reversed the direction.

The five-run results: on an ambiguous task the file cut wall time **27%**, credits **24%**, and
produced diffs **26% smaller**. On a multi-file task the median win was **9 to 10%**, and the more
useful result was in the tail: **two of five runs without the file** wasted time re-orienting or ran
an unrequested production build, which no run with the file did. **No run in either condition touched
the protected files**, so the win was context rather than guardrails.

**Why this is here rather than higher.** It is a single repository, a single agent, one author, and
no released data or scripts, which is tier 5 and not tier 4. **Self-interest flag, since this
collection insists on them:** the Agentic AI Foundation stewards `AGENTS.md`, and this is the
steward measuring its own standard and finding it works. That does not make it wrong. It means the
direction of the result is the flattering one for the publisher and should be read that way.

**What it corroborates, and it arrives from a direction this collection did not look.** The tier-1
nondeterminism finding is four academic groups measuring run-to-run variance on benchmarks. This is a
Linux Foundation project independently hitting the same wall on ordinary engineering work, publishing
the wrong single-run answer alongside the corrected five-run one. **It is the most legible
demonstration available that the rule is operational rather than academic**, and it lands on
instruction files, which is this collection's weakest-sourced topic.

**It does not close open gap 1.** It varies the whole file, not one content class, and its outcomes
are time, cost and diff size rather than task success or defects.

- **Agent skill supply chain.** A security vendor's study of agent skills found **36.8%, or 1,467
  of them, carrying at least one security flaw, and 76 carrying a confirmed malicious payload**
  established by human-in-the-loop review. Verified against the primary source 2026-09-04, which
  also separately reports **13.4%, or 534 skills, with critical-level issues**. Do not conflate the
  36.8% and the 13.4%: they measure different severities.
  Corrected 2026-09-02: this document previously reported it as "prompt injection in 36% of surveyed
  agent skills, with 1,467 malicious payloads", which is wrong twice over. It restated a
  flaw-of-any-kind count as a prompt-injection count, and it attached the flaw count to the word
  malicious, inflating 76 to 1,467. See error 6 below. Directly actionable either way: this is why
  installing a third-party skill without reading what it executes is prohibited.
- **Multi-agent scaling.** A large research organisation's blog reported that independent
  non-communicating parallel agents amplified errors 17.2x on tasks requiring coordination, and that
  every multi-agent variant degraded performance 39-70% on tasks requiring strict sequential
  reasoning. A blog post, not a peer-reviewed paper.
- **Context degradation with input length.** A company research report across 18 models found
  performance degrades as input length grows even on simple tasks, non-uniformly across models, and
  worse when relevant information sits mid-context.
- **A vendor cutting over 80% of its agent's system prompt with no measured evaluation loss.** Widely
  repeated. **Could not be confirmed from an official source**; the citation trail led to an
  aggregator. Treat the direction as real and the specific figure as unverified.
- **Supply-chain incidents, 2026.** A malicious repository issue title chained four vulnerabilities
  into an npm compromise of **Cline**, February 2026, by exploiting an AI triage workflow that read
  the issue title as instructions. Confirmed 2026-09-02, and vendor-named for the same reason the
  CVEs are. A separate campaign harvested a publishing token through a compromised CI action and
  pushed backdoored package versions. Reported by security vendors and press rather than in
  peer-reviewed work, which is what keeps these at tier 5 despite being well documented.

- **Throughput up, stability down.** A large industry survey with roughly 5,000 respondents, 2025
  edition, reversed its own prior year: AI adoption now associates positively with delivery
  throughput and **negatively with delivery stability**. Vendor-adjacent, survey-based, not
  peer-reviewed, and it is an association rather than a controlled comparison.
- **Vendor telemetry, cited with its magnitude flagged.** One vendor's telemetry across 22,000-plus
  developers reports median pull-request review time up 441%, incidents per pull request up 242.7%,
  and bugs per developer up 54%. **Treat these numbers with suspicion.** They sit far above the
  survey framing above and far above the enterprise study at tier 4, which found revert rates
  unchanged across 196,212 pull requests. Three sources, three magnitudes, one direction at most.
  Cite the direction if anything, never these figures.

### Tier 6, Analyst-forecast

**"Over 40% of agentic AI projects will be canceled by end of 2027."** A research firm's
survey-based projection, mid-2025. Frequently restated as "40% of multi-agent pilots fail", which is
a different claim: this measures **business project cancellation**, projected, not observed technical
failure. Cite it as a forecast about funding decisions or not at all.

### Tier 7, Practitioner judgment

Named, credible, no comparison arm. Useful, and often more actionable than the measured findings, but
not evidence in the same sense.

- The agent is fallible and stochastic; the discipline is specification design, diff review, eval
  design, security oversight and taste. Surface assumptions as numbered options rather than choosing
  silently; define verifiable success criteria before starting; change only the lines the task
  requires and leave pre-existing dead code alone.
- An LLM pair programmer is over-confident and will not volunteer that it is wrong. Writing code is
  cheap now, so the bottleneck moves to verification. Automated tests are no longer optional.
- Codebase properties that help agents: plain SQL over ORMs, functions with long descriptive names
  over clever class hierarchies, permission checks kept locally visible rather than hidden in config,
  fast tools, and logs an agent can read. Unsupervised agentic loops amplify weak invariants and can
  produce code that passes tests while becoming globally incoherent.
- For high-quality systems work you have to stay fully involved; models are excellent amplifiers on
  bounded tasks and produce fragile results when left unsupervised on non-trivial goals.
- Giving an agent a way to verify its own work makes it self-correct more reliably than better
  prompting does.
- Test-first is a superpower specifically because agents introduce regressions that only pre-existing
  tests catch, and agents have been observed deleting failing tests rather than fixing the cause.
- **A record written at the end of a session, into a file rather than into a vendor's memory store,
  is what makes a workflow survive switching harnesses.** Added 2026-09-07 from a practitioner
  running one workflow across two vendors' harnesses. The reported failure is specific and matches
  what `OPERATING.md` predicts from first principles: the local files transferred, and everything
  held in one vendor's own session state or authenticated services did not. `HANDOFF.md` is the
  mechanism this collection puts against it.
- **One context file, read at the start of every session, that says which stream of work the
  repository belongs to.** Same source. The claim is that classifying the work up front removes an
  explanation the human would otherwise repeat every session, and prevents an agent inventing the
  classification. Note what this is: a **cost and repetition** argument, not an outcome one, and no
  comparison arm exists for it.

**Self-interest flag on both, since this collection insists on them.** The source is content
published about a subscription its author had just bought at a stated monthly cost, which is a
reason to read the accompanying performance and quota claims as advocacy. Those claims are **not**
adopted here: they are vendor plan mechanics, they rot within a quarter, and `SKILL.md` treats a
stale administrative fact as a defect. The two mechanisms above stand on their own merits and are
tier 7 like everything else in this section.

### Tier 8, Unverifiable

- **"Orchestrator context overflow starts at 4+ workers."** Architecturally plausible and consistent
  with the context-degradation findings, but traced only to a practitioner pattern site with no
  benchmark, token count or model disclosed. Cite as engineering judgment.
- **The instruction-file line-count targets.** 20-30, 150 and 200 all circulate. None is measured.

  **Four independent appearances in three days, 2026-09-08 to 2026-09-11, none citing a measurement,
  and this is the strongest corroboration any tier-8 entry here has.** A repository's own instruction
  file asserted that passing roughly 150 lines costs 20% more inference with no gain, citing nothing,
  found by the first adoption run. A vendor-neutral architecture document put the figure at roughly
  200, attributing it to a vendor. A research summary put it at roughly 150, attributing it to an
  open standard's guidance. And the number circulates as 20-30 in the shortest advice. **Four
  numbers, four sources, one range of nearly ten to one, and not one of them names an experiment.**

  What makes this worth recording rather than repeating: the claim is **not** that a shorter file is
  no better. It may well be. The claim is that **a specific threshold is being passed between
  documents and gaining confidence with each hop**, which is the mechanism this collection was built
  to interrupt. A number nobody measured does not become measured by being repeated by a vendor, a
  standards body or a search engine's summary. Treat every one of these as judgment.

---

## Administrative facts are not research claims

The tier scale grades findings: something somebody measured, with a method that can be reviewed. A
donation, a governance change, a supported-tool list or an adoption count is a different kind of
statement. It has no method to review, so a review-trail scale grades it badly, and stuffing it into
tier 8 as this document previously did understates a fact confirmable from a primary organisational
record.

Grade these three ways instead: **primary record** (the organisation's own announcement or registry
entry), **vendor-claimed** (a number only its beneficiary publishes), or **aggregated** (a figure
circulating with no traceable origin).

**`AGENTS.md` and the ecosystem around it**, rechecked 2026-09-02:

- **Primary record.** Donated to the Agentic AI Foundation under the Linux Foundation on
  **2025-12-09**, by OpenAI and Anthropic jointly, alongside two other projects. Confirmed against
  the Linux Foundation's own announcement, so the governance detail this document previously left
  unchecked is now checked. Upgraded from tier 8.
- **Vendor-claimed.** The **"60,000+ adopting repositories"** figure originates in the foundation's
  own materials and is repeated verbatim by secondary blogs. No independent audit found. Cite it
  with its owner attached or not at all.
- **Aggregated, and softer than it looks.** The native-adopter list is real in direction and **not
  canonical**: which tools appear varies by source, across at least fifteen candidates. So "read
  natively by nine or more tools" should be stated as a direction rather than a roster.
- **No stable versioned specification was found.** Anyone depending on a fixed spec version should
  check before relying on it.
- **The skill format itself is now a cross-tool standard**, natively supported well beyond one
  vendor. A collection like this one therefore travels as a skill and does not have to degrade into
  a single instructions file to be portable.

**Why this section exists at all:** every fact in it is the kind that goes stale in months. A
document that grades its research carefully and then asserts an adoption number as timeless has
moved its weakest claim to where nobody is checking. Recheck this section on the cadence, and treat
a stale entry here as a defect rather than as background.

---

## Contested between verification passes, 2026-09-04

**A category this document did not have, and it is different from a disagreement between sources.**
Here the *sources agree with themselves*: two independent verification passes read the same primary
material and **extracted different figures**. That is a defect in the reading, not in the field, and
it means neither number can be asserted.

Both passes were competent, both cited primary material, and **neither can be preferred without a
third read**. Recording them rather than picking is the only honest option, and each entry names what
would settle it.

**1. The pull-request size numbers. SETTLED 2026-09-08 by reading the book, and the resolution is
better than either pass.** `WORKFLOW.md` leads on the claim that "keep pull requests under 400 lines"
misreads a 2006 study by turning a review *rate* into a *batch size*. One pass reported the study's
recommendation as **100 to 300 lines over 30 to 60 minutes**, with **400 lines per hour** as the rate
and defect density high *below* 200 lines. A second reported **200 to 400 lines over 60 to 90
minutes** yielding 70 to 90% defect discovery, rate threshold **under 500 lines per hour**.

The book was obtained and read. **Neither pass reported it correctly, and the second pass's error is
the finding.** Its "200 to 400 lines" and "70 to 90%" come from a Q&A about reviewing your own code
which reads, verbatim: *"your overall speed is going to be about 200 to 400 lines of code per hour...
you should expect to get a 70 to 90% yield."* **That is a rate and its yield.** The pass converted a
rate into a size, which is precisely the misreading this collection was arguing the popular rule
commits. A verification pass reproduced the error it was sent to adjudicate.

What the book measures, quoted: reviewers **slower than 400 lines per hour** were above average at
finding defects and above **450 lines/hour** defect density was below average in **87% of cases**;
**below 200 lines** produced a relatively high defect rate, "often several times the average"; and
reviewers **wear out after 60 minutes**. From those it *derives* a size ceiling in a hedged sentence:
*"a reviewer will **probably** not be able to review more than 300-400 lines of code before his
performance drops."*

**So the headline was right about the mechanism and too strong about the conclusion.** The 400 is a
rate. A 300-400 line ceiling is also in the book, as a stated hypothesis rather than a measurement,
so the popular rule is a reasonable heuristic misquoted as a finding rather than pure folklore.
`WORKFLOW.md` now carries the quotations and the distinction. **The book also flags a limit on its
own strongest size result**: it assumes true defect density is constant across large and small
changes, which the collection would otherwise have had to notice for it.

**2. The developer-written context-file gain.** One pass reported **+2.4% on average**; a second
reported **4% on average on the purpose-built benchmark**, at a cost of 3.34 extra steps and up to
19% more spend. These may both be true of different tables. **This collection previously "corrected"
4% to 2.4% on the strength of one pass**, which was premature. Settled by a direct read of the
paper's results tables. The rule built on it depends only on the direction and is unaffected.

**3. Two venue statuses. Both settled 2026-09-07, and they settled downward.** For the
adversarial-review paper, one pass confirmed acceptance at an ICML 2026 workshop; a second noted the
arXiv text carries **no acceptance line**, with acceptance known only from external commentary. For
the agent-context-file mining study, one pass called it a preprint; a second observed an **ISBN and
ACM subject categories** in the arXiv version, suggesting proceedings publication.

A recheck went looking for a publisher record for each and found neither. The adversarial-review
paper's acceptance rests on the author-supplied arXiv `Comments` field, so it **moved from tier 2 to
tier 4**. The mining study's only DOI is the arXiv one, `10.48550/arXiv.2511.12884`, so the ISBN hint
does not indicate proceedings publication and it **stays at tier 4**, where it already sat. The
prediction in the previous version of this entry, that this collection's tier 2 was doing more work
than its evidence supported in these two cases, was correct in one of them.

**Why this section exists at all.** Independent verification was meant to raise confidence, and on
most items it did: the majority of figures came back confirmed, several with added precision. But on
four items it **lowered** confidence, which is what independent verification is for and is the
opposite of what a document usually reports after a review pass. A collection that only ever gains
certainty from checking is not checking.

---

## Disagreements, left standing

**The reviewer's disagreement instruction, against the vendor's caution about it.** Added 2026-09-08.

- **This collection says**, on arXiv:2608.18167 (tier 2, ICML 2026 DL4C poster): a reviewer agent
  without an explicit disagreement instruction produced the worst measured F1 in its comparison by
  agreeing with the implementer, and adding the instruction produced the best.
- **Anthropic's best-practices page says**, verbatim, read 2026-09-08: *"A reviewer prompted to find
  gaps will usually report some, even when the work is sound, because that is what it was asked to
  do. Chasing every finding leads to over-engineering: extra abstraction layers, defensive code, and
  tests for cases that can't happen. Tell the reviewer to flag only gaps that affect correctness or
  the stated requirements, and treat the rest as optional."*

**They are not measuring the same failure.** The paper measures under-reporting, a reviewer that
converges on the implementer's conclusion. The vendor warns about over-reporting, a reviewer that
manufactures findings because it was asked for findings. Both are real and they are opposite ends of
the same dial.

**Default, and it is judgment rather than evidence:** keep the disagreement instruction and bound its
output. Tell the reviewer to disagree, and to flag only gaps affecting correctness or the stated
requirements. That is cheaper to reverse than either extreme, and it is what both sources would
predict works.

**Recorded because the collection had two expired vendor-conflict claims and zero live ones**, which
is the wrong ratio for a document whose conflict section is one of its selling points.

Not averaged into a consensus that does not exist.

**And each one now names what to do anyway, because "the evidence is split" is not an answer to a
question you have to settle today.** Added 2026-09-03 after an external review pointed out, correctly,
that an honest map of uncertainty is not by itself a decision tool.

The rule for these defaults: **pick the option that is cheapest to reverse and least damaging if the
other side turns out right, and label it judgment rather than evidence.** That is the same logic as
the asymmetric-burden rule, applied to a tie rather than to a weak source. A default chosen this way
is not a finding, and it must never be cited as one.

Each disagreement below carries a **Default** line on that basis.

**Does an agent context file rot like documentation? This collection says yes and the one study says
no.** Added 2026-09-03, and it is the clearest external contradiction of a first-party claim here.

`DOCS.md` treats instruction and context files as documentation subject to the same rot taxonomy as
everything else. arXiv:2511.12884, across 2,303 context files in 1,925 repositories, found they
behave as **living configuration**: frequently edited in small increments rather than left to decay.

Both can be true, and the reconciling variable is probably repository activity: a file edited weekly
does not rot, and the first-party observations here come from repositories where nobody revisited the
file for two hundred commits. But **the study has 1,925 repositories and the counter-claim has
five**, so the honest statement is that the rot taxonomy is **not established for agent context
files specifically**, and `DOCS.md` now says so where it makes that claim.

**Default while this stands:** treat an instruction file as configuration for *maintenance* purposes,
so edit it freely and do not schedule ceremonial audits of it. But still run the cheap mechanical
checks against it, the path checker and the count reconciler, because those cost nothing and catch
real drift whichever side is right. Judgment, not evidence.

One finding from the same paper is not in tension and is worth acting on directly: context files
cover tests at 75.9% and architecture at 68.1%, and **security at 14.8% and performance at 14.5%**.
Whatever else those files are, they are not carrying security context.

**How much harm does AI-assisted throughput actually do?** Three sources, one rough direction, wildly
incompatible magnitudes. An enterprise study of 196,212 pull requests found review load doubling
while **merge and revert rates held steady**. An industry survey found a negative association with
delivery stability. Vendor telemetry reported incidents per pull request up 242.7%. The first has the
best design and the least alarming result, which is a pattern worth noticing rather than resolving.

**Default while this stands:** plan for **review capacity** rather than for a defect surge. Add
reviewers or reviewing time before adding gates, because the best-designed study found load doubling
while revert rates held. If the alarming figures turn out right you will need the capacity anyway; if
they are wrong you have lost nothing. Judgment, not evidence.

**Do instruction files help or cost?** One study finds them raising cost 20-23%; another finds them
cutting runtime 28.6% and tokens 20%. Both are primary sources with disclosed methodology and they
disagree on the direction of the efficiency effect. The likely reconciling variable, untested by
either, is content quality and length rather than mere presence. Both broadly agree the correctness
effect is small.

**Default while this stands:** keep a **short, human-written** instruction file and no repository
overview. That is the one direction anything was measured in, the cost is bounded and visible, and
deleting a file later is free. **Do not generate one**, because generated files are the single case
where a measured effect points at harm. Judgment, not evidence.

**Positive or negative phrasing?** Practitioner guides advise writing constraints as positive
directives. The largest study of real rule files measured the opposite: positive directives were the
individually harmful ones. Tier 4 measured beats tier 7 advice here, but the disagreement is real and
the study is a preprint.

**Default while this stands:** use prohibitions, and above all use them **consistently**. Choosing a
phrasing convention retires no practice, so the asymmetric-burden rule does not bite, and mixed
phrasing is worse than either style whichever turns out better. Judgment, not evidence.

**Does test-first help?** Two credible practitioners advocate it from experience. The one controlled
study on agents found the procedural instruction alone made things worse and the *context* did the
work. No controlled comparison of test-first versus test-after for agents exists.

**Default while this stands:** supply the **test-impact context** and skip the ceremony. The one
controlled study found the procedural instruction alone made things worse and the context did the
work, so the ordering is the part with no support and the context is the part with some. Judgment,
not evidence.

---

## Open gaps

No primary source found by any pass. Do not present these as resolved.

1. **Prompt and output compression evaluated on agentic coding task success**, as opposed to
   question-answering or summarisation benchmarks. The published compression results are real and are
   measured on the wrong workload. Losing one load-bearing token in an agentic loop, a file path or
   an exact error string, is qualitatively different from losing detail in a summary.

   **No longer sourceless, as of 2026-09-02: partially addressed, tier 4.** arXiv:2607.09691
   measured compressed context against full files on a real code-editing workload and found it
   **matched full files while using one-third of the tokens**. That is the right workload, which is
   what this gap was asking for. It is not closed: one single-author preprint, and the same paper
   reports that **roughly 9% of per-instance outcomes flip between byte-identical temperature-0
   runs**, which bounds how much any single-run agent measurement in this document can carry,
   including its own.

   **Second data point, 2026-09-03, and this gap is now effectively closed on direction.**
   arXiv:2601.16746 reports 23 to 54% token reduction on agent tasks on the same benchmark while
   improving success rates, by a completely different method. Two independent measurements on the
   right workload, both saying compression is affordable there. What remains open is the boundary:
   nobody has characterised *which* content is safe to drop, and the load-bearing-token worry that
   opened this gap is unaddressed rather than refuted.

   The nondeterminism pair at tier 1 also came out of this line of work, and it partly undercuts
   both compression results, since each rests on single-run comparisons on a benchmark now measured
   to move several points run to run.

   **Narrowed 2026-09-06, and the boundary now has a first shape.** An independent pass found
   arXiv:2601.16746 (SWE-Pruner, preprint) proposes **task-aware adaptive pruning** and reports that
   **uniform compression hurts more than task-aware pruning** on repository-level editing. That is
   the first direct evidence that *which* tokens are dropped matters, not only how many. It stops
   short of what this gap asks for: it publishes no ablation by content type.

   Two weaker signals, both tier 7, both practitioner analysis rather than measurement, and reported
   because they name candidates for what to test rather than because they establish anything:
   summarisation is said to lose **negations and constraints, exact numbers and thresholds, goal
   refinements, records of what was rejected, and tool-output attribution** first; and compressing an
   agent's *control* context (system instructions, tool schemas, policies) is said to produce a
   reliability cliff. **Neither is a controlled ablation and neither should be cited as a finding.**

   **What would close this: an ablation that varies exactly one content class**, exact error strings
   being the obvious first candidate, and reports the task-success delta. Nobody has run it.
2. ~~**Whether a reviewing agent seeing the implementer's reasoning causes false consensus**, versus
   diff-only review.~~ **Closed 2026-09-02. Closed at tier 2 then, at tier 4 since 2026-09-07**,
   when the paper's acceptance turned out to rest on an author-supplied field. arXiv:2608.18167
   measures the false-consensus failure directly and measures a fix for it, and it also answers a
   question this document never thought to ask, which is how many reviewer agents to use. Three beat
   five. Kept visible rather than deleted, because a gap that stood as sourceless while a paper
   answering it already existed is itself the finding: the gap list records what four research passes
   failed to find, not what does not exist. Re-search the remaining two on that basis.
3. **Any empirical link between code-structure choices and agent task success.** ORMs, language
   features, indirection, module boundaries. **Partially answered 2026-09-03, tier 4.**
   arXiv:2605.06445 measured 8 web frameworks across 100 tasks and found data-layer and ORM defects
   the dominant failure mode, with convention-heavy frameworks performing worse than minimal ones.
   One group, no replication. Still open for the specific comparisons: ORM against plain queries as
   a controlled variable, monorepo against polyrepo, and file size. **Searched and not found**, as
   opposed to confirmed nonexistent.

   **Re-searched 2026-09-06 by an independent pass and still not found.** Exact strings tried:
   `"ORM vs hand-written queries" "agent" "task success" controlled`; `"monorepo vs polyrepo" "AI
   agent" "edit success" controlled experiment`; `"file size" "agent" "code edit" success controlled
   variable`. The monorepo-versus-polyrepo question has practitioner writing arguing that monorepos
   simplify context assembly, **with no measured outcome of any kind**, which is tier 7 and does not
   touch the gap. No replication of the framework-convention result was found either.
4. **A controlled comparison of defect rates with and without AI assistance. Narrowed on 2026-09-04,
   and the previous wording was closer to overclaiming than it should have been.** This document
   says repeatedly that no practice here has tier-1-or-2 defect-reduction evidence.

   **What changed.** A peer-reviewed two-phase controlled experiment with 151 participants exists on
   the adjacent question, and its answer is that the writing gets 30.7% faster while downstream
   evolution time and code quality show **no significant difference**. That is a real controlled
   result from a reviewed venue, on a question this document had been describing as unstudied. It
   measures **maintainability and evolution effort, not defect rates**, so the specific gap stands,
   but it is far narrower than "nobody has measured this" implied.

   **On defect rates specifically, the original search still holds.** Searched deliberately on
   2026-09-03, and it holds. No study was found meeting all
   three of: random assignment, a genuine defect outcome rather than a proxy, and adequate power.
   The near misses each fail a different axis, which is itself the useful result:
   - A vendor randomised trial, N=202, measures test-pass rate and expert quality ratings, not
     defects found later.
   - A practitioner study, N=785, measures real bugs and reports a 41% higher rate, but is not
     randomised and conflates tool *access* with tool *use*.
   - A randomised trial, N=96, measures time on task only.
   - A vendor release reporting a 30% defect-risk figure is correlational on code-health quintiles,
     with no AI comparison arm at all.

   **Re-searched 2026-09-06 and the status hardens from "could not confirm" toward "confirmed
   absent".** Thirteen further query strings against the SE venues returned no qualifying study. The
   largest randomised work now known is **Cui, Demirer, Jaffe, Musolff, Peng & Salz, "The Effects of
   Generative AI on High-Skilled Work", Management Science 2026, DOI 10.1287/mnsc.2025.00535**, tier
   2. N=4,867 developers pooled across three RCTs, preregistered, randomised tool access. It reports
   a **26.08% increase in completed tasks (SE 10.3%)**, plus more commits and more compiles.

   **It collects no defect outcome at all**, and its own co-author says so: the researchers did not
   have access to the code produced and were unable to evaluate its quality, naming that as an
   important next step. So it fails bar (b) by design rather than by accident.

   **That is the more useful finding, and it changes what closing this gap would take.** The largest,
   best-powered, preregistered randomised platform in the field deliberately did not instrument
   defects. Closing Gap A therefore looks less like mounting a fresh trial and more like **bolting a
   defect secondary-outcome onto an existing productivity RCT**. Recorded as a new gap below.

   Also newly logged as failing a different bar: a Google enterprise RCT (arXiv:2410.12944, N=96,
   about 21% time reduction, time-on-task only) and a peer-reviewed Meta study at FSE 2025 (DOI
   10.1145/3803437.3805217) whose outcome is review-state time rather than defects.

   Search terms used, recorded so the next person can do better rather than repeat it: randomised
   controlled trial AI coding defect rate control group; randomized controlled trial AI code quality
   bugs; no controlled study defect rate AI-assisted coding; escaped defects AI coding assistance
   randomized controlled experiment; bug injection randomized experiment professional developers;
   difference-in-differences defect density AI assisted.

   **This is a "could not confirm", not a "confirmed absent".** The distinction matters here more
   than anywhere: the whole collection leans on this gap, so anyone who finds a qualifying study
   should assume this entry is out of date rather than that the study does not exist.

   **The nearest thing found, named 2026-09-08 so the gap does not overstate how empty it is.**
   arXiv:2601.02200 associates Code Health with semantic preservation after LLM refactoring across
   5,000 files. It is not randomised, the corpus is competitive programming rather than fielded
   software, and the outcome is refactoring preservation rather than defects that reach anyone. **So
   it does not close this gap and it is the closest anyone has come.**
5. **Nobody is instrumenting defects on the trials that could carry it.** Opened 2026-09-06 out of
   gap 4. The field's largest randomised platform had 4,867 subjects, preregistration, and no defect
   outcome. This is a gap in *research design*, not in the literature: the studies exist and collect
   the wrong variable. Anyone with access to one of those programmes could close gap 4 far more
   cheaply than by starting over.
6. **The grader is becoming an agent, and nobody has asked what that does to reproducibility.**
   Opened 2026-09-06. Agent-based artifact evaluation now exists (arXiv:2602.02235, a rubric named
   ArtifactGuide and an evaluator agent named ArtifactCopilot, evaluated on 60 real artifacts against
   human-adjudicated badges) and it runs **repeated passes specifically to handle its own evaluator's
   nondeterminism**.

   **The paper reports three-run mean exact badge agreement of 70.56% for its best system**, which is
   what this entry said originally. It was "corrected" on 2026-09-07 to say the qualifier belonged to
   a different sentence, and the correction was wrong. The paper's introduction reads, verbatim:
   *"Across all evaluated systems and protocols, ARTIFACTCOPILOT achieves the highest three-run mean
   exact badge agreement at 70.56%."* Its methods section adds: *"All results reported for RQ1 and
   RQ2 are three-run means."* **Restored 2026-09-08 from the PDF. See error 19**, which is now about
   the withdrawal rather than the figure.

   Separately, the rubric improves coding agents' three-run mean exact badge agreement by **10.55 to
   28.34 percentage points** over ACM badge-policy prompts.

   **The number that matters most for this gap is neither of those, and it is worse than both.**
   Across three repeated runs on 60 artifacts, the best system reproduced its own badge on **32 of
   60**. The baselines: 37/60, 35/60, 21/60, 12/60. Failure rates, meaning runs that produced no
   review report at all, ran from **0% for the best system to 45%** for the worst. So a majority of
   artifacts got a different badge depending on which run you looked at, from the system that
   agreed with human adjudication most often. **Agent nondeterminism is not a caveat on artifact
   evaluation. At these numbers it is the dominant term.**
   So agent nondeterminism, this collection's only multiply-replicated finding, now threatens the
   **badging process** and not merely the artifacts being badged. The collection has no entry for
   nondeterminism of the evaluator and needs one.
7. **A binding legal provenance regime arrived under a set of voluntary conventions.** Opened
   2026-09-06. The **EU AI Act, in force 2 August 2026**, requires AI-generated public text to be
   labelled, and at least one major foundation now says so in its own guidance. Every provenance
   entry in `RESEARCH.md` is framed around voluntary trailers. Announcements, advisories, release
   notes and website copy are a different axis with actual enforcement, and there is no entry for it.
8. ~~**The aggregate security direction is contested and this collection asserts one side.**~~
   **Adjudicated 2026-09-06 rather than closed.** Both full texts were read. The disagreement is real
   but narrower than it looked: different populations, different analyzers, different normalisation,
   and **both find elevated high-risk patterns in at least one cut**. Kept visible rather than
   deleted, because the useful residue is that **neither study measures whether human review catches
   any of it**, which is gap 10.
9. **What fraction of repositories retain a review trail at all.** Opened 2026-09-06. The collection's
   most-wanted counter-example was a repository with a retrievable review trail, and a search found
   several: Gerrit corpora with reviewer and approver metadata across roughly 133,000 changes in 14
   projects, GitHub pull-request corpora across 37 projects, and tooling for extracting review
   metadata at scale. **So retrievable review trails plainly exist**, which weakens the collection's
   implicit framing that their absence is normal.

   **What nobody has published is the population figure**: what proportion of repositories, overall
   or by platform, retain any reviewer record. That single number would settle whether this
   collection's four-for-four observation is a quirk of four small repositories or a property of how
   git and its hosts are used. Exact string tried and not found: `"fraction of repositories" "review
   trail" git`.
10. **Whether human review catches AI-introduced defects at normal rates.** Opened 2026-09-06 out of
   gap 8. Two large studies count static-analyzer alerts on AI-generated code and **neither measures
   reviewer catch rate**. Every practical recommendation in this collection about reviewing agent
   output rests on the assumption that review works on it roughly as well as it works on human code,
   and that assumption is untested in either direction.
11. **Agent memory architecture is unmeasured, and this collection has no entry for it at all.**
   Opened 2026-09-06. A 2026 survey (arXiv:2603.07670) organises the space into five mechanism
   families and says plainly that empirical comparisons for coding agents are sparse. Everything else
   found was practitioner architecture writing with **no measured outcome**: three-tier patterns,
   write-manage-read loops, consolidation and decay, all tier 7.

   **No study was found showing that retrieval-augmented memory beats a flat file for coding-agent
   task success**, and no controlled study of memory decay or consolidation tied to edit success.
   Recorded because this is a daily practice for many people running on folklore, and because a gap
   with a mature-looking vocabulary is more dangerous than one that is obviously empty.

   **Rechecked 2026-09-07 against a fresh practitioner account and unchanged, which is the finding.**
   A new architecture description arrived, was read, and turned out to be another instance of the
   category this gap already names: an uncontrolled single-setup report with no comparison arm. It
   changed the tier-7 section and not this gap. **Rediscovery is not replication**, and a gap that
   says "all that exists here is practitioner architecture writing" is not closed by more
   practitioner architecture writing, however good the architecture is.

---

## This document's own errors

Kept deliberately, because they are the argument for the scale.

1. A submission line was read as a review trail, tiering a paper as reviewed when its venue had not
   accepted it.
2. The polarity study was cited as tier 3 when it has no venue at all.
3. A tier-4 self-published preprint was used to instruct the downgrade of a standing practice.
4. A source was cited as support after being read only through a thin automated summary, and later
   proved unverifiable with available tooling. It was removed rather than downgraded.
5. Three separate tools were reported as installed and working on the strength of a file or command
   existing. None of the three worked.
6. **A correctly sourced finding was restated with the wrong numbers, twice in one sentence.** The
   agent-skill security study was reported as prompt injection in 36% of skills with 1,467 malicious
   payloads. It measured a security flaw of any kind in 36.8% (1,467) of them, with 76 confirmed
   malicious payloads. The source was right; the retelling narrowed a broad category and inflated a
   count nineteenfold, in the security file, where an inflated threat number is the most damaging
   place to be wrong.
7. **A source was cited as saying the opposite of what it found.** The instruction-file study was
   reported as finding authorship irrelevant. It found generated files harmful and
   developer-written files mildly beneficial. Same paper, inverted conclusion.
8. **One paper was counted as two.** The 4-point developer-written-file result was read as a separate
   rebuttal by another author. It is internal to the paper it was said to rebut, so a single source
   was briefly doing the work of a disagreement between two.
9. **A verification check passed because it was inert.** The link checker prescribed in `DOCS.md` was
   run across this collection and reported it clean. It had extracted **zero** references: the
   pattern was broken, so it compared an empty list against the filesystem and exited successfully.
   The clean output and the broken output were identical. Caught by feeding it a filename known not
   to exist, which showed the comparison working while the extraction returned nothing; the fixed
   version found 17 references, all resolving.

   This one is a category the earlier entries missed. Errors 1 to 5 were unverified claims. Errors 6
   to 8 were paraphrase drift. **This is a verification instrument reporting success while measuring
   nothing**, which is worse than either, because it manufactures confidence rather than merely
   failing to supply it. The rule is in `DOCS.md`: make a check fail once, deliberately, before
   believing it when it passes.
10. **A search reported "confirmed absent" while looking for the wrong string.** An inventory of a
    large codebase reported **no pull-request-mediated merge flow anywhere in its history**. It had
    searched for the merge-commit wording used by one hosting platform. The repository was hosted on
    a different platform, whose wording differs. **36 real pull requests returned zero matches**, and
    the absence was written up with full confidence and published in this collection before being
    caught.

    Three things make this the most instructive entry on the list:

    - **It was caught by the reader, not by the author or the tool.** Someone who knew which platform
      the repository was hosted on asked whether the assumption held. No amount of internal rigour
      substitutes for the person with the missing context.
    - **It defeated the existing rule.** This document already required distinguishing *could not
      confirm* from *confirmed absent*, and the report said confirmed absent, correctly by its own
      lights: the search ran, completed, and matched nothing. **The rule protects against an
      unreached source, not against a well-executed search for the wrong pattern.**
    - **The corrected finding was better than the wrong one.** "The mechanism existed, was barely
      used, produced no review anyway, and was dropped with nothing recording the decision" is a
      sharper finding than "they never had one", and the first version had reported the second.

    New rule, since the old one did not cover this: **before reporting an absence, state what string
    or shape you searched for and confirm that shape is the one this system would produce.** A grep
    for a convention the target does not use returns zero, indistinguishable from a true absence.

    **Reproduced live, 2026-09-10, in a second repository, against the rule written to prevent it.**
    This is the only entry on the list with an independent replication, and it happened during the
    first adoption run rather than during a verification pass.

    Deriving the `reviewers` field, the procedure's own instruction is to try more than one hosting
    platform's wording. Against a repository whose history is entirely self-merged by one author,
    the searches disagreed completely:

    | Query | Result |
    |---|---|
    | The most widely documented platform's anchored wording | **0** |
    | The wording of the platform the repository is actually hosted on | **33** |
    | Case-insensitive, unanchored | 37 |
    | Two further platforms' wordings | 0 each, correctly |

    **The expected shape and the actual shape share no anchored prefix**: one names the pull request
    number after the branch, the other names the branch first and parenthesises the number. Had only
    the first query run, the profile would have recorded a repository with **no pull-request flow at
    all**, confidently, because a clean zero from a well-formed query is indistinguishable from a
    genuine absence.

    **And the finding that would have been lost is the character of the flow, not its existence.**
    All 33 merges carry **identical author and committer identity**, which makes it a
    continuous-integration gate rather than review. Recording `none` and recording `reviewers: one`
    would both have been wrong, in opposite directions, which is the same shape as this entry's
    original third bullet.

    **What would have caught it earlier than four parallel searches: read the platform off the
    configured remote before choosing the query, rather than after.** The remote URL names the host
    in one command and costs nothing, and it converts "try several wordings and hope" into "look up
    this host's wording". The multi-wording sweep stays as the safety net; it was never the right
    primary method for a question with a direct answer. `PROFILE.md` now says so.

    **Two things this replication establishes that the original could not.** The failure is not a
    property of one careless search: it recurred with the rule in force, in a different repository,
    on a different platform, run by a different agent. And **the multi-wording mitigation works and
    is still the wrong shape**: it caught the problem here, at the cost of four queries and a
    reader who thought to doubt a zero.
11. **A rewrite silently broke the field that routes this skill.** Shortening the frontmatter
    `description` to fit a 200-character platform cap introduced a colon followed by a space. A YAML
    plain scalar **cannot contain `": "`**, so the value truncated at the first colon and the tool
    fell back to displaying the document's heading instead of the description.

    Why this one is instructive rather than merely embarrassing:

    - **Every check in place passed.** Character count: fine. Em dashes: none. Identifier scan:
      clean. Link check: clean. None of them knew the field had a format constraint, so all of them
      reported success on a broken file.
    - **The symptom was visible and nearly ignored.** The tool's own listing changed from the
      description to the heading. That was the instrument reporting the fault, and the temptation was
      to read it as a display quirk. **Checking it was what found the bug.**
    - It is the fourth instance of the collection's dominant shape: something that ran cleanly and
      was wrong about what it produced. The others were the inert link checker, the wrong-platform
      search, and a file count that counted a virtual environment.

    New rule: **a field with a format constraint needs a check that knows the format.** For a skill
    frontmatter, that means parsing it as YAML rather than measuring its length, and confirming the
    value that comes back is the value you wrote. Length checks and content checks are not
    substitutes for a parse.
12. **A figure was attributed to the wrong paper, and another was overstated by more than half.**
    Both found on 2026-09-04 by fetching primary sources for every external claim in this document
    rather than trusting what a research pass reported.

    - The **1.5x bug-introducing** figure for inconsistent comments was credited to a 2019 mining
      study of 1.3 billion changes. **It is not in that paper.** It belongs to a later, separate
      paper. The 2019 study's actual finding is about *timing*: impact is highest immediately after
      an inconsistency appears and decays afterwards. Two papers had been fused into one citation,
      and the more useful of the two findings was the one being discarded.
    - **Developer-written instruction files gained 2.4% on average, not "roughly 4%".** Overstated
      by more than half. The rule built on it survives unchanged, because the rule depends on the
      *direction* rather than the size, but a reader checking the number would have found it wrong.

13. **An unverified sub-claim propagated to four documents before anyone checked it.** The
    nondeterminism entry had acquired a detail about interquartile ranges at different temperatures.
    A direct read of the paper found only standard deviations and min-max ranges: **no interquartile
    comparison exists in it.** Unconfirmed rather than contradicted, and removed.

    The instructive part is the spread. One unchecked detail, added once, had reached `SKILL.md`,
    `OPERATING.md`, this file, the changelog and the published page. **A claim's blast radius is
    every document that cites it**, and nothing here tracked that. New rule: **when a figure is
    corrected or retracted, grep the whole collection for it before considering the correction done.**
    The changelog is the exception and is corrected by a new entry rather than an edit, per this
    collection's own rule about history.
14. **A fabricated statistic was carried in this collection for a day, and it is the most serious
    error on this list.** A figure reporting that a single agent matched or beat multi-agent systems
    on **64% of benchmarked tasks**, with multi-agent adding **2.1 percentage points at roughly twice
    the cost**, was attributed to a named university group.

    A verification pass traced the exact wording to **a search-engine-optimised blog post that names
    no paper, no author and no identifier**, then fetched the one genuinely related paper in full and
    **found none of those numbers in it**. The attribution appears to be invented.

    Why this is worse than every earlier error here:

    - **It was not drift. It was laundering.** Errors 6 to 8 were real sources restated badly.
      Errors 12 and 13 were real sources misattributed or over-read. **This had no source at all**,
      and it arrived wearing an institutional name that made it feel checkable.
    - **A research agent produced it and this document recorded it.** The failure was not the
      agent's alone: a specific, quotable, flattering statistic with a prestigious attribution is
      exactly the shape of claim that should have triggered a primary-source check *before*
      publication, and it did not, because it agreed with a position already held.
    - **It survived one external review.** The reviewer that caught three real design flaws did not
      catch this, which is a useful limit on what review buys you.

    Recorded as **could not source** rather than **confirmed false**: extensive searching found no
    primary source, which is not proof none exists. New rule: **a statistic that is specific,
    quotable, and agrees with you gets its primary source fetched before it is written down**, not
    after.

15. **Two independent verification passes disagreed with each other on four items.** Not with the
    sources, with each other. This produced the contested-findings section above, and one of the four
    calls a headline claim in `WORKFLOW.md` into question. Recorded as an error rather than a
    curiosity because **the earlier single-pass "corrections" were asserted with a confidence one
    pass does not earn.**
16. **A profile field was derived from the author's own context instead of from the repository, and
    asserted a security gap that had already been fixed.** Found 2026-09-04 by an agent following
    this collection's own adoption procedure on the repository in question.

    The profile recorded `maturity: prototype` and justified it partly on an auth default that fails
    open. **That had been fixed and merged three days before the profile was written**, and the
    repository's own readme already described it correctly. The field's verdict happened to remain
    right for other reasons, which is what made the error survivable and also what made it hard to
    see.

    Why this is the most self-indicting entry on the list:

    - **`PROFILE.md` contains a section titled "Maturity is derived, not declared"**, which exists
      because three of three repositories were found claiming a maturity their process contradicted.
      The author of that section then declared a maturity from memory rather than deriving it.
    - **The repository was telling the truth and the profile was not.** The readme was accurate. The
      derivation did not read it.
    - **It was caught by a reader following the written procedure**, not by the author and not by an
      external reviewer. That is the procedure working, and it is the first time this collection has
      been corrected by its own documented method rather than by inspection.

    New rule, and it is narrower and sharper than "derive it": **when deriving a field, read the
    repository's own current claims about that field and reconcile with them explicitly.** If the
    readme says a property holds and your derivation says it does not, one of you is wrong and you
    must say which before writing the field. A derivation that never consults what the repository
    asserts is not derived from the repository, it is derived from whatever you already believed.

    Corollary for anyone using an agent to derive a profile: **the agent's context is not evidence
    about the repository.** A long session accumulates stale facts that feel like knowledge, and a
    fact that was true last week reads identically to one that is true now.

    **A second instance, same day, different mechanism, and it produced a fix to the procedure
    rather than to a file.** A profile's `secrets` field listed one credential-bearing path. An agent
    following this collection's procedure found a second one: gitignored, never committed, carrying
    database URLs that can embed credentials, and simply never mentioned.

    The verification commands in `PROFILE.md` were correct and had been run correctly. **They were
    being pointed at a list assembled from memory.** The procedure said how to verify a candidate and
    never said how to find the candidates, so a complete-looking verification ran against an
    incomplete set. `PROFILE.md` step 3 now enumerates first, from the ignore file and from disk,
    before verifying anything.

    The general lesson is the sharper one: **a verification step is only as complete as the list it
    is given, and a procedure that omits the enumeration will produce confident partial results
    forever.** Nothing about the output distinguishes "checked everything" from "checked what
    somebody happened to remember".
17. **The identifier-leak check searched file contents while the identifier sat in the metadata of
    every commit. Then the fix searched one ref while the leak survived on another.** Found
    2026-09-04, twice in the same afternoon, in the same direction.

    The collection forbids naming an employer anywhere outside `LOCAL.md`, and `build.py` enforces it
    with a regex over every shipped file. On first publication the check reported no identifier
    leaks. **Every commit in the repository was authored and committed under an employer email
    address**, which is not file content, so neither `build.py` nor the `git grep` run alongside it
    examined it. The prose was de-identified and the commit headers re-identified it, which defeats
    the de-identification completely: one `git log` recovers what the rounding was there to hide.

    The rewrite that fixed it was then verified with `git log` on the current branch. **A second
    branch on the remote still pointed at the original commits**, so the address remained published
    while the check reported it gone.

    Why it earns a number rather than a footnote:

    - **It is error 9's shape a third time.** A check that cannot fail because its scope excludes the
      failure. The collection documents that class, states it as the worst failure available, and
      then shipped two fresh instances of it inside four hours.
    - **The two instances have the same cause, not two causes.** Both drew the boundary at what was
      convenient to search rather than at where the identifier could be. Content but not metadata;
      one ref but not all refs. Fixing the first did not suggest the second, which is the evidence
      that the underlying habit was never addressed.
    - **The consequence class is different from every other entry.** The rest are wrong claims, which
      mislead a reader and can be corrected in a later version. This one published an identifier that
      the collection's own publication gate exists to withhold, and a distributed identifier cannot
      be recalled by a version bump.

    New rule: **an identifier check runs against commit metadata across all refs, not against file
    contents on the current branch.** Concretely, `git log --all` over author, committer and message,
    reporting the number of commits and refs examined. Corollary, and it is the general form: **when
    a check has a scope, state what the scope excludes next to the result.** "No identifier leaks"
    was true of the files and false of the repository, and the output gave a reader no way to tell
    which had been measured.

    One asymmetry the new check encodes deliberately: **the prose pattern and the metadata pattern
    are not the same pattern.** Skill prose must name nobody, the author included. Commit metadata
    must name the author, because that history is the ownership record. Only the employer identifiers
    are forbidden in both.

18. **A measured finding about one thing was restated as measuring a different thing, in a shipped
    template.** Found 2026-09-06 by an independent verification pass, in `templates/AGENTS.md`, which
    had never been audited against this collection's own discipline.

    The template said **"do not add a directory tree: measured as not helping"**. What is actually
    measured is that **repository overviews** do not help. A directory tree is a plausible instance of
    the same idea and **no measurement of it was found**, by that pass or by this document.

    Why it belongs on the list rather than being quietly fixed:

    - **It is errors 6 through 8's shape, in the file most likely to be copied.** The tier was right,
      the underlying source was right, and the sentence retelling it widened the scope. A template is
      the worst place for that, because it propagates into other people's repositories verbatim while
      the file that could correct it stays behind.
    - **It has the signature this collection warns about.** Specific, quotable, and flattering to a
      position already held. That is hard rule 1, and the template predated it.
    - **The templates were a known unaudited gap and stayed that way for days.** `ROADMAP.md` listed
      them as the most likely place a stale or unsupported claim was still sitting. It was right, and
      naming a risk is not the same as retiring it.

    Corrected by scoping rather than deleting: the measured claim keeps the word measured, the
    unmeasured extension is labelled judgment, and the independent reason to drop a directory tree,
    that it duplicates the readme, is stated on its own merits.

    New rule: **when a rule generalises a measured finding to a neighbouring case, the sentence must
    say which half was measured.** "Measured as not helping" attached to a broader category than the
    measurement covered is a claim nobody can trace back to a defect.

19. **A correct figure was withdrawn on weaker evidence than the assertion had required.** Found
    2026-09-08 by reading the PDF. **This entry originally described the opposite error and was
    itself wrong.**

    Open gap 6 read "three-run mean exact-badge agreement of 70.56%". A verification pass reported
    that the abstract does not state that figure. It does not: the abstract says "the highest
    badge-level agreement at 70.56%". On the strength of that, this document rewrote the entry,
    declared the qualifier had been welded on from a neighbouring sentence, and recorded an error.

    **The paper's introduction says, verbatim: "ARTIFACTCOPILOT achieves the highest three-run mean
    exact badge agreement at 70.56%."** Its methods section says all RQ1 and RQ2 results are
    three-run means. The original text was right, the pass was right about the abstract, and the
    inference from one to the other was wrong.

    Why it earns a number, and why it may be more instructive than the error it replaced:

    - **Every rule in this collection points one way, and the failure went the other way.** Hard rule
      1 forbids asserting a figure you have not seen in the primary source. Nothing forbade
      *retracting* one on the same evidence, and the asymmetric-burden rule protects safeguards, not
      figures. So a correct number was removed on a secondhand read of an abstract, by a document
      whose entire argument is that you do not do that.
    - **The withdrawal was more confident than the assertion had been.** It came with a new rule, a
      numbered error, and a paragraph explaining why the mistake was subtle. All of that was
      constructed on a source nobody had opened. **Constructing an explanation is not evidence that
      the thing being explained happened.**
    - **The environment was the proximate cause and not the excuse.** arXiv was unreachable, the
      limitation was recorded honestly, and the work proceeded anyway rather than waiting for the
      PDF. Recording a limit is not the same as respecting it.

    New rule: **a withdrawal needs the same primary-source standard as an assertion.** If the source
    could not be opened, the correct output is "this figure is unverified pending the PDF", left in
    place and flagged, not removed and explained. Removing a claim feels conservative and is not: it
    is an equally strong assertion about the source, made on the same missing evidence.

20. **Tier 2 was being awarded on things that are not venue records. Four entries, and the audit
    that found them only happened because a third pass questioned one of them.** Found 2026-09-07.

    This scale defines tier 2 as peer-reviewed and accepted, **confirmed against the venue or a
    publisher DOI**. A pass flagged that the arXiv `Comments` field, where several of these
    confirmations came from, is supplied by the submitting author and checked by nobody. Auditing
    **all nine papers rated tier 2**, rather than only the flagged one:

    - **arXiv:2508.21634 held.** A publisher record exists, IEEE Xplore 11229706, DOI
      10.1109/ISSRE66568.2025.00035, pages 252-263. Tier 2 stands and now cites the record rather
      than the author's claim.
    - **arXiv:2504.16485 held**, and was the one entry already doing this correctly: it cites the
      Crossref registrar record rather than the DOI printed on the arXiv listing, and says why.
    - **arXiv:2604.03196 held**, DOI 10.1145/3793302.3793614.
    - **arXiv:2409.10781 held.**
    - **arXiv:2507.00788 held**, and was under-recorded rather than over-tiered: it is in Empirical
      Software Engineering with DOI 10.1007/s10664-026-10889-1, and it is the only **preregistered**
      study here, through a Registered Reports track. The document had the journal name and neither
      of those.
    - **arXiv:2608.18167 did not hold.** Acceptance claimed in `Comments`, no reachable venue listing
      or index. **Moved to tier 4.**
    - **arXiv:2605.16706 did not hold.** Recorded as accepted at a named conference; the paper is on
      arXiv and nowhere else that could be reached. **Moved to tier 4.**
    - **arXiv:2605.02273 did not hold.** Recorded as EASE 2026 on the strength of a conference banner
      in the paper's own typesetting, which authors set. **Moved to tier 4.** It was the second paper
      in a paired entry and was the last one found, because a check reading one record per entry saw
      the other paper's DOI and stopped.
    - **arXiv:2507.09089 was never eligible.** It claims no venue at all. It was placed at tier 2
      because it is a well-designed randomised controlled trial. **Moved to tier 4.**

    **Four of nine moved.** Nearly half of this document's tier-2 ratings did not meet its own
    definition of tier 2.

    Why it earns a number rather than a quiet correction, and why it may be the worst entry here:

    - **The scale's own text already forbade all of it.** The tier-2 definition names the venue or a
      publisher DOI, in a table at the top of the same document. The rule was not missing, unclear or
      contested. It was not applied, four times, by the person who wrote it.
    - **The last one is the scale failing at its single distinguishing claim.** This collection's
      whole argument against existing evidence hierarchies is that it orders by **review trail**
      rather than by whether the work produced good numbers. arXiv:2507.09089 was tiered on the
      quality of its method. That is not a slip in applying the scale; it is the scale's thesis being
      abandoned in the one place it was supposed to bind hardest, and no reader could have detected
      it, because the entry reads exactly like a correct one.
    - **Most of them held, and that is the trap.** A rule that produces the right answer more often
      than not is the hardest kind to notice breaking, and the first entry checked was one that held,
      which would have made a persuasive case for not auditing the rest.
    - **It is error 1 returning at scale.** Error 1 is a submission line read as a review trail.
      These are acceptance lines read as venue records, and one paper's methodology read as a review
      trail: the same substitution of something adjacent to review for review itself, nineteen
      errors later.
    - **The flag came from outside and covered one entry.** The other three were found only because
      the flag was treated as a question about the rule rather than about the paper. **A finding
      about one instance of a rule being broken is a hypothesis about every instance**, and that
      generalisation is now the second half of the fix.

    New rule, stated in the scale itself rather than only here: **an author-controlled surface cannot
    confirm a venue.** Not the arXiv `Comments` field, not an institutional publication page, not a
    lab's replication repository, not a ResearchGate entry. A publisher DOI, the venue's own
    programme or proceedings, or an independent index. And **an arXiv DOI (`10.48550/arXiv.…`) is not
    a publisher DOI**, which is the specific way this nearly went wrong on a sixth paper.

    New check, because a rule this document already had and did not follow needs an instrument rather
    than a restatement: `build.py` reads the Tier 2 section and reports, for every paper it names,
    whether a venue record appears near the claim. It **warns rather than fails**, deliberately,
    because a failing build here would be fixed by deleting the check. It was made to fail on purpose
    before being believed. **Its first version accepted only a publisher DOI**, which is narrower
    than the rule it enforces, and it fired on three entries that were correctly confirmed against
    OpenReview and two conference programmes. Widened 2026-09-08 to the three routes the scale
    actually names. A check encoding a narrower rule than the document states is the boundary error
    pointing the other way: it rejects work that is right.

    **Outcome, recorded 2026-09-08, and it partly reverses this entry.** The four downgrades were
    "could not confirm" from an environment where arXiv, DBLP, IEEE Xplore, OpenReview and the
    authors' pages were all unreachable. The records were then fetched by hand:

    - **arXiv:2608.18167 restored to tier 2.** OpenReview record, ICML 2026 Workshop DL4C, Poster,
      submission 123.
    - **arXiv:2605.16706 restored to tier 2.** ICSME 2026 programme, Visions and Emerging Results
      track.
    - **arXiv:2605.02273 restored to tier 2.** EASE 2026 programme, Short Papers and Emerging Results
      track.
    - **arXiv:2507.09089 stayed at tier 4.** It never claimed a venue, so there was nothing to find.

    **So the rule was right and three of the four downgrades were wrong**, and the distinction is the
    lesson rather than an embarrassment: the rule concerns the *route*, and the route was genuinely
    unsound in all four cases. What the downgrades got wrong was treating "could not confirm" as
    grounds to act, which is error 19's failure committed the same day in the other direction. Both
    directions have the same cause: **a blocked network was allowed to function as a finding.**

    **One thing the restorations exposed that the tier cannot express.** All three are real
    acceptances at real venues, and all three are in the lightest categories those venues run: a
    workshop poster, a vision-track short paper, and a short-paper talk. Tier 2 says "peer-reviewed
    and accepted" and flattens a workshop poster together with a full research-track paper. Each
    restored entry now names its track, which is a patch on the prose rather than on the scale.
    **Recorded as an open weakness in the scale**, not fixed, because adding a tier would be a larger
    change than this evidence justifies.



21. **Three corrections landed in the file nobody loads and never reached the two files an agent
    does.** Found 2026-09-08 by an external audit. Three separate instances, one cause, and the rule
    that would have caught all three has been on this list since error 13.

    - **The trailer table, corrected at 0.9.0.** `RESEARCH.md` replaced "seven projects converged on
      `Assisted-by:`" with a verified per-project table showing **two camps and an abstainer**.
      `SKILL.md` and `WORKFLOW.md` kept the withdrawn sentence for two versions. Both were wrong
      about the **Apache Software Foundation**, which uses `Generated-by:`, and about
      **OpenTelemetry**, which prescribes no trailer at all. Both also named **LLVM and QEMU**, which
      appear in no verified table, in no research pass, and were never checked here by anyone.
    - **The evidence-base withdrawal, made at 0.8.0.** Every observation from a repository the author
      does not own was withdrawn, and the changelog stated that "every place that described the base
      has been rewritten to say four rather than five". `DOCS.md` still said five, and it was the one
      file that described the withdrawn codebase in prose. The withdrawal was made on the ground that
      the material should not have been the author's to publish, so this was not a stale count.
    - **The replication upgrade, made at 0.9.0.** `EVIDENCE.md` went from two independent groups to
      four and from "replicated" to "multiply replicated". `SKILL.md` still said "two independent
      groups" and "the only replicated finding" in two places.

    Why it earns a number:

    - **The rule already existed and names this exact failure.** Error 13: when a figure is corrected
      or retracted, grep the whole collection before considering the correction done. It was written
      after one unchecked detail reached five documents. It was then not applied to this collection's
      three largest corrections.
    - **The direction is what makes it serious.** In all three cases the correct version is in a
      reference file and the withdrawn version is in an agent-facing file. **`EVIDENCE.md` and
      `RESEARCH.md` load when a rule is challenged. `SKILL.md` loads every time.** So the collection
      was optimised to look right to anyone auditing it and to behave wrong in use.
    - **One of the three was factually false about a named third party.** Any repository that adopted
      this skill was told, on every load, that the Apache Software Foundation uses a trailer it does
      not use.

    New rule, an instrument rather than a restatement: **a correction is not finished until it has
    been grepped for in the agent-facing files specifically.** `AGENTS.md` now says so. The general
    form is sharper: **the file where a correction is easiest to write is not the file where it
    matters.**

22. **An audit found a defect, fixed every instance inside its own scope, and left the identical
    defect one section above.** Found 2026-09-08, in the same audit as error 21.

    The 0.10.1 audit established that an author-controlled surface cannot confirm a venue and checked
    **all nine papers rated tier 2**. The tier-1 entry claimed a workshop acceptance "confirmed from
    the paper's own front matter", which is the same surface, named in the same rule, one heading
    above the section being audited. It was not looked at. The tier-1 entry then contradicted itself
    for two days, saying "confirmed workshop-accepted" in one paragraph and "both preprints" four
    paragraphs later, with both statements shipping.

    - **It is errors 9, 17 and 20's shape, and this instance is the cleanest.** The audit's scope was
      the section named in the finding rather than the population the rule covers. Nothing about the
      result distinguished "no bad entries" from "no bad entries in tier 2".
    - **The rule was written by the same pass that failed to apply it.** Error 20 states the rule
      generally, about venues, not about tier 2, and was recorded three paragraphs from the entry it
      does not cover.

    New rule: **when a finding produces a rule, re-scan against the rule's population, not the
    finding's location.** Boundary table, sixth row.

23. **Numbers that are not in a paper were published under an explicit claim that the paper had been
    read in full.** Found 2026-09-08 when the PDF was finally obtained. **The worst entry on this
    list on the dimension that matters most, which is whether a reader could have caught it.**

    The contested-security block asserted that arXiv:2603.27130 reports "one table with AI at 12.81
    alerts per KLOC against human 11.58" and a risk breakdown with "AI more high-risk, 0.934 against
    0.464". It also stated, in the same paragraph: **"Both full texts were read on 2026-09-06."**

    Against the PDF:

    - **12.81 and 11.58 appear nowhere in the paper.**
    - The high-risk row is **0.514 against 0.52**, which the paper describes as *similar*. The
      published figures reversed the direction of the finding they named.
    - **10.04 against 13.56 was correct**, which is why nothing looked wrong.
    - The paper additionally finds **more hardcoded secrets in human-written code**, contradicting
      one of the two defect classes the collection tells you to check for, and this was not recorded
      at all.

    The conclusion built on those figures, "both find elevated high-risk patterns in AI-generated
    code in at least one cut", was the pivot of the whole adjudication and it was resting on a number
    that does not exist. It survives only in a much weaker language-sliced form.

    Why it earns a number, and why it is worse than errors 6 through 8:

    - **The claim of a full-text read is the defect, not the wrong figures.** A wrong figure is error
      14's category and this list has several. **A false statement about the verification method is
      new**, and it disables every downstream check: a reader who wanted to challenge the numbers was
      told the strongest possible provenance for them.
    - **It was the most heavily reasoned block in the document.** Four paragraphs of population,
      instrument and normalisation analysis, a stated default, an asymmetric-burden justification.
      All of it downstream of two invented numbers. **Density of reasoning is not evidence of
      grounding**, and this document repeatedly reads as though it were.
    - **The correction makes the collection's own safeguard harder to justify, and it stays.** The
      disagreement is wider than was claimed: at the aggregate the contesting paper finds AI code
      lower in alert density and cleaner on hardcoded secrets. The default survives on the
      asymmetric-burden rule alone. That is the rule doing real work for the first time against a
      source that genuinely hurts.

    New rule: **never write that a source was read in full unless you opened it.** Where a pass
    reports having read a full text, the document records that the *pass* reported it, not that it
    happened. Provenance of a verification is itself a claim and takes a tier like any other.

24. **A platform limit was invented, asserted with no source, encoded into a check, and starved the
    one field that decides whether the skill loads at all.** Found 2026-09-08.

    `AGENTS.md` stated that the `SKILL.md` frontmatter description is "capped at **200 characters** by
    the upload surface". `build.py` enforced it. The description was written to 198.

    **Anthropic's own skill-authoring documentation gives the limit as 1,024 characters**, read
    2026-09-08. The figure was wrong by a factor of five and had no source attached in the file that
    asserted it.

    Why it earns a number:

    - **The consequence is functional, not editorial.** The description is the only signal a model
      gets when deciding whether to load a skill. Written to a fifth of its budget, this one names
      five of about twelve covered areas, and a skill-craft audit found that requests about reviewing
      agent-authored code, disclosure trailers, merge gates, benchmarking, spec-writing and session
      handoff would very likely not load it, though the body has dedicated rules and whole companion
      files for each. **A collection that nothing triggers is worth nothing regardless of its
      contents.**
    - **The check made the error invisible rather than catching it.** Every build printed
      `ok description is 198 characters`. An instrument reporting success against a fabricated
      constraint is worse than no instrument, because it converts a fixable oversight into a
      maintained invariant.
    - **It is a new category on this list.** Every previous entry is a wrong claim about a *source*.
      This is a wrong claim about **the platform the collection runs on**, in the file that instructs
      contributors, enforced by the build. The collection grades external research carefully and
      asserted its own operating environment from memory.

    New rule: **a constraint encoded in a check needs a citation like any other claim.** The cap now
    names the documentation and the date it was read. `build.py` additionally **warns when the
    description is under 400 characters**, because a cap cannot catch under-use, and under-use is the
    failure that actually happened.

25. **A claim about what a third party recommends went stale in the agent-facing file, on a day the
    recheck date read zero days old.** Found 2026-09-08 by an external evaluation.

    `SKILL.md` asserted, in the present tense and in two places, that repository overviews are
    "recommended by model vendors" and were measured as not helping. It was the collection's flagship
    example of independent measurement beating vendor advice.

    **Anthropic's current best-practices page lists, in its exclude column, "File-by-file descriptions
    of the codebase" and "Anything Claude can figure out by reading code"**, read in full 2026-09-08.
    The vendor's published position agrees with the measurement. There is no conflict to cite.

    - **The rule is unaffected and that is what makes this instructive.** Overviews still do not help.
      What expired is the claim about who disagreed, which was doing rhetorical work the finding did
      not need.
    - **The recheck that should have caught it had just run.** The date on the file read zero days
      old and the build passed. **A recheck that never opened the vendor's page is not a recheck of
      the vendor claims**, and `REFRESH.md` named "administrative facts" as a category rather than
      naming pages by URL.
    - **A live conflict existed at the same moment and was unrecorded.** The same page cautions that
      "a reviewer prompted to find gaps will usually report some, even when the work is sound", which
      cuts against this collection's tier-4 instruct-the-reviewer-to-disagree rule. So the document
      carried two expired conflicts and zero live ones. Now recorded under disagreements.

    New rule: **a claim about what somebody else recommends is a dated claim about a page, and the
    page goes in the refresh list by URL.** `REFRESH.md` now names them.

26. **Three packaging defects shipped in the release made to fix packaging, and the check that
    would have caught all three was resolving against the wrong set.** Found 2026-09-09 by an outside
    reader inspecting the built zip rather than the repository.

    - **`templates/AGENTS.md` had not shipped in any distributable.** The exclusion list held the
      root `AGENTS.md`, the filter matched on **file name**, and the template of the same name was
      caught by it. Five of six templates shipped. The templates are the most-copied artifact here.
    - **Four rule files left the deliverable in the 0.14.0 split**, taking **47 prohibitions and
      8,523 words** with them: `WORKFLOW.md`, `OBSERVABILITY.md`, `DOCS.md` and `TOOLING.md`. The
      build comment called them reference material read once by a human. That is true of a
      vocabulary and false of seventeen rules about how changes move through a repository. **The
      boundary was drawn on length when it should have been drawn on apparatus against rules.**
    - **Ten shipped files referenced documents a consumer does not receive.** `SKILL.md`'s own
      provenance table described five of them.

    **One cause under all three, and it is the reason this earns a number rather than a patch note.**
    The cross-reference check resolved names against the **working tree**. Every reference resolved,
    the build was green, and none of it was true of what anybody installed. **It is row three of the
    boundary table, the distributable against the repository, for the seventh time.**

    Why it is the worst instance of that pattern so far:

    - **It happened inside the release whose entire purpose was to fix what ships.** The 0.14.0 split
      moved files between the deliverable and the apparatus and the check verifying the deliverable
      was never pointed at the deliverable.
    - **The check was actively taught to look in the wrong place.** When `evidence/` was created, the
      resolver was extended to search it, so that references to files that had just stopped shipping
      would keep resolving. **That is a check being edited to stay green through the exact change it
      existed to police**, and it took one line.
    - **Every other instrument passed.** No em dashes, no identifier leaks, 29 cross-references
      resolving, eight tier-2 papers with venue records, the staleness date zero days old. **A green
      build is a statement about the checks, not about the artifact**, and this collection has now
      said that four times and shipped it wrong anyway.

    New rules, both mechanical:

    - **A check on the distributable resolves against the shipped file list, never against the
      working tree.** The question a consumer needs answered is whether a reference resolves **in
      their copy**.
    - **An exclusion matches a relative path, not a file name.** Only `LOCAL.md` is excluded by name,
      because it can legitimately sit in a subdirectory and must never ship from any of them, and
      that exception is now the only member of its set and says why.

    New check: the build **asserts the template count** against the directory rather than reporting
    it. Both new checks were made to fail on purpose before being believed, which the previous three
    packaging defects would each have been caught by.

27. **An absence claim was asserted far beyond the scope of the search that produced it, and the
    thing it missed is doing this better.** Found 2026-09-09 by a third landscape pass, verified here
    by cloning the repository.

    `README.md` said: **"Nothing here has been measured against a control, and neither has anything
    else."** The first clause is true. The second was a generalisation from a search about **defect
    rates with and without AI assistance** to a claim about **the entire field**, and it was false.

    `martinholovsky/SOTA-skills` runs **guided against unguided arms** on multiple models, publishes
    **nine null results** next to its positive ones, **retracted a lift** that failed to reproduce
    when its sample grew from 15 to 49 cases, **pre-registers predictions** and publishes the wrong
    ones, and runs a CI job that **injects a known-bad per invariant and requires the intended check
    to be the one that complains**, reporting a non-zero exit for any other reason as a false pass.

    Why it earns a number, and why it may be the most embarrassing entry on this list:

    - **It is error 10's shape at the widest possible scope.** Error 10 is reporting an absence
      without stating what was searched for. This is worse: the search *was* stated, in the very next
      sentence, and it was narrower than the claim built on it. **A reader could see the scope and
      the overreach in the same bullet and neither the author nor six outside checks did.**
    - **It was the most self-flattering sentence in the collection**, and that is the tell. "Nobody
      has done this properly, including us" reads as humility and functions as a moat. It survived
      six outside checks because it costs the author nothing and sounds like a concession.
    - **The thing it missed is ahead on method, not behind.** This collection grades other people's
      published evidence. That repository generates its own with control arms. Its
      negative-control CI is strictly stronger than this collection's practice of making a check fail
      on purpose by hand: it automates the injection and verifies that the **right** check fired.
    - **Two landscape passes had already run** and neither found it, one of them specifically tasked
      with finding comparable work. **A landscape pass that searches for papers will not find a
      repository**, and the strongest work in this space is currently in repositories.

    New rule: **an absence claim may not be broader than the search that produced it, and the two
    must appear in the same sentence.** "No study meeting these criteria was found, searching for X"
    is a result. "And nobody else has done this" is a different claim needing its own search, which
    in this case would have been a code search rather than a literature search.

28. **The collection verified every artifact it produced and never verified the one that was
    running.** Reported 2026-09-09 by an outside audit session with access to the author's machine.
    The repository facts below are verified here. **The machine state is the author's report and was
    not observed from inside this repository**, which is itself part of the finding: nothing in this
    project can see the thing that matters most.

    The installed skill was **0.7.0, dated 2026-09-04 in `CHANGELOG.md`**. The repository was at
    0.15.0. **Eleven releases**, carrying every correction from errors 19 through 27, had landed in
    the repository and none had reached the thing that loads. It was a flat copy of the directory,
    so there was no mechanism by which any of them ever could.

    **The cause is a sentence in this collection's own README.** The install instruction read "Clone
    **or copy** the directory", offering the two as equivalent. They are not. A clone has a version
    and can be updated; a copy has neither. The document whose entire argument is that a claim must
    be traceable to a version told its only user to install it in the one way that discards the
    version.

    What was therefore loaded in every session for five days:

    - The **ASF trailer claim in its pre-correction form**, wrong about a named third party.
    - **"five repositories"** as the first-party evidence base, since corrected to four.
    - **No `SETUP.md`, `SPEC.md`, `MEASURING.md`, `SOLO.md`, `TEAM.md`, `HANDOFF.md` or
      `REFRESH.md`**, because none of them existed at 0.7.0.
    - **No `templates/AGENTS.md`**, and a **description two orders of magnitude shorter** than the
      921 characters the current version carries, which is the only field deciding whether the skill
      loads at all.

    Why it earns a number, and why it is the worst entry on this list:

    - **It is the eighth row of the boundary table and the first one drawn outside the repository.**
      Every previous row drew its boundary at a convenient unit *inside* the project: a branch, a
      file's contents, the distributable, the working tree. This one drew it at the project.
      `build.py` verifies what it builds, the watcher verifies what it cites, and nothing verified
      what runs.
    - **Every other error here is a wrong claim in a document. This one was a wrong claim in
      production.** The other twenty-seven were wrong where a reader might encounter them. This one
      was wrong in every session on the machine where the work was being done, including the
      sessions that wrote the corrections it did not have.
    - **It would have consumed the adoption run.** The 1.0 gate accepts exactly one input, an
      adoption run against a real repository. That run would have adopted 0.7.0 and produced a
      friction log against defects fixed three days earlier, and **nothing anywhere would have said
      so**. The most expensive item in the project was pointed at a stale artifact.
    - **The skill states its own version in its eighth line, and was never asked.** This was not a
      check nobody had built. It was a question nobody thought to ask of a file that answers it.

    New rule, and deliberately **not** a new build check: **install by a mechanism that carries a
    version, and make the loaded version the first thing asserted before acting on loaded rules.**
    A build check would be the wrong shape by construction, because the failure lives outside the
    build's reach, which is the whole finding. `README.md` now refuses the copy install and
    `ADOPTION.md` now opens by asking the skill which version it is.

    **Addendum, 2026-09-10, because it happened twice more within a day.** The install command
    written to fix this defect picked its zip with `sorted(glob("dist/*.zip"))[-1]`, which sorts
    **as strings**, so `0.9.0` beats `0.15.0`. `dist/` still held `dev-conventions-0.7.0.zip`, so
    **the fix for the stale install would have reinstalled the stale skill this error is about.** A
    bloat-audit script written the same day made the identical mistake and was caught only because
    its numbers disagreed with the build's own output.

    So, two rules rather than one:

    - **A version picker sorts on parsed integers, never on strings.** `max(paths, key=lambda p:
      tuple(int(x) for x in re.findall(r"\d+", p.name)))`. String order is not version order and it
      fails silently, always choosing plausibly.
    - **And leave nothing to pick wrongly.** `dist/` now holds the current version's outputs only,
      pruned by `build.py` on every build, because fixing every version picker is necessary and is
      not verifiable for commands that do not live in this repository. The reason is written into
      `prune_dist`, next to the code, rather than left as a convention.

29. **The leak check could not see itself, and what it would have published is the index of
    everything that was scrubbed.** Found 2026-09-10 by an outside audit reading `build.py` rather
    than the files `build.py` checks. Verified here by importing the module and asking `collect()`
    what it returns.

    Two regular expressions in `build.py` held the employer, customer and author-name patterns **in
    plaintext**. `check_prose` scanned the 28 files `collect()` returns. `build.py` is excluded from
    the distributable, so it was in none of them, and neither were `AGENTS.md` or `CLAUDE.md`. The
    manual grep command in `AGENTS.md` listed the same patterns again, in an agent-facing file, for
    the same reason.

    **This is worse than a prose mention of one identifier, and the difference is the point.** A
    stray mention leaks one fact. A published pattern list leaks the **shape of the redaction**: it
    tells a reader exactly which strings the author considered sensitive enough to scrub, which is
    the same reasoning that put `.agents/clearance-inventory.md` behind `.gitignore`. The
    instrument was a better disclosure than anything it was guarding against.

    Why it earns a number:

    - **It is the ninth instance of the boundary table and the first where the instrument is the
      thing that leaks.** Row three, the distributable against the repository, recurring. The
      repository is public, so the scope that matters is what is **published**, and everything
      tracked is published. The check was scoped to what **ships**, which is a strictly smaller set
      and was never the right one for this question.
    - **It survived eight outside checks**, several of which read `build.py` closely enough to find
      other defects in it, because a regex full of the strings you are protecting reads as the
      protection rather than as the exposure.

    Fixed:

    - Patterns moved to `.agents/leak-patterns.txt`, **gitignored**, read at runtime, with a tracked
      `.example` carrying placeholders and the reason.
    - **A missing or empty patterns file is a hard stop, never a quiet pass.** A build that skips its
      leak check silently is worse than one with no leak check, because it reports green. An empty
      section stops the build too, because an empty pattern list matches nothing and passes
      everything.
    - The employer and project patterns are now checked against **every tracked file**, 53 of them
      rather than 26. On its first run the new check failed on `AGENTS.md:278`, which is the line the
      old one structurally could not reach.
    - **One further identifier added to the enforced set**, a private project name that had sat only
      in a manual grep line, so nothing mechanical stopped a first-party observation naming the
      repository it came from. It is not written here, and the reason is the next bullet.
    - **The new check caught the writing of this entry.** The first draft of the bullet above named
      that identifier in plaintext, inside the numbered error about not publishing identifiers, and
      the build refused it. That is the entry's own argument arriving faster than expected: the
      instinct to name the thing you are protecting is strong enough to survive writing a rule
      against it two paragraphs earlier, which is exactly why the check has to be mechanical and
      has to run over every tracked file.
    - Three probes, each asserting the **intended** message fired: patterns file absent, a section
      emptied, and a real pattern planted in `build.py` itself. Plus a positive control, because
      three probes against a tree that cannot build prove nothing.

    **Still open, and it is the author's decision rather than a defect to fix.** The strings are in
    `AGENTS.md` and `build.py` on **every ref**, local and remote. Error 17 already established that
    removing text from HEAD does not remove it from the repository, and on a published code host it
    is stronger than that: unreachable objects stay addressable by hash and are served by the API
    long after a rewrite. So a history rewrite is not sufficient on its own and is not obviously
    worth its cost. Recorded rather than quietly dropped.

    New rule: **a check that protects a list must not publish the list.** Where a check needs secrets
    to do its job, they live outside the artifact and the check fails loudly when they are absent.

30. **The layer selector could never match, in every repository, silently, and eight verification
    passes read past it.** Found 2026-09-10 by the first adoption run, and that is what earns it a
    number rather than a changelog line.

    `SKILL.md` selected the two mutually exclusive layer files on **`team: 1`** and **`team: 2` or
    more**. `PROFILE.md`, `templates/profile.yml` and all three shipped example profiles have always
    used the enum **`solo | pair | small-team | open-source`**. The selector named values the schema
    cannot hold, so an agent following any shipped example loaded **neither layer**, applied Layer 1
    only, and **reported nothing**, because a condition that is never true is indistinguishable from
    a condition that did not apply. Introduced by the 0.14.0 split, which moved the layers out of
    `SKILL.md` and carried the old numeric phrasing with them.

    **Why this one is different from the twenty-nine before it.** Every previous error was found by
    reading: a claim traced to its source, a check read against its scope, an artifact opened. This
    was found by **running the procedure**. Eight verification passes, two outside audits and a
    competitive evaluation all read `SKILL.md`, several of them line by line, and the sentence
    `team: 1` reads perfectly. It is only wrong **against another file**, and only visibly wrong when
    somebody executes it. **The whole apparatus was pointed at whether claims were true and none of
    it asked whether the instructions could run.**

    - **Twelve checks verified provenance, packaging, metadata, staleness and venue records. Not one
      verified that the document's own conditions can be satisfied.** That is the gap, and it is a
      different kind from every other entry: not an unsupported claim, an inoperative one.
    - **It is the strongest argument in this repository for the 1.0 gate.** The gate says the skill
      does not publish until it has been adopted once. This defect is what the gate was for, it was
      found within an hour of the gate finally being satisfied, and it had survived everything else.
    - **It is also an argument against the release cadence.** Sixteen versions in six days, and the
      one thing that would have caught this was the one thing never done.

    **Provenance, split as the reporting agent asked and worth keeping split.** The adopting agent
    verified the mismatch **in its own install**: every `team:` occurrence across the skill's
    Markdown, five locations, two forms, zero overlap. It **relayed on the coordinator's authority**
    that the same holds in the source repository rather than having checked it. Both halves were
    confirmed here against the source at `ca1d38e` before this entry was written. Recording which
    half each party actually saw costs a sentence and is the difference between two independent
    observations and one observation repeated, which error 15 is about.

    **The sharper framing, from the adopting agent, and it is the part that matters.** It loaded
    `SOLO.md` correctly, and doing so required inferring what the author meant rather than following
    the document as written: `team: solo` is not `team: 1` by any mechanical reading, and the
    mapping was available only to a reader already reasoning about the skill's design intent. That
    reader is not the audience. A stranger follows `PROFILE.md` to write `team: solo`, follows
    `SKILL.md` to choose a layer, gets neither, and sees nothing. **The defect's cost is not that it
    is hard to work around. It is that bridging it needs context the document does not supply, and
    the failure when you lack that context looks exactly like success.**

    Fixed: the selectors now name enum members, in `SKILL.md` and in both layer headers. The schema
    was **not** changed to numbers, because every profile in existence uses the enum and the schema
    was never the wrong half.

    New check, the twelfth: **every value the skill selects on must be a member of that field's
    schema enum.** It parses the enums out of `PROFILE.md` and the selectors out of shipped prose,
    reports how many of each it examined, and **fails loudly if it parses no enums at all**, because
    a checker that finds nothing to check must never report clean. Made to fail on purpose three
    ways: the original defect restored verbatim, an invented value on a different field, and a
    schema mutated until it stops parsing.

    New rule: **a check that the documents are consistent with each other is not the same as a check
    that any of them is true, and this collection had twelve of the second kind and none of the
    first.** Where a document tells an agent to do something conditional, the condition is
    mechanically checkable and should be checked.

31. **A check hashed the bytes on disk when what mattered was the content, so every Windows user who
    cloned this repository on the day it went public would have failed their first build.** Found
    2026-09-10, roughly an hour after publication, by an orchestrator reading the fix rather than
    running it. Reproduced here.

    `check_example_placeholders` pinned the tracked example patterns file by `sha256` of
    `read_bytes()`. **`core.autocrlf=true` is the Windows default**, so a fresh clone there writes
    CRLF, and the same file hashes differently:

    | | digest |
    |---|---|
    | The file as checked out on Linux | `74ed4ed9…`, which is what was pinned |
    | The same file as checked out on Windows | `237aac65…` |
    | The git blob, which is what git actually stores | `1594bd62…`, identical on both |

    The failure message said the file **had changed** and told the reader to inspect the diff for a
    smuggled identifier. Nothing had changed. **A first-run failure that accuses the user of the one
    thing the check exists to prevent is worse than a crash**, because it is legible and wrong.

    Why it earns a number:

    - **Tenth instance of the boundary family, and the cheapest to state.** The check measured the
      **bytes in the working tree**. What mattered was the **content**. Git has drawn that
      distinction since it was written; this check did not.
    - **It is the same root cause as the friction log's POSIX-only derivation commands, one day
      apart.** Both were written on Linux, tested on Linux, and are consumed on Windows. Neither is
      subtle. Both were invisible because the author's platform is the one where they work.
    - **It is the first defect in this collection that a stranger would have hit rather than the
      author**, and it arrived with publication, which is what publication is for. Every one of the
      thirty before it was found by someone already inside the project.
    - **It was introduced by the fix for error 29**, which was itself introduced by the fix for the
      first draft of error 29's own compensating check. Three layers, each correct against the
      previous one's failure and none of them tested on a second platform.

    Fixed: `content_digest()` normalises `\r\n` to `\n` before hashing, so the pin measures content.
    **Made to fail on purpose under both line endings**, which is the test that would have caught it:
    a CRLF checkout must build, and a real identifier must be refused under CRLF and under LF alike.
    Three earlier probes tested the same check under one line ending only, which is why they all
    passed and the defect shipped.

    New rule: **a check that compares bytes must say which normalisation it assumes, and be tested
    on both sides of it.** Where the thing being compared is content rather than an encoding,
    normalise first. Line endings are the common case; trailing whitespace, BOM and Unicode
    normalisation are the same class.

Errors 1 through 5 were caught by an external check rather than by the tagging system. **Errors 6
through 8 are a different failure and they need a different check.** All three were paraphrase drift:
the tier was right, the source was right, and the sentence retelling it was not. So tiering a claim
protects its provenance and does nothing for its wording.

Two lessons, not one:

- **The taxonomy classifies, it does not verify.** The check is the deliverable.
- **Trace every external number back to the source's own words before publishing, separately from
  tiering it.** A cited claim and a correctly quoted claim are independent properties, and this
  document had the first without the second in three places.
- **Make a check fail on purpose before you believe it passing.** A verification instrument that
  reports success while measuring nothing is the worst failure available here, because every other
  error on this list at least leaves you uncertain. This one hands you confidence.

**And one pattern runs through errors 9 and 17 and every repeat of them, which is worth stating as a
rule because naming the instances did not stop it recurring.** Nine times in this repository, a check
drew its boundary at the convenient unit and the thing it was looking for sat one unit outside it:

| The check looked at | What it was looking for was in |
|---|---|
| File contents | Commit metadata |
| The current branch | Every other ref |
| The distributable | The repository |
| The prose files | The changelog, which ships |
| The paper's arXiv page | The publisher's record |
| The tier-2 section | Tier 1, where the same rule applied |
| The working tree | The zip a consumer installs |
| The built zip | The copy actually installed and loaded |
| The 28 files that ship | Every tracked file, this repository being public |
| The bytes in the working tree | The content, which git stores identically on every platform |

Every one of those checks passed. Every one was correct within its scope. **None of them stated its
scope**, so a clean result read as "clean" rather than as "clean in the half I looked at". The fifth,
error 20, shows the pattern is not only about identifier leaks: the convenient surface answered the
question asked, and the answer it gave was the author's. **The sixth, error 22, is the one that
should end the argument**: it was committed by the audit that discovered the fifth, in the same
session, against a rule it had just written.

**The eighth, error 28, is the only one whose boundary was the repository itself, and it is the
reason this table is not a curiosity.** The first seven cost a wrong sentence in a document. The
eighth meant that for five days none of the other twenty-seven corrections reached the artifact
being loaded, and no instrument in this project was positioned to notice. **A collection that
verifies only what it produces has verified nothing about what anyone runs.**

**The rule: a check must report the boundary it drew, next to its result.** "No identifier leaks in
22 files, contents only" is a result a reader can act on. "No identifier leaks" is compatible with
four different failures, and this repository shipped all four.

---

## External review, 2026-09-03

The first time anyone outside this project read the collection and pushed back. Recorded because the
README asks for exactly this and it would be dishonest to solicit challenge and then not log it.

**What it independently verified.** Three citations checked against primary sources and matched as
quoted: the nondeterminism paper, the rule-polarity study, and the agent-skill security figures. That
last one matters most, because the security figure was **wrong in an earlier version of this
document** and inflated nineteenfold. An outside check now confirms the corrected numbers.

**Three criticisms, all accepted, all acted on the same day:**

1. **A tier number reads as a truth score.** Valid, and a design flaw rather than a reading error:
   the scale is *named* by review trail but *numbered* like a quality ranking, and numbering carries
   rhetorical weight no disclaimer removes. Fixed with the warning now at the head of the scale.
2. **First-party claims were written with more confidence than the sample earns.** Half a misread and
   half a real gap. The dramatic figures have a large N *within* one case and an N of one *across*
   cases, and this document stated that distinction once, in the axis section, then never restated it
   where the numbers appear. Fixed by naming both numbers explicitly.
3. **"Disagreements left standing" gave no answer for Monday.** The sharpest of the three. An honest
   map of uncertainty is not a decision tool, and the asymmetric-burden rule covers a weak source but
   not a tie. Fixed: every standing disagreement now carries a **Default**, chosen for cheapest to
   reverse and least damaging if wrong, and labelled judgment rather than evidence.

**One thing the review got slightly wrong, and it is this document's fault.** It reported nine
recorded errors when there were ten. It had read a published version of the page that predated the
tenth being added, which is the staleness problem this collection warns about, arriving via its own
distribution. **A reviewer's version matters and should be stated when soliciting review.**

**What the review recommended, and it is fair.** Adopt the two tier-1-and-2-backed rules immediately
(do not let an agent review its own diff, and never trust a single run's pass rate), and cherry-pick
the rest rather than adopting it wholesale. That is a correct application of this document's own
advice to itself, and it is a better recommendation than "adopt this collection".

---

## Outside checks, and what each one cost the collection

Five now, and the useful way to read the table is the last column. **The rate at which checking finds
things has not slowed**, which is the honest argument for a sixth rather than for confidence.

| When | What it was | What it found |
|---|---|---|
| 2026-09-03 | Design review | Three design flaws, all accepted and fixed the same day. Verified three citations against primary sources |
| 2026-09-04 | Claim verification, every external claim | A fabricated statistic, two wrong figures, four items where two passes disagreed with each other |
| 2026-09-06 | Two independent research passes, run in parallel | Each reached primary sources the other could not. One tier upgrade, a contradiction adjudicated, seven new gaps, one shipped template found misstating its own source |
| 2026-09-07 | Figure and venue recheck | Error 20: an audit that moved **four of the nine tier-2 ratings down to tier 4**, one of which had never claimed a venue at all. Also produced error 19, a correct figure withdrawn on a secondhand read |
| 2026-09-09 | Third landscape pass, searching code hosts rather than literature | Error 27. **The claim that nobody else has measured against a control was false**, and had survived six checks because it reads as humility. `martinholovsky/SOTA-skills` runs guided-against-unguided arms, publishes nine nulls, retracted a lift, pre-registers predictions, and runs negative-control CI that verifies the intended check is the one that fired |
| 2026-09-08 | Competitive evaluation against comparable published work, and a skill-craft audit | Errors 24 and 25. **A platform limit this collection invented and enforced in its own build**, which starved the field that decides whether the skill loads. **A conflict claim about a vendor that had gone stale** while the recheck date read zero days old, with a live conflict unrecorded at the same moment. Also: the overlap with first-party vendor guidance is materially larger than this collection claimed |
| 2026-09-08 | Full external audit at 0.11.0, plus primary sources obtained on paper | Errors 21, 22 and 23. **Three corrections that never reached the agent-facing files**, one of them false about a named third party. An audit scoped to the section rather than the rule. And **two figures that are not in the paper they were attributed to, published under a claim that the paper had been read in full** |
| 2026-09-09 | An audit that looked at the **installed** skill rather than the repository | **Error 28, the worst one here.** The loaded copy was **eleven releases stale and had been for five days**, because this collection's own README offered a copy install. Seven checks had examined what the repository builds. This was the first to ask what actually runs |
| 2026-09-10 | An audit that read the checking instrument rather than the files it checks | **Error 29.** The leak check held its patterns in plaintext in `build.py`, which it never scanned, so what would publish is the **index of everything scrubbed**. Also caught a version picker that sorts as strings, which would have reinstalled the very artifact error 28 is about |
| 2026-09-10 | **The first adoption run**, executing the procedure in a real repository rather than reading it | **Error 30.** The layer selector had **never matched any profile**, in any repository, silently, since 0.14.0. Eight passes and two audits read the line and it reads correctly; it is only wrong against another file. The first check in this project of whether the documents' own conditions can ever be true |

**What the 2026-09-06 pair demonstrated is worth separating from what it found.** Neither pass alone
produced the trailer table, and neither alone would have caught the mis-tiering. Two passes cost
roughly twice one pass and returned considerably more than twice as much, because **the failure mode
of a single pass is not error, it is silence**: a source it cannot reach produces no output at all,
and nothing in a single pass's result distinguishes "not there" from "not reached".

**One limit on the 2026-09-07 recheck, stated because the result does not carry it.** arXiv, DBLP,
IEEE Xplore, OpenReview and the authors' institutional pages were all unreachable from the
environment it ran in. The publisher record for arXiv:2508.21634 and the abstract figures for
arXiv:2602.02235 were retrieved through a search engine's index of those pages, **not from the pages
themselves.** That is one step further from the primary source than this document's own rules ask
for. It is recorded here rather than buried, because the same recheck is what added the rule that an
author-controlled surface cannot confirm a venue, and a rule about provenance that hides its own
provenance would be the funnier version of error 20.
