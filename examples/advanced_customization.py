"""Advanced customization examples for MSUthemes.

This script demonstrates advanced theme customization, custom palettes,
and complex multi-panel figures.
"""

import matplotlib.pyplot as plt
import numpy as np
from msuthemes import (
    theme_msu,
    colors,
    palettes,
    load_bigten_data,
    get_bigten_colors
)
from msuthemes.palettes import MSUPalette
from msuthemes.utils import lighten_color, darken_color

print("Advanced Customization Examples")
print("="*60)

# Example 1: Custom theme parameters
print("\n1. Custom theme with specific styling...")
theme_msu(
    base_size=12,
    base_family='Metropolis',
    use_grid=True,
    grid_color='#E5E5E5',
    grid_linewidth=0.5,
    spine_linewidth=1.5,
    color_cycle=[colors.MSU_GREEN, colors.MSU_ORANGE, colors.MSU_TEAL,
                 colors.MSU_PURPLE, colors.MSU_GREY]
)

fig, axes = plt.subplots(2, 2, figsize=(14, 10))

# Plot 1: Custom color cycle demonstration
ax = axes[0, 0]
x = np.linspace(0, 10, 100)
for i in range(5):
    y = np.sin(x - i*0.5) + i
    ax.plot(x, y, linewidth=2, label=f'Series {i+1}')
ax.set_title('A) Custom Color Cycle')
ax.set_xlabel('X')
ax.set_ylabel('Y')
ax.legend()

# Plot 2: Monochromatic palette (shades of MSU Green)
ax = axes[0, 1]
base_color = colors.MSU_GREEN
mono_palette = [
    darken_color(base_color, 0.4),
    darken_color(base_color, 0.2),
    base_color,
    lighten_color(base_color, 0.2),
    lighten_color(base_color, 0.4),
]

categories = ['A', 'B', 'C', 'D', 'E']
values = [23, 45, 56, 32, 78]
ax.bar(categories, values, color=mono_palette)
ax.set_title('B) Monochromatic Palette\n(MSU Green Shades)')
ax.set_ylabel('Value')

# Plot 3: Custom diverging palette
ax = axes[1, 0]
custom_div = MSUPalette(
    [colors.MSU_TEAL, colors.MSU_WHITE, colors.MSU_PURPLE],
    palette_type='div',
    name='teal_purple_div'
)
data = np.random.randn(12, 12)
cmap = custom_div.as_matplotlib_cmap()
im = ax.imshow(data, cmap=cmap, vmin=-2, vmax=2)
ax.set_title('C) Custom Diverging Palette\n(Teal-White-Purple)')
plt.colorbar(im, ax=ax)

# Plot 4: Accent color highlighting
ax = axes[1, 1]
data = np.random.randn(20)
colors_highlight = [colors.MSU_ORANGE if x > 1 else colors.MSU_GREY for x in data]
ax.bar(range(len(data)), data, color=colors_highlight, alpha=0.7, edgecolor='black')
ax.axhline(y=1, color=colors.MSU_GREEN, linewidth=2, linestyle='--', label='Threshold')
ax.set_title('D) Accent Color Highlighting')
ax.set_xlabel('Index')
ax.set_ylabel('Value')
ax.legend()

fig.suptitle('Advanced Customization: Theme & Palettes',
             fontsize=16, fontweight='bold')

plt.tight_layout()
plt.savefig('examples/output/advanced_customization.png', dpi=300, bbox_inches='tight')
print("✓ Saved: examples/output/advanced_customization.png")
plt.show()

# Example 2: Complex multi-panel figure with mixed plot types
print("\n2. Creating complex multi-panel publication figure...")

fig = plt.figure(figsize=(16, 12))
gs = fig.add_gridspec(3, 3, hspace=0.3, wspace=0.3)

# Large subplot spanning 2x2
ax_main = fig.add_subplot(gs[0:2, 0:2])

# Load data for main plot
schools = ['MSU', 'Michigan', 'Ohio State', 'Penn State', 'Wisconsin']
data = load_bigten_data(
    institutions=schools,
    years=list(range(2000, 2024)),
    columns=['name', 'entry_term', 'UGDS']
).dropna()

school_colors = get_bigten_colors(schools)
for school in schools:
    school_data = data[data['name'] == school]
    ax_main.plot(
        school_data['entry_term'],
        school_data['UGDS'],
        label=school,
        color=school_colors[school],
        linewidth=3,
        marker='o',
        markersize=5
    )

ax_main.set_xlabel('Year', fontsize=14)
ax_main.set_ylabel('Undergraduate Enrollment', fontsize=14)
ax_main.set_title('Big Ten Enrollment Trends (2000-2023)', fontsize=16, fontweight='bold')
ax_main.legend(loc='best', fontsize=11)
ax_main.grid(True, alpha=0.3)

# Small subplot 1: Pie chart
ax1 = fig.add_subplot(gs[0, 2])
latest_data = data[data['entry_term'] == 2023]
sizes = latest_data['UGDS'].values
labels = latest_data['name'].values
colors_pie = [school_colors[name] for name in labels]

ax1.pie(sizes, labels=labels, colors=colors_pie, autopct='%1.1f%%',
        startangle=90, textprops={'fontsize': 8})
ax1.set_title('2023 Distribution', fontsize=10)

