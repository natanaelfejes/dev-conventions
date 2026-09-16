#!/usr/bin/env python3
"""Validate a repository profile against the schema in PROFILE.md.

    python3 templates/validate_profile.py .agents/profile.yml
    python3 templates/validate_profile.py .agents/profile.yml --cite .githooks/pre-push
    python3 templates/validate_profile.py --self-test

WHY THIS EXISTS. The first and most repeated rule in SKILL.md is "do not put in
an auto-loaded file what a linter, formatter or analyzer can enforce". The
profile is the one artefact every other rule in this collection reads, and until
2026-09-16 nothing checked it. An adoption run found a profile with a
comma-separated scalar where PROFILE.md says list, an absent `setup` where
PROFILE.md says never blank, and four stale values. Checking that finding found
two of the same defects in this collection's own profile, unseen by eleven build
checks and ten verification passes, because none of them looks at a profile.
Error 34.

WHAT IT DELIBERATELY DOES NOT DO. It cannot tell a derived value from a wrong
one. `reviewers` is counted from history and no file check substitutes for that.
What it checks is the half that is mechanical: enum membership, the shapes the
schema is explicit about, the fields whose absence is indistinguishable from
nobody having looked, and citations of field names that do not exist.

It reports the count it examined rather than exiting quietly, and it FAILS when
it finds nothing to check. A checker that can pass by finding nothing is worse
than no checker: that is error 9 in this collection's own list, and this file is
written to not repeat it. Run --self-test to watch it fail on purpose.

No third-party dependency, deliberately: it runs in a fresh clone of any
repository with a Python interpreter. The parser handles the flat, commented
subset of YAML this schema uses and says so when it meets something it cannot
read, rather than guessing.
"""

import argparse
import re
import sys
from pathlib import Path

ENUMS = {
    "team": {"solo", "pair", "small-team", "open-source"},
    "reviewers": {"none", "nominal", "agent", "one", "rotating"},
    "maturity": {"prototype", "production", "published"},
    "disclosure": {"assisted-by", "generated-by", "none", "undecided"},
}

# Fields whose ABSENCE cannot be told from "nobody checked", which is the
# distinction the whole schema exists to keep. Each carries the value to write
# when the honest answer is nothing.
REQUIRED = {
    "setup": "setup: none",
    "maturity": "a derived value, never the readme's claim",
    "team": "one of " + ", ".join(sorted(ENUMS["team"])),
    "reviewers": "counted from history, not read off a policy",
}

# Fields that must be a sequence even with one entry.
LISTS = {"secrets", "review", "declined"}

KNOWN_TOP = set(ENUMS) | {
    "derived", "commits_at_derivation", "docs", "stack", "review", "tools",
    "secrets", "setup", "declined",
}
KNOWN_STACK = {"language", "check", "format", "test", "build", "docs_check"}
KNOWN_DOCS = {"current_state", "history", "pending", "decisions", "contributing", "absent"}

TOP = re.compile(r"^([a-z_]+):(.*)$")
NESTED = re.compile(r"^(\s+)([a-z_]+):(.*)$")
ITEM = re.compile(r"^\s*-\s")
# A citation of a profile field in another file: `field: value` or field: value
CITATION = re.compile(r"`?\b([a-z_]+):\s*([A-Za-z0-9_.\-/]+)`?")


def strip_comment(text):
    """Drop a trailing comment. Not quote-aware beyond the simple cases this
    schema uses, and it says so rather than pretending otherwise."""
    if "#" not in text:
        return text.strip()
    quoted = re.match(r'\s*"[^"]*"', text)
    if quoted:
        return quoted.group(0).strip()
    return text.split("#", 1)[0].strip()


