"""Utility functions for MSUthemes.

This module contains helper functions used throughout the package.

Functions:
    validate_hex_color: Validate hex color format
    hex_to_rgb: Convert hex color to RGB tuple
    rgb_to_hex: Convert RGB tuple to hex color
    hex_to_rgba: Convert hex color to RGBA tuple
    normalize_hex: Normalize hex color to uppercase with # prefix

Examples:
    >>> from msuthemes.utils import validate_hex_color, hex_to_rgb
    >>>
    >>> validate_hex_color("#18453B")
    True
    >>>
    >>> hex_to_rgb("#18453B")
    (24, 69, 59)
"""

import re
from typing import Tuple, Union, Optional


def validate_hex_color(color: str) -> bool:
    """Validate if a string is a valid hex color code.

    Args:
        color: String to validate as hex color (must start with #)

    Returns:
        True if valid hex color, False otherwise

    Examples:
        >>> validate_hex_color("#18453B")
        True
        >>> validate_hex_color("18453B")
        False
        >>> validate_hex_color("#ZZZ")
        False
    """
    if not isinstance(color, str):
        return False

    # Must start with #
    if not color.startswith('#'):
        return False

    # Remove # for validation
    hex_part = color[1:]

    # Check if it's exactly 6 hex digits (strict validation)
    if len(hex_part) != 6:
        return False

    # Check if all characters are valid hex
    return bool(re.match(r'^[0-9A-Fa-f]{6}$', hex_part))


def normalize_hex(color: str) -> str:
    """Normalize hex color to uppercase with # prefix.

    Args:
        color: Hex color string

    Returns:
        Normalized hex color (uppercase, with #)

    Raises:
        ValueError: If color is not a valid hex color

    Examples:
        >>> normalize_hex("18453b")
        '#18453B'
        >>> normalize_hex("#18453b")
        '#18453B'
    """
    if not validate_hex_color(color):
        raise ValueError(f"Invalid hex color: {color}")

    # Remove # if present and convert to uppercase
    color = color.lstrip('#').upper()

    # Expand 3-digit hex to 6-digit
    if len(color) == 3:
        color = ''.join([c*2 for c in color])

    return f'#{color}'


def hex_to_rgb(hex_color: str) -> Tuple[int, int, int]:
    """Convert hex color to RGB tuple.

    Args:
        hex_color: Hex color string (e.g., "#18453B" or "18453B")

    Returns:
        Tuple of (R, G, B) values (0-255)

    Raises:
        ValueError: If hex_color is not a valid hex color

    Examples:
        >>> hex_to_rgb("#18453B")
        (24, 69, 59)
        >>> hex_to_rgb("FFFFFF")
        (255, 255, 255)
    """
    # Normalize the color first
    hex_color = normalize_hex(hex_color)

    # Remove the # prefix
    hex_color = hex_color.lstrip('#')

    # Convert to RGB
    r = int(hex_color[0:2], 16)
    g = int(hex_color[2:4], 16)
    b = int(hex_color[4:6], 16)

    return (r, g, b)


def rgb_to_hex(r: int, g: int, b: int) -> str:
    """Convert RGB tuple to hex color.

    Args:
        r: Red value (0-255)
        g: Green value (0-255)
        b: Blue value (0-255)

    Returns:
        Hex color string with # prefix

    Raises:
        ValueError: If RGB values are out of range

    Examples:
        >>> rgb_to_hex(24, 69, 59)
        '#18453B'
        >>> rgb_to_hex(255, 255, 255)
        '#FFFFFF'
    """
    # Validate RGB values
    for val, name in [(r, 'R'), (g, 'G'), (b, 'B')]:
        if not isinstance(val, int) or not 0 <= val <= 255:
            raise ValueError(f"{name} value must be an integer between 0 and 255, got {val}")

    return f'#{r:02X}{g:02X}{b:02X}'


def hex_to_rgba(hex_color: str, alpha: float = 1.0) -> Tuple[float, float, float, float]:
    """Convert hex color to RGBA tuple (normalized 0-1).

    Useful for matplotlib which often expects RGBA values in 0-1 range.

    Args:
        hex_color: Hex color string (e.g., "#18453B" or "18453B")
        alpha: Alpha/opacity value (0-1, default 1.0)

    Returns:
        Tuple of (R, G, B, A) values normalized to 0-1

    Raises:
        ValueError: If hex_color is not valid or alpha out of range

    Examples:
        >>> hex_to_rgba("#18453B")
        (0.09411764705882353, 0.27058823529411763, 0.23137254901960785, 1.0)
        >>> hex_to_rgba("#18453B", alpha=0.5)
        (0.09411764705882353, 0.27058823529411763, 0.23137254901960785, 0.5)
    """
    if not 0.0 <= alpha <= 1.0:
        raise ValueError(f"Alpha must be between 0 and 1, got {alpha}")

    r, g, b = hex_to_rgb(hex_color)

    return (r / 255.0, g / 255.0, b / 255.0, alpha)


