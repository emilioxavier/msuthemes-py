"""Pytest configuration and shared fixtures for MSUthemes tests."""

import pytest
import matplotlib
import matplotlib.pyplot as plt
import numpy as np
import pandas as pd


# Use non-interactive backend for testing
matplotlib.use('Agg')


@pytest.fixture(scope="session")
def sample_data():
    """Generate sample data for testing."""
    np.random.seed(42)
    return {
        'x': np.linspace(0, 10, 100),
        'y': np.sin(np.linspace(0, 10, 100)),
        'random': np.random.randn(100),
    }


@pytest.fixture(scope="session")
def sample_dataframe():
    """Generate sample pandas DataFrame for testing."""
    np.random.seed(42)
    return pd.DataFrame({
        'category': ['A', 'B', 'C', 'D', 'E'] * 20,
        'value': np.random.randn(100),
        'group': np.random.choice(['Group1', 'Group2'], 100),
    })


@pytest.fixture(scope="function")
def clean_matplotlib():
    """Reset matplotlib to defaults before each test."""
    # Store original rcParams
    original_params = matplotlib.rcParams.copy()

    yield

    # Restore original rcParams
    matplotlib.rcParams.update(original_params)

    # Close all figures
    plt.close('all')


@pytest.fixture(scope="session")
def bigten_institutions():
    """List of Big Ten institutions for testing."""
    return [
        'Illinois', 'Indiana', 'Iowa', 'MSU', 'Maryland',
        'Michigan', 'Minnesota', 'Nebraska', 'Northwestern',
        'Ohio State', 'Oregon', 'Penn State', 'Purdue',
        'Rutgers', 'UCLA', 'USoCal', 'Washington', 'Wisconsin'
    ]


@pytest.fixture(scope="session")
def msu_colors():
    """MSU color constants for testing."""
    return {
        'green': '#18453B',
        'white': '#FFFFFF',
        'black': '#000000',
        'orange': '#FF6F00',
        'teal': '#008183',
        'purple': '#5B3256',
        'grey': '#C3C4C6',
    }


@pytest.fixture(scope="function")
def temp_plot(clean_matplotlib):
    """Create a temporary plot for testing."""
    fig, ax = plt.subplots()
    yield fig, ax
    plt.close(fig)


@pytest.fixture(scope="session")
def color_tolerance():
    """Color comparison tolerance for testing."""
    return 1e-6


def pytest_configure(config):
    """Configure pytest with custom settings."""
    config.addinivalue_line(
        "markers", "unit: Unit tests for individual functions"
    )
    config.addinivalue_line(
        "markers", "integration: Integration tests for workflows"
    )
    config.addinivalue_line(
        "markers", "slow: Slow-running tests"
    )
    config.addinivalue_line(
        "markers", "mpl: Tests involving matplotlib"
    )
    config.addinivalue_line(
        "markers", "fonts: Tests involving font registration"
    )
    config.addinivalue_line(
        "markers", "data: Tests involving dataset loading"
    )
