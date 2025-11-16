"""MSUthemes: MSU and Big Ten color palettes and themes for Python.

This package provides color palettes and themes for Michigan State University
and all Big Ten Conference institutions, designed for data visualization with
matplotlib, seaborn, and plotly.

Modules:
    colors: Color constant definitions
    palettes: Palette generation and management
    themes: matplotlib and seaborn theme functions
    bigten: Big Ten institutional color utilities
    utils: Helper functions

Examples:
    >>> from msuthemes import theme_msu, colors
    >>> import matplotlib.pyplot as plt
    >>>
    >>> # Apply MSU theme
    >>> theme_msu()
    >>>
    >>> # Use MSU colors
    >>> plt.plot([1, 2, 3], color=colors.MSU_GREEN)
"""

__version__ = "0.1.0"
__author__ = "Emilio Xavier Esposito"
__email__ = "emilio@msu.edu"
__license__ = "CC-BY-SA-4.0"

# Package metadata
__all__ = [
    "__version__",
    "__author__",
    "__email__",
    "__license__",
]

# Placeholder imports - will be populated as modules are created
# from .colors import *
# from .palettes import *
# from .themes import theme_msu, set_msu_style
# from .bigten import get_bigten_colors, bigten_palette
# from .data import load_bigten_data
