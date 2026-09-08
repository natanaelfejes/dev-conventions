# Documentation conventions

Read the repository profile first. Every rule here is conditional on which slots that repository
actually has. **Do not prescribe a document set.**

This file is grounded in an inventory of **four real repositories**, all small, one or two people
each, and in the record of every documentation correction those repositories made. The useful part is
not a list of files. It is **which document types actually rot, and how**.

**It said five until 2026-09-08, and named a large third-party production codebase among them.** The
fifth was withdrawn at 0.8.0 along with every observation drawn from a repository the author does not
own. That withdrawal was applied to every other file and missed this one, which is the file that
described the withdrawn codebase in prose. Recorded as error 22.

**Everything in this file is `first-party` unless marked otherwise.** The rot taxonomy, the
displacement targets, the trust markers, the decision-record findings: all of it is direct
observation rather than published research, so it is stated once here instead of on every claim. Read
that as the warning `EVIDENCE.md` describes: strong for the cases it came from, unfalsifiable by you,
and not automatically generalisable, because four repositories worked on by one or two people share
confounds. Where a pattern appeared in genuinely independent contexts, the count is stated inline.

**Two external findings arrived 2026-09-03 and they pull in opposite directions. Both are here.**

- **Supporting, tier 2.** A study of 1.3 billion AST-level changes across 1,500 systems found comment
  changes inconsistent with their code are around 1.5 times more likely to be bug-introducing
  (Radmanesh et al., arXiv:2409.10781; the 1.3-billion-change mining study by Wen et al. is a
  separate paper and its finding is that the impact is **highest right after the inconsistency is
  introduced and decays over time**, which argues for catching drift early rather than auditing on a
  cycle). That
  is external, large-scale support for this file's central mechanism, which previously had none. It
  is also from 2019, which says the problem predates agents and was not created by them.
- **Contradicting, tier 4, and it is a real hit on this file's scope.** A study of 2,303 agent
  context files across 1,925 repositories found they behave as **living configuration rather than
  documentation**: frequently edited in small increments, not left to decay. This file treats
  instruction and context files as ordinary documents subject to the taxonomy below. **That is not
  established for them**, and 1,925 repositories outweigh four.

  The likely reconciling variable is repository activity: a file edited weekly cannot rot, and the
  first-party cases here come from repositories where nobody touched the file for two hundred
  commits. So read the taxonomy as applying to documents nobody has a reason to open, which is a
  narrower and more defensible claim than the one this file used to make.

  One finding from that study is not in tension at all and is worth acting on: those context files
  cover tests at 75.9% and architecture at 68.1%, and **security at 14.8% and performance at 14.5%**.
  Whatever else an instruction file is doing, it is almost certainly not carrying security context.
  See `SECURITY.md` on why prose is the last line and never the only one.

---

## The four slots

| Slot | Holds | Rots on |
|---|---|---|
| Current state | how the system works **now** | structural and numeric claims |
| History | what shipped and why, permanently | its own past reasoning |
| Pending | what is still open, and nothing that shipped | items that shipped and were not removed |
| Change description | why it is safe to merge **this**, **now** | nothing; it is immutable once merged |

- **Do not paste a history entry into a change description.** Different audience, different text: the
  history explains a change to someone reading in a year, the description argues to someone deciding
  today.
- **Do not let history bleed into the current-state document.** This is the most common structural
  failure and it has a cause, below.

## The displacement rule

**Dropping a slot does not remove its content. It relocates it, usually somewhere that forbids it.**

Confirmed across four repositories, with **four distinct displacement targets**. Knowing which one a
repository uses is the difference between an audit that finds the content and one that concludes it
does not exist.

**1. Sibling documents.** A repository deliberately had no history and no pending slot, with a
written rule that its current-state documents carried no "how we got here" narrative. Its history
then accumulated as a 200-line milestone log inside the current-state document, 90 lines of phase
notes in the readme, and a three-sentence changelog entry inside a decision record's status field.
All three violated that repository's own stated rule.

