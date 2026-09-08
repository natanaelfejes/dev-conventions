# External evaluation, 2026-09-08

**Scope: does this collection deserve to exist alongside what already exists, and is it pointed in
the right direction?** Not an internal audit. An internal audit ran on 2026-09-08 and its findings
are applied.

**This file develops the collection and is not part of it.** It lives in `.agents/`, which
`build.py` excludes from the distributable.

---

## How the outside evidence here was obtained, and its limits

Stated first because the collection's own rules require it and because the limits are real.

**Reachable from this environment and read directly:** the GitHub REST API (star counts, repository
metadata), `raw.githubusercontent.com`, `github.com`, `code.claude.com`, `platform.claude.com`. Two
comparables were cloned and measured with `wc` rather than described.

**Blocked by the network egress proxy, every attempt:** `arxiv.org`, `export.arxiv.org`,
`journals.plos.org`, `pmc.ncbi.nlm.nih.gov`, `api.semanticscholar.org`, `simonwillison.net`,
`karpathy.bearblog.dev`, `www.anthropic.com`, `developers.openai.com`, `antigravity.google`,
`aaif.io`, `agents.md`, `huggingface.co`, `emergentmind.com`.

So for roughly a third of the comparables below I have **could not confirm from the primary source**,
not **confirmed**. Where a claim rests on a search engine's index of a page rather than the page, it
says so on the line. No figure in this report is asserted from a blog's summary of a paper. Two
figures that circulate widely in this space are named below and deliberately **not** adopted.

One trap I walked into and back out of, recorded because it is the collection's own error 10 in a new
costume: a GitHub code search for `filename:EVIDENCE.md` with tier language returned exactly one
result, this repository. That looked like a clean absence result. It is not: the GitHub MCP search
runs authenticated as the repository owner, so its index includes this account's private
repositories. A follow-up unauthenticated fetch of the repository's web page returned HTTP 404, which
confirms the repository is still private and confirms that the code search was not a public-only
search. The absence claims in section 3 are therefore stated as **weak evidence of absence over
GitHub's public code index**, with the query given, and not as confirmed absence.

---

## 1. The verdict in five sentences

The evidence layer is genuinely differentiated and I could not find anything that does it for this
field, but the conventions layer it was built to support has been overtaken during the four days this
collection has existed, because the vendors now publish, for free and continuously, most of what
`SKILL.md`'s "Working with agents" section says. The direction should change: **split**, into a small
conventions skill that carries tiers inline and a standalone, citable evidence document that carries
the apparatus, because the two have different audiences, different cadences and different failure
modes, and the apparatus is currently suffocating the deliverable. Two of the collection's three
showcase claims about vendor advice conflicting with measurement are now stale against what the
vendor published as of the day I read it, and the one place a live conflict does exist is unrecorded,
which is a quarterly-cadence miss in the agent-facing file rather than a research failure. The
reputation play is real but not in its current shape: a 56,000-word private repository with zero
adoptions entering a field whose leading artifact has 283,098 stars will not land on completeness, it
will land on one checkable finding, and that finding already exists at line 1215 of `EVIDENCE.md`
where nobody will read it. Publish the venue audit, keep the errors list, cut the skill to roughly a
third, and stop running verification passes until somebody other than the author has run
`ADOPTION.md` once.

---

## 2. The landscape

Star counts retrieved from the **GitHub REST API on 2026-09-08** via authenticated repository search.
They are a popularity proxy and nothing more; they go stale, and one secondary blog encountered
during this research reported `hesreallyhim/awesome-claude-code` at 36.8k on the same day the API
returned 53,687, which is the reason for using the API.

### Direct comparables: practitioner conventions and methodology

| Comparable | Popularity, source, date | What it does better | What `dev-conventions` does better | Overlap or complement |
|---|---|---|---|---|
| **obra/superpowers**, "an agentic skills framework and software development methodology that works" | **283,098 stars**, GitHub API, 2026-09-08. Created 2025-10-09 | Distribution, by two orders of magnitude. Decomposed into 39 skill files averaging about 1,100 words, each loadable alone. Ships a `writing-skills` methodology and, unusually, a behavioural test file (`skills/writing-skills/examples/CLAUDE_MD_TESTING.md`) that probes whether an agent consults a skill under time pressure and sunk cost | Cites nothing. I grepped the clone for `arxiv|doi|peer-review|et al` across 94 markdown files: the hits are prose, not citations. No confidence marking. No repository profile: grep for `profile.yml`, `repository profile`, `adapt to your repo` returns zero across the clone | **Overlap, heavy.** Same topic, same format, same install path. This is the artifact a stranger already has installed |
| **addyosmani/agent-skills**, "production-grade engineering skills for AI coding agents" | **92,941 stars**, GitHub API, 2026-09-08. Created 2026-02-15 | 25 lifecycle skills, each a self-contained `SKILL.md` of 1,229 to 4,037 words, median about 2,000. Named authorship with existing reputation. Grounded explicitly in *Software Engineering at Google* and Google's engineering practices guide, which is a legible provenance story even though it is not evidence grading | One informal citation in the whole corpus (`context-engineering/SKILL.md` cites Liu et al. 2023 for lost-in-the-middle) and one bare "Research shows". No tiers, no gaps, no errors list, no profile | **Overlap, heavy**, on lifecycle conventions. Complementary only on `OPERATING.md` and the evidence apparatus |
| **msitarzewski/agency-agents** | **150,912 stars**, GitHub API, 2026-09-08 | Reach | Everything about rigour | Adjacent. Agent personas, not conventions |
| **hesreallyhim/awesome-claude-code** | **53,687 stars**, GitHub API, 2026-09-08 | The canonical index. Discovery | Not comparable: it is a list, which this collection permanently refuses to be | **Complement.** This is where a stranger would find the collection, not what they would compare it to |
| **ComposioHQ/awesome-claude-skills** | **74,665 stars**, GitHub API, 2026-09-08 | Reach | As above | Complement |
| **VoltAgent/awesome-agent-skills**, "1000+ agent skills, compatible with Claude Code, Codex, Gemini CLI, Cursor" | **33,926 stars**, GitHub API, 2026-09-08 | Independent corroboration that the skill format is genuinely cross-vendor | As above | Complement, and evidence for one of this collection's own administrative facts |
| **PatrickJS/awesome-cursorrules** | **40,741 stars**, GitHub API, 2026-09-08. Created 2024-09-16 | The prior generation's equivalent, still growing | Rules per framework, no evidence, no profile | Overlap, declining relevance as `.cursorrules` gives way to `AGENTS.md` |

