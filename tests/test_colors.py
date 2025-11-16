"""Tests for msuthemes.colors module."""

import pytest
from msuthemes import colors


class TestMSUColors:
    """Test MSU color constants."""

    @pytest.mark.unit
    def test_msu_green(self):
        """Test MSU Green color value."""
        assert colors.MSU_GREEN == '#18453B'
        assert isinstance(colors.MSU_GREEN, str)
        assert colors.MSU_GREEN.startswith('#')
        assert len(colors.MSU_GREEN) == 7

    @pytest.mark.unit
    def test_msu_white(self):
        """Test MSU White color value."""
        assert colors.MSU_WHITE == '#FFFFFF'
        assert isinstance(colors.MSU_WHITE, str)

    @pytest.mark.unit
    def test_msu_black(self):
        """Test MSU Black color value."""
        assert colors.MSU_BLACK == '#000000'
        assert isinstance(colors.MSU_BLACK, str)

    @pytest.mark.unit
    def test_msu_accent_colors(self):
        """Test MSU accent colors."""
        assert colors.MSU_ORANGE == '#FF6F00'
        assert colors.MSU_TEAL == '#008183'
        assert colors.MSU_PURPLE == '#5B3256'
        assert colors.MSU_GREY == '#C3C4C6'

    @pytest.mark.unit
    def test_msu_green_variants(self):
        """Test MSU Green variants."""
        assert colors.MSU_GREEN_LIGHT == '#9BB9A8'
        assert colors.MSU_GREEN_DARK == '#0F2922'
        assert colors.MSU_GREEN_BRIGHT == '#3FA060'

    @pytest.mark.unit
    def test_all_colors_are_hex(self):
        """Test that all MSU colors are valid hex format."""
        msu_color_attrs = [
            'MSU_GREEN', 'MSU_WHITE', 'MSU_BLACK',
            'MSU_ORANGE', 'MSU_TEAL', 'MSU_PURPLE', 'MSU_GREY',
            'MSU_GREEN_LIGHT', 'MSU_GREEN_DARK', 'MSU_GREEN_BRIGHT'
        ]

        for attr in msu_color_attrs:
            color_value = getattr(colors, attr)
            assert isinstance(color_value, str)
            assert color_value.startswith('#')
            assert len(color_value) == 7
            # Check hex format
            assert all(c in '0123456789ABCDEF' for c in color_value[1:].upper())


