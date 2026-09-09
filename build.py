#!/usr/bin/env python3
"""Build a distributable of the dev-conventions skill.

Produces two artifacts in dist/:

  dev-conventions-<version>.zip   the skill nested as dev-conventions/, ready to
                                  drop into a skills directory or upload
  dev-conventions-<version>.json  every file as one JSON object, for the
                                  one-command install described in ADOPTION.md

Excludes the files that develop the collection rather than being part of it, and
verifies the things that have actually broken before. Run it with no arguments.
"""

import json
import os
import re
import subprocess
import sys
import zipfile
from pathlib import Path

ROOT = Path(__file__).parent.resolve()
DIST = ROOT / "dist"

# Files that develop the collection but are not part of it.
EXCLUDE_FILES = {
    "LOCAL.md",       # machine paths and personal toolchain, never distributed
    "AGENTS.md",      # how to edit the collection, not part of it
    "CLAUDE.md",      # a pointer to AGENTS.md for harnesses that look for this name
    "ROADMAP.md",     # what is open here, not a convention
    "build.py",
    "CITATION.cff",   # belongs to the repository, not the skill
    "CONTRIBUTING.md",      # how to contribute here, not a convention
    "CODE_OF_CONDUCT.md",   # governs this repository, not a consumer's
    "CHANGELOG.md",   # see below
    "sources.yml",    # what the drift watcher tracks; governs this repo
    "scripts/watch_sources.py",
    ".gitignore",
}
# CHANGELOG.md was excluded on 2026-09-08, on the same logic as ROADMAP.md and
# CONTRIBUTING.md: it governs this repository rather than a consumer's. It had
# grown to roughly 40 minutes of reading, 15% of the distributable, none of it
# telling a consumer what to do. It stays in the repository and on the code host,
# where anyone comparing two versions will look for it, and README.md points
# there. The version line in SKILL.md is what a consumer needs, and the citation
# message already says to cite the version you read.
# Matched anywhere in the tree, by basename. Deliberately tiny: this is the
# mechanism that removed templates/AGENTS.md from every distributable at 0.14.0,
# because the root AGENTS.md was excluded and the match was on the file name.
# LOCAL.md earns it because it can legitimately sit in a subdirectory and must
# never ship from any of them. Nothing else does. Error 26.
EXCLUDE_ANYWHERE = {"LOCAL.md"}

EXCLUDE_DIRS = {".git", "dist", ".agents", "__pycache__", ".claude-plugin", ".github",
                "evidence", "scripts"}
# In a git worktree, .git is a FILE rather than a directory, so filtering it as a
# directory name alone ships it. Excluded by basename in collect() as well.
# evidence/ is the split, made 2026-09-08. It holds the apparatus: the tier scale,
# every source, the disagreements, the open gaps, the errors list, and the
# reference files that are read once by a human rather than loaded by an agent.
# It builds as its own artifact, dev-conventions-evidence-<version>.md, and it is
# the thing that gets a DOI. The skill ships without it.
#
# The reason is measured rather than aesthetic: the skill's mandatory first read
# was three to five times the median independently loadable unit in the two most
# widely used comparable collections, and the apparatus was 44% of what a
# consumer installed while telling them nothing about what to do.
# .github holds this repository's vulnerability-disclosure policy, which is a
# different document from the root SECURITY.md despite the near-identical name.
# The root one is skill content and ships. This one governs reporting here.
# .claude-plugin holds the marketplace and plugin manifests. Those describe how
# the REPOSITORY offers the skill, not the skill itself, so they belong with
# CITATION.cff and build.py rather than in the distributable. They also carry an
# owner handle, which the identifier-leak check is right to reject in skill prose.

# Reading order for the JSON bundle, so an unpacked copy reads sensibly.
ORDER = [
    "README.md", "ADOPTION.md", "SKILL.md", "PROFILE.md", "SECURITY.md",
    "SPEC.md", "HANDOFF.md", "REFRESH.md", "OPERATING.md", "LICENSE",
]

# The evidence document, built as one file in this order. Read once by a human,
# not loaded by an agent. EVIDENCE.md leads because the tier scale has to be read
# before anything graded by it means anything.
EVIDENCE_ORDER = ["EVIDENCE.md", "RESEARCH.md", "VOCABULARY.md"]
# Corrected 0.14.1. The 0.14.0 split put four rule files in here on a long-versus-
# short reading and removed 47 prohibitions and 8,523 words from what a consumer
# installs. The boundary is APPARATUS versus RULES: sources, gaps, disagreements
# and the errors list are apparatus; anything telling an engineer what to do
# ships. WORKFLOW.md, OBSERVABILITY.md, DOCS.md and TOOLING.md are back at root.

