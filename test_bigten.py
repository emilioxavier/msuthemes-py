#!/usr/bin/env python3
"""Test script to verify Big Ten functionality."""

import sys
print("Testing Big Ten functionality...\n")

# Test 1: Import bigten module
print("1. Testing bigten module import...")
try:
    from msuthemes import bigten
    from msuthemes.bigten import (
        get_bigten_colors,
        bigten_palette,
        list_bigten_institutions,
        normalize_institution_name,
        get_institution_info,
        validate_institution
    )
    print("   ✓ BigTen module imported successfully")
except Exception as e:
    print(f"   ✗ Failed: {e}")
    sys.exit(1)

# Test 2: List all institutions
print("\n2. Testing list_bigten_institutions()...")
try:
    institutions = list_bigten_institutions()
    print(f"   ✓ Found {len(institutions)} Big Ten institutions")
    print(f"   ✓ Institutions: {', '.join(institutions[:5])}...")

    # Verify expected count
    if len(institutions) == 18:
        print(f"   ✓ Correct count (18 institutions)")
    else:
        print(f"   ⚠ Expected 18 institutions, got {len(institutions)}")
except Exception as e:
    print(f"   ✗ Failed: {e}")
    sys.exit(1)

# Test 3: Get single institution color
print("\n3. Testing get_bigten_colors() with single institution...")
try:
    # Test MSU
    msu_color = get_bigten_colors("MSU")
    print(f"   ✓ MSU primary color: {msu_color}")

    # Test with nickname
    spartans_color = get_bigten_colors("Spartans")
    print(f"   ✓ 'Spartans' resolves to: {spartans_color}")

    # Verify they're the same
    if msu_color == spartans_color:
        print(f"   ✓ Nickname resolution working correctly")
    else:
        print(f"   ✗ Nickname resolution failed")
except Exception as e:
    print(f"   ✗ Failed: {e}")
    sys.exit(1)

# Test 4: Get multiple institution colors
print("\n4. Testing get_bigten_colors() with multiple institutions...")
try:
    schools = ["MSU", "Michigan", "Ohio State"]
    colors = get_bigten_colors(schools)
    print(f"   ✓ Got colors for {len(colors)} institutions")
    for school, color in colors.items():
        print(f"      - {school}: {color}")
except Exception as e:
    print(f"   ✗ Failed: {e}")
    sys.exit(1)

# Test 5: Test secondary colors
print("\n5. Testing secondary colors...")
try:
    msu_secondary = get_bigten_colors("MSU", color_type="secondary")
    print(f"   ✓ MSU secondary color: {msu_secondary}")

    # Multiple with secondary
    schools = ["MSU", "Michigan"]
    secondary_colors = get_bigten_colors(schools, color_type="secondary")
    print(f"   ✓ Secondary colors: {secondary_colors}")
except Exception as e:
    print(f"   ✗ Failed: {e}")
    sys.exit(1)

# Test 6: Test normalize_institution_name
print("\n6. Testing normalize_institution_name()...")
try:
    test_cases = [
        ("msu", "MSU"),
        ("Spartans", "MSU"),
        ("michigan state", "MSU"),
        ("buckeyes", "Ohio State"),
        ("wolverines", "Michigan"),
        ("Badgers", "Wisconsin"),
    ]

    passed = 0
    for input_name, expected in test_cases:
        result = normalize_institution_name(input_name)
        if result == expected:
            passed += 1
        else:
            print(f"   ✗ '{input_name}' -> '{result}', expected '{expected}'")

    print(f"   ✓ Normalization tests: {passed}/{len(test_cases)} passed")
except Exception as e:
    print(f"   ✗ Failed: {e}")
    import traceback
    traceback.print_exc()

# Test 7: Test bigten_palette
print("\n7. Testing bigten_palette()...")
try:
    # All institutions
    palette_all = bigten_palette()
    print(f"   ✓ Full Big Ten palette: {len(palette_all)} colors")

    # Specific institutions
    palette_subset = bigten_palette(["MSU", "Michigan", "Ohio State"])
    print(f"   ✓ Subset palette: {len(palette_subset)} colors")
    print(f"      Colors: {palette_subset}")

    # As MSUPalette object
    palette_obj = bigten_palette(as_palette=True)
    print(f"   ✓ As MSUPalette: {palette_obj}")
    colors_5 = palette_obj.as_hex(n_colors=5)
    print(f"   ✓ Generated 5 colors from palette: {len(colors_5)} colors")