class TestBigTenColors:
    """Test Big Ten color dictionaries."""

    @pytest.mark.unit
    def test_bigten_primary_colors_exists(self):
        """Test that BIGTEN_COLORS_PRIMARY exists."""
        assert hasattr(colors, 'BIGTEN_COLORS_PRIMARY')
        assert isinstance(colors.BIGTEN_COLORS_PRIMARY, dict)

    @pytest.mark.unit
    def test_bigten_secondary_colors_exists(self):
        """Test that BIGTEN_COLORS_SECONDARY exists."""
        assert hasattr(colors, 'BIGTEN_COLORS_SECONDARY')
        assert isinstance(colors.BIGTEN_COLORS_SECONDARY, dict)

    @pytest.mark.unit
    def test_bigten_primary_has_18_schools(self):
        """Test that primary colors has 18 institutions."""
        assert len(colors.BIGTEN_COLORS_PRIMARY) == 18

    @pytest.mark.unit
    def test_bigten_secondary_has_18_schools(self):
        """Test that secondary colors has 18 institutions."""
        assert len(colors.BIGTEN_COLORS_SECONDARY) == 18

    @pytest.mark.unit
    def test_bigten_msu_color(self):
        """Test MSU color in Big Ten."""
        assert 'MSU' in colors.BIGTEN_COLORS_PRIMARY
        assert colors.BIGTEN_COLORS_PRIMARY['MSU'] == '#18453B'

    @pytest.mark.unit
    def test_bigten_michigan_color(self):
        """Test Michigan color in Big Ten."""
        assert 'Michigan' in colors.BIGTEN_COLORS_PRIMARY
        assert colors.BIGTEN_COLORS_PRIMARY['Michigan'] == '#00274C'

    @pytest.mark.unit
    def test_bigten_ohio_state_color(self):
        """Test Ohio State color in Big Ten."""
        assert 'Ohio State' in colors.BIGTEN_COLORS_PRIMARY
        assert colors.BIGTEN_COLORS_PRIMARY['Ohio State'] == '#BB0000'

    @pytest.mark.unit
    def test_all_bigten_primary_colors_are_hex(self):
        """Test that all Big Ten primary colors are valid hex."""
        for school, color in colors.BIGTEN_COLORS_PRIMARY.items():
            assert isinstance(color, str), f"{school} color is not a string"
            assert color.startswith('#'), f"{school} color doesn't start with #"
            assert len(color) == 7, f"{school} color is not 7 characters"
            # Check hex format
            assert all(c in '0123456789ABCDEF' for c in color[1:].upper()), \
                f"{school} color is not valid hex"

    @pytest.mark.unit
    def test_all_bigten_secondary_colors_are_hex(self):
        """Test that all Big Ten secondary colors are valid hex."""
        for school, color in colors.BIGTEN_COLORS_SECONDARY.items():
            assert isinstance(color, str), f"{school} secondary color is not a string"
            assert color.startswith('#'), f"{school} secondary color doesn't start with #"
            assert len(color) == 7, f"{school} secondary color is not 7 characters"

    @pytest.mark.unit
    def test_bigten_institutions_match(self):
        """Test that primary and secondary have same institutions."""
        assert set(colors.BIGTEN_COLORS_PRIMARY.keys()) == set(colors.BIGTEN_COLORS_SECONDARY.keys())

    @pytest.mark.unit
    def test_all_expected_institutions_present(self, bigten_institutions):
        """Test that all expected Big Ten institutions are present."""
        expected = set(bigten_institutions)
        actual = set(colors.BIGTEN_COLORS_PRIMARY.keys())

        # Note: bigten_institutions has 'USoCal' but dict might have 'USC' or 'USoCal'
        # Adjust for this potential difference
        if 'USoCal' in expected and 'USC' in actual:
            expected.remove('USoCal')
            expected.add('USC')

        assert expected == actual, f"Missing: {expected - actual}, Extra: {actual - expected}"


class TestColorConstants:
    """Test color constant properties."""

    @pytest.mark.unit
    def test_msu_green_is_primary(self):
        """Test that MSU Green matches Big Ten primary."""
        assert colors.MSU_GREEN == colors.BIGTEN_COLORS_PRIMARY['MSU']

    @pytest.mark.unit
    def test_msu_white_is_secondary(self):
        """Test that MSU White matches Big Ten secondary."""
        assert colors.MSU_WHITE == colors.BIGTEN_COLORS_SECONDARY['MSU']

    @pytest.mark.unit
    def test_colors_are_immutable_strings(self):
        """Test that color values are strings (immutable)."""
        # Strings are immutable in Python
        assert isinstance(colors.MSU_GREEN, str)
        assert isinstance(colors.MSU_WHITE, str)
        assert isinstance(colors.MSU_ORANGE, str)

    @pytest.mark.unit
    def test_bigten_dicts_are_dicts(self):
        """Test that Big Ten color collections are dictionaries."""
        assert isinstance(colors.BIGTEN_COLORS_PRIMARY, dict)
        assert isinstance(colors.BIGTEN_COLORS_SECONDARY, dict)


class TestColorModule:
    """Test colors module structure."""

    @pytest.mark.unit
    def test_module_has_expected_attributes(self):
        """Test that colors module has expected attributes."""
        expected_attrs = [
            'MSU_GREEN', 'MSU_WHITE', 'MSU_BLACK',
            'MSU_ORANGE', 'MSU_TEAL', 'MSU_PURPLE', 'MSU_GREY',
            'MSU_GREEN_LIGHT', 'MSU_GREEN_DARK', 'MSU_GREEN_BRIGHT',
            'BIGTEN_COLORS_PRIMARY', 'BIGTEN_COLORS_SECONDARY'
        ]

        for attr in expected_attrs:
            assert hasattr(colors, attr), f"Missing attribute: {attr}"

    @pytest.mark.unit
    def test_module_docstring_exists(self):
        """Test that colors module has a docstring."""
        assert colors.__doc__ is not None
        assert len(colors.__doc__) > 0
