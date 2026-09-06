# Where engineering and research conventions converge

Load when you need to know whether a practice has support from outside software engineering, when
preparing work that a research community will read, or when deciding how to make a practitioner
document citable.

Researched 2026-09-04. Externally verified 2026-09-06.

> **Verified 2026-09-06, and the pass found a real error.** This file previously carried a warning
> that it rested on a single research pass. It has now had an independent verification pass, and the
> warning is replaced with what that pass actually found.
>
> **Confirmed from primary sources**: all four publishers' AI-authorship policies, including that
> IEEE's language explicitly covers code; the NeurIPS and ICML desk-rejection figures; the 640-paper
> badging corpus and its 9.8%; CITATION.cff 1.2.0; CRediT's fourteen roles.
>
> **Contradicted**: the git-trailer convergence claim, which named seven projects as converging on
> one token. Two of them use a different token and the "barring AI from `Co-Authored-By:`" half was
> one project's policy stated as a general rule. Corrected in place below, with per-project
> verification status.
>
> **Still unverified, and named rather than buried**: Fedora and Rocky Linux policies, the
> OpenTelemetry primary document, the Linux kernel's own file, and the citation-difference study.
> Those carry a status column or a withdrawal, and none of them should be cited from this file.

## Why this file exists, and why convergence is the strongest evidence available here

The rest of this collection asks "is this practice measured?" and usually answers "barely". This file
asks a different and cheaper question: **has anyone else independently arrived at the same rule for
their own reasons?**

That matters because most conventions here cannot be measured with the resources anyone actually has.
But when a research community's formal requirements and an engineering community's informal habits
land on the same rule **from different starting points**, that convergence is real evidence about the
rule, even though neither side ran a trial. It is the same logic as the tier-1 replication rule
applied across communities rather than across laboratories.

**And where they conflict, that is more interesting still.** One conflict below is currently
unresolved by anybody, and it is a genuine open problem rather than an oversight.

---

## The strongest convergence: disclose, do not co-author

**Two communities reached an identical rule for an identical legal reason, apparently
independently.** This is the best example in the file.

**Engineering side, corrected 2026-09-06 and the correction matters.** An earlier version of this
paragraph said seven named projects "converged on an `Assisted-by:` trailer" while "specifically
barring AI from `Co-Authored-By:`". A verification pass fetched them individually and **both halves
were overstated**. What each project actually does, with its verification status:

| Project | Trailer | Status |
|---|---|---|
| Linux kernel | `Assisted-by:` | Secondary sources agree; `coding-assistants.rst` not fetched directly |
| Zephyr | attribution trailer, voluntary | **Confirmed** from its own contribution guidelines. AI agents **must not** add `Signed-off-by`, because only a human can certify the DCO |
| Apache Software Foundation | **`Generated-by:`** | **Confirmed** from ASF's own Generative Tooling Guidance |
| OpenInfra | **`Generated-by:`** | **Confirmed**, and its policy credits the ASF for the label |
| OpenTelemetry | `Assisted-by:` style | Secondary only; primary CONTRIBUTING not fetched |
| Fedora, Rocky Linux | unknown | **Not verified.** Only secondary aggregators seen. Do not cite |

**So there is no single converged token.** Two of the seven use a different one, and the two named
foundations that were checked most carefully are the two that diverge. The convergence is on the
*structure*, disclose without claiming authorship, not on the string.

**"Barring AI from `Co-Authored-By:`" is one project's explicit policy, not a cross-foundation
rule.** Mesa states it directly. It is the kernel's practical stance. It is not established
elsewhere and this file previously implied it was general.

Mechanical enforcement is **weaker than previously claimed**. A Claude Code plugin exists that
enforces an `Assisted-by` trailer and blocks non-conforming commits, and Mesa blocks AI in
`Co-Authored-By` by policy. Whether a mainstream commit linter shipped an AI-attribution
configuration in 2026 **could not be verified to a primary source** and is withdrawn.

**One thing did get sharper rather than weaker.** The ASF guidance now notes that under the **EU AI
Act, in force 2 August 2026**, AI-generated *public* text must be labelled. That is a binding legal
regime arriving underneath a set of voluntary conventions, and it is the first item in this file
with actual enforcement behind it.

**Publishing side.** ACM, IEEE, Springer Nature and Elsevier all state that **AI cannot be an
author**, that human authors remain fully accountable, and that substantive generative use must be
disclosed, scaled to how much was used, with copy-editing and grammar checking generally exempt.
IEEE's language explicitly covers **code** as well as text and figures, and requires naming the
system and the sections and level of use.

