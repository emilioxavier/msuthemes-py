Colors Module
=============

.. automodule:: msuthemes.colors
   :members:
   :undoc-members:
   :show-inheritance:

MSU Primary Colors
------------------

.. data:: MSU_GREEN
   :annotation: = '#18453B'

   Michigan State University official green color.

.. data:: MSU_WHITE
   :annotation: = '#FFFFFF'

   Michigan State University official white color.

.. data:: MSU_BLACK
   :annotation: = '#000000'

   Michigan State University official black color.

MSU Secondary Colors
--------------------

.. data:: MSU_ORANGE
   :annotation: = '#FF6F00'

   MSU accent orange color.

.. data:: MSU_TEAL
   :annotation: = '#008183'

   MSU accent teal color.

.. data:: MSU_PURPLE
   :annotation: = '#5B3256'

   MSU accent purple/eggplant color.

.. data:: MSU_GREY
   :annotation: = '#C3C4C6'

   MSU grey color.

MSU Green Variants
------------------

.. data:: MSU_GREEN_LIGHT
   :annotation: = '#9BB9A8'

   Light variant of MSU Green.

.. data:: MSU_GREEN_DARK
   :annotation: = '#0F2922'

   Dark variant of MSU Green.

.. data:: MSU_GREEN_BRIGHT
   :annotation: = '#3FA060'

   Bright variant of MSU Green.

Big Ten Colors
--------------

.. data:: BIGTEN_COLORS_PRIMARY

   Dictionary mapping institution names to their primary colors.

   Contains primary colors for all 18 Big Ten Conference institutions.

   Example:
       >>> from msuthemes.colors import BIGTEN_COLORS_PRIMARY
       >>> BIGTEN_COLORS_PRIMARY['MSU']
       '#18453B'

.. data:: BIGTEN_COLORS_SECONDARY

   Dictionary mapping institution names to their secondary colors.

   Contains secondary colors for all 18 Big Ten Conference institutions.

   Example:
       >>> from msuthemes.colors import BIGTEN_COLORS_SECONDARY
       >>> BIGTEN_COLORS_SECONDARY['MSU']
       '#FFFFFF'

Usage Examples
--------------

Accessing Colors
^^^^^^^^^^^^^^^^

.. code-block:: python

   from msuthemes import colors

   # Use MSU Green in a plot
   import matplotlib.pyplot as plt
   plt.plot([1, 2, 3], color=colors.MSU_GREEN)

   # Get Big Ten color
   ohio_state_color = colors.BIGTEN_COLORS_PRIMARY['Ohio State']

All Available Colors
^^^^^^^^^^^^^^^^^^^^

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
   print(colors.MSU_GREY)     # '#C3C4C6'

   # Green variants
   print(colors.MSU_GREEN_LIGHT)   # '#9BB9A8'
   print(colors.MSU_GREEN_DARK)    # '#0F2922'
   print(colors.MSU_GREEN_BRIGHT)  # '#3FA060'