def parse(path):
    """Return {field: (value_or_None, kind, line_no)} for the top level, plus
    {parent: {child: (value, line_no)}} for the two nested blocks this schema
    has. kind is 'scalar', 'block' or 'list'."""
    top, nested, problems = {}, {}, []
    lines = path.read_text(encoding="utf-8").splitlines()
    current = None
    for n, raw in enumerate(lines, 1):
        if not raw.strip() or raw.lstrip().startswith("#"):
            continue
        m = TOP.match(raw)
        if m:
            field, rest = m.group(1), strip_comment(m.group(2))
            current = field
            if not rest:
                kind = "block"
            elif rest.startswith("["):
                # An inline empty or flow sequence. `secrets: []` is the list
                # form of "none", and it has to be accepted or the schema's own
                # "a LIST, always" rule has no way to say zero.
                kind = "list"
            else:
                kind = "scalar"
            top[field] = (rest or None, kind, n)
            nested.setdefault(field, {})
            continue
        if ITEM.match(raw):
            if current:
                value, _, ln = top[current]
                top[current] = (value, "list", ln)
                body = strip_comment(ITEM.sub("", raw, count=1))
                nested.setdefault(current, {})[f"__item_{n}"] = (body, n)
            continue
        m = NESTED.match(raw)
        if m and current:
            child, rest = m.group(2), strip_comment(m.group(3))
            nested.setdefault(current, {})[child] = (rest or None, n)
            continue
        if raw.strip():
            problems.append(f"line {n}: not a shape this checker reads: {raw.strip()[:60]}")
    return top, nested, problems


def check_profile(path):
    findings, examined = [], 0
    top, nested, problems = parse(path)
    findings += [(path, p) for p in problems]

    for field, (value, kind, line) in sorted(top.items()):
        examined += 1
        if field not in KNOWN_TOP:
            findings.append((path, f"line {line}: `{field}` is not in the schema. "
                                   f"Check the spelling against PROFILE.md"))
        if field in ENUMS and value is not None:
            if value.strip('"\'') not in ENUMS[field]:
                findings.append((path, f"line {line}: `{field}: {value}` is not one of "
                                       f"{sorted(ENUMS[field])}"))
        if field in LISTS and kind == "scalar":
            findings.append((path, f"line {line}: `{field}` is a scalar. PROFILE.md says a LIST, "
                                   f"always, even with one entry: a scalar leaves a reader "
                                   f"guessing whether to split it or iterate it"))

    for field, hint in sorted(REQUIRED.items()):
        examined += 1
        if field not in top:
            findings.append((path, f"`{field}` is absent. An absent field cannot be told from one "
                                   f"nobody checked. Write {hint}"))
        elif top[field][0] is None and top[field][1] == "scalar":
            findings.append((path, f"line {top[field][2]}: `{field}` is blank. Blank reads as "
                                   f"'not applicable' and as 'never checked' equally well"))

    if "docs" in top:
        blanks = [c for c, (v, _) in nested.get("docs", {}).items()
                  if c in KNOWN_DOCS and c != "absent" and v in (None, "null")]
        absent = nested.get("docs", {}).get("absent")
        examined += 1
        if blanks and absent is None:
            findings.append((path, f"docs has {len(blanks)} empty slot(s) ({', '.join(sorted(blanks))}) "
                                   f"and no `absent`. Dropping a slot relocates its content rather "
                                   f"than removing it. Record where it went"))
        if not blanks and absent is None:
            findings.append((path, "docs has no empty slot and no `absent`. Write `absent: {}` "
                                   "rather than omitting it, so it reads as checked"))
        for child, (_, line) in sorted(nested.get("docs", {}).items()):
            if child.startswith("__item_"):
                continue
            if child not in KNOWN_DOCS:
                findings.append((path, f"line {line}: `docs.{child}` is not a documentation slot "
                                       f"in the schema"))

    for child, (_, line) in sorted(nested.get("stack", {}).items()):
        examined += 1
        if child.startswith("__item_"):
            continue
        if child not in KNOWN_STACK:
            findings.append((path, f"line {line}: `stack.{child}` is not in the schema"))

    examined += 1
    if "derived" not in top:
        findings.append((path, "`derived` is absent, so nothing distinguishes this profile from a "
                               "copy of the template. Record the date you ran the commands"))
    examined += 1
    if "commits_at_derivation" not in top:
        findings.append((path, "`commits_at_derivation` is absent, so a reader cannot measure how "
                               "much has happened since anyone looked. "
                               "git rev-list --count HEAD"))
    return findings, examined


