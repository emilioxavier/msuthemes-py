# MSUthemes R to Python Conversion Roadmap

## Executive Summary

This document outlines the process for converting the MSUthemes R package (currently on CRAN) into a Python package. MSUthemes provides color palettes and themes for Michigan State University and all Big Ten Conference institutions, designed for data visualization with ggplot2 in R. The Python version will provide similar functionality for matplotlib, seaborn, and plotly.

---

## 1. Package Overview Analysis

### Current R Package Structure

**Core Functionality:**
- MSU-branded color palettes (sequential, diverging, qualitative)
- Big Ten institutional color palettes (18 institutions)
- ggplot2 themes using Metropolis font
- Dataset: BigTen (historical data 1996-2023 for all Big Ten institutions)
- Helper functions for color selection and matching

**Key Components:**
- Sequential palettes: `msu_seq`, `msu_seq_red`, `msu_seq_blue`
- Diverging palettes: `msu_div`
- Qualitative palettes: `msu_qual1`, `msu_qual2`
- Individual colors: `msu_green`, `msu_orange`, `msu_teal`, `msu_grellow`
- Big Ten colors: `bigten_colors_primary`, `bigten_colors_secondary`
- Theme function: `theme_MSU()`
- Helper: `get_bigten_colors()`

**Dependencies (R):**
- ggplot2
- showtext (for font management)
- scales

---

## 2. Python Package Design

### 2.1 Package Name
**Recommended:** `msuthemes` (lowercase, following Python conventions)

### 2.2 Target Visualization Libraries
1. **Primary:** matplotlib (most widely used)
2. **Secondary:** seaborn (built on matplotlib, popular for statistical graphics)
3. **Optional:** plotly (interactive visualizations)

### 2.3 Python Package Structure

```
msuthemes/
├── msuthemes/
│   ├── __init__.py
│   ├── colors.py              # Color palette definitions
│   ├── palettes.py            # Palette generation functions
│   ├── themes.py              # Matplotlib/seaborn themes
│   ├── bigten.py             # Big Ten specific functionality
│   ├── data/
│   │   ├── __init__.py
│   │   ├── bigten_dataset.csv  # BigTen dataset
│   │   └── data_loader.py      # Data loading utilities
│   ├── fonts/
│   │   └── metropolis/         # Metropolis font files
│   └── utils.py               # Helper functions
├── tests/
│   ├── __init__.py
│   ├── test_colors.py
│   ├── test_palettes.py
│   ├── test_themes.py
│   └── test_bigten.py
├── examples/
│   ├── basic_usage.py
│   ├── msu_plots.py
│   └── bigten_comparisons.py
├── docs/
│   ├── conf.py
│   ├── index.rst
│   ├── installation.rst
│   ├── quickstart.rst
│   └── api/
├── setup.py
├── pyproject.toml
├── README.md
├── LICENSE
├── MANIFEST.in
└── requirements.txt
```

---

## 3. Detailed Conversion Steps

### Phase 1: Setup and Infrastructure (Week 1)

#### 3.1 Repository Setup
- [ ] Create GitHub repository: `msuthemes-python` or `msuthemes`
- [ ] Initialize git with proper `.gitignore` for Python
- [ ] Set up project structure
- [ ] Create virtual environment
- [ ] Set up CI/CD pipeline (GitHub Actions)

#### 3.2 Project Configuration Files
- [ ] Create `pyproject.toml` with build system configuration
- [ ] Create `setup.py` for backward compatibility
- [ ] Create `requirements.txt` and `requirements-dev.txt`
- [ ] Configure `MANIFEST.in` to include fonts and data files

**Key Dependencies:**
```python
# Core dependencies
matplotlib >= 3.5.0
seaborn >= 0.12.0
numpy >= 1.20.0
pandas >= 1.3.0

# Optional dependencies
plotly >= 5.0.0  # For interactive plots

# Development dependencies
pytest >= 7.0.0
sphinx >= 4.0.0
black >= 22.0.0
flake8 >= 4.0.0
```

### Phase 2: Color System Implementation (Week 2)

#### 3.3 Color Palette Definition (`colors.py`)

**Task:** Extract all color values from R package and define in Python

