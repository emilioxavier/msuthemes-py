"""Data visualization examples using the BigTen dataset.

This script demonstrates comprehensive data analysis and visualization
workflows using the BigTen institutional dataset.
"""

import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
from msuthemes import (
    theme_msu,
    colors,
    get_bigten_colors,
    load_bigten_data,
    get_bigten_summary
)

# Apply MSU theme
theme_msu(use_grid=True)

print("Loading BigTen dataset...")
# Load complete dataset
full_data = load_bigten_data()
print(f"✓ Loaded {len(full_data)} rows, {len(full_data.columns)} columns")
print(f"✓ Years: {int(full_data['entry_term'].min())}-{int(full_data['entry_term'].max())}")
print(f"✓ Institutions: {full_data['name'].nunique()}")

# Create comprehensive visualization
fig = plt.figure(figsize=(16, 12))

# 1. MSU enrollment history
print("\n1. Creating MSU enrollment history...")
ax1 = plt.subplot(3, 3, 1)
msu_data = load_bigten_data(
    institutions=['MSU'],
    columns=['entry_term', 'UGDS']
).dropna()

ax1.plot(
    msu_data['entry_term'],
    msu_data['UGDS'],
    color=colors.MSU_GREEN,
    linewidth=2.5,
    marker='o',
    markersize=5
)
ax1.fill_between(
    msu_data['entry_term'],
    msu_data['UGDS'],
    alpha=0.3,
    color=colors.MSU_GREEN
)
ax1.set_xlabel('Year')
ax1.set_ylabel('Enrollment')
ax1.set_title('A) MSU Enrollment Over Time')
ax1.grid(True, alpha=0.3)

# 2. Admission rates comparison
print("2. Creating admission rates comparison...")
ax2 = plt.subplot(3, 3, 2)
schools = ['MSU', 'Michigan', 'Ohio State', 'Wisconsin', 'Penn State']
adm_data = load_bigten_data(
    institutions=schools,
    years=list(range(2010, 2024)),
    columns=['name', 'entry_term', 'ADM_RATE']
).dropna()

school_colors = get_bigten_colors(schools)
for school in schools:
    school_data = adm_data[adm_data['name'] == school]
    ax2.plot(
        school_data['entry_term'],
        school_data['ADM_RATE'] * 100,
        label=school,
        color=school_colors[school],
        linewidth=2,
        marker='o',
        markersize=4
    )

ax2.set_xlabel('Year')
ax2.set_ylabel('Admission Rate (%)')
ax2.set_title('B) Admission Rates (2010-2023)')
ax2.legend(loc='best', fontsize=8)
ax2.grid(True, alpha=0.3)

# 3. Tuition trends
print("3. Creating tuition trends...")
ax3 = plt.subplot(3, 3, 3)
tuition_data = load_bigten_data(
    institutions=['MSU'],
    columns=['entry_term', 'TUITIONFEE_IN', 'TUITIONFEE_OUT']
).dropna()

ax3.plot(
    tuition_data['entry_term'],
    tuition_data['TUITIONFEE_IN'],
    color=colors.MSU_GREEN,
    linewidth=2,
    marker='s',
    label='In-State'
)
ax3.plot(
    tuition_data['entry_term'],
    tuition_data['TUITIONFEE_OUT'],
    color=colors.MSU_ORANGE,
    linewidth=2,
    marker='^',
    label='Out-of-State'
)
ax3.set_xlabel('Year')
ax3.set_ylabel('Tuition & Fees ($)')
ax3.set_title('C) MSU Tuition Trends')
ax3.legend()
ax3.grid(True, alpha=0.3)

# 4. Enrollment by institution (2023)
print("4. Creating enrollment bar chart...")
ax4 = plt.subplot(3, 3, 4)
enrollment_2023 = load_bigten_data(
    years=[2023],
    columns=['name', 'UGDS']
).dropna().sort_values('UGDS', ascending=True)

from msuthemes import bigten_palette
colors_list = bigten_palette(enrollment_2023['name'].tolist())

ax4.barh(
    range(len(enrollment_2023)),
    enrollment_2023['UGDS'].values,
    color=colors_list
)
ax4.set_yticks(range(len(enrollment_2023)))
ax4.set_yticklabels(enrollment_2023['name'], fontsize=8)
ax4.set_xlabel('Enrollment')
ax4.set_title('D) Big Ten Enrollment (2023)')
ax4.grid(True, alpha=0.3, axis='x')

# 5. Demographics - MSU over time
print("5. Creating demographics stacked area...")
ax5 = plt.subplot(3, 3, 5)
demo_data = load_bigten_data(
    institutions=['MSU'],
    columns=['entry_term', 'UGDS_WHITE', 'UGDS_BLACK', 'UGDS_HISP', 'UGDS_ASIAN']
).dropna()

