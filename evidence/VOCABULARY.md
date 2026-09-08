# Vocabulary, graded

Load when a term is doing persuasive work in a decision: a proposal, a vendor pitch, an architecture
argument, or your own writing.

The rest of this collection grades **claims**. This file grades **words**, because a word that
sounds like it denotes something measurable will get used as though it does, and a decision built on
one is a decision built on nothing.

Every term gets one of three verdicts:

| Verdict | Means |
|---|---|
| **Operational** | Denotes something specific and testable, with evidence behind it |
| **Over-claimed** | Denotes something real, but the evidence is thin, narrow, or absent |
| **Vacuous** | No operational content. Used for positioning |

**Sourcing status, stated up front because it differs from the rest of this collection.** Compiled
from a research pass on 2026-09-03 and extended on 2026-09-04. The **verdicts** are judgements this
collection stands behind. Most **figures** here were gathered by research passes and have **not**
each been re-verified against a primary source in the way `EVIDENCE.md` entries now have. Treat a
number here as indicative and go to the paper before quoting it at anyone.

**That is a weaker standard than the rest of the collection, it is marked rather than hidden, and it
is the file's known weak point.** If you are going to quote this collection at somebody, quote
`EVIDENCE.md`. Two figures in the tiered sources were found overstated or misattributed on
2026-09-04 when every external claim there was fetched and checked; the same sweep has not been run
across this file.

---

## Agentic, agent, agentic workflow

**Over-claimed, and contested at the definition rather than at the evidence.**

There is a real distinction at the extremes. One vendor's taxonomy separates **workflows**, where
model calls are orchestrated through predefined code paths, from **agents**, where the model
dynamically directs its own process and tool use. That is a genuine difference. It is also a
spectrum label rather than a testable threshold, and nothing tells you where on the spectrum a given
system sits.

A standards body's 2026 agent initiative defines an agent by capability instead: autonomous tool
access, multi-step planning, sub-agent delegation, state persistence. That is a definition built for
regulatory scoping, not for measurement, and it does not help you decide whether a proposal in front
of you is one.

A 2026 critique argues that most systems marketed as agentic derive their competence from
**engineered scaffolding**, fixed loops and predefined tools, rather than from open-world autonomy,
and that the word blurs automation into agency. Independently, an analyst firm found the practice
common enough to name it: **agent washing**, relabelling a script or a chatbot as an agent without
adding planning or autonomy.

- **Do not accept "agentic" as a description of a system.** Ask what the model decides that a
  predefined code path would otherwise decide. If the answer is nothing, it is a workflow, and
  workflows are frequently the better engineering choice.
- **Do not let the word carry an autonomy claim into a security review.** What matters there is the
  permission boundary, not the label.

## Agent loops: ReAct, plan-and-execute, reflection, tree search

**Operational, unevenly, and every number below is one paper on one benchmark.**

These are the terms with real published comparisons attached, which distinguishes them from most of
this file:

- ReAct reported **+34 percentage points absolute** over imitation learning and **+10** over
  reinforcement learning on one embodied benchmark, with one or two in-context examples. Verified.
- Reflexion reported **91% pass@1** on a code benchmark against a **80%** prior state of the art,
  attributed to the self-reflection loop. Verified.
- Tree-of-thought search reported **74% against chain-of-thought's 4%** on one puzzle task, which is
  a dramatic win on a narrow task. On cost, **corrected 2026-09-04**: the widely quoted "100 times
  the compute" is a **third-party estimate from a different paper**, not the original's own figure.
  The original states its method used about **5,500 completion tokens, comparable to roughly 100
  chain-of-thought trials at 6,700 tokens**. So the honest statement is "comparable to about a
  hundred independent attempts", which is the same order and a different claim.
- A no-observation variant reported a substantial token reduction against ReAct on multi-step tasks.

