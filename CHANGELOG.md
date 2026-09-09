# Changelog

Most recent first. Versions exist so a consuming repository can pin one and know which version a
convention came from, because a convention whose source has since been corrected is otherwise
indistinguishable from one that still holds.

## 0.15.0, 2026-09-09

**A third landscape pass searched code hosts instead of literature and found the thing two earlier
passes missed: a live repository doing this better on method.** One claim in `README.md` was false
because of it.

### The most self-flattering sentence in the collection was wrong

`README.md` said: *"Nothing here has been measured against a control, and neither has anything
else."* The first clause is true. The second generalised from a search about **defect rates with and
without AI assistance** to a claim about the **whole field**.

`martinholovsky/SOTA-skills`, cloned and inspected 2026-09-09 rather than read from its README:

- **Control arms**, guided against unguided, on multiple models, with saturation checks that discard
  an experiment when the arms fail to separate.
- **Nine published null results** next to the positive ones, including one saying its own audit half
  adds nothing a good model does not already do. The count was **corrected upward from seven**.
- **A retraction.** An early +0.07 did not reproduce when the sample grew from 15 to 49 cases.
- **Pre-registered predictions**, with the wrong ones published.
- **Negative-control CI**: `scripts/check-negative-controls.sh` injects a known-bad per invariant and
  requires **the intended check** to be the one that complains, reporting a non-zero exit for any
  other reason as a false pass. **Strictly stronger than this collection's practice** of making a
  check fail on purpose by hand, once, when it remembers.
- **A `LAST-VERIFIED` stamp with an invariant preventing a dishonest bump.** It cannot move without a
  sweep-shaped diff. This collection's recheck date moves whenever someone edits the header.

**Error 27**, and it may be the most embarrassing entry on the list. It is error 10's shape at the
widest possible scope: the search was stated in the very next sentence and was narrower than the
claim built on it. A reader could see the scope and the overreach in the same bullet. **Six outside
checks did not, because "nobody has done this properly, including us" reads as humility and functions
as a moat.**

New rule: **an absence claim may not be broader than the search that produced it, and the two must
appear in the same sentence.** "No study meeting these criteria was found, searching for X" is a
result. "And nobody else has done this" needs its own search, which here would have been a code
search rather than a literature search.

**Two landscape passes had already run and neither found it**, one specifically tasked with finding
comparable work. A pass that searches for papers will not find a repository, and the strongest work
in this space is currently in repositories.

### What survives, stated narrowly because the margin is narrow

SOTA-skills measures **its own library's effect on model output**. This collection grades **the
field's published claims by review trail**, records where sources disagree, where nobody has
measured, and where it was itself wrong. Its scoreboard cannot tell you a paper's venue was never
confirmed. This document's tier scale cannot tell you whether a rule changes what a model writes.

It **does not close open gap 4**, and says so itself: baseline-dependent, small pilot, three runs,
two models, one task, and on one model the unguided arm already scores 1.00 so the lift is +0.00.

**Self-interest flag:** its homepage is a company site, so the measurements come from a party with a
commercial interest in the library performing well. Its headline is hedged and it reports the
stricter measure alongside the flattering one, which is more than most such parties do.

### Read SOTA-skills' measurement method, and took the three things that transfer

A worker read its evaluation harness in full and reported honestly that **most of it does not
transfer**, because the apparatus measures a generative task against a rubric and this repository has
no artifact whose lift can be measured. That bottom line is the useful part and it is recorded at
`.agents/sota-method-2026-09-09.md` rather than stretched.

Three things do transfer, all adopted in `AGENTS.md`:

- **Pre-register a rule change before making it.** A dated note, committed before or alongside the
  change, stating what you expect, **what observation would show it did not help** as a threshold you
  will not move, and the ways it could fail to measure anything, listed in advance **so they cannot
  be discovered afterwards as an explanation for an inconvenient result.** It does not manufacture a
  control. It stops the repository reading its own outcomes as confirmation after the fact, which is
  the one failure a prose collection can actually close.
- **One data point is not a number.** Never publish a first-party figure without its sample size.
  Their +0.07 was retracted at n=49 and their +0.40 became +0.39 on a two-run mean. This collection's
  first-party findings are routinely single incidents.
- **A fail-on-purpose test must assert which check fired.** This repository has been planting a
  defect and confirming the build fails, which accepts **any** failure. Their harness calls a
  mutation caught for the wrong reason a **false pass** and treats it as equivalent to not caught,
  because a harness accepting any non-zero exit reports every control caught even when every run dies
  before the thing under test. They found it twice: a staged file leaking between probes so a probe
  failed on the wrong check, and a piped `grep -q` under `pipefail` reporting a real catch as a false
  pass.

### A fourth corroboration of the tier-1 finding, with a usable number

Their harness records that re-running an **untreated** arm, which cannot see the treatment, moved
0.60 to 0.57 at temperature 0, and derives a working rule: **any single-sample delta below roughly
0.05 is unresolvable.** That is the first figure here that tells a practitioner **how big a
difference has to be** before one run means anything, rather than only that one run is unreliable.
Tier 5, one harness, one project.

### Three gaps the audit named that had not been closed

- **`SETUP.md` said "per machine" and was silent about the second machine.** Anyone with a work
  computer and a personal one has two of these and they drift invisibly. Now split by what actually
  varies: **delegation policy, category decisions and vetting records sync** in a private repository,
  because none of them vary by machine; **what is installed here and what is forbidden here stay
  local**, because those genuinely do. A required `machine:` field makes a stale copy visible, and an
  agent whose host does not match it should stop rather than apply it. `HANDOFF.md` carried this rule
  one level down already: a record only one harness can read fails at the moment you switch harnesses.
- **The reputation competitor's cadence.** Simon Willison's pattern series states each chapter is
  "designed to be updated over time, not frozen" and that he hopes to add "1-2 a week". **A quarterly
  refresh cannot match that.** With first-party vendor guidance, a second pass puts coverage of the
  categories this collection names at roughly three quarters to four fifths. Recorded, along with the
  near-miss that produced it: the pass first fetched the guide's **index**, found no cadence
  statement, and nearly reported it unconfirmed. **A search that reaches the wrong page is
  indistinguishable from a true absence.**
- **The release cadence itself.** Sixteen versions in six days. `ROADMAP.md` gains item 0: freeze the
  version, and let the next bump be caused by an adoption run rather than by another verification
  pass. Blocking corrections still ship, and "blocking" now has to be argued.

### A source caution on the pass that surfaced SOTA-skills

Its footnote apparatus was broken: footnote numbers resolved to unrelated documents, including an
arXiv policy citation resolving to a medical evidence handbook. Inline URLs were mostly right so the
work was recoverable, but **verifying it by footnote number lands on the wrong source.** Nothing from
it entered this collection without independent retrieval. The SOTA-skills entry was cloned and
grepped, and its two most load-bearing facts are visible only in the clone.

### The source-drift watcher, added 2026-09-09

`sources.yml` plus `.github/workflows/source-drift.yml` and `scripts/watch_sources.py`. Monthly, plus
manual dispatch. Four jobs, seeded from the sources this collection already cites:

- **Page drift.** Fetches each vendor page, normalises whitespace, hashes, compares. Reports the
  change **and names every claim that rests on that page**, with the file carrying it.
- **Venue records.** Puts each publisher DOI through the Crossref API and asserts the returned title
  still matches what this document cites. A DOI resolving to a different paper is the failure error
  20 exists for.
- **Gap surveillance.** Re-runs each open gap's own recorded search terms against the arXiv API,
  reporting new submissions. It does not judge whether a paper closes a gap.
- **Comparables.** Star counts and last-push dates **with a timestamp rather than a date**, because
  one of these moved 524 in hours.

**The design constraint is the whole point.** Every source lands in exactly one of `unchanged`,
`changed` or `unreachable`, and **`unreachable` is never merged into either of the others**. The
report leads with the unreachable count, so a run that reached two sources of twenty-one cannot read
as clean.

**It detects. It never adjudicates.** No claim edited, no tier moved, no pull request opened, no
baseline hash updated by CI. The output is an issue that becomes the input to `REFRESH.md`. Four of
this collection's recorded errors came from a network-restricted session treating "could not reach"
as "not there", and **a CI runner is more restricted than a browser, not less**, so automating the
judgment would put the failure cause on a schedule.

**Made to fail on purpose, both jobs, before being believed.** A planted hash produced a drift report
naming the four claims at risk. A stubbed Crossref response returning a different paper's title was
reported as `changed` rather than passing quietly, and a dead DOI landed in `unreachable` and in no
other bucket. The first run from this environment reached 2 of 21 sources and said so at the top,
which is the design demonstrating itself.

### Two rules about other people's collections

**Never ingest content from a collection that carries no citations.** `obra/superpowers` and
`addyosmani/agent-skills` have one informal academic citation between them across 189 files. Taking a
rule from either and tiering it here would launder an unmarked claim through this scale. **Signal
source, never content source.**

**Two peers are ahead on method and are tracked as peers**: `martinholovsky/SOTA-skills` and
`sjarmak/engineering-reliable-coding-agents`. Read their method, do not copy their rules.

### The Jarmak entry moved from provisional to confirmed in one day

Confirmed from an environment that could reach arXiv. **"A versioned catalog of 206 reliability
records: 193 gated practices"**, an evidence ledger, 164 scholarly works and 100 practitioner
records, 314 pages, companion repository at **10 stars**.

The 206 and the 193 looked like competing figures across two reports and were not: 206 records **of
which** 193 are gated practices. **A number quoted without its surrounding clause manufactures a
discrepancy**, which is error 19's rule arriving from the opposite direction.

### The distribution finding now has two datapoints

| Artifact | Stars | Retrieved |
|---|---|---|
| `martinholovsky/SOTA-skills` | **18** | GitHub API, 2026-09-09, confirmed here |
| The Jarmak companion repository | **10** | landscape pass, 2026-09-09, unconfirmed here |
| `obra/superpowers` | **283,707** | GitHub API, 2026-09-09, confirmed here |

