# API Reference

Complete API documentation for all MSUthemes modules.

## Module Overview

MSUthemes is organized into seven core modules:

### [colors](colors.md)
MSU and Big Ten institution colors

- Primary, secondary, and accent MSU colors
- All 18 Big Ten institutions' colors
- Color dictionaries and constants

### [palettes](palettes.md)
Color palettes for data visualization

- Sequential, diverging, and qualitative palettes
- `MSUPalette` class for palette manipulation
- Conversion to matplotlib/seaborn formats

### [themes](themes.md)
matplotlib and seaborn themes

- `theme_msu()` - Apply MSU branding to plots
- `set_msu_style()` - seaborn integration
- `reset_theme()` - Return to defaults

### [fonts](fonts.md)
Metropolis font management

- `register_metropolis_fonts()` - Register fonts with matplotlib
- `is_metropolis_available()` - Check font availability
- `get_font_path()` - Get path to font files

### [bigten](bigten.md)
Big Ten institution utilities

- `get_bigten_colors()` - Get institution colors
- `bigten_palette()` - Create Big Ten palettes
- `list_bigten_institutions()` - List all institutions
- Institution name normalization and aliases

### [data](data.md)
BigTen dataset access

- `load_bigten_data()` - Load institutional data (1996-2023)
- `get_bigten_summary()` - Summary statistics
- `get_dataset_info()` - Dataset metadata

### [utils](utils.md)
Utility functions

- Color conversion (hex, RGB, RGBA)
- Color validation
- Internal helper functions

## Quick Reference

### Common Imports

```python
# Colors
from msuthemes import colors
from msuthemes.colors import MSU_GREEN, MSU_WHITE

# Palettes
from msuthemes import palettes
from msuthemes.palettes import msu_seq, msu_div, msu_qual1

# Themes
from msuthemes import theme_msu, set_msu_style, reset_theme

# Big Ten
from msuthemes import get_bigten_colors, bigten_palette

# Data
from msuthemes import load_bigten_data, get_bigten_summary

# Fonts
from msuthemes import register_metropolis_fonts, is_metropolis_available
```

### Common Patterns

**Apply MSU theme:**
```python
from msuthemes import theme_msu
theme_msu()
```

**Get color palette:**
```python
from msuthemes import palettes
colors = palettes.msu_seq.as_hex(n_colors=5)
```

**Load Big Ten data:**
```python
from msuthemes import load_bigten_data
df = load_bigten_data(institutions=['MSU'], years=[2020, 2021, 2022])
```

## Module Details

Click on any module name above to see detailed API documentation including:

- Function signatures and parameters
- Return values and types
- Usage examples
- Related functions

## Type Hints

MSUthemes uses Python type hints for better code clarity and IDE support:

```python
def get_bigten_colors(
    institutions: Union[str, List[str]],
    color_type: str = "primary"
) -> Union[str, Dict[str, str]]:
    ...
```

## Docstring Format

All functions use NumPy-style docstrings:

```python
def function_name(param1, param2):
    """
    Short description.

    Longer description with more details.

    Parameters
    ----------
    param1 : type
        Description of param1
    param2 : type
        Description of param2

    Returns
    -------
    type
        Description of return value

    Examples
    --------
    >>> function_name(value1, value2)
    result
    """
```

## Version Information

```python
import msuthemes
print(msuthemes.__version__)  # '0.1.0'
```

## See Also

- [User Guide](../guide/colors.md) - Conceptual documentation and tutorials
- [Gallery](../gallery/index.md) - Example visualizations
- [Quick Start](../getting-started/quickstart.md) - Get started quickly
