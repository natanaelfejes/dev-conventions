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

import hashlib
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

# The identifier patterns are NOT in this file. They live in a gitignored file
# read at runtime, because until 2026-09-10 they sat here in plaintext, in a
# script that is published and that the leak check never scanned: the check's
# scope was the 28 files that ship, and this one does not. Publishing the list
# of strings you consider sensitive is worse than one mention of one, because
# it hands a reader the index of everything you scrubbed. Error 29.
PATTERNS_FILE = ROOT / ".agents" / "leak-patterns.txt"
PATTERNS_EXAMPLE = ROOT / ".agents" / "leak-patterns.txt.example"

# Three scopes, each stated, because a check that does not report its boundary
# is this repository's most repeated defect:
#   forbidden_everywhere        every tracked file, this script included
#   forbidden_in_shipped_prose  the shipped prose only. The repository is
#                               published under the author's name and its own
#                               URL carries his account handle, so a repo-wide
#                               ban on it is unsatisfiable rather than strict.
#   forbidden_in_commit_metadata  commit author and committer, every ref. Error 17.
SCOPES = ("forbidden_everywhere", "forbidden_in_shipped_prose", "forbidden_in_commit_metadata")


def load_patterns():
    """Absent or malformed means STOP, never a quiet pass. A build that silently
    skips its leak check is worse than one with no leak check, because it reports
    green. Error 29."""
    if not PATTERNS_FILE.exists():
        sys.exit(
            f"\n  STOP  {PATTERNS_FILE.relative_to(ROOT)} is missing, so nothing is being\n"
            f"        checked for identifier leaks. This is a hard stop and not a warning.\n\n"
            f"        cp {PATTERNS_EXAMPLE.relative_to(ROOT)} {PATTERNS_FILE.relative_to(ROOT)}\n\n"
            f"        then put your real identifiers in it. It is gitignored.\n")
    groups, current = {s: [] for s in SCOPES}, None
    for raw in PATTERNS_FILE.read_text(encoding="utf-8").splitlines():
        line = raw.strip()
        if not line or line.startswith("#"):
            continue
        if line.startswith("[") and line.endswith("]"):
            current = line[1:-1]
            if current not in SCOPES:
                sys.exit(f"\n  STOP  unknown section [{current}] in {PATTERNS_FILE.name}. "
                         f"Known sections: {', '.join(SCOPES)}\n")
            continue
        if current is None:
            sys.exit(f"\n  STOP  pattern before any [section] in {PATTERNS_FILE.name}\n")
        groups[current].append(line)
    empty = [s for s in SCOPES if not groups[s]]
    if empty:
        sys.exit(f"\n  STOP  these sections of {PATTERNS_FILE.name} are empty, so they check\n"
                 f"        nothing: {empty}. An empty pattern list passes everything.\n")
    return {s: re.compile("|".join(re.escape(p) for p in groups[s]), re.I) for s in SCOPES}


PATTERNS = load_patterns()
EVERYWHERE = PATTERNS["forbidden_everywhere"]
LEAK = PATTERNS["forbidden_in_shipped_prose"]
EMPLOYER = PATTERNS["forbidden_in_commit_metadata"]


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
        fail(f"author-name leaks in shipped prose: {leaks[:5]}")
    else:
        # Say what was measured, not "no errors". This check reported clean for a
        # day while the employer address sat in every commit header, because its
        # scope was file contents and nobody said so. Error 17.
        ok(f"no author-name leaks in {len(md)} shipped prose files (contents only, "
           f"see the metadata check)")

    # The employer, customer and private-project patterns are checked against
    # EVERY TRACKED FILE, not the 28 that ship.
    #
    # Until 2026-09-10 this ran only over the shipped set, so build.py, AGENTS.md
    # and CLAUDE.md were never examined, and build.py was the file carrying the
    # patterns in plaintext. The instrument was the leak. Ninth instance of the
    # boundary table and the first where the check itself is what it was looking
    # for. Error 29. The repository is public, so the scope that matters is what
    # is published, and everything tracked is published.
    tracked = subprocess.run(["git", "ls-files"], cwd=ROOT, capture_output=True,
                             text=True).stdout.split()
    scanned, found = 0, []
    for f in tracked:
        # The example patterns file is the one tracked file that must contain
        # pattern-shaped strings, because that is what it is for. A new adopter
        # copies it to seed the check, the placeholders become the live patterns,
        # and the scan then matches them inside the example itself: five hits on
        # the very first build, before anyone has done anything wrong. Found by
        # running the adoption. Excluded here, and PROTECTED INSTEAD by
        # check_example_placeholders, so the exclusion is not a hole a real
        # identifier can be parked in.
        if f == PATTERNS_EXAMPLE.relative_to(ROOT).as_posix():
            continue
        fp = ROOT / f
        if not fp.is_file():
            continue
        try:
            text = fp.read_text(encoding="utf-8")
        except (UnicodeDecodeError, OSError):
            continue
        scanned += 1
        for i, line in enumerate(text.splitlines(), 1):
            if EVERYWHERE.search(line):
                found.append(f"{f}:{i}")
    if found:
        fail(f"employer or project identifiers in tracked files: {found[:5]}")
    else:
        ok(f"no employer or project identifiers across {scanned} tracked files "
           f"(every tracked file except the example patterns file, which is "
           f"checked separately, and this build script included)")

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


