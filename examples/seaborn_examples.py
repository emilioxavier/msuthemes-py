"""Seaborn integration examples for MSUthemes.

This script demonstrates how to use MSUthemes with seaborn visualizations.
"""

import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
import seaborn as sns
from msuthemes import set_msu_style, palettes, colors, load_bigten_data

# Apply MSU style to seaborn
set_msu_style(style='whitegrid')

# Create figure with multiple examples
fig = plt.figure(figsize=(15, 12))

# Example 1: Scatter plot with hue
print("Creating scatter plot...")
ax1 = plt.subplot(2, 3, 1)
tips = sns.load_dataset('tips')
sns.scatterplot(
    data=tips,
    x='total_bill',
    y='tip',
    hue='time',
    palette=[colors.MSU_GREEN, colors.MSU_ORANGE],
    s=100,
    alpha=0.7,
    ax=ax1
)
ax1.set_title('A) Scatter Plot with MSU Colors')

# Example 2: Box plot
print("Creating box plot...")
ax2 = plt.subplot(2, 3, 2)
qual_colors = palettes.msu_qual1.as_hex()
sns.boxplot(
    data=tips,
    x='day',
    y='total_bill',
    palette=qual_colors,
    ax=ax2
)
ax2.set_title('B) Box Plot with Qualitative Palette')

# Example 3: Violin plot
print("Creating violin plot...")
ax3 = plt.subplot(2, 3, 3)
sns.violinplot(
    data=tips,
    x='day',
    y='tip',
    palette=qual_colors,
    ax=ax3
)
ax3.set_title('C) Violin Plot')

# Example 4: Heatmap with sequential palette
print("Creating heatmap...")
ax4 = plt.subplot(2, 3, 4)
data = np.random.rand(10, 10)
cmap = palettes.msu_seq.as_matplotlib_cmap()
sns.heatmap(
    data,
    cmap=cmap,
    square=True,
    cbar_kws={'label': 'Value'},
    ax=ax4
)
ax4.set_title('D) Heatmap with Sequential Palette')

# Example 5: Correlation heatmap with diverging palette
print("Creating correlation heatmap...")
ax5 = plt.subplot(2, 3, 5)
# Create sample correlation data
corr_data = pd.DataFrame(
    np.random.randn(100, 5),
    columns=['A', 'B', 'C', 'D', 'E']
).corr()
cmap = palettes.msu_div.as_matplotlib_cmap()
sns.heatmap(
    corr_data,
    cmap=cmap,
    center=0,
    annot=True,
    fmt='.2f',
    square=True,
    ax=ax5
)
ax5.set_title('E) Correlation Heatmap\n(Diverging Palette)')

# Example 6: Bar plot with Big Ten data
print("Creating bar plot with real data...")
ax6 = plt.subplot(2, 3, 6)
from msuthemes import bigten_palette

# Load and prepare data
bigten_data = load_bigten_data(
    years=[2023],
    columns=['name', 'UGDS']
).dropna().sort_values('UGDS', ascending=False).head(6)

# Get colors
bt_colors = bigten_palette(bigten_data['name'].tolist())

sns.barplot(
    data=bigten_data,
    x='name',
    y='UGDS',
    palette=bt_colors,
    ax=ax6
)
ax6.set_xlabel('Institution')
ax6.set_ylabel('Enrollment')
ax6.set_title('F) Big Ten Enrollment (Top 6)')
plt.setp(ax6.xaxis.get_majorticklabels(), rotation=45, ha='right')

fig.suptitle('Seaborn Integration Examples', fontsize=16, fontweight='bold')

plt.tight_layout()
plt.savefig('examples/output/seaborn_examples.png', dpi=300, bbox_inches='tight')
print("✓ Saved: examples/output/seaborn_examples.png")
plt.show()

# Create a second figure with more advanced examples
print("\nCreating advanced seaborn examples...")

fig, axes = plt.subplots(2, 2, figsize=(14, 10))

# Example 7: Pair plot
print("Creating pair plot...")
set_msu_style(style='white')
iris = sns.load_dataset('iris')
g = sns.pairplot(
    iris,
    hue='species',
    palette=[colors.MSU_GREEN, colors.MSU_ORANGE, colors.MSU_TEAL],
    diag_kind='kde',
    height=2.5
)
g.fig.suptitle('Pair Plot with MSU Colors', y=1.02, fontsize=14, fontweight='bold')
plt.savefig('examples/output/seaborn_pairplot.png', dpi=300, bbox_inches='tight')
print("✓ Saved: examples/output/seaborn_pairplot.png")

# Example 8: Joint plot
print("Creating joint plot...")
set_msu_style(style='white')
g = sns.jointplot(
    data=tips,
    x='total_bill',
    y='tip',
    kind='hex',
    color=colors.MSU_GREEN,
    height=8
)
g.fig.suptitle('Joint Plot with Hexbin', y=1.02, fontsize=14, fontweight='bold')
plt.savefig('examples/output/seaborn_jointplot.png', dpi=300, bbox_inches='tight')
print("✓ Saved: examples/output/seaborn_jointplot.png")

# Example 9: FacetGrid
print("Creating facet grid...")
set_msu_style(style='whitegrid')
g = sns.FacetGrid(
    tips,
    col='time',
    row='sex',
    height=3,
    aspect=1.2
)
g.map(plt.scatter, 'total_bill', 'tip', color=colors.MSU_GREEN, alpha=0.6, s=50)
g.add_legend()
g.fig.suptitle('Facet Grid Example', y=1.02, fontsize=14, fontweight='bold')
plt.savefig('examples/output/seaborn_facetgrid.png', dpi=300, bbox_inches='tight')
print("✓ Saved: examples/output/seaborn_facetgrid.png")

print("\n✓ All seaborn examples created successfully!")
