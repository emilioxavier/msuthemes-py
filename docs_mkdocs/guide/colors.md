# Colors

MSUthemes provides access to Michigan State University's official brand colors and all Big Ten Conference institution colors.

## MSU Colors

### Primary Colors

The core MSU brand colors are green and white:

```python
from msuthemes import MSU_GREEN, MSU_WHITE

print(MSU_GREEN)  # '#18453b'
print(MSU_WHITE)  # '#ffffff'
```

### Secondary Colors

MSU's secondary color palette includes additional colors for accents and emphasis:

```python
from msuthemes import MSU_BLACK, MSU_ORANGE, MSU_TEAL

print(MSU_BLACK)   # '#000000'
print(MSU_ORANGE)  # '#ff6e1b'
print(MSU_TEAL)    # '#008183'
```

### Color Usage Example

```python
import matplotlib.pyplot as plt
from msuthemes import MSU_GREEN, MSU_WHITE, MSU_ORANGE

fig, ax = plt.subplots(figsize=(10, 6))
ax.bar(['Category A', 'Category B', 'Category C'],
       [25, 40, 30],
       color=[MSU_GREEN, MSU_ORANGE, MSU_TEAL])
ax.set_facecolor(MSU_WHITE)
plt.show()
```

## Big Ten Colors

MSUthemes includes official primary and secondary colors for all 18 Big Ten Conference institutions.

### Accessing Big Ten Colors

Use the `get_bigten_colors()` function to retrieve colors for any Big Ten institution:

```python
from msuthemes import get_bigten_colors

# Get MSU colors
msu_colors = get_bigten_colors('Michigan State')
print(msu_colors)
# {'primary': '#18453b', 'secondary': '#ffffff'}

# Get Michigan colors
um_colors = get_bigten_colors('Michigan')
print(um_colors)
# {'primary': '#00274c', 'secondary': '#ffcb05'}

# Get Ohio State colors
osu_colors = get_bigten_colors('Ohio State')
print(osu_colors)
# {'primary': '#bb0000', 'secondary': '#666666'}
```

### Institution Name Flexibility

The function accepts various name formats and aliases:

```python
# All of these work for Michigan State:
get_bigten_colors('Michigan State')
get_bigten_colors('MSU')
get_bigten_colors('Spartans')
get_bigten_colors('michigan state')  # case-insensitive

# All of these work for Northwestern:
get_bigten_colors('Northwestern')
get_bigten_colors('NU')
get_bigten_colors('Wildcats')
```

### All Big Ten Institutions

You can list all available institutions:

```python
from msuthemes import list_bigten_institutions

institutions = list_bigten_institutions()
print(institutions)
# ['Illinois', 'Indiana', 'Iowa', 'Maryland', 'Michigan',
#  'Michigan State', 'Minnesota', 'Nebraska', 'Northwestern',
#  'Ohio State', 'Oregon', 'Penn State', 'Purdue', 'Rutgers',
#  'UCLA', 'USC', 'Washington', 'Wisconsin']
```

### Color Dictionary Access

For advanced usage, you can access the color dictionaries directly:

```python
from msuthemes.colors import BIGTEN_COLORS_PRIMARY, BIGTEN_COLORS_SECONDARY

# Get all primary colors
for institution, color in BIGTEN_COLORS_PRIMARY.items():
    print(f"{institution}: {color}")

# Get all secondary colors
for institution, color in BIGTEN_COLORS_SECONDARY.items():
    print(f"{institution}: {color}")
```

## Color Utilities

MSUthemes includes utility functions for working with colors:

```python
from msuthemes.utils import hex_to_rgb, rgb_to_hex, validate_hex_color

# Convert hex to RGB
rgb = hex_to_rgb('#18453b')
print(rgb)  # (24, 69, 59)

# Convert RGB to hex
hex_color = rgb_to_hex(24, 69, 59)
print(hex_color)  # '#18453b'

# Validate hex colors
is_valid = validate_hex_color('#18453b')
print(is_valid)  # True
```

## Direct Color Imports

All MSU colors can be imported directly from the main package:

```python
from msuthemes import (
    MSU_GREEN,
    MSU_WHITE,
    MSU_BLACK,
    MSU_ORANGE,
    MSU_TEAL
)
```

Or from the colors module:

```python
from msuthemes.colors import (
    MSU_GREEN,
    MSU_WHITE,
    MSU_BLACK,
    MSU_ORANGE,
    MSU_TEAL,
    BIGTEN_COLORS_PRIMARY,
    BIGTEN_COLORS_SECONDARY
)
```

## Color Values Reference

### MSU Color Palette

| Color Name | Hex Code | RGB |
|-----------|----------|-----|
| MSU Green | `#18453b` | (24, 69, 59) |
| MSU White | `#ffffff` | (255, 255, 255) |
| MSU Black | `#000000` | (0, 0, 0) |
| MSU Orange | `#ff6e1b` | (255, 110, 27) |
| MSU Teal | `#008183` | (0, 129, 131) |

### Big Ten Primary Colors

| Institution | Primary Color |
|------------|--------------|
| Illinois | `#e84a27` |
| Indiana | `#990000` |
| Iowa | `#000000` |
| Maryland | `#e03a3e` |
| Michigan | `#00274c` |
| Michigan State | `#18453b` |
| Minnesota | `#7a0019` |
| Nebraska | `#e41c38` |
| Northwestern | `#4e2a84` |
| Ohio State | `#bb0000` |
| Oregon | `#004f00` |
| Penn State | `#041e42` |
| Purdue | `#9d9795` |
| Rutgers | `#cc0033` |
| UCLA | `#2d68c4` |
| USC | `#990000` |
| Washington | `#4b2e83` |
| Wisconsin | `#c5050c` |

See the [Big Ten guide](bigten.md) for more information on working with Big Ten colors and creating comparative visualizations.
