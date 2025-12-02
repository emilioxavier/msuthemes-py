# Big Ten

MSUthemes includes comprehensive support for all 18 Big Ten Conference institutions, making it easy to create comparative visualizations and analyses across the conference.

## Overview

The Big Ten module provides:

- Official primary and secondary colors for all 18 institutions
- Flexible institution name recognition (handles abbreviations and aliases)
- Color palettes for comparative visualizations
- Integration with the Big Ten dataset

## Getting Big Ten Colors

### Basic Usage

```python
from msuthemes import get_bigten_colors

# Get colors for any institution
msu_colors = get_bigten_colors('Michigan State')
print(msu_colors)
# {'primary': '#18453b', 'secondary': '#ffffff'}

um_colors = get_bigten_colors('Michigan')
print(um_colors)
# {'primary': '#00274c', 'secondary': '#ffcb05'}
```

### Accessing Individual Colors

```python
from msuthemes import get_bigten_colors

# Get just the primary color
colors = get_bigten_colors('Ohio State')
primary = colors['primary']  # '#bb0000'

# Get just the secondary color
secondary = colors['secondary']  # '#666666'
```

## Institution Names and Aliases

The Big Ten module accepts many variations of institution names:

### Name Flexibility Examples

```python
from msuthemes import get_bigten_colors

# All of these work for Michigan State:
get_bigten_colors('Michigan State')
get_bigten_colors('Michigan State University')
get_bigten_colors('MSU')
get_bigten_colors('Spartans')
get_bigten_colors('michigan state')  # case-insensitive

# All of these work for Northwestern:
get_bigten_colors('Northwestern')
get_bigten_colors('Northwestern University')
get_bigten_colors('NU')
get_bigten_colors('Wildcats')

# All of these work for Ohio State:
get_bigten_colors('Ohio State')
get_bigten_colors('OSU')
get_bigten_colors('The Ohio State University')
get_bigten_colors('Buckeyes')
```

### List All Institutions

```python
from msuthemes import list_bigten_institutions

institutions = list_bigten_institutions()
print(institutions)
# ['Illinois', 'Indiana', 'Iowa', 'Maryland', 'Michigan',
#  'Michigan State', 'Minnesota', 'Nebraska', 'Northwestern',
#  'Ohio State', 'Oregon', 'Penn State', 'Purdue', 'Rutgers',
#  'UCLA', 'USC', 'Washington', 'Wisconsin']
```

## Big Ten Palettes

Create color palettes for comparative visualizations across institutions.

### Basic Palette Creation

```python
from msuthemes import bigten_palette

# Create palette for specific institutions
palette = bigten_palette(['Michigan State', 'Michigan', 'Ohio State'])
print(palette)
# ['#18453b', '#00274c', '#bb0000']
```

### Using Primary and Secondary Colors

```python
from msuthemes import bigten_palette

# Use primary colors (default)
primary_palette = bigten_palette(['MSU', 'Michigan', 'Wisconsin'])

# Use secondary colors
secondary_palette = bigten_palette(
    ['MSU', 'Michigan', 'Wisconsin'],
    color_type='secondary'
)
```

### Complete Conference Palette

```python
from msuthemes import bigten_palette, list_bigten_institutions

# Create palette for all Big Ten schools
all_institutions = list_bigten_institutions()
full_palette = bigten_palette(all_institutions)

# Use in visualization
import matplotlib.pyplot as plt
plt.bar(range(len(all_institutions)),
        [1] * len(all_institutions),
        color=full_palette)
plt.xticks(range(len(all_institutions)),
           all_institutions,
           rotation=45,
           ha='right')
plt.tight_layout()
plt.show()
```

## Visualization Examples

### Comparing Conference Rivals

```python
from msuthemes import bigten_palette, theme_msu
import matplotlib.pyplot as plt

# Apply MSU theme
theme_msu()

# Define institutions
schools = ['Michigan State', 'Michigan', 'Ohio State',
           'Penn State', 'Wisconsin']

# Get colors
colors = bigten_palette(schools)

# Create comparison plot
values = [85, 78, 92, 88, 81]
plt.bar(schools, values, color=colors)
plt.ylabel('Score')
plt.title('Big Ten Comparison')
plt.xticks(rotation=45, ha='right')
plt.tight_layout()
plt.show()
```

### Conference-Wide Analysis

```python
from msuthemes import bigten_palette, list_bigten_institutions, theme_msu
import matplotlib.pyplot as plt
import numpy as np

# Setup
theme_msu()
institutions = list_bigten_institutions()
colors = bigten_palette(institutions)

# Create data
values = np.random.randint(60, 100, size=len(institutions))

# Create horizontal bar chart
fig, ax = plt.subplots(figsize=(10, 8))
y_pos = np.arange(len(institutions))

ax.barh(y_pos, values, color=colors)
ax.set_yticks(y_pos)
ax.set_yticklabels(institutions)
ax.invert_yaxis()
ax.set_xlabel('Value')
ax.set_title('Big Ten Conference Overview')

plt.tight_layout()
plt.show()
```

