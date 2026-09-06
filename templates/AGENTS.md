# <project> - agent instructions

<!--
  Root instruction file. Named AGENTS.md rather than a vendor-specific name because it is the
  cross-tool convention; a vendor-specific file that only points here is a compatibility shim.

  This file is auto-loaded on every turn. Two rules govern what belongs in it:
    - if a linter, formatter or analyzer can enforce it, put it there and delete the prose
    - if it can be inferred from the code, leave it out

  Do not chase a line count. Every circulating number is unmeasured. Cut when you notice a rule
  being skipped. Do not add a repository overview: that specific thing is measured as not helping.
  A directory tree is the same idea and has not been measured, so treat dropping it as judgment,
  not as a finding. It also duplicates the readme, which is reason enough.

  Delete these comments and every unused section before committing.
-->

One paragraph: what this is, what the deliverable is, and the single most important thing an agent
must not do here.

## Start here

Only if the project has a current direction that older documents contradict. Point at the two or
three documents that are authoritative right now, and name any statement elsewhere that is
superseded. Delete this section when nothing is in flux.

## Key domain concepts

The vocabulary an agent cannot infer, and where each maps in the data model. Four to six entries.
Point at the full schema or glossary rather than reproducing it.

## Hard constraints

Permanent, independent of any milestone. Phrase as prohibitions.

- **Never <the irreversible thing>.**
- ...

Then the traps: rules that are invisible in the code, where a test written from the same
misunderstanding would pass. Each one cites the incident or commit it came from. If you cannot cite
an incident, it is general good practice and belongs in a linter or nowhere.

## Evidence discipline

- **A universal claim needs a disconfirming check.** Any "zero", "all", "never" or "only" is worth
  only the search that would have falsified it.
- **Prefer a whole read over a filtered one**, and name the blind spot when you cannot.
- **Two independent kinds of evidence** for a domain claim. Two runs of the same reasoning are one.

## Code style

State only what tooling cannot check. Everything mechanical belongs in the analyzer or formatter
config.

## Dev commands

The handful that matter, with the check command named explicitly since every gate depends on it.

## References

Progressive disclosure lives here. One line each, with the trigger for reading it.

- Current state:
- History:
- Pending:
- Decisions:
- Contribution conventions:
