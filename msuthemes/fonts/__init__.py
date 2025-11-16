"""Font utilities for MSUthemes.

This module provides utilities for managing and registering the Metropolis font
with matplotlib for use in MSU-branded visualizations.

The Metropolis font (version 5.1.0) is bundled with this package and is
released into the public domain under the Unlicense.

Functions:
    register_metropolis_fonts: Register Metropolis fonts with matplotlib
    get_font_path: Get path to font files directory
    list_available_fonts: List all available Metropolis fonts
    is_metropolis_available: Check if Metropolis font is available

Examples:
    >>> from msuthemes.fonts import register_metropolis_fonts
    >>> import matplotlib.pyplot as plt
    >>>
    >>> # Register fonts with matplotlib
    >>> register_metropolis_fonts()
    >>>
    >>> # Use Metropolis in plots
    >>> plt.rcParams['font.family'] = 'Metropolis'
"""

import os
from pathlib import Path
from typing import List, Optional
import warnings


def get_font_path() -> Path:
    """Get the path to the Metropolis font directory.

    Returns:
        Path object pointing to the fonts directory

    Examples:
        >>> font_path = get_font_path()
        >>> print(font_path)
        PosixPath('.../msuthemes/fonts/metropolis')
    """
    return Path(__file__).parent / "metropolis"


def list_available_fonts() -> List[str]:
    """List all available Metropolis font files.

    Returns:
        List of font filenames

    Examples:
        >>> fonts = list_available_fonts()
        >>> print(len(fonts))
        18
    """
    font_dir = get_font_path()
    if not font_dir.exists():
        return []

    return sorted([
        f.name for f in font_dir.glob("*.ttf")
    ])


def register_metropolis_fonts(verbose: bool = False) -> bool:
    """Register Metropolis fonts with matplotlib.

    This function finds all Metropolis .ttf files and registers them with
    matplotlib's font manager. After calling this function, you can use
    'Metropolis' as a font family in matplotlib plots.

    Args:
        verbose: If True, print registration messages

    Returns:
        True if fonts were registered successfully, False otherwise

    Examples:
        >>> from msuthemes.fonts import register_metropolis_fonts
        >>> import matplotlib.pyplot as plt
        >>>
        >>> register_metropolis_fonts()
        >>> plt.rcParams['font.family'] = 'Metropolis'
        >>> plt.title('MSU Branded Plot', fontfamily='Metropolis')
    """
    try:
        import matplotlib.font_manager as fm
    except ImportError:
        warnings.warn(
            "matplotlib is not installed. Cannot register fonts.",
            ImportWarning
        )
        return False

    font_dir = get_font_path()

    if not font_dir.exists():
        warnings.warn(
            f"Font directory not found: {font_dir}",
            RuntimeWarning
        )
        return False

    # Find all .ttf files
    font_files = list(font_dir.glob("*.ttf"))

    if not font_files:
        warnings.warn(
            f"No .ttf font files found in {font_dir}",
            RuntimeWarning
        )
        return False

    # Register each font
    registered_count = 0
    for font_file in font_files:
        try:
            fm.fontManager.addfont(str(font_file))
            registered_count += 1
            if verbose:
                print(f"Registered: {font_file.name}")
        except Exception as e:
            if verbose:
                print(f"Failed to register {font_file.name}: {e}")

    if verbose:
        print(f"\nSuccessfully registered {registered_count}/{len(font_files)} Metropolis fonts")

    # Rebuild font cache
    try:
        fm.fontManager._rebuild()
    except AttributeError:
        # Newer versions of matplotlib may not have _rebuild()
        pass

    return registered_count > 0


def is_metropolis_available() -> bool:
    """Check if Metropolis font is available in matplotlib.

    Returns:
        True if Metropolis font is available, False otherwise

    Examples:
        >>> if is_metropolis_available():
        ...     plt.rcParams['font.family'] = 'Metropolis'
        ... else:
        ...     print("Metropolis font not available")
    """
    try:
        import matplotlib.font_manager as fm

        # Get list of available font families
        available_fonts = {f.name for f in fm.fontManager.ttflist}

        return 'Metropolis' in available_fonts
    except ImportError:
        return False


def get_metropolis_font_weights() -> dict:
    """Get mapping of font weight names to font files.

    Returns:
        Dictionary mapping weight names to font filenames

    Examples:
        >>> weights = get_metropolis_font_weights()
        >>> print(weights['regular'])
        'metropolis-latin-400-normal.ttf'
    """
    return {
        'thin': 'metropolis-latin-100-normal.ttf',
        'thin-italic': 'metropolis-latin-100-italic.ttf',
        'extra-light': 'metropolis-latin-200-normal.ttf',
        'extra-light-italic': 'metropolis-latin-200-italic.ttf',
        'light': 'metropolis-latin-300-normal.ttf',
        'light-italic': 'metropolis-latin-300-italic.ttf',
        'regular': 'metropolis-latin-400-normal.ttf',
        'italic': 'metropolis-latin-400-italic.ttf',
        'medium': 'metropolis-latin-500-normal.ttf',
        'medium-italic': 'metropolis-latin-500-italic.ttf',
        'semi-bold': 'metropolis-latin-600-normal.ttf',
        'semi-bold-italic': 'metropolis-latin-600-italic.ttf',
        'bold': 'metropolis-latin-700-normal.ttf',
        'bold-italic': 'metropolis-latin-700-italic.ttf',
        'extra-bold': 'metropolis-latin-800-normal.ttf',
        'extra-bold-italic': 'metropolis-latin-800-italic.ttf',
        'black': 'metropolis-latin-900-normal.ttf',
        'black-italic': 'metropolis-latin-900-italic.ttf',
    }


__all__ = [
    "get_font_path",
    "list_available_fonts",
    "register_metropolis_fonts",
    "is_metropolis_available",
    "get_metropolis_font_weights",
]
