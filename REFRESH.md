# Refreshing this collection

A prompt to paste into a research-capable agent session **once a quarter**. It is what
`build.py`'s staleness check tells you to run when the recheck date goes past ninety days.

**Why a prompt rather than a schedule.** `SKILL.md` has carried a quarterly cadence since early on
and nothing enforced it, which made it a promise rather than a mechanism. Two things changed that:
the build now warns at 90 days and fails at 180, and the work itself is written down here so it does
not have to be reconstructed from memory each time. A cadence nobody can execute without thinking
hard first does not get executed.

**This does not re-research the field from scratch, and that is deliberate.** A from-scratch pass
rediscovers what the collection already holds, which is expensive and produces rediscovery rather
than replication. The value is in what changed: statuses that moved, gaps that got answered, and
claims that went stale.

---

## Before you start

Read `EVIDENCE.md`'s open-gaps list and its contested-findings section, and `ROADMAP.md`. Those three
are the entire input. **The gap list records what searching failed to find, not what does not
exist**, and it should be read that way every time.

---

## The four jobs, and they are different jobs

### 1. Administrative facts, checked as a unit

`EVIDENCE.md` keeps adoption figures, governance status, supported-tool lists and vendor claims in
one section for exactly this reason. **They rot fastest and matter least individually**, which is why
they get checked together and cheaply.

For each: is it still true, and what is the date of the source saying so. A figure that was right in
March and is unmarked in December reads as current, which is the failure mode.

### 2. Tier 3 entries, rechecked

Tier 3 means a decision was pending. **Pending decisions resolve, in both directions, and nobody
sends a notification.** For each tier-3 entry: check DBLP, the venue's accepted-papers list, or a
publisher DOI distinct from the preprint's. Report accepted-and-where, rejected, or still pending.

Do the same for anything in the contested-findings section whose contest was a venue status.

### 3. Open gaps, re-searched

Not the sources. **The gaps.** One gap in this collection stood as sourceless while an accepted paper
answering it already existed, missed by four separate research passes.

For each open gap, run the recorded query strings again plus at least two you invent, and report:
still open, narrowed, or closed. **Record the exact strings for anything that found nothing**, and
add them to the gap's entry, because a negative result with recorded terms is what lets the next
person do better rather than repeat the search.

### 4. Anything the collection asserts that a new source now contradicts

The most valuable outcome of a refresh is not a new source agreeing. It is a new source disagreeing.
Look specifically for work published since the last recheck date that points the other way on
anything currently asserted.

---

## Hard rules, which do not relax because this is a routine pass

1. **Never report a statistic you have not seen in the primary source.** A fabricated figure survived
   an external review of this collection because it was specific, quotable, and agreed with a
   position already held.
2. **Blog posts, vendor pages and aggregators locate a paper. They are never the source of a number.**
   A named practitioner is a valid source for their own stated position and never for a number they
   did not measure.
3. **"Could not find" and "does not exist" are different claims.** Never conflate them, and say which
   one you are making.
4. **Rediscovery is not replication.** Finding the same paper again confirms the paper exists. It
   does not corroborate the finding and it does not resolve a disagreement.
5. **A tier is a rater's judgment with known disagreement, not a property of the source.** If you
   would tier something differently from how it is tiered, say so and say why. That is a finding, not
   a correction.

## `SECURITY.md` moves on a faster clock

It cites CVEs, an OWASP ranking and active supply-chain campaigns. **Recheck it more often than
quarterly**, and treat a year-old security document as worse than an absent one, because it reads as
current.

---

## After the pass

1. Apply the corrections. **Record any new error on the numbered list rather than editing quietly**,
   because that list is the argument for the whole approach.
2. Bump the version and **the recheck date in both `SKILL.md` and `README.md`**. The staleness check
   reads the one in `SKILL.md`, so an unbumped date fails the build at 180 days, which is intended.
3. Update `CHANGELOG.md` with what changed and, more importantly, **what was checked and did not
   change**. A refresh that only records changes leaves a reader unable to tell a checked claim from
   an unchecked one.
4. State what you did not verify.
