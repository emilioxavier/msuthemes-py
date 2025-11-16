"""Tests for msuthemes.utils module."""

import pytest
from msuthemes import utils


class TestHexToRGB:
    """Test hex_to_rgb() function."""

    @pytest.mark.unit
    def test_basic_conversion(self):
        """Test basic hex to RGB conversion."""
        rgb = utils.hex_to_rgb('#18453B')
        assert rgb == (24, 69, 59)

    @pytest.mark.unit
    def test_white_conversion(self):
        """Test converting white."""
        rgb = utils.hex_to_rgb('#FFFFFF')
        assert rgb == (255, 255, 255)

    @pytest.mark.unit
    def test_black_conversion(self):
        """Test converting black."""
        rgb = utils.hex_to_rgb('#000000')
        assert rgb == (0, 0, 0)

    @pytest.mark.unit
    def test_lowercase_hex(self):
        """Test with lowercase hex values."""
        rgb = utils.hex_to_rgb('#ff6f00')
        assert rgb == (255, 111, 0)

    @pytest.mark.unit
    def test_mixed_case_hex(self):
        """Test with mixed case hex values."""
        rgb = utils.hex_to_rgb('#Ff6F00')
        assert rgb == (255, 111, 0)

    @pytest.mark.unit
    def test_invalid_hex_format(self):
        """Test with invalid hex format."""
        with pytest.raises((ValueError, AssertionError)):
            utils.hex_to_rgb('18453B')  # Missing #

    @pytest.mark.unit
    def test_invalid_hex_length(self):
        """Test with invalid hex length."""
        with pytest.raises((ValueError, AssertionError)):
            utils.hex_to_rgb('#184')  # Too short

    @pytest.mark.unit
    def test_invalid_hex_characters(self):
        """Test with invalid hex characters."""
        with pytest.raises((ValueError, AssertionError)):
            utils.hex_to_rgb('#GGGGGG')  # Invalid characters


class TestRGBToHex:
    """Test rgb_to_hex() function."""

    @pytest.mark.unit
    def test_basic_conversion(self):
        """Test basic RGB to hex conversion."""
        hex_color = utils.rgb_to_hex(24, 69, 59)
        assert hex_color.upper() == '#18453B'

    @pytest.mark.unit
    def test_white_conversion(self):
        """Test converting white."""
        hex_color = utils.rgb_to_hex(255, 255, 255)
        assert hex_color.upper() == '#FFFFFF'

    @pytest.mark.unit
    def test_black_conversion(self):
        """Test converting black."""
        hex_color = utils.rgb_to_hex(0, 0, 0)
        assert hex_color.upper() == '#000000'

    @pytest.mark.unit
    def test_returns_uppercase(self):
        """Test that result is uppercase."""
        hex_color = utils.rgb_to_hex(255, 111, 0)
        assert hex_color == hex_color.upper()

    @pytest.mark.unit
    def test_invalid_rgb_high(self):
        """Test with RGB values above 255."""
        with pytest.raises((ValueError, AssertionError)):
            utils.rgb_to_hex(256, 0, 0)

    @pytest.mark.unit
    def test_invalid_rgb_negative(self):
        """Test with negative RGB values."""
        with pytest.raises((ValueError, AssertionError)):
            utils.rgb_to_hex(-1, 0, 0)


class TestRoundTripConversion:
    """Test round-trip hex <-> RGB conversions."""

    @pytest.mark.unit
    def test_hex_to_rgb_to_hex(self):
        """Test converting hex -> RGB -> hex."""
        original = '#18453B'
        rgb = utils.hex_to_rgb(original)
        hex_color = utils.rgb_to_hex(*rgb)
        assert hex_color.upper() == original.upper()

    @pytest.mark.unit
    def test_rgb_to_hex_to_rgb(self):
        """Test converting RGB -> hex -> RGB."""
        original = (24, 69, 59)
        hex_color = utils.rgb_to_hex(*original)
        rgb = utils.hex_to_rgb(hex_color)
        assert rgb == original

    @pytest.mark.unit
    def test_multiple_colors_round_trip(self):
        """Test round trip with multiple colors."""
        test_colors = [
            '#18453B',  # MSU Green
            '#FFFFFF',  # White
            '#000000',  # Black
            '#FF6F00',  # Orange
            '#008183',  # Teal
        ]

        for original in test_colors:
            rgb = utils.hex_to_rgb(original)
            hex_color = utils.rgb_to_hex(*rgb)
            assert hex_color.upper() == original.upper()


class TestValidateHexColor:
    """Test validate_hex_color() function."""

    @pytest.mark.unit
    def test_valid_hex_color(self):
        """Test with valid hex color."""
        assert utils.validate_hex_color('#18453B') is True

    @pytest.mark.unit
    def test_valid_lowercase_hex(self):
        """Test with valid lowercase hex."""
        assert utils.validate_hex_color('#ff6f00') is True

    @pytest.mark.unit
    def test_invalid_no_hash(self):
        """Test with missing hash symbol."""
        assert utils.validate_hex_color('18453B') is False

    @pytest.mark.unit
    def test_invalid_too_short(self):
        """Test with too short hex."""
        assert utils.validate_hex_color('#184') is False

    @pytest.mark.unit
    def test_invalid_too_long(self):
        """Test with too long hex."""
        assert utils.validate_hex_color('#18453B00') is False

    @pytest.mark.unit
    def test_invalid_characters(self):
        """Test with invalid characters."""
        assert utils.validate_hex_color('#GGGGGG') is False

    @pytest.mark.unit
    def test_empty_string(self):
        """Test with empty string."""
        assert utils.validate_hex_color('') is False


class TestGetColorBrightness:
    """Test get_color_brightness() function."""

    @pytest.mark.unit
    def test_white_brightness(self):
        """Test brightness of white."""
        brightness = utils.get_color_brightness('#FFFFFF')
        assert brightness == pytest.approx(255.0, abs=1.0)

    @pytest.mark.unit
    def test_black_brightness(self):
        """Test brightness of black."""
        brightness = utils.get_color_brightness('#000000')
        assert brightness == pytest.approx(0.0, abs=1.0)

    @pytest.mark.unit
    def test_msu_green_brightness(self):
        """Test brightness of MSU Green."""
        brightness = utils.get_color_brightness('#18453B')
        # Should be relatively dark
        assert 0 < brightness < 128

    @pytest.mark.unit
    def test_brightness_range(self):
        """Test that brightness is in valid range."""
        test_colors = ['#18453B', '#FFFFFF', '#000000', '#FF6F00']

        for color in test_colors:
            brightness = utils.get_color_brightness(color)
            assert 0 <= brightness <= 255

    @pytest.mark.unit
    def test_brightness_ordering(self):
        """Test that lighter colors have higher brightness."""
        dark = utils.get_color_brightness('#000000')
        medium = utils.get_color_brightness('#808080')
        light = utils.get_color_brightness('#FFFFFF')

        assert dark < medium < light


class TestLightenColor:
    """Test lighten_color() function."""

    @pytest.mark.unit
    def test_lighten_by_20_percent(self):
        """Test lightening a color by 20%."""
        original = '#18453B'
        lightened = utils.lighten_color(original, amount=0.2)

        # Lightened color should be valid hex
        assert utils.validate_hex_color(lightened)

        # Lightened color should be brighter
        original_brightness = utils.get_color_brightness(original)
        lightened_brightness = utils.get_color_brightness(lightened)
        assert lightened_brightness > original_brightness

    @pytest.mark.unit
    def test_lighten_white_stays_white(self):
        """Test that lightening white doesn't change it."""
        lightened = utils.lighten_color('#FFFFFF', amount=0.2)
        assert lightened.upper() == '#FFFFFF'

    @pytest.mark.unit
    def test_lighten_amount_zero(self):
        """Test lightening by 0% returns same color."""
        original = '#18453B'
        lightened = utils.lighten_color(original, amount=0.0)
        assert lightened.upper() == original.upper()

    @pytest.mark.unit
    def test_lighten_amount_one(self):
        """Test lightening by 100% approaches white."""
        lightened = utils.lighten_color('#18453B', amount=1.0)
        # Should be very light (close to white)
        brightness = utils.get_color_brightness(lightened)
        assert brightness > 200