```python
# colors.py structure
from typing import Dict, List

# MSU Primary Colors
MSU_GREEN: str = "#18453B"
MSU_WHITE: str = "#FFFFFF"

# MSU Secondary Colors
MSU_BLACK: str = "#000000"
MSU_SILVER: str = "#C1C6C8"
MSU_GRAY: str = "#909090"

# MSU Accent Colors
MSU_ORANGE: str = "#D14D28"
MSU_TEAL: str = "#005F83"
MSU_GRELLOW: str = "#849E2A"
# ... etc

# Big Ten Primary Colors Dictionary
BIGTEN_COLORS_PRIMARY: Dict[str, str] = {
    "MSU": MSU_GREEN,
    "Michigan": "#00274C",
    "Ohio State": "#BB0000",
    # ... all 18 institutions
}

# Big Ten Secondary Colors Dictionary
BIGTEN_COLORS_SECONDARY: Dict[str, str] = {
    # ... all 18 institutions
}
```

**Steps:**
- [ ] Extract all hex color codes from R package
- [ ] Define individual MSU colors as constants
- [ ] Create dictionaries for Big Ten colors
- [ ] Document color values with references to brand guidelines

#### 3.4 Palette Generation (`palettes.py`)

**Task:** Create palette objects compatible with matplotlib/seaborn

```python
# palettes.py structure
from matplotlib.colors import LinearSegmentedColormap, ListedColormap
import numpy as np

class MSUPalette:
    """Base class for MSU color palettes"""
    
    def __init__(self, colors: List[str], name: str, palette_type: str):
        self.colors = colors
        self.name = name
        self.palette_type = palette_type  # 'sequential', 'diverging', 'qualitative'
    
    def as_matplotlib_cmap(self, n_colors: int = None):
        """Return matplotlib colormap"""
        pass
    
    def as_hex(self, n_colors: int = None) -> List[str]:
        """Return list of hex colors"""
        pass

# Sequential palettes
msu_seq = MSUPalette([...], "msu_seq", "sequential")
msu_seq_red = MSUPalette([...], "msu_seq_red", "sequential")

# Diverging palettes
msu_div = MSUPalette([...], "msu_div", "diverging")

# Qualitative palettes
msu_qual1 = MSUPalette([...], "msu_qual1", "qualitative")
```

**Steps:**
- [ ] Create `MSUPalette` class for palette management
- [ ] Implement methods for matplotlib colormap conversion
- [ ] Implement methods for seaborn palette conversion
- [ ] Create all MSU sequential palettes
- [ ] Create all MSU diverging palettes
- [ ] Create all MSU qualitative palettes
- [ ] Create Big Ten aggregate palettes

### Phase 3: Font Integration (Week 3)

#### 3.5 Metropolis Font Setup (`fonts/`)

**Task:** Include Metropolis font and create font management utilities

**Steps:**
- [ ] Download Metropolis font from https://fontsource.org/fonts/metropolis
- [ ] Place font files (.ttf) in `msuthemes/fonts/metropolis/` directory
- [ ] Create font registration function for matplotlib
- [ ] Handle cross-platform font installation (macOS, Windows, Linux)
- [ ] Test font fallback if Metropolis not available

```python
# In themes.py or utils.py
import matplotlib.font_manager as fm
from pathlib import Path

def register_metropolis_font():
    """Register Metropolis font with matplotlib"""
    font_dir = Path(__file__).parent / 'fonts' / 'metropolis'
    for font_file in font_dir.glob('*.ttf'):
        fm.fontManager.addfont(str(font_file))
    # Clear font cache
    fm._rebuild()
```

**Considerations:**
- Font licensing (Metropolis is open source)
- Font file size impact on package size
- Cross-platform compatibility
- Fallback fonts if Metropolis unavailable

### Phase 4: Theme Implementation (Week 4)

#### 3.6 Matplotlib Theme (`themes.py`)

**Task:** Create `theme_MSU()` equivalent for matplotlib

