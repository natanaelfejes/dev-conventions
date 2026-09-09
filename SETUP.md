# Deciding your stack once, so no repository re-decides it

**Run this once, not per repository.** It produces a file you own, `~/.agents/setup.yml`, which every
repository profile then points at. Adoption in repository number seven becomes a reference rather
than a decision.

**This is the friction fix, and it is worth being precise about which friction.** There are two, and
they need different answers:

- **"What is the best tool for X?"** No artifact can answer this durably. Anything named here rots in
  a quarter, and a study of published agent skills found a security flaw in **36.8%** of them, so a
  recommendation list would contradict `SECURITY.md` sitting next to it. This collection permanently
  refuses that, and `TOOLING.md` maps the categories instead.
- **"Which tool did I already decide on, why, and when did I last check it?"** This is answerable,
  it is the friction that actually recurs, and nobody was answering it. **That is what this file
  fixes.** You decide once, you record the decision and its date, and every subsequent repository
  inherits it.

**No outcome claim.** Nothing here has been measured. The argument is arithmetic: deciding once and
recording the decision costs less than deciding again in every repository, and a recorded decision
can be reviewed, whereas a remembered one cannot.

---

## 1. Fill one row per category, and leave rows empty on purpose

`TOOLING.md` has the nine categories and the argument for which ones matter at your scale.
The short version, from that file: **a solo developer genuinely needs permission gating, sandboxing,
secret scanning, and supply-chain scanning for anything third-party.** Everything on that list
constrains the agent. The team list observes it, and observation mostly does not scale down, because
you are already watching.

```yaml
# ~/.agents/setup.yml
# Decisions, not recommendations. Yours, dated, and reviewed on a cadence.
version: 1
reviewed: 2026-09-08          # the date you last opened this file and meant it

categories:
  permission_gating:   { tool: "", decided: "", note: "" }
  sandboxing:          { tool: "", decided: "", note: "" }
  secret_scanning:     { tool: "", decided: "", note: "" }
  supply_chain:        { tool: "", decided: "", note: "" }
  cost_accounting:     { tool: "", decided: "", note: "" }
  observability:       { tool: null, decided: "", note: "not needed at this scale" }
  eval_harness:        { tool: null, decided: "", note: "" }
  context_management:  { tool: "", decided: "", note: "" }
  static_analysis:     { tool: "per-repo", decided: "", note: "see each profile's stack.check" }
```

**A `null` with a reason is a filled row, not an empty one.** It records that you considered the
category and declined it, which is the difference between a decision and an oversight. This
collection has a recorded error about exactly that distinction.

**Do not copy someone else's file.** The categories are portable. The answers are not: they depend on
what you are allowed to install, what your employer forbids, and what you will actually maintain.

## 2. Record what you have installed, and when you vetted it

Every skill, plugin and MCP server you install runs with your filesystem, your credentials and
usually your shell. `SECURITY.md` has the five facts to establish before granting that. **The point
of writing them down is that you do not repeat the vetting, and that a stale vetting is visible.**

```yaml
installed:
  - name: ""
    kind: skill              # skill | plugin | mcp-server | hook
    source: ""               # where it came from, exactly
    vetted: 2026-09-08       # when you last established the five facts
    permissions: ""          # what it can actually reach
    why: ""                  # the one thing it does that you needed
```

- **Do not install anything without a row here.** An unrecorded install is one nobody will ever
  re-vet, because nobody knows it is there.
- **Re-vet on the same clock as `SECURITY.md`**, which is faster than quarterly. Governance moves,
  maintainers change, and a tool that was safe when you installed it is a claim with a date on it.
- **A row whose `why` you cannot fill is an uninstall.** If you cannot name the one thing it does
  that you needed, you are carrying its permissions for nothing.

## 3. Write the delegation policy down once

`OPERATING.md` has the reasoning. This is the part you stop re-deriving:

```yaml
delegation:
  orchestrator_lab: ""       # which lab TRAINED the model, not who bills you
  worker_lab: ""             # if these match, cross-vendor review buys you nothing
  worker_count: 2            # and see the note below
  delegate:                  # work whose process is large and output is small
    - research sweeps
    - verification passes
    - mechanical fixes across many files
  never_delegate:            # work where the reasoning IS the deliverable
    - design decisions
    - adjudicating two sources that disagree
    - anything you need the intermediate results of in order to decide
  check_time: ""             # when absence of an artifact means the dispatch failed
```

Three things to get right, and they are the ones most often got wrong:

- **`orchestrator_lab` and `worker_lab` record who trained the model, not who you pay.** Two
  harnesses serving the same lab's model share its training data and its failure modes, so a review
  across them is **not independent** however different the billing looks. This is the single most
  expensive thing to get wrong, because you pay the friction of two ecosystems and get none of the
  review independence you were paying for.
- **`worker_count` is not a dial to turn up.** Three reviewer agents outperformed five in the only
  study measuring it, tier 2. Past a small number they converge rather than diverge, so the marginal
  worker buys agreement rather than coverage. The "four or more workers overflows the orchestrator"
  figure in circulation is **tier 8, unverifiable**, so treat your own compaction as the signal.
- **`check_time` exists because a dispatch is not a delivery.** First-party, and it cost eight hours:
  work was handed to two peer sessions and reported as in progress the entire time. Nothing had
  happened. **Verify a delegation against the artifact, a branch or a commit or a file, never against
  the send.**

## 4. Point each repository at it

In `.agents/profile.yml`:

```yaml
setup: ~/.agents/setup.yml   # resolved stack, installs and delegation policy
```

The per-repository profile keeps what is genuinely per-repository: `stack.check`, `stack.test`,
the documentation slots, `team`, `reviewers`, `maturity`, `secrets`. **It does not repeat your tool
choices**, because those do not vary by repository and a value repeated in seven places is a value
that will be wrong in at least one of them.

## 4b. Two machines, and the file will drift between them

**Added 2026-09-09 because this file said "per machine" and then said nothing about the second
machine.** Anyone with a work computer and a personal one has two of these, they diverge silently,
and the divergence is invisible until an agent applies the wrong policy. `HANDOFF.md` carries this
exact rule one level down: **a record only one harness can read fails at the moment you switch
harnesses.** The same is true of machines.

**Split the file by what actually varies, because "sync it" and "keep it local" are both wrong.**

```yaml
machine: work-pc            # REQUIRED. Name the machine in the file.
setup_base: ~/dev/agents-setup/base.yml   # synced, one source of truth
```

- **Synced, in a private repository:** the **delegation policy**, the **category decisions and their
  reasons**, and the **vetting records** with their dates. None of these vary by machine. A tool you
  vetted on Tuesday is vetted, wherever you are sitting.
- **Local, in `~/.agents/setup.yml`:** what is **actually installed here**, and anything **your
  employer forbids here**. These genuinely differ, and pretending otherwise is how a work machine
  ends up configured from a personal policy.

**The `machine:` field is the part that does the work.** Without it, a stale file copied from the
other machine is indistinguishable from a current one, which is the same failure as an undated
claim. An agent reading a `setup.yml` whose `machine:` does not match the host it is running on
should say so and stop rather than apply it.

**If you will not maintain two files, keep one and accept the cost explicitly:** put the union in the
synced file, mark every row that is machine-specific, and never let the work machine's restrictions
silently become the personal machine's defaults.

## 5. Review it on a cadence, and make the cadence visible

Put the review date in the file, as above. Two things make it stale:

- **A vetting older than a quarter**, on anything holding credentials.
- **A category you declined that has since started mattering**, most often observability once a
  second person joins, and an eval harness once you start sharing agent configuration rather than
  each keeping your own.

**A setup file nobody reviews is worse than none**, for the same reason a year-old security document
is worse than an absent one: it reads as current.

---

## What this does not do

**It does not tell you what to install.** It records what you chose and makes the choice reviewable.
If you want a recommendation, the honest answer is that no durable one exists, and the closest thing
to one is `TOOLING.md`'s judgment about which categories are worth filling at your scale,
which is explicitly labelled as judgment rather than evidence.

**It does not make your stack good.** It makes it explicit, dated and portable, which is the
precondition for noticing that it is not.
