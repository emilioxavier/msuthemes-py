API Reference
=============

Complete API documentation for all MSUthemes modules.

Core Modules
------------

.. toctree::
   :maxdepth: 2

   colors
   palettes
   fonts
   themes
   bigten
   data
   utils

Quick Links
-----------

Colors
^^^^^^

* :mod:`msuthemes.colors` - MSU and Big Ten color constants

Palettes
^^^^^^^^

* :mod:`msuthemes.palettes` - Color palette generation and management
* :class:`msuthemes.palettes.MSUPalette` - Palette class

Fonts
^^^^^

* :mod:`msuthemes.fonts` - Metropolis font utilities
* :func:`msuthemes.fonts.register_metropolis_fonts` - Register fonts with matplotlib
* :func:`msuthemes.fonts.is_metropolis_available` - Check font availability

Themes
^^^^^^

* :mod:`msuthemes.themes` - matplotlib and seaborn themes
* :func:`msuthemes.themes.theme_msu` - Apply MSU theme to matplotlib
* :func:`msuthemes.themes.set_msu_style` - Apply MSU style to seaborn

Big Ten
^^^^^^^

* :mod:`msuthemes.bigten` - Big Ten institutional color utilities
* :func:`msuthemes.bigten.get_bigten_colors` - Get institution colors
* :func:`msuthemes.bigten.bigten_palette` - Create Big Ten color palette

Data
^^^^

* :mod:`msuthemes.data` - Dataset loading and management
* :func:`msuthemes.data.load_bigten_data` - Load BigTen dataset
* :func:`msuthemes.data.get_bigten_summary` - Get dataset summary

Utilities
^^^^^^^^^

* :mod:`msuthemes.utils` - Helper functions and utilities