```python
# themes.py
import matplotlib.pyplot as plt
from matplotlib import rcParams

def theme_msu(
    base_size: float = 11,
    base_family: str = "Metropolis",
    use_grid: bool = True,
    grid_color: str = "#E5E5E5",
    **kwargs
) -> None:
    """
    Apply MSU branding to matplotlib plots.
    
    Parameters
    ----------
    base_size : float
        Base font size
    base_family : str
        Font family to use
    use_grid : bool
        Whether to show grid lines
    grid_color : str
        Color for grid lines
    **kwargs
        Additional rcParams to override
    """
    # Register Metropolis font
    register_metropolis_font()
    
    # Set rcParams
    rcParams.update({
        'font.family': base_family,
        'font.size': base_size,
        'axes.facecolor': 'white',
        'axes.edgecolor': colors.MSU_BLACK,
        'axes.linewidth': 1.0,
        'axes.grid': use_grid,
        'grid.color': grid_color,
        'grid.linestyle': '-',
        'grid.linewidth': 0.5,
        'grid.alpha': 0.5,
        'xtick.color': colors.MSU_BLACK,
        'ytick.color': colors.MSU_BLACK,
        'legend.frameon': False,
        'figure.facecolor': 'white',
        # ... more parameters
    })
    
    # Apply any custom overrides
    rcParams.update(kwargs)
```

**Steps:**
- [ ] Analyze `theme_MSU()` from R package
- [ ] Map ggplot2 theme elements to matplotlib rcParams
- [ ] Create function to apply MSU theme
- [ ] Create context manager for temporary theme application
- [ ] Test with various plot types

#### 3.7 Seaborn Theme Integration

```python
def set_msu_style(context: str = "notebook", **kwargs):
    """
    Set seaborn style with MSU branding.
    
    Parameters
    ----------
    context : str
        Seaborn context ('paper', 'notebook', 'talk', 'poster')
    **kwargs
        Additional parameters
    """
    import seaborn as sns
    
    # Apply matplotlib theme first
    theme_msu(**kwargs)
    
    # Set seaborn context
    sns.set_context(context)
```

### Phase 5: Big Ten Functionality (Week 5)

#### 3.8 Big Ten Helper Functions (`bigten.py`)

**Task:** Implement Big Ten-specific color selection and utilities

```python
# bigten.py
from typing import List, Dict, Union
from .colors import BIGTEN_COLORS_PRIMARY, BIGTEN_COLORS_SECONDARY

def get_bigten_colors(
    institutions: Union[str, List[str]],
    color_type: str = "primary"
) -> Union[str, Dict[str, str]]:
    """
    Get Big Ten institutional colors.
    
    Parameters
    ----------
    institutions : str or list of str
        Institution name(s)
    color_type : str
        'primary' or 'secondary'
        
    Returns
    -------
    str or dict
        Color hex code or dictionary of institution: color
        
    Examples
    --------
    >>> get_bigten_colors("MSU")
    '#18453B'
    
    >>> get_bigten_colors(["MSU", "Michigan"])
    {'MSU': '#18453B', 'Michigan': '#00274C'}
    """
    color_dict = (
        BIGTEN_COLORS_PRIMARY if color_type == "primary"
        else BIGTEN_COLORS_SECONDARY
    )
    
    if isinstance(institutions, str):
        return color_dict.get(institutions)
    else:
        return {inst: color_dict.get(inst) for inst in institutions}

def bigten_palette(color_type: str = "primary") -> List[str]:
    """Return list of all Big Ten colors"""
    if color_type == "primary":
        return list(BIGTEN_COLORS_PRIMARY.values())
    else:
        return list(BIGTEN_COLORS_SECONDARY.values())
```

**Steps:**
- [ ] Implement `get_bigten_colors()` function
- [ ] Add input validation and error handling
- [ ] Create palette generation for all 18 institutions
- [ ] Add institution name normalization (handle variations)

### Phase 6: Data Integration (Week 6)

#### 3.9 BigTen Dataset (`data/`)

**Task:** Convert and include the BigTen dataset

**Steps:**
- [ ] Export BigTen dataset from R to CSV
- [ ] Create data loading utilities
- [ ] Document dataset variables
- [ ] Create data access functions

```python
# data/data_loader.py
import pandas as pd
from pathlib import Path

def load_bigten_data() -> pd.DataFrame:
    """
    Load BigTen institutional dataset.
    
    Returns
    -------
    pd.DataFrame
        BigTen dataset with institutional data from 1996-2023
        
    Examples
    --------
    >>> df = load_bigten_data()
    >>> df[df['name'] == 'MSU']
    """
    data_path = Path(__file__).parent / 'bigten_dataset.csv'
    return pd.read_csv(data_path)
```

### Phase 7: Documentation (Week 7)

#### 3.10 User Documentation