FAILURES = []

# Names that must not appear in anything distributed, in file contents OR in
# commit metadata. The second half is error 17: this regex passed over every
# shipped file while the employer address sat in the author and committer field
# of every commit, which is not file content and so was never examined.
LEAK = re.compile(r"REDACTED-EMPLOYER|REDACTED-PROJECT-A|Natanael|Fejes|Feješ", re.I)

# Commit metadata is checked against a NARROWER pattern, and the difference is
# deliberate rather than an oversight. Skill prose must name nobody, the author
# included. Commit metadata must name the author, because that is the ownership
# record and an unattributed history is worth less than an attributed one. What
# must never appear there is the employer, in any of the forms it takes on a
# machine provisioned by one: the domain, the company name, the account handle.
EMPLOYER = re.compile(r"REDACTED-EMPLOYER|REDACTED-PROJECT-A|REDACTED-USER", re.I)


def fail(msg):
    FAILURES.append(msg)
    print(f"  FAIL  {msg}")


def ok(msg):
    print(f"  ok    {msg}")


def collect():
    """Every file that ships, relative to the repo root."""
    files = []
    for dirpath, dirnames, filenames in os.walk(ROOT):
        dirnames[:] = [d for d in dirnames if d not in EXCLUDE_DIRS]
        for name in filenames:
            if name == ".git":      # a file, not a directory, inside a worktree
                continue
            rel = Path(dirpath, name).relative_to(ROOT).as_posix()
            if rel in EXCLUDE_FILES or Path(rel).name in EXCLUDE_ANYWHERE:
                continue
            files.append(rel)
    # ordered files first, then the rest sorted, so templates/ and examples/ follow
    rest = sorted(f for f in files if f not in ORDER)
    return [f for f in ORDER if f in files] + rest


def read_version():
    text = (ROOT / "SKILL.md").read_text(encoding="utf-8")
    m = re.search(r"\*\*Version (\d+\.\d+\.\d+)\.", text)
    if not m:
        fail("no version string found in SKILL.md")
        return "0.0.0"
    return m.group(1)


def check_frontmatter():
    """Error 11: the description broke while every other check passed."""
    text = (ROOT / "SKILL.md").read_text(encoding="utf-8")
    parts = text.split("---")
    if len(parts) < 3:
        fail("SKILL.md has no YAML frontmatter")
        return
    fm = parts[1]
    fields = {}
    for line in fm.strip().splitlines():
        key, sep, value = line.partition(": ")
        if sep:
            fields[key.strip()] = value
    if "name" not in fields or "description" not in fields:
        fail("frontmatter missing name or description")
        return
    desc = fields["description"]
    if ": " in desc:
        fail("description contains a colon followed by a space, which a YAML plain scalar cannot hold")
    else:
        ok("description is a valid plain scalar")
    # 1,024 is the documented limit, from Anthropic's skill-authoring guidance,
    # read 2026-09-08. This check enforced 200 for a week, on a figure asserted in
    # AGENTS.md with no source. It was wrong by a factor of five and it starved the
    # only field that decides whether the skill loads. Error 24. The check now also
    # warns when the description is short, because under-using the budget is the
    # failure that actually happened and a cap alone cannot catch it.
    CAP, THIN = 1024, 400
    if len(desc) > CAP:
        fail(f"description is {len(desc)} characters, documented cap is {CAP}")
    elif len(desc) < THIN:
        print(f"  WARN  description is {len(desc)} of {CAP} characters. It is the only "
              f"triggering signal the model gets, and this field was starved for a week "
              f"by a cap that was never true. Name the contexts, not just the topics.")
    else:
        ok(f"description is {len(desc)} of {CAP} characters")
    allowed = {"name", "description", "license", "compatibility", "metadata", "allowed-tools"}
    extra = set(fields) - allowed
    if extra:
        fail(f"frontmatter carries fields the spec rejects: {sorted(extra)}")
    else:
        ok("frontmatter carries only accepted fields")


