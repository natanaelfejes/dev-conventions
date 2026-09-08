# Observability and instrumentation

Load when deciding what to record about agent work, when a workflow's cost or behaviour needs
explaining, or when an instrument's readings are about to be used as evidence.

**This is not the evaluation section.** They answer different questions and get confused constantly:

| | Question | Cadence |
|---|---|---|
| **Evaluation** | Did this change help? | Point in time, deliberate, on a task set you built |
| **Observability** | What is actually happening, what does it cost, where does it fail? | Continuous, passive, on real work |

Evaluation is in `SKILL.md`. An eval suite tells you nothing about the session that went sideways
yesterday, and a dashboard tells you nothing about whether your new prompt is better. You need both,
and neither substitutes.

---

## Instrument to a standard, not to a product

The vendors in this space churn faster than the practices do. A standard outlives them, so record
against the standard and treat the storage and dashboard layer as replaceable.

**OpenTelemetry has GenAI semantic conventions**, and they are the closest thing to a durable
vendor-neutral answer. They define a span hierarchy that matches how agent work actually nests: a
top-level agent-invocation span, child spans per model call, and separate spans per tool execution.
Attributes cover the model requested, input and output token counts, finish reasons, and the
operation type.

**State their maturity honestly, because it is not settled.** As of the last check on 2026-09-03
these conventions are at **Development status, not Stable**. In June 2026 they were deprecated out
of the core semantic-conventions repository into a dedicated one, which **had no tagged releases** at
last look, so **there is no versioned schema URL to pin against yet.** Adoption is nonetheless real:
several major coding-agent products emit them, and at least one large observability vendor supports
them natively.

- **Do not build a proprietary trace schema when the standard covers your case.** Emitting standard
  attributes costs the same and survives a change of backend.
- **Do not pin to a schema version that does not exist yet.** Record which conventions you followed
  and the date, because this is a moving target and a future reader needs to know which shape your
  data is in.

## What to record, and what to leave off

**The default that matters, and it is the standard's own.** OpenTelemetry's GenAI instrumentation
**defaults message content to off.** Capturing prompts and responses requires an explicit opt-in, and
even then the content is carried as separate events correlated by trace and span id rather than
being embedded in the primary span.

That is a standards-body-endorsed version of a rule this collection would otherwise have to argue
for from first principles:

> **Structured metadata on by default. Raw prompt, response and tool-argument content off by
> default.**

The reason is concrete rather than abstract. Prompts and tool arguments in a coding workflow
routinely contain credentials, customer identifiers, and proprietary source. A trace store is
usually less protected than the systems the data came from, is retained longer than anyone intends,
and is readable by everyone with dashboard access.

**Record by default:**

- Tool or operation name, and the model actually used rather than the one requested.
- Caller identity, as a pseudonymous id rather than a name or email.
- Duration, input and output token counts, and cost.
- Outcome and error class. Not the error text, which frequently contains the same data as the
  arguments.
- A correlation id, threaded from the request, that is **findable in the log from what the caller was
  shown**. If it is not, it is decoration.
- The trajectory shape: which tools fired in which order, and how many rounds.

**Off by default, opt-in per investigation, with a retention limit:** prompts, responses, tool
arguments, retrieved documents, and diffs.

- **Do not log tool arguments by default.** In this collection's own first-party observations, tool
  arguments carried product serial numbers and barcodes, and a debug capture written ahead of the
  auth middleware recorded unauthenticated request bodies to an unrotated file. That is a credential
  log by another name. See `SECURITY.md`.
- **Do not let a debug capture outlive its investigation.** Turn it on with an end date.

## The layers, described as layers

Products move; the layering has been stable.

- **Collection and transport.** An OpenTelemetry collector. Vendor-neutral, and the right place to
  put redaction, because a redaction processor there protects every backend at once.
- **Storage and dashboards, generic.** Prometheus and Grafana, or the equivalent. Worth knowing that
  **this layer is no longer purely generic**: Grafana Cloud now ships first-party GenAI dashboards
  covering model observability, evaluations, vector-database and connector-protocol monitoring, all
  ingesting the same standard data. So "generic stack" no longer means "build the dashboards
  yourself".
