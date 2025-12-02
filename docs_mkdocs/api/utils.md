# utils

The `utils` module provides utility functions for color conversion and validation.

## Module Overview

This module provides:

- Color format conversions (hex ↔ RGB)
- Color validation
- Hex color normalization
- Support for alpha channel

## Functions

::: msuthemes.utils.hex_to_rgb

::: msuthemes.utils.rgb_to_hex

::: msuthemes.utils.hex_to_rgba

::: msuthemes.utils.validate_hex_color

::: msuthemes.utils.normalize_hex

## Usage Examples

### Hex to RGB Conversion

```python
from msuthemes.utils import hex_to_rgb

# Convert hex to RGB
rgb = hex_to_rgb('#18453b')
print(rgb)  # (24, 69, 59)

# Works with or without '#'
rgb = hex_to_rgb('18453b')
print(rgb)  # (24, 69, 59)
```

### RGB to Hex Conversion

```python
from msuthemes.utils import rgb_to_hex

# Convert RGB to hex
hex_color = rgb_to_hex(24, 69, 59)
print(hex_color)  # '#18453b'

# Pass as tuple
rgb_tuple = (24, 69, 59)
hex_color = rgb_to_hex(*rgb_tuple)
print(hex_color)  # '#18453b'
```

### Hex to RGBA Conversion

```python
from msuthemes.utils import hex_to_rgba

# Convert with default alpha
rgba = hex_to_rgba('#18453b')
print(rgba)  # (24, 69, 59, 255)

# Convert with custom alpha
rgba = hex_to_rgba('#18453b', alpha=128)
print(rgba)  # (24, 69, 59, 128)

# Convert with normalized alpha
rgba = hex_to_rgba('#18453b', alpha=0.5, normalize=True)
print(rgba)  # (24, 69, 59, 0.5)
```

### Color Validation

```python
from msuthemes.utils import validate_hex_color

# Validate hex colors
is_valid = validate_hex_color('#18453b')
print(is_valid)  # True

is_valid = validate_hex_color('18453b')
print(is_valid)  # True

is_valid = validate_hex_color('#gggggg')
print(is_valid)  # False

is_valid = validate_hex_color('#12345')
print(is_valid)  # False
```

### Hex Normalization

```python
from msuthemes.utils import normalize_hex

# Normalize hex colors (ensure '#' prefix, lowercase)
normalized = normalize_hex('18453B')
print(normalized)  # '#18453b'

normalized = normalize_hex('#18453B')
print(normalized)  # '#18453b'

# Invalid colors raise ValueError
try:
    normalized = normalize_hex('invalid')
except ValueError as e:
    print(f"Error: {e}")
```

## Complete Conversion Pipeline

```python
from msuthemes.utils import (
    hex_to_rgb,
    rgb_to_hex,
    validate_hex_color,
    normalize_hex
)

# Start with a hex color
original = '#18453b'

# Validate
if validate_hex_color(original):
    # Normalize
    normalized = normalize_hex(original)
    print(f"Normalized: {normalized}")

    # Convert to RGB
    rgb = hex_to_rgb(normalized)
    print(f"RGB: {rgb}")

    # Convert back to hex
    hex_again = rgb_to_hex(*rgb)
    print(f"Back to hex: {hex_again}")

    # Verify round-trip
    print(f"Round-trip successful: {normalized == hex_again}")
```

## Working with MSU Colors

```python
from msuthemes import MSU_GREEN, MSU_ORANGE
from msuthemes.utils import hex_to_rgb, hex_to_rgba

# Get RGB values for MSU colors
msu_green_rgb = hex_to_rgb(MSU_GREEN)
print(f"MSU Green RGB: {msu_green_rgb}")

msu_orange_rgb = hex_to_rgb(MSU_ORANGE)
print(f"MSU Orange RGB: {msu_orange_rgb}")

# Get RGBA with transparency
msu_green_rgba = hex_to_rgba(MSU_GREEN, alpha=0.5, normalize=True)
print(f"MSU Green RGBA (50% opacity): {msu_green_rgba}")
```

## Integration with Matplotlib

```python
from msuthemes import MSU_GREEN
from msuthemes.utils import hex_to_rgb
import matplotlib.pyplot as plt

# Matplotlib accepts various color formats
rgb = hex_to_rgb(MSU_GREEN)
rgb_normalized = tuple(c/255 for c in rgb)

# All of these work:
plt.plot([1, 2, 3], [1, 4, 2], color=MSU_GREEN)  # hex string
plt.plot([1, 2, 3], [1, 4, 2], color=rgb_normalized)  # normalized RGB tuple
plt.show()
```

## Batch Conversion

```python
from msuthemes import msu_qual1
from msuthemes.utils import hex_to_rgb

# Convert all colors in a palette
palette = msu_qual1.as_hex()
rgb_palette = [hex_to_rgb(color) for color in palette]

for hex_color, rgb_color in zip(palette, rgb_palette):
    print(f"{hex_color} -> {rgb_color}")
```

## Error Handling

```python
from msuthemes.utils import (
    hex_to_rgb,
    rgb_to_hex,
    validate_hex_color
)

# Validate before conversion
color = '#18453b'
if validate_hex_color(color):
    rgb = hex_to_rgb(color)
    print(f"Valid color: {rgb}")
else:
    print("Invalid color")

# Handle invalid RGB values
try:
    hex_color = rgb_to_hex(256, 0, 0)  # 256 is out of range
except ValueError as e:
    print(f"Error: {e}")

# Handle invalid hex strings
try:
    rgb = hex_to_rgb('#gggggg')
except ValueError as e:
    print(f"Error: {e}")
```

## See Also

- [Colors](colors.md) - Color constants
- [Palettes](palettes.md) - Color palettes
