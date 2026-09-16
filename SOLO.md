# Solo repositories

**Load this when the profile says `team: solo`.** Split out of `SKILL.md` on 2026-09-08: this and
`TEAM.md` are mutually exclusive by the profile's own rule, and both were loading on every session,
so roughly half of what an agent read applied to nobody.

**This file is a short appendix and it is meant to be.** `TEAM.md` is nine times its size because a
team carries obligations Layer 1 does not cover. A solo repository does not: **Layer 1 is where
almost all of this collection's first-party observation came from**, since the repositories it was
observed in were one or two people each. So read Layer 1 as the solo rules, and read this for the
three places where being alone changes the answer. That asymmetry was unstated until 2026-09-16 and
the companion table implied the two files were symmetric.

**Provenance: entirely `first-party`**, from small repositories worked on by one or two people. Read
every rule here as a hypothesis about your repository rather than a finding about it.

Apply only when the profile says there is no second human reviewer. **These are wrong on a team.**

- The change description **is** the review record, because nobody else will read the diff. On a team
  a human reads the diff, so the description is a summary and not the record. **This is the most
  consequential thing the profile selects and it is worth being concrete about what it means:** the
  description states which review passes ran, what each one found, and what it did not check.
  "No review passes run: documentation-only diff" is a complete record. Silence is not, because a
  reader cannot tell it from having forgotten. Layer 1's rules about risk, negative evidence and
  describing the whole diff rather than your own commits all become load-bearing here for the same
  reason: they are the only trace the change will leave.
- Self-merging is acceptable only if the description states which review passes ran and what they
  found. That record is the compensating control for the missing reviewer.
- **Do not assume no other branch is in flight.** This bullet said the opposite until 2026-09-16,
  that a repository-wide sweep can be scheduled at your own convenience because no one else's branch
  is in flight. **In a solo repository worked by parallel agent sessions, another branch is in
  flight, and it is yours.** Two recorded incidents, both in solo repositories: a concurrent session
  moved HEAD mid-procedure and a commit landed on the default branch because the working tree had
  been switched underneath; and four concurrent sessions in isolated worktrees clobbered each other's
  build output through a shared cache path, producing a phantom failure that cost one session real
  investigation time and taught another session to rerun until green. **Solo is a fact about humans,
  not about concurrency**, and the collection had been reading it as both.
- **Do not expect anything to prompt you to re-read a record that has gone stale.** On a team a
  second reader eventually meets a claim that is no longer true. Alone, nothing does. Measured twice
  in the same repository: a derived profile went stale **within hours** under concurrent development,
  and a profile field describing a security property was still wrong **five days** after the feature
  that falsified it shipped, in a repository whose author corrects stale claims promptly when
  something triggers a look. The gap is not diligence, it is that nothing triggers the look. Tie the
  re-read to an event that already happens: the change that alters the property is the moment, and
  `PROFILE.md` carries the rule.