**Create documentation using Sphinx:**

- [ ] **Installation Guide** (`docs/installation.rst`)
  - PyPI installation: `pip install msuthemes`
  - Font installation instructions for each OS
  - Troubleshooting common issues

- [ ] **Quickstart Guide** (`docs/quickstart.rst`)
  - Basic usage examples
  - Creating MSU-branded plots
  - Using Big Ten colors

- [ ] **API Reference** (`docs/api/`)
  - Automatic documentation from docstrings
  - Examples for each function

- [ ] **Gallery** (`docs/gallery/`)
  - Example plots showcasing different palettes
  - Big Ten comparison examples
  - Best practices

- [ ] **Migration Guide** (for R users)
  - Side-by-side R and Python code examples
  - Conceptual differences
  - Feature parity matrix

**README.md Structure:**
```markdown
# MSUthemes

MSU and Big Ten color palettes and themes for Python data visualization.

## Installation
## Quick Start
## Features
## Examples
## Documentation
## License
## Contributing
```

#### 3.11 Code Documentation

- [ ] Write comprehensive docstrings (Google or NumPy style)
- [ ] Add type hints throughout codebase
- [ ] Create inline code comments for complex logic
- [ ] Document all public APIs

### Phase 8: Testing (Week 8)

#### 3.12 Test Suite Development

**Test Categories:**

1. **Unit Tests** (`tests/test_colors.py`)
   - [ ] Test color constant values
   - [ ] Test Big Ten color dictionaries
   - [ ] Validate hex color formats

2. **Palette Tests** (`tests/test_palettes.py`)
   - [ ] Test palette generation
   - [ ] Test matplotlib colormap conversion
   - [ ] Test seaborn palette conversion
   - [ ] Test color interpolation

3. **Theme Tests** (`tests/test_themes.py`)
   - [ ] Test theme application
   - [ ] Test font registration
   - [ ] Test with different plot types
   - [ ] Test context manager

4. **Big Ten Tests** (`tests/test_bigten.py`)
   - [ ] Test helper functions
   - [ ] Test institution name variations
   - [ ] Test error handling

5. **Integration Tests**
   - [ ] Test complete plotting workflows
   - [ ] Test with different backends
   - [ ] Test cross-platform compatibility

**Testing Tools:**
```python
# requirements-dev.txt
pytest>=7.0.0
pytest-cov>=3.0.0
pytest-mpl>=0.16.0  # For matplotlib plot testing
```

### Phase 9: Examples and Tutorials (Week 9)

#### 3.13 Create Example Scripts

**Example 1: Basic MSU Plot** (`examples/basic_usage.py`)
```python
import matplotlib.pyplot as plt
from msuthemes import theme_msu, colors
import numpy as np

# Apply MSU theme
theme_msu()

# Create plot
fig, ax = plt.subplots(figsize=(8, 6))
x = np.linspace(0, 10, 100)
y = np.sin(x)

ax.plot(x, y, color=colors.MSU_GREEN, linewidth=2)
ax.set_xlabel('X axis')
ax.set_ylabel('Y axis')
ax.set_title('MSU-Branded Plot')

plt.show()
```

**Example 2: Big Ten Comparison** (`examples/bigten_comparisons.py`)
```python
import matplotlib.pyplot as plt
import pandas as pd
from msuthemes import theme_msu, get_bigten_colors, load_bigten_data

# Load data
df = load_bigten_data()
df_2023 = df[df['entry_term'] == 2023]

# Get colors
institutions = ["MSU", "Michigan", "Ohio State", "Northwestern"]
colors = get_bigten_colors(institutions)

# Create plot
theme_msu()
fig, ax = plt.subplots(figsize=(10, 6))

for inst in institutions:
    data = df_2023[df_2023['name'] == inst]
    ax.bar(inst, data['UGDS'].values[0], color=colors[inst])

ax.set_ylabel('Undergraduate Enrollment')
ax.set_title('Big Ten Enrollment Comparison (2023)')
plt.xticks(rotation=45)
plt.tight_layout()
plt.show()
```

**Steps:**
- [ ] Create 5-10 comprehensive examples
- [ ] Cover all major use cases
- [ ] Include both matplotlib and seaborn examples
- [ ] Add Jupyter notebooks for interactive tutorials

### Phase 10: Packaging and Distribution (Week 10)

