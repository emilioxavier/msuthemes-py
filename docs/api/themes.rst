Themes Module
=============

.. automodule:: msuthemes.themes
   :members:
   :undoc-members:
   :show-inheritance:

Functions
---------

.. autofunction:: msuthemes.themes.theme_msu

.. autofunction:: msuthemes.themes.set_msu_style

.. autofunction:: msuthemes.themes.reset_theme

.. autofunction:: msuthemes.themes.get_current_theme

Usage Examples
--------------

Applying MSU Theme
^^^^^^^^^^^^^^^^^^

.. code-block:: python

   from msuthemes import theme_msu
   import matplotlib.pyplot as plt

   # Apply basic MSU theme
   theme_msu()

   # Create a plot
   plt.plot([1, 2, 3], [1, 4, 2])
   plt.title('MSU-Themed Plot')
   plt.show()

Theme Customization
^^^^^^^^^^^^^^^^^^^

.. code-block:: python

   from msuthemes import theme_msu

   # Larger text
   theme_msu(base_size=14)

   # With grid
   theme_msu(use_grid=True)

   # Custom color cycle
   theme_msu(color_cycle=['#18453B', '#FF6F00', '#008183'])

   # Combined options
   theme_msu(
       base_size=12,
       use_grid=True,
       grid_color='#E5E5E5',
       spine_linewidth=1.5
   )

Seaborn Integration
^^^^^^^^^^^^^^^^^^^

.. code-block:: python

   from msuthemes import set_msu_style
   import seaborn as sns

   # Apply MSU style to seaborn
   set_msu_style(style='whitegrid')

   # Create seaborn plot
   tips = sns.load_dataset('tips')
   sns.scatterplot(data=tips, x='total_bill', y='tip')

   # For presentations
   set_msu_style(context='talk', font_scale=1.2)

Resetting Theme
^^^^^^^^^^^^^^^

.. code-block:: python

   from msuthemes import theme_msu, reset_theme

   # Apply MSU theme
   theme_msu()
   # ... create plots ...

   # Reset to matplotlib defaults
   reset_theme()

Getting Current Theme
^^^^^^^^^^^^^^^^^^^^^

.. code-block:: python

   from msuthemes import theme_msu, get_current_theme

   # Apply theme
   theme_msu(base_size=14)

   # Get current settings
   current = get_current_theme()
   print(current['font.size'])      # 14
   print(current['font.family'])    # ['Metropolis']
