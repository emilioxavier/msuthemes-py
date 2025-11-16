"""Big Ten institutional color utilities.

This module provides helper functions for working with Big Ten institutional colors.

Functions:
    get_bigten_colors: Get colors for specific institutions
    bigten_palette: Get palette of all Big Ten colors
    list_bigten_institutions: List all Big Ten institutions
    normalize_institution_name: Normalize institution name

Examples:
    >>> from msuthemes.bigten import get_bigten_colors
    >>>
    >>> # Get single institution color
    >>> color = get_bigten_colors("MSU")
    >>> print(color)
    '#18453B'
    >>>
    >>> # Get multiple institution colors
    >>> colors = get_bigten_colors(["MSU", "Michigan", "Ohio State"])
    >>> print(colors)
    {'MSU': '#18453B', 'Michigan': '#FFCB05', 'Ohio State': '#BB0000'}
"""

from typing import Union, List, Dict, Optional
from msuthemes.colors import BIGTEN_COLORS_PRIMARY, BIGTEN_COLORS_SECONDARY
from msuthemes.palettes import MSUPalette


# Institution name aliases for flexible input
INSTITUTION_ALIASES = {
    # Illinois
    "illinois": "Illinois",
    "uiuc": "Illinois",
    "fighting illini": "Illinois",
    "u of i": "Illinois",

    # Indiana
    "indiana": "Indiana",
    "iu": "Indiana",
    "hoosiers": "Indiana",

    # Iowa
    "iowa": "Iowa",
    "hawkeyes": "Iowa",
    "u of iowa": "Iowa",

    # Maryland
    "maryland": "Maryland",
    "umd": "Maryland",
    "terps": "Maryland",
    "terrapins": "Maryland",

    # Michigan
    "michigan": "Michigan",
    "um": "Michigan",
    "u-m": "Michigan",
    "umich": "Michigan",
    "wolverines": "Michigan",

    # Michigan State
    "msu": "MSU",
    "michigan state": "MSU",
    "spartans": "MSU",
    "state": "MSU",

    # Minnesota
    "minnesota": "Minnesota",
    "gophers": "Minnesota",
    "u of m": "Minnesota",

    # Nebraska
    "nebraska": "Nebraska",
    "huskers": "Nebraska",
    "cornhuskers": "Nebraska",

    # Northwestern
    "northwestern": "Northwestern",
    "nu": "Northwestern",
    "wildcats": "Northwestern",

    # Ohio State
    "ohio state": "Ohio State",
    "osu": "Ohio State",
    "buckeyes": "Ohio State",
    "the ohio state university": "Ohio State",

    # Oregon
    "oregon": "Oregon",
    "ducks": "Oregon",
    "uo": "Oregon",

    # Penn State
    "penn state": "Penn State",
    "psu": "Penn State",
    "nittany lions": "Penn State",

    # Purdue
    "purdue": "Purdue",
    "boilermakers": "Purdue",

    # Rutgers
    "rutgers": "Rutgers",
    "scarlet knights": "Rutgers",
    "ru": "Rutgers",

    # UCLA
    "ucla": "UCLA",
    "bruins": "UCLA",

    # USC
    "usc": "USC",
    "usocal": "USC",
    "southern california": "USC",
    "trojans": "USC",

    # Washington
    "washington": "Washington",
    "uw": "Washington",
    "huskies": "Washington",
    "udub": "Washington",

    # Wisconsin
    "wisconsin": "Wisconsin",
    "badgers": "Wisconsin",
    "uw-madison": "Wisconsin",
}


def normalize_institution_name(name: str) -> str:
    """Normalize institution name to standard format.

    This function handles various spellings, abbreviations, and nicknames
    for Big Ten institutions.

    Args:
        name: Institution name (case-insensitive)

    Returns:
        Normalized institution name

    Raises:
        ValueError: If institution name is not recognized

    Examples:
        >>> normalize_institution_name("msu")
        'MSU'
        >>> normalize_institution_name("Spartans")
        'MSU'
        >>> normalize_institution_name("buckeyes")
        'Ohio State'
    """
    # Convert to lowercase for lookup
    name_lower = name.strip().lower()

    # Check if already in canonical form
    if name in BIGTEN_COLORS_PRIMARY:
        return name

    # Check aliases
    if name_lower in INSTITUTION_ALIASES:
        return INSTITUTION_ALIASES[name_lower]

    # Not found
    available = list_bigten_institutions()
    raise ValueError(
        f"Institution '{name}' not recognized. "
        f"Available institutions: {', '.join(available)}"
    )


def list_bigten_institutions() -> List[str]:
    """List all Big Ten institutions.

    Returns:
        List of institution names in alphabetical order

    Examples:
        >>> institutions = list_bigten_institutions()
        >>> print(len(institutions))
        18
        >>> print(institutions[:3])
        ['Illinois', 'Indiana', 'Iowa']
    """
    # Get unique institutions (exclude aliases like USoCal)
    institutions = set(BIGTEN_COLORS_PRIMARY.keys())
    institutions.discard("USoCal")  # USC is the canonical name
    return sorted(institutions)


