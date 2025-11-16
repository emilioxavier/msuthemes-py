Big Ten Module
==============

.. automodule:: msuthemes.bigten
   :members:
   :undoc-members:
   :show-inheritance:

Functions
---------

.. autofunction:: msuthemes.bigten.get_bigten_colors

.. autofunction:: msuthemes.bigten.bigten_palette

.. autofunction:: msuthemes.bigten.list_bigten_institutions

.. autofunction:: msuthemes.bigten.normalize_institution_name

.. autofunction:: msuthemes.bigten.get_institution_info

.. autofunction:: msuthemes.bigten.validate_institution

Supported Institutions
----------------------

The module supports all 18 Big Ten Conference institutions:

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

Institution Name Aliases
-------------------------

The module recognizes 80+ aliases for Big Ten institutions:

**Michigan State:**
  * MSU
  * Michigan State
  * Spartans
  * State

**Michigan:**
  * Michigan
  * UM, U-M
  * UMich
  * Wolverines

**Ohio State:**
  * Ohio State
  * OSU
  * Buckeyes
  * The Ohio State University

*(See full list in source code)*

Usage Examples
--------------

Getting Institution Colors
^^^^^^^^^^^^^^^^^^^^^^^^^^

.. code-block:: python

   from msuthemes import get_bigten_colors

   # Single institution
   color = get_bigten_colors("MSU")
   print(color)  # '#18453B'

   # Multiple institutions
   colors = get_bigten_colors(["MSU", "Michigan", "Ohio State"])
   # Returns: {'MSU': '#18453B', 'Michigan': '#00274C', 'Ohio State': '#BB0000'}

   # Using nicknames
   color = get_bigten_colors("Spartans")      # Same as "MSU"
   color = get_bigten_colors("Wolverines")    # Same as "Michigan"
   color = get_bigten_colors("Buckeyes")      # Same as "Ohio State"

   # Secondary colors
   secondary = get_bigten_colors("MSU", color_type="secondary")

Creating Big Ten Palettes
^^^^^^^^^^^^^^^^^^^^^^^^^^

.. code-block:: python

   from msuthemes import bigten_palette

   # All Big Ten colors
   all_colors = bigten_palette()
   print(len(all_colors))  # 18

   # Specific institutions
   rivalry_colors = bigten_palette(["MSU", "Michigan", "Ohio State"])

   # As MSUPalette object
   palette = bigten_palette(as_palette=True)
   matplotlib_cmap = palette.as_matplotlib_cmap()

Listing Institutions
^^^^^^^^^^^^^^^^^^^^

.. code-block:: python

   from msuthemes import list_bigten_institutions

   # Get all institutions
   institutions = list_bigten_institutions()
   print(institutions)
   # ['Illinois', 'Indiana', 'Iowa', 'MSU', 'Maryland', ...]

Institution Information
^^^^^^^^^^^^^^^^^^^^^^^

.. code-block:: python

   from msuthemes.bigten import get_institution_info, normalize_institution_name

   # Get full information
   info = get_institution_info("MSU")
   print(info)
   # {'name': 'MSU',
   #  'primary_color': '#18453B',
   #  'secondary_color': '#FFFFFF'}

   # Normalize institution name
   normalized = normalize_institution_name("spartans")
   print(normalized)  # 'MSU'

Validating Institution Names
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

.. code-block:: python

   from msuthemes.bigten import validate_institution

   # Check if valid
   is_valid = validate_institution("MSU")  # True
   is_valid = validate_institution("Spartans")  # True
   is_valid = validate_institution("Invalid School")  # False