**2. Commit messages.** Another repository's history exists only in `git log`. An entire subsystem
was deleted along with the 158 lines of readme describing it; the sole surviving record that the
subsystem ever existed is one commit subject. Nothing indexes it, and it is invisible to anyone
reading the documents.

**3. Branch topology, the least visible of the four.** The same repository's pending work lives in
six unmerged remote branches. One sits 50 commits ahead and 60 behind the default branch, carrying a
settings page and a data-lifecycle module that **no document mentions as planned**. The roadmap is
real, and it is stored in the shape of the branch graph.

**4. An external tracker, deliberately.** A third repository routes roadmap and ticket detail to an
issue tracker and says so in writing, including an explicit instruction not to recreate a pending
document. This is the healthy case: the slot is absent, the destination is named, and the naming is
enforced. It is also the only one of the four where an auditor is not left guessing.

So if the profile declares a slot absent, it must name the destination, and that claim is something
to **verify rather than trust**. Check all four targets before concluding content is missing:
sibling documents, commit subjects, unmerged branches, and the tracker.

## A bias in the ranking below, stated before you read it

The ranking is built from **recorded corrections**: rot that somebody noticed, fixed, and wrote down.
That method has a blind spot large enough to change how you read the list.

One inventoried repository has **zero documentation-correction commits** across 254 commits and six
contributors. Not because its documents were accurate: its readme's progress section froze at one
week and then described a working, actively maintained CI pipeline as "setup in progress" through
200-plus further commits and full feature delivery. The rot was total and nothing ever corrected it.

So the taxonomy measures **rot in repositories that look at their own documents.** A repository that
never looks produces no corrective commits, no changelog entries, and no signal at all - and it is
the one whose documentation is worst. Ranking by recorded incidents systematically under-weights the
worst case.

**Round every count when you write up a private codebase.** Exact commit counts, contributor counts
and file counts **fingerprint a repository**, and combined with knowing where an author works they
identify it. The standing rule here is that an example keeps its mechanics and loses its identifiers:
a precise commit count is an identifier. The mechanics are what teach, the precision only leaks.
Rounding is not enough on its own, because de-identified is not anonymous to a reader who already
knows the codebase, so treat it as a floor rather than as clearance.

Two consequences:

- **Do not read a clean correction history as good documentation health.** It is equally consistent
  with nobody ever checking. Distinguish them by sampling the documents against the code directly.
- **The type most likely to be missing from this list entirely is whatever rots in repositories that
  never audit.** The frozen-readme pattern above is the one instance visible, and only because it was
  audited from outside.

## Which document types rot, ranked by recorded incidents

**1. A document that enumerates code is the most rot-prone type that exists.** An interface or tool
catalog carried wrong counts, omitted a real registered item entirely, asserted a blanket property of
every entry that was false for most of them, and repeated one stale status in three places. Every
addition to the code invalidates it and **nothing fails when it does**.

- Prefer generation. If the interface can emit its own schema, do that instead.
- If generation is impossible, say so in the document and pin a date.
- Never assert a property of "every" entry in a catalog. That claim ages the worst.

**2. The pending list rots even with an explicit hygiene rule.** One repository's pending document
states in its own header that shipped work moves to history. Shipped items sat in it anyway, and its
own entry describing a missing CI pipeline stayed after the pipeline was added. **A stated rule is
not sufficient.** This is the strongest argument in this document for mechanical checks.

**3. Current-state documents rot on structural and numeric claims only.** Phantom files that do not
exist, counts that disagree with the code and with other documents, dangling cross-references. Their
conceptual prose held up throughout. So audit the file paths and the numbers; leave the prose alone.

**4. Documents describing someone else's code rot on a schedule you do not control.** Decisive
detail: the one that pinned a survey date and a commit hash stayed accurate. The one that did not
went stale. **Pin the commit.**

**5. Decision records rot least, and only in one place**: a "deferred" or "not yet" clause in the
consequences or alternatives section, which silently becomes false when the thing ships. Context and
decision sections never needed correcting.

- **Do not rewrite the decision text.** It was correct when written.
- Flag the change in the status line and append a dated update section.

