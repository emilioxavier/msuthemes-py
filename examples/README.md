# MSUthemes Examples

This directory contains comprehensive examples and tutorials for using MSUthemes.

## Quick Start

Run any example script:

```bash
cd examples
python basic_usage.py
python bigten_comparisons.py
python palette_showcase.py
```

Output will be saved to `examples/output/`.

## Example Scripts

### basic_usage.py

**Simple MSU-branded visualization**

The simplest way to get started with MSUthemes. Creates a basic plot with:
- MSU theme applied
- MSU Green color
- Professional styling

**What you'll learn:**
- Applying the MSU theme
- Using MSU colors
- Creating basic plots

**Run:**
```bash
python basic_usage.py
```

---

### bigten_comparisons.py

**Comparing Big Ten institutions**

Demonstrates how to compare institutions using institutional colors and real data.

**Features:**
- Loading BigTen dataset
- Using institutional colors
- Multiple plot types (bar, line, scatter)
- Multi-panel figures

**What you'll learn:**
- `get_bigten_colors()` function
- `load_bigten_data()` with filtering
- Creating comparative visualizations
- Multi-subplot layouts

**Run:**
```bash
python bigten_comparisons.py
```

---

### palette_showcase.py

**All MSUthemes color palettes**

Comprehensive showcase of all 11 available palettes and how to use them.

**Features:**
- Sequential palettes for continuous data
- Diverging palettes for signed data
- Qualitative palettes for categories
- Big Ten palettes

**What you'll learn:**
- Choosing the right palette
- Converting palettes to colormaps
- Using palettes with different plot types
- Creating custom gradients

**Run:**
```bash
python palette_showcase.py
```

---

### seaborn_examples.py

**Seaborn integration**

Shows how to use MSUthemes with seaborn visualizations.

**Features:**
- Scatter plots with hue
- Box plots and violin plots
- Heatmaps with custom colormaps
- Pair plots and joint plots
- FacetGrid examples

**What you'll learn:**
- `set_msu_style()` function
- Using MSU palettes with seaborn
- Seaborn contexts and styles
- Advanced seaborn plots

**Run:**
```bash
python seaborn_examples.py
```

---

### data_visualization.py

**Comprehensive data analysis dashboard**

Complete data visualization workflow using the BigTen dataset.

**Features:**
- 9-panel analytical dashboard
- Enrollment trends
- Admission rates
- Tuition analysis
- Demographics
- Multi-institution comparisons

**What you'll learn:**
- Loading and filtering data
- Creating analytical dashboards
- Combining multiple visualizations
- Real-world data analysis workflow

**Run:**
```bash
python data_visualization.py
```

---

### advanced_customization.py

**Advanced theme customization**

Demonstrates advanced customization techniques and complex layouts.

**Features:**
- Custom theme parameters
- Monochromatic palettes
- Custom diverging palettes
- Complex multi-panel figures
- Custom color gradients
- Publication-quality figures

**What you'll learn:**
- Theme customization options
- Creating custom palettes
- Using `lighten_color()` and `darken_color()`
- GridSpec for complex layouts
- Creating publication figures

**Run:**
```bash
python advanced_customization.py
```

---

## Jupyter Notebooks

Interactive tutorials in Jupyter notebook format.

### notebooks/getting_started.ipynb

**Interactive introduction to MSUthemes**

Perfect for learning MSUthemes interactively in Jupyter.

**Topics covered:**
1. Your first MSU plot
2. Using MSU colors
3. Color palettes (sequential, diverging, qualitative)
4. Big Ten colors
5. Working with the BigTen dataset
6. Seaborn integration

**Run:**
```bash
jupyter notebook notebooks/getting_started.ipynb
```

---

## Output

All examples save their output to `examples/output/`:

```
output/
├── basic_usage.png
├── bigten_comparisons.png
├── palette_showcase.png
├── palette_applications.png
├── seaborn_examples.png
├── seaborn_pairplot.png
├── seaborn_jointplot.png
├── seaborn_facetgrid.png
├── data_visualization.png
├── advanced_customization.png
├── complex_multipanel.png
└── custom_gradients.png
```

---

## Learning Path

### Beginner

