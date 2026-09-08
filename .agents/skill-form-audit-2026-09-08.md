# Skill-craft audit: dev-conventions

Scope: form only (frontmatter, triggering, progressive disclosure, layout, packaging, evals), per skill-creator's own guidance. Not a review of the content's claims or evidence.

## 1. Frontmatter

Current:

```
name: dev-conventions
description: Evidence-graded conventions for AI-assisted development, covering claim verification, instruction files, delegation, docs and security. Adapts per repo. Load when setting up or auditing conventions.
```

`name` (15 chars) and `description` (198 chars) are both well inside any known limit, and `build.py` already checks the description is a valid plain YAML scalar with only accepted frontmatter fields. Mechanically well-formed.

The content of the description is the real problem: it names five topics (claim verification, instruction files, delegation, docs, security) but the skill's own companion-file table lists twelve areas, and several of the largest ones are absent from the description entirely: review practice and reviewer count, AI-authorship disclosure, commit/PR/diff descriptions, solo-vs-team conventions, branching and merge-gate workflow, benchmarking whether any of this works, vendor vocabulary, spec-writing before delegation, and session handoff notes. Skill-creator is explicit that the description is the *only* triggering signal and instructs authors to make it "a little pushy," covering contexts even when the user doesn't name them. At 198 of a much larger practical budget, there is plenty of room unused.

Suggested replacement:

```
description: Evidence-graded conventions for AI-assisted development: what belongs in an instruction file vs a linter, how many reviewers agent-authored code needs, whether to disclose AI authorship in a commit, solo-vs-team review and merge conventions, writing commit/PR descriptions for an agent's diff, branching and pre-merge gates, delegating to a subagent safely, and how to actually benchmark whether any of this reduces defects. Every claim is tiered by evidence rather than asserted, and rules adapt to a per-repository profile. Load when setting up or auditing a repo's AI-development conventions, reviewing an agent-authored PR, writing a commit/PR description, deciding on disclosure or review policy, or questioning whether a practice is actually supported.
```

## 2. Triggering (highest-value finding)

Requests that should load this skill, given the body's actual scope: auditing or setting up repo conventions (matches today); reviewing or merging an agent-authored PR with no second human reviewer; deciding whether/how to disclose AI-written code in a commit; writing a commit message or PR description for a large or partly-agent-authored diff; setting branch-protection or pre-merge gate policy for a team using agents; deciding how many review passes an agent's output needs, or whether an agent can review its own work; benchmarking or evaluating whether AI-assisted development is actually working; writing a spec before delegating a large task; leaving handoff notes at end of session; pushing back on inflated vendor claims ("agents write better code," "10x productivity").

Only the first of these is covered by the current description. Concretely, these phrasings would very likely fail to trigger it today:

- "this PR was mostly written by an agent and I'm the only one on the repo, can I just merge it myself"
- "write me a commit message for this diff, half of it isn't even mine"
- "should we add an `Assisted-by:` trailer to agent commits"
- "what branch protection / merge gate rules should we set up now that agents are pushing code"
- "how do I actually measure whether Claude is reducing bugs in this codebase, not just vibes"
- "I'm about to hand this feature off to an agent, should I write a spec first"
- "wrapping up for the day, what should I leave for the next session to pick up"

None of these mention "conventions," "setup," or "audit," which is the only phrase the description keys on. This is a real undertriggering gap, and it is the single highest-leverage fix available: the body already contains dedicated rules and even dedicated companion files (`WORKFLOW.md`, `HANDOFF.md`, `SPEC.md`, disclosure section) for most of these, so nothing needs to be written, only surfaced in the description.

Conversely there's no evidence of overtriggering risk: the description doesn't use generic words ("code," "development," "best practices") likely to false-positive on unrelated requests, so widening it to cover more of the actual body is low-risk.

## 3. Progressive disclosure

Split: SKILL.md ~525 lines / ~9,500 tokens (measured, not the ~8,000 stated), always loaded; twelve companion files loaded on demand. Skill-creator's ideal is under 500 lines with an added layer of hierarchy once approaching that limit, and the file is essentially at that boundary with a real hierarchy already in place (the companion-files table with load conditions), so this is not a violation, but it is worth trimming.

Two concrete opportunities to shrink the always-loaded body without losing content:

- **Layer 2 (solo) and Layer 3 (team)** are explicitly mutually exclusive per the profile ("do not apply the solo rules to a team repository, or vice versa"), yet both stay inline in SKILL.md, so every invocation loads roughly 100+ lines that apply to at most half of repositories. This is exactly the shape progressive disclosure is meant to eliminate: these two sections are strong candidates to become companion files selected by the profile's team-size field, loaded instead of always-resident.
- **"Measuring whether any of this works"** (the eval/benchmarking guidance, ~40 lines) is self-contained and only relevant to a subset of tasks (building a harness), unlike the claim-verification rules around it which apply to reading any external source. It reads more like a companion file than a Layer-1-applies-everywhere rule.

Nothing found in the current companion files that clearly belongs in SKILL.md instead; the split between "always-applicable rule" (kept in body) and "deep reference: evidence, vocabulary, tooling map, spec/handoff templates" (pushed to companions) is the right shape in principle, just not fully carried through for Layers 2/3.

## 4. Structure and layout

Skill-creator's expected shape is `SKILL.md` plus `scripts/`, `references/`, `assets/` subdirectories. This repo keeps all twelve companion files flat at repo root alongside README, CHANGELOG, CONTRIBUTING, LICENSE, etc., rather than under `references/`.

This is a defensible deviation, not a violation: skill-creator presents that layout as a convention, not a requirement, and the repo has to double as a normal, browsable git repository (with its own README, CONTRIBUTING, CHANGELOG) as well as a skill, so root-level docs match that dual purpose. The companion-files table in SKILL.md does the job a `references/` directory listing would do, naming each file and its load condition, and `build.py` explicitly excludes non-content files from the packaged distributable, so the flat layout doesn't leak into what a consuming agent actually sees packaged. `build.py` also functions as a maintainer/lint script, not a `scripts/`-style runtime script the skill instructs Claude to execute during use, so its root placement is correct either way.

One real gap: there is no `scripts/` or `assets/` at all, which is fine given the skill produces no deterministic file transforms and ships no templates-for-output beyond what already lives in `templates/` (itself a defensible non-standard name, since those are user-facing scaffolding files like `AGENTS.md`, `pull_request.md`, `profile.yml`, not skill-internal assets).

## 5. Packaging

`.claude-plugin/plugin.json` and `.claude-plugin/marketplace.json` both parse, and `marketplace.json` correctly nests `owner` and a `plugins` array with `source: "./"`. `CHANGELOG.md` records that an earlier version used a `plugin` key with no `owner`/`plugins` array and was "corrected against the published schema" alongside adding `plugin.json`, so this has already been through one real fix, not just an assumption of correctness. Fields present (`name`, `version`, `description`, `license`, `repository`, `keywords`) are consistent with the documented plugin/marketplace manifest shape. `build.py` runs its own checks (frontmatter validity, description length, no em dashes, no identifier leaks, cross-references resolving, citation-venue checks, staleness) and succeeded cleanly, producing `dist/dev-conventions-0.12.0.zip` and `.json`. Nothing found wrong with the manifests against current schema.

## 6. Evals

Skill-creator describes two eval mechanisms: (a) `evals/evals.json` task prompts with assertions, run with-skill vs. baseline via subagents, graded and viewed through `eval-viewer/generate_review.py`; (b) a separate description-triggering optimizer (`scripts/run_loop.py`) that scores a description against should-trigger/should-not-trigger queries and proposes revisions. Neither exists in this repo: there is no `evals/` directory anywhere.

Given the finding in section 2, the triggering optimizer (b) is the one worth building first and is cheap to run: an eval set of ~10 should-trigger queries drawn from the phrasings above (PR review, disclosure, branch policy, benchmarking, handoff, spec-writing) plus ~10 should-not-trigger near-misses (e.g., "write me an AGENTS.md from scratch," which the skill explicitly disclaims covering; general code review requests with no AI angle; questions about a specific vendor's SKILL.md syntax) would directly validate whether a widened description in fact fixes the gap without over-firing.

Task-output evals (a) are lower priority and harder to make useful here: because the skill deliberately "adapts, does not prescribe" and most of its output is judgment applied against a repo's profile rather than a fixed transform, assertions would mostly have to be subjective (did the agent correctly identify Layer 2 vs 3, did it cite a tier correctly, did it defer to profile) rather than the objectively-checkable kind skill-creator recommends assertions for. Worth doing eventually to catch cases where the model misapplies a tier or ignores the profile, but not as high-value as fixing triggering first.
