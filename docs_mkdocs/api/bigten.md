# bigten

The `bigten` module provides utilities for working with Big Ten Conference institution colors.

## Module Overview

This module provides:

- Color retrieval for all 18 Big Ten institutions
- Palette creation for comparative visualizations
- Flexible institution name recognition
- Institution listing functions

## Functions

::: msuthemes.bigten.get_bigten_colors

::: msuthemes.bigten.bigten_palette

::: msuthemes.bigten.list_bigten_institutions

::: msuthemes.bigten.normalize_institution_name

## Constants

::: msuthemes.bigten.INSTITUTION_ALIASES

## Usage Examples

### Getting Institution Colors

```python
from msuthemes import get_bigten_colors

# Get colors for any institution
msu_colors = get_bigten_colors('Michigan State')
print(msu_colors)
# {'primary': '#18453b', 'secondary': '#ffffff'}

# Access individual colors
primary = msu_colors['primary']
secondary = msu_colors['secondary']
```

### Creating Palettes

```python
from msuthemes import bigten_palette

# Create palette for specific schools
schools = ['Michigan State', 'Michigan', 'Ohio State']
colors = bigten_palette(schools)

# Use in plot
import matplotlib.pyplot as plt
plt.bar(schools, [80, 75, 85], color=colors)
plt.show()
```

### Using Primary and Secondary Colors

```python
from msuthemes import bigten_palette

# Primary colors (default)
primary_colors = bigten_palette(['MSU', 'Michigan', 'Wisconsin'])

# Secondary colors
secondary_colors = bigten_palette(
    ['MSU', 'Michigan', 'Wisconsin'],
    color_type='secondary'
)
```

### Name Flexibility

```python
from msuthemes import get_bigten_colors

# All of these work:
get_bigten_colors('Michigan State')
get_bigten_colors('MSU')
get_bigten_colors('Spartans')
get_bigten_colors('michigan state')  # case-insensitive
```

### Listing Institutions

```python
from msuthemes import list_bigten_institutions

# Get all Big Ten institutions
institutions = list_bigten_institutions()
print(institutions)
# ['Illinois', 'Indiana', 'Iowa', ...]
```

### Normalizing Institution Names

```python
from msuthemes.bigten import normalize_institution_name

# Normalize various inputs
canonical = normalize_institution_name('MSU')
print(canonical)  # 'Michigan State'

canonical = normalize_institution_name('Spartans')
print(canonical)  # 'Michigan State'

canonical = normalize_institution_name('The Ohio State University')
print(canonical)  # 'Ohio State'
```

### Complete Conference Visualization

```python
from msuthemes import (
    bigten_palette,
    list_bigten_institutions,
    theme_msu
)
import matplotlib.pyplot as plt
import numpy as np

# Apply theme
theme_msu()

# Get all institutions and colors
institutions = list_bigten_institutions()
colors = bigten_palette(institutions)

# Create data
values = np.random.randint(60, 100, size=len(institutions))

# Plot
fig, ax = plt.subplots(figsize=(12, 8))
ax.barh(range(len(institutions)), values, color=colors)
ax.set_yticks(range(len(institutions)))
ax.set_yticklabels(institutions)
ax.set_xlabel('Value')
ax.set_title('Big Ten Conference Comparison')

plt.tight_layout()
plt.show()
```

### Error Handling

```python
from msuthemes import get_bigten_colors

try:
    colors = get_bigten_colors('Invalid School')
except ValueError as e:
    print(f"Error: {e}")
    # Handle invalid institution
```

## Supported Institutions

All 18 Big Ten Conference institutions:

- Illinois
- Indiana
- Iowa
- Maryland
- Michigan
- Michigan State
- Minnesota
- Nebraska
- Northwestern
- Ohio State
- Oregon
- Penn State
- Purdue
- Rutgers
- UCLA
- USC
- Washington
- Wisconsin

## Institution Aliases

Each institution supports multiple name variations. Examples:

**Michigan State:**
- Michigan State
- Michigan State University
- MSU
- Spartans
- State

**Ohio State:**
- Ohio State
- The Ohio State University
- OSU
- Buckeyes

**Northwestern:**
- Northwestern
- Northwestern University
- NU
- Wildcats

See `INSTITUTION_ALIASES` constant for complete alias mapping.

## See Also

- [Big Ten Guide](../guide/bigten.md) - Detailed Big Ten usage guide
- [Colors](colors.md) - Color constants
- [Data](data.md) - Big Ten dataset
- [Gallery](../gallery/bigten.md) - Big Ten visualization examples
