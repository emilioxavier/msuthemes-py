Gallery
=======

Example visualizations using MSUthemes.

Basic Examples
--------------

Line Plots
^^^^^^^^^^

Create a simple line plot with MSU theme:

.. code-block:: python

   import matplotlib.pyplot as plt
   import numpy as np
   from msuthemes import theme_msu, colors

   theme_msu()

   x = np.linspace(0, 10, 100)
   y1 = np.sin(x)
   y2 = np.cos(x)

   fig, ax = plt.subplots(figsize=(8, 6))
   ax.plot(x, y1, color=colors.MSU_GREEN, label='sin(x)', linewidth=2)
   ax.plot(x, y2, color=colors.MSU_ORANGE, label='cos(x)', linewidth=2)
   ax.set_xlabel('X')
   ax.set_ylabel('Y')
   ax.set_title('MSU-Themed Line Plot')
   ax.legend()
   plt.show()

Bar Charts
^^^^^^^^^^

Create a bar chart with MSU qualitative palette:

.. code-block:: python

   import matplotlib.pyplot as plt
   from msuthemes import theme_msu, palettes

   theme_msu()

   categories = ['A', 'B', 'C', 'D', 'E']
   values = [23, 45, 56, 78, 32]
   colors = palettes.msu_qual1.as_hex(n_colors=5)

   fig, ax = plt.subplots(figsize=(8, 6))
   ax.bar(categories, values, color=colors)
   ax.set_xlabel('Category')
   ax.set_ylabel('Value')
   ax.set_title('MSU-Themed Bar Chart')
   plt.show()

Scatter Plots
^^^^^^^^^^^^^

Create a scatter plot with MSU colors:

.. code-block:: python

   import matplotlib.pyplot as plt
   import numpy as np
   from msuthemes import theme_msu, colors

   theme_msu()

   np.random.seed(42)
   x = np.random.randn(100)
   y = np.random.randn(100)

   fig, ax = plt.subplots(figsize=(8, 6))
   ax.scatter(x, y, c=colors.MSU_GREEN, s=50, alpha=0.6)
   ax.set_xlabel('X Variable')
   ax.set_ylabel('Y Variable')
   ax.set_title('MSU-Themed Scatter Plot')
   plt.show()

Seaborn Examples
----------------

Heatmaps
^^^^^^^^

Create a heatmap with MSU sequential palette:

.. code-block:: python

   import seaborn as sns
   import numpy as np
   from msuthemes import set_msu_style, palettes

   set_msu_style(style='white')

   data = np.random.rand(10, 10)
   cmap = palettes.msu_seq.as_matplotlib_cmap()

   sns.heatmap(data, cmap=cmap, square=True, cbar_kws={'label': 'Value'})
   plt.title('MSU-Themed Heatmap')
   plt.show()

Box Plots
^^^^^^^^^

Create box plots with Big Ten colors:

.. code-block:: python

   import seaborn as sns
   import pandas as pd
   import numpy as np
   from msuthemes import set_msu_style, bigten_palette

   set_msu_style()

   # Generate sample data
   data = pd.DataFrame({
       'School': ['MSU', 'Michigan', 'Ohio State'] * 30,
       'Score': np.random.randn(90) + [70, 65, 75] * 30
   })

   colors = bigten_palette(['MSU', 'Michigan', 'Ohio State'])

   sns.boxplot(data=data, x='School', y='Score', palette=colors)
   plt.title('Big Ten Comparison')
   plt.show()

Big Ten Data Examples
----------------------

Enrollment Trends
^^^^^^^^^^^^^^^^^

Visualize enrollment trends for Big Ten schools:

.. code-block:: python

   import matplotlib.pyplot as plt
   from msuthemes import (
       theme_msu,
       load_bigten_data,
       get_bigten_colors
   )

   theme_msu()

   # Load data for selected schools
   schools = ['MSU', 'Michigan', 'Ohio State']
   data = load_bigten_data(
       institutions=schools,
       columns=['name', 'entry_term', 'UGDS']
   )

   # Get school colors
   colors = get_bigten_colors(schools)

   # Plot
   fig, ax = plt.subplots(figsize=(10, 6))
   for school in schools:
       school_data = data[data['name'] == school]
       ax.plot(
           school_data['entry_term'],
           school_data['UGDS'],
           label=school,
           color=colors[school],
           linewidth=2
       )

   ax.set_xlabel('Year')
   ax.set_ylabel('Total Enrollment')
   ax.set_title('Big Ten Enrollment Trends (1996-2023)')
   ax.legend()
   plt.show()

Admission Rates
^^^^^^^^^^^^^^^

Compare admission rates across Big Ten schools:

.. code-block:: python

   import matplotlib.pyplot as plt
   from msuthemes import (
       theme_msu,
       load_bigten_data,
       bigten_palette
   )

   theme_msu()

   # Load recent data
   data = load_bigten_data(
       years=[2023],
       columns=['name', 'ADM_RATE']
   )

   # Sort by admission rate
   data = data.sort_values('ADM_RATE', ascending=False)

   # Get colors
   colors = bigten_palette(data['name'].tolist())

   # Plot
   fig, ax = plt.subplots(figsize=(10, 8))
   ax.barh(data['name'], data['ADM_RATE'] * 100, color=colors)
   ax.set_xlabel('Admission Rate (%)')
   ax.set_title('Big Ten Admission Rates (2023)')
   plt.tight_layout()
   plt.show()

Advanced Examples
-----------------

Multi-Panel Figures
^^^^^^^^^^^^^^^^^^^

Create complex multi-panel figures:

.. code-block:: python

   import matplotlib.pyplot as plt
   import numpy as np
   from msuthemes import theme_msu, palettes, colors

   theme_msu()

   fig, ((ax1, ax2), (ax3, ax4)) = plt.subplots(2, 2, figsize=(12, 10))

   # Panel 1: Line plot
   x = np.linspace(0, 10, 100)
   ax1.plot(x, np.sin(x), color=colors.MSU_GREEN, linewidth=2)
   ax1.set_title('A) Sine Wave')

   # Panel 2: Bar chart
   categories = ['A', 'B', 'C', 'D']
   values = [23, 45, 56, 32]
   palette_colors = palettes.msu_qual1.as_hex(n_colors=4)
   ax2.bar(categories, values, color=palette_colors)
   ax2.set_title('B) Categories')

   # Panel 3: Scatter plot
   ax3.scatter(np.random.randn(100), np.random.randn(100),
               c=colors.MSU_TEAL, alpha=0.5)
   ax3.set_title('C) Distribution')

   # Panel 4: Histogram
   data = np.random.normal(0, 1, 1000)
   ax4.hist(data, bins=30, color=colors.MSU_ORANGE, alpha=0.7)
   ax4.set_title('D) Histogram')

   plt.tight_layout()
   plt.show()

Custom Color Gradients
^^^^^^^^^^^^^^^^^^^^^^

Create custom color gradients:

.. code-block:: python

   import matplotlib.pyplot as plt
   import numpy as np
   from msuthemes import theme_msu
   from msuthemes.palettes import MSUPalette

   theme_msu()

   # Create custom gradient
   custom = MSUPalette(
       colors=['#18453B', '#FFFFFF', '#FF6F00'],
       palette_type='div',
       name='custom'
   )

   # Use in visualization
   data = np.random.rand(20, 20)
   cmap = custom.as_matplotlib_cmap()

   plt.imshow(data, cmap=cmap)
   plt.colorbar(label='Value')
   plt.title('Custom MSU Color Gradient')
   plt.show()

More Examples
-------------

For more examples and tutorials, see:

* :doc:`../quickstart` - Basic usage patterns
* :doc:`../api/index` - API documentation with examples
* GitHub repository examples/ directory