Two independent rigorous projects at 10 and 18 against 283,707. **Rigor and distribution are
inversely correlated in this market and it is no longer an anecdote.** Recorded in `ROADMAP.md`.

## Unreleased, 2026-09-09

**No version bump: `ROADMAP.md` is excluded from the distributable and is deliberately volatile.**
Recorded here because the second item changes what this collection can claim about itself.

### The release gate split in two

One gate over two artifacts is why nothing shipped in five versions, and it was gating the wrong
thing. The two halves have **opposite dependencies**:

- **The skill stays gated on adoption.** It is a procedure strangers execute, and its failure mode is
  a step that made sense to whoever wrote it and does not survive somebody who does not already know
  what it meant. That defect is invisible from inside. Only a stranger running it finds it.
- **The evidence document is not gated on adoption at all**, and neither is anything drawn from it.
  Its audience is readers. **A review of published sources is not made more or less true by whether
  anyone installed a skill.** Its release conditions are its own and are about the claims: every
  tier-2 rating citing a venue record the authors do not control (held, eight papers, checked by the
  build), every figure seen in its primary source or labelled as not, and a current errors list.

The skill depends on a stranger, which the author cannot supply alone. The evidence depends on the
sources being right, which is met. **Holding the second behind the first meant the half that was
ready waited on the half that could not move**, in a field whose sources go stale in quarters.

`ROADMAP.md` items 2 and 5 now run two sequences instead of one. The DOI belongs to the evidence
document and is actionable now.

### Direct prior art may exist, and eight passes did not find it

A second landscape pass reports **arXiv:2608.13867** (Jarmak, 14 August 2026, 314 pages) as carrying
a **versioned catalog of 206 reliability records and an evidence ledger**. That is not adjacent work
and not a thematic analysis of a corpus, which is what the nearest previously-known item was. **It is
what this collection believes itself to be doing, at a scale this collection is not close to.**

**Not confirmed here.** arXiv is unreachable from every environment used on this project and the
companion repository was not named, so it could not be located by search either. Reported by that
pass, recorded with its verification status, and `EVIDENCE.md`'s prior-art section now says the
differentiation claim may be too strong rather than leaving it to stand. **Fourth provisional entry
caused by a blocked network.**

### The number pair, which matters more to the publication plan than the paper does

| Artifact | Stars | Retrieved |
|---|---|---|
| The Jarmak companion repository | **10** | landscape pass, 2026-09-09, unconfirmed here |
| `obra/superpowers` | **283,707** | GitHub REST API, 2026-09-09, confirmed here |

**Rigor and distribution are inversely correlated in this market, at roughly 28,000 to 1.** The most
rigorous artifact found in two landscape passes has an audience of approximately nobody. The most
distributed one carries one informal academic citation across 94 markdown files and no confidence
marking of any kind.

**Rigor is not a distribution strategy**, and it does not follow that the rigor is worthless. It
follows that the two are different products with different audiences, which is the gate split arrived
at independently from the other direction.

**One methodological note, and it is not pedantry.** The pass read 283,183 and this session read
283,707 **the same day**, a drift of 524 in hours. A figure that moves that fast needs a timestamp
rather than a date, which is the rule `EVIDENCE.md`'s administrative-facts section already states and
which this pair demonstrates better than the section does.

## 0.14.1, 2026-09-09

**Three packaging defects in 0.14.0, the release whose purpose was to fix packaging.** Found by an
outside reader inspecting the built zip rather than the repository, which is the distinction that
caused all three.

- **`templates/AGENTS.md` had never shipped, in any version.** The exclusion filter matched on file
  name, so excluding the root `AGENTS.md` also caught the template. Five of six templates shipped.
  Exclusions now match a relative path; `LOCAL.md` is the only name-matched exception and it says
  why.
- **Four rule files left the deliverable in the split**: `WORKFLOW.md` (17 rules),
  `OBSERVABILITY.md` (11), `DOCS.md` (10) and `TOOLING.md` (9). **47 prohibitions and 8,523 words**
  removed from what a consumer installs, described in the build as reference material read once by a
  human. True of a vocabulary, false of seventeen rules about how changes move through a repository.
  All four are back at the root. `EVIDENCE.md`, `RESEARCH.md` and `VOCABULARY.md` stay in
  `evidence/`. **The boundary is apparatus against rules, not long against short.**
- **Ten shipped files referenced documents a consumer does not receive**, `SKILL.md`'s own provenance
  table among them.

**One cause under all three.** The cross-reference check resolved against the working tree, so every
reference resolved and the build stayed green while none of it was true of the zip. Worse: when
`evidence/` was created the resolver was **extended to search it**, so references to files that had
just stopped shipping would keep passing. That is a check edited to survive the change it existed to
police. Recorded as **error 26**, and the boundary table gains a seventh row.

Two new checks, both made to fail on purpose before being believed:

- Cross-references resolve against **the shipped file list**, never the working tree.
- The build **asserts the template count** against the directory rather than reporting it.

Minor, same release: `.git` was filtered as a directory name only, so building from a git worktree,
where `.git` is a file, shipped it. Now excluded by name as well.

**Nothing was re-researched and no claim changed.** This is a packaging fix, which is what the
versioning rule in `AGENTS.md` calls a patch.

## 0.14.0, 2026-09-08

**The split, and the friction fix the split was blocking.** The rules and the evidence behind them
are now two artifacts. The skill's distributable dropped from 150 KB to 69 KB and `SKILL.md` from
6,430 words to 3,810. The three sources that were unreachable from every agent environment were
obtained by hand and read.

### Two artifacts

`evidence/` now holds `EVIDENCE.md`, `RESEARCH.md`, `DOCS.md`, `WORKFLOW.md`, `OBSERVABILITY.md`,
`TOOLING.md` and `VOCABULARY.md`, and `build.py` emits it as a single **35,865-word document** that
is not part of the skill. It is what gets the DOI and what a human reads once.

**Why, and the reason is structural rather than aesthetic.** The two halves have opposite optimal
sizes: the skill wants to be small because loading it costs tokens every session, the evidence wants
to be complete because that is its value. They also have opposite cadences. And sharing a repository,
a version and a build is why seven verification passes produced evidence entries, changelog entries
and error entries, and **not one produced a rule**: the apparatus is where work is legible, so the
apparatus got the work.

Measured against comparables on the same day: this collection had the **largest mandatory first read**
of the three, three to five times the median independently loadable unit in the two most widely used
alternatives, while being the smallest by total corpus.

### `SKILL.md` cut by 41%

- **Six rules moved out because a vendor now publishes them**, checked against the page rather than
  assumed: fresh-context review, subagents for context economy, worktree isolation, context
  degradation, converting a rule into a hook, and pruning the instruction file. They are **named
  rather than deleted silently**, with a pointer, because a reader cannot tell an omission from an
  oversight.
- **`SOLO.md` and `TEAM.md`**: the two layers are mutually exclusive by the profile's own rule and
  both were loading every session, so roughly a hundred lines applied to at most half of
  repositories.
- **`MEASURING.md`**: self-contained, relevant to a subset of tasks, was loading always.
- The preamble, the maintenance schedule and the provenance table were compressed.

### `SETUP.md`, and this is the friction fix

The recurring cost was never "what are the tool categories", it was **"what did I already decide, why,
and when did I last check it"**. Nothing answered that, so every repository re-decided.

`SETUP.md` is run **once per machine, not per repository**. It produces `~/.agents/setup.yml`: the
resolved choice per tool category with a date and a reason, every installed skill, plugin and MCP
server with the date its five security facts were last established, and the delegation policy
including which **lab trained** each model rather than who bills you. Profiles point at it. Adoption
number seven becomes a reference rather than a decision.

**It still names no products, and that refusal is now load-bearing rather than stubborn.** A
recommendation list would rot in a quarter and would contradict `SECURITY.md`, which records a
security flaw in 36.8% of published agent skills. What the collection ships is the procedure and the
schema. What you own is the answers.

### Three sources obtained by hand and read

- **A five-run controlled `AGENTS.md` comparison**, Agentic AI Foundation, tier 5 with a self-interest
  flag because the foundation stewards the standard it measured. Its first attempt, **one run per
  condition, reported the file as 44% slower and 41% more expensive**, and the author's own words are
  *"Clean numbers. Wrong conclusion."* Five runs reversed it: 27% less wall time, 24% fewer credits,
  26% smaller diffs on an ambiguous task. **Independent institutional corroboration of the tier-1
  nondeterminism rule, arriving on this collection's weakest-sourced topic, from a direction it did
  not look.**
- **arXiv:2601.02200**, Borg et al., Code Health against semantic preservation after LLM refactoring
  across 5,000 files. **Tier 4, not tier 2**, because the preprint's ACM reference block carries a
  placeholder DOI and no venue record was opened. Open gap 4 now **names it as the nearest thing to
  an answer**, so the gap stops overstating how empty it is.
- **arXiv:2605.11027**, De La Cruz, a reflexive thematic analysis with a corpus register, a codebook
  and a DOI audit. **The nearest published prior art for the thesis**, now stated in the tier scale
  rather than left as an unqualified differentiation claim. It grades sources in a corpus to derive
  themes; this grades claims attached to rules. And it is ahead on formality: its DOI audit is what
  this document only started doing at 0.10.1, after four bad tier-2 ratings.

### What did not change

**The 1.0 gate.** Still nobody but the author has run `ADOPTION.md`. Seven passes, zero adoptions,
and this version is the eighth thing that is not an adoption. The gate is correct and it is the only
item on the roadmap that matters.

## 0.13.0, 2026-09-08

**Two outside evaluations ran in parallel: one on skill craft, one on whether this deserves to exist
alongside comparable published work.** Both found defects that a self-audit structurally could not,
because both were about the collection's relationship to things outside it.

### The description was written to a limit that does not exist

`AGENTS.md` asserted, with no source, that the frontmatter `description` is capped at **200
characters** "by the upload surface". `build.py` enforced it. The documented limit is **1,024**.

