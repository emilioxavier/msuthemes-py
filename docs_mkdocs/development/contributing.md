# Contributing to MSUthemes

Thank you for your interest in contributing to MSUthemes! This guide will help you get started.

## Code of Conduct

This project adheres to the [Contributor Covenant Code of Conduct](code_of_conduct.md). By participating, you are expected to uphold this code. Please report unacceptable behavior as described in the Code of Conduct.

## Development Setup

### Clone the Repository

```bash
git clone https://github.com/emilioxavier/msuthemes-py.git
cd msuthemes-py
```

### Install Development Dependencies

```bash
# Install in development mode with all dependencies
pip install -e .[dev]

# Or install with all optional dependencies
pip install -e .[all]
```

### Verify Installation

```bash
# Run tests
pytest

# Run with coverage
pytest --cov=msuthemes --cov-report=html --cov-report=term-missing
```

## Development Workflow

### 1. Create a Branch

```bash
git checkout -b feature/your-feature-name
```

Use descriptive branch names:
- `feature/new-palette` for new features
- `fix/color-conversion-bug` for bug fixes
- `docs/update-quickstart` for documentation

### 2. Make Your Changes

Follow the project structure and conventions:

```
msuthemes/
├── colors.py           # Color constants
├── palettes.py         # Palette classes
├── themes.py           # Theme functions
├── fonts/              # Font files and management
├── bigten.py           # Big Ten utilities
├── data/               # Dataset files and loaders
└── utils.py            # Utility functions
```

### 3. Write Tests

All new code should include tests:

```python
# tests/test_your_feature.py
import pytest
from msuthemes import your_feature

def test_your_feature():
    result = your_feature()
    assert result == expected_value
```

Run tests frequently:

```bash
# Run all tests
pytest

# Run specific test file
pytest tests/test_palettes.py

# Run specific test
pytest tests/test_colors.py::TestMSUColors::test_msu_green

# Run with markers
pytest -m unit
pytest -m integration
```

### 4. Code Quality

Format and lint your code:

```bash
# Format with black
black msuthemes/ tests/

# Check with flake8
flake8 msuthemes/ tests/

# Type check with mypy
mypy msuthemes/
```

### 5. Update Documentation

If you add new features:

- Update docstrings in code
- Add examples to relevant guide pages
- Update API reference if needed
- Add to changelog

### 6. Commit Your Changes

Write clear, descriptive commit messages:

```bash
git add .
git commit -m "Add new diverging color palette

- Implement msu_div2 palette with improved contrast
- Add tests for new palette
- Update palette documentation"
```

Follow commit message format:
- First line: Brief summary (50 chars or less)
- Blank line
- Detailed description with bullet points

### 7. Push and Create Pull Request

```bash
git push origin feature/your-feature-name
```

Create a pull request on GitHub with:
- Clear description of changes
- Reference to any related issues
- Screenshots for visual changes
- Test results

## Coding Standards

### Python Style

- Follow PEP 8
- Use Black for formatting (88 character line length)
- Use type hints where appropriate
- Write docstrings for all public functions/classes

### Docstring Format

Use NumPy-style docstrings:

```python
def function_name(param1, param2):
    """
    Brief description of function.

    Longer description if needed.

    Parameters
    ----------
    param1 : type
        Description of param1
    param2 : type
        Description of param2

    Returns
    -------
    return_type
        Description of return value

    Examples
    --------
    >>> function_name(value1, value2)
    expected_result
    """
    pass
```

### Testing Guidelines

- Use pytest framework
- Aim for >90% code coverage
- Use appropriate markers: `@pytest.mark.unit`, `@pytest.mark.integration`, etc.
- Use fixtures from `conftest.py`
- Always use `clean_matplotlib` fixture for matplotlib tests
- Close all matplotlib figures with `plt.close(fig)`

### Test Structure

Follow the Arrange-Act-Assert pattern:

```python
def test_example():
    # Arrange
    input_data = [1, 2, 3]
    expected = 6

    # Act
    result = sum(input_data)

    # Assert
    assert result == expected
```