- **The model-native platforms**, several of which are genuinely open source and self-hostable under
  permissive licences. What they add over the generic stack is **evaluation, prompt versioning,
  dataset management, and the link from a trace to an eval case.** Trace collection itself is
  converging on the standard.

**An honest gap:** every comparison of these platforms found in this pass was written by one of the
vendors or an adjacent party. **No independent adjudication exists** of whether the model-native
layer is necessary or a convenience over the generic one. The observation that the most
standards-native of them builds on the standard rather than a proprietary schema suggests the
additive part is the evaluation layer rather than the tracing, but that is inference, not a finding.

## Four failure modes, three of which have proper names

### The instrument that silently stopped

**First-party, twice, in one collection.** An output-compression hook was configured for a binary
not on `PATH`, failed silently on every call, and saved nothing for a whole session. A link checker
reported a document set clean while having extracted **zero** references to check.

Both reported success. Neither was working. **The named practice for this is a heartbeat, or dead
man's switch**: alert on the *absence* of an expected signal rather than on a bad one. The silent
outage is the dangerous one precisely because no alert fires when no data arrives.

- **Do not trust an instrument that has never reported a problem.** Make it fail once, deliberately.
- **Do not monitor only the thing. Monitor that the monitoring is alive.** An expected heartbeat that
  stops is an alert; a dashboard that goes quiet is not.
- **Do report what was examined, not that nothing was wrong.** "17 references checked, all resolve"
  is a result. "No errors" is compatible with having checked nothing.

### The metric that moves with your workload, not your quality

**First-party**: a drift-detection tool whose readings shift with **task mix**, so a
documentation-heavy week reads as a model regression when nothing about the model changed.

**This has a name and a literature, and it is not an AI problem.** It is a mix shift, the mechanism
behind Simpson's paradox: the relative sizes of your segments changed between periods, the segments
have different baseline rates, and the aggregate moves without any segment moving. Decades old,
well-studied, and it invalidates a great many confident before-and-after comparisons.

- **Do not compare an aggregate across periods when the work mix changed.** Segment first, then
  compare within segments.
- **Do not read a drift detector as evidence about a model** unless it controls for task mix. Read it
  as an audit of your workflow instead.

### Dashboards nobody reads

Alert fatigue is a real, peer-reviewed phenomenon in security and reliability operations, with a
reported finding that **attention drops around 30% for each repeat of the same alert.** No
equivalent study specific to model observability was found, so this transfers by analogy rather than
by evidence. The analogy is strong enough to act on and weak enough to say so.

- **Do not add a panel you have no decision for.** Every metric should have a stated action for when
  it moves.

### Measuring people

**Do not point any of this at individuals.** The best-documented critique in software measurement:
when commit counts are tracked, developers make more and smaller commits; when ticket counts are
tracked, tickets get split. The numbers improve and the work does not. The authors of the
best-known delivery metrics say plainly that they are for informing improvement rather than serving
as performance targets, and should never be used in isolation or to rank individuals.

This bites harder here than elsewhere, because agent telemetry makes per-developer attribution
trivially easy for the first time. Ease is not licence.

## Cost, which is the metric people actually want

Cost is the one number that is unambiguous, cheap to collect, and immediately actionable, and it is
the instrument for any claim that a change saved anything.

Published figures exist for enterprise coding-agent spend per developer per active day, and
per-task costs in the range of a few cents to low tens of cents on public benchmarks. **All of it is
vendor or vendor-adjacent, and no academic cost-attribution methodology was found.** So use the
shape of those numbers to sanity-check your own and never as a benchmark to hit.

- **Do not claim a change saved tokens without an instrument that measures tokens.** This collection
  has a first-party case where a compression tool was assumed to be saving and was saving nothing.
- **Do track cost per developer across the whole stack rather than per tool.** Per-tool figures move
  when work moves between tools and tell you nothing.
- **Do not optimise cost before you have a correctness signal.** A cheaper workflow that is worse is
  not a saving, and the nondeterminism finding in `EVIDENCE.md` means you will need several runs to
  know which you have.
