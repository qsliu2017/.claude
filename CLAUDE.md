- **Prefer not to `cd`** in Bash commands -- it changes the working directory for subsequent calls. Prefer subshells (`(cd <subdir> && cmd)`) or `pushd`/`popd` to keep the working directory at the project root.
- **ASCII only** in responses -- no emojis, no Unicode dashes/quotes (use `-`, `--`, `'`, `"`)
- Maximize parallel tool calls when exploring or editing multiple files.
- Delegate independent subtasks to subagents and keep working while they run. Intervene if a subagent goes off track or is missing relevant context.
- Before starting any long-running workflow or setting a goal, use CronCreate to schedule a recurring task every 1h with the prompt: "If the previous work was interrupted by a usage limit, resume it from where it left off. If work is complete or proceeding normally, do nothing." Delete the cron job (CronDelete) when the workflow completes.
- Prefer code than comments. Only comment if code is very non-obvious. Prefer header/inline comments and tests over separate docs. Shoud not write standalone explanation docs.

## Comment Conventions

Try to keep comments short. In general, comments should be one short line. Only in exceptional situations should comments be more than one short line. Code should be mostly self-descriptive and too many large comments make code harder to read and understand.

Avoid adding comments specific to how a change was made to the code that relates to a specific issue. For example, a comment like "add +1 to fix an off-by-one error" is not relevant to understanding the code. Such comments related to specific issues that were addressed belong in a PR description or commit message, not in the code itself.

## Python

- Always use `uv`. Prefer self-contained single file script.

## JavaScript/TypeScript

- Always use `bun`. Prefer bun script.
- Prefer TypeScript.

## Make

- Use `-j$(sysctl -n hw.ncpu)`.

## Git

- When updating a PR, only use `--amend` when this commit is a simple fix to the previous.
- Ask before opening a PR to a public GitHub repo.

---

## Prevent unrequested tidying or refactoring

Don't add features, refactor, or introduce abstractions beyond what the task requires. A
bug fix doesn't need surrounding cleanup and a one-shot operation usually doesn't need a
helper. Don't design for hypothetical future requirements: do the simplest thing that
works well. Avoid premature abstraction and half-finished implementations. Don't add
error handling, fallbacks, or validation for scenarios that cannot happen. Trust
internal code and framework guarantees. Only validate at system boundaries (user input,
external APIs). Don't use feature flags or backwards-compatibility shims when you can
just change the code.

## Readability when communicating with the user

Terse shorthand is fine between tool calls (that's you thinking out loud, and brevity
there is good). Your final summary is different: it's for a reader who didn't see any of
that.

If you've been working for a while without the user watching (overnight, across many
tool calls, since they last spoke), your final message is their first look at any of it.
Write it as a re-grounding, not a continuation of your working thread: the outcome
first, then the one or two things you need from them, each explained as if new. The
vocabulary you built up while working is yours, not theirs; leave it behind unless you
re-introduce it.

When you write the summary at the end, drop the working shorthand. Write complete
sentences. Spell out terms. Don't use arrow chains, hyphen-stacked compounds, or labels
you made up earlier. When you mention files, commits, flags, or other identifiers, give
each one its own plain-language clause. Open with the outcome: one sentence on what
happened or what you found. Then the supporting detail. If you have to choose between
short and clear, choose clear.

