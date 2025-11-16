Migration Guide for R Users
===========================

This guide helps users of the MSUthemes R package transition to the Python version.

Overview
--------

The Python implementation of MSUthemes provides similar functionality to the R package,
with adaptations for Python's visualization libraries (matplotlib, seaborn, plotly) instead
of R's ggplot2.

Installation Comparison
-----------------------

**R:**

.. code-block:: r

   install.packages("MSUthemes")
   library(MSUthemes)

**Python:**

.. code-block:: python

   pip install msuthemes
   import msuthemes

Core Concepts
-------------

Colors
^^^^^^

**R:**

.. code-block:: r

   library(MSUthemes)

   # Access MSU colors
   msu_colors$green
   msu_colors$white

   # Get Big Ten colors
   bigten_colors("MSU")
   bigten_colors(c("MSU", "Michigan", "Ohio State"))

**Python:**

.. code-block:: python

   from msuthemes import colors, get_bigten_colors

   # Access MSU colors
   colors.MSU_GREEN
   colors.MSU_WHITE

   # Get Big Ten colors
   get_bigten_colors("MSU")
   get_bigten_colors(["MSU", "Michigan", "Ohio State"])

Palettes
^^^^^^^^

**R:**

.. code-block:: r

   # Get MSU sequential palette
   scale_color_msu_seq()
   scale_fill_msu_seq()

   # Get MSU diverging palette
   scale_color_msu_div()

   # Get qualitative palette
   scale_color_msu_qual()

**Python:**

.. code-block:: python

   from msuthemes import palettes

   # Get colors from sequential palette
   colors = palettes.msu_seq.as_hex(n_colors=5)

   # Get diverging palette as colormap
   cmap = palettes.msu_div.as_matplotlib_cmap()

   # Get qualitative palette
   qual_colors = palettes.msu_qual1.as_hex()

Themes
^^^^^^

**R:**

.. code-block:: r

   library(ggplot2)
   library(MSUthemes)

   # Apply MSU theme to ggplot2
   ggplot(data, aes(x, y)) +
     geom_point() +
     theme_msu()

**Python:**

.. code-block:: python

   import matplotlib.pyplot as plt
   from msuthemes import theme_msu

   # Apply MSU theme to matplotlib
   theme_msu()

   plt.plot(x, y)
   plt.show()

Side-by-Side Examples
---------------------

Basic Plot
^^^^^^^^^^

**R (ggplot2):**

.. code-block:: r

   library(ggplot2)
   library(MSUthemes)

   ggplot(mtcars, aes(x = wt, y = mpg)) +
     geom_point(color = msu_colors$green, size = 3) +
     labs(title = "Fuel Efficiency vs Weight",
          x = "Weight (1000 lbs)",
          y = "Miles per Gallon") +
     theme_msu()

**Python (matplotlib):**

.. code-block:: python

   import matplotlib.pyplot as plt
   from msuthemes import theme_msu, colors

   theme_msu()

   plt.scatter(df['wt'], df['mpg'],
               color=colors.MSU_GREEN, s=50)
   plt.xlabel('Weight (1000 lbs)')
   plt.ylabel('Miles per Gallon')
   plt.title('Fuel Efficiency vs Weight')
   plt.show()

Bar Chart with Custom Colors
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

**R:**

.. code-block:: r

   library(ggplot2)
   library(MSUthemes)

   ggplot(data, aes(x = category, y = value, fill = category)) +
     geom_col() +
     scale_fill_msu_qual() +
     theme_msu()

**Python:**

.. code-block:: python

   import matplotlib.pyplot as plt
   from msuthemes import theme_msu, palettes

   theme_msu()

   colors = palettes.msu_qual1.as_hex(n_colors=len(categories))
   plt.bar(data['category'], data['value'], color=colors)
   plt.show()

Heatmap
^^^^^^^

**R:**

.. code-block:: r

   library(ggplot2)
   library(MSUthemes)

   ggplot(data, aes(x = x, y = y, fill = value)) +
     geom_tile() +
     scale_fill_gradient_msu() +
     theme_msu()

**Python:**

.. code-block:: python

   import seaborn as sns
   from msuthemes import set_msu_style, palettes

   set_msu_style()

   cmap = palettes.msu_seq.as_matplotlib_cmap()
   sns.heatmap(data, cmap=cmap)
   plt.show()

Big Ten Comparisons
^^^^^^^^^^^^^^^^^^^

**R:**

.. code-block:: r

   library(ggplot2)
   library(MSUthemes)

   # Load BigTen dataset
   data(BigTen)

   # Filter and plot
   BigTen %>%
     filter(name %in% c("MSU", "Michigan", "Ohio State")) %>%
     ggplot(aes(x = entry_term, y = UGDS, color = name)) +
     geom_line(size = 1.5) +
     scale_color_bigten() +
     labs(title = "Enrollment Trends",
          x = "Year",
          y = "Total Enrollment") +
     theme_msu()

**Python:**

.. code-block:: python

   import matplotlib.pyplot as plt
   from msuthemes import theme_msu, load_bigten_data, get_bigten_colors

   theme_msu()

   # Load BigTen dataset
   data = load_bigten_data(
       institutions=['MSU', 'Michigan', 'Ohio State'],
       columns=['name', 'entry_term', 'UGDS']
   )

   # Get colors
   colors = get_bigten_colors(['MSU', 'Michigan', 'Ohio State'])

   # Plot
   for school in ['MSU', 'Michigan', 'Ohio State']:
       school_data = data[data['name'] == school]
       plt.plot(school_data['entry_term'],
                school_data['UGDS'],
                label=school,
                color=colors[school],
                linewidth=2)

   plt.xlabel('Year')
   plt.ylabel('Total Enrollment')
   plt.title('Enrollment Trends')
   plt.legend()
   plt.show()

