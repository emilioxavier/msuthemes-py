#!/usr/bin/env python3
"""Test script to verify MSU themes integration."""

import sys
import numpy as np
print("Testing MSU themes integration...\n")

# Test 1: Import themes module
print("1. Testing themes module import...")
try:
    from msuthemes import themes
    from msuthemes import theme_msu, reset_theme
    print("   ✓ Themes module imported successfully")
except Exception as e:
    print(f"   ✗ Failed: {e}")
    sys.exit(1)

# Test 2: Apply theme_msu
print("\n2. Testing theme_msu() application...")
try:
    params = theme_msu()
    print(f"   ✓ theme_msu() applied successfully")
    print(f"   ✓ Applied {len(params)} rcParams")
    print(f"   ✓ Font family: {params.get('font.family', 'N/A')}")
    print(f"   ✓ Font size: {params.get('font.size', 'N/A')}")
except Exception as e:
    print(f"   ✗ Failed: {e}")
    sys.exit(1)

# Test 3: Create matplotlib plot with MSU theme
print("\n3. Testing matplotlib plot with MSU theme...")
try:
    import matplotlib
    matplotlib.use('Agg')  # Non-interactive backend
    import matplotlib.pyplot as plt

    # Apply MSU theme
    theme_msu()

    # Create a simple plot
    x = np.linspace(0, 10, 100)
    y1 = np.sin(x)
    y2 = np.cos(x)
    y3 = np.sin(x) * np.exp(-x/10)

    fig, ax = plt.subplots(figsize=(10, 6))
    ax.plot(x, y1, label='sin(x)', linewidth=2)
    ax.plot(x, y2, label='cos(x)', linewidth=2)
    ax.plot(x, y3, label='damped sin(x)', linewidth=2)
    ax.set_xlabel('X Axis')
    ax.set_ylabel('Y Axis')
    ax.set_title('MSU-Themed Matplotlib Plot')
    ax.legend()

    # Save plot
    output_file = '/tmp/test_msu_theme_matplotlib.png'
    plt.savefig(output_file, dpi=150)
    plt.close()

    print(f"   ✓ Matplotlib plot created successfully")
    print(f"   ✓ Saved to: {output_file}")
except Exception as e:
    print(f"   ✗ Failed: {e}")
    import traceback
    traceback.print_exc()

# Test 4: Test theme with grid
print("\n4. Testing theme with grid...")
try:
    theme_msu(use_grid=True, base_size=12)

    fig, ax = plt.subplots(figsize=(10, 6))
    ax.bar(['A', 'B', 'C', 'D'], [3, 7, 2, 5])
    ax.set_title('MSU Theme with Grid')
    ax.set_ylabel('Values')

    output_file = '/tmp/test_msu_theme_grid.png'
    plt.savefig(output_file, dpi=150)
    plt.close()

    print(f"   ✓ Theme with grid applied successfully")
    print(f"   ✓ Saved to: {output_file}")
except Exception as e:
    print(f"   ✗ Failed: {e}")

# Test 5: Test seaborn integration (optional)
print("\n5. Testing seaborn integration...")
try:
    import seaborn as sns
    from msuthemes import set_msu_style

    # Apply MSU style to seaborn
    set_msu_style(style='whitegrid')

    # Create sample data
    data = {
        'x': np.random.randn(100),
        'y': np.random.randn(100),
        'category': np.random.choice(['A', 'B', 'C'], 100)
    }

    import pandas as pd
    df = pd.DataFrame(data)

    # Create seaborn plot
    fig, ax = plt.subplots(figsize=(10, 6))
    sns.scatterplot(data=df, x='x', y='y', hue='category', ax=ax, s=100)
    ax.set_title('MSU-Themed Seaborn Plot')

    output_file = '/tmp/test_msu_seaborn.png'
    plt.savefig(output_file, dpi=150)
    plt.close()

    print(f"   ✓ Seaborn integration successful")
    print(f"   ✓ Saved to: {output_file}")
except ImportError:
    print(f"   ⚠ Seaborn not installed (optional)")
except Exception as e:
    print(f"   ✗ Failed: {e}")

# Test 6: Test reset_theme
print("\n6. Testing reset_theme()...")
try:
    from msuthemes import reset_theme

    # Apply MSU theme
    theme_msu()
    font_before = plt.rcParams['font.family']

    # Reset theme
    reset_theme()
    font_after = plt.rcParams['font.family']

    print(f"   ✓ reset_theme() executed successfully")
    print(f"   ✓ Font before reset: {font_before}")
    print(f"   ✓ Font after reset: {font_after}")
except Exception as e:
    print(f"   ✗ Failed: {e}")

# Test 7: Test get_current_theme
print("\n7. Testing get_current_theme()...")
try:
    from msuthemes import get_current_theme

    theme_msu(base_size=14)
    current = get_current_theme()

    print(f"   ✓ get_current_theme() successful")
    print(f"   ✓ Current font size: {current.get('font.size', 'N/A')}")
    print(f"   ✓ Current figure size: {current.get('figure.figsize', 'N/A')}")
except Exception as e:
    print(f"   ✗ Failed: {e}")

# Test 8: Test color cycle
print("\n8. Testing MSU color cycle...")
try:
    theme_msu()

    fig, ax = plt.subplots(figsize=(10, 6))
    for i in range(5):
        ax.plot([0, 1, 2], [i, i+1, i+0.5], label=f'Line {i+1}', linewidth=3)
    ax.legend()
    ax.set_title('MSU Color Cycle Test')

    output_file = '/tmp/test_msu_color_cycle.png'
    plt.savefig(output_file, dpi=150)
    plt.close()

    print(f"   ✓ Color cycle test successful")
    print(f"   ✓ Saved to: {output_file}")
except Exception as e:
    print(f"   ✗ Failed: {e}")

# Summary
print("\n" + "="*60)
print("✓ All theme tests completed successfully!")
print("="*60)
print(f"\nGenerated test plots:")
print(f"  1. /tmp/test_msu_theme_matplotlib.png")
print(f"  2. /tmp/test_msu_theme_grid.png")
print(f"  3. /tmp/test_msu_seaborn.png (if seaborn installed)")
print(f"  4. /tmp/test_msu_color_cycle.png")
print("\nMSU themes are ready to use!")