### First-party vendor guidance

| Comparable | Status | What it does better | What `dev-conventions` does better | Overlap or complement |
|---|---|---|---|---|
| **Anthropic, "Best practices for Claude Code"**, `code.claude.com/docs/en/best-practices` | **Read in full, 2026-09-08.** No star metric; the product repository is at 144,428 stars, GitHub API, same date | Free, continuously updated, authoritative on its own product, and **far broader than "authoring guidance"**. It covers verification loops, plan-then-code, subagent delegation for context economy, git worktrees for parallel session isolation, a Writer/Reviewer pattern justified by fresh context, an adversarial review step, and five named failure patterns | Says how strongly anything is supported: nothing. Single-vendor by construction. No profile conditioning. No account of what is contested | **Overlap far larger than the collection admits.** See section 9 |
| **Anthropic, "Skill authoring best practices"**, `platform.claude.com` | **Read in full, 2026-09-08** | Now includes an "Evaluation and iteration" section with "Build evaluations first" and a JSON evaluation structure, which is adjacent to `SKILL.md`'s "Measuring whether any of this works" | Independent measurement, tiers, the judge-bias caveat | Partial overlap on evaluation. The collection is right that authoring mechanics are taken |
| **OpenAI, Codex best practices**, `developers.openai.com/codex/learn/best-practices` | **Could not confirm.** Domain blocked. Search index reports it prescribes "Keep each file under 100 lines (hard limit 300 lines)" and "only store information that Codex cannot infer from the code" | If that wording is real, it is a first-party line-count target, which bears directly on two of this collection's claims | Grading, if the vendor number is unmeasured, which it almost certainly is | Overlap on instruction files. **Unverified** |
| **Google, Antigravity CLI best practices**, `antigravity.google/docs/cli/best-practices` | **Could not confirm.** Domain blocked. Search index reports Antigravity supports `SKILL.md` at `~/.gemini/config/skills/` and `<project-root>/.agents/skills/`, and that Gemini CLI is transitioning to Antigravity CLI | Third-vendor confirmation of the skill format, and a `.agents/` directory convention that matches this collection's own `.agents/profile.yml` placement | As above | Complement. **Unverified** |
| **AGENTS.md, stewarded by the Agentic AI Foundation under the Linux Foundation** | Collection already grades this correctly in "Administrative facts". `aaif.io` blocked | Cross-vendor neutrality | Nothing to compare | Complement |

### Named practitioners, the reputation competitors

| Comparable | Status | What it does better | What `dev-conventions` does better | Overlap or complement |
|---|---|---|---|---|
| **Simon Willison, "Agentic Engineering Patterns"** | **Could not confirm from primary source**, `simonwillison.net` blocked. Search index and his own post dated 2026-02-23 indicate a chapter-shaped guide, first two chapters published February 2026, adding 1 to 2 chapters a week, in the *Design Patterns* format | Audience, voice, and cadence. A pattern-per-post serial is readable, quotable, and accumulates followers, which is precisely the outcome goal 3 asks for. He is already the default citation in this space | Nothing on distribution. On evidence: unknown, could not read it. On profile conditioning: could not confirm either way | **Direct competitor for reputation**, not for function. The most important entry in this table for goal 3 |
| **Andrej Karpathy, "agentic engineering"** | **Could not confirm from primary source**, `karpathy.bearblog.dev` blocked. Search index attributes the term to his Sequoia Ascent 2026 talk and a January 2026 thread of guidelines | Coins the vocabulary the whole field then uses. `VOCABULARY.md` grades terms, and this is where the terms come from | Grading, provenance, and the refusal to assert | Complement. His framing ("the agent is fallible and stochastic") is the premise the tier-1 nondeterminism finding supplies evidence for |
| **Addy Osmani** | Repository measured above; also publishes long-form on spec writing | Reach, plus a named institutional provenance | Evidence grading | Overlap |

### Evidence-methodology comparables

