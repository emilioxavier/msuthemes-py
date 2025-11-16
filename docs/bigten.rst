Big Ten Colors and Data
=======================

Work with all 18 Big Ten Conference institutions.

For API documentation, see :doc:`api/bigten` and :doc:`api/data`.

Big Ten Institutions
--------------------

MSUthemes supports all 18 Big Ten Conference institutions:

* Illinois
* Indiana
* Iowa
* Maryland
* Michigan
* Michigan State (MSU)
* Minnesota
* Nebraska
* Northwestern
* Ohio State
* Oregon
* Penn State
* Purdue
* Rutgers
* UCLA
* USC
* Washington
* Wisconsin

Getting Institution Colors
---------------------------

Single Institution
^^^^^^^^^^^^^^^^^^

.. code-block:: python

   from msuthemes import get_bigten_colors

   # Get MSU green
   color = get_bigten_colors("MSU")
   print(color)  # '#18453B'

Multiple Institutions
^^^^^^^^^^^^^^^^^^^^^

.. code-block:: python

   from msuthemes import get_bigten_colors

   # Get colors for multiple schools
   colors = get_bigten_colors(["MSU", "Michigan", "Ohio State"])
   # Returns: {'MSU': '#18453B', 'Michigan': '#00274C', 'Ohio State': '#BB0000'}

Flexible Name Recognition
--------------------------

Institution names can be specified many ways:

.. code-block:: python

   from msuthemes import get_bigten_colors

   # All of these work for MSU
   get_bigten_colors("MSU")
   get_bigten_colors("Michigan State")
   get_bigten_colors("Spartans")
   get_bigten_colors("State")

   # All of these work for Michigan
   get_bigten_colors("Michigan")
   get_bigten_colors("UM")
   get_bigten_colors("Wolverines")

   # All of these work for Ohio State
   get_bigten_colors("Ohio State")
   get_bigten_colors("OSU")
   get_bigten_colors("Buckeyes")

Creating Big Ten Palettes
--------------------------

All Schools
^^^^^^^^^^^

.. code-block:: python

   from msuthemes import bigten_palette

   # Get all 18 Big Ten colors
   colors = bigten_palette()

Specific Schools
^^^^^^^^^^^^^^^^

.. code-block:: python

   from msuthemes import bigten_palette

   # Get colors for specific schools
   rivalry_colors = bigten_palette(["MSU", "Michigan", "Ohio State"])

As Palette Object
^^^^^^^^^^^^^^^^^

.. code-block:: python

   from msuthemes import bigten_palette

   # Get as MSUPalette object
   palette = bigten_palette(as_palette=True)

   # Convert to colormap
   cmap = palette.as_matplotlib_cmap()

Visualization Examples
-----------------------

Comparing Schools
^^^^^^^^^^^^^^^^^

.. code-block:: python

   import matplotlib.pyplot as plt
   from msuthemes import theme_msu, get_bigten_colors

   theme_msu()

   schools = ['MSU', 'Michigan', 'Ohio State', 'Penn State']
   values = [50, 45, 55, 48]

   colors_dict = get_bigten_colors(schools)
   colors_list = [colors_dict[s] for s in schools]

   plt.bar(schools, values, color=colors_list)
   plt.ylabel('Value')
   plt.title('Big Ten Comparison')
   plt.show()

With Dataset
^^^^^^^^^^^^

.. code-block:: python

   import matplotlib.pyplot as plt
   from msuthemes import theme_msu, get_bigten_colors, load_bigten_data

   theme_msu()

   # Load enrollment data
   schools = ['MSU', 'Michigan', 'Ohio State']
   data = load_bigten_data(
       institutions=schools,
       columns=['name', 'entry_term', 'UGDS']
   )

   # Get colors
   colors = get_bigten_colors(schools)

   # Plot
   for school in schools:
       school_data = data[data['name'] == school]
       plt.plot(
           school_data['entry_term'],
           school_data['UGDS'],
           label=school,
           color=colors[school],
           linewidth=2
       )

   plt.xlabel('Year')
   plt.ylabel('Enrollment')
   plt.title('Big Ten Enrollment Trends')
   plt.legend()
   plt.show()

Listing and Validating
-----------------------

List All Institutions
^^^^^^^^^^^^^^^^^^^^^

.. code-block:: python

   from msuthemes import list_bigten_institutions

   institutions = list_bigten_institutions()
   print(institutions)  # Sorted alphabetically

Get Institution Info
^^^^^^^^^^^^^^^^^^^^

.. code-block:: python

   from msuthemes.bigten import get_institution_info

   info = get_institution_info("MSU")
   print(info)
   # {'name': 'MSU',
   #  'primary_color': '#18453B',
   #  'secondary_color': '#FFFFFF'}

Validate Institution Name
^^^^^^^^^^^^^^^^^^^^^^^^^^

.. code-block:: python

   from msuthemes.bigten import validate_institution

   # Check if valid
   is_valid = validate_institution("MSU")  # True
   is_valid = validate_institution("Spartans")  # True
   is_valid = validate_institution("Invalid")  # False

Working with Data
-----------------

See :doc:`datasets` for complete guide on using the BigTen dataset.

Quick example:

.. code-block:: python

   from msuthemes import load_bigten_data

   # Load data for Big Ten East schools
   east = ['MSU', 'Michigan', 'Ohio State', 'Penn State',
           'Indiana', 'Maryland', 'Rutgers']

   data = load_bigten_data(
       institutions=east,
       years=[2020, 2021, 2022, 2023]
   )

Next Steps
----------

* :doc:`datasets` - Work with BigTen historical data
* :doc:`colors` - Learn about MSU colors
* :doc:`api/bigten` - Complete Big Ten reference
