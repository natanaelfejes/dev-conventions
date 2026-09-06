# The tooling around an agent

Load when deciding what to put around a coding agent, or when you suspect you are missing a whole
category of tooling rather than the best product in a category.

**This is a map, not a ranking.** Mapped 2026-09-04.

## Why this is a map and why that distinction is the whole file

There are two different questions and only one of them is answerable:

- **"Am I missing a category?"** Answerable, stable, and worth writing down. Categories change on a
  scale of years.
- **"Which product is best?"** Not answerable here. A deliberate search found **no independent,
  methodologically rigorous head-to-head** of these tools on real engineering tasks. What exists is
  vendor content, leaderboards with known contamination problems, and comparison sites with
  undisclosed incentives.

So every product named below is an **illustration of a category, not an endorsement**, carries its
licence so you can judge the commitment, and is dated. Three prominent agent tools changed status in
a single quarter of 2026, one archived, one acquired and shut down with user data deleted, one
absorbed and renamed. **Anything in here could be gone by the time you read it. The categories
will not be.**

For choosing between products in a category, `SECURITY.md` has the five facts to establish before
granting a tool access to your filesystem. That is the durable version of "which one".

---

## The categories

### 1. Permission and policy gating

**Necessary at any scale, including solo. And it is the most-skipped category on this page.**

Distinct from sandboxing, and the distinction matters: sandboxing limits **what damage a call can
do**, policy gating decides **whether the call happens at all**. Approval prompts, allowlists,
hooks that intercept a tool call, human-in-the-loop gates, general policy engines.

This is the difference between an agent that asks before a destructive command and one that does
not. It is skipped because most harnesses ship a default and the default is invisible.

- **Do not accept the default without reading it.** See `SECURITY.md`: whether the posture fails
  open or closed, and whether it lives in versioned text you can review or in UI state nobody can
  audit, is the single biggest determinant of blast radius.
- **Do not rely on a command allowlist as a boundary.** CVE-2026-22708 is the counter-example:
  shell built-ins bypassed the allowlist, poisoned the environment, and a later *allowlisted*
  command carried the payload. The command name was never what mattered.

### 2. Sandboxing and execution isolation

**Necessary as soon as an agent runs shell commands or untrusted code. Any scale.**

Layers, from primitive to managed: microVM and syscall-interception primitives (Firecracker, gVisor,
both open source), embeddable sandbox runtimes (E2B, Apache-2.0 core with a hosted option),
managed platforms (Daytona open-core, Modal proprietary).

- **Do not assume the sandbox holds.** Four major agent tools had documented sandbox escapes via
  prompt injection during 2026. Keep credentials narrow and network egress narrow *anyway*, so an
  escape costs you less.
- **Do not confuse a worktree with a sandbox.** A git worktree isolates *file state* between
  concurrent agents. It does not restrict what a command can reach. You often want both.

### 3. Secret scanning and pre-commit safety

**Necessary at any scale, and the reason is specific to agents rather than general hygiene.**

Examples: gitleaks (MIT), trufflehog (AGPL core with a commercial hosted option), detect-secrets
(Apache-2.0).

The agent-specific argument: **an agent writes credentials into files more readily than a human
does.** It has no embarrassment reflex, it is optimising for a working configuration, and pasting a
real value is the shortest path to one. `SECURITY.md` records a first-party case where an
undocumented secret destination meant chat became the destination; the same pressure applies to
source files.

- **Do not verify "no credentials in source" against the ignore file.** Verify against full history.
  `git log -- <path>` is the only output that is evidence.
- **Do not install a scanner and skip testing it.** Commit a fake credential to a scratch branch and
  confirm the scanner fires. A scanner that never fires is indistinguishable from a clean repository,
  and this collection has three recorded instances of exactly that class of failure.

### 4. Supply-chain scanning for skills and MCP servers

**A genuinely new category in 2026, and necessary as soon as you install anything third-party.**
Not team-only.

Examples: `mcp-scan` (Invariant Labs, configuration and prompt-injection checks), `mcp-scanner`
(Cisco, Apache-2.0, YARA plus model-based detection, self-hostable), and commercial agent-scanning
products that cover MCP servers, tools and skills for prompt injection, tool poisoning and tool
shadowing.

