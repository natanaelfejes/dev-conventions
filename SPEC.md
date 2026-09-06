# Specifying a change before building it

A prompt to paste into an agent session before implementation starts. It works in any harness that
reads plain text, which is the reason it is a document rather than a slash command: command file
formats are vendor-specific and this is not.

Use it when a change is large enough that getting it wrong costs a rebuild, or when you are about to
delegate it to a worker agent. Skip it for one-line fixes, where writing the spec costs more than
redoing the work.

**What this is not.** Not a claim that specifying first reduces defects. Nothing in this space has
evidence for that and this collection says so throughout. The honest argument for a spec is narrower
and still sufficient: **it makes disagreement surface before the code exists, when changing your mind
is free.** That is a scoping and cost argument, and it is the only one made here.

---

Before writing any code, produce a specification for this change. Do not implement anything yet.

## 1. The change, in one paragraph

What should be true after this that is not true now. Written from the outside, in terms of observable
behaviour rather than implementation. If you cannot state it without naming a file you intend to
create, you are describing a plan rather than an outcome.

## 2. Assumptions, as numbered options

**Every assumption gets a number and at least one stated alternative.** Not "I assume the config is
loaded at startup" but:

> **A1. Config load timing.**
> (a) Loaded once at startup. Simplest, and a config change needs a restart.
> (b) Re-read per request. No restart, and every request pays the read.
> **Taking (a)** because nothing here changes config at runtime. Reverse this if that stops being
> true.

Numbering them matters more than it looks. A numbered assumption can be rejected individually in one
line. A paragraph of assumptions can only be rejected wholesale, so in practice it is not rejected at
all, it is skimmed.

**Mark any assumption you could check but did not**, and say what checking it would cost. An
assumption that could have been resolved by reading one file is a decision you made for the reader
without telling them.

## 3. Success criteria, each one verifiable

A criterion that cannot fail is not a criterion. For each one, state **how it is checked and by
what**: a test name, a command, an observable output. "Works correctly" is not a criterion. "`just
test` passes, including a new case that fails against the current code" is.

**At least one criterion must be checkable by someone who did not write the change.** If every check
requires knowing what you intended, nobody can review it.

## 4. Test impact map

Before touching anything, list:

- **Tests that should fail after this change and currently pass.** If this list is empty, either the
  change is unobservable or you have not found the tests that cover it. Say which.
- **Tests that must keep passing**, particularly any whose subject you are about to edit.
- **The test you will add**, and **the assertion it makes**.
- **What is not covered**, stated plainly. Every change has an uncovered edge; naming it is cheaper
  than discovering it.

**Then verify the map against the code rather than from memory.** Run the test selection. A map
assembled from what you believe the tests cover is the same failure as a secrets list assembled from
memory, and this collection has recorded that one twice.

## 5. Out of scope, by name

List what this change deliberately does not do, especially the adjacent things a reader would expect
it to do. This is the section that keeps a diff reviewable, and it is the one most often skipped.

## 6. What would make this the wrong approach

One paragraph, written honestly. The condition under which this design is a mistake. If you cannot
think of one, you have not understood the alternatives well enough to have chosen between them.

---

## Then stop

Report the specification and **wait**. Do not begin implementing.

The stop is the point. A specification produced and immediately acted on by the same agent in the
same turn has not been reviewed by anybody, and its main value, that disagreement surfaces while
changing course is still free, has been skipped.

## When you do implement it

- **Change what the specification says and nothing adjacent.** A cleanup you noticed is its own
  change with its own review.
- **If an assumption turns out to be wrong, stop and say so.** Do not repair it silently. A
  specification whose assumptions were quietly corrected mid-implementation is a record of what you
  meant to do, not of what happened.
- **End with what you did not verify.** That sentence is more useful than a summary of what you did.