#### 3.14 Package Building

**pyproject.toml configuration:**
```toml
[build-system]
requires = ["setuptools>=61.0", "wheel"]
build-backend = "setuptools.build_meta"

[project]
name = "msuthemes"
version = "1.0.0"
description = "MSU and Big Ten color palettes and themes for Python"
authors = [
    {name = "Your Name", email = "your.email@msu.edu"}
]
readme = "README.md"
license = {text = "CC-BY-SA-4.0"}
requires-python = ">=3.8"
classifiers = [
    "Development Status :: 4 - Beta",
    "Intended Audience :: Science/Research",
    "License :: OSI Approved :: Creative Commons License",
    "Programming Language :: Python :: 3",
    "Programming Language :: Python :: 3.8",
    "Programming Language :: Python :: 3.9",
    "Programming Language :: Python :: 3.10",
    "Programming Language :: Python :: 3.11",
    "Topic :: Scientific/Engineering :: Visualization",
]
dependencies = [
    "matplotlib>=3.5.0",
    "numpy>=1.20.0",
    "pandas>=1.3.0",
]

[project.optional-dependencies]
seaborn = ["seaborn>=0.12.0"]
plotly = ["plotly>=5.0.0"]
dev = [
    "pytest>=7.0.0",
    "pytest-cov>=3.0.0",
    "sphinx>=4.0.0",
    "black>=22.0.0",
    "flake8>=4.0.0",
]

[project.urls]
Homepage = "https://github.com/yourusername/msuthemes"
Documentation = "https://msuthemes.readthedocs.io"
Repository = "https://github.com/yourusername/msuthemes"
```

**MANIFEST.in:**
```
include README.md
include LICENSE
recursive-include msuthemes/fonts *.ttf
recursive-include msuthemes/data *.csv
```

**Steps:**
- [ ] Configure build system
- [ ] Test local installation: `pip install -e .`
- [ ] Build distribution packages: `python -m build`
- [ ] Test installation from wheel
- [ ] Validate package metadata

#### 3.15 PyPI Publication

**Pre-publication checklist:**
- [ ] Verify all tests pass
- [ ] Check code style (black, flake8)
- [ ] Verify documentation builds correctly
- [ ] Test on multiple Python versions (3.8, 3.9, 3.10, 3.11)
- [ ] Test on multiple OS (Windows, macOS, Linux)
- [ ] Create release notes
- [ ] Tag version in git

**Publication steps:**
```bash
# Install build tools
pip install build twine

# Build package
python -m build

# Check package
twine check dist/*

# Upload to TestPyPI first
twine upload --repository testpypi dist/*

# Test installation from TestPyPI
pip install --index-url https://test.pypi.org/simple/ msuthemes

# If all good, upload to PyPI
twine upload dist/*
```

### Phase 11: CI/CD and Maintenance (Ongoing)

#### 3.16 Continuous Integration

**GitHub Actions Workflow** (`.github/workflows/ci.yml`):
```yaml
name: CI

on: [push, pull_request]

jobs:
  test:
    runs-on: ${{ matrix.os }}
    strategy:
      matrix:
        os: [ubuntu-latest, windows-latest, macos-latest]
        python-version: ['3.8', '3.9', '3.10', '3.11']
    
    steps:
    - uses: actions/checkout@v3
    - name: Set up Python
      uses: actions/setup-python@v4
      with:
        python-version: ${{ matrix.python-version }}
    - name: Install dependencies
      run: |
        pip install -e .[dev]
    - name: Run tests
      run: |
        pytest --cov=msuthemes tests/
    - name: Check code style
      run: |
        black --check msuthemes/
        flake8 msuthemes/
```

**Steps:**
- [ ] Set up GitHub Actions for automated testing
- [ ] Configure coverage reporting (Codecov)
- [ ] Set up documentation auto-build (Read the Docs)
- [ ] Configure automated PyPI releases on tag

---

## 4. Migration from R to Python: Key Considerations

### 4.1 Conceptual Differences

| Aspect | R (ggplot2) | Python (matplotlib) |
|--------|-------------|---------------------|
| Theme application | `+ theme_MSU()` | `theme_msu()` before plotting |
| Color scales | `scale_fill_msu_d()` | `ax.bar(..., color=palette.colors)` |
| Palette usage | Built into scale functions | Manual color assignment or colormap |
| Font handling | showtext package | matplotlib font_manager |

