.PHONY: help install lint format test problems reset-notes

help:
@grep -E '^[a-zA-Z_-]+:' Makefile | sed 's/:.*//' | sort

install:
python -m venv .venv
. .venv/bin/activate && pip install --upgrade pip
. .venv/bin/activate && pip install -e .[dev]

lint:
. .venv/bin/activate && ruff check src tests

format:
. .venv/bin/activate && ruff format src tests

test:
. .venv/bin/activate && pytest

problems:
PYTHONPATH=src python scripts/list_problems.py

reset-notes:
rm -f notes/*.md
