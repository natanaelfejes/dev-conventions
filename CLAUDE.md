# Working in this repository

**Read `AGENTS.md` first.** It carries the target, the scope, what is permanently out of scope, the
non-negotiable rules, and the checks to run before committing. This file exists only so that a
harness looking for `CLAUDE.md` finds the way there, and it deliberately duplicates nothing:
a second copy of the rules is a second thing to keep correct, and this repository has recorded four
separate errors caused by a correction landing in one file and not another.

Three things worth knowing before you read it:

- **The target is `AGENTS.md`'s first section**, quoted from the author rather than inferred. The
  short form: reduce the friction of having to keep researching what the best AI-assisted development
  practice currently is, adopt the result in every repository, and eventually publish it with credit.
- **`.agents/goals.md` holds the author's statements verbatim**, with a table of where each want
  actually stands. Read it if you are about to propose a direction.
- **The test for any change**: does it produce a rule an engineer can act on, or does it grow the
  apparatus that justifies the rules? Seven verification passes have run and none produced a rule.

`SKILL.md` is the collection itself and is a skill so that it loads on demand. **Never `@`-import it
from here.**