**The caveat is uniform and it matters more than any individual figure.** These are single-paper,
single-benchmark comparisons, not cross-laboratory replications, and at least one of them is
reported to shrink or reverse on harder benchmarks. Compare that to the one genuinely replicated
finding in this collection, where two groups converged, and the difference in confidence is obvious.

**Re-searched 2026-09-04 specifically for cross-lab replication of any loop architecture on coding
tasks. Found none**, recorded as could-not-confirm rather than confirmed-absent.

The planner-plus-parallel-executor comparison often cited as "plan-and-execute" reports **up to 3.7
times latency speedup, up to 6.7 times cost saving, and around 9% accuracy improvement** against a
ReAct baseline. Verified as the paper's own numbers, from an academic group with no commercial stake
in the comparison. **Two notes on how it gets retold:** the paper says "up to", not "typically"; and
it says "~9%", which is not necessarily 9 *percentage points*. **The speed and cost figures are the
ones that get dropped in retelling**, and they are the ones that decide whether you can afford it.

- **Do not cite one benchmark win as general superiority of a loop architecture.**
- **Do not adopt tree search without pricing it.** A 10 to 100 times token multiplier is a
  different product, not a tuning parameter.

## Multi-agent, orchestrator-worker, swarm

**Over-claimed, and the evidence points against the default assumption.**

This collection already holds tier-5 evidence that multi-agent decomposition degrades
sequential-reasoning tasks by 39 to 70% and that non-communicating parallel agents amplify errors
17.2 times, plus evidence that three reviewer agents beat five.

> **A statistic was removed from this section on 2026-09-04 because it appears to be fabricated.**
> An earlier version reported "a single agent matched or beat multi-agent on 64% of benchmarked
> tasks, with multi-agent adding 2.1 percentage points at roughly twice the cost", attributed to
> Princeton. A verification pass traced that wording to **a search-optimised blog post naming no
> paper, author or identifier**, then fetched the one genuinely related paper in full and found
> **none of those numbers in it**. See error 14. It is recorded as *could not source* rather than
> *confirmed false*, and it is gone from the argument.

**The two real papers, which support the same direction and are better than the invention:**

- **arXiv:2604.02460**, Tran & Kiela (Stanford). Title states the finding: single-agent systems
  outperform multi-agent systems on multi-hop reasoning **under equal thinking-token budgets**. The
  paper reports that single-agent setups "consistently match or outperform" multi-agent ones and
  **gives no single summary percentage**, which is why the invented figure was attractive and why
  its absence matters.
- **arXiv:2606.13003**, Jwalapuram et al. (Salesforce AI Research, NTU, UBC, HKUST), June 2026.
  Across reasoning datasets, interactive multi-step workflows including BrowseComp-Plus, and a
  purpose-built diagnostic set: **automatically-generated multi-agent systems consistently
  underperform chain-of-thought self-consistency while costing up to 10 times more.** Note the
  multiplier is **10x, not the 2x** in the removed figure, and note the nuance the invention lacked:
  **expert-architected multi-agent systems do outperform automatically-generated ones.** So the
  failure being measured is partly automation of the architecture, not the architecture itself.

**Not uniformly negative.** A 2026 clinical-workload paper reports orchestrated multi-agent setups
sustaining accuracy better than single agents under high load. So the honest position is
task-dependent rather than dismissive.

**A deliberate hunt for the strongest pro-multi-agent evidence, 2026-09-04, and what it found is
worth stating precisely.** The search was framed to disconfirm this collection's own position, and:

- **On accuracy, it found nothing.** No 2026 result was located showing multi-agent beating a single
  agent on accuracy **under matched compute or cost** on software tasks. That is a
  **could-not-confirm, not a confirmed-absent**, and it should be read as a gap in the search rather
  than a closed case.
