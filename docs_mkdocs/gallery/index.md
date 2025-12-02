# Gallery

Explore examples of MSUthemes in action. Each example includes full code and demonstrates different features of the package.

## Quick Examples

### Basic MSU Plot

A simple line plot with MSU branding:

```python
import matplotlib.pyplot as plt
import numpy as np
from msuthemes import theme_msu, colors

theme_msu()

x = np.linspace(0, 10, 100)
y = np.sin(x)

fig, ax = plt.subplots(figsize=(8, 6))
ax.plot(x, y, color=colors.MSU_GREEN, linewidth=2)
ax.set_title('MSU Sine Wave')
ax.set_xlabel('X')
ax.set_ylabel('Y')
plt.show()
```

### Using Color Palettes

Demonstrate sequential, diverging, and qualitative palettes:

```python
import matplotlib.pyplot as plt
import numpy as np
from msuthemes import theme_msu, palettes

theme_msu()

# Create sample data
data = np.random.randn(10, 10)

fig, (ax1, ax2, ax3) = plt.subplots(1, 3, figsize=(15, 4))

# Sequential
im1 = ax1.imshow(np.abs(data), cmap=palettes.msu_seq.as_matplotlib_cmap())
ax1.set_title('Sequential Palette')
plt.colorbar(im1, ax=ax1)

# Diverging
im2 = ax2.imshow(data, cmap=palettes.msu_div.as_matplotlib_cmap())
ax2.set_title('Diverging Palette')
plt.colorbar(im2, ax=ax2)

# Qualitative (bar chart)
categories = ['A', 'B', 'C', 'D', 'E']
values = [3, 7, 2, 5, 4]
colors_qual = palettes.msu_qual1.as_hex()
ax3.bar(categories, values, color=colors_qual)
ax3.set_title('Qualitative Palette')

plt.tight_layout()
plt.show()
```

### Big Ten Comparison

Compare Big Ten institutions using their official colors:

```python
import matplotlib.pyplot as plt
from msuthemes import theme_msu, get_bigten_colors, load_bigten_data

theme_msu(use_grid=True)

# Load data
data = load_bigten_data(
    institutions=['MSU', 'Michigan', 'Ohio State', 'Penn State'],
    columns=['name', 'entry_term', 'UGDS']
)

# Get institution colors
school_colors = get_bigten_colors(['MSU', 'Michigan', 'Ohio State', 'Penn State'])

# Create plot
fig, ax = plt.subplots(figsize=(12, 6))

for school in ['MSU', 'Michigan', 'Ohio State', 'Penn State']:
    school_data = data[data['name'] == school]
    ax.plot(
        school_data['entry_term'],
        school_data['UGDS'],
        label=school,
        color=school_colors[school],
        linewidth=2,
        marker='o',
        markersize=4
    )

ax.set_xlabel('Year')
ax.set_ylabel('Undergraduate Enrollment')
ax.set_title('Big Ten Enrollment Trends')
ax.legend()
plt.show()
```

## Gallery Sections

### [Basic Plots](basic.md)
Simple examples demonstrating core functionality:

- Line plots
- Scatter plots
- Bar charts
- Histograms
- Box plots

### [MSU Themes](msu.md)
Advanced MSU-branded visualizations:

- Multi-panel figures
- Subplots with shared themes
- Custom color cycles
- Publication-ready figures
- Annotations and labels

### [Big Ten Comparisons](bigten.md)
Working with Big Ten institutional data:

- Multi-institution comparisons
- Time series analysis
- Enrollment trends
- Admission rates
- Demographic breakdowns

## Code Examples

All examples in the gallery:

- Include complete, runnable code
- Use real or representative data
- Demonstrate best practices
- Show multiple approaches when applicable
- Include customization options

## Using Gallery Code

To run any example:

1. **Install MSUthemes**:
   ```bash
   pip install msuthemes
   ```

2. **Copy the code**: Each example is complete and self-contained

3. **Run in your environment**:
   ```python
   # Paste and run the code
   ```

4. **Customize**: Modify colors, sizes, and styles to fit your needs

## Contributing Examples

Have a great visualization using MSUthemes? We'd love to feature it!

1. Create your example with complete code
2. Include a brief description
3. Submit a pull request to add it to the gallery
4. See our [Contributing Guide](../development/contributing.md)

## Additional Resources

- [Quick Start Guide](../getting-started/quickstart.md) - Learn the basics
- [User Guide](../guide/colors.md) - Detailed documentation
- [API Reference](../api/index.md) - Complete API documentation
- [Examples Directory](https://github.com/emilioxavier/msuthemes-py/tree/main/examples) - More examples on GitHub