SELECTOR = re.compile(r"`([a-z_]+):\s*([A-Za-z0-9_-]+)`")
ENUM_LINE = re.compile(r"^([a-z_]+):\s*\S+\s+#\s*(.+\|.+)$", re.M)


def content_digest(path):
    """Hash CONTENT, not working-tree bytes.

    `core.autocrlf=true` is the Windows default, so a fresh clone there gets CRLF
    and a byte digest of the same file differs from the same file on Linux. This
    was written on Linux, passed on Linux, and would have failed the very first
    build of every Windows user who cloned the repository on the day it went
    public, telling them a file had changed when nothing had. Tenth instance of
    the boundary family: the check measured the bytes on disk and what mattered
    was the content."""
    return hashlib.sha256(path.read_bytes().replace(b"\r\n", b"\n")).hexdigest()


# The example patterns file is pinned by DIGEST rather than by listing what it
# may contain. The first version of this check held an allowlist of the
# placeholder strings, which put a list of pattern-shaped strings back into
# build.py: the exact defect error 29 had just moved out of it, reintroduced by
# its own fix, and caught only because a fresh-adopter test failed on
# build.py's own line. A hash cannot match a pattern and discloses nothing.
#
# Editing the example is fine and requires updating this digest, deliberately.
EXAMPLE_SHA256 = "74ed4ed9428c38fc780928da6bae81cae714f756cd209bf5dd10d631b1632df4"


# Exhaustive. Anything shipped that is not matched here is CC BY, which is the
# attribution-covered default. Inverted 2026-09-10: the fallback used to be MIT,
# and an enumerated CC BY list had gone stale by seven prose files.
MIT_PREFIXES = ("templates/", "examples/", ".claude-plugin/")
MIT_FILES = {"build.py", "LICENSE", "LICENSE-DOCS"}


def check_licence_cover(files):
    """Every shipped file under exactly one licence, and both licence files present.

    A collection whose argument is that claims should be traceable to who made
    them and when cannot leave its own attribution terms to a hand-maintained
    list. That list under-covered seven prose files, including both layer rule
    sets, which silently made them MIT and dropped the attribution requirement
    nobody had decided to drop."""
    mit, ccby = [], []
    for f in files:
        (mit if f.startswith(MIT_PREFIXES) or f in MIT_FILES else ccby).append(f)
    if not mit or not ccby:
        fail(f"licence split degenerate: {len(mit)} MIT, {len(ccby)} CC BY. One side empty "
             f"means the rule matched everything or nothing and checked neither")
        return
    for name in ("LICENSE", "LICENSE-DOCS"):
        if name not in files:
            fail(f"{name} does not ship, so a consumer receives the files and not the terms")
            return
    # the prose licence must state the default rather than enumerate, or it rots again
    doc = (ROOT / "LICENSE-DOCS").read_text(encoding="utf-8")
    if "EVERY .md file" not in doc:
        fail("LICENSE-DOCS no longer states coverage as a default. An enumerated list "
             "silently under-covers every file added after it was written")
        return
    ok(f"{len(files)} shipped files covered by exactly one licence, {len(ccby)} CC BY and "
       f"{len(mit)} MIT, coverage stated as a default rather than a list")


