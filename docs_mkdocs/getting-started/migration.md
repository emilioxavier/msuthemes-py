# Migration from R

This guide helps R users of the MSUthemes R package transition to the Python version.

## Overview

The Python implementation of MSUthemes closely mirrors the R package's functionality, making migration straightforward. The main differences are syntax-related due to Python vs R conventions.

## Package Comparison

| Feature | R Package | Python Package |
|---------|-----------|----------------|
| Installation | `install.packages("MSUthemes")` | `pip install msuthemes` |
| Import | `library(MSUthemes)` | `import msuthemes` or `from msuthemes import ...` |
| Colors | `msu_green`, `msu_white` | `colors.MSU_GREEN`, `colors.MSU_WHITE` |
| Palettes | `msu_palettes$seq` | `palettes.msu_seq` |
| Theme | `theme_msu()` | `theme_msu()` |
| Big Ten | `bigten_colors("MSU")` | `get_bigten_colors("MSU")` |
| Dataset | `bigten` (data.frame) | `load_bigten_data()` (DataFrame) |

## Installation

=== "R"
    ```r
    # From CRAN
    install.packages("MSUthemes")

    # From GitHub
    devtools::install_github("emilioxavier/MSUthemes")
    ```

=== "Python"
    ```bash
    # From PyPI
    pip install msuthemes

    # From GitHub
    git clone https://github.com/emilioxavier/msuthemes-py.git
    cd msuthemes-py
    pip install -e .
    ```

## Loading the Package

=== "R"
    ```r
    library(MSUthemes)
    library(ggplot2)
    ```

=== "Python"
    ```python
    from msuthemes import theme_msu, colors, palettes
    import matplotlib.pyplot as plt
    ```

## Using Colors

=== "R"
    ```r
    # Access colors
    msu_green
    msu_white
    msu_orange

    # In ggplot2
    ggplot(data, aes(x, y)) +
      geom_line(color = msu_green)
    ```

=== "Python"
    ```python
    # Access colors
    colors.MSU_GREEN
    colors.MSU_WHITE
    colors.MSU_ORANGE

    # In matplotlib
    plt.plot(x, y, color=colors.MSU_GREEN)
    ```

## Color Palettes

=== "R"
    ```r
    # Get palette colors
    msu_palettes$seq
    msu_palettes$div
    msu_palettes$qual1

    # Use in ggplot2
    ggplot(data, aes(x, y, fill = category)) +
      geom_bar() +
      scale_fill_manual(values = msu_palettes$qual1)
    ```

=== "Python"
    ```python
    # Get palette colors
    palettes.msu_seq.as_hex(n_colors=5)
    palettes.msu_div.as_hex(n_colors=7)
    palettes.msu_qual1.as_hex()

    # Use in matplotlib
    colors_list = palettes.msu_qual1.as_hex()
    plt.bar(categories, values, color=colors_list)
    ```

## Applying Themes

=== "R"
    ```r
    # Apply MSU theme to ggplot2
    ggplot(data, aes(x, y)) +
      geom_point() +
      theme_msu()

    # With options
    ggplot(data, aes(x, y)) +
      geom_point() +
      theme_msu(base_size = 14, use_grid = TRUE)
    ```

=== "Python"
    ```python
    # Apply MSU theme to matplotlib
    theme_msu()
    plt.plot(x, y)
    plt.show()

    # With options
    theme_msu(base_size=14, use_grid=True)
    plt.plot(x, y)
    plt.show()
    ```

## Big Ten Colors

=== "R"
    ```r
    # Single institution
    bigten_colors("MSU")

    # Multiple institutions
    bigten_colors(c("MSU", "Michigan", "Ohio State"))

    # Create palette
    bigten_palette(c("MSU", "Michigan"))
    ```

=== "Python"
    ```python
    # Single institution
    get_bigten_colors("MSU")

    # Multiple institutions
    get_bigten_colors(["MSU", "Michigan", "Ohio State"])

    # Create palette
    bigten_palette(["MSU", "Michigan"])
    ```

## Working with Data

=== "R"
    ```r
    # Load dataset
    data(bigten)

    # Filter data
    msu_data <- bigten %>%
      filter(name == "Michigan State")

    # Plot with ggplot2
    ggplot(msu_data, aes(x = entry_term, y = UGDS)) +
      geom_line(color = msu_green) +
      theme_msu()
    ```

=== "Python"
    ```python
    # Load dataset
    df = load_bigten_data()

    # Filter data
    msu_data = df[df['name'] == 'Michigan State']

    # Or filter at load time
    msu_data = load_bigten_data(institutions=['MSU'])

    # Plot with matplotlib
    theme_msu()
    plt.plot(msu_data['entry_term'], msu_data['UGDS'],
             color=colors.MSU_GREEN)
    plt.show()
    ```

