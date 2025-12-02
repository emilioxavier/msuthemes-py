# Metropolis Font

## Overview

The Metropolis font (version 5.1.0) is bundled with MSUthemes for use in MSU-branded data visualizations. Metropolis is a modern, geometric sans-serif typeface that provides excellent readability for both print and digital applications.

## Font Information

- **Font Family**: Metropolis
- **Version**: 5.1.0
- **Format**: TrueType (.ttf)
- **Character Set**: Latin
- **License**: Public Domain (Unlicense)

## Available Weights

Metropolis includes 9 weights, each with normal and italic variants:

- **Thin** (100): Normal & Italic
- **Extra Light** (200): Normal & Italic
- **Light** (300): Normal & Italic
- **Regular** (400): Normal & Italic
- **Medium** (500): Normal & Italic
- **Semi Bold** (600): Normal & Italic
- **Bold** (700): Normal & Italic
- **Extra Bold** (800): Normal & Italic
- **Black** (900): Normal & Italic

**Total**: 18 font files

## Usage with MSUthemes

### Automatic Registration

When you import msuthemes and apply an MSU theme, the Metropolis font is automatically registered with matplotlib:

```python
from msuthemes import theme_msu
import matplotlib.pyplot as plt

# Apply MSU theme (automatically registers Metropolis)
theme_msu()

# Create plot - Metropolis is now the default font
plt.plot([1, 2, 3], [1, 2, 3])
plt.title('MSU-Branded Plot')
plt.show()
```

### Manual Registration

You can also manually register the fonts:

```python
from msuthemes.fonts import register_metropolis_fonts
import matplotlib.pyplot as plt

# Register fonts
register_metropolis_fonts(verbose=True)

# Use Metropolis font
plt.rcParams['font.family'] = 'Metropolis'
plt.plot([1, 2, 3], [1, 2, 3])
plt.show()
```

### Check Font Availability

```python
from msuthemes.fonts import is_metropolis_available

if is_metropolis_available():
    print("Metropolis font is ready to use!")
else:
    print("Metropolis font is not available")
```

### List Available Fonts

```python
from msuthemes.fonts import list_available_fonts

fonts = list_available_fonts()
for font in fonts:
    print(font)
```

## License

The Metropolis font is released into the **public domain** under the **Unlicense**.

This means you can:
- Use the font for any purpose (commercial or non-commercial)
- Modify the font
- Distribute the font
- Include it in your projects without attribution

For the full license text, see the [LICENSE](metropolis/LICENSE) file.

## Font Source

Metropolis was designed by Chris Simpson and is available at:
- GitHub: https://github.com/chrismsimpson/Metropolis

## MSU Brand Guidelines

When using Metropolis for MSU-branded materials:

1. **Primary Usage**: Use Metropolis for data visualization text (titles, labels, legends, annotations)
2. **Recommended Weights**:
   - Regular (400) for body text
   - Semi Bold (600) or Bold (700) for titles
   - Medium (500) for emphasis
3. **Color Pairing**: Combine with MSU Green (#18453B) and other MSU brand colors
4. **Consistency**: Use consistently throughout a project for professional appearance

## Technical Details

### Font Files

All font files follow the naming convention:
```
metropolis-latin-{weight}-{style}.ttf
```

Where:
- `{weight}`: 100, 200, 300, 400, 500, 600, 700, 800, 900
- `{style}`: normal, italic

### File Sizes

Each font file is approximately 56-60 KB, for a total of ~1.1 MB for all 18 files.

## Troubleshooting

### Fonts Not Appearing

If Metropolis doesn't appear in your plots:

1. **Clear matplotlib cache**:
   ```python
   import matplotlib as mpl
   import os
   cache_dir = mpl.get_cachedir()
   # Remove cache files and restart Python
   ```

2. **Manually register fonts**:
   ```python
   from msuthemes.fonts import register_metropolis_fonts
   register_metropolis_fonts(verbose=True)
   ```

3. **Verify installation**:
   ```python
   from msuthemes.fonts import is_metropolis_available
   print(is_metropolis_available())
   ```

### System Font vs Package Font

MSUthemes uses the bundled Metropolis font files, which are automatically registered with matplotlib when you use MSU themes. You don't need to install Metropolis as a system font.

## Support

For issues or questions about the Metropolis font in MSUthemes:
- GitHub Issues: https://github.com/emilioxavier/msuthemes-py/issues
- Email: emilio@msu.edu
