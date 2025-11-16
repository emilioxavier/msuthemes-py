Quickstart Guide
================

This guide will get you started with MSUthemes in just a few minutes.

Your First MSU Plot
-------------------

Let's create a simple plot with MSU branding:

.. code-block:: python

   import matplotlib.pyplot as plt
   import numpy as np
   from msuthemes import theme_msu, colors

   # Apply MSU theme
   theme_msu()

   # Create data
   x = np.linspace(0, 10, 100)
   y = np.sin(x)

   # Create plot
   fig, ax = plt.subplots(figsize=(8, 6))
   ax.plot(x, y, color=colors.MSU_GREEN, linewidth=2)
   ax.set_xlabel('X Axis')
   ax.set_ylabel('Y Axis')
   ax.set_title('My First MSU Plot')
   plt.show()

That's it! Your plot now has MSU branding with:

* Metropolis font
* MSU color palette
* Professional styling

Using MSU Colors
----------------

Access MSU's official colors directly:

.. code-block:: python

   from msuthemes import colors

   # Primary colors
   print(colors.MSU_GREEN)    # '#18453B'
   print(colors.MSU_WHITE)    # '#FFFFFF'
   print(colors.MSU_BLACK)    # '#000000'

   # Accent colors
   print(colors.MSU_ORANGE)   # '#FF6F00'
   print(colors.MSU_TEAL)     # '#008183'
   print(colors.MSU_PURPLE)   # '#5B3256'

   # Use in plots
   plt.scatter(x, y, c=colors.MSU_TEAL, s=50)

Color Palettes
--------------

MSUthemes provides 11 carefully designed palettes:

Sequential Palettes
^^^^^^^^^^^^^^^^^^^

For continuous data from low to high:

.. code-block:: python

   from msuthemes import palettes

   # Get 5 colors from MSU sequential palette
   colors_seq = palettes.msu_seq.as_hex(n_colors=5)

   # Use in a heatmap
   import seaborn as sns
   data = np.random.rand(10, 10)
   sns.heatmap(data, cmap=palettes.msu_seq.as_matplotlib_cmap())

Diverging Palettes
^^^^^^^^^^^^^^^^^^

For data with a meaningful midpoint:

.. code-block:: python

   # Get 7 colors from diverging palette
   colors_div = palettes.msu_div.as_hex(n_colors=7)

   # Use with seaborn
   sns.heatmap(data - 0.5, cmap=palettes.msu_div.as_matplotlib_cmap())

Qualitative Palettes
^^^^^^^^^^^^^^^^^^^^

For categorical data:

.. code-block:: python

   # Get qualitative palette
   colors_qual = palettes.msu_qual1.as_hex()

   # Use for categories
   categories = ['A', 'B', 'C', 'D']
   values = [3, 7, 2, 5]
   plt.bar(categories, values, color=colors_qual[:4])

Big Ten Colors
--------------

Get colors for any Big Ten institution:

.. code-block:: python

   from msuthemes import get_bigten_colors

   # Single institution
   msu_color = get_bigten_colors("MSU")
   print(msu_color)  # '#18453B'

   # Multiple institutions
   colors = get_bigten_colors(["MSU", "Michigan", "Ohio State"])
   # Returns: {'MSU': '#18453B', 'Michigan': '#00274C', 'Ohio State': '#BB0000'}

   # Works with nicknames!
   color = get_bigten_colors("Spartans")  # Same as "MSU"
   color = get_bigten_colors("Buckeyes")  # Same as "Ohio State"

Create a Big Ten comparison:

.. code-block:: python

   from msuthemes import bigten_palette

   # Get all Big Ten colors
   all_colors = bigten_palette()

   # Get specific schools
   rivalry_colors = bigten_palette(["MSU", "Michigan", "Ohio State"])

Applying Themes
---------------

Apply MSU theme with customization:

.. code-block:: python

   from msuthemes import theme_msu

   # Basic theme
   theme_msu()

   # With grid
   theme_msu(use_grid=True)

   # Larger text
   theme_msu(base_size=14)

   # Custom color cycle
   theme_msu(color_cycle=['#18453B', '#FF6F00', '#008183'])

Seaborn Integration
^^^^^^^^^^^^^^^^^^^

For seaborn plots:

.. code-block:: python

   from msuthemes import set_msu_style
   import seaborn as sns

   # Apply MSU style to seaborn
   set_msu_style(style='whitegrid')

   # Create seaborn plot
   tips = sns.load_dataset('tips')
   sns.scatterplot(data=tips, x='total_bill', y='tip', hue='time')

Resetting Theme
^^^^^^^^^^^^^^^

Return to matplotlib defaults:

.. code-block:: python

   from msuthemes import reset_theme

   # Apply MSU theme
   theme_msu()
   # ... create plots ...

   # Reset to defaults
   reset_theme()

