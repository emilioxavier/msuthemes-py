# Installation Guide

This guide covers the installation of MSUthemes and its dependencies.

## Requirements

MSUthemes requires:

- **Python 3.8 or higher**
- **NumPy** >= 1.20.0
- **matplotlib** >= 3.5.0
- **pandas** >= 1.3.0

Optional dependencies:

- **seaborn** >= 0.12.0 (for seaborn integration)
- **plotly** >= 5.0.0 (for plotly support)

## Installing MSUthemes

### Via pip (Recommended)

Install MSUthemes using pip:

```bash
pip install msuthemes
```

To install with optional dependencies:

=== "With seaborn"
    ```bash
    pip install msuthemes[seaborn]
    ```

=== "With plotly"
    ```bash
    pip install msuthemes[plotly]
    ```

=== "With all optional dependencies"
    ```bash
    pip install msuthemes[all]
    ```

### From Source

To install the latest development version from GitHub:

```bash
git clone https://github.com/emilioxavier/msuthemes-py.git
cd msuthemes-py
pip install -e .
```

For development with all dev dependencies:

```bash
pip install -e .[dev]
```

## Verifying Installation

To verify that MSUthemes is installed correctly:

```python
import msuthemes
print(msuthemes.__version__)

# Check available modules
from msuthemes import colors, palettes, themes, bigten, data
print("✓ MSUthemes installed successfully!")
```

## Font Installation

MSUthemes includes the Metropolis font, which is automatically bundled with the package. The font needs to be registered with matplotlib:

```python
from msuthemes import register_metropolis_fonts, is_metropolis_available

# Register Metropolis fonts
register_metropolis_fonts()

# Verify font is available
if is_metropolis_available():
    print("✓ Metropolis font is ready!")
else:
    print("⚠ Metropolis font not available. You may need to:")
    print("  1. Clear matplotlib font cache")
    print("  2. Restart Python")
```

### Clearing matplotlib Font Cache

If the Metropolis font is not recognized after registration, you may need to clear matplotlib's font cache:

=== "Linux/macOS"
    ```bash
    rm -rf ~/.cache/matplotlib
    rm -rf ~/.matplotlib
    ```

=== "Windows"
    ```bash
    del /s %USERPROFILE%\.matplotlib\*
    del /s %LOCALAPPDATA%\matplotlib\*
    ```

After clearing the cache, restart Python and register the fonts again.

## Troubleshooting

### Import Errors

If you encounter import errors:

```python
ModuleNotFoundError: No module named 'msuthemes'
```

Make sure MSUthemes is installed in your current Python environment:

```bash
pip list | grep msuthemes
```

### Font Not Found

If matplotlib doesn't recognize the Metropolis font:

1. Clear matplotlib's font cache (see above)
2. Restart your Python session
3. Re-register the fonts:

```python
from msuthemes import register_metropolis_fonts
register_metropolis_fonts(verbose=True)
```

The `verbose=True` option will print detailed information about font registration.

### Dataset Not Found

If you get a "Dataset not found" error when loading BigTen data:

```python
FileNotFoundError: BigTen dataset not found
```

This usually means the package wasn't installed correctly. Try reinstalling:

```bash
pip uninstall msuthemes
pip install msuthemes --no-cache-dir
```

### Dependency Conflicts

If you encounter dependency conflicts, create a fresh virtual environment:

=== "venv"
    ```bash
    # Create virtual environment
    python -m venv msu_env

    # Activate (Linux/macOS)
    source msu_env/bin/activate

    # Activate (Windows)
    msu_env\Scripts\activate

    # Install MSUthemes
    pip install msuthemes
    ```

=== "conda"
    ```bash
    # Create conda environment
    conda create -n msu_env python=3.11

    # Activate environment
    conda activate msu_env

    # Install MSUthemes
    pip install msuthemes
    ```

## Platform-Specific Notes

### Windows

On Windows, you may need to install Microsoft Visual C++ 14.0 or greater for some dependencies.

[Download Visual C++ Build Tools](https://visualstudio.microsoft.com/visual-cpp-build-tools/)

### macOS

On macOS, make sure you have Xcode command line tools installed:

```bash
xcode-select --install
```

### Linux

On Linux, you may need to install additional system dependencies:

=== "Ubuntu/Debian"
    ```bash
    sudo apt-get install python3-dev build-essential
    ```

=== "Fedora/RHEL"
    ```bash
    sudo dnf install python3-devel gcc
    ```

## Getting Help

If you encounter issues not covered here:

1. Check the [GitHub Issues](https://github.com/emilioxavier/msuthemes-py/issues)
2. Search for similar problems in closed issues
3. Open a new issue with:
    - Your Python version (`python --version`)
    - Your MSUthemes version (`pip show msuthemes`)
    - The complete error message
    - A minimal reproducible example

## Next Steps

Now that MSUthemes is installed, check out the [Quick Start](quickstart.md) guide to start creating MSU-branded visualizations!
