# Measuring whether any of this works

**Split out of `SKILL.md` on 2026-09-08.** It applied to a subset of tasks, building a harness, and
was loading on every session regardless. Load it when you are about to compare two configurations,
two models, two prompts, or decide whether a practice is earning its cost.

**Why this file exists at all.** This collection says repeatedly that a practice has no measured
defect-reduction evidence. That is honest and unsatisfying, so here is how to generate the evidence
rather than wait for someone else to.

This collection says repeatedly that a practice has no measured defect-reduction evidence. That is
an honest position and it is also an unsatisfying one, so here is how to generate the evidence for
your own repository. **Mostly tier 7**, because the working knowledge on this lives in vendor and
practitioner writing rather than in the literature, with two exceptions noted.

**Nobody has measured this properly, and that is a finding rather than an excuse.** A deliberate
search for a controlled comparison of defect rates with and without AI assistance found nothing
meeting all three of random assignment, a real defect outcome rather than a proxy, and adequate
power. The near misses each fail a different axis: a randomised trial measuring test-pass rate
instead of defects, a larger study measuring real bugs but not randomised and conflating access with
use, another randomised trial measuring only time on task. `EVIDENCE.md` records the search terms so
the next person can do better rather than repeat it.

- **Do not compare two configurations on one run each.** The single most important rule here, and the
  only tier-1 finding in the collection: outcomes flip between byte-identical runs, and temperature
  zero does not fix it. **Run each candidate five to ten times per task.**
- **Do not report pass@k when you care about reliability.** pass@k, meaning at least one success in
  k attempts, flatters an agent. What production needs is closer to pass^k, meaning it works every
  time. **Measured across 500 tasks and six configurations: the gap between pass@1 and pass@5 reaches
  24.9 percentage points, and between pass@1 and pass^5 reaches 18.9 percentage points.** That is the
  distance between the number you would report and the number you could rely on.
- **Do not build your task set out of a public benchmark's tasks.** Build a small expert-labelled
  set, ten to twenty real tasks from your own repository, and decide up front what counts as
  success, as an acceptable alternative, and as a meaningful failure. Those three categories are the
  harness. Benchmark critiques exist in reviewed venues, and one major vendor has stopped using the
  best-known coding benchmark as a frontier evaluation, which tells you how much a score on it says
  about your codebase.
- **Do not only test the happy path.** Include tool failure, context overflow, and the fiftieth tool
  call in a long run. A harness of clean tasks measures something, and it is not the thing that
  breaks.
- **Do not grade only the final answer where many paths are valid.** Capture the trajectory. A right
  answer reached by luck and a right answer reached by a sound route are the same row in your
  results table and very different things in your repository.
- **Do not use a model as a judge without knowing its bias.** Measured: LLM judges at a true
  positive rate above 96% against a true negative rate below 25% on validity judgments, which is a
  grader that mostly approves. Across 13 studies in one domain, judge-to-expert concordance ranged
  0.66 to 0.96 with a median of 0.83, worst on fine-grained tasks. A rubric-anchored ensemble of
  three reached 0.90. So anchor the rubric, use more than one judge, and never let a model judge be
  the whole gate on a fine-grained property.

