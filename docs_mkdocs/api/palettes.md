# palettes

The `palettes` module provides color palettes optimized for data visualization.

## Module Overview

This module provides:

- Four built-in MSU-branded palettes
- `MSUPalette` class for palette management
- Functions to access and list palettes
- Format conversion for matplotlib, seaborn, and plotly

## Classes

::: msuthemes.palettes.MSUPalette
    options:
      show_root_heading: true
      show_source: true
      members:
        - __init__
        - as_hex
        - as_rgb
        - as_matplotlib_cmap
        - as_seaborn_palette

## Palette Objects

::: msuthemes.palettes.msu_seq

::: msuthemes.palettes.msu_div

::: msuthemes.palettes.msu_qual1

::: msuthemes.palettes.msu_qual2

## Functions

::: msuthemes.palettes.get_palette

::: msuthemes.palettes.list_palettes

## Palette Dictionary

::: msuthemes.palettes.MSU_PALETTES

## Usage Examples

### Getting a Palette

```python
from msuthemes import get_palette

# Get sequential palette
seq = get_palette('msu_seq')
colors = seq.as_hex()
print(colors)
```

### Using with Matplotlib

```python
from msuthemes import msu_seq
import matplotlib.pyplot as plt
import numpy as np

data = np.random.rand(10, 10)
plt.imshow(data, cmap=msu_seq.as_matplotlib_cmap())
plt.colorbar()
plt.show()
```

### Using with Seaborn

```python
from msuthemes import msu_qual1
import seaborn as sns

palette = msu_qual1.as_seaborn_palette()
sns.boxplot(data=data, palette=palette)
plt.show()
```

### Creating Custom Palettes

```python
from msuthemes.palettes import MSUPalette

# Create custom palette
custom = MSUPalette(
    name='my_palette',
    colors=['#18453b', '#ff6e1b', '#008183'],
    palette_type='qual'
)

hex_colors = custom.as_hex()
rgb_colors = custom.as_rgb()
```

## See Also

- [Palette Guide](../guide/palettes.md) - Detailed palette usage guide
- [Gallery](../gallery/basic.md) - Example visualizations
