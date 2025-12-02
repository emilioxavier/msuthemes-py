# colors

The `colors` module provides access to MSU and Big Ten color constants.

## Module Overview

This module defines:

- MSU primary and secondary colors
- Big Ten primary and secondary colors for all 18 institutions
- Color dictionaries for programmatic access

## MSU Colors

::: msuthemes.colors.MSU_GREEN

::: msuthemes.colors.MSU_WHITE

::: msuthemes.colors.MSU_BLACK

::: msuthemes.colors.MSU_ORANGE

::: msuthemes.colors.MSU_TEAL

## Big Ten Color Dictionaries

::: msuthemes.colors.BIGTEN_COLORS_PRIMARY

::: msuthemes.colors.BIGTEN_COLORS_SECONDARY

## Usage Examples

### Basic Usage

```python
from msuthemes.colors import MSU_GREEN, MSU_WHITE
import matplotlib.pyplot as plt

plt.plot([1, 2, 3], [1, 4, 2], color=MSU_GREEN)
plt.show()
```

### Accessing Big Ten Colors

```python
from msuthemes.colors import BIGTEN_COLORS_PRIMARY

# Get Michigan State's primary color
msu_color = BIGTEN_COLORS_PRIMARY['Michigan State']
print(msu_color)  # '#18453b'

# Iterate over all Big Ten colors
for institution, color in BIGTEN_COLORS_PRIMARY.items():
    print(f"{institution}: {color}")
```

## See Also

- [Color Guide](../guide/colors.md) - Detailed color usage guide
- [bigten module](bigten.md) - Big Ten utility functions
