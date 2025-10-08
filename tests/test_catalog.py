from __future__ import annotations

import importlib
from pathlib import Path

import pytest

from ctci import catalog


def test_problem_count() -> None:
    problems = list(catalog.iter_problems())
    assert len(problems) == 189


@pytest.mark.parametrize(
    "problem",
    list(catalog.iter_problems()),
)
def test_stub_modules_exist(problem: catalog.Problem) -> None:
    module = importlib.import_module(problem.code_path)
    assert hasattr(module, "PROBLEM")
    assert module.PROBLEM == problem


def test_chapter_directories_match_catalog() -> None:
    base = Path("src/ctci/chapters")
    expected = {chapter["id"] for chapter in catalog.iter_chapters()}
    found = {path.name for path in base.iterdir() if path.is_dir()}
    assert expected == found