Working with Data
-----------------

MSUthemes includes the BigTen dataset with historical institutional data:

.. code-block:: python

   from msuthemes import load_bigten_data

   # Load all data (1996-2023, 18 institutions)
   df = load_bigten_data()
   print(df.shape)  # (504, 38)

   # Filter for MSU
   msu_data = load_bigten_data(institutions=['MSU'])

   # Recent years only
   recent = load_bigten_data(years=[2020, 2021, 2022, 2023])

   # Multiple institutions and years
   comparison = load_bigten_data(
       institutions=['MSU', 'Michigan', 'Ohio State'],
       years=[2020, 2021, 2022, 2023]
   )

Create a visualization with the data:

.. code-block:: python

   import matplotlib.pyplot as plt
   from msuthemes import theme_msu, get_bigten_colors, load_bigten_data

   # Apply theme
   theme_msu()

   # Load data
   data = load_bigten_data(
       institutions=['MSU', 'Michigan', 'Ohio State'],
       columns=['name', 'entry_term', 'UGDS', 'ADM_RATE']
   )

   # Get colors for schools
   school_colors = get_bigten_colors(['MSU', 'Michigan', 'Ohio State'])

   # Create plot
   fig, ax = plt.subplots(figsize=(10, 6))

   for school in ['MSU', 'Michigan', 'Ohio State']:
       school_data = data[data['name'] == school]
       ax.plot(
           school_data['entry_term'],
           school_data['ADM_RATE'] * 100,
           label=school,
           color=school_colors[school],
           linewidth=2
       )

   ax.set_xlabel('Year')
   ax.set_ylabel('Admission Rate (%)')
   ax.set_title('Big Ten Admission Rates Over Time')
   ax.legend()
   plt.show()

Complete Example
----------------

Here's a complete example combining multiple features:

.. code-block:: python

   import matplotlib.pyplot as plt
   import numpy as np
   from msuthemes import (
       theme_msu,
       palettes,
       colors,
       load_bigten_data,
       get_bigten_summary
   )

   # Apply MSU theme with grid
   theme_msu(use_grid=True, base_size=12)

   # Load and summarize data
   summary = get_bigten_summary()
   top_5 = summary.nlargest(5, 'UGDS_mean')

   # Create figure with subplots
   fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(14, 6))

   # Left plot: Bar chart
   palette_colors = palettes.msu_qual1.as_hex(n_colors=5)
   ax1.barh(top_5['name'], top_5['UGDS_mean'], color=palette_colors)
   ax1.set_xlabel('Average Enrollment')
   ax1.set_title('Top 5 Big Ten Schools by Enrollment')

   # Right plot: Line plot
   msu_data = load_bigten_data(
       institutions=['MSU'],
       columns=['entry_term', 'UGDS']
   )
   ax2.plot(
       msu_data['entry_term'],
       msu_data['UGDS'],
       color=colors.MSU_GREEN,
       linewidth=2,
       marker='o'
   )
   ax2.set_xlabel('Year')
   ax2.set_ylabel('Enrollment')
   ax2.set_title('MSU Enrollment Over Time')

   plt.tight_layout()
   plt.savefig('msu_analysis.png', dpi=300)
   plt.show()

Next Steps
----------

Now that you know the basics, explore:

* :doc:`colors` - Complete guide to colors and palettes
* :doc:`themes` - Advanced theme customization
* :doc:`bigten` - Working with Big Ten institutional data
* :doc:`gallery/index` - More example visualizations
* :doc:`api/index` - Full API reference

Tips and Best Practices
------------------------

1. **Always apply theme first**: Call ``theme_msu()`` before creating plots

2. **Use MSU colors consistently**: Stick to MSU Green for primary elements

3. **Choose appropriate palettes**:

   * Sequential: For continuous data (temperature, time series)
   * Diverging: For data with a midpoint (profit/loss, deviations)
   * Qualitative: For categories (departments, schools)

4. **Font clarity**: Metropolis is optimized for readability at all sizes

5. **Save high-resolution**: Use ``dpi=300`` for publication-quality figures

6. **Accessibility**: Test your visualizations for colorblind accessibility

Common Patterns
---------------

Create a standard MSU figure:

.. code-block:: python

   def create_msu_figure(figsize=(8, 6)):
       """Create a figure with MSU theme."""
       theme_msu()
       fig, ax = plt.subplots(figsize=figsize)
       return fig, ax

Apply and save:

.. code-block:: python

   def save_msu_plot(filename, dpi=300):
       """Save plot with MSU branding."""
       plt.savefig(filename, dpi=dpi, bbox_inches='tight', facecolor='white')

Create a reusable color function:

.. code-block:: python

   def get_school_color(school_name):
       """Get color for a Big Ten school."""
       from msuthemes import get_bigten_colors
       return get_bigten_colors(school_name)
