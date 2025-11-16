Themes and Styling
==================

Apply MSU branding to all your visualizations with a single function call.

For API documentation, see :doc:`api/themes`.

Quick Start
-----------

Apply MSU theme to matplotlib:

.. code-block:: python

   from msuthemes import theme_msu
   import matplotlib.pyplot as plt

   # Apply MSU theme
   theme_msu()

   # All subsequent plots will use MSU styling
   plt.plot([1, 2, 3], [1, 4, 2])
   plt.show()

That's it! Your plots now have:

* Metropolis font
* MSU color palette
* Professional styling
* Clean, publication-ready appearance

Theme Features
--------------

The MSU theme includes:

* **Typography**: Metropolis font (automatically registered)
* **Colors**: MSU color cycle for multiple series
* **Layout**: Clean grid options, minimal spines
* **Sizing**: Optimized for readability
* **Style**: Professional, academic appearance

Customizing the Theme
---------------------

Base Font Size
^^^^^^^^^^^^^^

.. code-block:: python

   from msuthemes import theme_msu

   # Larger text for presentations
   theme_msu(base_size=14)

   # Smaller text for publications
   theme_msu(base_size=10)

Grid Lines
^^^^^^^^^^

.. code-block:: python

   from msuthemes import theme_msu

   # Enable grid
   theme_msu(use_grid=True)

   # Customize grid appearance
   theme_msu(
       use_grid=True,
       grid_color='#E5E5E5',
       grid_linewidth=0.5
   )

Custom Color Cycle
^^^^^^^^^^^^^^^^^^

.. code-block:: python

   from msuthemes import theme_msu, colors

   # Custom color cycle
   my_colors = [colors.MSU_GREEN, colors.MSU_ORANGE, colors.MSU_TEAL]
   theme_msu(color_cycle=my_colors)

Font Family
^^^^^^^^^^^

.. code-block:: python

   from msuthemes import theme_msu

   # Use different font (if Metropolis unavailable)
   theme_msu(base_family='sans-serif')

Seaborn Integration
-------------------

For seaborn plots, use ``set_msu_style()``:

.. code-block:: python

   from msuthemes import set_msu_style
   import seaborn as sns

   # Apply MSU style
   set_msu_style()

   # Create seaborn plot
   tips = sns.load_dataset('tips')
   sns.scatterplot(data=tips, x='total_bill', y='tip')

Seaborn Styles
^^^^^^^^^^^^^^

.. code-block:: python

   from msuthemes import set_msu_style

   # Different seaborn styles
   set_msu_style(style='white')      # Clean background
   set_msu_style(style='whitegrid')  # With grid
   set_msu_style(style='dark')       # Dark background
   set_msu_style(style='darkgrid')   # Dark with grid

Seaborn Contexts
^^^^^^^^^^^^^^^^

.. code-block:: python

   from msuthemes import set_msu_style

   # Different contexts
   set_msu_style(context='paper')      # For publications
   set_msu_style(context='notebook')   # For notebooks (default)
   set_msu_style(context='talk')       # For presentations
   set_msu_style(context='poster')     # For posters

Presentations
^^^^^^^^^^^^^

.. code-block:: python

   from msuthemes import set_msu_style

   # Optimize for presentations
   set_msu_style(context='talk', font_scale=1.2)

Resetting Theme
---------------

Return to matplotlib defaults:

.. code-block:: python

   from msuthemes import reset_theme

   # Reset to default matplotlib style
   reset_theme()

Inspecting Current Theme
------------------------

.. code-block:: python

   from msuthemes import get_current_theme

   # Get current rcParams
   current = get_current_theme()
   print(current['font.size'])
   print(current['font.family'])

Examples
--------

Basic Plot
^^^^^^^^^^

.. code-block:: python

   import matplotlib.pyplot as plt
   import numpy as np
   from msuthemes import theme_msu

   theme_msu()

   x = np.linspace(0, 10, 100)
   plt.plot(x, np.sin(x))
   plt.xlabel('X')
   plt.ylabel('sin(X)')
   plt.title('Sine Wave')
   plt.show()

Multiple Subplots
^^^^^^^^^^^^^^^^^

.. code-block:: python

   import matplotlib.pyplot as plt
   from msuthemes import theme_msu

   theme_msu()

   fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(12, 5))

   ax1.plot([1, 2, 3], [1, 4, 2])
   ax1.set_title('Plot 1')

   ax2.bar(['A', 'B', 'C'], [3, 7, 2])
   ax2.set_title('Plot 2')

   plt.tight_layout()
   plt.show()

Seaborn Plot
^^^^^^^^^^^^

.. code-block:: python

   import seaborn as sns
   from msuthemes import set_msu_style

   set_msu_style(style='whitegrid')

   tips = sns.load_dataset('tips')
   sns.boxplot(data=tips, x='day', y='total_bill')

Best Practices
--------------

1. **Apply theme first**: Call ``theme_msu()`` before creating any plots
2. **Consistent usage**: Use the same theme settings across related visualizations
3. **Font availability**: Ensure Metropolis font is registered (happens automatically)
4. **Grid usage**: Use grids for data-heavy plots, omit for simpler visuals
5. **Save high-res**: Use ``dpi=300`` for publication-quality figures

Troubleshooting
---------------

Font Not Found
^^^^^^^^^^^^^^

If Metropolis font isn't recognized:

.. code-block:: python

   from msuthemes import register_metropolis_fonts, is_metropolis_available

   # Re-register fonts
   register_metropolis_fonts(verbose=True)

   # Check availability
   if is_metropolis_available():
       print("Font ready!")
   else:
       print("Clear matplotlib cache and restart Python")

Theme Not Applied
^^^^^^^^^^^^^^^^^

Ensure you call ``theme_msu()`` before creating plots:

.. code-block:: python

   from msuthemes import theme_msu

   # CORRECT order
   theme_msu()  # Apply theme first
   plt.plot([1, 2, 3])

   # INCORRECT order
   plt.plot([1, 2, 3])
   theme_msu()  # Too late!

Next Steps
----------

* :doc:`colors` - Learn about MSU colors
* :doc:`palettes` - Explore color palettes
* :doc:`api/themes` - Complete theme reference
