# Contributing

This collection grades every claim by the strength of the evidence behind it, so what counts as a
useful contribution here is unusual. Read this before opening anything.

**Contributions are ranked, and the ranking is the point.**

## 1. A counter-example. This is worth more than everything else combined.

A repository where one of these rules is wrong, **with the mechanism**. Not "this did not work for
me" but "this rule assumes X, my repository has not-X, and here is what broke."

The first-party evidence base is four small repositories, one or two people each, all observed by one
person. That is a genuine confound: a pattern across all four may be a pattern in how one person
works. It is the collection's central weakness, it is stated as such throughout, and a
counter-example is the only thing that fixes it.

**Most wanted, specifically: a repository with a retrievable review trail.** Every context
inventoried so far records who *merged* a change and nothing about who *reviewed* it. One had a
pull-request mechanism and still recorded no reviewer. If your repository has review comments, approval trailers, or a review history an outsider
could reconstruct, that is the single most valuable thing you could bring.

## 2. An outside adoption.

Run `ADOPTION.md` against a repository nobody here has seen, then report **where the procedure was
unclear or wrong**. The report matters more than the outcome.

This is the 1.0 gate and nothing substitutes for it. Three profiles exist and one person derived all
three, which tests the document rather than whether the procedure is followable. More sources, more
files and more verification passes do not close this. Only usage does.

## 3. A source.

If a claim here is tiered too high, or an open gap has an answer, that is worth more than new
practices. One gap in this collection stood as sourceless while an accepted paper answering it
already existed.

**What makes a source submission usable:**

- A link to the **primary source**, not a summary of it. Blog posts, vendor pages and aggregators may
  be used to locate a paper. They are never cited as the source of a number.
- **Peer-review status and how you established it.** The venue's own accepted list or a publisher DOI
  distinct from the preprint's. A paper's own "submitted to" line states intent, not outcome.
- Sample size, design, and **what outcome was actually measured**, which is frequently not the
  outcome a headline implies.
- Any conflict of interest, including authors employed by a vendor whose product is evaluated.

**Do not submit a statistic you have not seen in the source itself.** This collection carried a
fabricated figure for a day, attributed to a named university group, traced afterwards to a
search-optimised page naming no paper and appearing in no real one. It survived an external review
because it was specific, quotable, and agreed with a position already held. That is error 14, and it
is why this paragraph exists.

## 4. A correction.

An error in what is already written. The collection keeps a numbered list of its own errors and adds
to it rather than quietly editing, because the list is the argument for the whole approach.

## Least useful: a new practice without evidence.

This is what the tier scale exists to hold at arm's length. A practice that is sensible, widely
followed and unmeasured is a tier-7 claim at best, and the collection already has more of those than
it would like.

## Rules for any change

- **Do not use em dashes.** Anywhere, including commit messages. Use a comma, a colon, or a full
  stop. `build.py` fails the build on one.
- **Do not name an employer, customer, product, repository or commit hash** outside `LOCAL.md`.
  Round exact commit and contributor counts: precise counts fingerprint a private repository. This is
  checked in file contents and in commit metadata across all refs, because it once leaked through the
  half nothing was checking.
- **Trace every number to the source's own words** before writing it down, separately from tiering
  it. A cited claim and a correctly quoted claim are independent properties.
- **A weak source may raise a doubt. It may not retire a safeguard.** Any revision using a
  tier-4-or-weaker source to justify *stopping* something must say so explicitly.
- **Run `python build.py` before committing.** It fails on em dashes, identifier leaks in files and
  in commit metadata, a broken skill description, and unresolved cross-references. Every check
  reports the count it examined rather than "no errors", because a check that passes by finding
  nothing to check is the worst failure available here.
- **Make any new check fail on purpose before you trust it passing.** A link checker in this
  repository's own history reported everything clean while having extracted zero references.

## Attribution

Agents are disclosed with an `Assisted-by:` trailer and **never** placed in an authorship field, not
in `Co-Authored-By:` and not in the git author header. The reason is not etiquette: a co-authorship
field is an ownership claim, and naming a non-human in one risks attributing rights in the work to
its vendor. `RESEARCH.md` documents the two independent communities that converged on this rule and
why.
