Palettes Module
===============

.. automodule:: msuthemes.palettes
   :members:
   :undoc-members:
   :show-inheritance:

MSUPalette Class
----------------

.. autoclass:: msuthemes.palettes.MSUPalette
   :members:
   :undoc-members:
   :show-inheritance:
   :special-members: __init__

Available Palettes
------------------

Sequential Palettes
^^^^^^^^^^^^^^^^^^^

.. data:: msu_seq

   MSU sequential palette (light to dark green).

.. data:: msu_seq2

   Alternative MSU sequential palette.

Diverging Palettes
^^^^^^^^^^^^^^^^^^

.. data:: msu_div

   MSU diverging palette (green to white to orange).

.. data:: msu_div2

   Alternative MSU diverging palette.

Qualitative Palettes
^^^^^^^^^^^^^^^^^^^^

.. data:: msu_qual1

   MSU qualitative palette #1 (5 colors).

.. data:: msu_qual2

   MSU qualitative palette #2 (5 colors).

.. data:: msu_qual3

   MSU qualitative palette #3 (8 colors).

Big Ten Palettes
^^^^^^^^^^^^^^^^

.. data:: bigten_primary

   All 18 Big Ten primary colors.

.. data:: bigten_secondary

   All 18 Big Ten secondary colors.

Functions
---------

.. autofunction:: msuthemes.palettes.get_palette

.. autofunction:: msuthemes.palettes.list_palettes

.. autofunction:: msuthemes.palettes.show_all_palettes

Usage Examples
--------------

Using Palettes
^^^^^^^^^^^^^^

.. code-block:: python

   from msuthemes import palettes

   # Get colors from sequential palette
   colors = palettes.msu_seq.as_hex(n_colors=5)

   # Convert to matplotlib colormap
   cmap = palettes.msu_seq.as_matplotlib_cmap()

   # Use with seaborn
   import seaborn as sns
   sns.heatmap(data, cmap=cmap)

Getting Palettes by Name
^^^^^^^^^^^^^^^^^^^^^^^^^

.. code-block:: python

   from msuthemes.palettes import get_palette, list_palettes

   # List all available palettes
   all_palettes = list_palettes()

   # Get palette by name
   palette = get_palette('msu_seq')
   colors = palette.as_hex(n_colors=7)

Customizing Palettes
^^^^^^^^^^^^^^^^^^^^

.. code-block:: python

   from msuthemes.palettes import MSUPalette

   # Create custom palette
   custom = MSUPalette(
       colors=['#18453B', '#FF6F00', '#008183'],
       palette_type='qual',
       name='my_custom_palette'
   )

   # Get colors
   hex_colors = custom.as_hex()
   rgb_colors = custom.as_rgb()
