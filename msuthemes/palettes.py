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

from typing import List, Optional, Union
import numpy as np
from matplotlib.colors import LinearSegmentedColormap, ListedColormap


class MSUPalette:
    """MSU Color Palette class.

    This class represents a color palette and provides methods to:
    - Get colors as hex strings
    - Get colors as RGB tuples
    - Generate matplotlib colormaps
    - Interpolate colors for continuous palettes
    """

    def __init__(self, colors: List[str], palette_type: str, name: str = ""):
        """Initialize an MSU color palette.

        Args:
            colors: List of hex color codes
            palette_type: Type of palette ("seq", "div", or "qual")
            name: Name of the palette
        """
        self.colors = colors
        self.palette_type = palette_type
        self.name = name
        self._validate()

    def _validate(self):
        """Validate palette configuration."""
        valid_types = ["seq", "div", "qual", "core"]
        if self.palette_type not in valid_types:
            raise ValueError(
                f"Invalid palette type: {self.palette_type}. "
                f"Must be one of {valid_types}"
            )

        if not self.colors:
            raise ValueError("Palette must contain at least one color")

    def __repr__(self) -> str:
        """String representation of the palette."""
        return f"MSUPalette(name='{self.name}', type='{self.palette_type}', n_colors={len(self.colors)})"

    def __len__(self) -> int:
        """Return the number of colors in the palette."""
        return len(self.colors)

    def as_hex(self, n_colors: Optional[int] = None, reverse: bool = False) -> List[str]:
        """Get colors as hex strings.

        Args:
            n_colors: Number of colors to return. If None, returns all colors.
                     If greater than palette length, interpolates (continuous mode).
            reverse: If True, reverse the color order

        Returns:
            List of hex color strings

        Examples:
            >>> palette = msu_seq
            >>> palette.as_hex()  # All colors
            >>> palette.as_hex(n_colors=5)  # 5 colors
            >>> palette.as_hex(n_colors=5, reverse=True)  # 5 colors, reversed
        """
        if n_colors is None:
            colors = self.colors[::-1] if reverse else self.colors
            return colors

        if n_colors <= 0:
            raise ValueError("n_colors must be positive")

        # Get the colors without reversing first
        if n_colors <= len(self.colors):
            # For discrete selection, evenly space the colors
            if n_colors == len(self.colors):
                result = self.colors[:]
            else:
                indices = np.linspace(0, len(self.colors) - 1, n_colors).astype(int)
                result = [self.colors[i] for i in indices]
        else:
            # If requesting more colors than available, interpolate
            result = self._interpolate_colors(n_colors, reverse=False)

        # Apply reverse after selection
        return result[::-1] if reverse else result

    def as_rgb(self, n_colors: Optional[int] = None, reverse: bool = False) -> List[tuple]:
        """Get colors as RGB tuples (0-255 range).

        Args:
            n_colors: Number of colors to return. If None, returns all colors.
                     If greater than palette length, interpolates (continuous mode).
            reverse: If True, reverse the color order

        Returns:
            List of RGB tuples with values in 0-255 range

        Examples:
            >>> palette = msu_seq
            >>> palette.as_rgb()  # All colors as RGB
            >>> palette.as_rgb(n_colors=5)  # 5 colors as RGB
            >>> palette.as_rgb(n_colors=5, reverse=True)  # 5 colors, reversed
        """
        hex_colors = self.as_hex(n_colors=n_colors, reverse=reverse)

        rgb_colors = []
        for hex_color in hex_colors:
            hex_color = hex_color.lstrip('#')
            r = int(hex_color[0:2], 16)
            g = int(hex_color[2:4], 16)
            b = int(hex_color[4:6], 16)
            rgb_colors.append((r, g, b))

        return rgb_colors

    def _hex_to_rgb_normalized(self, hex_color: str) -> tuple:
        """Convert hex to normalized RGB (0-1)."""
        hex_color = hex_color.lstrip('#')
        r, g, b = int(hex_color[0:2], 16), int(hex_color[2:4], 16), int(hex_color[4:6], 16)
        return (r / 255.0, g / 255.0, b / 255.0)

    def _rgb_to_hex(self, rgb: tuple) -> str:
        """Convert normalized RGB (0-1) to hex."""
        r, g, b = int(rgb[0] * 255), int(rgb[1] * 255), int(rgb[2] * 255)
        return f'#{r:02X}{g:02X}{b:02X}'

    def _interpolate_colors(self, n_colors: int, reverse: bool = False) -> List[str]:
        """Interpolate colors to generate more colors than in palette.

        Args:
            n_colors: Number of colors to generate
            reverse: Whether to reverse the palette

        Returns:
            List of interpolated hex colors
        """
        colors = self.colors[::-1] if reverse else self.colors

        # Convert hex to RGB
        rgb_colors = [self._hex_to_rgb_normalized(c) for c in colors]

        # Create interpolation positions
        positions = np.linspace(0, 1, len(rgb_colors))
        new_positions = np.linspace(0, 1, n_colors)

        # Interpolate each channel
        r_interp = np.interp(new_positions, positions, [c[0] for c in rgb_colors])
        g_interp = np.interp(new_positions, positions, [c[1] for c in rgb_colors])
        b_interp = np.interp(new_positions, positions, [c[2] for c in rgb_colors])

        # Convert back to hex
        interpolated_colors = [
            self._rgb_to_hex((r, g, b))
            for r, g, b in zip(r_interp, g_interp, b_interp)
        ]

        return interpolated_colors

    def as_matplotlib_cmap(self, name: Optional[str] = None, n_colors: int = 256) -> Union[LinearSegmentedColormap, ListedColormap]:
        """Create a matplotlib colormap from the palette.

        Args:
            name: Name for the colormap (defaults to palette name)
            n_colors: Number of discrete colors for qualitative palettes

        Returns:
            matplotlib colormap object

        Examples:
            >>> import matplotlib.pyplot as plt
            >>> cmap = msu_seq.as_matplotlib_cmap()
            >>> plt.imshow([[1,2,3]], cmap=cmap)
        """
        cmap_name = name or self.name or "msu_palette"

        if self.palette_type in ["seq", "div"]:
            # Create continuous colormap with interpolation
            colors_rgb = [self._hex_to_rgb_normalized(c) for c in self.colors]
            return LinearSegmentedColormap.from_list(cmap_name, colors_rgb, N=256)
        else:
            # Create discrete colormap for qualitative/core palettes
            colors_rgb = [self._hex_to_rgb_normalized(c) for c in self.colors]
            return ListedColormap(colors_rgb, name=cmap_name)

    def show(self, n_colors: Optional[int] = None):
        """Display the palette colors (requires matplotlib).

        Args:
            n_colors: Number of colors to display (default: all)
        """
        try:
            import matplotlib.pyplot as plt
            import matplotlib.patches as mpatches
        except ImportError:
            raise ImportError("matplotlib is required to display palettes")

        colors = self.as_hex(n_colors=n_colors)

        fig, ax = plt.subplots(figsize=(len(colors) * 0.5, 1))
        ax.set_xlim(0, len(colors))
        ax.set_ylim(0, 1)
        ax.axis('off')

        for i, color in enumerate(colors):
            rect = mpatches.Rectangle((i, 0), 1, 1, facecolor=color, edgecolor='black', linewidth=0.5)
            ax.add_patch(rect)
            ax.text(i + 0.5, 0.5, color, ha='center', va='center',
                   fontsize=7, rotation=90, color='white' if i % 2 == 0 else 'black')

        plt.title(f"{self.name} ({self.palette_type})")
        plt.tight_layout()
        plt.show()