ax5.stackplot(
    demo_data['entry_term'],
    demo_data['UGDS_WHITE'] * 100,
    demo_data['UGDS_BLACK'] * 100,
    demo_data['UGDS_HISP'] * 100,
    demo_data['UGDS_ASIAN'] * 100,
    labels=['White', 'Black', 'Hispanic', 'Asian'],
    colors=[colors.MSU_GREEN, colors.MSU_ORANGE, colors.MSU_TEAL, colors.MSU_PURPLE],
    alpha=0.8
)
ax5.set_xlabel('Year')
ax5.set_ylabel('Percentage of Students')
ax5.set_title('E) MSU Student Demographics')
ax5.legend(loc='upper left', fontsize=8)
ax5.grid(True, alpha=0.3)

# 6. Completion rates
print("6. Creating completion rates...")
ax6 = plt.subplot(3, 3, 6)
completion_data = load_bigten_data(
    institutions=schools,
    years=[2023],
    columns=['name', 'C150_4']
).dropna().sort_values('C150_4', ascending=False)

school_colors_comp = get_bigten_colors(completion_data['name'].tolist())
colors_comp = [school_colors_comp[name] for name in completion_data['name']]

ax6.bar(
    range(len(completion_data)),
    completion_data['C150_4'].values * 100,
    color=colors_comp
)
ax6.set_xticks(range(len(completion_data)))
ax6.set_xticklabels(completion_data['name'], rotation=45, ha='right', fontsize=8)
ax6.set_ylabel('4-Year Completion Rate (%)')
ax6.set_title('F) Completion Rates (2023)')
ax6.grid(True, alpha=0.3, axis='y')

# 7. Scatter: Enrollment vs Admission Rate
print("7. Creating scatter plot...")
ax7 = plt.subplot(3, 3, 7)
scatter_data = load_bigten_data(
    years=[2023],
    columns=['name', 'UGDS', 'ADM_RATE']
).dropna()

# Color by institution
for _, row in scatter_data.iterrows():
    try:
        color = get_bigten_colors([row['name']])[row['name']]
    except:
        color = colors.MSU_GREY

    ax7.scatter(
        row['UGDS'],
        row['ADM_RATE'] * 100,
        s=150,
        color=color,
        alpha=0.7,
        edgecolors='black',
        linewidth=1
    )

ax7.set_xlabel('Enrollment')
ax7.set_ylabel('Admission Rate (%)')
ax7.set_title('G) Enrollment vs. Selectivity (2023)')
ax7.grid(True, alpha=0.3)

# 8. Gender distribution
print("8. Creating gender distribution...")
ax8 = plt.subplot(3, 3, 8)
gender_data = load_bigten_data(
    institutions=['MSU'],
    columns=['entry_term', 'UGDS_MEN', 'UGDS_WOMEN']
).dropna()

ax8.plot(
    gender_data['entry_term'],
    gender_data['UGDS_MEN'] * 100,
    color=colors.MSU_GREEN,
    linewidth=2,
    marker='s',
    label='Men'
)
ax8.plot(
    gender_data['entry_term'],
    gender_data['UGDS_WOMEN'] * 100,
    color=colors.MSU_ORANGE,
    linewidth=2,
    marker='o',
    label='Women'
)
ax8.set_xlabel('Year')
ax8.set_ylabel('Percentage of Students')
ax8.set_title('H) MSU Gender Distribution')
ax8.legend()
ax8.grid(True, alpha=0.3)

# 9. Pell Grant recipients
print("9. Creating Pell Grant trends...")
ax9 = plt.subplot(3, 3, 9)
pell_schools = ['MSU', 'Michigan', 'Ohio State']
pell_data = load_bigten_data(
    institutions=pell_schools,
    years=list(range(2010, 2024)),
    columns=['name', 'entry_term', 'PCTPELL']
).dropna()

pell_colors = get_bigten_colors(pell_schools)
for school in pell_schools:
    school_data = pell_data[pell_data['name'] == school]
    ax9.plot(
        school_data['entry_term'],
        school_data['PCTPELL'] * 100,
        label=school,
        color=pell_colors[school],
        linewidth=2,
        marker='o',
        markersize=4
    )

ax9.set_xlabel('Year')
ax9.set_ylabel('Pell Grant Recipients (%)')
ax9.set_title('I) Pell Grant Recipients (2010-2023)')
ax9.legend(fontsize=8)
ax9.grid(True, alpha=0.3)

# Overall title
fig.suptitle('Big Ten Institutional Data Analysis Dashboard',
             fontsize=18, fontweight='bold', y=0.995)

plt.tight_layout()
plt.savefig('examples/output/data_visualization.png', dpi=300, bbox_inches='tight')
print("\n✓ Saved: examples/output/data_visualization.png")
plt.show()

# Print summary statistics
print("\n" + "="*60)
print("Dataset Summary Statistics")
print("="*60)
summary = get_bigten_summary()
print(summary.head())
print("\n✓ Data visualization examples created successfully!")
