.PHONY: help install fullinstall format lint test typecheck runall clean


help: 
	@echo "Usage: make <target>"
	@echo ""
	@echo "Targets:"
	@echo "  install    Install dependencies"
	@echo "  f-install Install all dependencies"
	@echo "  format     Format the code"
	@echo "  lint       Lint the code"
	@echo "  test       Run tests"
	@echo "  typecheck  Type check the code"
	@echo "  runall	 Run all tasks (format, lint, test, typecheck)"
	@echo "  clean      Clean up"


install:
	@echo "Installing dependencies..."
	@uv sync

f-install:
	@echo "Installing dependencies..."
	@uv sync --all-groups

format:
	@echo "Formatting code..."
	uv run ruff format .

lint:
	@echo "Linting code..."
	uv run ruff check . --fix

test:
	@echo "Running tests..."
	uv run pytest 

typecheck:
	@echo "Type checking code..."
	uv run mypy .

runall: format lint test typecheck

clean:
	@echo "Cleaning up..."
	rm -rf .pytest_cache .ruff_cache dist build