| Comparable | Status | What it does better | What `dev-conventions` does better | Overlap or complement |
|---|---|---|---|---|
| **GRADE** (medicine) | Already engaged, correctly and self-critically, in `EVIDENCE.md`'s "A tier is a rater's judgment" | Three decades of reliability studies on the instrument itself | Applies to this domain at all | Complement. The collection's use of GRADE's reliability literature against its own scale is the single strongest piece of intellectual honesty in the artifact |
| **Kitchenham, Budgen and Brereton, *Evidence-Based Software Engineering and Systematic Reviews***, CRC Press, ISBN 9781482228656 | Confirmed to exist as a book via multiple retailer and ACM Digital Library index entries, 2026-09-08. **Not read** | The canonical treatment of evidence models for software engineering primary studies | Currency. EBSE predates coding agents entirely | Complement, and the collection already records the key fact: EBSE's appraisal half largely did not take hold |
| **Hillel Wayne and Laurent Bossavit**, empirical software engineering skepticism | Talks and writing confirmed to exist via multiple index entries, 2026-09-08. Not read in this pass | The genre's best-known practitioner voice for "we do not actually know this" | Turns the skepticism into per-rule action, which they mostly do not | **Complement, and the closest intellectual ancestor.** Not cited anywhere in the collection |
| **arXiv:2605.11027**, "From Code-Centric to Intent-Centric Software Engineering" | **Could not confirm.** arXiv blocked. Search index reports a corpus curated in three layers: peer-reviewed research, technical preprints and benchmark artifacts, public thought-leadership | If that description is accurate, it is the nearest published thing to stratifying this field's evidence by review trail | Attaches the strata to actionable rules, which a thematic analysis does not | **The closest prior art found.** Unverified, and it grades a corpus rather than a practice set |
| **arXiv:2606.22484**, "Governed AI-Assisted Engineering: Graduated Human Oversight" | **Could not confirm.** Search index reports a three-tier oversight model routing tasks by regulatory impact, reversibility and data sensitivity, with a per-tier evidence artifact model | If accurate: a published, conditional-on-context oversight scheme, which is `PROFILE.md`'s idea in a regulated setting | Broader scope, no regulatory assumption | **Overlap with the profile thesis.** Unverified |
| **arXiv:2604.09388**, "The AI Codebase Maturity Model" | **Could not confirm.** Search index reports six CMMI-inspired levels validated by a 100-day experience report | A published maturity ladder, which is `PROFILE.md`'s `maturity` field with a literature behind it | Refuses to promise the top of the ladder | Overlap with `PROFILE.md`. Unverified |
| **Borg, Hagatulah, Tornhill and Söderberg, "Code for Machines, Not Just Humans"**, FORGE 2026 | Venue and DOI `10.1145/3793655.3793722` reported by two non-author-controlled surfaces on 2026-09-08: the conference programme at `conf.researchr.org` and an ACM DOI. **Neither opened.** A press release attributes a "defect risk by at least 30 percent in unhealthy code" figure to it; **that figure is not adopted here** | A peer-reviewed empirical study on the exact question the collection says nobody has answered | Nothing. This is a gap, not a comparison | **A source the collection should hold and does not.** See section 5 |
| **DORA, State of AI-assisted Software Development** | Publication series confirmed to exist via `dora.dev` index entries and a Google Cloud landing page, 2026-09-08. Reports not opened. A 2026 "ROI of AI-assisted Software Development" report is reported by InfoQ, May 2026 | The largest recurring survey instrument in this exact field | Would rate it honestly, probably tier 6 | **Absent from the collection entirely.** `grep -rn "DORA" *.md` returns zero. See section 9 |
| **AAIF, "Measuring AGENTS.md: Five-Run Benchmark Results"** | **Could not confirm**, `aaif.io` blocked. Search index describes two identical clones, one with a twelve-line `AGENTS.md`, same agent, same prompt, same starting commit, five runs per condition, and reports that a single run per condition produced a misleading result that the five-run design overturned | A Linux Foundation project running, and publishing, exactly the multi-run protocol this collection prescribes, on the exact artifact class the collection calls uniformly tier 4 | Nothing here | **The most important unclaimed source in this report.** Independent institutional corroboration of the tier-1 rule, arriving from a direction the collection did not look |

---

## 3. Is the thesis differentiated?

**Yes, and more so than I expected before running the searches. I found nothing that grades
AI-assisted development conventions by review trail, and the two artifacts most likely to are
confirmed not to.**

What I actually established, separated by strength:

**Confirmed, by reading the artifacts.** `obra/superpowers` (283,098 stars) and
`addyosmani/agent-skills` (92,941 stars) were cloned on 2026-09-08 and grepped. Across 94 and 95
markdown files respectively, there is one informal academic citation in the two corpora combined
(Liu et al. 2023, in `context-engineering/SKILL.md`) and one bare "Research shows". Neither carries
confidence marking of any kind. Neither adapts to a repository profile: grep for `profile.yml`,
`repository profile` and `adapt to your repo` returns zero across both clones. Superpowers states
"Evidence over claims" as a philosophy line, and it means *verify before declaring success* at
runtime, not *grade the provenance of the rule*. Those are different things and the collection is
entitled to the distinction.

**Confirmed, by reading the vendors.** Anthropic's two current guidance pages, read in full on
2026-09-08, contain no strength-of-evidence marking on any claim, and no citation to any study. The
skill-authoring page's "Evaluation and iteration" section is about testing your own skill, not about
grading a claim's provenance.

**Weak evidence of absence, stated as such.** GitHub code search for `"evidence-graded" OR "evidence
graded"` with agent and conventions terms returned zero results across the public index. A search for
`"tier 1" "tier 8" "peer-reviewed"` with evidence and conventions terms returned three results, two
of them this repository. GitHub code search indexes default branches and matches phrases, so a
collection using different words would not appear. This is not confirmed absence.

**Could not confirm, and it is the honest caveat on the whole claim.** arXiv:2605.11027 is described
by a search index as stratifying this field's literature into peer-reviewed, preprint and
thought-leadership layers. If that description is right, someone has done the classification, in an
academic register, and published it before this collection existed. I could not open the paper. **If
one thing in this report should be checked first, it is that paper.**

**What is not differentiated, and should stop being claimed as if it were.** The conventions
themselves. Every Layer 1 rule about working with agents that I could check has a first-party vendor
equivalent published for free. Section 9 lists them side by side.

**One genuine differentiator nobody has priced.** The numbered errors list. I found no comparable
artifact in this space that keeps one. It is not a research contribution, it is a credibility
instrument, and it is the only thing here that a skeptical reader cannot dismiss as more advice.

---

## 4. Direction: split

**Recommendation: split into two artifacts, on different cadences, with different audiences, and cut
the conventions half by roughly two thirds.** Not keep as is. Not narrow to evidence only. Not merge.
Not abandon.

### Artifact A: the skill, and it should be small

Target: `SKILL.md` at 2,000 to 2,500 words, down from 6,124. It keeps the profile mechanism, the
tier tag on every rule, and only rules that clear one of two bars:

- **tier 1 or tier 2**, of which there are few and they are the best thing here, or
- **`first-party` with a specific incident behind it**, which is the collection's own standard for a
  rule in an instruction file and which it does not fully apply to itself.

Everything that merely restates current vendor guidance is deleted, with a line saying where it now
lives. That is not a retreat: a rule that the vendor documents, updates and ships to every user is a
rule this artifact should not be carrying, maintaining or rechecking quarterly.

