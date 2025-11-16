"""MSU themes for matplotlib and seaborn.

This module provides theme functions to apply MSU branding to plots.

Functions:
    theme_msu: Apply MSU theme to matplotlib
    set_msu_style: Apply MSU style to seaborn
    reset_theme: Reset to matplotlib defaults

Examples:
    >>> from msuthemes import theme_msu
    >>> import matplotlib.pyplot as plt
    >>>
    >>> # Apply MSU theme
    >>> theme_msu()
    >>>
    >>> # Create plot
    >>> plt.plot([1, 2, 3], [1, 4, 2])
    >>> plt.title('MSU-Branded Plot')
    >>> plt.show()
"""

from typing import Optional, Dict, Any
import matplotlib as mpl
import matplotlib.pyplot as plt
from matplotlib import cycler
import warnings

from msuthemes.colors import MSU_GREEN, MSU_ORANGE, MSU_TEAL, MSU_PURPLE, MSU_GREY
from msuthemes.fonts import register_metropolis_fonts, is_metropolis_available


def _get_msu_color_cycle() -> list:
    """Get the default MSU color cycle for plots.

    Returns:
        List of hex colors for the color cycle
    """
    return [
        MSU_GREEN,      # MSU Green
        MSU_ORANGE,     # MSU Orange
        MSU_TEAL,       # MSU Teal
        MSU_PURPLE,     # MSU Purple/Eggplant
        MSU_GREY,       # MSU Grey
        "#0DB14B",      # Kelly Green
        "#CB5A28",      # Sienna/Red
        "#909AB7",      # Blue-Grey
        "#D1DE3F",      # Yellow-Green
        "#94AE4A",      # Split Pea
    ]


def theme_msu(
    base_size: float = 11,
    base_family: str = "Metropolis",
    use_grid: bool = False,
    grid_color: str = "#E5E5E5",
    grid_linewidth: float = 0.8,
    spine_color: str = "#000000",
    spine_linewidth: float = 1.0,
    color_cycle: Optional[list] = None,
    register_fonts: bool = True,
) -> Dict[str, Any]:
    """Apply MSU theme to matplotlib plots.

    This function sets matplotlib rcParams to use MSU branding including:
    - Metropolis font (automatically registered)
    - MSU color palette
    - Clean, professional styling
    - Optional grid lines

    Args:
        base_size: Base font size for all text elements (default: 11)
        base_family: Font family to use (default: "Metropolis")
        use_grid: Whether to show grid lines (default: False)
        grid_color: Color of grid lines (default: "#E5E5E5")
        grid_linewidth: Width of grid lines (default: 0.8)
        spine_color: Color of axis spines (default: "#000000")
        spine_linewidth: Width of axis spines (default: 1.0)
        color_cycle: Custom color cycle (default: MSU colors)
        register_fonts: Whether to register Metropolis fonts (default: True)

    Returns:
        Dictionary of applied rcParams

    Examples:
        >>> from msuthemes import theme_msu
        >>> import matplotlib.pyplot as plt
        >>>
        >>> # Apply MSU theme
        >>> theme_msu()
        >>>
        >>> # Create plot with MSU styling
        >>> plt.plot([1, 2, 3], [1, 4, 2])
        >>> plt.title('MSU Plot')
        >>> plt.show()

        >>> # Apply theme with grid
        >>> theme_msu(use_grid=True)

        >>> # Apply theme with larger font
        >>> theme_msu(base_size=14)
    """
    # Register Metropolis fonts if requested
    if register_fonts:
        try:
            register_metropolis_fonts(verbose=False)
        except Exception as e:
            warnings.warn(
                f"Could not register Metropolis fonts: {e}. Using default font.",
                RuntimeWarning
            )

    # Check if Metropolis is available, fallback to sans-serif if not
    if not is_metropolis_available() and base_family == "Metropolis":
        warnings.warn(
            "Metropolis font not available. Using 'sans-serif' instead. "
            "Try clearing matplotlib cache or restarting Python.",
            RuntimeWarning
        )
        base_family = "sans-serif"

    # Get color cycle
    if color_cycle is None:
        color_cycle = _get_msu_color_cycle()

    # Calculate relative sizes
    small_size = base_size * 0.85
    medium_size = base_size
    large_size = base_size * 1.15

    # Define MSU rcParams
    msu_params = {
        # Figure
        'figure.facecolor': 'white',
        'figure.edgecolor': 'white',
        'figure.figsize': (8, 6),
        'figure.dpi': 100,

        # Font
        'font.family': base_family,
        'font.size': base_size,
        'font.weight': 'normal',

        # Text sizes
        'axes.titlesize': large_size,
        'axes.labelsize': medium_size,
        'xtick.labelsize': small_size,
        'ytick.labelsize': small_size,
        'legend.fontsize': small_size,
        'figure.titlesize': large_size,

        # Axes
        'axes.facecolor': 'white',
        'axes.edgecolor': spine_color,
        'axes.linewidth': spine_linewidth,
        'axes.labelcolor': 'black',
        'axes.axisbelow': True,  # Grid lines below plot elements
        'axes.prop_cycle': cycler('color', color_cycle),
        'axes.spines.top': False,
        'axes.spines.right': False,
        'axes.spines.left': True,
        'axes.spines.bottom': True,

        # Grid
        'axes.grid': use_grid,
        'axes.grid.axis': 'both',
        'grid.color': grid_color,
        'grid.linestyle': '-',
        'grid.linewidth': grid_linewidth,
        'grid.alpha': 0.5,

        # Ticks
        'xtick.color': 'black',
        'ytick.color': 'black',
        'xtick.direction': 'out',
        'ytick.direction': 'out',
        'xtick.major.size': 5,
        'ytick.major.size': 5,
        'xtick.minor.size': 3,
        'ytick.minor.size': 3,
        'xtick.major.width': spine_linewidth,
        'ytick.major.width': spine_linewidth,

        # Legend
        'legend.frameon': True,
        'legend.framealpha': 0.8,
        'legend.facecolor': 'white',
        'legend.edgecolor': '#CCCCCC',
        'legend.fancybox': False,
        'legend.shadow': False,

        # Lines
        'lines.linewidth': 2.0,
        'lines.markersize': 6,
        'lines.markeredgewidth': 0,

        # Patches
        'patch.linewidth': 0.5,
        'patch.edgecolor': 'black',

        # Savefig
        'savefig.dpi': 300,
        'savefig.facecolor': 'white',
        'savefig.edgecolor': 'white',
        'savefig.bbox': 'tight',
    }

    # Apply the theme
    mpl.rcParams.update(msu_params)

    return msu_params