### 4.2 Feature Parity Matrix

| Feature | R Package | Python Status |
|---------|-----------|---------------|
| MSU sequential palettes | ✅ | 📋 To implement |
| MSU diverging palettes | ✅ | 📋 To implement |
| MSU qualitative palettes | ✅ | 📋 To implement |
| Big Ten colors (18 schools) | ✅ | 📋 To implement |
| Metropolis font | ✅ | 📋 To implement |
| BigTen dataset | ✅ | 📋 To implement |
| ggplot2 theme | ✅ | 📋 Adapt for matplotlib |
| Helper functions | ✅ | 📋 To implement |

### 4.3 Python-Specific Enhancements

**Opportunities beyond R package:**
- Interactive plots with plotly
- Better integration with pandas DataFrames
- Jupyter notebook support
- Easier cross-platform font handling
- Type hints for better IDE support

---

## 5. Metropolis Font Integration Details

### 5.1 Font File Acquisition
- **Source:** https://fontsource.org/fonts/metropolis
- **License:** SIL Open Font License 1.1 (freely distributable)
- **Files needed:**
  - Metropolis-Regular.ttf
  - Metropolis-Bold.ttf
  - Metropolis-Medium.ttf
  - Metropolis-Light.ttf

### 5.2 Font Registration Strategy

**Option 1: Bundle fonts with package** (Recommended)
```python
# Automatically register fonts when package is imported
import matplotlib.font_manager as fm
from pathlib import Path

def _register_fonts():
    """Register bundled fonts with matplotlib"""
    font_dir = Path(__file__).parent / 'fonts' / 'metropolis'
    for font_path in font_dir.glob('*.ttf'):
        fm.fontManager.addfont(str(font_path))
    fm._rebuild()

# Call on import
_register_fonts()
```

**Option 2: System font installation**
- Provide instructions for manual installation
- Create helper script for automated installation
- Check if font is already installed before bundling

### 5.3 Font Fallback Handling
```python
def get_font_family() -> str:
    """Get appropriate font family with fallback"""
    available_fonts = [f.name for f in fm.fontManager.ttflist]
    
    if 'Metropolis' in available_fonts:
        return 'Metropolis'
    else:
        # Fallback to system default
        import warnings
        warnings.warn(
            "Metropolis font not found. Using system default. "
            "For best results, install Metropolis font."
        )
        return 'sans-serif'
```

---

## 6. Testing Strategy

### 6.1 Visual Regression Testing

Use `pytest-mpl` for comparing generated plots:

```python
import pytest
import matplotlib.pyplot as plt
from msuthemes import theme_msu, colors

@pytest.mark.mpl_image_compare
def test_basic_plot_theme():
    """Test that MSU theme produces consistent output"""
    theme_msu()
    fig, ax = plt.subplots()
    ax.plot([1, 2, 3], [1, 2, 3], color=colors.MSU_GREEN)
    return fig
```

### 6.2 Cross-Platform Testing

- Test on Windows, macOS, Linux
- Test with different matplotlib backends
- Test font rendering on each platform

### 6.3 Version Compatibility Testing

- Python 3.8, 3.9, 3.10, 3.11+
- Different matplotlib versions
- With and without optional dependencies

---

## 7. Documentation Strategy

### 7.1 Documentation Hierarchy

1. **README.md** - Quick start and overview
2. **Installation Guide** - Detailed installation instructions
3. **User Guide** - Comprehensive usage examples
4. **API Reference** - Auto-generated from docstrings
5. **Migration Guide** - For R users
6. **Gallery** - Visual examples
7. **Contributing Guide** - For contributors

### 7.2 Documentation Tools

- **Sphinx** - Documentation generator
- **Read the Docs** - Hosting
- **sphinx-gallery** - Automatic example gallery
- **numpydoc** or **google-style** docstrings

---

## 8. Timeline Summary

| Phase | Duration | Key Deliverables |
|-------|----------|------------------|
| 1. Setup | Week 1 | Repository, project structure, CI/CD |
| 2. Colors | Week 2 | All color definitions, palette classes |
| 3. Fonts | Week 3 | Metropolis font integration |
| 4. Themes | Week 4 | Matplotlib/seaborn theme functions |
| 5. Big Ten | Week 5 | Big Ten helper functions |
| 6. Data | Week 6 | BigTen dataset integration |
| 7. Documentation | Week 7 | Complete documentation suite |
| 8. Testing | Week 8 | Comprehensive test coverage |
| 9. Examples | Week 9 | Tutorial notebooks and examples |
| 10. Packaging | Week 10 | PyPI publication |