`PROFILE.md`, `ADOPTION.md`, `SPEC.md`, `HANDOFF.md`, `SECURITY.md` and `OPERATING.md` stay as
companions. `DOCS.md`, `WORKFLOW.md`, `TOOLING.md`, `OBSERVABILITY.md`, `VOCABULARY.md` and
`RESEARCH.md` move to artifact B or go, per section 6.

### Artifact B: the evidence document, and it is the reputational asset

`EVIDENCE.md` becomes a standalone, human-readable, citable **living review** of what is actually
known about AI-assisted development, published as a document rather than shipped as a skill. It
carries the tier scale, the sources, the disagreements, the gaps, the errors list, the outside-checks
table and the administrative facts. It gets the DOI. It gets the quarterly cadence. It gets read by
humans, which is what it was written for: 32,000 estimated tokens is not a reference an agent should
be loading, and nothing in `ADOPTION.md`'s two phases requires it.

### Why split rather than keep

Three reasons, in order of force.

1. **The two halves have opposite optimal sizes and are fighting.** The skill wants to be small
   because the author's own stated pain is token burn and friction. The evidence document wants to be
   large because completeness is its whole value. Bundling them means every adoption pays the
   apparatus's weight and every reader of the apparatus is handed a skill they did not want.
2. **They have opposite cadences.** Vendor-adjacent conventions rot in weeks. The evidence base moves
   in quarters. A single version number over both means either the conventions are stale or the
   evidence is churned.
3. **`AGENTS.md` already diagnosed this and the structure prevents the cure.** "Seven verification
   passes have run and zero adoptions. Every one of those passes generated evidence, changelog and
   error entries. None of them generated a rule." That is not a discipline failure. It is what
   happens when the apparatus and the deliverable share a repository, a version and a build: the
   apparatus is the part that rewards work, so it gets the work.

### Why not narrow to the evidence layer only

Because the profile mechanism is the second differentiator and it would be thrown away. I checked
both leading comparables and neither has anything like it. It is unexercised, three profiles all
derived by one person, but unexercised is a reason to test it, not to delete it.

### Why not merge into an existing collection

`superpowers` and `agent-skills` are single-author artifacts with a stated philosophy and no evidence
apparatus. A pull request adding tier tags to 39 skill files would be rejected or, worse, accepted and
then rot, because neither maintainer has committed to a recheck cadence and the tags would silently
become the thing this collection warns about: a strength marking nobody is maintaining. Merging the
evidence layer into somebody else's conventions is how you get authority laundering.

### The strongest argument against my own recommendation

**The split recreates the exact artifact the collection was built to replace.** Its founding
complaint is that "a measured finding and somebody's blog post arrive looking identical". A
2,000-word skill of terse prohibitions, physically separated from the evidence, is a document that
looks identical to every other rules file in the field. The tier tag inline is a thinner protection
than it sounds, because a reader who will not click through to `EVIDENCE.md` is reading an
ungrounded rules file with decoration on it.

I think this objection is serious and partly right, and here is why I still recommend the split.
What separates is the **apparatus**, not the **grading**. The tier stays on every rule, the phrasing
that names what is contested stays inline, and the "what this rests on" table in `SKILL.md` stays.
What leaves is the gap list, the errors list, the outside-checks table, the search records and the
sources themselves, none of which an agent applying a rule needs and all of which a human evaluating
the collection needs. If the objection is right, the failure will be visible: readers will quote the
skill without the tiers. That is a testable prediction and it is worth taking the risk to find out,
because the current arrangement has produced zero adoptions in seven passes and is testing nothing.

---

## 5. What to take from existing work, file by file

Specific, and none of it is a curated list or a product ranking.

**`EVIDENCE.md`, tier 2 section. Add Borg, Hagatulah, Tornhill and Söderberg, "Code for Machines, Not
Just Humans: Quantifying AI-Friendliness with Code Health Metrics", FORGE 2026, DOI
10.1145/3793655.3793722.** The collection already holds a different Borg et al. paper and holds it
well. This one is on the exact question `SKILL.md` says nobody has answered. **Fetch the paper
before writing anything.** The "30 percent defect risk" figure circulating for it comes from a press
release and is precisely the shape of error 14. Take the venue confirmation from the ACM DOI and the
conference programme, both non-author-controlled, which is what the collection's own error 20 rule
requires. Expect it not to close the gap, because it is not randomised and the outcome is a
refactoring-preservation proxy rather than a fielded defect, but the gap statement needs to name it.

**`EVIDENCE.md`, open gaps and the instruction-files section. Add the AAIF five-run `AGENTS.md`
benchmark.** A Linux Foundation project ran a controlled, five-runs-per-condition comparison of a
twelve-line `AGENTS.md` against no `AGENTS.md`, and reported that the single-run result was
misleading and the five-run result overturned it. That is: independent institutional corroboration of
the collection's only tier-1 rule, arriving on the collection's weakest-sourced topic, from an
organisation the collection already cites for governance. It probably rates tier 5, vendor-disclosed,
and it should be in the document at whatever tier it earns. `aaif.io` is blocked from here; fetch it
from a browser.

**`EVIDENCE.md`, administrative facts. Add DORA.** `grep -rn "DORA" *.md` returns zero across the
whole collection. The State of AI-assisted Software Development series is the largest recurring
instrument in this field. It rates low on this scale, probably tier 6, and rating it low is a
different act from not knowing it exists. A reader who does know it exists will read the omission as
ignorance rather than as judgment.

**`EVIDENCE.md`, the tier-scale section. Cite arXiv:2605.11027 or rule it out.** If its three-layer
corpus stratification is what the index says it is, it is prior art for the central thesis and the
collection should say so and say how it differs. If it is not, saying so is worth a sentence. Either
outcome is better than silence.

**`EVIDENCE.md`, the "a tier is a rater's judgment" section. Add Bossavit and Wayne.** The
skepticism-about-software-engineering-claims genre has a practitioner lineage and the collection
writes as if it invented the posture. Naming the ancestors costs three lines and makes the section
harder to dismiss as a hobbyist's affectation, which is exactly the dismissal a publication attempt
will attract.