Why it earns a category of its own: a vendor study found **36.8%, or 1,467 of the agent skills
surveyed, carrying at least one security flaw**, with 76 confirmed malicious payloads. A separate
figure circulating in early 2026 put the number of **unauthenticated public MCP servers in the
thousands**; that one is secondhand and **unconfirmed**, so treat the direction rather than the
number.

- **Do not install a skill or MCP server without reading what it executes.** The scanners help and
  they are not a substitute for reading.
- **Do not assume a scanned artifact stays scanned.** Skills and servers change between installs.
  Re-check on update.

### 5. Observability and tracing for agent runs

**Necessary once agents run unattended or on a team. Genuinely optional solo**, where your own
terminal scrollback is a serviceable trace.

Examples, all with self-hostable open-source options: Langfuse (MIT), Arize Phoenix (Apache-2.0,
built on OpenTelemetry), Helicone (Apache-2.0, proxy-based, cost-focused). Proprietary and
eval-focused: Braintrust, LangSmith.

**The durable part is the wire format, not the product.** The OpenTelemetry GenAI semantic
conventions are emerging as the vendor-neutral substrate underneath most of these, which means the
backend is replaceable if you instrument to the standard. `OBSERVABILITY.md` covers what to record,
what to leave off by default, and the four failure modes, including the two with proper names.

### 6. Evaluation harnesses

**Necessary once you have an agent configuration you intend to reuse or tune. Not needed for one-off
work.**

Examples: Inspect AI (UK AI Safety Institute, MIT), DeepEval and Promptfoo (permissive), plus
evaluation features inside several observability platforms.

`SKILL.md`'s measurement section is the method: build a small expert-labelled task set from your own
repository rather than reusing a public benchmark's tasks, and run each candidate five to ten times,
because the only replicated finding in this collection is that single runs are noise.

### 7. Cost and token accounting

**Team-relevant, mostly optional solo** unless spend is itself the constraint.

Increasingly bundled into observability tooling rather than standing alone. The one rule worth
stating: **do not claim a change saved tokens without an instrument that measures tokens.** This
collection has a first-party case where a compression tool was assumed to be saving and was saving
nothing, silently, for a whole session.

### 8. Context and compaction management

**Mostly not a separate product category yet.** In practice this lives inside the harness: its own
compaction, its own summarisation, its own checkpointing.

Worth knowing that the underlying question is measured rather than settled. Summarisation beats
simple truncation **only under severe compression**, not uniformly; and a model deciding its own
compaction timing matched or beat threshold-based compaction at much lower token cost. Both are
single papers.

- **Do not buy a compression tool to solve a context problem you have not measured.** Check whether
  the harness you already run does it, and whether the loss is real for your workload.

### 9. Static analysis and linters

**Necessary at any scale, and unchanged by AI except in one respect that matters a lot.**

Not a new category, and existing tools serve fine. What changed: **agents consume linter output as
loop feedback.** A fast, precise linter is now an input to the agent's own correction cycle rather
than only a gate at the end.

That is the strongest practical argument for the rule in `SKILL.md` about moving enforceable rules
out of prose and into config: a linter rule teaches the agent every iteration, while the same rule
written in an instruction file costs context on every turn and is followed inconsistently.

---

## What you actually need

Opinionated, and **not benchmarked**. This is judgment.

**Solo developer, genuinely needed:** permission gating, sandboxing, secret scanning, and
supply-chain scanning if you install anything third-party. All four are about limiting damage rather
than improving output, which is why they get skipped and why skipping them is the expensive choice.

**Team, add:** observability and tracing, cost accounting, and a real evaluation harness once you
share agent configurations rather than each keeping your own.

**Optional at any scale:** dedicated compression tooling, and elaborate multi-tool observability
stacks where one log file would do.

**The pattern worth noticing:** everything in the "needed solo" list constrains the agent, and
everything in the "team" list observes it. Constraint scales down to one person. Observation mostly
does not, because you are already watching.
