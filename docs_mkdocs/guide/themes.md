# Themes

MSUthemes provides a complete theming system that applies Michigan State University's brand guidelines to your matplotlib plots. The theme includes colors, fonts, spacing, and styling to create professional, on-brand visualizations.

## Quick Start

Apply the MSU theme to all your plots:

```python
from msuthemes import theme_msu
import matplotlib.pyplot as plt

# Apply the theme
theme_msu()

# Create a plot - it will automatically use MSU styling
plt.plot([1, 2, 3, 4], [1, 4, 2, 3])
plt.title('My MSU-Themed Plot')
plt.show()
```

## Theme Features

The MSU theme includes:

- **Colors**: MSU green color cycle and MSU-branded colors
- **Fonts**: Metropolis font family (MSU's official typeface)
- **Styling**: Clean, professional appearance with appropriate spacing
- **Grid**: Optional gridlines for improved readability
- **Spines**: Configurable axes borders

## Basic Usage

### Default Theme

```python
from msuthemes import theme_msu
import matplotlib.pyplot as plt
import numpy as np

# Apply theme with defaults
theme_msu()

# Create a plot
x = np.linspace(0, 10, 100)
y = np.sin(x)
plt.plot(x, y, linewidth=2)
plt.xlabel('X-axis')
plt.ylabel('Y-axis')
plt.title('Sine Wave with MSU Theme')
plt.show()
```

### With Grid

```python
from msuthemes import theme_msu
import matplotlib.pyplot as plt

# Apply theme with grid
theme_msu(grid=True)

# Your plot will now have gridlines
plt.plot([1, 2, 3, 4], [1, 4, 2, 3])
plt.show()
```

## Customization Options

### Base Size

Control the overall size of text elements:

```python
from msuthemes import theme_msu

# Larger text for presentations
theme_msu(base_size=14)

# Smaller text for publications
theme_msu(base_size=9)
```

The `base_size` parameter controls:
- Axis labels
- Tick labels
- Title sizes
- Legend text

### Grid Options

Control gridline appearance:

```python
# Enable grid
theme_msu(grid=True)

# Enable only major gridlines (default when grid=True)
theme_msu(grid=True)

# Disable grid (default)
theme_msu(grid=False)
```

### Axes Spines

Control which axes borders (spines) are visible:

```python
# Show only bottom and left spines (default)
theme_msu(spines='bl')

# Show all spines
theme_msu(spines='all')

# Show only bottom spine
theme_msu(spines='b')

# Show no spines
theme_msu(spines='none')
```

Spine options:
- `'bl'`: Bottom and left (default)
- `'all'`: All four spines
- `'b'`: Bottom only
- `'l'`: Left only
- `'t'`: Top only
- `'r'`: Right only
- `'none'`: No spines

### Font Control

Control Metropolis font registration:

```python
# Register fonts automatically (default)
theme_msu(register_fonts=True)

# Skip font registration (if already registered)
theme_msu(register_fonts=False)
```

### Complete Example

```python
from msuthemes import theme_msu
import matplotlib.pyplot as plt
import numpy as np

# Apply customized theme
theme_msu(
    base_size=12,
    grid=True,
    spines='bl',
    register_fonts=True
)

# Create multiple subplots
fig, axes = plt.subplots(2, 2, figsize=(12, 10))

# Plot 1: Line plot
x = np.linspace(0, 10, 100)
axes[0, 0].plot(x, np.sin(x))
axes[0, 0].set_title('Sine Wave')

# Plot 2: Scatter plot
axes[0, 1].scatter(np.random.rand(50), np.random.rand(50))
axes[0, 1].set_title('Scatter Plot')

# Plot 3: Bar plot
axes[1, 0].bar(['A', 'B', 'C', 'D'], [3, 7, 2, 5])
axes[1, 0].set_title('Bar Chart')

# Plot 4: Histogram
axes[1, 1].hist(np.random.randn(1000), bins=30)
axes[1, 1].set_title('Histogram')

plt.tight_layout()
plt.show()
```

## Seaborn Integration

MSUthemes also provides seaborn styling:

```python
from msuthemes import set_msu_style
import seaborn as sns

# Apply MSU style to seaborn
set_msu_style()

# Use seaborn plotting functions
sns.boxplot(data=data)
plt.show()
```

### Seaborn with MSU Palettes

```python
from msuthemes import set_msu_style, msu_qual1
import seaborn as sns

# Apply style
set_msu_style()

# Use MSU palette
palette = msu_qual1.as_seaborn_palette()
sns.boxplot(data=data, palette=palette)
plt.show()
```

## Resetting the Theme

Return to matplotlib defaults:

```python
from msuthemes import reset_theme

# Reset to default matplotlib style
reset_theme()
```

Or use matplotlib's built-in reset:

```python
import matplotlib.pyplot as plt

# Reset to matplotlib defaults
plt.rcdefaults()
```

## Font Management

### Checking Font Availability

```python
from msuthemes import is_metropolis_available

# Check if Metropolis fonts are registered
available = is_metropolis_available()
print(f"Metropolis available: {available}")
```

### Manual Font Registration

```python
from msuthemes import register_metropolis_fonts

# Manually register Metropolis fonts
register_metropolis_fonts()
```

### Font Troubleshooting

If fonts don't appear:

1. Clear matplotlib's font cache:
```bash
rm -rf ~/.cache/matplotlib
```

2. Re-register fonts:
```python
from msuthemes import register_metropolis_fonts
register_metropolis_fonts()
```

3. Verify registration:
```python
from msuthemes import is_metropolis_available
print(is_metropolis_available())
```

## Theme Components

The MSU theme modifies these matplotlib rcParams:

### Text and Fonts
- Font family: Metropolis (sans-serif)
- Font sizes scaled by `base_size`
- Figure title size: 1.2× base
- Axes title size: 1.1× base
- Axes label size: 1.0× base
- Tick label size: 0.9× base
- Legend size: 0.9× base

### Colors
- Color cycle: MSU green, orange, teal, and additional colors
- Axes face color: White
- Axes edge color: Dark gray
- Grid color: Light gray
- Text color: Black

### Layout
- Figure DPI: 100
- Figure face color: White
- Axes line width: 1.5
- Tick width: 1.5
- Grid line width: 0.8

### Grids
- Grid style: Dashed lines
- Grid alpha: 0.3
- Grid color: Light gray

## Complete Theming Example

```python
from msuthemes import theme_msu, msu_qual1
import matplotlib.pyplot as plt
import numpy as np

# Apply full MSU theme
theme_msu(base_size=11, grid=True, spines='bl')

# Create professional visualization
fig, ax = plt.subplots(figsize=(10, 6))

# Multiple series with MSU colors
x = np.linspace(0, 10, 50)
colors = msu_qual1.as_hex()

for i, color in enumerate(colors):
    y = np.sin(x + i * 0.5) + i
    ax.plot(x, y, color=color, linewidth=2.5,
            label=f'Series {i+1}')

ax.set_xlabel('Time (seconds)')
ax.set_ylabel('Amplitude')
ax.set_title('Multi-Series Time Plot with MSU Theme')
ax.legend(frameon=False)

plt.tight_layout()
plt.show()
```

## Tips and Best Practices

1. **Apply theme early**: Call `theme_msu()` before creating plots
2. **Consistent sizing**: Use the same `base_size` across related figures
3. **Grid usage**: Enable grids for data-heavy plots, disable for simple plots
4. **Color cycles**: The theme sets up an MSU color cycle, but you can override with specific colors
5. **Font availability**: The theme works even if Metropolis fonts aren't available (falls back to sans-serif)
6. **Save settings**: Store your preferred theme settings in a configuration file for reuse

## See Also

- [Colors](colors.md) - Color values and palettes
- [Fonts](fonts.md) - Metropolis font details
- [Gallery](../gallery/msu.md) - Example themed plots