- **On cost, there is a real result and it is a different claim.** Orchestrator-worker routing, where
  a capable orchestrator hands subtasks to cheaper specialist models, is reported to cut cost
  substantially. Vendor-sourced and unconfirmed independently, but it is the shape this collection
  already recommends in `OPERATING.md`, and note what it claims: **cheaper for the same outcome, not
  better.**
- **And the mechanism behind the negative results got sharper.** A 2026 paper argues that reported
  multi-agent gains are largely **uncontrolled inference-budget artifacts**: the multi-agent system
  simply spent more tokens. That is a better explanation than "coordination overhead", because it
  predicts the gain disappears under matched budget, which is exactly what the comparisons that
  control for budget find.

So the honest verdict splits by claim: **marketing for accuracy, operational for cost routing.**

- **Do not add agents to a problem that is one chain of dependent steps.** That is the measured
  worst case.
- **Do delegate work whose process is large and whose output is small.** That is a context argument
  rather than an accuracy argument, and it is the one that survives.

## Context engineering

**Over-claimed, but the distinction is real.**

Popularised in 2025 and widely adopted since. The scope distinction it draws is legitimate: a prompt
is the instruction, while context is everything the model can see, including memory, tool results,
retrieved data and accumulated state. That is a genuinely larger surface than prompt wording and it
deserves a name.

What it does not have is evidence. **No controlled study was found comparing context-engineering
practice against plain prompt engineering on outcome metrics.** That is a *could not confirm* rather
than a *confirmed absent*, but it means the term currently names a methodology supported by anecdote.

Worth noting that this collection's own strongest actionable finding, context beating procedure, is
evidence for the underlying idea even though it predates the label.

## Memory, persistent memory, knowledge graphs for agents

**Operational, with a conflict-of-interest problem that is worse than "vendor-adjacent".**

Verified 2026-09-04, and the conflict is concrete: **in both leading cases the paper's authors
include the product's own founders or team.** These are not third-party evaluations with a vendor
sponsor. They are the vendor running the benchmark on itself.

- One product reports roughly **66.9%** on a long-conversation benchmark, and about **68.4%** for its
  graph-augmented variant. Confirmed only **through convergent secondary citation** rather than a
  direct read of the paper's own table, which is a weaker verification than the rest of this
  collection uses.
- A second product's widely quoted **63.8%** is **corrected here**: that is its **overall** score on
  a long-memory benchmark, **not a temporal-reasoning subtask score** as this file previously implied.
  The same paper's own breakdown puts its temporal-reasoning score at **54.1%** on one model and
  **62.4%** on another, both below the headline.

- **Do not compare memory products on vendor-published benchmark numbers.** They select the
  benchmark, the configuration, and the baselines.
- **Do not quote a headline score as a subtask score.** That is the specific error corrected above,
  and it flattered the product by several points on exactly the capability being discussed.

## Skills, tools, MCP, function calling

**Operational, and three of the four are the same mechanism at different layers.**

- **Function calling** is the base mechanism: the model emits a structured call.
- **MCP** is a transport and interoperability standard for connecting that mechanism to external
  systems. Genuinely cross-vendor, and now under neutral foundation governance.
- **Skills** are packaged instructions and context. **Not a new invocation mechanism.** An MCP
  server can expose a skill as a tool, which tells you they are not competing categories.

- **Do not treat "supports MCP" as a capability claim.** It is a connector standard. What matters is
  what the connected thing can do and what permissions it holds.
- **Do not argue about skills versus MCP as though choosing one.** They sit at different layers.

## Autonomy levels

**Over-claimed. Attempted, not achieved.**

Several proposals exist for driving-automation-style levels, including at least one attempting
measurement by code inspection. **None has convergent adoption** comparable to the driving standard
it imitates. So a claim that a system is "level 3 autonomous" is a claim in a private vocabulary.

- **Do not use a level number in a contract, a policy or a security review** without attaching the
  specific scheme and its definitions.

## Evals, guardrails, observability, tracing

**Operational, and the most mature and least contested category in this file.**