def check_example_placeholders():
    """The example file is excluded from the repository-wide leak scan, because a
    new adopter copies it to seed the check and its placeholders then match
    themselves. This is what makes that exclusion safe rather than a hole: any
    edit at all, a real identifier pasted in most of all, stops the build."""
    if not PATTERNS_EXAMPLE.exists():
        fail(f"{PATTERNS_EXAMPLE.name} is missing, so a fresh clone cannot seed the leak check")
        return
    actual = content_digest(PATTERNS_EXAMPLE)
    if actual != EXAMPLE_SHA256:
        fail(f"{PATTERNS_EXAMPLE.name} has changed. It is excluded from the leak scan, so it is "
             f"pinned instead. Read the diff, confirm no real identifier was added, then set "
             f"EXAMPLE_SHA256 to {actual}. Line endings are normalised before hashing, so this "
             f"is not a CRLF difference.")
        return
    lines = [l.strip() for l in PATTERNS_EXAMPLE.read_text(encoding="utf-8").splitlines()]
    listed = [l for l in lines if l and not l.startswith(("#", "["))]
    sections = [l for l in lines if l.startswith("[")]
    if not listed:
        fail(f"{PATTERNS_EXAMPLE.name} lists no patterns, so a fresh clone seeds an empty check "
             f"that passes everything")
    else:
        ok(f"example patterns file matches its pinned digest, {len(listed)} placeholders "
           f"across {len(sections)} sections")


def check_selectors(files):
    """Can the document's own conditions ever be true?

    Eleven checks verified claims, provenance, packaging and metadata. Not one
    asked whether a rule that fires on a profile value names a value the profile
    schema can hold. The 0.14.0 split moved the two layer files out of SKILL.md
    and left them selecting on `team: 1` and `team: 2 or more` while the schema
    had said `solo | pair | small-team | open-source` all along. Every shipped
    example uses the enum, so the selector matched nothing, in every repository,
    and an agent following it loaded neither layer and reported no error. Silent,
    because a condition that is never true looks exactly like a condition that
    did not apply.

    Found by RUNNING the adoption rather than reading the documents, after eight
    verification passes and two audits. Error 30."""
    schema = ROOT / "PROFILE.md"
    enums = {f: {v.strip() for v in vals.split("|")}
             for f, vals in ENUM_LINE.findall(schema.read_text(encoding="utf-8"))}
    if not enums:
        fail("no enum fields parsed from PROFILE.md, so this check verified nothing")
        return

    bad, checked = [], 0
    for f in files:
        if not f.endswith(".md"):
            continue
        for i, line in enumerate((ROOT / f).read_text(encoding="utf-8").splitlines(), 1):
            for field, value in SELECTOR.findall(line):
                if field not in enums:
                    continue
                checked += 1
                if value not in enums[field]:
                    bad.append(f"{f}:{i} selects `{field}: {value}`, not in {sorted(enums[field])}")
    if bad:
        fail(f"selectors that can never match the schema: {bad[:5]}")
    else:
        ok(f"{checked} profile selectors across {len(enums)} enum fields "
           f"({', '.join(sorted(enums))}), every value a member of its schema enum")


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


def prune_dist(version):
    """dist/ holds the CURRENT version's outputs and nothing else.

    The decision, and the reason, because "it is gitignored" was not enough.
    Until 2026-09-10 this directory accumulated every build ever made, twelve
    versions back to 0.7.0. Gitignored means it does not reach a consumer; it
    does not mean nothing reads it. Something did: an install command handed to
    the author picked a zip with sorted(glob(...))[-1], which sorts as STRINGS,
    so "0.9.0" beats "0.15.0" and the command would have installed 0.7.0. That
    is the version error 28 is about, so the fix for the stale install would
    have re-created the stale install.

    Two ways to close that. Fix every version picker, which is necessary and
    which you cannot verify for commands that do not live in this repository.
    Or leave nothing here to pick wrongly, which is the one that holds. Both.

    An older artifact is not lost: check out its tag and rebuild, which is the
    only way to be sure the artifact matches the tag anyway."""
    if not DIST.exists():
        return
    keep = {f"dev-conventions-{version}.zip", f"dev-conventions-{version}.json",
            f"dev-conventions-evidence-{version}.md"}
    stale = sorted(f for f in DIST.iterdir() if f.is_file() and f.name not in keep)
    for f in stale:
        f.unlink()
    if stale:
        print(f"  Removed {len(stale)} build outputs from versions no longer in the tree. "
              f"dist/ holds {version} only.")


def main():
    print("Checking before building.\n")
    version = read_version()
    files = collect()
    check_frontmatter()
    check_prose(files)
    check_metadata()
    check_licence_cover(files)
    check_example_placeholders()
    check_selectors(files)
    check_venue_confirmation()
    check_staleness()

    if FAILURES:
        print(f"\n{len(FAILURES)} check(s) failed. Nothing built.")
        return 1

    DIST.mkdir(exist_ok=True)

    prune_dist(version)
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
        "**Licence: CC BY 4.0.** Share and adapt this, including commercially, with credit to "
        "the collection and the version. This document travels on its own, so it carries its own "
        "terms rather than relying on a LICENSE file next to it. `CITATION.cff` in the repository "
        "carries the citation metadata.\n",
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
