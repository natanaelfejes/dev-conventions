# Adopting this in a repository

A prompt to paste into a fresh agent session, rooted in the repository you want to adopt these
conventions in. It works unchanged in any repository, any language, any team size.

**Prerequisite:** this collection installed where your tool looks for skills. Nothing else.

**And one assertion before you start, which costs a sentence and once cost five days.** The first
thing the prompt does is report the version of the skill it loaded. Check it against the version you
expect. An installed skill is a copy of a document, it goes stale silently, and an adoption run
against a stale copy produces a friction log about defects you already fixed. That is error 28 and
it is the reason this line exists.

Run it once per repository. It is deliberately **two phases with a stop in between**, because the
second phase is wrong if the first one guessed. The stop is friction on purpose.

**Why a prompt rather than a checklist.** Every step below is something the collection already says
somewhere. What the prompt adds is order and refusal: it puts security before documentation, forbids
copying a profile from the examples, and makes the agent report before it changes anything. Those are
the three places an adoption pass usually goes wrong.

---

Load the `dev-conventions` skill and adopt it in this repository. Work in two phases and **stop
between them for my approval**. Do not skip ahead.

**First, before anything else, quote the version line from the top of the skill's `SKILL.md` back to
me and stop if I say it is wrong.** One line. Everything you do after this is decided by that
document, so I need to know which one you have.

## Phase 1: derive and write the profile. Nothing else.

The skill reads `.agents/profile.yml` before any of its rules apply, and it is wrong in most
repositories without one. Follow the seven-step derivation procedure in the skill's `PROFILE.md`
exactly, running the commands rather than reasoning from what the repository looks like.

Non-negotiable in this phase:

- **Do not fill the profile in from a template or from the examples.** A copied profile is worse than
  no profile, because it looks derived. The examples show shape, not answers.
- **`reviewers` is counted, never read off a policy, a template or a branch-protection setting.**
  Count commits where the authoring and committing identity differ, count review trailers, and try
  **more than one hosting platform's pull-request wording**. A search for the wrong platform's
  phrasing returns zero and looks exactly like a genuine absence. This has already produced a false
  finding in this collection's own research.
- **`secrets` is verified with `git log -- <path>`**, not against the ignore file. An ignored path can
  have been committed before it was ignored. The history command is the only output that is evidence.
- **`maturity` is derived from process evidence, not from what the readme claims.** No licence caps
  it below `published` whatever else is true.
- **`docs.absent` records where displaced content actually went**, not that a slot is missing. Check
  all four displacement targets before concluding anything is absent: sibling documents, commit
  messages, branch topology, and an external tracker.
- **Comment any field you guessed, with today's date.** A profile that hides its guesses is worse
  than a blank one.

Then **stop** and report: the profile you wrote, how you derived each field, and anything about this
repository that surprised you. Do not change any other file yet.

## Phase 2: apply the conventions, once I have approved the profile

Read the `SKILL.md` layers the profile selects, plus `DOCS.md` and `SECURITY.md`. Then work in this
order, because it is ordered by how much damage each item prevents.

**1. Security first, and report before fixing.** Work through `SECURITY.md`'s repository obligations
against this repository. Verify credentials against **full history**, not the ignore file. Check
whether any auth or safety default fails open on a fresh clone. Check whether a stated security
property is actually true in the code rather than only in a document.

**Report every finding before changing anything.** If something is exposed, I need to know before a
commit touches it, because the fix and the disclosure are different decisions.

**2. Check whether this repository's own safeguards actually install.** If a hook, a pre-commit check
or a setup step is the last line of defence for something, confirm that a fresh clone following the
documented instructions ends up with it installed. **A safeguard present in the repository but absent
from its setup instructions protects nobody.**

**3. Documentation, against the profile rather than a default set.** Apply `DOCS.md`'s rot taxonomy to
what the profile says exists. Prioritise **structural and numeric claims**: file paths named that do
not exist, counts that no longer match the code, "in progress" language on finished work, stale merge
or branch status. Leave conceptual prose alone; it holds up far better than counts do.

Where the profile records displaced content, verify it is not accumulating somewhere this
repository's own rules forbid.

**4. Add the mechanical checks that would have caught what you just found by reading.** A path
checker, an internal link checker, a banned-character grep, a count reconciler if any document states
counts.

**Then make each one fail on purpose before you trust it.** A check that can pass by finding nothing
to check is worse than no check, and this has happened in this collection's own history: a link
checker reported everything clean while having extracted zero references to check. Report the count
each check examined, never "no errors". "17 references checked, all resolve" is a result; "no errors"
is compatible with having checked nothing.

**5. The instruction file, last and least.** If an `AGENTS.md` or equivalent exists, move anything a
linter, formatter or analyzer could enforce into config and delete the prose. Do not add a repository
overview; it is measured as not helping. Do not chase a line count; no published number is measured.
**Do not generate a new instruction file from scratch if none exists**: generated context files
measurably underperform having none, so if nothing about this repository is hard to infer from its
code, the correct instruction file is none.

## Rules for the whole job

- **Never `@`-import the skill from an instruction file.** It is a skill so it loads on demand.
  Importing it turns a reference document into per-turn context, which is the exact cost it exists to
  prevent.
- **Do not touch adjacent code.** Change what the task requires. A repository-wide cleanup is its own
  change with its own review.
- **Do not invent a convention this repository does not have.** A pattern that is followed but
  written nowhere is a finding to report, not a licence to formalise it unasked.
- **Do not claim a practice reduces defects.** Nothing in this space has evidence for that, this
  collection says so explicitly, and justifying a change on scoping or cost grounds is both honest
  and sufficient.
- **Work on a branch, never the default branch.** Commit in logical pieces. Do not push and do not
  open a pull request unless I ask.
- **State what you did not verify** at the end of each phase. That sentence is more useful than a
  summary of what you did.

## What I want in your final report

1. The profile, and how each field was derived.
2. Security findings, separately and first.
3. What you changed, and what you found but deliberately left alone.
4. **What you could not verify**, and what would settle it.

If this repository contradicts something the skill asserts, **say so plainly and do not work around
it.** A counter-example is the most valuable thing this exercise can produce, and the README asks for
exactly that.
