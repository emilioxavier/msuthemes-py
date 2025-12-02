# Fonts

MSUthemes bundles the Metropolis font family, Michigan State University's official typeface for digital communications. This ensures your visualizations maintain consistent MSU branding.

## Overview

The Metropolis font is:

- **Open Source**: SIL Open Font License
- **Complete**: 18 font files (9 weights × 2 styles)
- **Professional**: Designed specifically for digital use
- **Automatic**: Registered automatically when using `theme_msu()`

## Font Weights and Styles

Metropolis includes these weights:

- Thin (100)
- ExtraLight (200)
- Light (300)
- Regular (400)
- Medium (500)
- SemiBold (600)
- Bold (700)
- ExtraBold (800)
- Black (900)

Each weight is available in:

- Regular style
- Italic style

## Automatic Font Registration

Fonts are automatically registered when you apply the MSU theme:

```python
from msuthemes import theme_msu

# Fonts are automatically registered
theme_msu()

# Now create plots with Metropolis font
import matplotlib.pyplot as plt
plt.plot([1, 2, 3], [1, 4, 2])
plt.title('This title uses Metropolis')
plt.show()
```

## Manual Font Registration

You can manually register the fonts if needed:

```python
from msuthemes import register_metropolis_fonts

# Register fonts with matplotlib
register_metropolis_fonts()

# Now Metropolis is available
import matplotlib.pyplot as plt
plt.rcParams['font.family'] = 'Metropolis'
```

## Checking Font Availability

Verify that Metropolis fonts are registered:

```python
from msuthemes import is_metropolis_available

# Check if fonts are available
available = is_metropolis_available()

if available:
    print("Metropolis fonts are ready to use")
else:
    print("Metropolis fonts need to be registered")
```

## Getting Font File Paths

Access the bundled font files directly:

```python
from msuthemes.fonts import get_font_path

# Get path to a specific font file
regular_path = get_font_path('Metropolis-Regular.otf')
print(regular_path)

# Get path to bold font
bold_path = get_font_path('Metropolis-Bold.otf')
print(bold_path)
```

## Font Files Included

All 18 Metropolis font files:

```
Metropolis-Thin.otf
Metropolis-ThinItalic.otf
Metropolis-ExtraLight.otf
Metropolis-ExtraLightItalic.otf
Metropolis-Light.otf
Metropolis-LightItalic.otf
Metropolis-Regular.otf
Metropolis-RegularItalic.otf
Metropolis-Medium.otf
Metropolis-MediumItalic.otf
Metropolis-SemiBold.otf
Metropolis-SemiBoldItalic.otf
Metropolis-Bold.otf
Metropolis-BoldItalic.otf
Metropolis-ExtraBold.otf
Metropolis-ExtraBoldItalic.otf
Metropolis-Black.otf
Metropolis-BlackItalic.otf
```

## Using Specific Font Weights

Control font weight in your plots:

```python
from msuthemes import theme_msu
import matplotlib.pyplot as plt

# Apply theme
theme_msu()

fig, ax = plt.subplots(figsize=(10, 6))
ax.plot([1, 2, 3, 4], [1, 4, 2, 3])

# Use different weights
ax.set_title('Title in Default Weight', fontsize=16)
ax.set_xlabel('X-axis Label', fontsize=12, fontweight='light')
ax.set_ylabel('Y-axis Label', fontsize=12, fontweight='bold')

# Add text with specific weight
ax.text(2, 3, 'Annotation', fontweight='semibold', fontsize=14)

plt.show()
```

## Font Troubleshooting

### Fonts Not Appearing

If Metropolis fonts don't appear in your plots:

1. **Clear matplotlib's font cache**:

```bash
rm -rf ~/.cache/matplotlib
```

2. **Re-register fonts**:

```python
from msuthemes import register_metropolis_fonts
register_metropolis_fonts()
```

3. **Restart Python**:
Exit and restart your Python session to ensure changes take effect.

4. **Verify registration**:

```python
from msuthemes import is_metropolis_available
print(is_metropolis_available())  # Should print True
```

### Check Registered Fonts