The consequence is functional. The description is the only signal a model gets when deciding whether
to load a skill, and this one named five of about twelve covered areas. Requests about reviewing
agent-authored code, disclosure trailers, merge gates, benchmarking, spec-writing and session handoff
would very likely not have loaded it, though the body has dedicated rules and whole companion files
for each. **Every build printed `ok description is 198 characters` while the field that routes the
skill was starved.** Error 24.

Fixed: the cap now cites the documentation and its read date, the check **warns below 400
characters** because a cap cannot catch under-use, and the description is rewritten to 921 characters
naming the contexts rather than the topics.

### A conflict claim about a vendor had expired, and a live one was unrecorded

`SKILL.md` said, in the present tense and in two places, that repository overviews are "recommended
by model vendors" and were measured as not helping. It was the flagship example of independent
measurement beating vendor advice.

**Anthropic's current best-practices page lists "File-by-file descriptions of the codebase" and
"Anything Claude can figure out by reading code" in its exclude column.** The vendor agrees with the
measurement. There is no conflict left to cite. The rule is unaffected; the claim about who disagreed
expired. Error 25.

**And a real conflict existed at the same moment.** The same page cautions that "a reviewer prompted
to find gaps will usually report some, even when the work is sound", which cuts against this
collection's instruct-the-reviewer-to-disagree rule. Both are true and they measure opposite ends of
one dial: the paper measured under-reporting, the vendor warns about over-reporting. Now recorded
under disagreements with a stated default: keep the instruction and bound its output.

So the document carried two expired conflicts and zero live ones. `REFRESH.md` now **names the vendor
pages by URL** rather than treating them as a category, because a recheck that never opened them is
not a recheck of them.

### The overlap with vendor guidance was understated

`README.md` said this is "not competing" with vendor guidance, scoped to authoring. As of 2026-09-08
first-party guidance also covers fresh-context review, subagent delegation for context economy,
worktree isolation, context degradation, and converting a prose rule into a hook. **Roughly eight
Layer 1 rules now have a free, continuously updated first-party equivalent.**

The honest sentence, now in `README.md`: the vendors publish most of the workflow advice too, better
maintained than this can be, and what remains here is the strength marking, the profile conditioning,
the disagreements, and the things a vendor has no incentive to say.

### What the competitive evaluation established, and what it did not change yet

Two comparables were cloned and measured: `obra/superpowers` and `addyosmani/agent-skills`. Across
189 markdown files there is **one informal academic citation between them**, no confidence marking of
any kind, and no repository-profile mechanism. **So both differentiators hold.** Star counts were
verified independently against the GitHub API on the same day.

The evaluation recommends splitting the collection into a small skill and a standalone citable
evidence document, and cutting `SKILL.md` by roughly two thirds. **That decision is not taken in this
version.** It is a direction change and it belongs to the author, not to a verification pass. The
report is at `.agents/external-eval-2026-09-08.md` and the argument against its own recommendation is
stated there too.

### Also

- Three sources named that the collection should hold and does not: a FORGE 2026 code-health paper
  with an ACM DOI on the exact question the collection says nobody has answered, a Linux Foundation
  five-run `AGENTS.md` benchmark that independently corroborates the tier-1 rule, and arXiv:2605.11027
  as candidate prior art for the thesis itself. All three were unreachable from the evaluating
  environment. **A blocked network is not a finding**, so none is cited yet.
- `SKILL.md` is 525 lines against the vendor's published guidance of under 500. The evaluation
  reported 605, which is wrong; the finding stands at the corrected number.

## 0.12.0, 2026-09-08

**An external audit at 0.11.0 found three corrections that had never reached the files an agent
actually loads, and the primary sources were then obtained on paper.** Reading them reversed three
tier downgrades, settled the oldest open item on the roadmap, restored a figure this collection had
wrongly withdrawn, and exposed two numbers that appear nowhere in the paper they were attributed to.
Three new errors, one rewritten, and the changelog leaves the distributable.

### The agent-facing files were carrying withdrawn claims, one of them false about a named third party

Three corrections landed in `EVIDENCE.md` or `RESEARCH.md` and never propagated:

- **The trailer table.** `SKILL.md` and `WORKFLOW.md` still said seven projects had converged on
  `Assisted-by:`, two versions after that was replaced with a verified table showing **two camps and
  an abstainer**. Both were wrong about the **Apache Software Foundation**, which uses
  `Generated-by:`, and about **OpenTelemetry**, which prescribes no trailer at all. Both also named
  **LLVM and QEMU**, which no pass here ever verified.
- **The evidence-base withdrawal.** `DOCS.md` still said five repositories and still described the
  withdrawn third-party codebase, while the 0.8.0 changelog asserted every file had been rewritten.
- **The replication upgrade.** `SKILL.md` and `README.md` still said two independent groups and "the
  only replicated finding" after `EVIDENCE.md` went to four groups and multiply replicated.

All fixed. Recorded as **error 21**, whose lesson is that the file where a correction is easiest to
write is not the file where it matters. `AGENTS.md` now requires grepping the agent-facing files
specifically before a correction counts as done.

### Three tier-2 downgrades reversed, one upheld

The 0.10.1 audit moved four papers to tier 4 because their acceptance rested on a surface the authors
control. **The rule was right and three of the four downgrades were wrong.** The records existed and
were unreachable from a network-restricted session:

- **arXiv:2608.18167 restored.** OpenReview record, ICML 2026 Workshop DL4C, **Poster**, submission
  123.
- **arXiv:2605.16706 restored.** ICSME 2026 programme, **Visions and Emerging Results** track.
- **arXiv:2605.02273 restored.** EASE 2026 programme, **Short Papers and Emerging Results** track.
- **arXiv:2507.09089 stays at tier 4.** It never claimed a venue.

**A weakness in the scale that the restorations exposed and this version does not fix:** all three
are real acceptances in the lightest categories their venues run, and tier 2 flattens a workshop
poster together with a full research-track paper. Each entry now names its track. That is a patch on
the prose, not on the scale, and it is recorded as an open weakness.

### Two numbers that are not in the paper, published under a claim the paper had been read

The contested-security block asserted a table with "AI at 12.81 alerts per KLOC against human 11.58"
and a risk breakdown with "AI more high-risk, 0.934 against 0.464", in the same paragraph as the
sentence **"Both full texts were read on 2026-09-06."**

Against the PDF: **12.81 and 11.58 appear nowhere in the paper.** The high-risk row is **0.514
against 0.52**, which the paper calls *similar*, so the published figures reversed the direction of
the finding they named. The one correct figure, 10.04 against 13.56, is why nothing looked wrong.

The conclusion built on them, "both find elevated high-risk patterns in at least one cut", was the
pivot of the whole adjudication. It survives only in a weak language-sliced form: four of eight
languages higher, three lower. At the aggregate the contesting paper finds AI-generated code **lower
in alert density and cleaner on hardcoded secrets**, the second of which contradicts one of the two
defect classes this collection tells you to check for and had not been recorded at all.

**The safeguard stays, on the asymmetric-burden rule alone.** That rule has now done real work
against a source that genuinely hurts, which is the first time it has been tested rather than cited.
Recorded as **error 23**.

### The 2006 code review book was read, and the top roadmap item is settled

Both verification passes had it wrong. The famous "400" is **400 lines per hour**, a review rate:
reviewers slower than that were above average at finding defects, and above 450 lines/hour defect
density was below average in **87% of cases**. The second pass's "200 to 400 lines" and "70 to 90%"
come from a Q&A about reviewing your own code, where both numbers describe **a rate and its yield**.
That pass converted a rate into a size, which is exactly the misreading the collection was arguing
the popular rule commits.

**And the original headline was too strong.** The book does derive a 300-400 line ceiling, explicitly
as a hypothesis, from the 60-minute wear-out finding. So the popular rule is a hedged derivation
misquoted as a measurement rather than pure folklore. `WORKFLOW.md` now carries the quotations, the
distinction, and the caveat the book raises about its own strongest size result.

### A withdrawal that was wrong, and the rule that was missing

Error 19 previously recorded that gap 6 had joined a figure to the wrong qualifier. **The paper's
introduction says, verbatim, "ARTIFACTCOPILOT achieves the highest three-run mean exact badge
agreement at 70.56%."** The original text was right and the correction was made on a secondhand read
of the abstract.

Error 19 is now about the withdrawal. New rule: **a withdrawal needs the same primary-source standard
as an assertion.** Hard rule 1 forbids asserting an unseen figure and nothing forbade retracting one,
so a correct number was removed by a document whose entire argument is that you do not do that.

Gap 6 also gains the number that matters more than either: across three runs on 60 artifacts, the
best evaluator agent reproduced its own badge on **32 of 60**, with baselines from 37/60 down to
12/60 and failure rates up to 45%.

### An audit that fixed its own scope and not the rule's

The 0.10.1 venue audit checked all nine tier-2 papers. The tier-1 entry claimed a workshop acceptance
"confirmed from the paper's own front matter", the same disqualified surface, one heading above. It
was never looked at, and the entry then contradicted itself for two days, saying both "confirmed
workshop-accepted" and "both preprints". Both shipped. Recorded as **error 22**, and the boundary
table gains a sixth row: the check looked at tier 2, and the same rule applied to tier 1.

### `CHANGELOG.md` leaves the distributable

Same logic `build.py` already applies to `ROADMAP.md` and `CONTRIBUTING.md`: it governs this
repository rather than a consumer's. It had reached roughly 40 minutes of reading and 15% of the
distributable while telling a consumer nothing about what to do. It stays in the repository, where
anyone comparing two versions will look for it, and `README.md` says so.

### Also

- **arXiv:2607.27250's venue is now confirmed preprint-only** from the PDF, closing a "could not
  confirm" from 2026-09-03, and its finding is stated properly for the first time: a **bounded null**
  on context files, correctness effect within 10 and 15 percentage points by equivalence testing
  across 288 runs, with failures attributed to implementation skill rather than missing repository
  knowledge.
- **arXiv:2603.17973 stays tier 3** and **arXiv:2511.12884 stays tier 4**, both confirmed against
  their PDFs rather than against page metadata.