def get_bigten_colors(
    institutions: Union[str, List[str]],
    color_type: str = "primary"
) -> Union[str, Dict[str, str]]:
    """Get Big Ten institutional colors.

    Retrieve primary or secondary colors for one or more Big Ten institutions.
    Supports flexible institution name input (abbreviations, nicknames, etc.).

    Args:
        institutions: Single institution name or list of institution names
        color_type: Type of color - "primary" or "secondary" (default: "primary")

    Returns:
        If single institution: hex color string
        If multiple institutions: dictionary mapping institution names to colors

    Raises:
        ValueError: If institution name not recognized or invalid color type

    Examples:
        >>> # Single institution
        >>> color = get_bigten_colors("MSU")
        >>> print(color)
        '#18453B'

        >>> # Multiple institutions
        >>> colors = get_bigten_colors(["MSU", "Michigan", "Ohio State"])
        >>> print(colors)
        {'MSU': '#18453B', 'Michigan': '#FFCB05', 'Ohio State': '#BB0000'}

        >>> # Using nicknames
        >>> color = get_bigten_colors("Spartans")
        >>> print(color)
        '#18453B'

        >>> # Secondary colors
        >>> color = get_bigten_colors("MSU", color_type="secondary")
        >>> print(color)
        '#FFFFFF'
    """
    # Validate color type
    if color_type not in ("primary", "secondary"):
        raise ValueError(
            f"color_type must be 'primary' or 'secondary', got '{color_type}'"
        )

    # Select color dictionary
    color_dict = (
        BIGTEN_COLORS_PRIMARY if color_type == "primary"
        else BIGTEN_COLORS_SECONDARY
    )

    # Handle single institution
    if isinstance(institutions, str):
        normalized_name = normalize_institution_name(institutions)
        return color_dict[normalized_name]

    # Handle multiple institutions
    result = {}
    for inst in institutions:
        normalized_name = normalize_institution_name(inst)
        result[normalized_name] = color_dict[normalized_name]

    return result


def bigten_palette(
    institutions: Optional[List[str]] = None,
    color_type: str = "primary",
    as_palette: bool = False
) -> Union[List[str], MSUPalette]:
    """Create a color palette from Big Ten institutional colors.

    Args:
        institutions: List of institutions to include (default: all 18)
        color_type: Type of color - "primary" or "secondary" (default: "primary")
        as_palette: If True, return MSUPalette object; if False, return list

    Returns:
        List of hex colors or MSUPalette object

    Examples:
        >>> # Get all Big Ten colors
        >>> palette = bigten_palette()
        >>> print(len(palette))
        18

        >>> # Get colors for specific schools
        >>> palette = bigten_palette(["MSU", "Michigan", "Ohio State"])
        >>> print(palette)
        ['#18453B', '#FFCB05', '#BB0000']

        >>> # Get as MSUPalette object
        >>> palette = bigten_palette(as_palette=True)
        >>> colors = palette.as_hex(n_colors=5)
    """
    # Use all institutions if not specified
    if institutions is None:
        institutions = list_bigten_institutions()

    # Get colors
    colors_dict = get_bigten_colors(institutions, color_type=color_type)

    # Extract colors in order
    if isinstance(colors_dict, str):
        colors = [colors_dict]
    else:
        colors = list(colors_dict.values())

    # Return as list or palette
    if as_palette:
        return MSUPalette(
            colors=colors,
            palette_type="qual",
            name=f"bigten_{color_type}"
        )
    return colors


def get_institution_info(institution: str) -> Dict[str, str]:
    """Get comprehensive information about a Big Ten institution.

    Args:
        institution: Institution name

    Returns:
        Dictionary with institution information including:
        - name: Canonical name
        - primary_color: Primary color hex
        - secondary_color: Secondary color hex

    Examples:
        >>> info = get_institution_info("MSU")
        >>> print(info['name'])
        'MSU'
        >>> print(info['primary_color'])
        '#18453B'
    """
    normalized_name = normalize_institution_name(institution)

    return {
        "name": normalized_name,
        "primary_color": BIGTEN_COLORS_PRIMARY[normalized_name],
        "secondary_color": BIGTEN_COLORS_SECONDARY[normalized_name],
    }


def validate_institution(institution: str) -> bool:
    """Check if an institution name is valid.

    Args:
        institution: Institution name to validate

    Returns:
        True if valid, False otherwise

    Examples:
        >>> validate_institution("MSU")
        True
        >>> validate_institution("Spartans")
        True
        >>> validate_institution("Invalid School")
        False
    """
    try:
        normalize_institution_name(institution)
        return True
    except ValueError:
        return False


__all__ = [
    "get_bigten_colors",
    "bigten_palette",
    "list_bigten_institutions",
    "normalize_institution_name",
    "get_institution_info",
    "validate_institution",
]