**6. Code comments rot exactly like documents** and need the same sweep. One repository had "all 39
tools" in two comments long after the count reached 41.

**7. History rots differently from everything else** - not on facts but on its own past *reasoning*.
The correction is a new entry, never an edit. The most valuable entry found in any repository was one
that corrected an earlier entry's explanation after it was challenged and did not hold up.

**8. An index naming a superseded authority.** The worst of the four below, because it misdirects
every reader rather than misinforming them once. One instruction file declares a particular document
to be "our only persistent memory" **twelve commits after** a second document took over that role,
and never mentions the replacement at all - 903 lines, the largest document in the repository, absent
from that instruction file's own index. A stale fact costs a reader one wrong belief. A stale index
costs them the correct document.

**9. A self-check that flags the repository's own convention.** One pre-merge command greps commit
messages for AI-attribution markers, expecting zero hits, while the repository's own convention
appends a session marker to every commit body. **38 of the last 60 commits trip it.** A check that
always fails is a check nobody runs, and it is worse than no check because its presence implies
coverage.

**10. Doc-ahead-of-code inversion.** The reverse direction of every type above. Documentation
described a 24-hour expiry that nothing implemented; by the time it was noticed, 935 of 1,039 records
had aged past the window and accumulated indefinitely. It was resolved by **writing the code to match
the document**, which is the right call when the document describes the intended behaviour, and is
why this type is easy to miss: the document was never wrong about the design, only about reality.

**11. A checklist that exists and is never filled in.** One change template carries a reviewer
checklist naming both contributors and listing "no undocumented environment variables". An
undocumented environment variable shipped anyway, through that exact item, in a repository where
every change is self-merged. The checklist is not a control; it is a record of what somebody once
hoped would be checked.

## Per-file trust markers

The single best convention found, and it came from the third-party codebase rather than either
purpose-built repo. Every one of its guides ends with an identical line declaring it a first-pass
scaffold, not deep-reviewed, verify before relying on it.

That marker is demonstrably load-bearing: a downstream repository cites it as its stated reason to
verify against source rather than trusting those guides. A self-declared confidence marker was
consumed correctly by a reader who had never spoken to the author.

**Every document carries a one-line header stating what it is, when it was last verified, and what
would make it wrong.** Freehand is worse than uniform: one repository does this well in 9 of 15
documents and the pattern is invisible in the rest.

## Mechanical checks, because prose rules are not enough

The sharpest gap found. One repository enforces code style through analyzer severities set to
`error`, and argues explicitly that analyzers beat prose. **It applies none of that to
documentation.** Every documentation correction in its entire history was found by a human or an
agent reading, never by a tool.

Worth having, in order of value per effort:

1. **A path checker.** Any file path named in a document must exist. This alone would have caught the
   phantom-file incident, the highest-severity type.
2. **A link checker** for internal cross-references. Both inventoried repositories have unchecked
   link graphs and both had dangling references.
3. **A banned-character grep** in the same gate as formatting, for whatever your instruction file
   prohibits.
4. **A count reconciler**, if a catalog document states counts: derive the number from source and
   fail on mismatch. Counts disagreed across documents at least four separate times.

**Then test each check against a known-bad input before trusting it, every time you write one.**

This is not general caution. It happened while writing this file. The link checker above was run
across this collection and reported everything clean. It had extracted **zero** references: the
pattern matching a backticked filename was broken, so the loop compared an empty list against the
filesystem and passed. Feeding it a filename that does not exist proved the comparison worked while
the extraction returned nothing, and re-running it with a fixed pattern found 17 references, all of
which then resolved correctly.

The clean result and the broken result were **indistinguishable from the output**. A check that can
pass by finding nothing to check is worse than no check, because it converts an unexamined document
set into a verified one in the reader's mind, including your own.

- **Do not trust a check that has never failed.** Add a deliberately broken case, confirm the check
  catches it, then remove the case. Ten seconds.
- **Do not report a document set as verified on the strength of a check exiting zero.** Report the
  count it examined. "17 references checked, all resolve" is a result; "no errors" is compatible with
  having checked nothing.