**`SKILL.md`, "Working with agents" and "Instruction files". Take the vendor's current text as a
delete list, not as an addition.** Every rule with a first-party equivalent should be cut or reduced
to a one-line pointer. Section 9 has the mapping. This is the single highest-value edit in the
report and it makes the file smaller, not larger.

**`SKILL.md`, the conflict section. Take the vendor's reviewer caution as a live disagreement.**
Anthropic's page now warns that "a reviewer prompted to find gaps will usually report some, even when
the work is sound, because that is what it was asked to do", and that chasing every finding leads to
over-engineering. `SKILL.md` says "do not stop at isolating the reviewer, instruct it to disagree",
on a tier-4 source that was demoted from tier 2 on 2026-09-07. That is a real, current, checkable
conflict between a weak measurement and first-party guidance, and it is exactly what the
"Disagreements, left standing" section is for. It is not recorded anywhere.

**`ROADMAP.md` or a new file. Take superpowers' `CLAUDE_MD_TESTING.md` method, not its content.**
Superpowers ships scenario prompts that test whether an agent actually consults a skill under time
pressure, sunk cost and authority bias. That is a cheap behavioural eval of a rules file, it is
directly aimed at the failure mode `SKILL.md` worries about (a rule being skipped), and it can be
run five to ten times per the collection's own tier-1 rule. It costs an afternoon and it would be the
first thing in this collection that was measured rather than reasoned about. MIT-licensed, so
adaptable with credit.

**`OPERATING.md`. Take Karpathy's vocabulary, with a `VOCABULARY.md` verdict.** "Agentic engineering"
is the term the field settled on for what `OPERATING.md` describes and the collection uses none of
it. `VOCABULARY.md` exists precisely to grade terms like this one. Grading the field's own headline
term, rather than only the terms in vendor pitches, would make that file matter to somebody outside
the repository.

**Nothing to take from the awesome-lists.** Correctly out of scope, and they are complements: they
are where a stranger would find this, not what they would weigh it against.

---

## 6. What a stranger adopts, and what they never open

Assume a competent engineer with no attachment, who already has `superpowers` or `agent-skills`
installed, thirty minutes, and no reason to be generous.

### Adopted, and would survive contact

- **`ADOPTION.md`, in full.** It is the best-designed thing in the collection. Two phases with a
  forced stop, an explicit refusal to copy a profile from the examples, security before
  documentation, and report-before-changing. Nothing in either comparable clone does this. It is
  1,169 words, it is a prompt rather than a document, and it produces an artifact on first contact.
  **If only one file survives the split, it is this one.**
- **`SKILL.md`, "Verifying a claim", roughly nine bullets.** This is the section with no competitor.
  "Could not confirm and confirmed absent are different results", "do not report an absence without
  stating what you searched for", "do not trust your own paraphrase of a number", "run the thing".
  These are portable beyond this domain, they are stated as prohibitions, and each is traceable to a
  specific failure. A stranger would lift these into their own `AGENTS.md` verbatim.
- **The tier-1 nondeterminism rule and its operational form**, "run each candidate five to ten times
  per task". One rule, one number, four independent groups. It is the collection's single most
  quotable sentence.
- **`SPEC.md` and `HANDOFF.md`.** 817 and 978 words, both prompts, both immediately usable, both
  harness-agnostic. Low ceremony, obvious payoff. A stranger would try these before reading anything
  else.
- **`SECURITY.md`, the thesis paragraph and the third-party-supply-chain section.** "The agent held
  permissions broad enough to make one manipulated instruction consequential, and nothing between the
  instruction and the action was checking" is the best single sentence in the collection. The five
  vetting facts are actionable and the refusal to name products makes them more useful, not less.
- **`EVIDENCE.md`'s errors list**, but read once, as an argument, not as a reference. It is what
  makes a skeptic decide the rest is worth reading. It is also what they will quote at other people.
- **`templates/`.** MIT, drop-in, no obligation travels. Correct licensing decision.

### Opened once, skimmed, not returned to

- **`README.md`.** Does its job. The "Read this before trusting any of it" section is unusual and
  good, and it is also six bullets of self-criticism before the reader knows what the thing is, which
  is a hard sell for a stranger with thirty minutes.
- **`OPERATING.md`.** The orchestrator and worker split, and the finding that review independence
  depends on which lab trained the model rather than who sells the harness, are worth reading. The
  rest is one person's habits, honestly labelled as such. A stranger reads it once for the
  cross-vendor insight and never opens it again.
- **`PROFILE.md`.** Only opened if `ADOPTION.md` sends them there, which it does. Then never again.
  That is correct behaviour for a schema.

### Never opened

- **`EVIDENCE.md` as a working reference.** 19,926 words, an estimated 32,000 tokens. Nobody loads
  this in a session and no agent should. The tier scale and the errors list get read as prose, once.
  The sources section, the contested-between-passes section, the disagreements and the fourteen open
  gaps are archive.
- **`VOCABULARY.md`.** 2,798 words to tell a reader that some words are vague. The file's own header
  says its figures were not verified to primary sources and that the reader should quote
  `EVIDENCE.md` instead. A file that tells you not to quote it will not be opened twice.
- **`OBSERVABILITY.md`.** Genuinely good on the evaluation-versus-observability distinction, and
  `ROADMAP.md` correctly notes it is the one rule file with no file-level sourcing statement. A
  stranger instrumenting an agent workflow will read their vendor's OpenTelemetry docs instead.
- **`TOOLING.md`.** The file is honest that its named products are dated illustrations and that three
  changed status in one quarter. A stranger reading a category map that disclaims its own examples
  will conclude, correctly, that the answer is "read `SECURITY.md`'s five facts", and go do that.
- **`RESEARCH.md`.** Only relevant to somebody making their own work citable. The disclosure-trailer
  table is genuinely well verified and belongs in the evidence document, not in a skill.
- **`WORKFLOW.md`.** The file leads by saying almost nothing in it is measured. That is admirable and
  it is also a reason not to read it, and a stranger will apply exactly that logic.