- **The venue check in `build.py` was widened.** Its first version accepted only a publisher DOI,
  which is narrower than the rule it enforces, and it fired on three entries correctly confirmed
  against OpenReview and two conference programmes. It now accepts all three routes the scale names,
  states its own proximity window as its scope, and was made to fail on purpose again.

## 0.11.0, 2026-09-07

**A practitioner account of running one workflow across two vendors' harnesses was read, graded, and
mostly not adopted.** What it produced is one new file and two tier-7 entries. What it did not
produce is a single number, which is the correct outcome for a source of that kind.

### New file: `HANDOFF.md`

A pasteable prompt that closes a session into a record the next session can act on: what landed, what
was decided and against what, what is deliberately **not** done, open questions with what would settle
each, and the verification with its scope stated.

`OPERATING.md` already carried the rule, that anything outliving a conversation goes into the
repository in the same turn it is decided, with **no mechanism attached to it**. This is the
mechanism, and it is the third pasteable prompt here after `SPEC.md` and `REFRESH.md`.

**It carries no outcome claim.** Nothing about session handoffs has been measured, gap 11 records
that agent memory architecture is unmeasured in general, and the argument made is the narrow one:
everything lost is lost in the gap between deciding and recording, and that gap is one turn wide.

Two design choices worth stating, because both come from failures already recorded here:

- **It writes to a file in the repository, never to a vendor's memory store.** A record only one
  harness can read fails at the moment you switch harnesses, which is the moment you most need it.
- **Section 6 forces the verification's boundary out.** "Tests pass" is compatible with several
  different failures, and a handoff reporting a clean result without its scope reproduces error 17 by
  hand.

### Two tier-7 entries, and a self-interest flag on both

The session-record-as-a-file mechanism, and a single context file read at session start that says
which stream of work a repository belongs to. Both are practitioner judgment with no comparison arm.

The flag is recorded because this collection insists on them elsewhere and would be inconsistent
without it: the source is content published about a subscription its author had just bought at a
stated monthly cost. **The accompanying performance and quota claims are not adopted**, being vendor
plan mechanics that rot within a quarter, which `SKILL.md` already treats as a defect rather than as
background.

### Gap 11 rechecked and unchanged, which is the finding

The gap says the only thing that exists on agent memory architecture is uncontrolled practitioner
writing. A fresh, well-built practitioner architecture arrived and turned out to be another instance
of that category. **Rediscovery is not replication**, and a gap describing an absence of measurement
is not closed by another unmeasured example, however good the example is.

## 0.10.1, 2026-09-07

**A third verification pass questioned two things the second pass had just added, and the audit it
triggered found that four of this collection's nine tier-2 ratings did not meet the tier-2
definition printed at the top of its own document.** Two new errors, four tier downgrades, two
tier-2 entries citing a publisher record for the first time, a new rule in the scale, and a new check
that reports the count on every build.

### Four of the nine tier-2 ratings did not meet the tier-2 definition

A third pass pointed out that an arXiv `Comments` line reading "accepted at X" is written by the
submitting author and verified by nobody, and that two entries here rested on one. **Treating that as
a question about the rule rather than about those two papers**, all nine papers rated tier 2 were
audited. Four moved to tier 4.

**Held, and now cite the record rather than the claim:**

- **arXiv:2508.21634**, IEEE Xplore 11229706, DOI 10.1109/ISSRE66568.2025.00035, pages 252-263.
- **arXiv:2507.00788**, Empirical Software Engineering, DOI 10.1007/s10664-026-10889-1. It is also
  **the only preregistered study in the collection**, through a Registered Reports track, which this
  document did not know and which is a stronger guarantee than ordinary review against the failure
  mode it worries about most.
- **arXiv:2504.16485** and **arXiv:2604.03196**, both already citing publisher records.

**Moved to tier 4**, in a new subsection for entries moved down from tier 2:

- **arXiv:2608.18167**, acceptance claimed in `Comments`, no reachable venue listing.
- **arXiv:2605.16706**, recorded as accepted at a named conference, found on arXiv and nowhere else.
- **arXiv:2605.02273**, recorded as EASE 2026 on the strength of a conference banner in the paper's
  own typesetting. It was the second paper in a paired entry, sitting behind the other paper's DOI.
- **arXiv:2507.09089**, which **never claimed a venue at all** and had been tiered on the quality of
  its randomised design. That is grading by method rather than by review trail, which is the one
  substitution this scale exists to prevent, committed in the scale's own document.

**Every rule built on the four downgraded papers stands**, at the lower tier, on the asymmetric-burden
rule: a weak source may raise a doubt about a safeguard and may not retire it. `SKILL.md` and
`OPERATING.md` carry the new tiers where they state those rules. The clearest case is the developer
speed-estimate study: the rule it supports is "believe your own speed estimate less", and a lower tier
is not an argument for believing it more.

New in the scale: **an author-controlled surface cannot confirm a venue.** Not the arXiv `Comments`
field, not a conference banner the authors typeset, not an institutional page, not a lab's
replication repository, not a ResearchGate entry. And **an arXiv DOI is not a publisher DOI**, which
is the specific way this nearly went wrong on a sixth paper.

New check in `build.py`: it reads every tier-2 entry, counts the preprints it names against the
publisher records it cites, and reports both. It **warns rather than fails**, because a failing build
here would be fixed by deleting the check. It was made to fail on purpose before being believed, and
the per-paper count rather than a per-entry one is what surfaced the fourth downgrade.

### A number was taken from one sentence and its qualifier from another

Open gap 6 read "three-run mean exact-badge agreement of 70.56%". The source reports 70.56% as its
best system's **exact badge agreement**; "three-run mean" belongs to a different sentence, about a
10.55 to 28.34 percentage-point improvement. Both halves are in the abstract. The join is not.

This is the hardest paraphrase error to catch yet recorded here, because **the number is exactly
right**: a check that verifies figures against the source passes it, and only reading the two
sentences together shows the problem. New rule: a figure and the words qualifying it must come from
the same sentence.

### Errors 19 and 20, and the boundary table gains a fifth row

The pattern behind errors 9 and 17, a check drawing its boundary at the convenient unit, now has a
fifth instance that has nothing to do with identifier leaks: the check looked at the paper's arXiv
page, and the venue record was at the publisher. The audit repeated the shape once more before
escaping it, reading one record per entry while a second paper sat behind the first one's DOI.

### New section: outside checks, and what each one cost

Five of them now, tabulated at the end of `EVIDENCE.md` with what each one found. **The 2026-09-07
recheck states its own limit**, which is that arXiv, DBLP, IEEE Xplore, OpenReview and the authors'
pages were all unreachable from the environment it ran in, so its confirmations came through a search
index of those pages rather than the pages themselves. One step further from the primary source than
this collection's rules ask for, recorded rather than buried.

### What did not change

**The recheck date stays 2026-09-06.** This was a targeted recheck of two claims, not a pass over
every external claim, and moving the date would reset the ninety-day staleness warning on the
strength of work that did not cover it. That is the same boundary error the fifth table row is about.

## 0.10.0, 2026-09-06

**A second independent research pass ran, and the case for running two rather than one is now
demonstrated rather than argued.** Each pass reached primary sources the other could not, and the
combined answer is different from either alone.

### The trailer table is now complete, and the answer is a split rather than a convergence

The first pass established that the Apache Software Foundation and OpenInfra use `Generated-by:`,
and correctly **refused** to assert Fedora and Rocky Linux from aggregators. The second reached all
four primary pages the first could not. Together:

- **`Assisted-by:`**: the Linux kernel, Fedora, Rocky Linux. The kernel gives the exact form,
  `Assisted-by: LLM [TOOL1] [TOOL2]`, and states AI agents **MUST NOT** add `Signed-off-by`.
- **`Generated-by:`**: the Apache Software Foundation, OpenInfra.
- **No token at all**: OpenTelemetry, which describes assistance levels instead.

So the original claim, seven projects converging on one trailer, was wrong in a way that matters:
**there are two camps and an abstainer.** What is genuinely converged is the structure, disclose
without claiming authorship, and never in a field carrying legal certification.

**Neither pass alone produces that table.** One found the divergence, the other found the sources.

### A tier upgrade, and a contradiction adjudicated rather than left standing

**arXiv:2508.21634 is accepted at IEEE ISSRE 2025**, not a preprint. Moved from tier 4 to tier 2,
where it sat mis-tiered for two days because the first pass did not reach its acceptance line.

Both full texts of the contested security pair were then read, and the disagreement is **real but
narrower than it looked**. Different populations: prompt-generated functions against AI-generated
files found in the wild. Different instruments: Pylint, PMD and Semgrep against CodeQL. Different
normalisation, and the preprint's own cuts do not agree with each other, reporting AI both above and
below human alert density in different tables.

**Where they agree is the part that matters: both find elevated high-risk patterns in at least one
cut.** The disagreement is about totals and severity bands, and it dissolves substantially once
population and instrument are compared. Not entirely.

### Three new gaps, and one of them undercuts a framing this collection has leaned on

- **Gap 9. What fraction of repositories retain a review trail at all.** The collection's most-wanted
  counter-example was a repository with a retrievable review trail. Several exist: Gerrit corpora
  with reviewer and approver metadata across roughly 133,000 changes, GitHub pull-request corpora
  across 37 projects. **So retrievable review trails plainly exist**, which weakens the implicit
  framing that their absence is normal. What nobody has published is the population figure, and that
  single number would settle whether four-for-four here is a quirk or a property of git.
- **Gap 10. Whether human review catches AI-introduced defects at normal rates.** Neither security
  study measures it. Every recommendation here about reviewing agent output assumes review works on
  it about as well as on human code, and that is untested in either direction.
- **Gap 11. Agent memory architecture, where this collection has no entry at all.** A 2026 survey
  organises five mechanism families and says empirical comparisons for coding agents are sparse.
  Everything else found was practitioner writing with no measured outcome. **No study shows
  retrieval-augmented memory beating a flat file for coding-agent task success.** Recorded because a
  gap with a mature-looking vocabulary is more dangerous than one that is obviously empty.

### Gaps B and C

