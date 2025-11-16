Fonts Module
============

.. automodule:: msuthemes.fonts
   :members:
   :undoc-members:
   :show-inheritance:

Functions
---------

.. autofunction:: msuthemes.fonts.register_metropolis_fonts

.. autofunction:: msuthemes.fonts.is_metropolis_available

.. autofunction:: msuthemes.fonts.get_font_path

.. autofunction:: msuthemes.fonts.list_available_fonts

.. autofunction:: msuthemes.fonts.get_metropolis_font_weights

Usage Examples
--------------

Registering Fonts
^^^^^^^^^^^^^^^^^

.. code-block:: python

   from msuthemes import register_metropolis_fonts, is_metropolis_available

   # Register Metropolis fonts with matplotlib
   register_metropolis_fonts()

   # Check if available
   if is_metropolis_available():
       print("Metropolis font ready!")

Using Metropolis Font
^^^^^^^^^^^^^^^^^^^^^

.. code-block:: python

   import matplotlib.pyplot as plt
   from msuthemes import register_metropolis_fonts

   # Register fonts
   register_metropolis_fonts()

   # Use in plots
   plt.rcParams['font.family'] = 'Metropolis'
   plt.plot([1, 2, 3], [1, 4, 2])
   plt.title('Plot with Metropolis Font', weight='bold')

Font Weights
^^^^^^^^^^^^

.. code-block:: python

   from msuthemes.fonts import get_metropolis_font_weights

   # Get available font weights
   weights = get_metropolis_font_weights()
   print(weights.keys())
   # ['thin', 'extra-light', 'light', 'regular', 'medium',
   #  'semi-bold', 'bold', 'extra-bold', 'black', ...]

Listing Font Files
^^^^^^^^^^^^^^^^^^

.. code-block:: python

   from msuthemes.fonts import list_available_fonts, get_font_path

   # Get font directory path
   font_path = get_font_path()

   # List all available font files
   fonts = list_available_fonts()
   for font in fonts:
       print(font)
