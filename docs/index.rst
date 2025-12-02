MSUthemes Documentation
=======================

**MSU and Big Ten color palettes and themes for Python data visualization**

MSUthemes provides a comprehensive suite of color palettes, themes, and datasets for creating professional,
MSU-branded visualizations using matplotlib, seaborn, and plotly.

.. image:: https://img.shields.io/badge/License-CC%20BY--SA%204.0-lightgrey.svg
   :target: https://creativecommons.org/licenses/by-sa/4.0/
   :alt: License: CC BY-SA 4.0

Quick Links
-----------

* :doc:`installation` - Get started with MSUthemes
* :doc:`quickstart` - Basic usage examples
* :doc:`api/index` - Complete API reference
* :doc:`gallery/index` - Example plots and visualizations
* :doc:`migration` - Guide for R users

Features
--------

✓ **MSU Brand Colors**
   Official Michigan State University colors including MSU Green, White, and accent colors

✓ **Big Ten Colors**
   Complete color sets for all 18 Big Ten Conference institutions with flexible name recognition

✓ **Color Palettes**
   11 carefully designed palettes (sequential, diverging, qualitative) optimized for data visualization

✓ **Metropolis Font**
   Professional typography with bundled Metropolis font (9 weights, italic variants)

✓ **matplotlib/seaborn Themes**
   Ready-to-use themes that apply MSU branding to all your plots

✓ **BigTen Dataset**
   Historical institutional data (1996-2023) for research and analysis

Installation
------------

Install MSUthemes via pip:

.. code-block:: bash

   pip install msuthemes

Or install from source:

.. code-block:: bash

   git clone https://github.com/emilioxavier/msuthemes-py.git
   cd msuthemes-py
   pip install -e .

Quick Example
-------------

.. code-block:: python

   import matplotlib.pyplot as plt
   from msuthemes import theme_msu, colors
   import numpy as np

   # Apply MSU theme
   theme_msu()

   # Create a plot with MSU Green
   x = np.linspace(0, 10, 100)
   y = np.sin(x)

   fig, ax = plt.subplots()
   ax.plot(x, y, color=colors.MSU_GREEN, linewidth=2)
   ax.set_title('MSU-Branded Plot')
   plt.show()

Table of Contents
-----------------

.. toctree::
   :maxdepth: 2
   :caption: User Guide

   installation
   quickstart
   colors
   palettes
   themes
   bigten
   datasets

.. toctree::
   :maxdepth: 2
   :caption: API Reference

   api/index
   api/colors
   api/palettes
   api/fonts
   api/themes
   api/bigten
   api/data
   api/utils

.. toctree::
   :maxdepth: 1
   :caption: Gallery

   gallery/index

.. toctree::
   :maxdepth: 1
   :caption: Additional Resources

   migration
   contributing
   changelog
   license

Indices and tables
------------------

* :ref:`genindex`
* :ref:`modindex`
* :ref:`search`

About
-----

MSUthemes is developed and maintained by Emilio Xavier Esposito at Michigan State University.
It is the Python implementation of the `MSUthemes R package <https://cran.r-project.org/package=MSUthemes>`_.

License
-------

This project is licensed under the Creative Commons Attribution-ShareAlike 4.0 International License (CC BY-SA 4.0).

See :doc:`license` for more information.

Contact
-------

* **Author**: Emilio Xavier Esposito
* **Email**: emilio@msu.edu
* **GitHub**: https://github.com/emilioxavier/msuthemes-py
* **Issues**: https://github.com/emilioxavier/msuthemes-py/issues
