#!/usr/bin/env python3
"""Quick test script to verify basic package functionality."""

print("Testing MSUthemes package imports and basic functionality...")

# Test 1: Import package
print("\n1. Testing package import...")
try:
    import msuthemes
    print(f"   ✓ Package version: {msuthemes.__version__}")
except Exception as e:
    print(f"   ✗ Failed: {e}")
    exit(1)

# Test 2: Import colors
print("\n2. Testing color imports...")
try:
    from msuthemes import MSU_GREEN, MSU_ORANGE, BIGTEN_COLORS_PRIMARY
    print(f"   ✓ MSU_GREEN: {MSU_GREEN}")
    print(f"   ✓ MSU_ORANGE: {MSU_ORANGE}")
    print(f"   ✓ Big Ten schools: {len(BIGTEN_COLORS_PRIMARY)} institutions")
except Exception as e:
    print(f"   ✗ Failed: {e}")
    exit(1)

# Test 3: Import palettes
print("\n3. Testing palette imports...")
try:
    from msuthemes import msu_seq, msu_div, list_palettes
    print(f"   ✓ msu_seq: {msu_seq}")
    print(f"   ✓ Available palettes: {len(list_palettes())}")
except Exception as e:
    print(f"   ✗ Failed: {e}")
    exit(1)

# Test 4: Test palette functionality
print("\n4. Testing palette functionality...")
try:
    colors_5 = msu_seq.as_hex(n_colors=5)
    print(f"   ✓ Generated 5 colors from msu_seq: {len(colors_5)} colors")
    print(f"      Colors: {colors_5}")
except Exception as e:
    print(f"   ✗ Failed: {e}")
    exit(1)

# Test 5: Test utils
print("\n5. Testing utility functions...")
try:
    from msuthemes.utils import hex_to_rgb, validate_hex_color
    rgb = hex_to_rgb(MSU_GREEN)
    print(f"   ✓ MSU_GREEN RGB: {rgb}")
    print(f"   ✓ Validation: {validate_hex_color('#18453B')}")
except Exception as e:
    print(f"   ✗ Failed: {e}")
    exit(1)

# Test 6: Test matplotlib colormap generation
print("\n6. Testing matplotlib colormap...")
try:
    cmap = msu_seq.as_matplotlib_cmap()
    print(f"   ✓ Created colormap: {cmap.name}")
except Exception as e:
    print(f"   ✗ Failed: {e}")
    exit(1)

print("\n" + "="*60)
print("✓ All tests passed successfully!")
print("="*60)