def check_staleness():
    """A cadence nobody enforces is a promise, not a mechanism.

    SKILL.md says a stale entry counts as a defect rather than as background.
    That was true of everybody else's documents and not of this one, because
    nothing checked it. Warn at 90 days, fail at 180.
    """
    import datetime
    text = (ROOT / "SKILL.md").read_text(encoding="utf-8")
    m = re.search(r"External claims last rechecked (\d{4})-(\d{2})-(\d{2})", text)
    if not m:
        fail("no recheck date in SKILL.md, so staleness could NOT be checked")
        return
    checked = datetime.date(*map(int, m.groups()))
    age = (datetime.date.today() - checked).days
    if age >= 180:
        fail(f"external claims last rechecked {checked}, {age} days ago. Run REFRESH.md")
    elif age >= 90:
        print(f"  WARN  external claims are {age} days old (rechecked {checked}). "
              f"Quarterly refresh is due; build fails at 180.")
    else:
        ok(f"external claims rechecked {checked}, {age} days ago")


def check_prose(files):
    """The two content rules, plus a link check that reports its count."""
    md = [f for f in files if f.endswith((".md", ".yml", ".yaml")) or "/" in f]
    dashes = [f for f in md if "—" in (ROOT / f).read_text(encoding="utf-8", errors="ignore")]
    if dashes:
        fail(f"em dashes present in: {dashes}")
    else:
        ok(f"no em dashes across {len(md)} files")

    leaks = []
    for f in md:
        for i, line in enumerate((ROOT / f).read_text(encoding="utf-8", errors="ignore").splitlines(), 1):
            if LEAK.search(line):
                leaks.append(f"{f}:{i}")
    if leaks:
        fail(f"identifier leaks: {leaks[:5]}")
    else:
        # Say what was measured, not "no errors". This check reported clean for a
        # day while the employer address sat in every commit header, because its
        # scope was file contents and nobody said so. Error 17.
        ok(f"no identifier leaks in {len(md)} files (contents only, see the metadata check)")

    # cross-references, resolved against WHAT SHIPS rather than what is on disk.
    #
    # Until 0.14.1 this resolved against the working tree, so a file that stopped
    # shipping still resolved and the check stayed green. At 0.14.0 that let ten
    # shipped files reference documents a consumer does not receive. It is row
    # three of the boundary table, the distributable against the repository,
    # recurring for the seventh time, in the release made to fix the split.
    # Error 26. The question a consumer needs answered is whether the reference
    # resolves IN THEIR COPY, so that is the only set consulted.
    external = {
        "CLAUDE.md", "GEMINI.md", "skills.md", ".agents/profile.yml",
        "dev-conventions/SKILL.md", "requirements.txt", "ADR-NNN.md",
        "ADR-NNN-kebab-case-title.md", "LOCAL.md", "AGENTS.md", "ROADMAP.md",
        "setup.yml",   # the user's own resolved-stack file, produced by SETUP.md
                       # and living in their home directory, not in this repository
        "CHANGELOG.md",   # in the repository and not in the distributable, on
                          # purpose. README.md says where to read it.
        "EVIDENCE.md", "RESEARCH.md", "VOCABULARY.md",   # the evidence document,
                          # built separately. Named in shipped prose deliberately.
    }
    shipped = {Path(f).name for f in files} | set(files)
    refs = set()
    pattern = re.compile(r"`([A-Za-z_./-]+\.(?:md|yml))`")
    for f in md:
        refs.update(pattern.findall((ROOT / f).read_text(encoding="utf-8", errors="ignore")))
    missing = sorted(r for r in refs if r not in external and r not in shipped)
    if missing:
        fail(f"shipped files reference documents that do not ship: {missing}")
    else:
        ok(f"{len(refs)} cross-references examined against the {len(files)} shipped files, "
           f"all resolve in a consumer's copy")

    # The templates are the most-copied thing here and the least noticed when one
    # goes missing: every local check passed at 0.14.0 while templates/AGENTS.md
    # was absent from every distributable. A count is the cheapest instrument that
    # would have caught it, and it is asserted rather than reported.
    on_disk = sorted(p.name for p in (ROOT / "templates").iterdir() if p.is_file())
    shipped_templates = sorted(Path(f).name for f in files if f.startswith("templates/"))
    if shipped_templates != on_disk:
        missing_t = sorted(set(on_disk) - set(shipped_templates))
        fail(f"{len(on_disk)} templates on disk, {len(shipped_templates)} ship. "
             f"Not shipping: {missing_t}")
    else:
        ok(f"all {len(on_disk)} templates ship: {', '.join(on_disk)}")


