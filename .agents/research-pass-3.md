# Research pass 3: the brief, and where it stands

Written 2026-09-05. **Not part of the distributable.** `.agents/` is excluded by `build.py`, same as
the profile beside it. This is working state for whoever picks the collection up next, including a
later session of the same author.

## Status

**Not yet run.** The prompt below is finished and patched. It has not been sent to any research
system. Work on the collection paused here to resolve an unrelated tooling decision.

Two runs are intended, on **identical text**, without showing either system the other's output:

1. Claude Desktop, Research mode, high effort.
2. Perplexity Deep Research.

The independence is the entire point. Two prior verification passes disagreed with each other on
four items, and that disagreement is recorded as error 15 rather than as a nuisance, because a
collection that only ever gains certainty from being checked is not being checked. Showing one
system the other's answer destroys the only thing the second run is being paid for.

**Agreement between the two runs is worth much less than it looks.** The standing rule applies:
rediscovery is not replication. What to look for in the diff is disagreement, and coverage that only
one of them found.

## Why a third pass at all, and why it is scoped this way

The first external review found three design flaws. The second fetched every external claim in
`EVIDENCE.md` and found a fabricated statistic, two wrong figures, and four items where independent
passes disagreed. **The rate of discovery has not slowed**, which means the remaining defect count is
unknown rather than low.

The scoping went through one correction worth recording. The pass was first drafted as
verification-only, on the reasoning that the readme ranks new practices last. That was wrong: the
readme ranks **sources** second, and states that a gap here once stood sourceless while an accepted
paper answering it already existed. Targeted source-hunting against named gaps has a demonstrated hit
rate in this collection. Verification is also the cheaper half, being fetch-and-compare, while broad
literature sweep is the thing a research mode does that an ordinary session cannot. So discovery
leads, at roughly 65% of effort.

## Four patches applied to the draft, and why each one matters

Recorded because each was a real defect in the brief and the reasoning generalises.

1. **A carve-out exempting "respected authors" from the primary-source rule was removed.** It would
   have restored the exact mechanism behind error 14, where a fabricated figure survived review
   because it arrived wearing an institutional name that made it feel checkable. Replaced with a
   narrower and correct version: a named practitioner is a legitimate **tier-7 source for their own
   judgment**, never for a number they did not measure.
2. **"A source that merely agrees is still somewhat useful" was qualified with an independence
   test.** A second paper from the same group on the same benchmark adds nothing and inflates
   apparent confidence. Different group, different data, different method, and say which hold.
3. **The out-of-scope rule on new practices was leaking.** Split in two: practices may be reported
   only when present in two or more independent named sources, and **newly discovered gaps became
   their own explicitly wanted deliverable**, which the original brief failed to ask for.
4. **An assertion of repository access was replaced with a verification step that fails loudly.** The
   repository is private. A research session that cannot read it will otherwise reason from the
   prompt's own summaries and produce something that looks complete.

## What the pass must not touch

The 2006 code-review study behind the "under 400 lines" rule. It is a book, it cannot be fetched, and
two passes reading its secondary sources already extracted contradictory numbers. A third reading of
the same secondaries yields a third number and makes the contested item worse rather than better. It
stays withdrawn until somebody reads the original, which is one library request.

## Integrating the results, when they arrive

1. Triage both outputs into CONFIRMED, CONTRADICTED, COULD NOT VERIFY.
2. Diff the two systems against each other. **Every disagreement is a finding**, and if two
   independent extractions differ, neither number can be asserted.
3. Apply corrections. Record any new error on the numbered list rather than editing quietly.
4. Bump the version and the recheck date in `SKILL.md`, `README.md`, `CITATION.cff` and both plugin
   manifests.

---

# The brief, final text