**The reason both landed in the same place is legal, and it is worth understanding.**
`Co-Authored-By:` is an authorship claim. Under United States copyright law, naming an AI as a
co-author risks attributing rights in the work to the model's vendor. `Assisted-by:` discloses the
assistance **without transferring authorship**. Publisher policy encodes exactly the same structure:
disclosed use is permitted, authorship is not available to a non-human.

- **Do not put an agent in an authorship field.** Not in `Co-Authored-By:`, not in a paper's author
  list. The reason is not etiquette, it is who ends up owning the work.
- **Do not invent a disclosure scheme.** Two independent communities have converged; copy the one
  your ecosystem uses.
- **Do disclose in proportion to use.** Both sides scale the obligation the same way, and both
  exempt trivial assistance like grammar correction.

## Real but partial convergence

### Environment pinning

Engineering keeps lockfiles because builds break otherwise. Research asks for the same thing to make
an artifact runnable: FSE 2026 asks explicitly for a requirements file **with explicit version
information**, and ICSE and ASE require a hardware and software requirements file with containers or
virtual machines preferred and deviations justified.

**But the research requirement is weaker than it looks.** It is bundled into an **opt-in** badge, so
a paper with no pinned environment loses nothing on the paper track itself. The convergence is on the
principle, not on the enforcement.

### Redacting secrets while documenting their shape

This one is a genuinely striking match. ICSE 2026's artifact guidance says proprietary artifacts need
not be included and that **only anonymised data should be shared, with proxies substituted for what
is withheld**. That is structurally identical to the engineering practice of scrubbing credentials
and shipping an example configuration file with the key names and no values.

**Both traditions independently arrived at: redact the sensitive item, document its shape, keep
everything else open.** `SECURITY.md` reaches the same rule from the direction of incidents rather
than ethics review.

### Recording what was and was not verified

**Weaker convergence, and the asymmetry is instructive.** Engineering records this continuously and
cheaply: coverage reports, known-issues sections, build status. Research records it periodically and
manually: limitations sections, and preregistration where it is used.

Engineering's version is automated and therefore actually happens. Research's version is manual and
depends on candour. This collection's own habit of ending a report with "what I did not verify" sits
closer to the engineering side, and that is probably why it survives.

---

## The conflict nobody has resolved: what does "reproducible" mean for an agent?

**This is the most important finding in the file, and the answer is that there is no answer.**

Reproducibility standards assume a computation can be re-run to the same result. The tier-1 finding
in `EVIDENCE.md` is that **agent runs are not deterministic even at temperature 0**. A June 2026
controlled study across two providers, three model tiers and five configurations found some items
**still non-reproducible under forced greedy decoding**, and noted that some newer models have
**deprecated the temperature parameter entirely**, removing even the nominal mitigation. The causes
are structural: floating-point non-associativity, batch-dependent reductions, mixture-of-experts
routing, and provider load balancing.

**Has the artifact-evaluation community addressed this? Confirmed absent, not merely unconfirmed.** A
search across the 2026 artifact-evaluation calls for ICSE, ASE, FSE, ICSA, CGO, PPoPP, CAV and CCS
found **none** mentioning agent nondeterminism, seed variance, or multi-run reporting as a badge
criterion. The reference badging definition predates agent-based artifacts. One 2026 paper on
automating artifact evaluation observes that the badge **"provides limited signal regarding
reproducibility"** even for ordinary code, without addressing agents at all.

The only place it is met head-on is a **non-binding community guideline**, which tells authors to log
full prompts and responses, report model version, configuration and date of execution, and states
plainly that inherent nondeterminism **cannot be an excuse to dismiss verifiability**. That is good
advice with no institutional force behind it.

- **Do not claim an agent pipeline is reproducible.** Nothing currently defines what that would mean.
  Report what you ran, when, with which model version and configuration, and **how many times**.
- **Do report run counts and variance** even though no venue requires it. It is the only honest
  description of an agent measurement, and this collection's own tier-1 entry is the reason.
- **Do not let a badge stand in for reproducibility.** Even its automation researchers say it does
  not carry that signal.

---

## Artifact evaluation, and the honest picture of what a badge buys

