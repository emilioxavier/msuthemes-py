# MSUthemes

<div class="hero">
  <h1>MSUthemes</h1>
  <p>MSU and Big Ten color palettes and themes for Python data visualization</p>
</div>

[![Python Version](https://img.shields.io/pypi/pyversions/msuthemes)](https://pypi.org/project/msuthemes/)
[![PyPI Version](https://img.shields.io/pypi/v/msuthemes)](https://pypi.org/project/msuthemes/)
[![License: CC BY-SA 4.0](https://img.shields.io/badge/License-CC%20BY--SA%204.0-lightgrey.svg)](https://creativecommons.org/licenses/by-sa/4.0/)

MSUthemes provides a comprehensive suite of color palettes, themes, and datasets for creating professional, MSU-branded visualizations using matplotlib, seaborn, and plotly.

This package is a Python port of the [MSUthemes R package](https://cran.r-project.org/package=MSUthemes) available on CRAN.

## Features

<div class="feature-grid">
  <div class="feature-card">
    <h3>🎨 MSU Brand Colors</h3>
    <p>Official Michigan State University colors including MSU Green, White, and carefully selected accent colors for data visualization.</p>
  </div>

  <div class="feature-card">
    <h3>🏈 Big Ten Colors</h3>
    <p>Complete color sets for all 18 Big Ten Conference institutions with flexible name recognition supporting common aliases.</p>
  </div>

  <div class="feature-card">
    <h3>📊 Color Palettes</h3>
    <p>11 carefully designed palettes (sequential, diverging, qualitative) optimized for effective data visualization.</p>
  </div>

  <div class="feature-card">
    <h3>✍️ Metropolis Font</h3>
    <p>Professional typography with bundled Metropolis font including 9 weights and italic variants.</p>
  </div>

  <div class="feature-card">
    <h3>🎭 matplotlib/seaborn Themes</h3>
    <p>Ready-to-use themes that automatically apply MSU branding to all your plots with a single function call.</p>
  </div>

  <div class="feature-card">
    <h3>📈 BigTen Dataset</h3>
    <p>Historical institutional data (1996-2023) from the College Scorecard for research and analysis.</p>
  </div>
</div>

## Quick Start

### Installation

Install MSUthemes from PyPI:

```bash
pip install msuthemes
```

For all optional dependencies (seaborn, plotly):

```bash
pip install msuthemes[all]
```

### Basic Example

Create an MSU-branded plot in just a few lines:

```python
import matplotlib.pyplot as plt
from msuthemes import theme_msu, colors
import numpy as np

# Apply MSU theme
theme_msu()

# Create a plot with MSU Green
x = np.linspace(0, 10, 100)
y = np.sin(x)

fig, ax = plt.subplots()
ax.plot(x, y, color=colors.MSU_GREEN, linewidth=2)
ax.set_title('MSU-Branded Plot')
ax.set_xlabel('X axis')
ax.set_ylabel('Y axis')
plt.show()
```

### Color Palettes

Access MSU and Big Ten color palettes:

```python
from msuthemes import palettes, get_bigten_colors

# Sequential palette for heatmaps
colors_seq = palettes.msu_seq.as_hex(n_colors=5)

# Diverging palette for comparative data
colors_div = palettes.msu_div.as_hex(n_colors=7)

# Qualitative palette for categorical data
colors_qual = palettes.msu_qual1.as_hex()

# Big Ten institution colors
msu_color = get_bigten_colors("MSU")
rival_colors = get_bigten_colors(["MSU", "Michigan", "Ohio State"])
```

### BigTen Dataset

Access and analyze Big Ten institutional data:

```python
from msuthemes import load_bigten_data, get_bigten_summary

# Load all data (504 rows × 38 columns)
df = load_bigten_data()

# Filter for specific institutions and years
recent_data = load_bigten_data(
    institutions=['MSU', 'Michigan', 'Ohio State'],
    years=[2020, 2021, 2022, 2023]
)

# Get summary statistics
summary = get_bigten_summary()
print(summary)
```

## MSU Color Reference

### Primary Colors

<div class="color-palette">
  <div class="color-item">
    <div class="color-swatch" style="background-color: #18453B; color: white;">
      MSU Green
    </div>
    <div class="color-label">#18453B</div>
  </div>
  <div class="color-item">
    <div class="color-swatch" style="background-color: #FFFFFF; color: black; border: 2px solid #ddd;">
      MSU White
    </div>
    <div class="color-label">#FFFFFF</div>
  </div>
</div>

### Secondary Colors

<div class="color-palette">
  <div class="color-item">
    <div class="color-swatch" style="background-color: #000000; color: white;">
      MSU Black
    </div>
    <div class="color-label">#000000</div>
  </div>
  <div class="color-item">
    <div class="color-swatch" style="background-color: #C1C6C8; color: black;">
      MSU Silver
    </div>
    <div class="color-label">#C1C6C8</div>
  </div>
  <div class="color-item">
    <div class="color-swatch" style="background-color: #909090; color: white;">
      MSU Gray
    </div>
    <div class="color-label">#909090</div>
  </div>
</div>

### Accent Colors

<div class="color-palette">
  <div class="color-item">
    <div class="color-swatch" style="background-color: #D14D28; color: white;">
      MSU Orange
    </div>
    <div class="color-label">#D14D28</div>
  </div>
  <div class="color-item">
    <div class="color-swatch" style="background-color: #005F83; color: white;">
      MSU Teal
    </div>
    <div class="color-label">#005F83</div>
  </div>
  <div class="color-item">
    <div class="color-swatch" style="background-color: #849E2A; color: white;">
      MSU Grellow
    </div>
    <div class="color-label">#849E2A</div>
  </div>
</div>

## Documentation

<div class="feature-grid">
  <div class="feature-card">
    <h3>📖 Getting Started</h3>
    <p><a href="getting-started/installation/">Installation</a> - Install MSUthemes and dependencies</p>
    <p><a href="getting-started/quickstart/">Quick Start</a> - Get up and running quickly</p>
    <p><a href="getting-started/migration/">Migration from R</a> - Guide for R users</p>
  </div>

  <div class="feature-card">
    <h3>📚 User Guide</h3>
    <p><a href="guide/colors/">Colors</a> - MSU and Big Ten colors</p>
    <p><a href="guide/palettes/">Palettes</a> - Sequential, diverging, and qualitative palettes</p>
    <p><a href="guide/themes/">Themes</a> - Apply MSU branding to plots</p>
    <p><a href="guide/bigten/">Big Ten</a> - Work with Big Ten institutions</p>
    <p><a href="guide/datasets/">Datasets</a> - BigTen dataset documentation</p>
  </div>

  <div class="feature-card">
    <h3>🎨 Gallery</h3>
    <p><a href="gallery/">View Examples</a> - See MSUthemes in action</p>
  </div>

  <div class="feature-card">
    <h3>🔧 API Reference</h3>
    <p><a href="api/">Complete API Documentation</a> - Detailed reference for all modules</p>
  </div>
</div>

## Development Status

MSUthemes is currently in **alpha development** (v0.1.0). The API is stable but may evolve based on user feedback.

### Roadmap Highlights

- ✅ Core color system and palettes
- ✅ Metropolis font integration
- ✅ matplotlib and seaborn themes
- ✅ Big Ten institution support (all 18 schools)
- ✅ BigTen dataset integration
- ✅ Comprehensive test suite (170+ tests, >90% coverage)
- ✅ PyPI publication
- 🔄 plotly theme support (coming soon)

## Contributing

Contributions are welcome! Please see our [Contributing Guide](development/contributing.md) for details.

## License

MSUthemes is licensed under the [Creative Commons Attribution-ShareAlike 4.0 International License (CC BY-SA 4.0)](development/license.md).

## Citation

If you use MSUthemes in your research or publications, please cite:

```bibtex
@software{msuthemes_python,
  author = {Esposito, Emilio Xavier},
  title = {MSUthemes: MSU and Big Ten Color Palettes and Themes for Python},
  year = {2025},
  url = {https://github.com/emilioxavier/msuthemes-py}
}
```

## Contact

- **Author**: Emilio Xavier Esposito
- **Email**: emilio.esposito@gmail.com
- **GitHub**: [emilioxavier/msuthemes-py](https://github.com/emilioxavier/msuthemes-py)
- **Issues**: [Report an issue](https://github.com/emilioxavier/msuthemes-py/issues)

## Acknowledgments

- Michigan State University for brand guidelines and color specifications
- The Big Ten Conference for institutional color information
- The original [MSUthemes R package](https://cran.r-project.org/package=MSUthemes) and its contributors