# =============================================================================
# MSU Sequential Palettes
# =============================================================================

msu_seq = MSUPalette(
    colors=[
        "#18453B", "#2F574E", "#466A62",
        "#5D7C75", "#748F89", "#8BA29D",
        "#A2B4B0", "#B9C7C4", "#D0D9D7",
        "#E7ECEB"
    ],
    palette_type="seq",
    name="msu_seq"
)
"""MSU Sequential Palette - Main (10 colors, green-based)"""

msu_seq_red = MSUPalette(
    colors=[
        "#280D01", "#511D06", "#792F0E",
        "#A24319", "#CB5A28", "#D5764C",
        "#DF9573", "#EAB69E", "#F4D9CD"
    ],
    palette_type="seq",
    name="msu_seq_red"
)
"""MSU Sequential Palette - Red (9 colors)"""

msu_seq_purple = MSUPalette(
    colors=[
        "#150012", "#2C0025", "#420038",
        "#58004B", "#6E005F", "#8B1B7B",
        "#A7439A", "#C476BA", "#E2B4DB"
    ],
    palette_type="seq",
    name="msu_seq_purple"
)
"""MSU Sequential Palette - Purple (9 colors)"""

msu_seq_yellow = MSUPalette(
    colors=[
        "#313608", "#51590F", "#798418",
        "#A5B326", "#D1DE3F", "#D5E051",
        "#DCE365", "#E3ED84", "#F2F6C8"
    ],
    palette_type="seq",
    name="msu_seq_yellow"
)
"""MSU Sequential Palette - Yellow (9 colors)"""