def check_citation(path):
    """Flag a file citing a profile field or value the schema does not have.

    Two sibling repositories both shipped files citing `review: none`. The field
    is `reviewers`; `review` holds the list of available passes. Both cited a
    field and value pair that does not exist, and nothing caught it."""
    findings, examined = [], 0
    for n, raw in enumerate(path.read_text(encoding="utf-8").splitlines(), 1):
        for field, value in CITATION.findall(raw):
            if field not in ENUMS and field not in KNOWN_TOP:
                continue
            examined += 1
            if field in ENUMS and value not in ENUMS[field]:
                findings.append((path, f"line {n}: cites `{field}: {value}`, and `{field}` "
                                       f"holds one of {sorted(ENUMS[field])}"))
            elif field in LISTS and value in {"none", "null"}:
                findings.append((path, f"line {n}: cites `{field}: {value}`, and `{field}` is a "
                                       f"list. Did you mean `reviewers`?"))
    return findings, examined


SELF_TEST = """\
team: 1
reviewers: none
maturity: prototype
secrets: .env, config/local.json
docs:
  current_state: README.md
"""


def self_test():
    """Make it fail on purpose. A checker you have never seen fail is a checker
    you are taking on faith, and one that passes by finding nothing is worse
    than none: error 9 in this collection's own list."""
    import tempfile
    expected = ["team", "secrets", "setup", "absent", "derived", "commits_at_derivation"]
    with tempfile.NamedTemporaryFile("w", suffix=".yml", delete=False, encoding="utf-8") as fh:
        fh.write(SELF_TEST)
        tmp = Path(fh.name)
    findings, examined = check_profile(tmp)
    tmp.unlink()
    text = " ".join(m for _, m in findings)
    missed = [e for e in expected if e not in text]
    print(f"  self-test: {len(findings)} findings from {examined} checks on a deliberately "
          f"broken profile")
    for _, message in findings:
        print(f"    - {message}")
    if missed:
        print(f"\n  SELF-TEST FAILED: nothing reported about {missed}")
        return 1
    print("\n  self-test passed: every planted defect was reported, by name.")
    return 0


def main(argv=None):
    ap = argparse.ArgumentParser(description=__doc__.splitlines()[0])
    ap.add_argument("profile", nargs="?", help="path to .agents/profile.yml")
    ap.add_argument("--cite", action="append", default=[],
                    help="a file that cites profile fields, checked for field names "
                         "the schema does not have. Repeatable")
    ap.add_argument("--self-test", action="store_true",
                    help="run the checker against a deliberately broken profile and "
                         "require every planted defect to be reported")
    args = ap.parse_args(argv)

    if args.self_test:
        return self_test()
    if not args.profile:
        ap.error("give a profile path, or --self-test")

    path = Path(args.profile)
    if not path.is_file():
        print(f"  no profile at {path}. SKILL.md: do not proceed silently when no profile "
              f"exists. State the inferences you are making, then offer to write one.")
        return 2

    findings, examined = check_profile(path)
    for cited in args.cite:
        cp = Path(cited)
        if not cp.is_file():
            print(f"  --cite {cited} does not exist")
            return 2
        f, e = check_citation(cp)
        findings += f
        examined += e

    if examined == 0:
        print("  FAILED: this checker examined nothing. A check that can pass by finding "
              "nothing to check is worse than no check.")
        return 1

    for where, message in findings:
        print(f"  {where}: {message}")
    scope = f"{examined} checks against {path}"
    if args.cite:
        scope += f" and {len(args.cite)} citing file(s)"
    if findings:
        print(f"\n  {len(findings)} findings, {scope}.")
        return 1
    print(f"  clean: {scope}, every field a member of its schema.")
    return 0


if __name__ == "__main__":
    sys.exit(main())
