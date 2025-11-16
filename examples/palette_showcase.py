"""Showcase of all MSUthemes color palettes.

This script demonstrates all available color palettes and how to use them.
"""

import matplotlib.pyplot as plt
import numpy as np
from msuthemes import theme_msu, palettes, list_palettes

# Apply MSU theme
theme_msu()

# Get all palette names
palette_names = list_palettes()

# Create figure
fig = plt.figure(figsize=(14, 12))

# Show each palette
for i, name in enumerate(palette_names):
    palette = palettes.MSU_PALETTES[name]

    # Get colors (interpolate to 10 colors for display)
    try:
        colors = palette.as_hex(n_colors=10)
    except:
        colors = palette.as_hex()
        # Pad to 10 if fewer
        while len(colors) < 10:
            colors.append(colors[-1])

    # Create subplot
    ax = plt.subplot(len(palette_names), 1, i + 1)

    # Display palette as color bars
    for j, color in enumerate(colors[:10]):
        ax.add_patch(plt.Rectangle((j, 0), 1, 1, facecolor=color))

    # Format
    ax.set_xlim(0, 10)
    ax.set_ylim(0, 1)
    ax.set_yticks([])
    ax.set_xticks([])

    # Add palette name and type
    palette_type = palette.palette_type
    ax.text(-0.5, 0.5, f"{name}\n({palette_type})",
            va='center', ha='right', fontsize=10)

    # Remove spines
    for spine in ax.spines.values():
        spine.set_visible(False)

# Overall title
fig.suptitle('MSUthemes Color Palettes', fontsize=16, fontweight='bold')

plt.tight_layout()
plt.savefig('examples/output/palette_showcase.png', dpi=300, bbox_inches='tight')
print("✓ Saved: examples/output/palette_showcase.png")
plt.show()

# Create a second figure showing palette applications
print("\nCreating palette application examples...")

fig, axes = plt.subplots(2, 3, figsize=(15, 10))
axes = axes.flatten()

# Example 1: Sequential palette - heatmap
ax = axes[0]
data = np.random.rand(10, 10)
cmap = palettes.msu_seq.as_matplotlib_cmap()
im = ax.imshow(data, cmap=cmap)
ax.set_title('Sequential Palette\n(Heatmap)')
plt.colorbar(im, ax=ax)

# Example 2: Diverging palette - signed data
ax = axes[1]
data = np.random.randn(10, 10)
cmap = palettes.msu_div.as_matplotlib_cmap()
im = ax.imshow(data, cmap=cmap, vmin=-2, vmax=2)
ax.set_title('Diverging Palette\n(Signed Data)')
plt.colorbar(im, ax=ax)

# Example 3: Qualitative palette - categories
ax = axes[2]
categories = ['A', 'B', 'C', 'D', 'E']
values = [23, 45, 56, 32, 78]
colors = palettes.msu_qual1.as_hex()
ax.bar(categories, values, color=colors)
ax.set_title('Qualitative Palette\n(Categories)')
ax.set_ylabel('Value')

# Example 4: Sequential - line plot
ax = axes[3]
x = np.linspace(0, 10, 100)
colors = palettes.msu_seq.as_hex(n_colors=5)
for i, color in enumerate(colors):
    y = np.sin(x - i*0.5)
    ax.plot(x, y, color=color, linewidth=2, label=f'Series {i+1}')
ax.set_title('Sequential Palette\n(Line Plot)')
ax.legend()

# Example 5: Big Ten palette
ax = axes[4]
from msuthemes import bigten_palette
schools = ['MSU', 'Michigan', 'Ohio State', 'Penn State']
values = [45, 38, 52, 41]
colors = bigten_palette(schools)
ax.bar(schools, values, color=colors)
ax.set_title('Big Ten Palette\n(Institutional Colors)')
ax.set_ylabel('Value')
plt.setp(ax.xaxis.get_majorticklabels(), rotation=45, ha='right')

# Example 6: Custom gradient
ax = axes[5]
from msuthemes import colors as msu_colors
from msuthemes.palettes import MSUPalette

custom = MSUPalette(
    [msu_colors.MSU_GREEN, msu_colors.MSU_WHITE, msu_colors.MSU_ORANGE],
    palette_type='div',
    name='custom'
)
data = np.random.randn(10, 10)
cmap = custom.as_matplotlib_cmap()
im = ax.imshow(data, cmap=cmap)
ax.set_title('Custom Palette\n(Green-White-Orange)')
plt.colorbar(im, ax=ax)

fig.suptitle('Palette Application Examples', fontsize=16, fontweight='bold')

plt.tight_layout()
plt.savefig('examples/output/palette_applications.png', dpi=300, bbox_inches='tight')
print("✓ Saved: examples/output/palette_applications.png")
plt.show()

print("\n✓ All palette examples created successfully!")
