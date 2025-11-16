"""MSUthemes: MSU and Big Ten color palettes and themes for Python.

This package provides color palettes and themes for Michigan State University
and all Big Ten Conference institutions, designed for data visualization with
matplotlib, seaborn, and plotly.

Modules:
    colors: Color constant definitions
    palettes: Palette generation and management
    fonts: Metropolis font utilities and management
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

# Import submodules
from msuthemes import colors
from msuthemes import palettes
from msuthemes import fonts
from msuthemes import utils

# Import commonly used items for convenience
from msuthemes.colors import (
    MSU_GREEN,
    MSU_WHITE,
    MSU_BLACK,
    MSU_ORANGE,
    MSU_TEAL,
    BIGTEN_COLORS_PRIMARY,
    BIGTEN_COLORS_SECONDARY,
)

from msuthemes.palettes import (
    msu_seq,
    msu_div,
    msu_qual1,
    msu_qual2,
    MSU_PALETTES,
    get_palette,
    list_palettes,
)

from msuthemes.fonts import (
    register_metropolis_fonts,
    is_metropolis_available,
    get_font_path,
)

# Package metadata and exports
__all__ = [
    # Version info
    "__version__",
    "__author__",
    "__email__",
    "__license__",
    # Submodules
    "colors",
    "palettes",
    "fonts",
    "utils",
    # Common colors
    "MSU_GREEN",
    "MSU_WHITE",
    "MSU_BLACK",
    "MSU_ORANGE",
    "MSU_TEAL",
    "BIGTEN_COLORS_PRIMARY",
    "BIGTEN_COLORS_SECONDARY",
    # Palettes
    "msu_seq",
    "msu_div",
    "msu_qual1",
    "msu_qual2",
    "MSU_PALETTES",
    "get_palette",
    "list_palettes",
    # Fonts
    "register_metropolis_fonts",
    "is_metropolis_available",
    "get_font_path",
]

# Future imports (to be added in later phases)
# from .themes import theme_msu, set_msu_style
# from .bigten import get_bigten_colors, bigten_palette
# from .data import load_bigten_data
