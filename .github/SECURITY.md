# Security policy

**This file is about reporting a vulnerability in this repository.** It is not the collection's
security guidance. That is `SECURITY.md` at the repository root, which covers agentic security
obligations and is part of the skill itself. Two different documents with nearly the same name, which
is worth stating plainly rather than letting a reader find out the slow way.

## What could actually be a vulnerability here

This repository ships prose, templates, and one build script. It has no runtime, no server, no
dependencies and no credentials. The realistic report categories are:

- **An identifier leak.** A name, an employer, a customer, an internal hostname, a repository path or
  a commit hash that should not be public, in file contents **or in commit metadata**. The latter is
  the one that has actually happened: the leak check read file contents while an employer address sat
  in the author field of every commit. Report either.
- **A malicious or unsafe instruction in the skill text.** These files are loaded into agent
  sessions. Text that would cause an agent to exfiltrate data, disable a safeguard, run something
  destructive, or fetch and execute from an untrusted location is a security defect here even though
  no code executes in this repository.
- **A template that establishes an unsafe default.** `templates/pre-push`, the profile schema, and
  the instruction-file skeleton get copied into other people's repositories. A weak default
  propagates.
- **Anything in `build.py`.** It reads files, runs `git`, and writes a zip. Path traversal, command
  injection through a filename, or a zip that writes outside its extraction root would all qualify.

## What is not a vulnerability

A claim being wrong is not a security issue. It is an error, and errors have their own numbered list
in `EVIDENCE.md`. Open a normal issue.

## Reporting

**Use GitHub's private vulnerability reporting** on this repository, under the Security tab, "Report
a vulnerability". That opens a private advisory visible only to the maintainer, which is the right
channel for anything involving an exposed identifier, because a public issue describing the leak
republishes it.

If private reporting is unavailable to you, open a public issue **only if the report does not itself
disclose the sensitive value**. Say that a leak exists and where to look, not what it is.

## What to expect

- Acknowledgement within seven days.
- An assessment of whether it is accepted, and if not, why.
- For an accepted identifier leak, a history rewrite rather than a follow-up commit, because a commit
  that removes a value leaves the value in history.
- Credit in the changelog unless you ask otherwise.

This is a single-maintainer project with no service-level commitment and no bounty. The timelines
above are intent, not a guarantee.

## Scope

This repository only. The collection describes practices for other people's repositories and carries
no responsibility for how they are implemented there.
