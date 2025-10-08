"""Pretty-print the available Cracking the Coding Interview problems."""
from __future__ import annotations

from ctci.catalog import iter_chapters


def main() -> None:
    for chapter in iter_chapters():
        print(f"{chapter['title']} ({chapter['id']})")
        for problem in chapter["problems"]:
            tags = ", ".join(problem.tags) if problem.tags else "—"
            print(
                f"  {problem.number:2d}. {problem.title}"
                f"\n      module: {problem.code_path}"
                f"\n      tags:   {tags}"
            )
        print()


if __name__ == "__main__":
    main()
