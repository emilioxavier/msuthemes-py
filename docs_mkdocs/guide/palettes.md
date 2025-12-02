# Palettes

MSUthemes provides carefully designed color palettes based on Michigan State University's brand colors. These palettes are optimized for data visualization and work seamlessly with matplotlib, seaborn, and plotly.

## Available Palettes

MSUthemes includes four built-in palettes:

| Palette | Type | Colors | Best For |
|---------|------|--------|----------|
| `msu_seq` | Sequential | 9 | Continuous data, heatmaps |
| `msu_div` | Diverging | 11 | Data with a meaningful midpoint |
| `msu_qual1` | Qualitative | 5 | Categorical data (main) |
| `msu_qual2` | Qualitative | 5 | Categorical data (alternative) |

## Using Palettes

### Getting a Palette

```python
from msuthemes import get_palette

# Get the sequential palette
seq_palette = get_palette('msu_seq')

# Get colors as hex codes
colors = seq_palette.as_hex()
print(colors)
# ['#18453b', '#1f5a4d', '#277060', ..., '#b8e6dd', '#d9f2ed']
```

### Listing Available Palettes

```python
from msuthemes import list_palettes

palettes = list_palettes()
print(palettes)
# ['msu_seq', 'msu_div', 'msu_qual1', 'msu_qual2']
```

### Direct Palette Access

You can also import palettes directly:

```python
from msuthemes import msu_seq, msu_div, msu_qual1, msu_qual2

# Use directly
colors = msu_qual1.as_hex()
```

## Palette Formats

### Hex Colors

Get colors as hex strings (default):

```python
from msuthemes import msu_qual1

colors = msu_qual1.as_hex()
print(colors)
# ['#18453b', '#ff6e1b', '#008183', '#ffb81c', '#6e005f']
```

### RGB Colors

Get colors as RGB tuples:

```python
from msuthemes import msu_qual1

colors = msu_qual1.as_rgb()
print(colors)
# [(24, 69, 59), (255, 110, 27), (0, 129, 131), (255, 184, 28), (110, 0, 95)]
```

### Matplotlib Colormap

Convert to matplotlib colormap for use with continuous data:

```python
import matplotlib.pyplot as plt
import numpy as np
from msuthemes import msu_seq

# Create colormap
cmap = msu_seq.as_matplotlib_cmap()

# Use in a plot
data = np.random.rand(10, 10)
plt.imshow(data, cmap=cmap)
plt.colorbar()
plt.show()
```

### Seaborn Palette

Convert to seaborn palette:

```python
import seaborn as sns
from msuthemes import msu_qual1

# Create seaborn palette
palette = msu_qual1.as_seaborn_palette()

# Use in a plot
sns.boxplot(data=data, palette=palette)
plt.show()
```

## Sequential Palette

The sequential palette (`msu_seq`) is ideal for continuous data that progresses from low to high values.

```python
import matplotlib.pyplot as plt
import numpy as np
from msuthemes import msu_seq, theme_msu

# Apply MSU theme
theme_msu()

# Create heatmap
data = np.random.rand(10, 10)
plt.imshow(data, cmap=msu_seq.as_matplotlib_cmap())
plt.colorbar(label='Value')
plt.title('Sequential Palette Example')
plt.show()
```

### Reversed Sequential

```python
from msuthemes import get_palette

# Get reversed sequential palette
seq_rev = get_palette('msu_seq', reverse=True)
colors = seq_rev.as_hex()
```

## Diverging Palette

The diverging palette (`msu_div`) is ideal for data with a meaningful midpoint (e.g., correlation coefficients, differences from a baseline).

```python
import matplotlib.pyplot as plt
import numpy as np
from msuthemes import msu_div, theme_msu

# Apply MSU theme
theme_msu()

# Create diverging heatmap
data = np.random.randn(10, 10)  # Data centered around 0
plt.imshow(data, cmap=msu_div.as_matplotlib_cmap(),
           vmin=-2, vmax=2, aspect='auto')
plt.colorbar(label='Deviation')
plt.title('Diverging Palette Example')
plt.show()
```