**Gap B narrowed.** arXiv:2601.16746 reports that **uniform compression hurts more than task-aware
pruning**, the first direct evidence that which tokens are dropped matters rather than only how many.
It publishes no ablation by content type, which is what the gap asks for.

**Gap C re-searched and still open**, with the exact strings recorded so the next person does not
repeat them.

### The citation-difference figure is restored with a real source

Withdrawn in 0.9.0 as unlocatable, now found: **Winter et al., ESEC/FSE 2022, peer-reviewed**, 3,650
articles across 64 venue-years. Significant citation differences for **2 of 64 pairs** after
Benjamini-Hochberg correction, and both were **short papers without badges**, which is the opposite
of what a badge advocate would predict.

### Also

- `REFRESH.md` and the build's staleness check, which were written for 0.9.0 and did not reach the
  remote before the branch was deleted.

## 0.9.0, 2026-09-06

**An independent research and verification pass ran, and it contradicted a headline.** One new file,
one new error, four new gaps, one finding that bears on the collection's own architecture, and a
claim upgraded from replicated to multiply replicated.

### The architecture criticism, which is the most important item here

**Evidence hierarchies have measurably poor inter-rater reliability, and this scale is not exempt.**
Trained raters applying a mature grading scheme to the same evidence agree at kappa around 0.27,
worse than chance on four of twelve outcomes in one test. This scale is younger, less documented and
has been applied by one person.

The tier scale already warned that a tier is not a correctness score. It now says the
better-sourced version: **a tier is a judgment made by whoever assigned it, with known disagreement
between raters, not a measured property of the source.** Two people applying it to the same paper
will sometimes differ and neither is necessarily wrong.

It cuts both ways honestly. It **strengthens** the asymmetric-burden rule, because noisy grades make
"a weak grade may not retire a safeguard" do more work. And it does not invalidate the scale: the
critique literature's own conclusion is that hierarchies are useful and oversold.

Recorded alongside it because it explains an absence: evidence-based software engineering kept its
systematic-review half and largely abandoned its grading half. This collection is attempting
something the field tried and dropped.

### The contradicted headline

**`RESEARCH.md` said seven named projects converged on an `Assisted-by:` git trailer while barring
AI from `Co-Authored-By:`. Both halves were overstated.** The Apache Software Foundation and
OpenInfra use **`Generated-by:`**, and those two were the most carefully verified of the seven.
Fedora and Rocky Linux were never verified at all and are now marked as such rather than sitting in
a list as though they had been. The `Co-Authored-By:` prohibition is one project's explicit policy
stated as a cross-foundation rule.

The paragraph is replaced with a per-project table carrying a verification-status column. **The
convergence is real but it is on the structure, disclose without claiming authorship, and not on the
string.**

One item got sharper: the **EU AI Act, in force 2 August 2026**, requires AI-generated public text to
be labelled, and at least one major foundation now says so in its guidance. That is the first
provenance item in the file with enforcement behind it.

### Error 18: a measured finding restated as measuring something else, in a template

`templates/AGENTS.md` said **"do not add a directory tree: measured as not helping"**. What is
measured is that **repository overviews** do not help. No measurement of directory trees was found.

It is errors 6 through 8's shape in the worst possible file, because a template propagates verbatim
into other people's repositories while the document that could correct it stays behind. `ROADMAP.md`
had listed the templates as the likeliest place an unsupported claim was still sitting, which was
correct and did not retire the risk.

Corrected by scoping rather than deletion: the measured half keeps the word measured, the unmeasured
extension is labelled judgment, and the independent reason to drop a tree, that it duplicates the
readme, stands on its own.

### Nondeterminism: replicated to multiply replicated

Two more independent groups, four in total, and the **causes are now named rather than inferred**:
floating-point non-associativity, batch-size variation under concurrent server load, and
non-deterministic kernel scheduling. One source confirms that reasoning models **no longer expose a
temperature parameter**, which this collection had listed as an open question. Every single-run
number here inherits a larger caveat than before, not a smaller one.

### Gap A hardens, and what would close it changed

Thirteen further queries found nothing qualifying. The strongest near-miss is now a **Management
Science 2026 RCT, N=4,867, preregistered**, which collects **no defect outcome at all** and whose
co-author says so plainly.

That reframes the gap. The best-powered randomised platform in the field deliberately did not
instrument defects, so closing this looks less like mounting a fresh trial and more like **bolting a
secondary outcome onto an existing one.**

### Four new gaps

1. Nobody is instrumenting defects on the trials that could carry it.
2. **The grader is becoming an agent.** Agent-based artifact evaluation now runs three repeated
   passes to handle its own evaluator's nondeterminism. Agent nondeterminism now threatens the
   badging process, not only the artifacts.
3. A binding legal provenance regime arrived under the voluntary conventions.
4. The aggregate security direction is contested.

### A contradiction logged rather than resolved

A large real-world measurement reports **fewer analyzer alerts and lower defect density** for
AI-generated code, opposite to the direction this collection held. Neither paper's numbers are
restated, because neither full text was read. The disagreement stands with a default: keep checking
for the two named defect classes, because they are cheap to check and a contested source may raise a
doubt without retiring a safeguard. **Both studies count analyzer alerts, so neither answers whether
human review catches these at normal rates.**

### New file: `SPEC.md`

A pasteable prompt that specifies a change before it is built: numbered assumptions with stated
alternatives, verifiable success criteria, a test-impact map verified against the code rather than
from memory, out-of-scope by name, and a deliberate stop before implementation.

A document rather than a slash command, because command file formats are vendor-specific and
`ROADMAP.md` rules those out. **It carries no defect-reduction claim.** The argument for it is that
disagreement surfaces while changing course is still free, which is a scoping and cost argument and
is sufficient.

### One boundary rule, extracted from four instances

Four times in this repository a check drew its boundary at the convenient unit and the exposure sat
one unit outside: contents but not metadata, one ref but not all refs, the distributable but not the
repository, the prose files but not the changelog. Every check passed and every one was correct
within its scope. **None stated its scope.** The rule is now explicit: a check reports the boundary
it drew, next to its result.

### Also

- `OPERATING.md` splits "vendor" into who trained the model and who sells the harness. A harness
  serving another lab's model is **same-vendor for review independence and cross-vendor for
  everything else**, which is the worst case to be in unknowingly.

## 0.8.0, 2026-09-06

**The evidence base got smaller on purpose.** Every first-party observation drawn from a repository
the author does not personally own has been withdrawn. No claim was corrected and nothing was found
to be wrong. The material was removed because it should not have been the author's to publish.

### What went, and what it cost

The withdrawn case was a large, long-lived, closed-source codebase, and it was the only one in the
collection observed at organisational scale. Losing it costs real things and they are named rather
than glossed:

- **The scale findings.** An entire section of `SKILL.md` on what size and age do not fix, including
  the merge-signal, written-convention, branch-naming and identity-fragmentation figures.
- **The documentation-rot confirmation at scale** in `DOCS.md`, which was the strongest support for
  the taxonomy's known bias toward repositories that never audit.
- **Five entries in `SECURITY.md`'s repository obligations**, covering fail-open auth defaults, raw
  database errors reaching model context, privileged accounts contradicting the documentation,
  liveness-endpoint disclosure, and unrotated debug captures.
- **The evidence base itself**, from five repositories to four, all small, one or two people each.

Every place that described the base has been rewritten to say four rather than five, and to say
plainly that **nothing here is observed at organisational scale**. A reader who took the earlier
framing as partial protection against the small-sample problem should re-read the warnings, because
that protection is gone.

### Why, since the reasoning generalises

De-identification was doing the work, and it was doing it well enough that an agent reading the text
could not tell which observations came from where. **That is not the same as safe.** De-identified is
not anonymous: rounding a commit count defeats a stranger and defeats nobody who already knows the
codebase. Combine the text with knowing where an author works and the case is identifiable.

`ROADMAP.md` had already dropped a blog post drawing on the same material, on the grounds that it
was attributable by employment and unflattering about people who had not agreed to be studied. That
reasoning applied to the collection too and had not been carried across. It has been now.

The remaining `SECURITY.md` obligations and every remaining first-party claim come from repositories
the author owns.

### The part that is easy to get wrong

**Removing text in a commit does not remove it from the repository.** That is error 17's lesson,
learned here eight commits ago in a different form, and it applies directly: a withdrawal is complete
only once history no longer carries the withdrawn text. The publication sequence in `ROADMAP.md` now
starts with confirming that rather than with going public.

### Also

- Publication is no longer blocked on a clearance conversation, because the material needing
  clearance no longer exists.
- `ROADMAP.md`'s "deliberately not doing" list now forbids the whole category rather than one
  artifact drawn from it.

## 0.7.1, 2026-09-04

**The collection was published for the first time, and publishing it produced the worst-consequence
error on its list.** No claim changed. Everything here is packaging, licensing, governance, and one
error entry.

### Error 17: the leak check read the half that was clean

Every commit was authored and committed under an employer email address. The identifier-leak check
read **file contents**, which is not where the address was, so it reported clean while the prose was
de-identified and the commit headers re-identified it. One `git log` recovered exactly what the
rounding in `EVIDENCE.md` exists to hide.

The fix was then verified on the current branch while a second branch still pointed at the original
commits, so the address stayed published while the check said it was gone. **Same mistake twice in
one afternoon, in the same direction**: the boundary drawn at what was convenient to search rather
than at where the identifier could be.

This is error 9's shape a third time, and its consequence class is new. Every other entry is a wrong
claim, correctable in a later version. **A distributed identifier is not recallable by a version
bump.**

`build.py` now reads `git log --all` over author, committer and message, and reports the count of
commits and refs examined. It fails rather than passes when git is missing, when git log errors, and
when zero commits are found. It was made to fail on purpose against a leak planted on a non-current
ref before it was believed.

The metadata pattern is deliberately narrower than the prose pattern: **skill prose must name nobody,
the author included; commit metadata must name the author**, because that history is the ownership
record. Only the employer identifiers are forbidden in both.

### The licence is now split, and the reason is the collection's own argument

