"""MSU and Big Ten color definitions.

This module contains all color constant definitions for MSU and Big Ten institutions.

Color naming convention:
    - All color constants are uppercase
    - MSU colors prefixed with MSU_
    - Big Ten colors organized in dictionaries by institution

Examples:
    >>> from msuthemes.colors import MSU_GREEN, MSU_ORANGE
    >>> from msuthemes.colors import BIGTEN_COLORS_PRIMARY
    >>>
    >>> print(MSU_GREEN)
    '#18453B'
    >>>
    >>> print(BIGTEN_COLORS_PRIMARY['MSU'])
    '#18453B'
"""

from typing import Dict

# =============================================================================
# MSU Primary Colors
# =============================================================================

MSU_GREEN: str = "#18453B"
"""MSU Spartan Green - Primary institutional color"""

MSU_SPARTAN_GREEN: str = "#18453B"
"""MSU Spartan Green (alias) - Primary institutional color"""

MSU_WHITE: str = "#FFFFFF"
"""MSU White - Primary institutional color"""

MSU_BLACK: str = "#000000"
"""MSU Black - Primary institutional color"""


# =============================================================================
# MSU Secondary/Accent Colors
# =============================================================================

MSU_GREY: str = "#C3C4C6"
"""MSU Grey"""

MSU_GRAY: str = "#C3C4C6"
"""MSU Gray (alias)"""

MSU_ORANGE: str = "#FF6F00"
"""MSU Orange"""

MSU_TEAL: str = "#008183"
"""MSU Teal"""

MSU_PURPLE: str = "#5B3256"
"""MSU Purple"""

MSU_BLUE: str = "#909AB7"
"""MSU Blue (Blue-Grey)"""

MSU_BLUE_GREY: str = "#909AB7"
"""MSU Blue-Grey (alias)"""

MSU_BLUE_GRAY: str = "#909AB7"
"""MSU Blue-Gray (alias)"""

MSU_DARK_GREY: str = "#535054"
"""MSU Dark Grey"""

MSU_DARK_GRAY: str = "#535054"
"""MSU Dark Gray (alias)"""

MSU_YELLOW: str = "#D1DE3F"
"""MSU Yellow (Yellow-Green / Grellow)"""

MSU_YELLOW_GREEN: str = "#D1DE3F"
"""MSU Yellow-Green (alias)"""

MSU_GREEN_YELLOW: str = "#D1DE3F"
"""MSU Green-Yellow (alias)"""

MSU_GRELLOW: str = "#D1DE3F"
"""MSU Grellow (alias) - Green + Yellow"""

MSU_PEACH: str = "#E8D9B5"
"""MSU Peach"""

MSU_BURNT_ORANGE: str = "#C89A58"
"""MSU Burnt Orange"""

MSU_SPLIT_PEA: str = "#94AE4A"
"""MSU Split Pea"""

MSU_EGGPLANT: str = "#6E005F"
"""MSU Eggplant"""

MSU_RED: str = "#CB5A28"
"""MSU Red (Sienna)"""

MSU_SIENNA: str = "#CB5A28"
"""MSU Sienna (alias)"""


# =============================================================================
# Additional MSU Green Variants
# =============================================================================

MSU_GREEN_LIGHT: str = "#9BB9A8"
"""MSU Light Green"""

MSU_GREEN_DARK: str = "#0F2922"
"""MSU Dark Green"""

MSU_GREEN_BRIGHT: str = "#3FA060"
"""MSU Bright Green"""

MSU_KELLY_GREEN: str = "#008208"
"""MSU Kelly Green"""

MSU_LIME_GREEN: str = "#7BBD00"
"""MSU Lime Green"""

MSU_EXCELLENCE_GREEN: str = "#0B9A6D"
"""MSU Excellence Green"""

MSU_REFRESH_GREEN: str = "#008934"
"""MSU Refresh Green"""


# =============================================================================
# Big Ten Institutional Colors - Primary
# =============================================================================

BIGTEN_COLORS_PRIMARY: Dict[str, str] = {
    "Illinois": "#FF552E",
    "Indiana": "#990000",
    "Iowa": "#FFCD00",
    "MSU": "#18453B",
    "Maryland": "#F0163A",
    "Michigan": "#00274C",
    "Minnesota": "#FFCC33",
    "Nebraska": "#D00000",
    "Northwestern": "#4E2A84",
    "Ohio State": "#BB0000",
    "Oregon": "#007030",
    "Penn State": "#001E44",
    "Purdue": "#CFB991",
    "Rutgers": "#CC0033",
    "UCLA": "#2774AE",
    "USoCal": "#990000",
    "Washington": "#4B2E83",
    "Wisconsin": "#DA004C",
}
"""Big Ten institutional primary colors"""


# =============================================================================
# Big Ten Institutional Colors - Secondary
# =============================================================================

BIGTEN_COLORS_SECONDARY: Dict[str, str] = {
    "Illinois": "#13294B",
    "Indiana": "#EDEBEB",
    "Iowa": "#000000",
    "MSU": "#FFFFFF",
    "Maryland": "#FFD90F",
    "Michigan": "#FFCB05",
    "Minnesota": "#7A0019",
    "Nebraska": "#F5F1E7",
    "Northwestern": "#E4E0EE",
    "Ohio State": "#666666",
    "Oregon": "#FEE11A",
    "Penn State": "#FFFFFF",
    "Purdue": "#000000",
    "Rutgers": "#525C5C",
    "UCLA": "#FFD100",
    "USoCal": "#FFCC00",
    "Washington": "#E8E3D3",
    "Wisconsin": "#FFFFFF",
}
"""Big Ten institutional secondary colors"""


# =============================================================================
# Export all color constants
# =============================================================================

__all__ = [
    # MSU Primary
    "MSU_GREEN",
    "MSU_SPARTAN_GREEN",
    "MSU_WHITE",
    "MSU_BLACK",
    # MSU Secondary/Accent
    "MSU_GREY",
    "MSU_GRAY",
    "MSU_ORANGE",
    "MSU_TEAL",
    "MSU_PURPLE",
    "MSU_BLUE",
    "MSU_BLUE_GREY",
    "MSU_BLUE_GRAY",
    "MSU_DARK_GREY",
    "MSU_DARK_GRAY",
    "MSU_YELLOW",
    "MSU_YELLOW_GREEN",
    "MSU_GREEN_YELLOW",
    "MSU_GRELLOW",
    "MSU_PEACH",
    "MSU_BURNT_ORANGE",
    "MSU_SPLIT_PEA",
    "MSU_EGGPLANT",
    "MSU_RED",
    "MSU_SIENNA",
    # Additional MSU Greens
    "MSU_GREEN_LIGHT",
    "MSU_GREEN_DARK",
    "MSU_GREEN_BRIGHT",
    "MSU_KELLY_GREEN",
    "MSU_LIME_GREEN",
    "MSU_EXCELLENCE_GREEN",
    "MSU_REFRESH_GREEN",
    # Big Ten Colors
    "BIGTEN_COLORS_PRIMARY",
    "BIGTEN_COLORS_SECONDARY",
]