> You are running a combined **source-discovery and verification pass** on a documentation collection
> called `dev-conventions`, which grades every claim it makes by the strength of the evidence behind
> it.
>
> The collection is in a **private** GitHub repository at `natanaelfejes/dev-conventions`, branch
> `claude/research-continuation-standards-ihym7d`.
>
> **Before anything else, verify you can actually read it.** Fetch `EVIDENCE.md` and report its first
> heading and its approximate line count. If you cannot retrieve the file, **stop immediately and say
> so**. Do not proceed from the summaries in this prompt, and do not infer file contents. A pass
> built on files you could not open is worse than no pass, because it will look complete.
>
> Work in two phases, discovery first. Do not reorder them. **Budget roughly 65% of your effort on
> Phase 1 and 35% on Phase 2**, and if you run short, cut Phase 2's tier sweep rather than Phase 1's
> Gap A.
>
> ## Hard rules. Read these before searching anything.
>
> 1. **Never report a statistic you have not seen in the primary source itself.** This collection
>    once carried a fabricated figure ("a single agent matched or beat multi-agent systems on 64% of
>    benchmarked tasks, multi-agent adding 2.1 percentage points at roughly twice the cost"),
>    attributed to a named university group. It was traced to a search-optimised page naming no
>    paper, author or identifier, and the numbers appear in no real paper. It survived an external
>    review because it was specific, quotable, and agreed with a position already held. A statistic
>    that is specific, quotable and flattering to a position gets its primary source fetched
>    **before** it is written down. If you cannot open the paper and see the number, report the paper
>    without the number.
> 2. **Blog posts, vendor pages, newsletters, LinkedIn, and aggregator summaries are never sources
>    for numbers.** They may be used to locate a paper. Then the paper is what you cite.
>
>    **One narrow exception, and it is about judgment, not measurement.** A named, credible
>    practitioner writing under their own name is a legitimate **tier-7 source for their own stated
>    position, reasoning, or reported experience**, and you should report it as such, labelled
>    `tier 7, practitioner judgment, no comparison arm`. That exception **never extends to a number
>    they did not themselves measure**. If a respected author quotes a statistic, the statistic's
>    source is whoever produced it, and you fetch that or you do not report the figure. Authority is
>    not a substitute for provenance, and this collection has already been burned exactly once by a
>    number that felt checkable because of whose name was attached to it.
> 3. **Establish acceptance against the venue's own accepted-papers list, a publisher DOI distinct
>    from the preprint's, or DBLP.** A paper's own "submitted to X" line states intent, not outcome.
>    DBLP is usually fastest. Also useful: OpenAlex, Semantic Scholar, ACM Digital Library, IEEE
>    Xplore, SpringerLink, ScienceDirect.
> 4. **Record exact query strings for searches that found nothing.** A negative result with recorded
>    terms is a real deliverable: it lets the next person do better rather than repeat the search.
>    **"Could not find" and "does not exist" are different claims** and you must never conflate them.
> 5. **The gap descriptions below are the collection's own account of what it is missing, and it has
>    been wrong about that before.** If a gap is mis-specified, or the thing it wants has already
>    been answered under different terminology, say so. That is a finding.
>
> ## What counts as valuable, in descending order
>
> 1. A **peer-reviewed study** (ICSE, FSE, ASE, ISSTA, MSR, EMSE, TSE, TOSEM, CHI, CSCW, or
>    comparable) answering a gap. Worth more than anything else you can bring.
> 2. An **independent replication** of a finding currently held from a single group.
> 3. A **contradiction** of something the collection asserts.
> 4. A **preprint** answering a gap, clearly labelled unreviewed.
> 5. A **named practitioner source** outlining a consensus the collection missed or misrepresented,
>    labelled tier 7.
>
> A source that merely agrees with something already held is worth reporting **only if it is
> independent**: a different group, different data, and a different method. State which of those
> three hold. If it shares any of them with the source already held, say so and rank it accordingly,
> because rediscovery is not replication and agreement from a dependent source is not evidence.
>
> ---
>
> # PHASE 1: DISCOVERY
>
> ### Gap A. A controlled comparison of defect rates with and without AI assistance. This is the single most valuable thing you could find, because the whole collection leans on its absence.
>
> The bar is **all three** of: random assignment; a **genuine defect outcome** (bugs found later in
> review, test, or production) rather than a proxy like test-pass rate or expert quality rating; and
> adequate power. Searched 2026-09-03 and not found. Recorded as *could not confirm*, not *confirmed
> absent*.
>
> Known near-misses, each failing a different axis. **Do not re-report these**: a vendor randomised
> trial N=202 measuring test-pass rate and expert ratings; a practitioner study N=785 measuring real
> bugs, reporting 41% higher, not randomised and conflating tool *access* with tool *use*; a
> randomised trial N=96 measuring time on task only; a vendor release reporting 30% defect-risk,
> correlational on code-health quintiles with no AI arm.
>
> Search well beyond the obvious terms: defect density, escaped defects, post-release defects, bug
> injection rate, review findings per KLOC, industrial case study with control group,
> quasi-experiment, difference-in-differences. Go to the SE journals directly, not only arXiv. Cover
> 2024 through 2026.
>
> ### Gap B. Which content is safe to drop when compressing agent context.
>
> Two independent measurements already establish that compression is affordable on real code-editing
> workloads (arXiv:2607.09691, arXiv:2601.16746), so direction is settled. **The boundary is
> unaddressed**: nobody has characterised which content is load-bearing. Losing a file path or an
> exact error string inside an agentic loop is qualitatively different from losing detail in a
> summary. Look for ablation studies, saliency or attribution work on agent context, and
> retrieval-failure analyses that say *what* was lost when compression hurt.
>
> ### Gap C. Code structure against agent task success, as controlled variables.
>
> Partially answered by arXiv:2605.06445 (8 web frameworks, 100 tasks, data-layer and ORM defects
> dominant, convention-heavy frameworks worse than minimal). One group, no replication. **Still open
> specifically**: ORM against plain queries as a controlled variable; monorepo against polyrepo; file
> size. Also wanted: any replication of the framework result by another group.
>
> ### Gap D. Has any venue defined what "reproducible" means for an agent-run artifact?
>
> A search across eight 2026 artifact-evaluation calls (ICSE, ASE, FSE, ICSA, CGO, PPoPP, CAV, CCS)
> found **none** mentioning agent nondeterminism, seed variance, or multi-run reporting as a badge
> criterion. **Recheck**, including 2027 calls now open, any ACM badging terminology revision, and
> NeurIPS/ICLR/ICML reproducibility-checklist changes covering agents. This gap sits directly in the
> path of anyone publishing agent-based work, so a change here matters a great deal.
>
> ### Gap E. Replication of the nondeterminism finding.
>
> The collection's only replicated entry rests on two sources: arXiv:2607.09691 (single author, ~9%
> of 70 SWE-bench Verified instances flip between byte-identical temperature-0 runs) and
> arXiv:2602.07150 (Bjarnason, Silva & Monperrus, KTH, ICLR 2026 workshop). **A third independent
> group measuring run-to-run variance in agent evaluation would be a significant strengthening.**
> Also wanted: work on models that have deprecated the temperature parameter, and on batch-dependent
> or mixture-of-experts-routing nondeterminism.
>
> ### Gap F. A repository with a retrievable review trail.
>
> The collection's most-wanted counter-example. Every codebase it has inventoried records who
> **merged** a change and nothing about who **reviewed** it. Look for published **datasets or mining studies** of code review that report
> reviewer identity, approval trailers, or reconstructable review history at scale, and for any study
> reporting what fraction of repositories retain a review trail at all.
>
> ### Gap G. The evidence-grading meta-literature. Nobody has looked at this and it bears on the collection's central design.
>
> This collection's core device is an **eight-tier scale ordered by review trail rather than by
> whether numbers exist**, plus a standing rule that a weak source may raise a doubt but may not
> retire a safeguard.
>
> Medicine and evidence-based practice have run this experiment for three decades. **Find what is
> known about evidence hierarchies and grading schemes as instruments**: GRADE and its development,
> the older levels-of-evidence hierarchies, and specifically the **documented critiques and failure
> modes** of hierarchy-based grading. Known criticisms worth chasing: that hierarchies conflate study
> design with study quality; that they systematically under-rate observational evidence where
> randomisation is infeasible; that graders disagree with each other at measurable rates; and that a
> numbered scale does rhetorical work no disclaimer undoes.
>
> Also look for grading or confidence schemes in **software engineering** specifically, and in
> evidence-based software engineering as a movement, including why it did not take hold.
>
> **This is the one place a finding could indicate the collection's architecture is wrong rather than
> one of its claims.** Report it plainly if so.
>
> ### Adjacent literatures never mined
>
> Sweep each briefly, report anything bearing on a claim:
>
> - **Automation bias and human factors.** The collection holds a randomised finding that 16
>   experienced developers forecast 24% faster, believed afterwards they had been 20% faster, and
>   were measured **19% slower**. There is a decades-old human-factors literature on automation bias,
>   complacency, and self-assessment calibration. CHI, CSCW, Human Factors, the automation-trust
>   literature. Older foundational work is welcome here; this is not a recency-limited question.
> - **Empirical code review effectiveness**, independent of AI. What is actually measured about
>   review rate, defect detection, and reviewer count?
> - **Metascience.** Whether registered reports demonstrably reduce questionable research practices
>   **in software engineering specifically**. Currently recorded as *could not confirm* for SE, with
>   cross-disciplinary support from psychology and neuroscience only.
> - **Security of AI-generated code.** The collection holds a finding from over 500,000 samples
>   across two languages: more unused constructs, more hardcoded debugging artefacts, more high-risk
>   vulnerabilities. Look for replications, and for anything measuring whether normal review catches
>   these at normal rates.
>
> ---
>
> # PHASE 2: VERIFICATION
>
> **Method, and it is non-negotiable, because it is what previous passes got wrong.** Two prior
> passes failed in opposite directions: one confirmed figures by reading the collection's own summary
> and pattern-matching against the source; another extracted numbers a third reading contradicted.
>
> So: **extract each figure from the primary source yourself before you look at what the collection
> says it is.** Write your extracted value, then diff. If you cannot fetch the primary source, say
> *could not fetch* and stop on that item. Never substitute a secondary source or an abstract for
> full text.
>
> Report in three buckets: **CONFIRMED** (independently reproduced), **CONTRADICTED** (different
> figure, give both), **COULD NOT VERIFY**. A pass with no COULD NOT VERIFY entries has probably not
> been honest about its limits.
>
> **Targets, in order:**
>
> 1. **`RESEARCH.md`, end to end.** Highest-risk file: single-pass, and written in the same session
>    that produced the fabricated statistic. Check especially: the `Assisted-by:` trailer adoption
>    list (Linux kernel, Zephyr, Fedora, Rocky Linux, OpenInfra, Apache Software Foundation,
>    OpenTelemetry) — **verify each project individually, several may be wrong**; the four publishers'
>    AI-authorship policies; "178 of 967 desk-rejected"; the "roughly 2% of submissions, around 500
>    papers apiece" prompt-injection-trap figure; the 640-paper corpus and its 9.8% badged figure;
>    and whether IEEE's policy really covers code as well as text.
> 2. **`templates/AGENTS.md` and `templates/pull_request.md`.** These predate the verification
>    discipline and have never been audited. Flag any claim needing a source and lacking one.
> 3. **Tier upgrade sweep.** For each of 2607.09691, 2602.07150, 2608.18167, 2605.06445, 2601.16746:
>    has it been accepted, published, or superseded? Report venue and DOI for any that moved.
> 4. **Recheck two "proposals with no adoption"** from `RESEARCH.md`: any AI-inclusive extension to
>    the 14-role contributor taxonomy, and content-provenance standards used for citing text or code
>    provenance in academic work. Both were recorded as zero-adoption; that is the kind of claim that
>    goes stale fastest.
>
> ---
>
> ## Explicitly out of scope. Do not work on these.
>
> - **The 2006 code-review study** behind the popular "pull requests under 400 lines" rule. It is a
>   book, you cannot fetch it, and two passes reading its secondary sources already extracted
>   contradictory numbers (100 to 300 lines over 30 to 60 minutes, versus 200 to 400 over 60 to 90).
>   A third reading of the same secondaries produces a third number and makes the contested item
>   worse. **If you find yourself reasoning about it, stop.** You may report any *other* primary study
>   measuring review batch size against defect detection.
> - **Do not propose new conventions or practices of your own.** You may report a practice you found
>   in the literature **only when it appears in two or more independent sources**, and you must name
>   both. A practice from a single source is a tier-7 observation at best and this collection already
>   has more of those than it wants.
>
>   **And a separate, explicitly wanted deliverable: new gaps.** If you find a question this
>   collection should be asking and is not, or an area where the literature has moved and the
>   collection has no entry at all, **report it in its own section**. That is a finding, not scope
>   creep, and it is one of the more valuable things this pass can produce. Say what the gap is, why
>   it matters to a claim already here, and whether anyone has answered it.
> - Style, tone, or structural edits.
>
> ## Deliverable
>
> For every source: full citation, authors, venue, year, **working link to the primary source**;
> **peer-review status and how you established it**; sample size, design, and **what outcome was
> actually measured**; which gap it bears on and whether it **closes, narrows, or contradicts**; any
> **conflict of interest** (vendor-employed authors, or an author list including the evaluated
> product's own team); and the numbers, **only if you saw them in the source**.
>
> **Finding nothing on a gap is an acceptable and reportable outcome.** Report it with the exact
> query strings. Do not manufacture a partial answer to avoid an empty section.
>
> End with three sections: **what you found**; **what you searched for and did not find, with exact
> query strings**; **what you could not access**, so someone with institutional access can finish it.

---

## Other work left open at the pause

Neither of these is blocked on the research.

- **A DOI.** `CITATION.cff` plus an archival-repository DOI is mature and adoptable, and the
  collection asks consumers to pin a version while offering no citable identifier for one. Blocked on
  the repository being public, which is blocked on employer clearance for the de-identified
  observations. Sequence: clearance, public, tagged release, DOI, DOI into `CITATION.cff`.
- **An ORCID** in `CITATION.cff`. One line, free, and it is how academic credit attaches to a person
  rather than to a string.