**MIT for `templates/`, `examples/`, `build.py`, `.claude-plugin/`. CC BY 4.0 for the prose.**

MIT permits use without attribution. That is correct for a template, which exists to be copied with
no obligation travelling with it, and wrong for a document collection whose entire argument is that a
claim should be traceable to who made it and when. CC BY requires the credit that makes a corrected
claim followable back to its source, which is the same thing the versioning rule asks of consumers.

### Packaging that did not work and now does

The first `marketplace.json` carried a `plugin` key and no `owner` or `plugins` array. It was
well-formed JSON, resolved as nothing, and would have failed `/plugin marketplace add` while every
local check passed. Corrected against the published schema, with a `plugin.json` alongside it.

### `RESEARCH.md` now warns that it is single-pass

It rests on one research pass, none of its external claims have been fetched by a second reader, and
it was written in the same session that produced error 14. The warning went in **before** the
verification rather than after, because a warning that waits for a pass that may not come is worth
nothing. The adoption lists are flagged as the likeliest thing there to be wrong.

### Also

- `CONTRIBUTING.md` and `CODE_OF_CONDUCT.md`, both excluded from the distributable because they
  govern this repository rather than a consumer's. `.github/SECURITY.md` for vulnerability
  disclosure, which is a different document from the root `SECURITY.md` despite the name.
- Two error counts that had drifted in opposite directions: the readme said sixteen, `CITATION.cff`
  still said fifteen. A count that no longer matches is a defect by this collection's own rot
  taxonomy, and one of them was already wrong before this version.

## 0.7.0, 2026-09-04

**Three independent verification passes ran against this collection, and the checking found more
than the research did.** Two errors, one fabricated statistic, four items where the passes disagreed
with each other, and one new peer-reviewed source that narrows the collection's biggest stated gap.
Plus a new file on where research standards and engineering practice converge.

### Error 14, and it is the worst one on the list

**A fabricated statistic was in this collection for a day.** A figure reporting that a single agent
matched or beat multi-agent systems on **64% of benchmarked tasks**, with multi-agent adding **2.1
percentage points at roughly twice the cost**, attributed to a named university group.

A verification pass traced the wording to **a search-optimised blog post naming no paper, author or
identifier**, then fetched the one genuinely related paper in full and **found none of those numbers
in it**. Recorded as *could not source* rather than *confirmed false*.

Why it is worse than everything before it: earlier errors were real sources restated badly or
misattributed. **This had no source at all**, and it arrived wearing an institutional name that made
it feel checkable. A research agent produced it and this document recorded it, because it was
specific, quotable, and agreed with a position already held. **It also survived the first external
review.** New rule: a statistic that is specific, quotable and flattering to your position gets its
primary source fetched **before** it is written down.

The two real papers replacing it are better anyway, and one adds a nuance the invention lacked:
automatically-generated multi-agent systems underperform while costing **up to 10 times more**, but
**expert-architected ones do outperform automatically-generated ones**. So part of what is being
measured is the automation of the architecture, not the architecture.

### Error 15: independent passes disagreeing with each other

**A new epistemic category, and a new section in `EVIDENCE.md`.** On four items the sources agree
with themselves and **two independent verification passes extracted different figures**. That is a
defect in the reading, not the field, and neither number can be asserted:

1. **The pull-request size numbers, which undercuts a headline.** `WORKFLOW.md` led on the claim that
   "under 400 lines" misreads a 2006 study by turning a review *rate* into a *batch size*. One pass
   read the recommendation as 100 to 300 lines over 30 to 60 minutes; the other as **200 to 400 lines
   over 60 to 90 minutes**. If the second is right, the popular rule is roughly correct and this
   collection was wrong. The headline is withdrawn and replaced with what survives either reading:
   **the numbers attributed to that study vary between retellings, so no threshold from it is safe to
   cite.**
2. **The developer-written context-file gain**: 2.4% against 4%. This collection had already
   "corrected" 4% to 2.4% on one pass, which was premature.
3. **Two venue statuses**, where one pass confirmed acceptance and the other found no acceptance line
   on the paper itself. Both now tiered provisionally.

**Why this section matters more than the individual items.** Independent verification was meant to
raise confidence and on most claims it did. On four it **lowered** confidence. A collection that only
ever gains certainty from being checked is not being checked.

### Corrections from primary sources

- **Tier 1 upgraded.** One of the two nondeterminism papers is **published at an ICLR 2026 workshop**,
  not a preprint. The scale correction it originally forced still stands, for a different reason.
- **A figure this collection should have been quoting all along**: the gap between pass@1 and pass@5
  reaches **24.9 percentage points**, and pass@1 to pass^5 reaches **18.9**. That is the distance
  between the number you would report and the number you could rely on, and it is now in the
  measurement rules.
- **A rule was scoped rather than corrected, and the scoping reverses it in one case.** Generated
  instruction files hurt when documentation already exists, but **improve performance by about 2.7
  percentage points when existing documentation is removed**. So the rule is "do not generate one
  over the top of existing docs", not "never generate one".
- **The autonomy figures were wrong in two directions.** The roughly 89-day doubling time **is the
  measurement programme's own** post-2024 figure, not a tracker extrapolation as this file claimed;
  and the current horizon is **at least 16 hours, not 14**, with a confidence interval running from
  about 8.5 to 55 hours and the programme's own caveat that anything past 16 is unreliable.
- **A memory benchmark score was quoted as a subtask score.** The widely cited 63.8% is an
  **overall** figure; the same paper's temporal-reasoning breakdown is 54.1% and 62.4%. And in both
  leading memory cases **the paper's authors include the product's own team**, which is worse than
  vendor-adjacent.
- **A cost multiple was third-party.** The "100 times the compute" figure for tree search is an
  estimate from a different paper; the original says its method used tokens comparable to about a
  hundred chain-of-thought trials.
- **A judge-concordance range was domain-scoped.** The 0.66 to 0.96 range with median 0.83 comes from
  a review whose 13 underlying studies are **all clinical**. Presented as general here. Corrected.

### New sources, including the most important addition to date

- **A peer-reviewed journal controlled experiment, 151 participants, roughly 95% professionals.**
  Phase one: AI assistance gives a **30.7% median reduction in completion time**, 55.9% for habitual
  users. Phase two: *different* participants, randomly assigned, evolve those solutions **without**
  AI, and there is **no significant difference** in evolution time or code quality, with a Bayesian
  analysis calling any improvement "at most small and highly uncertain". **This narrows the
  collection's biggest stated gap** and shows the previous "nobody has measured this" wording was
  closer to overclaiming than it should have been.
- **Developers cannot introspect their own throughput.** A randomised trial: 16 experienced
  open-source developers forecast **24% faster**, believed afterwards they had been **20% faster**,
  and were measured **19% slower** with an interval of +2% to +39%.
- **AI-generated code carries more of two specific defect classes**, from over 500,000 samples across
  two languages: unused constructs and hardcoded debugging artefacts, plus more high-risk security
  vulnerabilities.

### New file: `RESEARCH.md`

Answers a sharper question than the one originally asked. Not "what are the scientific conventions"
as a separate topic, but **where do research standards and engineering practice converge** since
convergence from different starting points is real evidence about a rule even when neither side ran
a trial.

The strongest case: **two communities reached an identical rule for an identical legal reason,
apparently independently.** Engineering converged on an `Assisted-by:` trailer while barring AI from
`Co-Authored-By:`; all four major publishers state AI cannot be an author but disclosed use is
permitted. The shared reason is that a co-authorship field is an ownership claim, and naming an AI in
one risks attributing rights to its vendor.

**And one open problem stated as confirmed absent rather than merely unconfirmed:** a search across
eight 2026 artifact-evaluation calls found **none** mentioning agent nondeterminism, seed variance or
multi-run reporting as a badge criterion. **Nothing currently defines what "reproducible" means for
an agent pipeline.** Given that this collection's only replicated finding is that agent runs are
nondeterministic even at temperature 0, that gap is squarely in the path of anyone trying to publish
agent-based work.

Also practical: `CITATION.cff` plus an archival-repository DOI is a mature, adoptable-today route to
making a practitioner document citable and version-pinnable in a form a researcher will accept.

## 0.6.0, 2026-09-04

Two new files closing two real gaps, and **the first pass where every external claim in
`EVIDENCE.md` was fetched from its primary source rather than trusted as reported.** That pass found
two errors and one unverifiable sub-claim.

### Corrections, and the first one is the collection's own thesis landing on itself

- **The "keep pull requests under 400 lines" rule is folklore, and now documented as such.** The
  source is a 2006 study of roughly 2,500 reviews and 3.2 million lines. What it actually found:
  **anything below 200 lines produced a relatively high defect rate**, reviewers slower than **400
  lines per hour** found more defects, effectiveness dropped after about **60 minutes**, and the
  recommendation was **100 to 300 lines over 30 to 60 minutes**. The popular rule takes a *rate*,
  lines per hour, and turns it into a *batch size*, then rounds the real figure up. This is the same
  failure as the 30-line instruction file this collection opens with, better documented, and it is
  now the headline example in `WORKFLOW.md`.
- **A figure was attributed to the wrong paper.** The 1.5x bug-introducing statistic for inconsistent
  comments was credited to a 2019 mining study of 1.3 billion changes. It is not in that paper; it
  belongs to a separate later one. The 2019 study's real finding is that **impact is highest
  immediately after an inconsistency appears and decays over time**, which is more actionable than
  the figure that displaced it. Error 12.
- **A figure was overstated by more than half.** Developer-written instruction files gained **2.4% on
  average**, not "roughly 4%". The rule built on it survives, because it depends on the direction
  rather than the size, but the number was wrong. Error 12.
- **An unverified sub-claim had propagated to four documents.** The nondeterminism entry had acquired
  a detail about interquartile ranges at different temperatures; the paper contains no interquartile
  comparison. Retracted as **unconfirmed rather than contradicted**. Error 13, and the instructive
  part is the spread: one unchecked detail reached `SKILL.md`, `OPERATING.md`, `EVIDENCE.md`, the
  changelog and the published page. New rule: **when a figure is corrected, grep the whole collection
  before calling the correction done.** The changelog is excepted and corrected by a new entry rather
  than an edit, per this collection's own rule about history, which is why the 0.4.0 entry still
  carries the retracted phrasing.

