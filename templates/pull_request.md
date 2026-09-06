<!--
  Change description template.

  FIRST: run `git log --oneline main..HEAD` and account for every commit it prints, including any
  you did not write. Describing only your own commits on a stacked branch is how a source change
  merges as "documentation only".

  Three sections are required: Purpose, Changes, Risk, Verification. Delete the optional ones rather
  than leaving an empty heading.
-->

## Purpose

<!-- Why this exists and what would be wrong without it. Not a restatement of the title. -->

## Changes

<!-- Grouped by area, one bullet per file or coherent group. Mark new files `path (new)`.
     What changed, not why. -->

## Key decisions

<!-- OPTIONAL. Only where a reader could reasonably have expected a different choice.
     Each one: the choice, the alternative rejected, the reason. -->

## Risk

<!-- Blast radius and reversibility. "Low" on its own is not a risk section: name what could break,
     and name what would surface it. If nothing would surface it, that is the most useful sentence
     in this description. -->

## Verification

<!-- What ran, what the result was, and what was NOT verified. Numbers, not adjectives.
     Name the review passes that ran, or say why none applied. Negative evidence is stated, not
     omitted: "no review passes run, documentation-only diff" is complete; silence is not. -->

## Known limitations

<!-- OPTIONAL but expected on anything shipping incomplete. -->

## Follow-ups

<!-- OPTIONAL. Concrete, with an identifier where one exists. Name the item, never a list position:
     numbers shift when the list is pruned. -->