## Qualitative Palettes

Qualitative palettes (`msu_qual1`, `msu_qual2`) are ideal for categorical data with no inherent order.

### Main Qualitative Palette (msu_qual1)

```python
import matplotlib.pyplot as plt
from msuthemes import msu_qual1, theme_msu

# Apply MSU theme
theme_msu()

# Create bar chart
categories = ['A', 'B', 'C', 'D', 'E']
values = [23, 45, 56, 78, 32]

plt.bar(categories, values, color=msu_qual1.as_hex())
plt.title('Qualitative Palette Example')
plt.show()
```

### Alternative Qualitative Palette (msu_qual2)

```python
import matplotlib.pyplot as plt
from msuthemes import msu_qual2, theme_msu

# Apply MSU theme
theme_msu()

# Create line chart
x = range(5)
for i, color in enumerate(msu_qual2.as_hex()):
    y = [val + i * 2 for val in x]
    plt.plot(x, y, color=color, linewidth=2,
             label=f'Series {i+1}')

plt.legend()
plt.title('Alternative Qualitative Palette')
plt.show()
```

## Palette Customization

### Specifying Number of Colors

For continuous palettes (sequential and diverging), you can specify the number of colors through interpolation:

```python
from msuthemes import get_palette

# Get 5 colors from sequential palette
seq_5 = get_palette('msu_seq', n_colors=5)
print(seq_5.as_hex())

# Get 20 colors for finer gradation
seq_20 = get_palette('msu_seq', n_colors=20)
print(len(seq_20.as_hex()))  # 20
```

### Reversing Palettes

All palettes can be reversed:

```python
from msuthemes import get_palette

# Normal palette
normal = get_palette('msu_seq')

# Reversed palette
reversed_pal = get_palette('msu_seq', reverse=True)
```

## Integration with Visualization Libraries

### Matplotlib

```python
import matplotlib.pyplot as plt
from msuthemes import msu_seq

# As colormap
cmap = msu_seq.as_matplotlib_cmap()
plt.imshow(data, cmap=cmap)

# As discrete colors
colors = msu_seq.as_hex()
plt.bar(x, y, color=colors)
```

### Seaborn

```python
import seaborn as sns
from msuthemes import msu_qual1

# As palette
palette = msu_qual1.as_seaborn_palette()
sns.boxplot(data=data, palette=palette)

# Set as default palette
sns.set_palette(palette)
```

### Plotly

```python
import plotly.graph_objects as go
from msuthemes import msu_qual1

# Use hex colors directly
colors = msu_qual1.as_hex()
fig = go.Figure(data=[
    go.Bar(x=['A', 'B', 'C'],
           y=[1, 2, 3],
           marker_color=colors)
])
fig.show()
```

## Advanced Usage

### Creating Custom Palettes

You can create your own palettes using the `MSUPalette` class:

```python
from msuthemes.palettes import MSUPalette

# Create a custom qualitative palette
custom_colors = ['#18453b', '#ff6e1b', '#008183']
custom_palette = MSUPalette(
    name='my_custom',
    colors=custom_colors,
    palette_type='qual'
)

# Use it
hex_colors = custom_palette.as_hex()
```

### Accessing Palette Objects

All palettes are stored in a dictionary:

```python
from msuthemes.palettes import MSU_PALETTES

# Access any palette
seq_palette = MSU_PALETTES['msu_seq']
print(seq_palette.name)
print(seq_palette.palette_type)
print(seq_palette.as_hex())
```

## Best Practices

1. **Sequential palettes**: Use for ordered data (e.g., temperature, population)
2. **Diverging palettes**: Use for data with a meaningful midpoint (e.g., profit/loss, above/below average)
3. **Qualitative palettes**: Use for categorical data (e.g., species, departments, products)
4. **Color count**: Use 5-7 colors for qualitative data; humans struggle to distinguish more
5. **Accessibility**: Test your visualizations for colorblind accessibility

## See Also

- [Colors](colors.md) - Individual color values
- [Themes](themes.md) - Complete MSU styling
- [Gallery](../gallery/index.md) - Example visualizations
