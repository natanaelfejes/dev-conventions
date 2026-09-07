# Closing a session so the next one does not start from nothing

A prompt to paste at the end of a working session, before the context is gone. Like `SPEC.md` it is a
document rather than a slash command, because command formats are vendor-specific and this is not.
**That is the whole point here:** the record it produces is a file in the repository, so the next
session reads it whichever harness or vendor it runs in.

Run it when the work outlives the session: a decision was made, a direction was rejected, something
is half-finished, or you learned something about the codebase that is not written down anywhere.
Skip it when the session produced a merged change and nothing else, because the diff and its message
already are the record.

**What this is not.** Not a claim that session handoffs improve anything measurable. Nothing here has
been measured, `EVIDENCE.md` gap 11 records that agent memory architecture is unmeasured in general,
and practitioner writing on it is abundant and uncontrolled. The honest argument is narrower and
sufficient: **everything lost is lost in the gap between deciding and recording, and that gap is
usually one turn wide.** This closes that turn. It is a cost argument, not an outcome claim.

**The failure this is designed against** is specific and it is not forgetting. It is a next session
that reads a confident conclusion, cannot see what produced it, and either redoes the work or, worse,
builds on it without being able to check it. So the rule running through every section below:
**record the state that produced a conclusion, not only the conclusion.**

---

At the end of this session, write a handoff record. Do not summarise the conversation.

## 1. What is now true that was not true before

Changes that landed, in terms of observable behaviour rather than files touched. A reader who does
not have this conversation should be able to tell what moved without reading the diff.

If nothing landed, say so plainly. A session that produced only a decision is a valid session and a
handoff claiming otherwise is worse than no handoff.

## 2. Decisions, each with what it was chosen over

**A decision without its rejected alternative is not a decision, it is a preference**, and the next
session cannot tell whether the alternative was considered or never occurred to anybody. One line
each:

> **Chose X over Y** because Z. Reverse this if Z stops holding.

The reversal condition matters more than the reason. It is what lets a later session overturn the
decision deliberately instead of by accident.

## 3. What is deliberately not done

By name, and with why. This is the section that prevents the most waste, because an unfinished thing
and a rejected thing look identical from outside and the next session will pick up whichever it finds
first.

Separate the two:

- **Not done yet**, with what it is waiting on.
- **Decided against**, with the reason, so nobody re-proposes it as a fresh idea.

## 4. Open questions, each with what would settle it

Not "unsure whether the cache is safe" but "unsure whether the cache is safe; running the
concurrency test under load would settle it". A question without a resolution path is a worry, and
worries accumulate in handoff documents until nobody reads them.

## 5. What you learned about this repository that is not written down

The thing that took twenty minutes to work out and takes one line to state. A non-obvious build step,
a test that is flaky for a known reason, a file that looks unused and is not.

**Then put it where it belongs rather than leaving it here.** If it is a repository fact it goes in
the instruction file or the profile; if it is a documentation defect it goes to `DOCS.md`'s process.
A handoff record is a queue, not a destination, and a fact that lives only in the handoff will be
re-learned.

## 6. State the verification, and its scope

What you actually ran, and what that run did not cover. "Tests pass" is compatible with several
different failures. "The unit suite passes, 340 tests, integration not run" is a result the next
session can act on.

This collection has recorded four separate cases of a check that was correct within a scope nobody
stated. **A handoff that reports a clean result without its boundary reproduces that error by hand.**

---

## Where it goes

Into the repository, in the same turn. Not into chat, not into a scratch file outside version
control, and not into a vendor's own memory store, because a record only one harness can read fails
at the moment you switch harnesses, which is the moment you most need it.

**The profile decides the destination.** If the repository has a pending or working-notes document,
append there. If it does not, `HANDOFF.md` at the root is a reasonable default and `PROFILE.md`'s
`docs` field should then be updated to say the slot now exists, because a document nothing declares
is a document nothing maintains.

**Keep one, and prune it.** A handoff file that accumulates every session becomes the thing nobody
opens, which is `DOCS.md`'s rot pattern arriving through the front door. Resolved items move out or
get deleted. The test is whether the file is still readable in one sitting.

## One thing this does not solve

**A handoff record is a claim about a session, written by the agent that ran it.** It inherits every
weakness of self-reported work: it will not record what the agent did not notice, and it will present
a partial result with the confidence of a complete one unless section 6 forces the boundary out. Read
it as a starting point that a fresh session should verify cheaply, never as established fact about
the repository.
