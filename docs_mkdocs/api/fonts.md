# fonts

The `fonts` module manages Metropolis font registration with matplotlib.

## Module Overview

This module provides:

- Automatic font registration with matplotlib
- Font availability checking
- Access to bundled font files
- 18 Metropolis font files (9 weights × 2 styles)

## Functions

::: msuthemes.fonts.register_metropolis_fonts

::: msuthemes.fonts.is_metropolis_available

::: msuthemes.fonts.get_font_path

## Usage Examples

### Automatic Registration

```python
from msuthemes import theme_msu

# Fonts are automatically registered
theme_msu()
```

### Manual Registration

```python
from msuthemes import register_metropolis_fonts

# Manually register fonts
register_metropolis_fonts()
```

### Check Font Availability

```python
from msuthemes import is_metropolis_available

if is_metropolis_available():
    print("Metropolis fonts are ready")
else:
    print("Need to register fonts")
```

### Get Font File Path

```python
from msuthemes.fonts import get_font_path

# Get path to specific font
regular_path = get_font_path('Metropolis-Regular.otf')
bold_path = get_font_path('Metropolis-Bold.otf')

print(f"Regular font: {regular_path}")
print(f"Bold font: {bold_path}")
```

### Using Specific Font Weights

```python
from msuthemes import theme_msu
import matplotlib.pyplot as plt

# Apply theme (registers fonts)
theme_msu()

fig, ax = plt.subplots()
ax.plot([1, 2, 3], [1, 4, 2])

# Use different font weights
ax.set_title('Title in Default Weight', fontsize=16)
ax.set_xlabel('Light Weight', fontweight='light')
ax.set_ylabel('Bold Weight', fontweight='bold')

plt.show()
```

## Font Files

The following Metropolis font files are included:

**Regular Styles:**
- Metropolis-Thin.otf
- Metropolis-ExtraLight.otf
- Metropolis-Light.otf
- Metropolis-Regular.otf
- Metropolis-Medium.otf
- Metropolis-SemiBold.otf
- Metropolis-Bold.otf
- Metropolis-ExtraBold.otf
- Metropolis-Black.otf

**Italic Styles:**
- Metropolis-ThinItalic.otf
- Metropolis-ExtraLightItalic.otf
- Metropolis-LightItalic.otf
- Metropolis-RegularItalic.otf
- Metropolis-MediumItalic.otf
- Metropolis-SemiBoldItalic.otf
- Metropolis-BoldItalic.otf
- Metropolis-ExtraBoldItalic.otf
- Metropolis-BlackItalic.otf

## Troubleshooting

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

3. Restart Python session

4. Verify registration:
```python
from msuthemes import is_metropolis_available
print(is_metropolis_available())
```

## Font License

Metropolis is licensed under the SIL Open Font License 1.1, which allows:
- Free use in personal and commercial projects
- Modification and redistribution
- Embedding in documents and websites

## See Also

- [Font Guide](../guide/fonts.md) - Detailed font usage guide
- [Themes](themes.md) - MSU theme application
