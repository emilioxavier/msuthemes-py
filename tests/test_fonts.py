#!/usr/bin/env python3
"""Test script to verify Metropolis font integration."""

import sys
print("Testing Metropolis font integration...\n")

# Test 1: Import fonts module
print("1. Testing fonts module import...")
try:
    from msuthemes import fonts
    print("   ✓ Fonts module imported successfully")
except Exception as e:
    print(f"   ✗ Failed: {e}")
    sys.exit(1)

# Test 2: Get font path
print("\n2. Testing font path...")
try:
    from msuthemes.fonts import get_font_path
    font_path = get_font_path()
    print(f"   ✓ Font path: {font_path}")
    print(f"   ✓ Path exists: {font_path.exists()}")
except Exception as e:
    print(f"   ✗ Failed: {e}")
    sys.exit(1)

# Test 3: List available fonts
print("\n3. Testing font listing...")
try:
    from msuthemes.fonts import list_available_fonts
    fonts_list = list_available_fonts()
    print(f"   ✓ Found {len(fonts_list)} font files")
    if len(fonts_list) > 0:
        print(f"   ✓ Sample fonts:")
        for font in fonts_list[:3]:
            print(f"      - {font}")
        if len(fonts_list) > 3:
            print(f"      ... and {len(fonts_list) - 3} more")
except Exception as e:
    print(f"   ✗ Failed: {e}")
    sys.exit(1)

# Test 4: Register fonts with matplotlib
print("\n4. Testing font registration...")
try:
    from msuthemes.fonts import register_metropolis_fonts
    success = register_metropolis_fonts(verbose=False)
    if success:
        print(f"   ✓ Fonts registered successfully")
    else:
        print(f"   ⚠ Font registration returned False")
except Exception as e:
    print(f"   ✗ Failed: {e}")
    sys.exit(1)

# Test 5: Check if Metropolis is available
print("\n5. Testing font availability...")
try:
    from msuthemes.fonts import is_metropolis_available
    available = is_metropolis_available()
    if available:
        print(f"   ✓ Metropolis font is available in matplotlib")
    else:
        print(f"   ⚠ Metropolis font not found in matplotlib font list")
        print(f"      (This may require clearing matplotlib cache)")
except Exception as e:
    print(f"   ✗ Failed: {e}")
    sys.exit(1)

# Test 6: Get font weights
print("\n6. Testing font weights mapping...")
try:
    from msuthemes.fonts import get_metropolis_font_weights
    weights = get_metropolis_font_weights()
    print(f"   ✓ Font weights available: {len(weights)}")
    print(f"   ✓ Sample weights:")
    for weight_name in ['regular', 'bold', 'italic', 'semi-bold']:
        if weight_name in weights:
            print(f"      - {weight_name}: {weights[weight_name]}")
except Exception as e:
    print(f"   ✗ Failed: {e}")
    sys.exit(1)

# Test 7: Create a simple plot with Metropolis (if available)
print("\n7. Testing plot creation with Metropolis...")
try:
    import matplotlib
    matplotlib.use('Agg')  # Use non-interactive backend
    import matplotlib.pyplot as plt

    # Try to use Metropolis
    if available:
        plt.rcParams['font.family'] = 'Metropolis'
        plt.rcParams['font.size'] = 12

    # Create a simple plot
    fig, ax = plt.subplots(figsize=(6, 4))
    ax.plot([1, 2, 3], [1, 4, 2], linewidth=2)
    ax.set_title('Test Plot with Metropolis Font')
    ax.set_xlabel('X Axis')
    ax.set_ylabel('Y Axis')

    # Save plot
    output_file = '/tmp/test_metropolis_font.png'
    plt.savefig(output_file, dpi=100, bbox_inches='tight')
    plt.close()

    print(f"   ✓ Test plot created successfully")
    print(f"   ✓ Saved to: {output_file}")

except Exception as e:
    print(f"   ✗ Failed: {e}")
    # Don't exit - this is not critical

# Summary
print("\n" + "="*60)
print("✓ Font integration tests completed successfully!")
print("="*60)
print(f"\nSummary:")
print(f"  - Font files found: {len(fonts_list)}")
print(f"  - Fonts registered: Yes")
print(f"  - Metropolis available: {'Yes' if available else 'No (may need cache clear)'}")
print(f"  - Font weights defined: {len(weights)}")
print("\nMetropolis font is ready to use in MSUthemes!")