msu_seq_blue = MSUPalette(
    colors=[
        "#282B42", "#3D4263", "#5E668F",
        "#7980A3", "#909AB7", "#A5AABF",
        "#B3B7C9", "#C2C6D4", "#D5D8E3"
    ],
    palette_type="seq",
    name="msu_seq_blue"
)
"""MSU Sequential Palette - Blue (9 colors)"""

msu_seq_orange = MSUPalette(
    colors=[
        "#4B2704", "#6E3B0B", "#945110",
        "#BD6A15", "#F08521", "#F2AC62",
        "#F5C487", "#F7D8AD", "#FFE3BF"
    ],
    palette_type="seq",
    name="msu_seq_orange"
)
"""MSU Sequential Palette - Orange (9 colors)"""

msu_seq_green = MSUPalette(
    colors=[
        "#00230D", "#02461C", "#046A2B",
        "#088D3A", "#0DB14B", "#31C067",
        "#5CD088", "#8CDFAC", "#C3EFD3"
    ],
    palette_type="seq",
    name="msu_seq_green"
)
"""MSU Sequential Palette - Green (9 colors, bright green variant)"""

msu_seq2 = MSUPalette(
    colors=[
        "#0F2922", "#18453B", "#3FA060",
        "#9BB9A8", "#D0D9D7", "#E7ECEB"
    ],
    palette_type="seq",
    name="msu_seq2"
)
"""MSU Sequential Palette 2 (6 colors, green gradient)"""


# =============================================================================
# MSU Diverging Palettes
# =============================================================================

msu_div = MSUPalette(
    colors=[
        "#E41B12", "#EB5751", "#F29490",
        "#F9D1CF", "#D4D4D4", "#CCEBF3",
        "#88D0E3", "#43B6D3", "#009CC4"
    ],
    palette_type="div",
    name="msu_div"
)
"""MSU Diverging Palette (9 colors, red to blue)"""

msu_div2 = MSUPalette(
    colors=[
        "#CB5A28", "#DF9573", "#F4D9CD",
        "#FFFFFF", "#9BB9A8", "#466A62",
        "#18453B"
    ],
    palette_type="div",
    name="msu_div2"
)
"""MSU Diverging Palette 2 (7 colors, orange to green through white)"""


# =============================================================================
# MSU Core Palette
# =============================================================================

msu_core = MSUPalette(
    colors=["#18453B", "#FFFFFF", "#000000"],
    palette_type="core",
    name="msu_core"
)
"""MSU Core Palette (3 colors: MSU Green, White, Black)"""


# =============================================================================
# MSU Qualitative Palettes
# =============================================================================