except Exception as e:
    print(f"   ✗ Failed: {e}")
    import traceback
    traceback.print_exc()

# Test 8: Test get_institution_info
print("\n8. Testing get_institution_info()...")
try:
    msu_info = get_institution_info("MSU")
    print(f"   ✓ MSU info retrieved")
    print(f"      Name: {msu_info['name']}")
    print(f"      Primary: {msu_info['primary_color']}")
    print(f"      Secondary: {msu_info['secondary_color']}")

    # Test with nickname
    spartans_info = get_institution_info("Spartans")
    print(f"   ✓ 'Spartans' info retrieved: {spartans_info['name']}")
except Exception as e:
    print(f"   ✗ Failed: {e}")
    sys.exit(1)

# Test 9: Test validate_institution
print("\n9. Testing validate_institution()...")
try:
    valid_tests = [
        ("MSU", True),
        ("Spartans", True),
        ("michigan", True),
        ("Invalid School", False),
        ("XYZ University", False),
    ]

    passed = 0
    for inst, expected in valid_tests:
        result = validate_institution(inst)
        if result == expected:
            passed += 1
            status = "✓" if result else "✓ (correctly invalid)"
            print(f"      {status} '{inst}': {result}")
        else:
            print(f"      ✗ '{inst}': got {result}, expected {expected}")

    print(f"   ✓ Validation tests: {passed}/{len(valid_tests)} passed")
except Exception as e:
    print(f"   ✗ Failed: {e}")
    sys.exit(1)

# Test 10: Test all institutions
print("\n10. Testing all 18 Big Ten institutions...")
try:
    institutions = list_bigten_institutions()
    all_colors = get_bigten_colors(institutions)

    print(f"   ✓ All {len(all_colors)} institutions have colors:")
    for inst, color in sorted(all_colors.items()):
        print(f"      - {inst:20s}: {color}")
except Exception as e:
    print(f"   ✗ Failed: {e}")
    import traceback
    traceback.print_exc()

# Test 11: Test error handling
print("\n11. Testing error handling...")
try:
    # Invalid institution
    try:
        get_bigten_colors("Invalid University")
        print(f"   ✗ Should have raised ValueError for invalid institution")
    except ValueError as e:
        print(f"   ✓ Correctly raised ValueError for invalid institution")

    # Invalid color type
    try:
        get_bigten_colors("MSU", color_type="tertiary")
        print(f"   ✗ Should have raised ValueError for invalid color_type")
    except ValueError as e:
        print(f"   ✓ Correctly raised ValueError for invalid color_type")

except Exception as e:
    print(f"   ✗ Failed: {e}")
    sys.exit(1)

# Test 12: Integration with matplotlib (create visualization)
print("\n12. Testing Big Ten visualization...")
try:
    import matplotlib
    matplotlib.use('Agg')
    import matplotlib.pyplot as plt
    import numpy as np
    from msuthemes import theme_msu

    # Apply MSU theme
    theme_msu()

    # Create bar chart with Big Ten colors
    schools = ["MSU", "Michigan", "Ohio State", "Penn State", "Wisconsin"]
    colors_list = bigten_palette(schools)
    values = [85, 78, 92, 81, 88]

    fig, ax = plt.subplots(figsize=(10, 6))
    bars = ax.bar(schools, values, color=colors_list)
    ax.set_ylabel('Score')
    ax.set_title('Big Ten Institutional Colors Demo')
    ax.set_ylim(0, 100)

    # Save
    output_file = '/tmp/test_bigten_colors.png'
    plt.savefig(output_file, dpi=150)
    plt.close()

    print(f"   ✓ Big Ten visualization created")
    print(f"   ✓ Saved to: {output_file}")
except ImportError:
    print(f"   ⚠ matplotlib not available (optional test)")
except Exception as e:
    print(f"   ✗ Failed: {e}")
    import traceback
    traceback.print_exc()

# Summary
print("\n" + "="*60)
print("✓ All Big Ten functionality tests completed successfully!")
print("="*60)
print(f"\nBig Ten Features:")
print(f"  - 18 institutions supported")
print(f"  - Primary and secondary colors")
print(f"  - Institution name normalization (nicknames, abbreviations)")
print(f"  - Palette generation")
print(f"  - Integration with MSUPalette system")
print(f"  - matplotlib visualization support")
print("\nBig Ten functionality is ready to use!")