- **`DOCS.md`.** The rot taxonomy is interesting and the file states, at the top, that a study of
  2,303 context files across 1,925 repositories contradicts part of it. A stranger reads the
  contradiction and stops. **The honesty is right and the placement is self-defeating**: putting the
  strongest objection above the content means the content never gets read. Move the taxonomy to the
  evidence document and keep one rule in the skill.

---

## 7. Publication and reception, candidly

**Is the reputation goal plausible? Yes, but not for this artifact in this shape.**

### The realistic reception of the collection as it stands

A 56,000-word private repository, zero external adoptions, no DOI, entering a field where the leading
comparable has 283,098 stars and the vendor publishes the same advice for free. Posted to the usual
places, the honest forecast is: a small number of readers who admire the errors list, one or two who
say "this is what evidence-based practice should look like", a larger number who say "too long, I
already have superpowers", and no adoption. The prose quality is high enough that it will not be
mocked. It is not differentiated enough, in its current packaging, to be shared.

The specific problem is that **the collection's differentiator is invisible from the outside.** A
reader skimming `SKILL.md` sees a rules file. The thing that makes it unlike every other rules file
is at line 1215 of a 1,700-line companion document. Nobody gets there.

### Who the audience actually is

Not the awesome-list audience, which wants installable things and is served. Three real audiences,
and they want different artifacts:

1. **Engineers who have been burned by an AI-written claim** and want to know what is actually known.
   They want artifact B, the evidence document, and they want it as a web page they can link to.
   This is the largest and most reachable audience.
2. **People writing conventions for a team** who need to justify a rule to a skeptical colleague.
   They want the tier tags and the disagreements. Also artifact B.
3. **Solo and small-team maintainers** who want to install something. They want artifact A, small,
   and they are currently choosing between two artifacts with 283,098 and 92,941 stars.

Audience 1 and 2 are where the reputation is, and they are served by the half that is currently
packaged as an appendix.

### The framing that would land harder, and it is not a rewrite

**Publish one finding first, as a post, before publishing the collection.** The candidate is already
written:

> Nine papers in this collection were rated tier 2, meaning peer-reviewed. An audit against a stricter
> standard, that a venue must be confirmed from a publisher DOI, the venue's own programme or an
> independent index and never from a surface the authors control, moved **four of the nine down to
> tier 4**. One of them had never claimed a venue at all and had been rated on the quality of its
> method. An arXiv `Comments` field saying "accepted at X" is supplied by the submitting author and
> verified by nobody. An arXiv DOI is not a publisher DOI.

That is a finding about **the field's evidence base**, not about the author's repository. It is
checkable by anyone in an afternoon. It implicates every blog post, every rules file and every
vendor page that cites a 2026 preprint as though it were reviewed, which is most of them. It needs no
adoption gate, no 1.0, and no permission. It is the kind of thing that gets quoted back.

Second candidate, and it pairs with the first: **"I graded thirty papers on AI-assisted development
and here is what is actually replicated: one thing."** The tier-1 nondeterminism finding, four
independent groups, temperature zero providing no protection, discounting every other number in the
field including its own. That is a genuinely useful public service and it is a post, not a
repository.

Third, and it is the one that would travel furthest with the least work: **the errors list, published
as a standalone piece about what it is like to keep one.** Twenty-three numbered errors, each with the
rule it produced. Nobody in this space publishes their own mistakes with this specificity. It is the
most distinctive writing in the collection and it is currently reachable only by scrolling.

### On the video content and business visibility goal

The collection is a bad video. The errors list is a good one. "I built a rules file, then checked
every claim in it, and here are the twenty-three ways I was wrong" is a format that works, requires
no adoption, and demonstrates the discipline rather than asserting it.

### The uncomfortable part

**Publication is currently gated on the 1.0 adoption gate, and the gate is correct for the skill and
wrong for the evidence document.** Artifact A genuinely should not ship before a stranger has run
`ADOPTION.md`. Artifact B needs no such gate: a review of published sources is not made more or less
correct by whether anyone installed it. Keeping both behind the same gate is why nothing has been
published in four days of work at this intensity, and it will be why nothing is published in four
weeks. The split unblocks the half that is ready.

---

## 8. Size, measured

Word counts by `wc -w` on 2026-09-08. Token estimates use four characters per token and are
estimates, not measurements.

**This collection's distributable prose: 56,359 words**, measured across the sixteen distributed
markdown files plus `templates/` and `examples/`. Excluding licences. The brief for this evaluation
said roughly 62,000; the difference is accounting, not disagreement.

| File | Words | Estimated tokens |
|---|---|---|
| `EVIDENCE.md` | 19,926 | ~32,300 |
| `SKILL.md` | 6,124 | ~9,600 |
| `DOCS.md` | 3,273 | ~5,100 |
| `VOCABULARY.md` | 2,798 | ~4,600 |
| `PROFILE.md` | 2,691 | ~4,300 |
| `RESEARCH.md` | 2,632 | ~4,500 |
| `SECURITY.md` | 2,474 | ~3,800 |
| `WORKFLOW.md` | 2,167 | ~3,400 |
| `OPERATING.md` | 2,122 | ~3,300 |
| `README.md` | 2,056 | ~3,100 |
| `OBSERVABILITY.md` | 1,616 | ~2,500 |
| `TOOLING.md` | 1,467 | ~2,400 |
| `ADOPTION.md` | 1,169 | ~1,800 |
| `HANDOFF.md` | 978 | ~1,400 |
| `REFRESH.md` | 936 | ~1,400 |
| `SPEC.md` | 817 | ~1,200 |

**Comparables, cloned and measured the same day:**

| Corpus | Markdown files | Total words | Smallest independently loadable unit |
|---|---|---|---|
| `obra/superpowers` | 94 | 167,939 | `skills/` is 39 files, 42,543 words, about 1,100 words per skill |
| `addyosmani/agent-skills` | 95 | 99,435 | 25 `SKILL.md` files, 1,229 to 4,037 words, median about 2,000 |
| `dev-conventions` | 16 plus templates | 56,359 | **`SKILL.md`, 6,124 words**, which is mandatory before any rule applies |

