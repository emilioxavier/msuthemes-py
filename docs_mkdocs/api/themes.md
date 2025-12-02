# themes

The `themes` module provides complete MSU theming for matplotlib plots.

## Module Overview

This module provides:

- Complete MSU theme application
- Seaborn style integration
- Theme reset functionality
- Automatic font registration

## Functions

::: msuthemes.themes.theme_msu

::: msuthemes.themes.set_msu_style

::: msuthemes.themes.reset_theme

## Usage Examples

### Basic Theme Application

```python
from msuthemes import theme_msu
import matplotlib.pyplot as plt

# Apply MSU theme
theme_msu()

# Create plot
plt.plot([1, 2, 3, 4], [1, 4, 2, 3])
plt.title('MSU-Themed Plot')
plt.show()
```

### Customized Theme

```python
from msuthemes import theme_msu
import matplotlib.pyplot as plt

# Apply theme with customization
theme_msu(
    base_size=12,
    grid=True,
    spines='bl'
)

# Create plot
plt.plot([1, 2, 3, 4], [1, 4, 2, 3])
plt.show()
```

### Seaborn Integration

```python
from msuthemes import set_msu_style
import seaborn as sns
import matplotlib.pyplot as plt

# Apply MSU style to seaborn
set_msu_style()

# Create seaborn plot
sns.boxplot(data=data)
plt.show()
```

### Resetting Theme

```python
from msuthemes import theme_msu, reset_theme
import matplotlib.pyplot as plt

# Apply MSU theme
theme_msu()
plt.plot([1, 2, 3], [1, 4, 2])
plt.show()

# Reset to defaults
reset_theme()
plt.plot([1, 2, 3], [1, 4, 2])
plt.show()
```

### Different Spine Configurations

```python
from msuthemes import theme_msu
import matplotlib.pyplot as plt

# Only bottom and left spines (default)
theme_msu(spines='bl')
plt.plot([1, 2, 3], [1, 4, 2])
plt.show()

# All spines
theme_msu(spines='all')
plt.plot([1, 2, 3], [1, 4, 2])
plt.show()

# No spines
theme_msu(spines='none')
plt.plot([1, 2, 3], [1, 4, 2])
plt.show()
```

### Presentation vs Publication

```python
from msuthemes import theme_msu
import matplotlib.pyplot as plt

# Larger text for presentations
theme_msu(base_size=14, grid=True)
plt.plot([1, 2, 3], [1, 4, 2])
plt.title('Presentation Figure')
plt.show()

# Smaller text for publications
theme_msu(base_size=9, grid=False, spines='bl')
plt.plot([1, 2, 3], [1, 4, 2])
plt.title('Publication Figure')
plt.show()
```

## Theme Components

The MSU theme modifies these matplotlib rcParams:

### Fonts
- Font family: Metropolis
- Scaled font sizes based on `base_size` parameter

### Colors
- Color cycle using MSU colors
- Axes colors and backgrounds
- Grid colors

### Layout
- Figure size and DPI
- Axes line widths
- Grid line styles

### Spines
- Configurable axes borders
- Options: 'bl', 'all', 'none', or combinations

## See Also

- [Theme Guide](../guide/themes.md) - Detailed theme usage guide
- [Fonts](fonts.md) - Font management
- [Gallery](../gallery/msu.md) - Themed examples
