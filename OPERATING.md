# Operating guide

**Audience: the human, not the agent.** Everything else in this collection tells an agent what to
do. This file is about how you drive it, which is roughly half of where the results come from and is
covered by no rules file anywhere.

Provenance: **mostly `first-party`**, with the failure modes tiered where an external source exists.
The numbers in here that are not cited to a tier are direct measurements of mechanical things like
token counts. Nothing here has been tested against a control.

Keep your own machine-specific notes in a sibling `LOCAL.md` rather than in this file. Tool names,
paths, shell aliases and per-machine quirks go stale fastest and are the least portable thing you
own, so they do not belong in a document you might hand to someone else. There is a template for
that split at the bottom.

---

## The split

| Role | Model tier | Does |
|---|---|---|
| Orchestrator | Frontier | Direction, adjudicating conflicting evidence, reviewing worker claims, deciding what *not* to do, writing the documents others read |
| Worker | Cheaper | Implementation against clear acceptance criteria, mechanical sweeps, verification passes, multi-angle reviews |

Cost reduction of 40-60%, sometimes 5-10x, is the usual reason given. **The stronger reason is
context, not cost.**

**Delegate work whose process is large and whose output is small.** One research sweep consumed
149,539 tokens across 87 tool calls and returned a one-page report. None of that intermediate work
entered the orchestrator's context. That is the win, and it holds even where the worker costs the
same as the orchestrator.

**Do not delegate work whose intermediate results you need in order to decide.** Design questions,
adjudicating two sources that disagree, anything where the reasoning *is* the deliverable. A summary
of reasoning you needed to follow is not a substitute for having followed it.

## Choosing who fills each role

**Role is architecture, vendor is a deployment detail.** Write your setup down in terms of
orchestrator and worker tiers, so swapping a vendor is a configuration change rather than a
rethink. The profile's `tools` field is named for tiers rather than brands for this reason.

**Same vendor.** Cross-session messaging works, both ends read the same instruction files, and the
back-and-forth is cheap enough to be conversational. The default for anything where you expect to
iterate.

**Cross vendor.** Usually cheaper per token, and the directory conventions across major vendors are
structurally parallel, so a shared root instruction file plus a vendor-specific file is a workable
shape. The costs are real: no shared session channel, and two instruction files to keep in sync.
**Use it where the task is self-contained enough to hand over as a written brief**, because you lose
the cheap follow-up question. For small tasks where cost dominates, that trade is usually worth it.

**Cross-vendor review is a genuine advantage and the one reason to accept the friction.** An
independent-context review is stronger when the reviewer does not share the implementer's training
data and failure modes. A single-vendor setup cannot buy that at any price.

**"Vendor" is now two different things and this section used to conflate them.** Added 2026-09-06.
The paragraphs above assume the company you subscribe to is the company that trained the model.
Harnesses that serve another lab's models break that: you can reach a frontier model from one lab
through a subscription sold by another.

Split the question, because the two halves answer differently:

- **Who trained the model** decides whether you get the independent-context benefit. Two harnesses
  serving the same model share its training data and its failure modes, so a review across them is
  **not** independent however different the billing looks.
- **Who sells the harness** decides your cost, your quotas, your instruction-file layout and whether
  a session channel exists between the two ends.

So a setup can be **same-vendor for review purposes and cross-vendor for everything else**, which is
the worst case to be in unknowingly: you pay the friction of two ecosystems and get none of the
review independence you were paying it for.

**Write down which lab trained each model in your setup, not which company you pay.** The profile's
`tools` field records tiers rather than brands, which is right for delegation and does not capture
this. If you rely on cross-vendor review, the thing to record next to it is the training lab.

No measurement supports any of this; it follows from what independent review means. Judgment, not
evidence.

## Failure modes, with what is actually known

- **Orchestrator context accumulation.** Real mechanism, unsourced threshold. The "four or more
  workers" figure in circulation is a practitioner heuristic with no benchmark behind it, so treat
  it as judgment rather than a limit. What you can observe directly is your own session compacting.
- **Sequential work degrades under decomposition.** Measured 39-70% worse on tasks requiring strict
  sequential reasoning, and 17.2x error amplification for independent non-communicating parallel
  agents. Tier 5. So parallelise genuinely independent work, and never split a chain where each step
  depends on the previous step's actual state.
- **More reviewers is not better.** Three reviewer agents outperformed five in the only study
  measuring it. Tier 4: it was tier 2 until 2026-09-07, when its stated acceptance turned out to be
  author-supplied rather than confirmed against a venue. Past a small number they converge rather
  than diverge, so the marginal reviewer buys agreement rather than coverage.
- **A reviewer that is not told to disagree will agree.** Same study: a reviewer agent without an
  explicit disagreement instruction produced the worst measured result in the comparison, and adding
  that instruction produced the best. Isolating the reviewer's context is necessary and not
  sufficient.