1. **basic_usage.py** - Start here
2. **notebooks/getting_started.ipynb** - Interactive learning
3. **palette_showcase.py** - Explore color options

### Intermediate

4. **bigten_comparisons.py** - Institutional comparisons
5. **seaborn_examples.py** - Seaborn integration
6. **data_visualization.py** - Data analysis workflows

### Advanced

7. **advanced_customization.py** - Complex customization
8. Create your own visualizations!

---

## Example Categories

### By Feature

**Colors:**
- basic_usage.py
- palette_showcase.py
- bigten_comparisons.py

**Themes:**
- basic_usage.py
- advanced_customization.py

**Data:**
- bigten_comparisons.py
- data_visualization.py

**Seaborn:**
- seaborn_examples.py

**Advanced:**
- advanced_customization.py

### By Plot Type

**Line plots:**
- basic_usage.py
- bigten_comparisons.py
- data_visualization.py

**Bar charts:**
- palette_showcase.py
- bigten_comparisons.py
- data_visualization.py

**Heatmaps:**
- palette_showcase.py
- seaborn_examples.py

**Scatter plots:**
- bigten_comparisons.py
- seaborn_examples.py

**Multi-panel figures:**
- bigten_comparisons.py
- data_visualization.py
- advanced_customization.py

---

## Tips

### Running All Examples

Create a script to run all examples:

```bash
#!/bin/bash
for script in *.py; do
    echo "Running $script..."
    python "$script"
done
echo "✓ All examples complete!"
```

### Customizing Examples

All examples are designed to be modified. Try:

1. **Change colors:**
   ```python
   # Instead of
   color=colors.MSU_GREEN

   # Try
   color=colors.MSU_ORANGE
   ```

2. **Change palettes:**
   ```python
   # Instead of
   cmap = palettes.msu_seq.as_matplotlib_cmap()

   # Try
   cmap = palettes.msu_div.as_matplotlib_cmap()
   ```

3. **Filter different data:**
   ```python
   # Instead of
   data = load_bigten_data(institutions=['MSU'])

   # Try
   data = load_bigten_data(institutions=['Wisconsin', 'Iowa'])
   ```

### Saving Figures

All examples save high-resolution figures:

```python
plt.savefig('output/myplot.png', dpi=300, bbox_inches='tight')
```

Use `dpi=300` for publication quality.

### Using in Your Work

These examples are templates! Copy and modify them for your own visualizations.

---

## Requirements

All examples require:

- Python >= 3.8
- matplotlib >= 3.5.0
- numpy >= 1.20.0
- pandas >= 1.3.0
- msuthemes (this package)

For seaborn examples:
- seaborn >= 0.12.0

For Jupyter notebooks:
- jupyter

Install all dependencies:

```bash
pip install msuthemes[all]
pip install jupyter
```

---

## Troubleshooting

### Fonts Not Showing

If Metropolis font doesn't appear:

```python
from msuthemes import register_metropolis_fonts
register_metropolis_fonts(verbose=True)
```

Then clear matplotlib cache and restart Python.

### Import Errors

Make sure MSUthemes is installed:

```bash
pip install -e .  # If running from source
# or
pip install msuthemes  # If installed from PyPI
```

### Output Directory

If you get "No such file or directory" errors:

```bash
mkdir -p examples/output
```

---

## Contributing Examples

Have a great example? Contribute it!

1. Create your example script
2. Follow the existing format
3. Add documentation
4. Save outputs to `output/`
5. Submit a pull request

Good examples:
- Solve a real problem
- Are well-commented
- Include print statements showing progress
- Save high-quality outputs
- Are self-contained

---

## License

These examples are provided under the same license as MSUthemes (CC BY-SA 4.0).

Feel free to use them in your own work with attribution.

---

## Getting Help

- **Documentation:** https://emilioxavier.github.io/MSUpythemes/
- **Issues:** https://github.com/emilioxavier/MSUpythemes/issues
- **Questions:** Open a discussion on GitHub

---

## Related Resources

- [MSUthemes Documentation](../docs/)
- [MSUthemes Tests](../tests/)
- [MSU Brand Guidelines](https://brand.msu.edu/)
- [Big Ten Conference](https://bigten.org/)

Happy visualizing! 🎨📊