The reference scheme has three main levels: **Available** (deposited in an archival repository,
where a code-hosting URL alone is **explicitly insufficient**), **Evaluated-Functional**, and
**Evaluated-Reusable**, which subsumes Functional, with only one of the two ever awarded. Some venues
add Results Reproduced or Replicated. Adoption is **per-community rather than central**, and
**opt-in almost everywhere**.

**What a badge is worth, stated bluntly.** A 2025 corpus of 640 papers in this field found **9.8%
badged**, and treated badges as **associational rather than causal**, noting they often signal that
an artifact exists without guaranteeing execution fidelity or long-term reproducibility. A separate
citation study reported a statistically significant citation difference for only a small number of
venue-year pairs after correcting for multiple comparisons, and null everywhere else. **The study
itself was not located by the 2026-09-06 verification pass**, so the direction stands and the exact
count is withdrawn until somebody reaches the primary source.

One vendor-neutral asymmetry worth knowing: IEEE-native badging is rare. In that same 640-paper
corpus, **two papers** used it, both with the weakest badge only.

## Disclosure policy, including where it has teeth

No major publisher bans AI-assisted writing outright: **confirmed absent**. But enforcement exists at
the margins and it is sharper than most people expect:

- One 2026 conference prohibits LLM-generated text specifically, exempting formatting and grammar.
- One major venue's position track in 2026 required papers be **substantially human-written** and
  desk-rejected **178 of 969 submissions**, 18.4%, with a further 12.7% asked for evidence.
- Two major machine-learning venues each rejected roughly **2% of submissions**, around 500 papers
  apiece, by catching **AI-generated peer reviews** using prompt-injection traps planted in
  submissions.

That last one is the item to notice. **The enforcement effort is going into reviewing, not writing**,
because an AI-generated review is a failure of the process itself rather than of one paper.

**Self-interest flag, since this collection insists on them.** Publisher no-AI-authorship rules also
protect each publisher's copyright and liability chain: someone must be legally accountable and able
to assign rights. The rule is defensible on its merits and it is not disinterested. And disclosure is
author-self-reported and largely unverified.

## Preregistration

Registered reports run at MSR, ICSME with a partner journal, and the empirical-methods venues, using
a two-stage model where a stage-one acceptance does not appear in the proceedings and the full paper
goes to the journal.

**Adoption is real and small**: single-digit papers per year per venue in the programmes observed.
And on whether it works in this field: **could not confirm.** No software-engineering-specific study
of whether registered reports reduce questionable research practices was found. Cross-disciplinary
evidence exists from psychology and neuroscience, where registered reports rate higher on rigour and
report positive results far less often, which is the signal you would expect if they are working.

## Making a practitioner document citable

**This part is mature, adoptable today, and has zero proposal-stage risk.** Two pieces:

1. **A `CITATION.cff` file**, version 1.2.0, YAML, with title, authors, version and a DOI field. It
   is rendered natively by major code hosts and parsed by archival repositories and reference
   managers.
2. **Tagged releases connected to an archival repository**, which mints a **concept DOI covering all
   versions plus a version-specific DOI per release**. That satisfies the same "archival repository,
   not a code host" bar that artifact-evaluation tracks apply to their Available badge.

Together those make a non-academic document **citable and version-pinnable in a form a researcher
will accept**, which is exactly what this collection's own versioning rule asks consumers to do.

**What is not ready, stated bluntly so nobody waits for it:**

- **Contributor-role taxonomies do not cover AI.** The established 14-role standard explicitly
  excludes AI systems. An extension was proposed in a 2026 commentary; **institutional adoption is
  zero**.
- **A faceted attribution scheme** for AI-assisted text was proposed in 2026 and is **unadopted**.
- **Content provenance standards** are mature and regulator-referenced, but the adoption evidence is
  camera, image and video. **No use for citing text or code provenance in academic documents was
  confirmed.**

## The verdict, in three buckets

**Enforced.** No AI authorship, plus disclosure of substantive use, at all four major publishers,
mirrored independently by the `Assisted-by:` trailer in engineering. Archival deposit wherever an
Available badge is claimed. AI-generated peer review actively policed and rejected at two major
venues.

**Encouraged but optional.** Artifact evaluation and badging generally. Environment pinning, which is
required only inside an opt-in badge. Data-availability statements outside two journals. Registered
reports. The community guideline on reporting model version, configuration and date.

**Proposals with no adoption, bluntly.** Any AI-inclusive contributor-role taxonomy. Faceted AI
attribution. Content-provenance standards for academic text. **And any badge criterion or venue
policy defining what "reproducible" means for an agent-run artifact: this does not exist.**
