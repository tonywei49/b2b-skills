# b2b-skills

Collection repository for reusable OpenClaw skills.

This repo is a monorepo. Each top-level folder is one standalone skill package with its own `SKILL.md` and supporting files.

## Structure

```text
b2b-skills/
|-- README.md
|-- .gitignore
|-- b2b-lead-scout/
|   |-- SKILL.md
|   |-- README.md
|   |-- examples/
|   |-- references/
|   `-- scripts/
`-- tavily-search/
    |-- SKILL.md
    |-- tavily.py
    `-- check_install_deps.ps1
```

## Included Skills

| Skill | Purpose |
|------|---------|
| `b2b-lead-scout` | Find and structure B2B leads by product and region, with export workflows for CSV/Markdown/JSON and runtime-aware fallbacks. |
| `hidden-buyer-scout` | Find non-obvious cross-industry buyers by usage scenario, buying logic, and hidden bulk-purchase signals. |
| `tavily-search` | Tavily-based search helper skill for search execution and related tooling. |

## Adding New Skills

Add each new skill as a new top-level directory, for example:

```text
b2b-skills/
|-- my-new-skill/
|   |-- SKILL.md
|   |-- README.md
|   |-- examples/
|   |-- references/
|   `-- scripts/
```

Recommended conventions:

- one skill per top-level folder
- always include `SKILL.md`
- include a local `README.md` if the skill has setup, examples, or runtime requirements
- keep examples, scripts, and references inside the skill folder
- do not nest standalone git repositories inside this repo

## Notes

- This repository intentionally does **not** preserve the old `b2b-lead-scout` git history.
- The old standalone `b2b-lead-scout` repository can be archived or deleted after you confirm this repo is the new source of truth.