def set_msu_style(
    style: str = "white",
    context: str = "notebook",
    palette: Optional[list] = None,
    font: str = "Metropolis",
    font_scale: float = 1.0,
    register_fonts: bool = True,
) -> None:
    """Set MSU styling for seaborn plots.

    This function configures seaborn with MSU branding including colors,
    fonts, and styling preferences.

    Args:
        style: Seaborn style ('white', 'whitegrid', 'dark', 'darkgrid', 'ticks')
               Default: 'white'
        context: Seaborn context ('paper', 'notebook', 'talk', 'poster')
                Default: 'notebook'
        palette: Custom color palette (default: MSU colors)
        font: Font family (default: 'Metropolis')
        font_scale: Scale factor for fonts (default: 1.0)
        register_fonts: Whether to register Metropolis fonts (default: True)

    Examples:
        >>> from msuthemes import set_msu_style
        >>> import seaborn as sns
        >>> import matplotlib.pyplot as plt
        >>>
        >>> # Apply MSU style to seaborn
        >>> set_msu_style()
        >>>
        >>> # Create seaborn plot
        >>> tips = sns.load_dataset('tips')
        >>> sns.scatterplot(data=tips, x='total_bill', y='tip')
        >>> plt.show()

        >>> # Use with whitegrid style
        >>> set_msu_style(style='whitegrid')

        >>> # Use for presentation
        >>> set_msu_style(context='talk', font_scale=1.2)
    """
    try:
        import seaborn as sns
    except ImportError:
        raise ImportError(
            "seaborn is required for set_msu_style(). "
            "Install it with: pip install seaborn"
        )

    # Register fonts if requested
    if register_fonts:
        try:
            register_metropolis_fonts(verbose=False)
        except Exception as e:
            warnings.warn(
                f"Could not register Metropolis fonts: {e}",
                RuntimeWarning
            )

    # Check font availability
    if not is_metropolis_available() and font == "Metropolis":
        warnings.warn(
            "Metropolis font not available. Using default seaborn font.",
            RuntimeWarning
        )
        font = "sans-serif"

    # Get color palette
    if palette is None:
        palette = _get_msu_color_cycle()

    # Set seaborn style and context
    sns.set_style(style)
    sns.set_context(context, font_scale=font_scale)

    # Set color palette
    sns.set_palette(palette)

    # Set font
    mpl.rcParams['font.family'] = font

    # Additional MSU-specific styling
    mpl.rcParams.update({
        'axes.prop_cycle': cycler('color', palette),
        'axes.spines.top': False,
        'axes.spines.right': False,
    })


def reset_theme() -> None:
    """Reset matplotlib to default settings.

    This function restores matplotlib's default rcParams, removing
    any MSU theme customizations.

    Examples:
        >>> from msuthemes import theme_msu, reset_theme
        >>>
        >>> # Apply MSU theme
        >>> theme_msu()
        >>>
        >>> # ... create plots ...
        >>>
        >>> # Reset to defaults
        >>> reset_theme()
    """
    mpl.rcParams.update(mpl.rcParamsDefault)


def get_current_theme() -> Dict[str, Any]:
    """Get current matplotlib rcParams.

    Returns:
        Dictionary of current rcParams

    Examples:
        >>> from msuthemes import theme_msu, get_current_theme
        >>>
        >>> theme_msu()
        >>> params = get_current_theme()
        >>> print(params['font.family'])
        'Metropolis'
    """
    return dict(mpl.rcParams)


__all__ = [
    "theme_msu",
    "set_msu_style",
    "reset_theme",
    "get_current_theme",
]
