# Research pass 4: the remainder, for Perplexity Deep Research

Written 2026-09-06. **Not part of the distributable.**

## Why this is narrow

Pass 3 ran on Claude Desktop and closed most of what it was asked. It was explicit about where it
ran out of budget, which is the only reason this pass can be small. **Do not re-run pass 3's brief.**
Everything it settled is settled, and re-asking would produce rediscovery, which is not replication.

This pass targets exactly two things: **the gaps pass 3 said it under-searched rather than
confirmed absent**, and **the sources it could not reach**.

## What is deliberately not in scope

- Gap A (controlled defect-rate comparison). Exhaustively searched twice and confirmed absent under
  the three-bar test. Do not spend budget re-confirming it.
- Gaps D, E, G. Answered.
- The 2006 code-review study. It is a book, two passes extracted contradictory numbers from its
  secondary sources, and a third reading makes the contested item worse. If you find yourself
  reasoning about it, stop.

---

# The brief

> You are completing an unfinished literature search for a documentation collection that grades every
> claim by the strength of the evidence behind it. A previous pass covered most of the ground and
> **explicitly recorded which questions it did not have budget to search properly**. Those are your
> targets. Nothing else.
>
> ## Hard rules
>
> 1. **Never report a statistic you have not seen in the primary source.** This collection once
>    carried a fabricated figure that survived an external review because it was specific, quotable,
>    and agreed with a position already held. If you cannot open the paper and see the number, report
>    the paper without the number.
> 2. **Blog posts, vendor pages, newsletters and aggregators are never sources for numbers.** They
>    may locate a paper; then the paper is what you cite. A named practitioner writing under their
>    own name is a valid source for **their own stated position**, labelled as such, and never for a
>    number or ranking they did not personally measure.
> 3. **Establish peer-review status** against the venue's own accepted-papers list, a publisher DOI
>    distinct from the preprint's, or DBLP. A paper's own "submitted to" line states intent, not
>    outcome.
> 4. **Record the exact query strings for anything you do not find.** "Could not find" and "does not
>    exist" are different claims. Never conflate them.
> 5. **Finding nothing is an acceptable and complete answer.** Do not manufacture a partial result to
>    avoid an empty section.
>
> ---
>
> ## Part 1: three gaps that were under-searched, not confirmed absent
>
> The previous pass ran out of budget on these and said so. Treat each as genuinely open.
>
> ### Gap B. Which content is safe to drop when compressing agent context
>
> Two independent measurements already show that compressing an agent's context is affordable on real
> code-editing workloads, so the direction is settled. **The boundary is not.** Nobody has
> characterised which content is load-bearing. Losing a file path or an exact error string inside an
> agentic loop is qualitatively different from losing detail in a summary.
>
> Look for: ablation studies on agent context; saliency or attribution work identifying which context
> elements drive task success; retrieval-failure analyses that say **what** was lost when compression
> hurt rather than only that it hurt; and any work on selective versus uniform context pruning for
> tool-using agents.
>
> ### Gap C. Code structure against agent task success, as controlled variables
>
> One group has measured framework conventions against agent success across eight web frameworks and
> found data-layer and ORM defects dominant. No replication exists.
>
> Specifically open, and each is a controlled-variable question rather than an observational one:
> **ORM against hand-written queries**; **monorepo against polyrepo**; **file size** against agent
> edit success. Also wanted: any independent replication of the framework-convention result.
>
> ### Gap F. A repository with a retrievable review trail
>
> Every codebase this collection has inventoried records who **merged** a change and nothing about
> who **reviewed** it, including one with a pull-request mechanism that still recorded no reviewer.
>
> Look for: published **datasets or mining studies** of code review that report reviewer identity,
> approval trailers, or reconstructable review history at scale; and any study reporting **what
> fraction of repositories retain a review trail at all**. That last figure would be the single most
> useful number for this collection, because it would say whether the observation is a quirk of four
> repositories or a property of git.
>
> ---
>
> ## Part 2: sources a previous pass could not reach
>
> These are lookups rather than searches. Each is a specific document.
>
> 1. **Fedora's and Rocky Linux's AI-contribution policies.** Their own primary pages. The question
>    is narrow: do they specify a git trailer for AI-assisted commits, and if so which token? A
>    previous pass saw only secondary aggregators and the collection now marks both as unverified.
> 2. **The OpenTelemetry CONTRIBUTING document**, primary. Same question: which trailer, stated
>    where.
> 3. **The Linux kernel's `coding-assistants.rst`**, the file itself. The exact trailer specification,
>    quoted. Multiple secondary sources agree on it and none of them is the file.
> 4. **A bibliometric study of artifact-evaluation badges and citation counts**, reporting a
>    statistically significant citation difference for only a small number of venue-year pairs after
>    correcting for multiple comparisons. The previous pass could not locate it at all and the figure
>    is currently withdrawn. If it does not exist, say so, because that is also an answer.
> 5. **Venue status via DBLP or a publisher index** for: **arXiv:2608.18167** (Qiu and Gill,
>    adversarial code review, contested ICML 2026 DL-for-Code workshop acceptance, the collection has
>    it tiered provisionally), **arXiv:2607.09691**, **arXiv:2605.06445**, **arXiv:2601.16746**. For
>    each: accepted, where, DOI, or confirmed still preprint.
>
> ---
>
> ## Part 3: one contradiction to adjudicate, and it needs full texts
>
> Two large studies point opposite ways on the security of AI-generated code and the collection now
> logs the disagreement rather than asserting either side.
>
> - **arXiv:2508.21634**: over 500,000 samples across two languages, reports AI-generated code as
>   carrying more unused constructs, more hardcoded debugging artefacts, and **more high-risk
>   security vulnerabilities**.
> - **arXiv:2603.27130**: a large-scale measurement in real-world repositories, reports **fewer
>   static-analyzer alerts and lower defect density** overall, with high-risk rates varying by
>   language.
>
> **Read both full texts and extract each paper's own numbers, methods and populations.** Then answer
> three questions:
>
> 1. Are they measuring the same thing? Both count analyzer alerts, but on what corpora, with what
>    matching, and normalised how?
> 2. Is the disagreement real, or does it dissolve once population and normalisation are compared?
> 3. **Does either measure whether human review catches these defects at normal rates?** The
>    collection believes neither does. Confirm or contradict that.
>
> Do not restate a number from either paper unless you read it in that paper.
>
> ---
>
> ## Part 4: one area with no entry at all
>
> **Agent memory architecture.** This collection has one benchmark citation about memory systems and
> **nothing about how to structure agent memory in practice**: what belongs in a persistent store
> versus a per-session context, how memory files decay, whether retrieval-augmented memory beats a
> flat file for coding agents, and what failure modes are documented.
>
> Report what exists. If the honest answer is that this is unmeasured practitioner folklore, say that
> plainly, because "this area has no evidence" is exactly the kind of finding this collection
> records rather than papers over.
>
> ---
>
> ## Deliverable
>
> For each source: full citation, authors, venue, year, **a working link to the primary source**;
> **peer-review status and how you established it**; sample size, design, and **what outcome was
> actually measured**; which part above it answers, and whether it **closes, narrows, or
> contradicts**; any conflict of interest, including vendor-employed authors or an author list
> containing the evaluated product's own team; and numbers **only if you saw them in the source**.
>
> End with three sections: **what you found**, **what you searched for and did not find with exact
> query strings**, and **what you could not access**.