- **Shared working tree.** A worker without isolation moves `HEAD`, switches branches and edits
  files underneath the orchestrator. **Use worktree isolation for anything that commits or
  branches.** `first-party`, and observed rather than theorised.
- **Session name drift after a restart.** Peer session identifiers change. Confirm which session you
  are addressing before sending it branch work, especially when more than one peer is listed.
- **A dispatch is not a delivery, and this is the one that cost the most.** `first-party`: work was
  handed to two peer sessions and reported as in progress for **eight hours**. Nothing had happened.
  No branch, no commits, no files. The sessions were listed as alive the entire time. The likely
  mechanism is that a message to a peer is processed on that peer's next turn, and a session sitting
  idle with no human in front of it may never take one.

  Two rules follow, and the second is the general one:

  - **Verify a delegation against the artifact, not against the send.** A branch, a commit, a file
    on disk. "Sent successfully" describes your outbox.
  - **Set a check time when you dispatch.** Not a reminder to chase; a moment at which absence of an
    artifact means the dispatch failed and you re-plan. Without it, "waiting on the worker" is
    indistinguishable from "nothing is happening", and both look identical for as long as you let
    them.

  This is the same failure as a hook configured for a missing binary and a check that passes by
  finding nothing: **an unverified success report from a channel you did not test.** Third instance
  of that shape in one collection, which is enough to call it the dominant one. A
  dispatch to a dead session name reaches nobody and reports no error.

## Before you believe your own results

You will form opinions about which model, which prompt and which setup works better for you. Almost
all of those opinions will be formed from single runs, and single runs do not support them.

Two independent groups measured this, which makes it the only replicated finding in this collection:
outcomes flip between byte-identical runs, and **temperature zero does not make it deterministic**.
One measured roughly 9% of per-instance outcomes flipping. The other, across 60,000 trajectories,
found run-to-run variation of 2.2 to 6.0 percentage points, with a standard deviation above 1.5
percentage points even at temperature 0.

- **Do not switch your setup because one run went badly.** That is inside the noise. So is one run
  going well, which is the more dangerous direction because you will keep the change.
- **Do not compare two models on one task each.** If you actually want the answer, five to ten runs
  per task, and `SKILL.md` has the section on building a small task set worth running them against.
- **Do notice when you are reasoning from a memorable run rather than a count.** The vivid failure
  and the impressive success are both single samples, and they are the ones you will remember.

The practical upshot for daily work is not to run everything ten times. It is to hold your
performance opinions loosely, and to reach for the harness only when a decision actually rides on
the answer.

## Prompting, the human side

- **Inspect before retrying.** A retry without inspection discards what the failed run produced,
  which is usually the most informative artefact available.
- **If two attempts fail, the task is too big.** Narrow it rather than rephrasing it.
- **End runs with a demand for verifiable output.** "Run the check and show me the output" grounds a
  claim in something falsifiable.
- **Never write "you are failing, do better".** Zero instruction content. Say what to do instead.
- **Give the acceptance criteria before the work, not the correction after it.**

### The one habit that actually works

**Replace stake-raising with one falsifiable question: "what did you not verify?"**

"This is important, be thorough" is a positive directive with no measured support, and the largest
study of real rule files found positive directives were the individually harmful ones. What actually
catches errors is specific challenge: *did you do that?*, *have you read that paper?*, *you forgot
that item*. Each is checkable and each lands, which is the whole difference.

### Corollary, learned the hard way

**A confident report is not a verified one.** A worker's report can be accurate while the
orchestrator's summary of it is not, which is a failure with no error message anywhere in it. When a
worker reports, spot-check the one claim that load-bears. Read the artifact, not the report about
the artifact.

## Queue discipline

The largest process failure available to a solo workflow is letting branches accumulate. It is
invisible while it happens and expensive to unwind.

- **One branch in flight.** Merge or close before starting the next.
- **Read `git log --oneline main..<branch>` before merging.** Five seconds, and it catches a
  multi-commit stack that merged looking like a documentation change.
- **Merge a stack bottom-up**, and if a diff contains commits its description does not account for,
  fix the description rather than merging and reconciling afterwards.

## When to stop and write it down

Anything that outlives the current conversation goes into the repository's pending document **in the
same turn it is decided**, not later. Chat is not storage. Everything lost is lost in the gap
between deciding and recording, and that gap is usually one turn wide.

## Your `LOCAL.md`

Keep one, do not distribute it, and put these in it:

- **Where your paths actually resolve.** Skill and agent directories are sometimes symlinked
  elsewhere on a given machine. Check rather than assume, on every new machine, because a symlink is
  exactly the kind of thing that is true here and false there.
- **Your instrumentation, and whether it is actually running.** Any tool that compresses output,
  tracks cost or detects drift needs verifying by running it, not by confirming it is installed. All
  three of those failed silently in one week in the setup this collection came from.
- **Settings your tooling needs to behave.** Task tracking, telemetry and output limits are often
  opt-in and default off, and their absence shows up as dropped work rather than as an error.
- **Which model pairings you actually have access to**, and what each costs you.