msu_qual1 = MSUPalette(
    colors=[
        "#18453B",  # MSU green
        "#0DB14B",  # Kelly green
        "#97A2A2",  # Grey
        "#F08521",  # Orange
        "#008183",  # Teal
        "#909AB7",  # Blue-grey
        "#535054",  # Dark grey
        "#D1DE3F",  # Yellow-green
        "#E8D9B5",  # Cream
        "#C89A58",  # Texas-brown
        "#94AE4A",  # Split pea soup green
        "#6E005F",  # Eggplant
        "#CB5A28"   # Sienna
    ],
    palette_type="qual",
    name="msu_qual1"
)
"""MSU Qualitative Palette 1 (13 colors for categorical data)"""

msu_qual2 = MSUPalette(
    colors=[
        "#18453B",  # MSU green
        "#F08521",  # Orange
        "#6E005F",  # Purple/Eggplant
        "#97A2A2"   # Grey
    ],
    palette_type="qual",
    name="msu_qual2"
)
"""MSU Qualitative Palette 2 (4 colors for categorical data)"""


# =============================================================================
# Big Ten Palettes
# =============================================================================

# Import colors from colors module
from .colors import BIGTEN_COLORS_PRIMARY, BIGTEN_COLORS_SECONDARY

bigten_primary = MSUPalette(
    colors=list(BIGTEN_COLORS_PRIMARY.values()),
    palette_type="qual",
    name="bigten_primary"
)
"""Big Ten Primary Colors Palette (18 colors)"""

bigten_secondary = MSUPalette(
    colors=list(BIGTEN_COLORS_SECONDARY.values()),
    palette_type="qual",
    name="bigten_secondary"
)
"""Big Ten Secondary Colors Palette (18 colors)"""


# =============================================================================
# Palette Dictionary (for easy access by name)
# =============================================================================

MSU_PALETTES = {
    "msu_seq": msu_seq,
    "msu_seq2": msu_seq2,
    "msu_seq_red": msu_seq_red,
    "msu_seq_purple": msu_seq_purple,
    "msu_seq_yellow": msu_seq_yellow,
    "msu_seq_blue": msu_seq_blue,
    "msu_seq_orange": msu_seq_orange,
    "msu_seq_green": msu_seq_green,
    "msu_div": msu_div,
    "msu_div2": msu_div2,
    "msu_core": msu_core,
    "msu_qual1": msu_qual1,
    "msu_qual2": msu_qual2,
    "bigten_primary": bigten_primary,
    "bigten_secondary": bigten_secondary,
}
"""Dictionary of all MSU palettes for easy access by name"""


def get_palette(name: str) -> MSUPalette:
    """Get a palette by name.

    Args:
        name: Name of the palette

    Returns:
        MSUPalette object

    Raises:
        ValueError: If palette name not found

    Examples:
        >>> palette = get_palette("msu_seq")
        >>> colors = palette.as_hex(n_colors=5)
    """
    if name not in MSU_PALETTES:
        available = ", ".join(MSU_PALETTES.keys())
        raise ValueError(
            f"Palette '{name}' not found. Available palettes: {available}"
        )
    return MSU_PALETTES[name]


def list_palettes() -> List[str]:
    """List all available palette names.

    Returns:
        List of palette names

    Examples:
        >>> palettes = list_palettes()
        >>> print(palettes)
        ['msu_seq', 'msu_seq_red', ...]
    """
    return list(MSU_PALETTES.keys())


__all__ = [
    "MSUPalette",
    # Sequential palettes
    "msu_seq",
    "msu_seq_red",
    "msu_seq_purple",
    "msu_seq_yellow",
    "msu_seq_blue",
    "msu_seq_orange",
    "msu_seq_green",
    # Diverging palette
    "msu_div",
    # Core palette
    "msu_core",
    # Qualitative palettes
    "msu_qual1",
    "msu_qual2",
    # Dictionary and utilities
    "MSU_PALETTES",
    "get_palette",
    "list_palettes",
]
