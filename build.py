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
    "ROADMAP.md",     # what is open here, not a convention
    "build.py",
    "CITATION.cff",   # belongs to the repository, not the skill
    "CONTRIBUTING.md",      # how to contribute here, not a convention
    "CODE_OF_CONDUCT.md",   # governs this repository, not a consumer's
    ".gitignore",
}
EXCLUDE_DIRS = {".git", "dist", ".agents", "__pycache__", ".claude-plugin", ".github"}
# .github holds this repository's vulnerability-disclosure policy, which is a
# different document from the root SECURITY.md despite the near-identical name.
# The root one is skill content and ships. This one governs reporting here.
# .claude-plugin holds the marketplace and plugin manifests. Those describe how
# the REPOSITORY offers the skill, not the skill itself, so they belong with
# CITATION.cff and build.py rather than in the distributable. They also carry an
# owner handle, which the identifier-leak check is right to reject in skill prose.

# Reading order for the JSON bundle, so an unpacked copy reads sensibly.
ORDER = [
    "README.md", "ADOPTION.md", "SKILL.md", "EVIDENCE.md", "DOCS.md",
    "SECURITY.md", "WORKFLOW.md", "RESEARCH.md", "TOOLING.md",
    "OBSERVABILITY.md", "VOCABULARY.md", "PROFILE.md", "OPERATING.md",
    "CHANGELOG.md", "LICENSE",
]

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
            rel = Path(dirpath, name).relative_to(ROOT).as_posix()
            if rel in EXCLUDE_FILES or Path(rel).name in EXCLUDE_FILES:
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
    if len(desc) > 200:
        fail(f"description is {len(desc)} characters, cap is 200")
    else:
        ok(f"description is {len(desc)} characters")
    allowed = {"name", "description", "license", "compatibility", "metadata", "allowed-tools"}
    extra = set(fields) - allowed
    if extra:
        fail(f"frontmatter carries fields the spec rejects: {sorted(extra)}")
    else:
        ok("frontmatter carries only accepted fields")


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

    # cross-references. External concepts and template placeholders are expected.
    external = {
        "CLAUDE.md", "GEMINI.md", "skills.md", ".agents/profile.yml",
        "dev-conventions/SKILL.md", "requirements.txt", "ADR-NNN.md",
        "ADR-NNN-kebab-case-title.md", "LOCAL.md", "AGENTS.md", "ROADMAP.md",
    }
    refs = set()
    pattern = re.compile(r"`([A-Za-z_./-]+\.(?:md|yml))`")
    for f in md:
        refs.update(pattern.findall((ROOT / f).read_text(encoding="utf-8", errors="ignore")))
    missing = sorted(
        r for r in refs
        if r not in external
        and not (ROOT / r).exists()
        and not (ROOT / "templates" / r).exists()
        and not (ROOT / "examples" / r).exists()
    )
    if missing:
        fail(f"cross-references that do not resolve: {missing}")
    else:
        # Print the count, never just "no errors": a check that passes by
        # finding nothing to check is error 9.
        ok(f"{len(refs)} cross-references examined, all resolve")


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

    print(f"\nBuilt version {version}, {len(files)} files.")
    print(f"  {zip_path.relative_to(ROOT)}  {zip_path.stat().st_size / 1024:.1f} KB")
    print(f"  {json_path.relative_to(ROOT)}  {json_path.stat().st_size / 1024:.1f} KB")
    excluded = sorted(EXCLUDE_FILES) + sorted(f"{d}/" for d in EXCLUDE_DIRS if d != ".git")
    print("\nExcluded from the distributable: " + ", ".join(excluded))
    return 0


if __name__ == "__main__":
    sys.exit(main())
