.PHONY: tests
tests:
	@echo "Running tests..."
	@PYTHONPATH=. pytest -v