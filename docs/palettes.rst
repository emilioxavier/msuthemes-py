Color Palettes
==============

MSUthemes provides 11 carefully designed color palettes for different visualization needs.

For API documentation, see :doc:`api/palettes`.

Palette Types
-------------

Sequential Palettes
^^^^^^^^^^^^^^^^^^^

For continuous data from low to high values.

.. code-block:: python

   from msuthemes import palettes

   # MSU sequential (light to dark green)
   colors = palettes.msu_seq.as_hex(n_colors=5)

   # Use in heatmap
   import seaborn as sns
   sns.heatmap(data, cmap=palettes.msu_seq.as_matplotlib_cmap())

Available: ``msu_seq``, ``msu_seq2``, ``msu_seq_full``, ``msu_green``

Diverging Palettes
^^^^^^^^^^^^^^^^^^

For data with a meaningful midpoint (e.g., above/below average).

.. code-block:: python

   from msuthemes import palettes

   # MSU diverging (green to white to orange)
   colors = palettes.msu_div.as_hex(n_colors=7)

   # Use with centered data
   sns.heatmap(data, cmap=palettes.msu_div.as_matplotlib_cmap(),
               center=0)

Available: ``msu_div``, ``msu_div2``, ``msu_div_orange``, ``msu_div_purple``

Qualitative Palettes
^^^^^^^^^^^^^^^^^^^^

For categorical data with no inherent order.

.. code-block:: python

   from msuthemes import palettes

   # MSU qualitative (distinct colors)
   colors = palettes.msu_qual1.as_hex()

   # Use for categories
   plt.bar(categories, values, color=colors[:len(categories)])

Available: ``msu_qual1`` (5 colors), ``msu_qual2`` (5 colors), ``msu_qual3`` (8 colors)

Working with Palettes
---------------------

Get Colors
^^^^^^^^^^

.. code-block:: python

   from msuthemes import palettes

   # Get specific number of colors
   colors = palettes.msu_seq.as_hex(n_colors=7)

   # Get RGB values
   rgb_colors = palettes.msu_seq.as_rgb(n_colors=5)

   # Reverse palette
   reversed_colors = palettes.msu_seq.as_hex(n_colors=5, reverse=True)

Convert to Colormaps
^^^^^^^^^^^^^^^^^^^^

.. code-block:: python

   from msuthemes import palettes

   # Get matplotlib colormap
   cmap = palettes.msu_seq.as_matplotlib_cmap()

   # Use in plots
   plt.imshow(data, cmap=cmap)

List All Palettes
^^^^^^^^^^^^^^^^^

.. code-block:: python

   from msuthemes.palettes import list_palettes

   # See all available palettes
   all_palettes = list_palettes()
   print(all_palettes)

Get Palette by Name
^^^^^^^^^^^^^^^^^^^

.. code-block:: python

   from msuthemes.palettes import get_palette

   # Get palette by name
   palette = get_palette('msu_seq')
   colors = palette.as_hex(n_colors=5)

Choosing the Right Palette
---------------------------

Use Sequential When:
^^^^^^^^^^^^^^^^^^^^

* Showing progression or magnitude
* Data has a natural low-to-high order
* Examples: temperature, time series, rankings

Use Diverging When:
^^^^^^^^^^^^^^^^^^^

* Data has a meaningful midpoint
* Showing positive and negative values
* Comparing to average or benchmark
* Examples: temperature anomalies, profit/loss, above/below average

Use Qualitative When:
^^^^^^^^^^^^^^^^^^^^^^

* Showing categorical data
* Categories have no inherent order
* Need to distinguish between groups
* Examples: departments, product types, geographic regions

Examples
--------

Heatmap with Sequential Palette
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

.. code-block:: python

   import seaborn as sns
   from msuthemes import set_msu_style, palettes

   set_msu_style()

   # Create heatmap
   cmap = palettes.msu_seq.as_matplotlib_cmap()
   sns.heatmap(data, cmap=cmap, square=True)

Line Plot with Qualitative Palette
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

.. code-block:: python

   import matplotlib.pyplot as plt
   from msuthemes import theme_msu, palettes

   theme_msu()

   colors = palettes.msu_qual1.as_hex()

   for i, series in enumerate(data_series):
       plt.plot(x, series, color=colors[i], label=f'Series {i+1}')

   plt.legend()

Diverging Heatmap
^^^^^^^^^^^^^^^^^

.. code-block:: python

   import seaborn as sns
   from msuthemes import palettes

   cmap = palettes.msu_div.as_matplotlib_cmap()

   # Center at zero
   sns.heatmap(data, cmap=cmap, center=0,
               vmin=-10, vmax=10)

Next Steps
----------

* :doc:`colors` - Learn about individual colors
* :doc:`themes` - Apply complete themes
* :doc:`api/palettes` - Complete palette reference
