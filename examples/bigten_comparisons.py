"""Big Ten institutional comparison examples.

This script demonstrates how to compare Big Ten institutions using
institutional colors and the BigTen dataset.
"""

import matplotlib.pyplot as plt
import numpy as np
from msuthemes import (
    theme_msu,
    get_bigten_colors,
    bigten_palette,
    load_bigten_data
)

# Apply MSU theme
theme_msu()

# Create figure with multiple subplots
fig, ((ax1, ax2), (ax3, ax4)) = plt.subplots(2, 2, figsize=(14, 10))

# Example 1: Enrollment comparison (bar chart)
print("Creating enrollment comparison...")
schools = ['MSU', 'Michigan', 'Ohio State', 'Penn State', 'Wisconsin']
data = load_bigten_data(
    institutions=schools,
    years=[2023],
    columns=['name', 'UGDS']
)

# Get colors for these schools
school_colors = get_bigten_colors(schools)
colors_list = [school_colors[s] for s in schools]

# Plot
data_sorted = data.sort_values('UGDS', ascending=False)
ax1.barh(
    range(len(data_sorted)),
    data_sorted['UGDS'].values,
    color=[school_colors[name] for name in data_sorted['name']]
)
ax1.set_yticks(range(len(data_sorted)))
ax1.set_yticklabels(data_sorted['name'])
ax1.set_xlabel('Undergraduate Enrollment')
ax1.set_title('A) Big Ten Enrollment (2023)')

# Example 2: Enrollment trends over time
print("Creating enrollment trends...")
trend_schools = ['MSU', 'Michigan', 'Ohio State']
trend_data = load_bigten_data(
    institutions=trend_schools,
    years=list(range(2015, 2024)),
    columns=['name', 'entry_term', 'UGDS']
)

trend_colors = get_bigten_colors(trend_schools)
for school in trend_schools:
    school_data = trend_data[trend_data['name'] == school]
    ax2.plot(
        school_data['entry_term'],
        school_data['UGDS'],
        label=school,
        color=trend_colors[school],
        linewidth=2.5,
        marker='o',
        markersize=6
    )

ax2.set_xlabel('Year')
ax2.set_ylabel('Enrollment')
ax2.set_title('B) Enrollment Trends (2015-2023)')
ax2.legend()
ax2.grid(True, alpha=0.3)

# Example 3: Admission rates comparison
print("Creating admission rates comparison...")
adm_data = load_bigten_data(
    years=[2023],
    columns=['name', 'ADM_RATE']
).dropna(subset=['ADM_RATE'])

# Sort and take top 8
adm_data = adm_data.sort_values('ADM_RATE', ascending=True).head(8)

# Get colors
adm_colors = bigten_palette(adm_data['name'].tolist())

ax3.bar(
    range(len(adm_data)),
    adm_data['ADM_RATE'].values * 100,
    color=adm_colors
)
ax3.set_xticks(range(len(adm_data)))
ax3.set_xticklabels(adm_data['name'], rotation=45, ha='right')
ax3.set_ylabel('Admission Rate (%)')
ax3.set_title('C) Most Selective Big Ten Schools (2023)')

# Example 4: Multi-variable comparison (scatter plot)
print("Creating multi-variable comparison...")
scatter_data = load_bigten_data(
    institutions=schools,
    years=[2023],
    columns=['name', 'UGDS', 'ADM_RATE']
).dropna()

for school in schools:
    school_data = scatter_data[scatter_data['name'] == school]
    if len(school_data) > 0:
        ax4.scatter(
            school_data['UGDS'],
            school_data['ADM_RATE'] * 100,
            s=200,
            color=school_colors[school],
            label=school,
            alpha=0.7,
            edgecolors='black',
            linewidth=1.5
        )

ax4.set_xlabel('Undergraduate Enrollment')
ax4.set_ylabel('Admission Rate (%)')
ax4.set_title('D) Enrollment vs. Admission Rate (2023)')
ax4.legend(loc='best')
ax4.grid(True, alpha=0.3)

# Overall title
fig.suptitle('Big Ten Conference Institutional Comparisons',
             fontsize=16, fontweight='bold', y=0.995)

# Save and show
plt.tight_layout()
plt.savefig('examples/output/bigten_comparisons.png', dpi=300, bbox_inches='tight')
print("✓ Saved: examples/output/bigten_comparisons.png")
plt.show()