**Total estimated time:** 10-12 weeks for full implementation

---

## 9. Success Criteria

- [ ] All MSU color palettes accurately reproduced
- [ ] All Big Ten institutional colors available
- [ ] Metropolis font properly integrated
- [ ] BigTen dataset accessible via simple API
- [ ] Theme produces visually similar output to R version
- [ ] Package installable via `pip install msuthemes`
- [ ] Documentation complete and published
- [ ] Test coverage >90%
- [ ] Works on Python 3.8+
- [ ] Works on Windows, macOS, Linux
- [ ] PyPI package published
- [ ] Example gallery demonstrating all features

---

## 10. Maintenance and Future Development

### 10.1 Versioning Strategy
- Follow Semantic Versioning (SemVer)
- Major version: Breaking changes
- Minor version: New features, backward compatible
- Patch version: Bug fixes

### 10.2 Future Enhancements
- Plotly theme support
- Additional institutional themes (if requested)
- Color accessibility features (colorblind-safe palettes)
- Interactive palette picker tool
- VS Code extension for easy color selection
- Bokeh support
- Altair/Vega-Lite support

### 10.3 Community Engagement
- Respond to GitHub issues promptly
- Accept community contributions
- Maintain changelog
- Regular releases

---

## 11. Resources and References

### Official Documentation
- MSU Brand Guidelines: https://brand.msu.edu
- MSU Color Palette: https://brand.msu.edu/visual/color-palette
- MSU Typography: https://brand.msu.edu/visual/typography
- Metropolis Font: https://fontsource.org/fonts/metropolis

### Python Package Development
- Python Packaging Guide: https://packaging.python.org
- Matplotlib Documentation: https://matplotlib.org
- Seaborn Documentation: https://seaborn.pydata.org
- Sphinx Documentation: https://www.sphinx-doc.org

### Original R Package
- CRAN: https://cran.r-project.org/package=MSUthemes
- GitHub: https://github.com/emilioxavier/MSUthemes
- Documentation: https://emilioxavier.github.io/MSUthemes/

---

## 12. Contact and Collaboration

For questions or collaboration on this conversion project:
- Original R package author: Emilio Xavier Esposito (emilio@msu.edu)
- R package GitHub: https://github.com/emilioxavier/MSUthemes/issues

---

## Appendix A: Quick Reference Commands

```bash
# Development setup
git clone <repository-url>
cd msuthemes
python -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate
pip install -e .[dev]

# Testing
pytest
pytest --cov=msuthemes

# Code quality
black msuthemes/
flake8 msuthemes/

# Documentation
cd docs
make html

# Building package
python -m build

# Installing locally
pip install -e .

# Publishing to PyPI
twine upload dist/*
```

---

## Appendix B: File Checklist

Essential files for Python package:

```
✓ msuthemes/
  ✓ __init__.py
  ✓ colors.py
  ✓ palettes.py
  ✓ themes.py
  ✓ bigten.py
  ✓ utils.py
  ✓ data/
    ✓ __init__.py
    ✓ bigten_dataset.csv
    ✓ data_loader.py
  ✓ fonts/
    ✓ metropolis/
      ✓ Metropolis-Regular.ttf
      ✓ Metropolis-Bold.ttf
      ✓ Metropolis-Medium.ttf
✓ tests/
  ✓ __init__.py
  ✓ test_colors.py
  ✓ test_palettes.py
  ✓ test_themes.py
  ✓ test_bigten.py
✓ docs/
  ✓ conf.py
  ✓ index.rst
  ✓ installation.rst
  ✓ quickstart.rst
✓ examples/
  ✓ basic_usage.py
  ✓ bigten_comparisons.py
✓ .github/
  ✓ workflows/
    ✓ ci.yml
✓ setup.py
✓ pyproject.toml
✓ README.md
✓ LICENSE
✓ MANIFEST.in
✓ requirements.txt
✓ requirements-dev.txt
✓ .gitignore
```

---

**End of Roadmap**