Function Mapping
----------------

This table shows equivalent functions between R and Python:

.. list-table::
   :header-rows: 1
   :widths: 40 40 20

   * - R Function
     - Python Equivalent
     - Notes
   * - ``msu_colors$green``
     - ``colors.MSU_GREEN``
     - Direct access
   * - ``bigten_colors("MSU")``
     - ``get_bigten_colors("MSU")``
     - Same syntax
   * - ``scale_color_msu_seq()``
     - ``palettes.msu_seq.as_hex()``
     - Returns list
   * - ``scale_fill_msu_div()``
     - ``palettes.msu_div.as_matplotlib_cmap()``
     - Returns colormap
   * - ``theme_msu()``
     - ``theme_msu()``
     - Apply before plotting
   * - ``data(BigTen)``
     - ``load_bigten_data()``
     - Returns pandas DataFrame

Key Differences
---------------

1. **Plotting Paradigm**

   * R: Declarative (ggplot2 layers)
   * Python: Imperative (matplotlib) or declarative (seaborn)

2. **Theme Application**

   * R: Added as ggplot2 layer
   * Python: Applied globally before creating plots

3. **Data Loading**

   * R: ``data(BigTen)`` loads into environment
   * Python: ``load_bigten_data()`` returns DataFrame

4. **Color Access**

   * R: List-style (``msu_colors$green``)
   * Python: Module attributes (``colors.MSU_GREEN``)

5. **Palette Integration**

   * R: Integrated with ggplot2 scales
   * Python: Must be explicitly applied to plots

Workflow Comparison
-------------------

Typical R Workflow
^^^^^^^^^^^^^^^^^^

.. code-block:: r

   library(ggplot2)
   library(MSUthemes)
   library(dplyr)

   # Load data
   data(BigTen)

   # Process and plot
   BigTen %>%
     filter(name == "MSU") %>%
     ggplot(aes(x = entry_term, y = UGDS)) +
     geom_line(color = msu_colors$green, size = 1.5) +
     labs(title = "MSU Enrollment",
          x = "Year",
          y = "Enrollment") +
     theme_msu()

Equivalent Python Workflow
^^^^^^^^^^^^^^^^^^^^^^^^^^^

.. code-block:: python

   import matplotlib.pyplot as plt
   from msuthemes import theme_msu, colors, load_bigten_data

   # Apply theme first
   theme_msu()

   # Load and filter data
   data = load_bigten_data(
       institutions=['MSU'],
       columns=['entry_term', 'UGDS']
   )

   # Plot
   plt.plot(data['entry_term'], data['UGDS'],
            color=colors.MSU_GREEN, linewidth=2)
   plt.xlabel('Year')
   plt.ylabel('Enrollment')
   plt.title('MSU Enrollment')
   plt.show()

Tips for R Users
----------------

1. **Import modules explicitly**: Unlike R's ``library()``, import what you need

   .. code-block:: python

      from msuthemes import theme_msu, colors, palettes

2. **Apply theme before plotting**: Unlike ggplot2, theme is applied globally

   .. code-block:: python

      theme_msu()  # Do this first
      # Then create all your plots

3. **Use pandas for data manipulation**: Similar to dplyr

   .. code-block:: python

      import pandas as pd
      df = load_bigten_data()
      msu_data = df[df['name'] == 'MSU']  # Like filter()

4. **Seaborn is closer to ggplot2**: Consider using seaborn for declarative plotting

   .. code-block:: python

      import seaborn as sns
      from msuthemes import set_msu_style

      set_msu_style()
      sns.scatterplot(data=df, x='x', y='y', hue='category')

5. **Save plots explicitly**: Unlike R, plots aren't automatically displayed

   .. code-block:: python

      plt.savefig('plot.png', dpi=300)
      plt.show()

Feature Parity Matrix
---------------------

.. list-table::
   :header-rows: 1
   :widths: 40 15 15 30

   * - Feature
     - R
     - Python
     - Notes
   * - MSU Colors
     - ✓
     - ✓
     - Complete
   * - Big Ten Colors
     - ✓
     - ✓
     - Complete
   * - Color Palettes
     - ✓
     - ✓
     - 11 palettes
   * - Metropolis Font
     - ✓
     - ✓
     - Bundled
   * - ggplot2 Theme
     - ✓
     - N/A
     - R only
   * - matplotlib Theme
     - N/A
     - ✓
     - Python only
   * - seaborn Integration
     - N/A
     - ✓
     - Python only
   * - BigTen Dataset
     - ✓
     - ✓
     - Same data
   * - plotly Support
     - Partial
     - Planned
     - Future

Getting Help
------------

If you're transitioning from R and have questions:

1. Check the :doc:`quickstart` guide
2. Review the :doc:`gallery/index` for examples
3. Consult the :doc:`api/index` reference
4. Open an issue on GitHub with your R code for Python equivalents

Common Questions
----------------

**Q: Can I use both R and Python versions together?**

A: Yes! The packages are completely independent and can be used in the same project
(e.g., R for analysis, Python for visualization).

**Q: Is the Python version as complete as the R version?**

A: The core functionality is equivalent. Some R-specific ggplot2 integrations don't
have direct Python equivalents, but matplotlib/seaborn provide similar capabilities.

**Q: Which should I use?**

A: Use R if you're already in the R ecosystem and using ggplot2. Use Python if you're
working with matplotlib/seaborn or prefer Python's data science stack.

**Q: Can I convert my R plots to Python?**

A: While not automatic, most R visualizations can be recreated in Python using similar
patterns. See the side-by-side examples above.

Next Steps
----------

* :doc:`quickstart` - Get started with Python MSUthemes
* :doc:`api/index` - Full API documentation
* :doc:`gallery/index` - More examples
