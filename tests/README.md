# MSUthemes Test Suite

Comprehensive test suite for MSUthemes package.

## Test Structure

```
tests/
├── conftest.py              # Pytest configuration and shared fixtures
├── test_colors.py           # Color constants and Big Ten colors
├── test_palettes.py         # Palette generation and conversion
├── test_fonts.py            # Font registration and management
├── test_themes.py           # Theme application (matplotlib/seaborn)
├── test_bigten.py           # Big Ten utilities and name recognition
├── test_data.py             # Dataset loading and filtering
├── test_utils.py            # Utility functions (color conversion, etc.)
├── test_imports.py          # Import tests
├── test_integration.py      # Integration tests for workflows
└── README.md                # This file
```

## Running Tests

### Run all tests

```bash
pytest
```

### Run with coverage

```bash
pytest --cov=msuthemes --cov-report=html
```

### Run specific test categories

```bash
# Unit tests only
pytest -m unit

# Integration tests only
pytest -m integration

# Skip slow tests
pytest -m "not slow"

# Tests involving matplotlib
pytest -m mpl

# Tests involving fonts
pytest -m fonts

# Tests involving data loading
pytest -m data
```

### Run specific test files

```bash
pytest tests/test_colors.py
pytest tests/test_palettes.py
pytest tests/test_integration.py
```

### Run specific test classes or functions

```bash
pytest tests/test_colors.py::TestMSUColors
pytest tests/test_colors.py::TestMSUColors::test_msu_green
```

### Using the test runner script

```bash
# Run all tests with coverage
./run_tests.sh

# Run without coverage
./run_tests.sh --no-coverage

# Run only unit tests
./run_tests.sh --unit

# Run only integration tests
./run_tests.sh --integration

# Skip slow tests
./run_tests.sh --fast

# Quiet mode
./run_tests.sh --quiet
```

## Test Categories

Tests are marked with the following markers:

- `@pytest.mark.unit`: Unit tests for individual functions
- `@pytest.mark.integration`: Integration tests for complete workflows
- `@pytest.mark.slow`: Tests that take longer to run
- `@pytest.mark.mpl`: Tests involving matplotlib
- `@pytest.mark.fonts`: Tests involving font registration
- `@pytest.mark.data`: Tests involving dataset loading

## Test Coverage

To generate a coverage report:

```bash
pytest --cov=msuthemes --cov-report=html
```

Open `htmlcov/index.html` in your browser to view the detailed coverage report.

Target coverage: > 90%

## Shared Fixtures

Common fixtures available in all tests (defined in `conftest.py`):

- `sample_data`: Sample numerical data for plotting
- `sample_dataframe`: Sample pandas DataFrame
- `clean_matplotlib`: Resets matplotlib to defaults before each test
- `bigten_institutions`: List of Big Ten institutions
- `msu_colors`: MSU color constants
- `temp_plot`: Temporary matplotlib figure
- `color_tolerance`: Color comparison tolerance

## Writing New Tests

### Test File Template

```python
"""Tests for msuthemes.MODULE module."""

import pytest
from msuthemes import MODULE


class TestFeatureName:
    """Test description."""

    @pytest.mark.unit
    def test_something(self):
        """Test description."""
        # Arrange
        expected = ...

        # Act
        result = MODULE.function()

        # Assert
        assert result == expected
```

### Best Practices

1. **Use descriptive names**: Test names should clearly describe what they test
2. **One assertion per test**: Keep tests focused
3. **Use fixtures**: Leverage shared fixtures for common setup
4. **Mark your tests**: Use appropriate pytest markers
5. **Clean up**: Use `clean_matplotlib` fixture for matplotlib tests
6. **Test edge cases**: Include tests for error conditions
7. **Document tests**: Add docstrings to test classes and functions

### Testing matplotlib

Always use the `clean_matplotlib` fixture:

```python
@pytest.mark.mpl
def test_plot_something(clean_matplotlib):
    """Test matplotlib functionality."""
    theme_msu()
    fig, ax = plt.subplots()
    # ... create plot ...
    plt.close(fig)
```

### Testing with data

```python
@pytest.mark.data
def test_data_loading():
    """Test data loading."""
    data = load_bigten_data(institutions=['MSU'])
    assert len(data) > 0
```

## Continuous Integration

Tests are run automatically on:

- Every commit
- Every pull request
- Before releases

All tests must pass before code can be merged.

## Troubleshooting

### Font tests failing

If font tests fail, you may need to clear matplotlib's font cache:

```bash
rm -rf ~/.cache/matplotlib
```

### Import errors

Make sure MSUthemes is installed in development mode:

```bash
pip install -e .
```

### Slow tests

Skip slow tests during development:

```bash
pytest -m "not slow"
```

## Test Statistics

Current test count (as of Phase 8):

- Color tests: 30+
- Palette tests: 40+
- Font tests: 7
- Theme tests: 8
- Big Ten tests: 12
- Data tests: 14
- Utility tests: 40+
- Integration tests: 20+

**Total: 170+ tests**

## Coverage Goals

| Module | Target | Current |
|--------|--------|---------|
| colors | 100% | TBD |
| palettes | 95% | TBD |
| fonts | 90% | TBD |
| themes | 90% | TBD |
| bigten | 95% | TBD |
| data | 95% | TBD |
| utils | 100% | TBD |
| **Overall** | **> 90%** | **TBD** |

Run `pytest --cov=msuthemes` to check current coverage.