**So the total is not the problem and the entry unit is.** This collection is the smallest of the
three by total corpus, by a factor of three against superpowers. It has the **largest mandatory
first read** of the three, by a factor of three against `agent-skills`' median skill and a factor of
five and a half against superpowers'. Loading `dev-conventions` costs an estimated 9,600 tokens
before a single rule has been applied to anything; loading `agent-skills`' `code-review-and-quality`
costs an estimated 3,000 and does one job.

That is the measured form of the author's own stated worry, quoted in `.agents/goals.md`: "it will
burn tokens very quick when adopting and using it in repositories". The collection answered that
worry with a rule, never `@`-import this from an instruction file, which is correct and does not
address it. **Progressive disclosure was applied between the skill and its companions and was never
applied inside the skill.** Anthropic's own skill-authoring guidance, read 2026-09-08, advises
keeping a `SKILL.md` body under 500 lines and splitting when it approaches that. `SKILL.md` is 605
lines.

**Is 56,000 words defensible?** For an evidence document, yes and it is on the small side: a
systematic review of this scope would be longer. For a skill, no. The number is defensible and the
distribution is not.

---

## 9. Anything now wrong, stale or over-claimed

Spot-checks against what the field publishes as of 2026-09-08. Two of these are real and one of them
is in the agent-facing file.

### 9.1 The repository-overview conflict is stale, and it is in `SKILL.md`

`SKILL.md` states, twice:

> **Do not include a repository or directory overview.** Measured as providing no benefit for file
> discovery, despite being recommended by model vendors.

and, in the conflict section:

> One documented instance: repository overviews are recommended by model vendors and were measured as
> not helping.

**Anthropic's current best-practices page, read in full on 2026-09-08 at
`code.claude.com/docs/en/best-practices`, recommends the opposite.** Its `CLAUDE.md` exclude column
lists, verbatim, "File-by-file descriptions of the codebase" and "Anything Claude can figure out by
reading code". It further states that for a checked-in `CLAUDE.md`, `/doctor` "proposes cuts for
content it can derive from the codebase". The vendor's current published position agrees with the
measurement.

Additionally, and **unverified because the domain is blocked**, a search index reports OpenAI's Codex
guidance as saying to "only store information that Codex cannot infer from the code". If that wording
is real, both major vendors now agree with the measurement.

**Why this matters more than the sentence does.** It is the collection's flagship example of
independent measurement beating vendor advice, it is asserted in the present tense with no date, and
it appears in `SKILL.md`, which loads on every session. That is error 21's exact shape: the file
where a correction is easiest to write is not the file where it matters, inverted. The recheck date
is 2026-09-08, zero days old, and the build passed. **A recheck that is zero days old and did not
open the vendor's own current page is not a recheck of the vendor claims.** `REFRESH.md` should name
the vendor pages as things to open, by URL, not as a category.

The rule itself is fine. The finding that overviews do not help stands. What is stale is the claim
about who disagrees with it.

### 9.2 The live conflict that exists is unrecorded

`SKILL.md` says:

> **Do not stop at isolating the reviewer. Instruct it to disagree.**

on a source that was **demoted from tier 2 to tier 4 on 2026-09-07** because its acceptance rested on
an author-supplied field.

Anthropic's current best-practices page says, verbatim:

> A reviewer prompted to find gaps will usually report some, even when the work is sound, because
> that is what it was asked to do. Chasing every finding leads to over-engineering: extra abstraction
> layers, defensive code, and tests for cases that can't happen. Tell the reviewer to flag only gaps
> that affect correctness or the stated requirements, and treat the rest as optional.

This is a first-party caution that cuts directly against a tier-4 rule the collection elevates and
describes as "the one rule here whose omission actively inverts the outcome". It is not a refutation:
the vendor is warning about over-reporting, the paper is measuring under-reporting, and both can be
true, which is what makes it a good entry for "Disagreements, left standing" with a stated default.
**It is currently in neither the disagreements section nor the conflict section.** The collection has
two stale examples of vendor conflict and zero live ones.

### 9.3 The overlap with vendor guidance is materially larger than `README.md` and `SKILL.md` admit

Both files say the collection is not competing with vendor guidance, and both scope that claim to
**authoring**: "not a guide to writing an instruction file or a skill". That scoping was accurate at
some point and is not accurate against the page as it reads on 2026-09-08. Mapping, from that page:

| `SKILL.md` rule | Current first-party equivalent |
|---|---|
| Do not let an agent review its own work; review from a fresh context | "A fresh context improves code review since Claude won't be biased toward code it just wrote", plus a Writer/Reviewer table and an "Add an adversarial review step" section |
| Do not delegate work whose intermediate results you need; delegate large process, small output | "Since context is your fundamental constraint, use subagents to keep research out of it. When Claude researches a codebase it reads lots of files, all of which consume your context" |
| Do not run a worker agent in your own working tree | "Worktrees: run separate CLI sessions in isolated git checkouts so edits don't collide" |
| Do not stack many workers on one orchestrator; degradation with input length | "LLM performance degrades as context fills", stated as the constraint most best practices derive from |
| Do not put in an auto-loaded file what a linter can enforce | "If Claude already does something correctly without the instruction, delete it or convert it to a hook" |
| Do not include a repository or directory overview | The exclude table, quoted in 9.1 |
| Do not leave a superseded rule in place with an annotation | "Treat CLAUDE.md like code: review it when things go wrong, prune it regularly" |
| Do not only test the happy path; capture the trajectory | Weaker equivalent: "Have Claude show evidence rather than asserting success" |

**Eight of the roughly twenty Layer 1 rules now have a first-party equivalent that is free,
continuously updated and shipped to every user of the harness.** The collection's claim to those
rules is that it grades them and the vendor does not, which is true and is a much narrower claim than
"not competing". The honest sentence is: *the vendors now publish most of the workflow advice too,
better maintained than this can be; what remains here is the strength marking, the profile
conditioning, and the things the vendors have no incentive to say.*

That sentence is more defensible than the current one and it also justifies the cut in section 4.

### 9.4 Smaller items

