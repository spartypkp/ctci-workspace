# Cracking the Coding Interview Practice Hub

This repository is a fresh workspace tailored for deliberate practice with *Cracking the Coding
Interview (6th Edition)*. Every question now ships with a dedicated Python module, metadata, and a
journaling workflow so you can track progress without hunting for prompts.

## What's Included

- **Full catalog (189 problems)** — All chapters from arrays to hard problems live under
  `src/ctci/chapters`. Each module contains a lightweight scaffold with a `solve` helper ready to
  replace.
- **Problem metadata** — `ctci.catalog` exposes chapter names, tags, and helper functions so you can
  script your own drills or dashboards.
- **Practice tooling**
  - `make install` bootstraps a virtual environment with `pytest` and `ruff`.
  - `make lint`, `make format`, and `make test` keep your solutions healthy.
  - `make problems` prints the entire catalog with module paths and tags.
  - `python scripts/new_problem_note.py <chapter> <number>` creates a journal entry in `notes/` using
    the opinionated template under `docs/templates/`.
- **Study guidance** — Opinionated practice plan and note-taking templates in `docs/` to encourage a
  consistent rhythm.

## Getting Started

1. **Install tooling**

   ```bash
   make install
   ```

2. **List available problems**

   ```bash
   make problems | head
   ```

3. **Start practicing**

   ```bash
   # Example: Chapter 1 (Arrays and Strings), Problem 1 (Is Unique)
   python scripts/new_problem_note.py ch01_arrays_and_strings 1
   code src/ctci/chapters/ch01_arrays_and_strings/p01_is_unique.py
   ```

4. **Run tests and linting** as you iterate:

   ```bash
   make test
   make lint
   ```

## Folder Layout

```
src/ctci/             # Python package with catalog + problem stubs
  catalog.py          # Central metadata for chapters and problems
  chapters/           # Implementation stubs grouped by chapter
scripts/              # Utility scripts (listing problems, creating notes)
docs/                 # Study plan + templates
tests/                # Sanity tests for the catalog
notes/                # Your personal journal entries (initially empty)
```

## Customizing the Workflow

- Add your own helper libraries inside `src/ctci/` and import them in problem files.
- Keep solved solutions in place or branch them into separate modules—`ctci.catalog` will always
  know where the canonical entry point lives.
- Extend `scripts/list_problems.py` to filter by tag or difficulty and surface spaced-repetition
  reminders.

Happy grinding! Commit early, journal often, and revisit old problems to reinforce the patterns you
want to master.