## Types of Contributions

### Bug Reports

Submit bug reports via [GitHub Issues](https://github.com/emilioxavier/msuthemes-py/issues):

- Use clear, descriptive title
- Describe expected vs actual behavior
- Provide minimal reproducible example
- Include Python version, OS, and package version
- Include error messages and tracebacks

### Feature Requests

Submit feature requests via [GitHub Issues](https://github.com/emilioxavier/msuthemes-py/issues):

- Describe the feature and use case
- Explain why it would be useful
- Provide examples of desired API
- Consider implementation challenges

### Documentation

Documentation improvements are always welcome:

- Fix typos or unclear explanations
- Add examples to guides
- Improve API documentation
- Add visualization examples to gallery

### Code Contributions

Areas where contributions are especially welcome:

- New color palettes
- Additional Big Ten datasets
- Integration with other plotting libraries
- Performance improvements
- Bug fixes

## Project Structure

### Module Organization

```
msuthemes/
├── __init__.py         # Package exports
├── colors.py           # Color constants and definitions
├── palettes.py         # MSUPalette class and palette objects
├── themes.py           # theme_msu() and related functions
├── fonts/
│   ├── __init__.py     # Font registration functions
│   └── metropolis/     # Font files (.otf)
├── bigten.py           # Big Ten utilities
├── data/
│   ├── __init__.py     # Data loading functions
│   └── BigTen.csv      # Big Ten dataset
└── utils.py            # Color conversion utilities
```

### Test Organization

```
tests/
├── conftest.py              # Shared fixtures
├── test_colors.py           # Color constant tests
├── test_palettes.py         # Palette tests
├── test_themes.py           # Theme tests
├── test_fonts.py            # Font registration tests
├── test_bigten.py           # Big Ten utility tests
├── test_data.py             # Dataset loading tests
├── test_utils.py            # Utility function tests
└── test_integration.py      # End-to-end tests
```

## Common Development Tasks

### Adding a New Color

1. Add constant to `msuthemes/colors.py`
2. Update `__init__.py` exports if public
3. Add test to `tests/test_colors.py`
4. Document in `docs_mkdocs/guide/colors.md`

### Adding a New Palette

1. Define colors in `msuthemes/palettes.py`
2. Create `MSUPalette` instance
3. Add to `MSU_PALETTES` dictionary
4. Update `__init__.py` exports
5. Add tests to `tests/test_palettes.py`
6. Document in `docs_mkdocs/guide/palettes.md`

### Updating Documentation

```bash
# Build documentation locally
mkdocs serve

# View at http://localhost:8000
```

### Running Full Test Suite

```bash
# Run with custom script
./run_tests.sh

# Run with pytest directly
pytest --cov=msuthemes --cov-report=html --cov-report=term-missing

# Skip slow tests
pytest -m "not slow"

# Run specific marker
pytest -m unit
```

### Building Package

```bash
# Build package
./build_package.sh

# Or manually
rm -rf dist/ build/ *.egg-info
python -m build
twine check dist/*
```

## Code Review Process

Pull requests will be reviewed for:

1. **Functionality**: Does it work as intended?
2. **Tests**: Are there adequate tests with good coverage?
3. **Documentation**: Is it well-documented?
4. **Code quality**: Does it follow style guidelines?
5. **Compatibility**: Does it maintain backward compatibility?

## Getting Help

- **Questions**: Open a [GitHub Discussion](https://github.com/emilioxavier/msuthemes-py/discussions)
- **Bugs**: Open a [GitHub Issue](https://github.com/emilioxavier/msuthemes-py/issues)
- **Chat**: Contact via email (see README)

## License

By contributing to MSUthemes, you agree that your contributions will be licensed under the Creative Commons Attribution-ShareAlike 4.0 International (CC BY-SA 4.0) license.

## Recognition

Contributors will be acknowledged in:
- CHANGELOG.md
- GitHub contributors page
- Package metadata

Thank you for contributing to MSUthemes!