ARXIV = re.compile(r"arXiv:\d{4}\.\d{4,5}")
# A DOI that is not the arXiv one. Every preprint has 10.48550/arXiv.NNNN.NNNNN
# and its existence says only that the preprint exists, so it is excluded here
# deliberately: treating it as a publisher DOI is how error 20 nearly recurred a
# third time on a different paper.
PUBLISHER_DOI = re.compile(r"\b10\.(?!48550)\d{4,9}/[^\s`)\]]+")
# The scale accepts three confirmation routes, not one: a publisher DOI, the
# venue's own programme or proceedings, or an independent index. The first
# version of this check counted only DOIs, so it fired on three entries that
# were correctly confirmed against OpenReview and two conference programmes.
# A check that encodes a narrower rule than the document states is error 9's
# shape pointing the other way: it fails work that is right.
CONFIRMED_AGAINST = re.compile(r"onfirmed\s+\d{4}-\d{2}-\d{2}\s+against", re.I)
RECORD_WINDOW = 14   # lines after a paper's first mention in which its record must appear


def check_venue_confirmation():
    """Error 20: tier 2 was awarded on surfaces the papers' own authors control.

    Tier 2 means peer-reviewed and accepted, confirmed against the venue or a
    publisher DOI. An arXiv Comments field, and a conference banner a paper sets
    in its own typesetting, are written by the authors and checked by nobody.

    What this measures, stated because a check must report its boundary: for
    every distinct arXiv identifier in the Tier 2 section, whether a record token
    appears within RECORD_WINDOW lines of its first mention. A record token is a
    non-arXiv DOI or a "confirmed <date> against" phrase. It is a proximity test
    over prose, so it cannot tell which record belongs to which paper, and it
    will miss a record written far from its claim.

    It WARNS rather than fails, deliberately: a failing build here would be fixed
    by deleting the check.
    """
    text = (ROOT / "evidence" / "EVIDENCE.md").read_text(encoding="utf-8")
    sections = re.split(r"^### Tier (\d)[^\n]*$", text, flags=re.M)
    tier2 = "".join(sections[i + 1] for i in range(1, len(sections), 2)
                    if sections[i] == "2")
    if not tier2:
        fail("no Tier 2 section found in EVIDENCE.md, so venue confirmation was NOT checked")
        return

    # Blockquoted lines are asides: contesting sources, adjudications, caveats.
    # A preprint named in one is being discussed, not tiered, so it must not be
    # counted as a tier-2 paper. Blanked rather than dropped so line offsets, and
    # therefore the proximity window, stay aligned with the section.
    lines = ["" if l.lstrip().startswith(">") else l for l in tier2.splitlines()]
    # An entry opening with the relocation marker points at a paper that has been
    # moved OUT of this tier. The marker is a fixed phrase, documented in
    # AGENTS.md, so a reworded pointer cannot silently leave the check.
    moved = set()
    for i, line in enumerate(lines):
        if line.startswith("**Moved out of this tier"):
            for j in range(i, min(i + 6, len(lines))):
                moved.update(ARXIV.findall(lines[j]))

    seen, unconfirmed = set(), []
    for i, line in enumerate(lines):
        for pid in ARXIV.findall(line):
            if pid in seen or pid in moved:
                continue
            seen.add(pid)
            window = "\n".join(lines[i:i + RECORD_WINDOW])
            if not (PUBLISHER_DOI.search(window) or CONFIRMED_AGAINST.search(window)):
                unconfirmed.append(pid)
    if unconfirmed:
        print(f"  WARN  {len(unconfirmed)} of {len(seen)} tier-2 papers cite no venue record "
              f"within {RECORD_WINDOW} lines of first mention: {', '.join(unconfirmed)}. "
              f"A venue named in prose is the author's claim until a record is cited.")
    else:
        ok(f"{len(seen)} tier-2 papers, each citing a venue record "
           f"(publisher DOI, programme or index) within {RECORD_WINDOW} lines")