- **`AGENTS.md`'s 200-character `description` cap.** Anthropic's current skill-authoring page states
  the `description` maximum is **1,024 characters**. The collection's claim is scoped to "the upload
  surface", which may still be true, but it is undated, unattributed to a page, and `build.py`
  enforces it as a hard limit. Date it and name the surface, or verify it. If the cap has been
  raised, the collection is enforcing a constraint that cost it error 11 and no longer exists.
- **The 20-to-200 line-count range.** `SKILL.md` says "published advice ranges from 20 lines to 200".
  A search index reports OpenAI's Codex guidance prescribing 100 lines with a 300-line hard limit.
  **Could not confirm**, domain blocked. If confirmed, the range is understated at the top end. The
  rule, do not chase a line-count target because none of them is measured, is unaffected and if
  anything strengthened.
- **`SKILL.md` is 605 lines** against the vendor's own published guidance of keeping a skill body
  under 500 lines and splitting when approaching it. The collection cites vendor authoring guidance
  as authoritative and does not follow it.
- **`ROADMAP.md` says the repository is "on a code host, private".** Confirmed still private: an
  unauthenticated fetch of its web page returned HTTP 404 on 2026-09-08. Recorded because the
  authenticated code search made it briefly look otherwise, and because that near-miss is the same
  shape as error 10.
- **`DORA` appears nowhere.** Not wrong, but an omission a reader will read as a gap in awareness
  rather than as a judgment. See section 5.
- **Nothing else I checked was wrong.** The administrative-facts section on `AGENTS.md` governance is
  well handled and the "vendor-claimed" labelling of the 60,000-repository figure is exactly right;
  I encountered that same figure repeated as fact by four secondary sources during this research.
  The Borg et al. "Echoes of AI" entry, with its preregistration note, is the best-written source
  entry I have seen in a practitioner document.

---

## 10. The five things I would do next, ordered

**1. Publish the venue audit as a standalone post, this week, before anything else ships.** Four of
nine tier-2 ratings failed a venue check; an arXiv `Comments` field is author-supplied; an arXiv DOI
is not a publisher DOI. It is written, it is checkable, it is about the field rather than about the
repository, it needs no adoption gate, and it is the highest-reputation-per-word thing in the
collection. Everything in goal 3 that is achievable this month is achievable through this.

**2. Do the split, and cut `SKILL.md` to 2,000 to 2,500 words.** Delete every rule with a current
first-party equivalent, replacing the section with one dated line saying where it now lives. Keep the
tier tags, the profile gate, the verification section, and the tier-1 rule. Move `EVIDENCE.md`,
`DOCS.md`'s taxonomy, `VOCABULARY.md`, `RESEARCH.md`, `WORKFLOW.md` and `OBSERVABILITY.md` into the
evidence document. This is a deletion task, not a writing task, and it is the only one on this list
that makes the artifact smaller.

**3. Fix 9.1 and 9.2 in the same commit, and add vendor URLs to `REFRESH.md` by name.** The
repository-overview conflict claim is stale in the agent-facing file. The reviewer-disagreement
conflict is live and unrecorded. Both are quarterly-cadence misses, both are error 21's shape, and
the fix for the class is that `REFRESH.md` must list the specific vendor pages to open, because a
recheck that never opened them is not a recheck of them.

**4. Run `ADOPTION.md` against one repository that is not yours, or hand it to one person, and record
where it broke.** This is item 1 on `ROADMAP.md` and has been for five versions, and I am repeating
it because everything above is a reason it matters more, not less: the split, the cut and the
publication all become easier to get right once one stranger has hit the procedure. **Do not run
another verification pass until this is done.** Seven passes, zero adoptions, and by the collection's
own accounting not one pass has produced a rule. An eighth will produce another errors-list entry and
another changelog entry, and the errors list is already long enough to make its argument.

**5. Fetch three sources by hand, from a browser, in this order: the FORGE 2026 code-health paper,
the AAIF five-run `AGENTS.md` benchmark, and arXiv:2605.11027.** The first is on the question the
collection says nobody has answered. The second is institutional corroboration of its only tier-1
rule, on its weakest topic. The third is the only candidate prior art for the thesis, and if it is
what the index says it is, the differentiation claim in section 3 needs qualifying and the collection
should be the one to qualify it. All three were unreachable from this environment, and the collection
already knows what that means: a blocked network is not a finding.

---

## What I disagree with, collected

Stated separately because agreement is not the deliverable.

- **`README.md` and `SKILL.md`: "this is not competing with them".** Under-claims the overlap by
  roughly eight Layer 1 rules. Section 9.3.
- **`SKILL.md`: repository overviews "recommended by model vendors".** Stale in the present tense
  against the vendor page as of the recheck date. Section 9.1.
- **`AGENTS.md`: "the apparatus is not the deliverable and it has been growing faster than the thing
  it supports".** I agree with the diagnosis and disagree with the implied cure. The document treats
  this as a discipline problem to be solved by a test applied to each proposed change. It is a
  structural problem: the apparatus and the deliverable share a repository, a version and a build, so
  the apparatus is where work is legible. Discipline has been applied for five versions and the ratio
  has not moved. Split them.
- **`ROADMAP.md`: publication is "half done" and sequenced behind the 1.0 gate.** Correct for the
  skill, wrong for the evidence document, and applying one gate to both is why nothing has shipped.
- **`.agents/goals.md`: "publication, credit, reputation: blocked on the 1.0 gate, which is adoption
  by someone else, not more research".** Half right. Adoption gates the skill. The single most
  publishable thing in the collection is a finding about other people's papers and is gated on
  nothing.
- **The framing that `EVIDENCE.md` is the companion and `SKILL.md` is the artifact.** It is the other
  way round. `EVIDENCE.md` is the thing nobody else has. `SKILL.md` is the thing two people have,
  with 283,098 and 92,941 stars respectively.

---

*Written 2026-09-08. Star counts and vendor documentation read the same day and will go stale. Every
figure here is either measured locally with a named command, retrieved from the GitHub REST API, or
read from a named page; where neither, the line says could not confirm.*