def rgb_to_rgba(r: int, g: int, b: int, alpha: float = 1.0) -> Tuple[float, float, float, float]:
    """Convert RGB tuple to RGBA tuple (normalized 0-1).

    Args:
        r: Red value (0-255)
        g: Green value (0-255)
        b: Blue value (0-255)
        alpha: Alpha/opacity value (0-1, default 1.0)

    Returns:
        Tuple of (R, G, B, A) values normalized to 0-1

    Raises:
        ValueError: If RGB values or alpha are out of range

    Examples:
        >>> rgb_to_rgba(24, 69, 59)
        (0.09411764705882353, 0.27058823529411763, 0.23137254901960785, 1.0)
    """
    # Validate using rgb_to_hex (which validates the RGB values)
    hex_color = rgb_to_hex(r, g, b)
    return hex_to_rgba(hex_color, alpha)


def get_color_brightness(hex_color: str) -> float:
    """Calculate perceived brightness of a color.

    Uses the relative luminance formula from WCAG, scaled to 0-255 range.

    Args:
        hex_color: Hex color string

    Returns:
        Brightness value (0-255, where 255 is brightest)

    Examples:
        >>> get_color_brightness("#FFFFFF")  # White
        255.0
        >>> get_color_brightness("#000000")  # Black
        0.0
    """
    r, g, b = hex_to_rgb(hex_color)

    # Convert to 0-1 range
    r, g, b = r / 255.0, g / 255.0, b / 255.0

    # Apply gamma correction
    def adjust(c):
        if c <= 0.03928:
            return c / 12.92
        return ((c + 0.055) / 1.055) ** 2.4

    r, g, b = adjust(r), adjust(g), adjust(b)

    # Calculate relative luminance and scale to 0-255
    return (0.2126 * r + 0.7152 * g + 0.0722 * b) * 255.0


def lighten_color(hex_color: str, amount: float = 0.2) -> str:
    """Lighten a color by mixing it with white.

    Args:
        hex_color: Hex color string to lighten
        amount: Amount to lighten (0-1, where 0 is no change, 1 is white)

    Returns:
        Lightened hex color string

    Raises:
        ValueError: If amount is not in range [0, 1]

    Examples:
        >>> lighten_color("#18453B", amount=0.2)
        '#466959'
        >>> lighten_color("#FFFFFF", amount=0.5)  # White stays white
        '#FFFFFF'
    """
    if not 0.0 <= amount <= 1.0:
        raise ValueError(f"Amount must be between 0 and 1, got {amount}")

    r, g, b = hex_to_rgb(hex_color)

    # Mix with white (255, 255, 255)
    r = int(r + (255 - r) * amount)
    g = int(g + (255 - g) * amount)
    b = int(b + (255 - b) * amount)

    # Clamp to valid range
    r = max(0, min(255, r))
    g = max(0, min(255, g))
    b = max(0, min(255, b))

    return rgb_to_hex(r, g, b)


def darken_color(hex_color: str, amount: float = 0.2) -> str:
    """Darken a color by mixing it with black.

    Args:
        hex_color: Hex color string to darken
        amount: Amount to darken (0-1, where 0 is no change, 1 is black)

    Returns:
        Darkened hex color string

    Raises:
        ValueError: If amount is not in range [0, 1]

    Examples:
        >>> darken_color("#9BB9A8", amount=0.2)
        '#7C947F'
        >>> darken_color("#000000", amount=0.5)  # Black stays black
        '#000000'
    """
    if not 0.0 <= amount <= 1.0:
        raise ValueError(f"Amount must be between 0 and 1, got {amount}")

    r, g, b = hex_to_rgb(hex_color)

    # Mix with black (0, 0, 0)
    r = int(r * (1 - amount))
    g = int(g * (1 - amount))
    b = int(b * (1 - amount))

    # Clamp to valid range
    r = max(0, min(255, r))
    g = max(0, min(255, g))
    b = max(0, min(255, b))

    return rgb_to_hex(r, g, b)


def get_contrasting_text_color(hex_color: str,
                               dark_color: str = "#000000",
                               light_color: str = "#FFFFFF",
                               threshold: float = 127.5) -> str:
    """Get contrasting text color (black or white) for a background color.

    Args:
        hex_color: Background hex color
        dark_color: Dark text color (default black)
        light_color: Light text color (default white)
        threshold: Brightness threshold (0-255, default 127.5)

    Returns:
        Contrasting text color (dark_color or light_color)

    Examples:
        >>> get_contrasting_text_color("#18453B")  # MSU Green
        '#FFFFFF'
        >>> get_contrasting_text_color("#FFFFFF")  # White
        '#000000'
    """
    brightness = get_color_brightness(hex_color)
    return light_color if brightness < threshold else dark_color


__all__ = [
    "validate_hex_color",
    "normalize_hex",
    "hex_to_rgb",
    "rgb_to_hex",
    "hex_to_rgba",
    "rgb_to_rgba",
    "get_color_brightness",
    "lighten_color",
    "darken_color",
    "get_contrasting_text_color",
]