List all fonts registered with matplotlib:

```python
import matplotlib.font_manager as fm

# List all available fonts
fonts = [f.name for f in fm.fontManager.ttflist]

# Check if Metropolis is included
if 'Metropolis' in fonts:
    print("Metropolis is registered")
else:
    print("Metropolis not found")
```

### Manual Font Cache Rebuild

Force matplotlib to rebuild its font cache:

```python
import matplotlib.font_manager as fm

# Rebuild font cache
fm._rebuild()

# Register Metropolis fonts
from msuthemes import register_metropolis_fonts
register_metropolis_fonts()
```

## Font Configuration

### Setting as Default Font

Make Metropolis the default for all plots:

```python
import matplotlib.pyplot as plt
from msuthemes import register_metropolis_fonts

# Register fonts
register_metropolis_fonts()

# Set as default
plt.rcParams['font.family'] = 'Metropolis'

# All subsequent plots use Metropolis
plt.plot([1, 2, 3], [1, 4, 2])
plt.show()
```

### Specifying Font in Specific Elements

```python
import matplotlib.pyplot as plt
from msuthemes import theme_msu

theme_msu()

fig, ax = plt.subplots()
ax.plot([1, 2, 3], [1, 4, 2])

# Specify font for specific elements
ax.set_title('Title', fontfamily='Metropolis', fontsize=16)
ax.set_xlabel('X-axis', fontfamily='Metropolis', fontsize=12)

plt.show()
```

## Using Without Theme

Use Metropolis fonts without applying the full MSU theme:

```python
from msuthemes import register_metropolis_fonts
import matplotlib.pyplot as plt

# Just register fonts, don't apply theme
register_metropolis_fonts()

# Manually set font
plt.rcParams['font.family'] = 'Metropolis'

# Create plot
plt.plot([1, 2, 3, 4], [1, 4, 2, 3])
plt.title('Using Metropolis Without Full Theme')
plt.show()
```

## Font in Different Plotting Libraries

### Matplotlib

```python
from msuthemes import theme_msu
import matplotlib.pyplot as plt

theme_msu()
plt.plot([1, 2, 3], [1, 4, 2])
plt.title('Matplotlib with Metropolis')
plt.show()
```

### Seaborn

```python
from msuthemes import set_msu_style
import seaborn as sns
import matplotlib.pyplot as plt

set_msu_style()
sns.boxplot(data=data)
plt.title('Seaborn with Metropolis')
plt.show()
```

### Plotly

Plotly doesn't automatically use matplotlib fonts. You need to specify the font:

```python
import plotly.graph_objects as go

fig = go.Figure()
fig.add_trace(go.Scatter(x=[1, 2, 3], y=[1, 4, 2]))

# Specify Metropolis font
fig.update_layout(
    font=dict(
        family="Metropolis, sans-serif",
        size=12
    ),
    title="Plotly with Metropolis Font"
)

fig.show()
```

## Font License

The Metropolis font is licensed under the [SIL Open Font License 1.1](https://scripts.sil.org/OFL), which allows:

- Free use in personal and commercial projects
- Modification and redistribution
- Embedding in documents and websites

See the license file in the package for complete terms.

## Font Information

- **Name**: Metropolis
- **Designer**: Chris Simpson
- **Type**: Sans-serif
- **Format**: OpenType (.otf)
- **Use Case**: Digital interfaces and data visualization
- **Official MSU Font**: Yes (for digital communications)

## Tips and Best Practices

1. **Cache clearing**: If fonts don't appear, first try clearing the matplotlib cache
2. **Restart needed**: After registering fonts, restart your Python session
3. **Fallback fonts**: The theme works even if Metropolis isn't available (uses sans-serif)
4. **Consistent usage**: Apply `theme_msu()` at the start of your scripts for consistency
5. **Weight selection**: Use regular weight for body text, bold for emphasis

## See Also

- [Themes](themes.md) - Complete MSU theme including fonts
- [API Reference](../api/fonts.md) - Font module documentation
- [Gallery](../gallery/msu.md) - Examples using Metropolis fonts
