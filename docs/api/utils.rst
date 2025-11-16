Utilities Module
================

.. automodule:: msuthemes.utils
   :members:
   :undoc-members:
   :show-inheritance:

Functions
---------

Color Conversion
^^^^^^^^^^^^^^^^

.. autofunction:: msuthemes.utils.hex_to_rgb

.. autofunction:: msuthemes.utils.rgb_to_hex

.. autofunction:: msuthemes.utils.validate_hex_color

Color Analysis
^^^^^^^^^^^^^^

.. autofunction:: msuthemes.utils.get_color_brightness

.. autofunction:: msuthemes.utils.lighten_color

.. autofunction:: msuthemes.utils.darken_color

Usage Examples
--------------

Color Conversion
^^^^^^^^^^^^^^^^

.. code-block:: python

   from msuthemes.utils import hex_to_rgb, rgb_to_hex

   # Convert hex to RGB
   rgb = hex_to_rgb('#18453B')
   print(rgb)  # (24, 69, 59)

   # Convert RGB to hex
   hex_color = rgb_to_hex(24, 69, 59)
   print(hex_color)  # '#18453B'

Color Validation
^^^^^^^^^^^^^^^^

.. code-block:: python

   from msuthemes.utils import validate_hex_color

   # Validate hex colors
   is_valid = validate_hex_color('#18453B')  # True
   is_valid = validate_hex_color('#XYZ123')  # False
   is_valid = validate_hex_color('18453B')   # False (missing #)

Color Brightness
^^^^^^^^^^^^^^^^

.. code-block:: python

   from msuthemes.utils import get_color_brightness

   # Get brightness (0-255)
   brightness = get_color_brightness('#18453B')
   print(f"Brightness: {brightness:.1f}")  # Lower values are darker

   # Use for choosing text color
   bg_color = '#18453B'
   text_color = '#FFFFFF' if get_color_brightness(bg_color) < 128 else '#000000'

Lightening and Darkening Colors
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

.. code-block:: python

   from msuthemes.utils import lighten_color, darken_color
   from msuthemes.colors import MSU_GREEN

   # Lighten MSU Green by 20%
   lighter = lighten_color(MSU_GREEN, amount=0.2)

   # Darken MSU Green by 30%
   darker = darken_color(MSU_GREEN, amount=0.3)

   # Create a gradient
   gradient = [
       darken_color(MSU_GREEN, 0.3),
       darken_color(MSU_GREEN, 0.15),
       MSU_GREEN,
       lighten_color(MSU_GREEN, 0.15),
       lighten_color(MSU_GREEN, 0.3),
   ]

Practical Examples
^^^^^^^^^^^^^^^^^^

Creating Color Variations
"""""""""""""""""""""""""""

.. code-block:: python

   from msuthemes.colors import MSU_GREEN
   from msuthemes.utils import lighten_color, darken_color

   # Create a monochromatic palette
   base_color = MSU_GREEN
   palette = [
       darken_color(base_color, 0.4),
       darken_color(base_color, 0.2),
       base_color,
       lighten_color(base_color, 0.2),
       lighten_color(base_color, 0.4),
   ]

   # Use in plot
   import matplotlib.pyplot as plt
   plt.bar(range(5), [1, 2, 3, 4, 5], color=palette)

Automatic Text Color Selection
"""""""""""""""""""""""""""""""

.. code-block:: python

   from msuthemes.utils import get_color_brightness

   def get_text_color(background_color):
       """Choose white or black text based on background brightness."""
       brightness = get_color_brightness(background_color)
       return '#FFFFFF' if brightness < 128 else '#000000'

   # Use with Big Ten colors
   from msuthemes import get_bigten_colors
   bg_color = get_bigten_colors("MSU")
   text_color = get_text_color(bg_color)
   print(f"For {bg_color}, use {text_color} text")
