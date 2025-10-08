"""Create a problem journal entry from the template."""
from __future__ import annotations

from datetime import date
from pathlib import Path
from typing import Optional

from ctci.catalog import get_problem

TEMPLATE_PATH = Path("docs/templates/problem_journal.md")
NOTES_DIR = Path("notes")


def create_note(chapter: str, number: int, *, overwrite: bool = False) -> Path:
    problem = get_problem(chapter, number)
    template = TEMPLATE_PATH.read_text()
    note_body = template.format(
        title=f"Practice Log — {problem.title}",
        chapter_title=problem.chapter.replace("_", " ").title(),
        chapter_id=problem.chapter,
        problem_number=f"{problem.number:02d}",
        problem_title=problem.title,
        module_path=problem.code_path,
        tags=", ".join(problem.tags) or "—",
        date=date.today().isoformat(),
    )
    NOTES_DIR.mkdir(exist_ok=True)
    note_path = NOTES_DIR / problem.note_filename
    if note_path.exists() and not overwrite:
        raise FileExistsError(f"Note already exists: {note_path}")
    note_path.write_text(note_body)
    return note_path


def main(argv: Optional[list[str]] = None) -> None:
    import argparse

    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("chapter", help="Chapter identifier, e.g., ch01_arrays_and_strings")
    parser.add_argument("number", type=int, help="Problem number within the chapter")
    parser.add_argument(
        "--overwrite",
        action="store_true",
        help="Overwrite the note if it already exists",
    )
    args = parser.parse_args(argv)

    note_path = create_note(args.chapter, args.number, overwrite=args.overwrite)
    print(f"Created {note_path}")


if __name__ == "__main__":
    main()
