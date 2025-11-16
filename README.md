# MSUthemes

[![Python Version](https://img.shields.io/pypi/pyversions/msuthemes)](https://pypi.org/project/msuthemes/)
[![License: CC BY-SA 4.0](https://img.shields.io/badge/License-CC%20BY--SA%204.0-lightgrey.svg)](https://creativecommons.org/licenses/by-sa/4.0/)

MSU and Big Ten color palettes and themes for Python data visualization.

## Overview

MSUthemes is a Python package that provides color palettes and themes for Michigan State University and all Big Ten Conference institutions. It's designed to work seamlessly with popular Python visualization libraries including matplotlib, seaborn, and plotly.

This package is a Python port of the [MSUthemes R package](https://cran.r-project.org/package=MSUthemes) available on CRAN.

## Features

- **MSU Color Palettes**: Sequential, diverging, and qualitative palettes using official MSU colors
- **Big Ten Colors**: Primary and secondary colors for all 18 Big Ten institutions
- **Metropolis Font**: Bundled with MSU's preferred font for consistent branding
- **BigTen Dataset**: Historical data (1996-2023) for all Big Ten institutions
- **matplotlib Integration**: Easy-to-use themes for matplotlib plots
- **seaborn Support**: Compatible with seaborn's styling system
- **plotly Support**: (Coming soon) Interactive visualizations with MSU branding

## Installation

Install from PyPI:

```bash
pip install msuthemes
```

For optional dependencies:

```bash
# With seaborn support
pip install msuthemes[seaborn]

# With plotly support
pip install msuthemes[plotly]

# Install all optional dependencies
pip install msuthemes[all]
```

For development:

```bash
git clone https://github.com/emilioxavier/MSUpythemes.git
cd MSUpythemes
pip install -e .[dev]
```

## Quick Start

### Basic Usage with matplotlib

```python
import matplotlib.pyplot as plt
from msuthemes import theme_msu, colors
import numpy as np

# Apply MSU theme
theme_msu()

# Create a simple plot
x = np.linspace(0, 10, 100)
y = np.sin(x)

fig, ax = plt.subplots(figsize=(8, 6))
ax.plot(x, y, color=colors.MSU_GREEN, linewidth=2)
ax.set_xlabel('X axis')
ax.set_ylabel('Y axis')
ax.set_title('MSU-Branded Plot')
plt.show()
```

### Using MSU Color Palettes

```python
from msuthemes import palettes

# Use sequential palette
colors = palettes.msu_seq.as_hex(n_colors=5)

# Use diverging palette
colors_div = palettes.msu_div.as_hex(n_colors=7)

# Use qualitative palette
colors_qual = palettes.msu_qual1.as_hex()
```

### Big Ten Colors

```python
from msuthemes import get_bigten_colors

# Get single institution color
msu_color = get_bigten_colors("MSU")

# Get multiple institution colors
colors = get_bigten_colors(["MSU", "Michigan", "Ohio State"])
# Returns: {'MSU': '#18453B', 'Michigan': '#00274C', 'Ohio State': '#BB0000'}
```

### Using Metropolis Font

The Metropolis font is bundled with MSUthemes and can be easily registered with matplotlib:

```python
from msuthemes import register_metropolis_fonts
import matplotlib.pyplot as plt

# Register Metropolis font with matplotlib
register_metropolis_fonts()

# Use Metropolis in your plots
plt.rcParams['font.family'] = 'Metropolis'

# Create plot with Metropolis font
fig, ax = plt.subplots()
ax.plot([1, 2, 3], [1, 4, 2])
ax.set_title('Plot with Metropolis Font', fontsize=16, weight='bold')
ax.set_xlabel('X Axis', fontsize=12)
plt.show()
```

Check if Metropolis is available:

```python
from msuthemes import is_metropolis_available

if is_metropolis_available():
    print("Metropolis font is ready!")
```

The Metropolis font includes 18 font files with 9 weights (100-900), each with normal and italic variants. See [fonts documentation](msuthemes/fonts/README.md) for more details.

### BigTen Dataset

MSUthemes includes historical data (1996-2023) for all 18 Big Ten Conference institutions from the College Scorecard:

```python
from msuthemes import load_bigten_data, get_bigten_summary

# Load all data (504 rows × 38 columns)
df = load_bigten_data()

# Filter for specific institutions (supports aliases)
msu_data = load_bigten_data(institutions=['MSU'])
rivalries = load_bigten_data(institutions=['MSU', 'Michigan', 'Ohio State'])

# Filter by years
recent = load_bigten_data(years=[2020, 2021, 2022, 2023])

# Combine filters and select columns
msu_recent = load_bigten_data(
    institutions=['MSU'],
    years=[2020, 2021, 2022, 2023],
    columns=['name', 'entry_term', 'UGDS', 'ADM_RATE', 'TUITIONFEE_IN']
)

# Get summary statistics
summary = get_bigten_summary()
print(summary)
```

The dataset includes:
- **Enrollment data**: Total, by gender, by race/ethnicity
- **Admission rates**: Percentage of applicants admitted
- **Completion rates**: 4-year completion percentage
- **Tuition and fees**: In-state and out-of-state
- **Cost of attendance**: Total estimated costs
- **Demographics**: Student body composition

## Color Palettes

### MSU Primary Colors

- **MSU Green**: `#18453B`
- **MSU White**: `#FFFFFF`

### MSU Secondary Colors

- **MSU Black**: `#000000`
- **MSU Silver**: `#C1C6C8`
- **MSU Gray**: `#909090`

### MSU Accent Colors

- **MSU Orange**: `#D14D28`
- **MSU Teal**: `#005F83`
- **MSU Grellow**: `#849E2A`

## Big Ten Institutions

The package includes colors for all 18 Big Ten institutions:

- Illinois
- Indiana
- Iowa
- Maryland
- Michigan
- Michigan State (MSU)
- Minnesota
- Nebraska
- Northwestern
- Ohio State
- Oregon
- Penn State
- Purdue
- Rutgers
- UCLA
- USC
- Washington
- Wisconsin

## Documentation

Full documentation is available at: [https://emilioxavier.github.io/MSUpythemes/](https://emilioxavier.github.io/MSUpythemes/)

## Examples

See the `examples/` directory for comprehensive usage examples:

- `basic_usage.py` - Simple MSU-branded plots
- `msu_plots.py` - Various plot types with MSU themes
- `bigten_comparisons.py` - Comparing Big Ten institutions

## Development Status

MSUthemes is currently in **alpha development** (v0.1.0). The API may change in future releases.

### Roadmap

- [x] Phase 1: Project setup and infrastructure
- [x] Phase 2: Color system implementation
- [x] Phase 3: Metropolis font integration
- [x] Phase 4: matplotlib/seaborn themes
- [x] Phase 5: Big Ten functionality
- [x] Phase 6: BigTen dataset integration
- [ ] Phase 7: Documentation
- [ ] Phase 8: Test suite
- [ ] Phase 9: Examples and tutorials
- [ ] Phase 10: PyPI publication

## Related Projects

- [MSUthemes R package (CRAN)](https://cran.r-project.org/package=MSUthemes) - Original R implementation
- [MSUthemes R package (GitHub)](https://github.com/emilioxavier/MSUthemes)

## License

This project is licensed under the Creative Commons Attribution-ShareAlike 4.0 International License (CC BY-SA 4.0).

See [LICENSE](LICENSE) for more information.

## Contributing

Contributions are welcome! Please feel free to submit a Pull Request.

## Citation

If you use MSUthemes in your research or publications, please cite:

```bibtex
@software{msuthemes_python,
  author = {Esposito, Emilio Xavier},
  title = {MSUthemes: MSU and Big Ten Color Palettes and Themes for Python},
  year = {2025},
  url = {https://github.com/emilioxavier/MSUpythemes}
}
```

## Contact

- **Author**: Emilio Xavier Esposito
- **Email**: emilio@msu.edu
- **GitHub**: [https://github.com/emilioxavier/MSUpythemes](https://github.com/emilioxavier/MSUpythemes)
- **Issues**: [https://github.com/emilioxavier/MSUpythemes/issues](https://github.com/emilioxavier/MSUpythemes/issues)

## Acknowledgments

- Michigan State University for brand guidelines and color specifications
- The Big Ten Conference for institutional color information
- The original MSUthemes R package and its contributors