## Complete Example

### R Version

```r
library(MSUthemes)
library(ggplot2)
library(dplyr)

# Load and filter data
data(bigten)
rivalry <- bigten %>%
  filter(name %in% c("Michigan State", "Michigan", "Ohio State"))

# Get school colors
school_colors <- bigten_palette(c("MSU", "Michigan", "Ohio State"))

# Create plot
ggplot(rivalry, aes(x = entry_term, y = ADM_RATE * 100,
                    color = name)) +
  geom_line(linewidth = 1.5) +
  scale_color_manual(values = school_colors) +
  labs(
    title = "Big Ten Admission Rates Over Time",
    x = "Year",
    y = "Admission Rate (%)",
    color = "Institution"
  ) +
  theme_msu(use_grid = TRUE)
```

### Python Version

```python
from msuthemes import (
    theme_msu,
    get_bigten_colors,
    load_bigten_data
)
import matplotlib.pyplot as plt

# Apply theme
theme_msu(use_grid=True)

# Load and filter data
rivalry = load_bigten_data(
    institutions=['MSU', 'Michigan', 'Ohio State'],
    columns=['name', 'entry_term', 'ADM_RATE']
)

# Get school colors
school_colors = get_bigten_colors(['MSU', 'Michigan', 'Ohio State'])

# Create plot
fig, ax = plt.subplots(figsize=(10, 6))

for school in ['MSU', 'Michigan', 'Ohio State']:
    school_data = rivalry[rivalry['name'] == school]
    ax.plot(
        school_data['entry_term'],
        school_data['ADM_RATE'] * 100,
        label=school,
        color=school_colors[school],
        linewidth=1.5
    )

ax.set_xlabel('Year')
ax.set_ylabel('Admission Rate (%)')
ax.set_title('Big Ten Admission Rates Over Time')
ax.legend(title='Institution')
plt.show()
```

## Key Differences

### Naming Conventions

| R Convention | Python Convention |
|--------------|-------------------|
| `snake_case` for functions | `snake_case` for functions |
| `snake_case` for variables | `UPPER_CASE` for constants |
| `.` for list access | `.` for attribute access |
| `$` for list/dataframe columns | `.` for attributes, `[]` for dict keys |

### Data Structures

| R | Python |
|---|--------|
| `data.frame` | `pandas.DataFrame` |
| `list` | `dict` or `list` |
| `vector` | `list` or `numpy.array` |
| `c()` | `[]` |

### Plotting Libraries

| R | Python |
|---|--------|
| `ggplot2` | `matplotlib` (primary) |
| Base R graphics | `matplotlib` |
| - | `seaborn` (statistical) |
| - | `plotly` (interactive) |

## Common Gotchas

!!! warning "Theme Application"
    - **R**: Theme is applied per-plot with `+ theme_msu()`
    - **Python**: Theme is applied globally with `theme_msu()` before creating plots

!!! warning "Color Names"
    - **R**: `msu_green` (lowercase, no quotes)
    - **Python**: `colors.MSU_GREEN` (uppercase constant)

!!! warning "Palette Access"
    - **R**: `msu_palettes$seq` (dollar sign)
    - **Python**: `palettes.msu_seq` (dot notation)

!!! warning "Data Loading"
    - **R**: `data(bigten)` loads into environment
    - **Python**: `df = load_bigten_data()` returns DataFrame

## Tips for R Users Learning Python

1. **Indexing**: Python uses 0-based indexing (R uses 1-based)
2. **Indentation**: Python requires proper indentation (no `{}`)
3. **Lists**: Use `[]` for lists, not `c()`
4. **Assignment**: Use `=` for assignment (though `<-` enthusiasts exist!)
5. **Help**: Use `help(function_name)` or `?function_name` in IPython

## Additional Resources

- [Python for R Users](https://www.rebeccabarter.com/blog/2023-09-11-from_r_to_python)
- [matplotlib for ggplot2 users](https://matplotlib.org/matplotblog/posts/pyplot-vs-object-oriented-interface/)
- [pandas for dplyr users](https://pandas.pydata.org/docs/getting_started/comparison/comparison_with_r.html)

## Getting Help

If you encounter issues during migration:

- Check the [API Reference](../api/index.md)
- See the [Gallery](../gallery/index.md) for Python examples
- [Open an issue](https://github.com/emilioxavier/msuthemes-py/issues) on GitHub
