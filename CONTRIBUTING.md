# Contributing to Word Histogram

Thank you for considering contributing to Word Histogram! This document provides guidelines and instructions for contributing to this project.

## Code of Conduct

By participating in this project, you agree to abide by our Code of Conduct, which expects all participants to be respectful and considerate of others.

## Getting Started

### Development Environment

1. Clone the repository:
   ```bash
   git clone https://github.com/username/word-histogram.git
   cd word-histogram
   ```

2. Create a virtual environment and install the development dependencies:
   ```bash
   python -m venv venv
   source venv/bin/activate  # On Windows: venv\Scripts\activate
   pip install -e ".[dev,wordcloud]"
   ```

### Project Structure

```
word-histogram/
├── docs/               # Documentation
├── examples/           # Example usage scripts
├── src/                # Source code
│   └── word_histogram/ # Main package
│       ├── core.py     # Core functionality
│       ├── cli.py      # Command-line interface
│       └── ...
├── tests/              # Unit tests
├── LICENSE             # License file
├── pyproject.toml      # Project metadata and dependencies
├── README.md           # Project README
└── ...
```

## Making Changes

### Workflow

1. Create a new branch for your feature or bug fix:
   ```bash
   git checkout -b feature-name
   ```

2. Make your changes, following the project's coding style and guidelines

3. Add tests for your changes to ensure they work as expected

4. Ensure all tests pass:
   ```bash
   pytest
   ```

5. Format your code using Black:
   ```bash
   black src tests examples
   ```

6. Check for linting issues with Flake8:
   ```bash
   flake8 src tests examples
   ```

### Coding Style

- Follow PEP 8 guidelines for Python code
- Use descriptive variable names and function names
- Include docstrings for all functions, classes, and modules
- Keep functions focused on a single responsibility
- Write clear comments for complex logic

## Pull Requests

1. Update the documentation if necessary
2. Update the CHANGELOG.md file with your changes
3. Push your branch to GitHub:
   ```bash
   git push origin feature-name
   ```
4. Create a pull request on GitHub
5. Describe your changes in the pull request, including:
   - What the changes do
   - Why the changes are needed
   - How to test the changes
   - Any relevant screenshots or examples

## Testing

We use pytest for testing. To run the tests:

```bash
# Run all tests
pytest

# Run tests with coverage report
pytest --cov=word_histogram

# Run a specific test
pytest tests/test_specific_file.py
```

## Documentation

We use MkDocs for documentation. To build and preview the documentation:

```bash
# Install MkDocs and the theme
pip install mkdocs mkdocs-material

# Build the documentation
mkdocs build

# Serve the documentation locally
mkdocs serve
```

## Release Process

1. Update version number in `src/word_histogram/__init__.py`
2. Update CHANGELOG.md with the new version and changes
3. Create a new release on GitHub
4. Build and upload the package to PyPI:
   ```bash
   python -m build
   twine upload dist/*
   ```

## Questions?

If you have any questions or need help, please:
- Open an issue on GitHub
- Contact the maintainers via email
- Join our community discussion forum

Thank you for contributing to Word Histogram!