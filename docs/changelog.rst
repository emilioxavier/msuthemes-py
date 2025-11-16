Changelog
=========

All notable changes to MSUthemes will be documented in this file.

The format is based on `Keep a Changelog <https://keepachangelog.com/en/1.0.0/>`_,
and this project adheres to `Semantic Versioning <https://semver.org/spec/v2.0.0.html>`_.

[0.1.0] - 2025-01-XX
--------------------

Initial alpha release of MSUthemes for Python.

Added
^^^^^

* **Colors Module**

  * MSU primary colors (green, white, black)
  * MSU secondary/accent colors (orange, teal, purple, grey)
  * MSU green variants (light, dark, bright)
  * Big Ten primary and secondary colors for all 18 institutions
  * Color constants accessible as module attributes

* **Palettes Module**

  * MSUPalette class for palette management
  * 4 sequential palettes (msu_seq, msu_seq2, msu_seq_full, msu_green)
  * 4 diverging palettes (msu_div, msu_div2, msu_div_orange, msu_div_purple)
  * 3 qualitative palettes (msu_qual1, msu_qual2, msu_qual3)
  * Big Ten primary and secondary palettes
  * Conversion to matplotlib colormaps
  * Conversion to seaborn palettes
  * Color interpolation for continuous palettes

* **Fonts Module**

  * Bundled Metropolis font (9 weights: 100-900)
  * Italic variants for all weights
  * Automatic font registration with matplotlib
  * Font availability checking
  * Font path utilities

* **Themes Module**

  * ``theme_msu()`` function for matplotlib theming
  * Customizable theme parameters (font size, grid, colors)
  * ``set_msu_style()`` for seaborn integration
  * ``reset_theme()`` to restore defaults
  * ``get_current_theme()`` to inspect settings
  * MSU color cycle (10 colors)
  * Professional default styling

* **Big Ten Module**

  * ``get_bigten_colors()`` for institutional colors
  * ``bigten_palette()`` for color palette generation
  * 80+ institution name aliases (nicknames, abbreviations)
  * ``normalize_institution_name()`` for flexible input
  * ``list_bigten_institutions()`` to list all schools
  * ``get_institution_info()`` for comprehensive data
  * ``validate_institution()`` for name validation

* **Data Module**

  * BigTen dataset (1996-2023, 18 institutions, 38 variables)
  * ``load_bigten_data()`` with filtering by institution, year, columns
  * ``get_bigten_summary()`` for summary statistics
  * ``get_dataset_info()`` for dataset metadata
  * Integration with institution name aliases
  * College Scorecard data including:

    * Enrollment (total, by gender, by race/ethnicity)
    * Admission rates
    * Completion rates
    * Tuition and fees
    * Cost of attendance
    * Demographics

* **Utilities Module**

  * ``hex_to_rgb()`` color conversion
  * ``rgb_to_hex()`` color conversion
  * ``validate_hex_color()`` validation
  * ``get_color_brightness()`` brightness calculation
  * ``lighten_color()`` and ``darken_color()`` utilities

* **Documentation**

  * Comprehensive Sphinx documentation
  * Installation guide
  * Quickstart guide
  * API reference for all modules
  * Gallery with examples
  * Migration guide for R users
  * Contributing guidelines

* **Testing**

  * Test scripts for all modules
  * Import tests
  * Font tests
  * Theme tests
  * Big Ten functionality tests
  * Data loading tests

Dependencies
^^^^^^^^^^^^

* Python >= 3.8
* NumPy >= 1.20.0
* matplotlib >= 3.5.0
* pandas >= 1.3.0
* seaborn >= 0.12.0 (optional)
* plotly >= 5.0.0 (optional, planned)

Notes
^^^^^

This is an alpha release. The API is subject to change in future versions.

[Unreleased]
------------

Planned
^^^^^^^

* Plotly theme support
* Additional color palettes
* Interactive palette picker
* More dataset utilities
* PyPI publication
* Read the Docs hosting

---

**Legend:**

* ``Added`` for new features
* ``Changed`` for changes in existing functionality
* ``Deprecated`` for soon-to-be removed features
* ``Removed`` for now removed features
* ``Fixed`` for any bug fixes
* ``Security`` for vulnerability fixes
