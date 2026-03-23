- **Never `cd` into subdirectories** in Bash commands -- it changes the working directory for subsequent calls. Use subshells (`(cd <subdir> && git ...)`) or `pushd`/`popd` (`pushd <subdir>; git ...; popd`) to keep the working directory at the project root.
- **ASCII only** in responses -- no emojis, no Unicode dashes/quotes (use `-`, `--`, `'`, `"`)
- When exploring or editting multiple files, run in parallel whenever possible, instead of processing them sequentially.
- To avoid _Docs Rot_, prefer header comment, inline comment, tests than seperate standalone docs. keep docs near the code. Do NOT write separate explanation docs or duplicate what code already says. Maintain header comments after each edit. Inline comments only when logic is non-obvious.

