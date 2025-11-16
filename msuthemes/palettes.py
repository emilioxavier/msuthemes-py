"""MSU color palette definitions and utilities.

This module provides palette generation and management for MSU color schemes.

Palette types:
    - Sequential: For continuous data
    - Diverging: For data with a meaningful midpoint
    - Qualitative: For categorical data

Examples:
    >>> from msuthemes.palettes import msu_seq, msu_div
    >>>
    >>> # Get 5 colors from sequential palette
    >>> colors = msu_seq.as_hex(n_colors=5)
    >>>
    >>> # Get matplotlib colormap
    >>> cmap = msu_seq.as_matplotlib_cmap()
"""

from typing import List, Optional
from matplotlib.colors import LinearSegmentedColormap, ListedColormap

# TODO: Phase 2 - Implement palette classes and instances
# - MSUPalette class
# - msu_seq, msu_seq_red, msu_seq_blue (sequential palettes)
# - msu_div (diverging palette)
# - msu_qual1, msu_qual2 (qualitative palettes)

__all__ = []
