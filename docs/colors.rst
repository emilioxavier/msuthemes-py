Working with Colors
===================

This guide covers using MSU and Big Ten colors in your visualizations.

For API documentation, see :doc:`api/colors`.

MSU Brand Colors
----------------

Michigan State University has three primary brand colors:

MSU Green
^^^^^^^^^

The iconic MSU Green is the primary brand color.

.. code-block:: python

   from msuthemes import colors

   print(colors.MSU_GREEN)  # '#18453B'

Use MSU Green for:

* Primary plot elements
* Main data series
* Highlighting key information
* Branding elements

MSU White and Black
^^^^^^^^^^^^^^^^^^^

White and black provide contrast and clarity.

.. code-block:: python

   from msuthemes import colors

   print(colors.MSU_WHITE)  # '#FFFFFF'
   print(colors.MSU_BLACK)  # '#000000'

MSU Accent Colors
-----------------

Accent colors add variety while maintaining brand consistency.

.. code-block:: python

   from msuthemes import colors

   # Accent colors
   colors.MSU_ORANGE  # '#FF6F00'
   colors.MSU_TEAL    # '#008183'
   colors.MSU_PURPLE  # '#5B3256'
   colors.MSU_GREY    # '#C3C4C6'

Use accent colors for:

* Secondary data series
* Category differentiation
* Supporting visual elements

Big Ten Colors
--------------

All 18 Big Ten institutions have primary and secondary colors available.

.. code-block:: python

   from msuthemes import get_bigten_colors

   # Get single institution color
   msu_color = get_bigten_colors("MSU")

   # Get multiple institution colors
   colors = get_bigten_colors(["MSU", "Michigan", "Ohio State"])

   # Works with nicknames
   color = get_bigten_colors("Spartans")  # Same as "MSU"

Flexible Institution Names
^^^^^^^^^^^^^^^^^^^^^^^^^^

The module recognizes many variations of institution names:

.. code-block:: python

   from msuthemes import get_bigten_colors

   # All of these work
   get_bigten_colors("MSU")
   get_bigten_colors("Michigan State")
   get_bigten_colors("Spartans")
   get_bigten_colors("State")

See :doc:`api/bigten` for the complete list of supported aliases.

Color Usage Best Practices
---------------------------

Consistency
^^^^^^^^^^^

* Use MSU Green as your primary color
* Limit accent colors to 2-3 per visualization
* Maintain consistency across related visualizations

Accessibility
^^^^^^^^^^^^^

* Ensure sufficient contrast between foreground and background
* Don't rely solely on color to convey information
* Test visualizations for colorblind accessibility
* Use patterns or labels in addition to colors when appropriate

Readability
^^^^^^^^^^^

* Use lighter colors for backgrounds
* Reserve saturated colors for important elements
* Consider your audience's viewing conditions (print vs screen)

Examples
--------

Single Color Plot
^^^^^^^^^^^^^^^^^

.. code-block:: python

   import matplotlib.pyplot as plt
   from msuthemes import theme_msu, colors

   theme_msu()

   plt.plot([1, 2, 3, 4], [1, 4, 2, 3],
            color=colors.MSU_GREEN, linewidth=2)
   plt.show()

Multi-Color Plot
^^^^^^^^^^^^^^^^

.. code-block:: python

   import matplotlib.pyplot as plt
   from msuthemes import theme_msu, colors

   theme_msu()

   plt.plot([1, 2, 3, 4], [1, 4, 2, 3],
            color=colors.MSU_GREEN, label='Series 1')
   plt.plot([1, 2, 3, 4], [2, 3, 4, 1],
            color=colors.MSU_ORANGE, label='Series 2')
   plt.plot([1, 2, 3, 4], [3, 1, 3, 2],
            color=colors.MSU_TEAL, label='Series 3')
   plt.legend()
   plt.show()

Big Ten Comparison
^^^^^^^^^^^^^^^^^^

.. code-block:: python

   import matplotlib.pyplot as plt
   from msuthemes import theme_msu, get_bigten_colors

   theme_msu()

   schools = ['MSU', 'Michigan', 'Ohio State']
   values = [50, 45, 55]
   colors_list = [get_bigten_colors(s) for s in schools]

   plt.bar(schools, values, color=colors_list)
   plt.ylabel('Value')
   plt.title('Big Ten Comparison')
   plt.show()

Next Steps
----------

* :doc:`palettes` - Learn about color palettes
* :doc:`quickstart` - More usage examples
* :doc:`api/colors` - Complete color reference
