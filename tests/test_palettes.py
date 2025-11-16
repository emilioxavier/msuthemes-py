"""Tests for msuthemes.palettes module."""

import pytest
import numpy as np
from matplotlib.colors import LinearSegmentedColormap, ListedColormap
from msuthemes import palettes
from msuthemes.palettes import MSUPalette, get_palette, list_palettes


class TestMSUPaletteClass:
    """Test MSUPalette class functionality."""

    @pytest.mark.unit
    def test_palette_creation(self):
        """Test creating a basic palette."""
        colors_list = ['#18453B', '#FFFFFF', '#FF6F00']
        palette = MSUPalette(colors_list, palette_type='div', name='test')

        assert palette.name == 'test'
        assert palette.palette_type == 'div'
        assert len(palette.colors) == 3

    @pytest.mark.unit
    def test_as_hex(self):
        """Test as_hex() method."""
        palette = palettes.msu_seq
        hex_colors = palette.as_hex(n_colors=5)

        assert isinstance(hex_colors, list)
        assert len(hex_colors) == 5
        assert all(isinstance(c, str) for c in hex_colors)
        assert all(c.startswith('#') for c in hex_colors)

    @pytest.mark.unit
    def test_as_hex_reverse(self):
        """Test as_hex() with reverse=True."""
        palette = palettes.msu_seq
        normal = palette.as_hex(n_colors=5)
        reversed_colors = palette.as_hex(n_colors=5, reverse=True)

        assert len(normal) == len(reversed_colors)
        assert normal == list(reversed(reversed_colors))

    @pytest.mark.unit
    def test_as_rgb(self):
        """Test as_rgb() method."""
        palette = palettes.msu_seq
        rgb_colors = palette.as_rgb(n_colors=3)

        assert isinstance(rgb_colors, list)
        assert len(rgb_colors) == 3
        assert all(isinstance(c, tuple) for c in rgb_colors)
        assert all(len(c) == 3 for c in rgb_colors)
        assert all(all(0 <= val <= 255 for val in c) for c in rgb_colors)

    @pytest.mark.unit
    @pytest.mark.mpl
    def test_as_matplotlib_cmap(self):
        """Test as_matplotlib_cmap() method."""
        palette = palettes.msu_seq
        cmap = palette.as_matplotlib_cmap()

        assert isinstance(cmap, (LinearSegmentedColormap, ListedColormap))
        assert cmap.N > 0

    @pytest.mark.unit
    @pytest.mark.mpl
    def test_as_matplotlib_cmap_with_name(self):
        """Test as_matplotlib_cmap() with custom name."""
        palette = palettes.msu_seq
        cmap = palette.as_matplotlib_cmap(name='custom_cmap')

        assert cmap.name == 'custom_cmap'

    @pytest.mark.unit
    def test_default_n_colors(self):
        """Test that default n_colors returns all colors."""
        palette = palettes.msu_qual1
        default_colors = palette.as_hex()

        # Should return all colors in palette
        assert isinstance(default_colors, list)
        assert len(default_colors) > 0


class TestPredefinedPalettes:
    """Test predefined palettes."""

    @pytest.mark.unit
    def test_sequential_palettes_exist(self):
        """Test that sequential palettes exist."""
        assert hasattr(palettes, 'msu_seq')
        assert hasattr(palettes, 'msu_seq2')
        assert isinstance(palettes.msu_seq, MSUPalette)

    @pytest.mark.unit
    def test_diverging_palettes_exist(self):
        """Test that diverging palettes exist."""
        assert hasattr(palettes, 'msu_div')
        assert hasattr(palettes, 'msu_div2')
        assert isinstance(palettes.msu_div, MSUPalette)

    @pytest.mark.unit
    def test_qualitative_palettes_exist(self):
        """Test that qualitative palettes exist."""
        assert hasattr(palettes, 'msu_qual1')
        assert hasattr(palettes, 'msu_qual2')
        assert isinstance(palettes.msu_qual1, MSUPalette)

    @pytest.mark.unit
    def test_bigten_palettes_exist(self):
        """Test that Big Ten palettes exist."""
        assert hasattr(palettes, 'bigten_primary')
        assert hasattr(palettes, 'bigten_secondary')

    @pytest.mark.unit
    def test_palette_types(self):
        """Test that palettes have correct types."""
        assert palettes.msu_seq.palette_type in ['seq', 'sequential']
        assert palettes.msu_div.palette_type in ['div', 'diverging']
        assert palettes.msu_qual1.palette_type in ['qual', 'qualitative']

    @pytest.mark.unit
    def test_sequential_palette_colors(self):
        """Test sequential palette generates colors correctly."""
        colors = palettes.msu_seq.as_hex(n_colors=7)
        assert len(colors) == 7
        # Sequential should be ordered from light to dark or vice versa
        assert all(c.startswith('#') for c in colors)

    @pytest.mark.unit
    def test_diverging_palette_colors(self):
        """Test diverging palette generates colors correctly."""
        colors = palettes.msu_div.as_hex(n_colors=7)
        assert len(colors) == 7
        # Diverging should have a midpoint
        assert colors[len(colors)//2] != colors[0]

    @pytest.mark.unit
    def test_qualitative_palette_colors(self):
        """Test qualitative palette has distinct colors."""
        colors = palettes.msu_qual1.as_hex()
        # Qualitative should have distinct colors
        assert len(colors) == len(set(colors))  # All unique


class TestPaletteFunctions:
    """Test palette utility functions."""

    @pytest.mark.unit
    def test_list_palettes(self):
        """Test list_palettes() function."""
        palette_list = list_palettes()

        assert isinstance(palette_list, list)
        assert len(palette_list) > 0
        assert all(isinstance(name, str) for name in palette_list)

    @pytest.mark.unit
    def test_list_palettes_contains_expected(self):
        """Test that list_palettes contains expected palettes."""
        palette_list = list_palettes()

        expected = ['msu_seq', 'msu_div', 'msu_qual1']
        for name in expected:
            assert name in palette_list

    @pytest.mark.unit
    def test_get_palette_by_name(self):
        """Test get_palette() function."""
        palette = get_palette('msu_seq')

        assert isinstance(palette, MSUPalette)
        assert palette.name == 'msu_seq'

    @pytest.mark.unit
    def test_get_palette_invalid_name(self):
        """Test get_palette() with invalid name."""
        with pytest.raises(ValueError):
            get_palette('invalid_palette_name')

    @pytest.mark.unit
    def test_get_palette_case_sensitive(self):
        """Test that get_palette is case-sensitive."""
        # Should work
        palette = get_palette('msu_seq')
        assert isinstance(palette, MSUPalette)

        # Should fail (wrong case)
        with pytest.raises(ValueError):
            get_palette('MSU_SEQ')


class TestPaletteInterpolation:
    """Test color interpolation in palettes."""

    @pytest.mark.unit
    def test_interpolation_increases_colors(self):
        """Test that interpolation can increase number of colors."""
        # Original palette has fewer colors
        palette = palettes.msu_seq
        original_count = len(palette.colors)

        # Request more colors
        interpolated = palette.as_hex(n_colors=original_count * 2)

        assert len(interpolated) == original_count * 2

    @pytest.mark.unit
    def test_interpolation_decreases_colors(self):
        """Test that requesting fewer colors works."""
        palette = palettes.msu_qual1
        original_count = len(palette.colors)

        # Request fewer colors
        subset = palette.as_hex(n_colors=3)

        assert len(subset) == 3

    @pytest.mark.unit
    def test_interpolated_colors_are_valid_hex(self):
        """Test that interpolated colors are valid hex."""
        palette = palettes.msu_seq
        colors = palette.as_hex(n_colors=20)

        for color in colors:
            assert color.startswith('#')
            assert len(color) == 7
            assert all(c in '0123456789ABCDEFabcdef' for c in color[1:])


class TestMSUPalettesDict:
    """Test MSU_PALETTES dictionary."""

    @pytest.mark.unit
    def test_msu_palettes_dict_exists(self):
        """Test that MSU_PALETTES dictionary exists."""
        assert hasattr(palettes, 'MSU_PALETTES')
        assert isinstance(palettes.MSU_PALETTES, dict)

    @pytest.mark.unit
    def test_msu_palettes_dict_has_palettes(self):
        """Test that MSU_PALETTES contains palette objects."""
        assert len(palettes.MSU_PALETTES) > 0

        for name, palette in palettes.MSU_PALETTES.items():
            assert isinstance(name, str)
            assert isinstance(palette, MSUPalette)

    @pytest.mark.unit
    def test_msu_palettes_dict_keys_match(self):
        """Test that MSU_PALETTES keys match list_palettes."""
        dict_keys = set(palettes.MSU_PALETTES.keys())
        list_names = set(list_palettes())

        assert dict_keys == list_names


class TestPaletteModule:
    """Test palettes module structure."""

    @pytest.mark.unit
    def test_module_exports(self):
        """Test that palettes module exports expected items."""
        expected_exports = [
            'MSUPalette',
            'msu_seq', 'msu_div', 'msu_qual1',
            'get_palette', 'list_palettes',
            'MSU_PALETTES'
        ]

        for export in expected_exports:
            assert hasattr(palettes, export)

    @pytest.mark.unit
    def test_module_docstring(self):
        """Test that palettes module has docstring."""
        assert palettes.__doc__ is not None
        assert len(palettes.__doc__) > 0


class TestPaletteEdgeCases:
    """Test edge cases and error handling."""

    @pytest.mark.unit
    def test_empty_colors_list(self):
        """Test creating palette with empty colors list."""
        with pytest.raises((ValueError, AssertionError)):
            MSUPalette([], palette_type='seq', name='empty')

    @pytest.mark.unit
    def test_single_color_palette(self):
        """Test palette with single color."""
        palette = MSUPalette(['#18453B'], palette_type='seq', name='single')

        colors = palette.as_hex(n_colors=1)
        assert len(colors) == 1
        assert colors[0] == '#18453B'

    @pytest.mark.unit
    def test_request_zero_colors(self):
        """Test requesting zero colors."""
        palette = palettes.msu_seq

        with pytest.raises((ValueError, AssertionError)):
            palette.as_hex(n_colors=0)

    @pytest.mark.unit
    def test_request_negative_colors(self):
        """Test requesting negative number of colors."""
        palette = palettes.msu_seq

        with pytest.raises((ValueError, AssertionError)):
            palette.as_hex(n_colors=-5)
