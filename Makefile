.PHONY: tests
tests:
	@echo "Running tests..."
	@PYTHONPATH=src pytest -v
