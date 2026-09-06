# ADR-NNN: short imperative title

Date: YYYY-MM-DD
Status: Proposed

<!--
Filename: NNN-kebab-case-title.md, zero-padded. The number and the title both
belong in the filename, because a directory listing is how anyone finds these
and a bare number tells them nothing.

Status is for the decision lifecycle ONLY: Proposed, Accepted, Superseded,
Deprecated. Never put implementation state here. "Accepted, partially built" is
two facts wearing one label, and the second one belongs in the pending document.

The Date line is mandatory. An undated decision record cannot be reasoned about
at all: you cannot tell whether it predates the constraint that would have
changed it.
-->

## Context

What was true when this was decided. Constraints, deadlines, what was and was not
known yet. Write it so a reader who arrives two years later does not need you.

Say what you did not know. A record that reads as though the decision were obvious
is the one that gets overturned by someone who thinks you missed something.

## Decision

What was decided, in the active voice, one paragraph.

## Reconsider if

<!--
The highest-value section here and the one most records omit. Write it while the
decision is still cheap.

The failure it prevents, observed rather than hypothesised: a team was advised
against an architecture, agreed the advice was sound, and continued anyway
because reversing had become expensive. They recorded that reasoning in their
own meeting log. After months of work a decision defends itself, and the
argument against changing is the cost of changing rather than the merits.

A trigger written on day three costs one sentence. Make it observable: a number
crossed, a dependency shipped, a date reached, a licence changed. "If it becomes
a problem" is not a trigger.
-->

- Condition, stated so somebody could notice it without being told to look.

## Consequences

What this makes easier and what it makes harder. Include the costs you accepted
knowingly, because a record listing only benefits reads as advocacy.

<!--
This is the one section that rots, and it rots in one specific place: a
"deferred" or "not yet" clause that quietly became true or false. Context and
Decision almost never need correcting. So when this drifts, do not edit it.
-->

## Alternatives considered

Each with the reason it lost. An alternative with no stated reason is not
evidence of consideration.

<!--
## Update YYYY-MM-DD

Amendment pattern: leave everything above exactly as written, flag it in the
Status line, and append a dated section here.

Never rewrite a decision record to match what happened. The record's value is
that it captures what was believed at the time; edited into hindsight it becomes
a description of the present, which the current-state document already provides
and does better.
-->