def check_metadata():
    """Error 17: the leak lived in commit headers, which no check read.

    Scope is every ref, not the current branch. The first fix for error 17 was
    verified on one branch while the address remained published on another.
    """
    fmt = "--format=%H%x00%an %ae%x00%cn %ce%x00%B%x00%x00"
    try:
        out = subprocess.run(
            ["git", "log", "--all", fmt],
            cwd=ROOT, capture_output=True, text=True, encoding="utf-8", errors="ignore",
        )
    except FileNotFoundError:
        fail("git not on PATH, so commit metadata was NOT checked")
        return
    if out.returncode != 0:
        fail(f"git log failed, so commit metadata was NOT checked: {out.stderr.strip()[:120]}")
        return

    commits = [c for c in out.stdout.split("\x00\x00") if c.strip()]
    if not commits:
        # A check that passes by finding nothing to check is error 9, and this
        # one would otherwise pass in a directory that is not a repository.
        fail("no commits found, so the metadata check measured nothing")
        return

    hits = []
    for c in commits:
        parts = c.split("\x00")
        sha = parts[0].strip()[:8]
        for field, text in zip(("author", "committer", "message"), parts[1:4]):
            if EMPLOYER.search(text or ""):
                hits.append(f"{sha} {field}")

    refs = subprocess.run(
        ["git", "for-each-ref", "--format=%(refname)"],
        cwd=ROOT, capture_output=True, text=True,
    ).stdout.split()

    if hits:
        fail(f"employer identifiers in commit metadata: {sorted(set(hits))[:5]} ({len(hits)} total)")
    else:
        ok(f"no employer identifiers across {len(commits)} commits on {len(refs)} refs")


def main():
    print("Checking before building.\n")
    version = read_version()
    files = collect()
    check_frontmatter()
    check_prose(files)
    check_metadata()
    check_venue_confirmation()
    check_staleness()

    if FAILURES:
        print(f"\n{len(FAILURES)} check(s) failed. Nothing built.")
        return 1

    DIST.mkdir(exist_ok=True)
    zip_path = DIST / f"dev-conventions-{version}.zip"
    with zipfile.ZipFile(zip_path, "w", zipfile.ZIP_DEFLATED) as z:
        for rel in files:
            # nested folder, not files at the archive root, or upload is rejected
            z.write(ROOT / rel, arcname=f"dev-conventions/{rel}")

    bundle = {rel: (ROOT / rel).read_text(encoding="utf-8") for rel in files}
    json_path = DIST / f"dev-conventions-{version}.json"
    json_path.write_text(json.dumps(bundle, indent=2), encoding="utf-8")

    # Artifact B: the evidence document, one file, for a human to read and cite.
    ev_parts = [
        f"# dev-conventions: the evidence\n",
        f"**Version {version}.** The apparatus behind the `dev-conventions` skill: the tier scale,",
        "every source, the disagreements left standing, the open gaps, and this document's own",
        "numbered errors.\n",
        "**This is not the skill.** The skill is a separate, much smaller artifact that an agent",
        "loads. This is the record a human reads once, argues with, and cites. They were one",
        "artifact until 2026-09-08 and splitting them is recorded in `CHANGELOG.md`.\n",
        "**Cite the version.** A claim corrected between versions is otherwise indistinguishable",
        "from one that still holds, which is the same reason the skill carries a version line.\n",
        "---\n",
    ]
    for rel in EVIDENCE_ORDER:
        src = ROOT / "evidence" / rel
        if not src.exists():
            fail(f"evidence file missing, so the evidence document was NOT built: {rel}")
            return 1
        ev_parts.append(src.read_text(encoding="utf-8").rstrip() + "\n\n---\n")
    ev_path = DIST / f"dev-conventions-evidence-{version}.md"
    ev_path.write_text("\n".join(ev_parts), encoding="utf-8")

    print(f"\nBuilt version {version}, {len(files)} files.")
    print(f"  {zip_path.relative_to(ROOT)}  {zip_path.stat().st_size / 1024:.1f} KB")
    print(f"  {json_path.relative_to(ROOT)}  {json_path.stat().st_size / 1024:.1f} KB")
    ev_words = len(ev_path.read_text(encoding="utf-8").split())
    print(f"  {ev_path.relative_to(ROOT)}  {ev_path.stat().st_size / 1024:.1f} KB, "
          f"{ev_words:,} words, {len(EVIDENCE_ORDER)} sections")
    excluded = sorted(EXCLUDE_FILES) + sorted(f"{d}/" for d in EXCLUDE_DIRS if d != ".git")
    print("\nExcluded from the distributable: " + ", ".join(excluded))
    return 0


if __name__ == "__main__":
    sys.exit(main())