This is the same failure as a hook configured for a binary that is not installed, or a tool present
on disk that cannot execute. Same rule as `EVIDENCE.md`: **run the thing, and make it fail once so
you know it can.**

## Decision records

Two inventoried repositories diverged, and one side is better on each point:

- **Filename**: `ADR-NNN-kebab-case-title.md`, not `ADR-NNN.md`. Greppable and self-describing in a
  directory listing; the number-only form requires opening files to find anything.
- **Date**: a mandatory ISO date line. One repository has no decision record that can be dated: dates
  migrated into the status field as milestone labels, and after a certain number the date line stops
  appearing at all.
- **Status is for decision lifecycle only.** `Accepted`, `Proposed`, `Superseded by NNN`. Never
  overload it with implementation state. One repository's status field contains a three-sentence
  changelog entry, which is the missing history slot showing through.
- **An index.** Neither inventoried repository has one, and with a dozen records and title-less
  filenames, finding the relevant record means opening files.

### Give a record its own expiry condition

The best decision-record convention found anywhere, observed exactly once across four repositories:

```
Status: Accepted - TEMPORARY, must be reworked post-demo
```

A staleness trigger in the status line itself. Decision records already rot least of any document
type, and this is why: the one place they do rot is a "deferred" or "not yet" clause that silently
becomes false, and a written trigger converts that from silent decay into a visible condition.

**Write the reconsider-if trigger at decision time, not later.** The failure this prevents is
documented, first-party, and was stated out loud by the team it happened to: external reviewers
advised against an architecture, and the team continued because reversing was expensive, recording
that reasoning in the meeting log. Nobody missed the feedback. They received it and the decision
defended itself, because by then it had months of work behind it.

A trigger written when the decision is cheap costs one line. Reconsidering after months costs the
argument.

## Naming and cross-references

- **Do not cross-reference a numbered list item.** Numbers shift when the list is pruned. One
  document cited item G2 of another; that list was renumbered when an item shipped and the reference
  came to point at something unrelated. **Name the item.**
- **Do not store a convention in a file nothing references.** One repository's entire documentation
  convention lives in a command file with zero inbound references, making the rules invisible to
  anyone reading the documents they govern.

## The instruction file

- **`AGENTS.md` at the root**, not a vendor-specific name. It is the cross-tool convention read by
  agent tooling from many vendors; a vendor-specific file that only points at it is a compatibility
  shim, not the source. One inventoried codebase uses a vendor-specific name and is tool-locked as a
  result.
- **Do not chase a line count.** See `EVIDENCE.md`: every circulating number is unmeasured.
- **Do not include a directory tree.** Measured as not helping, and in both inventoried repositories
  it duplicated content already in the readme and the current-state document.
- One repository's instruction file grew to roughly 5,000 tokens loaded on every turn before being
  cut by 57%. Growth is the default; shrinking requires a decision.

## Archiving

When a document is read in full by a recurring process, its length is an attention cost rather than a
scrolling one. Archive when **both** conditions hold: a size threshold is passed, **and** a phase or
milestone boundary has just closed.

**Never archive mid-boundary.** A phase's story stays together, whether in the live file or the
archive. Leave a one-line pointer so a search for an old entry still lands in the right file. This is
a size convention, not a retention policy: version control keeps everything regardless.

## Documents commonly absent and worth considering

Absent from **both** purpose-built repositories inventoried, and each one a real gap:

- **A security policy.** Neither had one. Both handle credentials.
- **A licence.** Neither had one, which makes them unusable by anyone they might be shared with.
- **A runbook.** What to do when it breaks, where the logs are, how to recover. One repository
  explicitly disclaims having tested disaster recovery.
- **A testing strategy.** Both had test *commands*; neither stated what is tested, what is
  deliberately not, and why. Notably the third-party codebase **did** have one.
- **A glossary.** The most conspicuous absence, because domain vocabulary was precisely the thing all
  three codebases disagreed about most. Both had four bullets inside the instruction file instead.
- **An onboarding document** distinct from the readme.