class TestDarkenColor:
    """Test darken_color() function."""

    @pytest.mark.unit
    def test_darken_by_20_percent(self):
        """Test darkening a color by 20%."""
        original = '#9BB9A8'  # Light MSU Green
        darkened = utils.darken_color(original, amount=0.2)

        # Darkened color should be valid hex
        assert utils.validate_hex_color(darkened)

        # Darkened color should be darker
        original_brightness = utils.get_color_brightness(original)
        darkened_brightness = utils.get_color_brightness(darkened)
        assert darkened_brightness < original_brightness

    @pytest.mark.unit
    def test_darken_black_stays_black(self):
        """Test that darkening black doesn't change it."""
        darkened = utils.darken_color('#000000', amount=0.2)
        assert darkened.upper() == '#000000'

    @pytest.mark.unit
    def test_darken_amount_zero(self):
        """Test darkening by 0% returns same color."""
        original = '#9BB9A8'
        darkened = utils.darken_color(original, amount=0.0)
        assert darkened.upper() == original.upper()

    @pytest.mark.unit
    def test_darken_amount_one(self):
        """Test darkening by 100% approaches black."""
        darkened = utils.darken_color('#9BB9A8', amount=1.0)
        # Should be very dark (close to black)
        brightness = utils.get_color_brightness(darkened)
        assert brightness < 50


class TestUtilsModule:
    """Test utils module structure."""

    @pytest.mark.unit
    def test_module_exports(self):
        """Test that utils module exports expected functions."""
        expected_functions = [
            'hex_to_rgb',
            'rgb_to_hex',
            'validate_hex_color',
            'get_color_brightness',
            'lighten_color',
            'darken_color',
        ]

        for func_name in expected_functions:
            assert hasattr(utils, func_name)
            assert callable(getattr(utils, func_name))

    @pytest.mark.unit
    def test_module_docstring(self):
        """Test that utils module has docstring."""
        assert utils.__doc__ is not None
        assert len(utils.__doc__) > 0


class TestColorManipulation:
    """Test color manipulation edge cases."""

    @pytest.mark.unit
    def test_lighten_then_darken(self):
        """Test lightening then darkening a color."""
        original = '#18453B'
        lightened = utils.lighten_color(original, amount=0.3)
        back = utils.darken_color(lightened, amount=0.3)

        # Should be close to original (may not be exact due to rounding)
        orig_brightness = utils.get_color_brightness(original)
        back_brightness = utils.get_color_brightness(back)
        assert abs(orig_brightness - back_brightness) < 20  # Within 20 units

    @pytest.mark.unit
    def test_gradual_lightening(self):
        """Test creating a gradient by lightening."""
        base_color = '#18453B'
        gradient = [
            base_color,
            utils.lighten_color(base_color, 0.2),
            utils.lighten_color(base_color, 0.4),
            utils.lighten_color(base_color, 0.6),
        ]

        # Each color should be brighter than the previous
        brightnesses = [utils.get_color_brightness(c) for c in gradient]
        for i in range(len(brightnesses) - 1):
            assert brightnesses[i] < brightnesses[i + 1]

    @pytest.mark.unit
    def test_gradual_darkening(self):
        """Test creating a gradient by darkening."""
        base_color = '#9BB9A8'
        gradient = [
            base_color,
            utils.darken_color(base_color, 0.2),
            utils.darken_color(base_color, 0.4),
            utils.darken_color(base_color, 0.6),
        ]

        # Each color should be darker than the previous
        brightnesses = [utils.get_color_brightness(c) for c in gradient]
        for i in range(len(brightnesses) - 1):
            assert brightnesses[i] > brightnesses[i + 1]