# Small subplot 2: Bar chart showing growth
ax2 = fig.add_subplot(gs[1, 2])
growth = []
for school in schools:
    school_data = data[data['name'] == school].sort_values('entry_term')
    if len(school_data) >= 2:
        initial = school_data.iloc[0]['UGDS']
        final = school_data.iloc[-1]['UGDS']
        pct_change = ((final - initial) / initial) * 100
        growth.append(pct_change)
    else:
        growth.append(0)

colors_growth = [school_colors[s] for s in schools]
ax2.barh(schools, growth, color=colors_growth)
ax2.set_xlabel('% Change', fontsize=9)
ax2.set_title('Enrollment Growth\n(2000-2023)', fontsize=10)
ax2.tick_params(axis='both', labelsize=8)
ax2.grid(True, alpha=0.3, axis='x')

# Bottom row: Three small plots
ax3 = fig.add_subplot(gs[2, 0])
# Histogram
all_enrollments = data['UGDS'].values
ax3.hist(all_enrollments, bins=20, color=colors.MSU_GREEN, alpha=0.7, edgecolor='black')
ax3.set_xlabel('Enrollment', fontsize=9)
ax3.set_ylabel('Frequency', fontsize=9)
ax3.set_title('Enrollment Distribution', fontsize=10)
ax3.tick_params(axis='both', labelsize=8)

ax4 = fig.add_subplot(gs[2, 1])
# Box plot
box_data = [data[data['name'] == s]['UGDS'].values for s in schools[:3]]
bp = ax4.boxplot(box_data, labels=schools[:3], patch_artist=True)
for patch, school in zip(bp['boxes'], schools[:3]):
    patch.set_facecolor(school_colors[school])
    patch.set_alpha(0.7)
ax4.set_ylabel('Enrollment', fontsize=9)
ax4.set_title('Enrollment Variability', fontsize=10)
ax4.tick_params(axis='both', labelsize=8)
plt.setp(ax4.xaxis.get_majorticklabels(), rotation=45, ha='right')

ax5 = fig.add_subplot(gs[2, 2])
# Scatter plot
recent = data[data['entry_term'] >= 2020]
for school in schools[:3]:
    school_data = recent[recent['name'] == school]
    ax5.scatter(
        school_data['entry_term'],
        school_data['UGDS'],
        color=school_colors[school],
        s=100,
        alpha=0.7,
        label=school,
        edgecolors='black',
        linewidth=1
    )
ax5.set_xlabel('Year', fontsize=9)
ax5.set_ylabel('Enrollment', fontsize=9)
ax5.set_title('Recent Trends (2020+)', fontsize=10)
ax5.legend(fontsize=7)
ax5.tick_params(axis='both', labelsize=8)
ax5.grid(True, alpha=0.3)

fig.suptitle('Multi-Panel Publication Figure: Big Ten Enrollment Analysis',
             fontsize=18, fontweight='bold', y=0.995)

plt.savefig('examples/output/complex_multipanel.png', dpi=300, bbox_inches='tight')
print("✓ Saved: examples/output/complex_multipanel.png")
plt.show()

# Example 3: Custom gradient and colormap
print("\n3. Creating custom color gradients...")

fig, axes = plt.subplots(2, 3, figsize=(15, 10))

# Create various custom gradients
custom_palettes = [
    {
        'name': 'Green→Orange',
        'colors': [colors.MSU_GREEN, colors.MSU_ORANGE],
        'type': 'seq'
    },
    {
        'name': 'Green→White→Teal',
        'colors': [colors.MSU_GREEN, colors.MSU_WHITE, colors.MSU_TEAL],
        'type': 'div'
    },
    {
        'name': 'Dark→Light Green',
        'colors': [colors.MSU_GREEN_DARK, colors.MSU_GREEN, colors.MSU_GREEN_LIGHT],
        'type': 'seq'
    },
    {
        'name': 'Full Spectrum',
        'colors': [colors.MSU_GREEN, colors.MSU_TEAL, colors.MSU_PURPLE, colors.MSU_ORANGE],
        'type': 'qual'
    },
    {
        'name': 'Purple→White→Orange',
        'colors': [colors.MSU_PURPLE, colors.MSU_WHITE, colors.MSU_ORANGE],
        'type': 'div'
    },
    {
        'name': 'Monochrome Green',
        'colors': [lighten_color(colors.MSU_GREEN, 0.6), colors.MSU_GREEN,
                   darken_color(colors.MSU_GREEN, 0.4)],
        'type': 'seq'
    }
]

for idx, (ax, palette_def) in enumerate(zip(axes.flatten(), custom_palettes)):
    custom_pal = MSUPalette(
        palette_def['colors'],
        palette_type=palette_def['type'],
        name=palette_def['name']
    )

    # Generate test data
    data = np.random.rand(20, 20)
    if palette_def['type'] == 'div':
        data = np.random.randn(20, 20)
        vmin, vmax = -2, 2
        center = 0
    else:
        vmin, vmax = 0, 1
        center = None

    cmap = custom_pal.as_matplotlib_cmap()
    im = ax.imshow(data, cmap=cmap, vmin=vmin, vmax=vmax)
    ax.set_title(palette_def['name'])
    ax.set_xticks([])
    ax.set_yticks([])
    plt.colorbar(im, ax=ax, fraction=0.046)

fig.suptitle('Custom Color Gradients & Colormaps',
             fontsize=16, fontweight='bold')

plt.tight_layout()
plt.savefig('examples/output/custom_gradients.png', dpi=300, bbox_inches='tight')
print("✓ Saved: examples/output/custom_gradients.png")
plt.show()

print("\n" + "="*60)
print("✓ All advanced customization examples created successfully!")
print("="*60)
