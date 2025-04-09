.PHONY: test lint type-check install-dev clean

# Install development dependencies
install-dev:
	pip install -e ".[dev]"

# Run tests with coverage
test:
	pytest --cov=promptly_ai tests/

# Run type checking
type-check:
	mypy promptly_ai/

# Run linting
lint:
	flake8 promptly_ai/ tests/

# Clean up build artifacts
clean:
	rm -rf build/
	rm -rf dist/
	rm -rf *.egg-info/
	rm -rf .pytest_cache/
	rm -rf .coverage
	rm -rf .mypy_cache/ 