**Everything else checked out**, including several with added precision: the Snyk figure is 36.8% or
1,467 skills with **at least one security flaw** and 76 confirmed malicious payloads, with a separate
13.4% at critical severity that must not be conflated; both CVE mechanisms confirmed in detail, and
the Cursor one is sharper than recorded (shell built-ins bypass the allowlist, poison the
environment, and a later *allowlisted* command carries the payload, so **the command name was never
what mattered**).

### New file: `WORKFLOW.md`

Branch, merge, pull request and pre-merge gate conventions. **Filing slash-command *authoring* as
out of scope was right; letting the workflow conventions those commands encode fall through the same
gap was wrong**, and they had been scattered across three files with no consolidated treatment.

The file leads with how little is measured, because that is the finding: PR size rests on one 2006
case study, trunk-based development on correlational survey data whose own authors do not claim
causation, **merge strategy on nothing at all** (a deliberate search found no measurement comparing
squash, merge and rebase against bisectability, revert success or blame usefulness), gates on
plausible reasoning with bypass rates undocumented, and commit conventions on measured adoption with
purely asserted benefit. The AI-specific layer is early and mostly self-reported, including a survey
figure of **PR size up about 154% and review time up about 91%** alongside AI adoption.

### New file: `TOOLING.md`

A functional map of what goes around an agent, by category, with dated examples that are explicitly
illustrations rather than endorsements. **Refusing product rankings was right; refusing a category
map was an accident**, and "am I missing a whole category?" is a different question from "which is
best" with a different shelf life.

Nine categories, and the map surfaced one that had been missed entirely: **permission and policy
gating**, distinct from sandboxing, because sandboxing limits what damage a call can do while gating
decides whether the call happens. It is the most-skipped category and it matters even solo. Closes
with an opinionated view of what a solo developer actually needs, and the pattern that everything in
that list constrains the agent while everything in the team list observes it.

### Deepened: `VOCABULARY.md`

A hunt framed to **disconfirm** this collection's position on multi-agent systems. On accuracy it
found nothing: no 2026 result showing multi-agent beating a single agent under matched compute on
software tasks, recorded as **could-not-confirm rather than confirmed-absent**. On cost it found a
real and different claim, orchestrator-worker routing to cheaper specialists. And the mechanism
behind the negative results got sharper: reported multi-agent gains are argued to be **uncontrolled
inference-budget artifacts**, which predicts the gain vanishes under matched budget, and that is what
budget-controlled comparisons find.

Also added a **long-horizon autonomy** section with the reliability wall stated carefully: task
length at 50% reliability doubling roughly every seven months, frontier agents around the 14-hour
human-equivalent mark, a much shorter doubling figure circulating that is **a tracker extrapolation
and not the measurement programme's own number**, and the programme's own caveat that estimates past
about 16 hours are unreliable because the benchmarks saturate. **50% reliability is not an operating
point**, which is the honest answer to "can I leave it running".

## 0.5.2, 2026-09-03

**First external review, and three accepted criticisms.** Someone outside the project read the
published collection and pushed back. All three points were valid and all three are fixed. The review
also independently verified three citations against primary sources, including the agent-skill
security figures that an earlier version had inflated nineteenfold, so the correction now has outside
confirmation.

- **A tier number was reading as a truth score.** A design flaw, not a reading error: the scale is
  *named* by review trail and *numbered* like a quality ranking, and numbering carries rhetorical
  weight no disclaimer removes. The scale now opens by stating plainly that a tier records how much
  scrutiny a claim survived, not whether it is right, and that a tier-4 preprint can be correct while
  a tier-2 paper can be wrong.
- **First-party claims carried more confidence than their sample earned.** The dramatic figures have
  a large N *within* one case and an N of one *across* cases, and that distinction was stated once in
  the axis section and never where the numbers appear. Both numbers are now named explicitly at the
  axis, with the instruction to read a first-party figure as strong about its own case and weak about
  yours.
- **"Disagreements left standing" offered nothing to do on Monday.** The sharpest criticism. An honest
  map of uncertainty is not a decision tool, and the asymmetric-burden rule covers a weak source but
  not a tie. **All five standing disagreements now carry a `Default`**, chosen on the rule of
  cheapest to reverse and least damaging if the other side is right, and labelled judgment rather
  than evidence so it can never be cited as a finding.

**One correction to the review, which was this collection's own fault.** It counted nine recorded
errors when there were ten, having read a published version that predated the tenth. That is the
staleness problem this collection warns about, arriving through its own distribution channel. Noted:
**state the version when soliciting review.**

**Error 11 recorded, found while shipping this release.** Shortening the frontmatter `description` to
fit a 200-character cap introduced a colon followed by a space, which a YAML plain scalar cannot
contain, so the value truncated at the first colon and the tool displayed the document heading
instead. **Every existing check passed**: length, em dashes, identifiers, links. None of them knew
the field had a format constraint. The symptom was the tool's own listing changing, which was nearly
dismissed as a display quirk. New rule: **a field with a format constraint needs a check that knows
the format**, so parse the frontmatter as YAML rather than measuring its length.

## 0.5.1, 2026-09-03

**Adds `ADOPTION.md`**, a two-phase prompt that adopts the collection in one repository. Patch rather
than minor because **no claim, source, tier or rule changed**: it packages a procedure the collection
already implied but never stated in one place.

What it adds over reading the files in order is **sequence and refusal**. It puts security before
documentation, forbids copying a profile from `examples/`, requires reporting before changing
anything, and stops between deriving the profile and acting on it, because phase two is wrong if
phase one guessed. Those are the three places an adoption pass usually goes wrong.

Also promoted in `README.md` from "write a profile first" to "start here", since the honest answer to
how somebody should begin is a prompt, not a reading order.

## 0.5.0, 2026-09-03

The release that exercised the central mechanism for the first time.

**Two repositories now carry a profile, and they are genuinely different shapes**: a C# work
repository with all four documentation slots filled, and a Python and TypeScript repository that
deliberately has neither a changelog nor a roadmap. Until today the adapt-rather-than-prescribe
claim, which is the whole differentiated pitch, **had never been run anywhere**. It has now been run
twice. That is still two repositories and still one observer, so it is a minor version rather than a
1.0.

**`PROFILE.md` gained a seven-step derivation procedure with the actual commands**, ordered by
dependency rather than by importance. It was written by deriving two real profiles and recording what
that took, not by imagining the process. Two steps carry hard-won detail:

- **`reviewers` requires counting, not reading a policy**, and requires trying **three different
  pull-request wordings**, because the single-wording version of that check already produced a false
  absence in this collection's own research: zero pull requests reported where 36 existed.
- **`secrets` is verified with `git log -- <path>`**, not with the ignore file, and the procedure says
  plainly that the history command is the only one whose output is evidence.

**Identity fragmentation is not a team problem.** It was filed as one, observed in a six-person and a
fifty-person repository. Then `git shortlog -sne` on a **solo** repository resolved to **three
identities for one person**: two spellings of a surname and two letter cases of one email address. So
it is a per-machine-configuration problem that teams merely make visible. Generalised accordingly,
which makes the claim both broader and better supported.

**The documentation method bias is now measured rather than argued.** Commits mentioning
documentation: about **21%** in one repository against about **0.03%** in the large industrial
codebase. Three orders of magnitude apart, and the difference is not documentation quality but
whether anyone ever looks. `DOCS.md` has argued this since 0.1.0 with one supporting case; it now has
two, at opposite extremes.

**A third instance of the dominant error shape.** A file-count command ran cleanly and reported 40,814
Python source files, having counted a virtual environment's installed dependencies. Had that number
been used it would have been a confidently wrong figure with a real command behind it. Alongside the
inert link checker and the wrong-platform search, **commands that execute correctly and measure the
wrong thing now have three recorded instances**, which is enough to treat it as the failure mode this
collection is most prone to. Both new profiles deliberately carry no file counts, and the new
procedure avoids recursive scans.

## 0.4.0, 2026-09-03

Two new files, and one inventory that changed what the collection can honestly claim about itself.

**A third context was inventoried, and its findings were the most useful first-party data the
collection held.**

> **Redacted 2026-09-06.** That context was a repository the author does not own, and every
> observation drawn from it was withdrawn in 0.8.0. The findings that stood here are gone from the
> collection and are gone from this entry. What survives is the shape of the lesson, kept because
> two later errors are unintelligible without it: **scale and age did not produce the discipline the
> small teams lacked**, a review mechanism was adopted and abandoned with nothing recording either
> decision, and documentation existed while being essentially never corrected in a way that left a
> record. No figures are restated. See the 0.8.0 entry for why the withdrawal happened and what it
> cost.

**Error 10 recorded, and it is the most instructive one on the list.** The first version of the above
reported **no pull-request flow at all**. The inventory had searched for one hosting platform's
merge-commit wording against a repository hosted on a different platform, so 36 real pull requests
returned zero matches and were written up as *confirmed absent*. It was **caught by a reader who knew
which platform the repository used**, not by the tool or the author. It also defeated an existing
rule: the collection already required separating "could not confirm" from "confirmed absent", and
this search genuinely completed and genuinely matched nothing. New rule added in both `SKILL.md` and
`EVIDENCE.md`: **before reporting an absence, state what shape you searched for and confirm it is the
shape this system would produce.**

**A fourth warning was added to the front of the collection**, and it constrains every first-party
claim: **absence of a recorded signal is not absence of the practice.** Git proves what was written
down. A team that reviews by screen-share leaves the same trace as a team that does not review.