Real tooling, real practice, and a useful distinction inside it: **guardrails** are runtime blocking
and approval controls, while **observability and tracing** are evidentiary logging that feeds
regression evaluation. One prevents, the other explains.

**One scope correction, 2026-09-04.** The judge-concordance figures this collection cites, a range of
**0.66 to 0.96 with a median of 0.83 across 13 studies**, and a **three-judge rubric-anchored
ensemble reaching 0.90**, come from a scoping review whose **13 underlying studies are all clinical
evaluation tasks**. This collection presented them as a general finding about model judges. They are
domain-specific, and code review is not the domain they were measured in. The direction is still the
best signal available; the numbers should not be quoted as general.

See the measurement section in `SKILL.md`. This is the part of the vocabulary where the words track
something you can actually build.

## RAG, agentic RAG, deep research

**RAG operational, the agentic layer over-claimed.**

Retrieval augmentation is well established. The agentic variants, query rewriting, multi-hop
retrieval, planner-driven retrieval, have evaluation *frameworks* but the survey literature itself
lists evaluation as an open research problem rather than a solved one. So the frameworks exist and
the answers do not.

## Long-horizon autonomy, and the reliability wall

**Operational, and the most useful number in this file for planning purposes.** Added 2026-09-04.

An ongoing measurement programme tracks the **length of task an agent can complete at 50%
reliability**. Figures below verified against the programme's own publications on 2026-09-04, and
**two of them corrected in the process**:

- **The headline trend: doubling roughly every seven months** across 2019 to 2025, about 196 to 212
  days. Confirmed as the programme's own finding.
- **The much shorter doubling figure, around 89 days, is the programme's own number, not a tracker
  extrapolation.** Corrected: an earlier version of this file dismissed it as third-party. It is the
  **post-2024 subset** doubling time from a methodology update, distinct from the all-time trend,
  which that same update leaves essentially unchanged. So both figures are real and they measure
  different windows.
- **The current horizon is at least 16 hours, not 14.** Corrected. The most recent public evaluation
  puts the frontier at a 50%-time-horizon of **at least 16 hours with a confidence interval running
  from roughly 8.5 to 55 hours**, and the programme states measurements above 16 hours are
  **unreliable with its current task suite**. An earlier intermediate 2026 figure was around 12
  hours with an interval of 5 to 61.

**And the caveat that matters more than any of the numbers: 50% reliability is not an operating
point.** A task that succeeds half the time needs a human at the end of it. "16 hours" is not "leave
it running overnight", it is the length at which a coin flip decides the outcome. The confidence
intervals are also enormous, which is the honest signal that this is an early measurement rather
than a curve to plan against.

**The practical reading: a reliability wall exists well short of full-day autonomy as of September
2026.** That is a bound on planning, not a prediction about next year, and it is the honest answer
to "can I just let it run".

## Two 2026 terms that are about the vocabulary itself

- **Agent washing.** An analyst term for relabelling existing automation as agentic without adding
  planning or autonomy. Useful precisely because it is diagnostic: if you cannot say what the model
  decides, this is the word for what you are looking at.
- **Vibe coding.** Coined in a specific and narrower sense than it is now used. The widely repeated
  claim about its share of enterprise code is **vendor-sourced and unverifiable**, and it is the kind
  of figure this collection exists to hold at arm's length.

---

## How to use this file in an argument

The point is not to be dismissive. Several of these terms name real things, and two of them,
function calling and retrieval, name things that plainly work.

The point is that **the word and the evidence travel separately**, and the words travel faster. When
a term is doing persuasive work in a decision, three questions settle it:

1. **What would it look like if this were false?** A term that cannot fail is positioning.
2. **Who measured it, and on what?** One benchmark in one paper is a result, not a property.
3. **Who benefits from the number?** Vendor-run benchmarks of vendor products are tier 5, however
   sophisticated the methodology looks.
