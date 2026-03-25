- **Prefer not to `cd`** in Bash commands -- it changes the working directory for subsequent calls. Prefer subshells (`(cd <subdir> && cmd)`) or `pushd`/`popd` to keep the working directory at the project root.
- **ASCII only** in responses -- no emojis, no Unicode dashes/quotes (use `-`, `--`, `'`, `"`)
- Maximize parallel tool calls when exploring or editing multiple files.
- Prefer header/inline comments and tests over separate docs. Do NOT write standalone explanation docs. Maintain header comments after edits. Inline comments only when logic is non-obvious.

## Python

- Always use `uv`. Prefer self-contained single file script.

## Make

- Use `-j$(sysctl -n hw.ncpu)`.

## Git

- When updating a PR, only use `--amend` when this commit is a simple fix to the previous.
- Ask before opening a PR to a public GitHub repo.