**New file, `OBSERVABILITY.md`.** The collection could say how to evaluate a change and nothing about
how to instrument daily work. Covers the OpenTelemetry GenAI semantic conventions with their maturity
stated plainly (**Development, not Stable**, moved to a dedicated repository in June 2026 with no
tagged releases, so nothing to pin against yet), and takes from that standard the rule it would
otherwise have had to argue for: **structured metadata on by default, raw prompt, response and
tool-argument content off by default.** Also names two things this collection had only described:
the drift-detector-moves-with-task-mix problem is a **mix shift**, the mechanism behind Simpson's
paradox; and the fix for silently dead instruments is a **heartbeat or dead man's switch**, alerting
on the absence of an expected signal. Closes with the warning against pointing any of it at
individuals, since agent telemetry makes per-developer attribution trivially easy for the first time.

**New file, `VOCABULARY.md`.** Grades the field's own terms operational, over-claimed, or vacuous.
"Agentic" has no agreed operational boundary and the practice of relabelling automation as agentic
has its own analyst term, **agent washing**. Loop architectures have real numbers from single papers
on single benchmarks with no cross-lab replication. Multi-agent gained two further results pointing
against it, including one where a single agent matched or beat multi-agent on **64% of tasks**, the
latter adding 2.1 percentage points at roughly twice the cost. Memory benchmarks are almost entirely
run by memory vendors. **This file carries weaker sourcing than the rest of the collection and says
so at the top:** the verdicts are judgement, the figures come from one pass and were not each
re-verified to primary sources.

**Deliberately not written: a tool comparison table.** Three candidate tools changed status inside
one quarter of 2026, one archived, one acqui-hired and shut down with its data deleted, one absorbed
and renamed. A product table would have been wrong before publication. The durable version is
capability axes with dated examples, and the research surfaced one axis worth more than any feature
grid: **incident and disclosure history**, since four major agent tools had documented sandbox
escapes via prompt injection during 2026.

## 0.3.0, 2026-09-03

A research pass across three fronts: replications and open gaps, the team and documentation layer,
and evaluation. The point was to move the evidence base rather than to relabel it.

**The ratio, stated honestly, because the previous version's figure is not directly comparable.**
Version 0.2.0 reported roughly 18% external-and-tiered against 52% first-party against 30%
unlabelled, from a hand count of about 125 load-bearing claims. That method cannot be reproduced
exactly, so here is what is mechanically checkable instead:

- **Externally identified papers went from 7 to 19.** Twelve new ones.
- **Peer-reviewed sources went from 1 paper plus 2 CVEs to 6 papers plus 2 CVEs**, the new ones
  accepted at EASE 2026, MSR 2026, ICSME 2026, ICPC 2019, and one ICSE-SEIP 2026 entry recorded for
  its existence only because the text could not be retrieved.
- **Tier 1 went from empty to one entry.**
- **Unlabelled claims are now zero by construction.** Every section of every rule file carries a
  provenance statement, so no claim can sit without one.
- 85 bolded prohibitions across the five rule files.

**The scale itself was wrong, and that is the most important change here.** Tier 1 was implicitly
treated as tier 2 plus a replication. The first tier-1 entry turned out to be two independent
preprints, which the ordering could not express.

> **Replication and review are orthogonal axes.** Tier 1 says independent groups converged. Tier 2
> says reviewers accepted the method. Neither implies the other, and for deciding whether to act,
> convergence is usually more informative.

Tier-1 entries now state their review status explicitly instead of implying one.

**Added, tier 1:** run-to-run nondeterminism, from two independent groups. One found roughly 9% of
per-instance outcomes flipping between byte-identical runs at temperature 0. The other, across
60,000 trajectories and three models, found pass@1 varying 2.2 to 6.0 percentage points run to run
with the spread at temperature 0 comparable to or wider than at 0.7. **Temperature zero does not
make agent evaluation deterministic**, and this discounts every other single-run number in the
collection including its own.

**Added, tier 2, and it fills the collection's weakest section:** two mining studies of
agent-authored pull requests. Most receive no review at all, and where a review agent was the only
reviewer those changes merged at 45.20% against 68.37%, with 12 of 13 agents averaging a
signal-to-noise ratio below 60%. This is the external backing the team layer previously lacked
entirely, and it reaches the same conclusion the first-party self-merge observation reached from one
repository. Also added: AI-contribution policy prevalence across 1,000 repositories, and the
documentation-inconsistency result across 1.3 billion AST-level changes that finally gives the rot
taxonomy an external leg.

**Added, and immediately actionable:** major open-source projects converged during 2026 on an
`Assisted-by:` trailer for AI disclosure while barring AI from `Signed-off-by`. Follow the
convention rather than inventing one.

**A rule was contradicted, which was an explicit goal of this pass.** A study of 2,303 agent context
files across 1,925 repositories found they behave as **living configuration rather than decaying
documentation**. `DOCS.md` treated instruction files as ordinary documents subject to the rot
taxonomy. It no longer claims that, and the taxonomy is narrowed to what it can support: documents
nobody has a reason to open. The contradiction is recorded in the disagreements section rather than
resolved, since 1,925 repositories outweigh five but both observations can be true.

**New profile value, `reviewers: agent`.** A repository where a review agent reviews and no human
reads the diff is now its own state rather than being folded into `one` or `nominal`, because it has
a distinct and measured failure mode. It reads as reviewed on every dashboard and catches closer to
what `none` catches. The Layer 2 solo discipline still applies under it: an agent's comment thread is
not a review record. `PROFILE.md`, `templates/profile.yml` and `SKILL.md` Layer 3 all updated.

**`SECURITY.md` gained the measurement that reframes its own advice.** Across 2,303 agent context
files, security appears in 14.8% of them and performance in 14.5%. So the common state is not a
security rule badly enforced by a model, it is no security rule at all in five files out of six. The
file explicitly declines to conclude that instruction files should carry more security prose, since
moving an unenforceable control does not enforce it, and reframes the absence as a signal about the
repository rather than about the file.

**Two open gaps moved.** Compression on agentic coding workloads has a second independent
measurement and is closed on direction, though which content is safe to drop remains unknown. Code
structure against agent success has its first non-opinion evidence, which happens to support a
practitioner claim already here about data-layer and ORM defects.

**Evaluation harnesses are no longer an acknowledged hole.** New section in `SKILL.md` covering trial
counts under nondeterminism, pass@k against pass^k, building an expert-labelled task set instead of
reusing benchmark tasks, adversarial scenarios, trajectory capture, and model-judge bias measured at
a true positive rate above 96% against a true negative rate below 25%.

**One standing claim was tested and held.** A deliberate search for a controlled comparison of defect
rates with and without AI assistance found nothing meeting random assignment, a genuine defect
outcome, and adequate power. The four near misses each fail a different axis and are named. Search
terms are recorded, and the entry says plainly that this is a "could not confirm" rather than a
"confirmed absent".

## 0.2.0, 2026-09-02

The release that made the collection honest about itself. An audit against the underlying research
found roughly 30% of load-bearing claims carrying neither a tier nor a first-party label, and three
factual errors.

**Corrections, all recorded in `EVIDENCE.md`'s own-errors list:**

- **The agent-skill security figure was wrong in two ways at once.** Reported as prompt injection in
  36% of skills with 1,467 malicious payloads. The study found a security flaw of any kind in 36.8%
  (1,467) of them, with **76** confirmed malicious payloads. A narrow category widened, and a count
  inflated nineteenfold, in the security file.
- **One source was cited as saying the opposite of its finding.** Instruction-file authorship was
  reported as making no difference. The paper found generated files harmful and developer-written
  files mildly beneficial. This produced a new rule: do not let a model write your instruction file.
- **One paper was counted as two.** A result read as an independent rebuttal turned out to be
  internal to the paper it was said to rebut.

All three were paraphrase drift with correct provenance, which the tiering system does not catch.
Added a separate verification pass for it, and the rule that a tier protects a claim's origin and
not its wording.

**Added:**

- **arXiv:2608.18167**, accepted at the ICML 2026 Workshop on Deep Learning for Code, tier 2. Three
  reviewer agents beat five; a reviewer without an explicit disagreement instruction produced the
  worst measured result through false consensus, and adding that instruction produced the best. This
  **closes an open gap the collection had declared sourceless**, having been missed by four research
  passes, so the gap list is now explicitly documented as a record of failed searching rather than of
  nonexistence.
- A section separating **administrative facts from research claims**. Adoption figures and governance
  status have no method to review, so grading them on a review-trail scale understated them. The
  `AGENTS.md` foundation donation is now confirmed against a primary organisational record and
  upgraded from tier 8; the adoption figure stays marked vendor-claimed and the supported-tool list
  is marked non-canonical.
- Two epistemic rules: **a failed verification is not a negative finding**, and **do not trust your
  own paraphrase of a number**. The first came from nearly downgrading the strongest source in the
  collection because one pass could not reach a URL.
- A **provenance table** mapping every section to its evidence kind, replacing the previous situation
  where the weakest-sourced sections were the least obviously so.
- A **maintenance schedule**, a version line, and a recheck date. Previously the collection graded
  everyone else's staleness and carried no cadence of its own.
- `OPERATING.md` **split**: the human-facing guide is now shareable, with machine-specific notes
  moved to a `LOCAL.md` that is excluded from distribution. The whole human half had previously been
  withheld.
- Templates completed: **ADR, pre-push hook, editorconfig**. Three `examples/` profiles for
  repository shapes other than the author's. A `README.md` for people rather than agents.
- An explicit **out-of-scope list**, including evaluation harnesses named as the collection's largest
  acknowledged hole rather than quietly omitted.

**Changed:**

- The opening no longer claims portability as a differentiator. The skill format is itself a
  cross-tool standard now, and all three major vendors publish their own authoring guidance, so that
  ground is taken. The differentiated claim is narrower and stated as such.
- CVE and incident entries now name their vendors. A public disclosure is public record, and "an
  agentic IDE" gives a reader nothing to patch against.
- Re-verified the tier-2 anchor directly against the Crossref registrar record after a second pass
  reported it unconfirmed.

## 0.1.0, 2026-09-01

First assembled version. Eight-tier evidence scale ordered by review trail, the asymmetric-burden
rule, the check-the-artifact habit, three profile-conditional rule layers, the documentation rot
taxonomy, the displacement rule, and the per-repository profile mechanism.