### Time Series Comparison

```python
from msuthemes import bigten_palette, theme_msu
import matplotlib.pyplot as plt
import numpy as np

# Setup
theme_msu()
schools = ['Michigan State', 'Michigan', 'Ohio State']
colors = bigten_palette(schools)

# Create time series data
years = np.arange(2015, 2025)
fig, ax = plt.subplots(figsize=(10, 6))

for school, color in zip(schools, colors):
    values = np.random.randint(70, 95, size=len(years))
    ax.plot(years, values, color=color, linewidth=2.5,
            marker='o', markersize=6, label=school)

ax.set_xlabel('Year')
ax.set_ylabel('Metric')
ax.set_title('Trend Comparison')
ax.legend()
ax.grid(True, alpha=0.3)

plt.tight_layout()
plt.show()
```

## Working with Big Ten Data

Combine Big Ten colors with the dataset module:

```python
from msuthemes import (
    load_bigten_data,
    bigten_palette,
    theme_msu
)
import matplotlib.pyplot as plt

# Load data
df = load_bigten_data()

# Filter to recent years
df_recent = df[df['YEAR'] >= 2020]

# Calculate average by institution
avg_by_school = df_recent.groupby('INSTNM')['ADM_RATE'].mean()

# Get colors
colors = bigten_palette(avg_by_school.index.tolist())

# Plot
theme_msu()
plt.figure(figsize=(12, 6))
plt.bar(range(len(avg_by_school)),
        avg_by_school.values,
        color=colors)
plt.xticks(range(len(avg_by_school)),
           avg_by_school.index,
           rotation=45,
           ha='right')
plt.ylabel('Admission Rate')
plt.title('Average Admission Rates (2020-2023)')
plt.tight_layout()
plt.show()
```

## Advanced Usage

### Direct Color Dictionary Access

For advanced usage, access the color dictionaries directly:

```python
from msuthemes.colors import (
    BIGTEN_COLORS_PRIMARY,
    BIGTEN_COLORS_SECONDARY
)

# Iterate over all primary colors
for institution, color in BIGTEN_COLORS_PRIMARY.items():
    print(f"{institution}: {color}")

# Get specific colors
msu_primary = BIGTEN_COLORS_PRIMARY['Michigan State']
msu_secondary = BIGTEN_COLORS_SECONDARY['Michigan State']
```

### Custom Institution Groups

```python
from msuthemes import bigten_palette

# East Division schools
east_schools = [
    'Illinois', 'Indiana', 'Maryland', 'Michigan',
    'Michigan State', 'Northwestern', 'Ohio State',
    'Penn State', 'Rutgers'
]
east_colors = bigten_palette(east_schools)

# West Division schools
west_schools = [
    'Iowa', 'Minnesota', 'Nebraska', 'Oregon',
    'Purdue', 'UCLA', 'USC', 'Washington', 'Wisconsin'
]
west_colors = bigten_palette(west_schools)
```

### Error Handling

```python
from msuthemes import get_bigten_colors

try:
    colors = get_bigten_colors('Invalid School')
except ValueError as e:
    print(f"Error: {e}")
    # Handle invalid institution name
```

## Big Ten Color Reference

### Complete Color Table

| Institution | Primary | Secondary |
|------------|---------|-----------|
| Illinois | `#e84a27` | `#13294b` |
| Indiana | `#990000` | `#edebeb` |
| Iowa | `#000000` | `#ffcd00` |
| Maryland | `#e03a3e` | `#ffd520` |
| Michigan | `#00274c` | `#ffcb05` |
| Michigan State | `#18453b` | `#ffffff` |
| Minnesota | `#7a0019` | `#ffcc33` |
| Nebraska | `#e41c38` | `#fefdfa` |
| Northwestern | `#4e2a84` | `#ffffff` |
| Ohio State | `#bb0000` | `#666666` |
| Oregon | `#004f00` | `#ffc425` |
| Penn State | `#041e42` | `#ffffff` |
| Purdue | `#9d9795` | `#daaa00` |
| Rutgers | `#cc0033` | `#5f6a72` |
| UCLA | `#2d68c4` | `#ffc72c` |
| USC | `#990000` | `#ffcc00` |
| Washington | `#4b2e83` | `#b7a57a` |
| Wisconsin | `#c5050c` | `#ffffff` |

## Tips and Best Practices

1. **Consistent naming**: Use the canonical names from `list_bigten_institutions()` for consistency
2. **Color type**: Use primary colors for main elements, secondary for accents
3. **Ordering**: Order institutions alphabetically or by a meaningful metric
4. **Color accessibility**: Test visualizations for colorblind accessibility
5. **Legend clarity**: Include institution names in legends for clarity

## See Also

- [Colors](colors.md) - Color utilities and constants
- [Datasets](datasets.md) - Big Ten dataset
- [Gallery](../gallery/bigten.md) - Big Ten visualization examples
