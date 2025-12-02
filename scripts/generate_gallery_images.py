#!/usr/bin/env python3
"""
Generate example plot images for the MkDocs gallery.

This script creates PNG images of all example plots shown in the documentation
gallery. Images are saved to docs_mkdocs/images/examples/ and can be referenced
in the markdown files.

Usage:
    python scripts/generate_gallery_images.py
"""

import os
import sys
import numpy as np
import matplotlib
import matplotlib.pyplot as plt

# Use non-interactive backend
matplotlib.use('Agg')

# Add package to path for development
sys.path.insert(0, os.path.join(os.path.dirname(__file__), '..'))

from msuthemes import (
    theme_msu, msu_seq, msu_div, msu_qual1, msu_qual2,
    MSU_GREEN, MSU_ORANGE, MSU_TEAL, MSU_WHITE,
    bigten_palette, list_bigten_institutions, load_bigten_data
)

# Configuration
OUTPUT_DIR = os.path.join('docs_mkdocs', 'images', 'examples')
DPI = 150
FIGSIZE_STANDARD = (10, 6)
FIGSIZE_SQUARE = (8, 8)
FIGSIZE_WIDE = (12, 7)
FIGSIZE_TALL = (10, 8)

# Ensure output directories exist
for subdir in ['basic', 'msu', 'bigten']:
    os.makedirs(os.path.join(OUTPUT_DIR, subdir), exist_ok=True)


def save_plot(filename, subdir='basic'):
    """Save current plot to file."""
    filepath = os.path.join(OUTPUT_DIR, subdir, filename)
    plt.savefig(filepath, dpi=DPI, bbox_inches='tight', facecolor='white')
    plt.close()
    print(f"Generated: {filepath}")


def generate_basic_plots():
    """Generate basic plot examples."""
    print("\n=== Generating Basic Plots ===")

    # Apply MSU theme
    theme_msu()

    # 1. Single series line plot
    x = np.linspace(0, 10, 100)
    y = np.sin(x)
    fig, ax = plt.subplots(figsize=FIGSIZE_STANDARD)
    ax.plot(x, y, color=MSU_GREEN, linewidth=2.5)
    ax.set_xlabel('X-axis')
    ax.set_ylabel('Y-axis')
    ax.set_title('Single Series Line Plot')
    save_plot('line_single.png')

    # 2. Multiple series line plot
    colors = msu_qual1.as_hex()
    fig, ax = plt.subplots(figsize=FIGSIZE_STANDARD)
    for i, color in enumerate(colors[:3]):
        y = np.sin(x + i * 0.5)
        ax.plot(x, y, color=color, linewidth=2.5, label=f'Series {i+1}')
    ax.set_xlabel('X-axis')
    ax.set_ylabel('Y-axis')
    ax.set_title('Multiple Series Line Plot')
    ax.legend(frameon=False)
    save_plot('line_multiple.png')

    # 3. Vertical bar chart
    categories = ['A', 'B', 'C', 'D', 'E']
    values = [23, 45, 56, 34, 41]
    fig, ax = plt.subplots(figsize=FIGSIZE_STANDARD)
    ax.bar(categories, values, color=msu_qual1.as_hex())
    ax.set_xlabel('Category')
    ax.set_ylabel('Value')
    ax.set_title('Vertical Bar Chart')
    save_plot('bar_vertical.png')

    # 4. Horizontal bar chart
    categories = ['Category A', 'Category B', 'Category C', 'Category D', 'Category E']
    values = [23, 45, 56, 34, 41]
    fig, ax = plt.subplots(figsize=FIGSIZE_STANDARD)
    ax.barh(categories, values, color=msu_qual1.as_hex())
    ax.set_xlabel('Value')
    ax.set_title('Horizontal Bar Chart')
    save_plot('bar_horizontal.png')

    # 5. Grouped bar chart
    categories = ['A', 'B', 'C', 'D']
    group1 = [23, 45, 56, 34]
    group2 = [17, 38, 42, 29]
    fig, ax = plt.subplots(figsize=FIGSIZE_STANDARD)
    x_pos = np.arange(len(categories))
    width = 0.35
    colors = msu_qual1.as_hex()
    ax.bar(x_pos - width/2, group1, width, label='Group 1', color=colors[0])
    ax.bar(x_pos + width/2, group2, width, label='Group 2', color=colors[1])
    ax.set_xlabel('Category')
    ax.set_ylabel('Value')
    ax.set_title('Grouped Bar Chart')
    ax.set_xticks(x_pos)
    ax.set_xticklabels(categories)
    ax.legend()
    save_plot('bar_grouped.png')

    # 6. Basic scatter plot
    np.random.seed(42)
    x = np.random.rand(100)
    y = np.random.rand(100)
    fig, ax = plt.subplots(figsize=FIGSIZE_STANDARD)
    ax.scatter(x, y, color=MSU_GREEN, s=50, alpha=0.6)
    ax.set_xlabel('X Variable')
    ax.set_ylabel('Y Variable')
    ax.set_title('Scatter Plot')
    save_plot('scatter_basic.png')

    # 7. Scatter with categories
    colors = msu_qual1.as_hex()
    fig, ax = plt.subplots(figsize=FIGSIZE_STANDARD)
    n_per_category = 30
    for i, color in enumerate(colors[:3]):
        x = np.random.rand(n_per_category) + i
        y = np.random.rand(n_per_category) + i
        ax.scatter(x, y, color=color, s=50, alpha=0.7, label=f'Category {i+1}')
    ax.set_xlabel('X Variable')
    ax.set_ylabel('Y Variable')
    ax.set_title('Scatter Plot with Categories')
    ax.legend()
    save_plot('scatter_categories.png')

    # 8. Histogram
    data = np.random.randn(1000)
    fig, ax = plt.subplots(figsize=FIGSIZE_STANDARD)
    ax.hist(data, bins=30, color=MSU_GREEN, alpha=0.7, edgecolor='white')
    ax.set_xlabel('Value')
    ax.set_ylabel('Frequency')
    ax.set_title('Histogram')
    save_plot('histogram_basic.png')

    # 9. Overlapping histograms
    data1 = np.random.randn(1000)
    data2 = np.random.randn(1000) + 1
    colors = msu_qual1.as_hex()
    fig, ax = plt.subplots(figsize=FIGSIZE_STANDARD)
    ax.hist(data1, bins=30, alpha=0.6, color=colors[0], label='Distribution 1', edgecolor='white')
    ax.hist(data2, bins=30, alpha=0.6, color=colors[1], label='Distribution 2', edgecolor='white')
    ax.set_xlabel('Value')
    ax.set_ylabel('Frequency')
    ax.set_title('Overlapping Histograms')
    ax.legend()
    save_plot('histogram_overlapping.png')

    # 10. Box plot
    data = [np.random.randn(100) + i for i in range(5)]
    colors = msu_qual1.as_hex()
    fig, ax = plt.subplots(figsize=FIGSIZE_STANDARD)
    bp = ax.boxplot(data, patch_artist=True)
    for patch, color in zip(bp['boxes'], colors):
        patch.set_facecolor(color)
    ax.set_xlabel('Category')
    ax.set_ylabel('Value')
    ax.set_title('Box Plot')
    ax.set_xticklabels(['A', 'B', 'C', 'D', 'E'])
    save_plot('boxplot.png')

    # 11. Pie chart
    sizes = [15, 30, 45, 10]
    labels = ['A', 'B', 'C', 'D']
    colors = msu_qual1.as_hex()[:4]
    fig, ax = plt.subplots(figsize=FIGSIZE_SQUARE)
    ax.pie(sizes, labels=labels, colors=colors, autopct='%1.1f%%', startangle=90)
    ax.set_title('Pie Chart')
    save_plot('pie.png')

    # 12. Heatmap
    data = np.random.rand(10, 10)
    fig, ax = plt.subplots(figsize=FIGSIZE_STANDARD)
    im = ax.imshow(data, cmap=msu_seq.as_matplotlib_cmap(), aspect='auto')
    ax.set_xlabel('X-axis')
    ax.set_ylabel('Y-axis')
    ax.set_title('Heatmap')
    plt.colorbar(im, ax=ax, label='Value')
    save_plot('heatmap.png')

    # 13. Correlation matrix
    np.random.seed(42)
    n_vars = 8
    data = np.random.randn(100, n_vars)
    corr_matrix = np.corrcoef(data.T)
    fig, ax = plt.subplots(figsize=FIGSIZE_STANDARD)
    im = ax.imshow(corr_matrix, cmap=msu_div.as_matplotlib_cmap(),
                   vmin=-1, vmax=1, aspect='auto')
    var_names = [f'Var {i+1}' for i in range(n_vars)]
    ax.set_xticks(np.arange(n_vars))
    ax.set_yticks(np.arange(n_vars))
    ax.set_xticklabels(var_names)
    ax.set_yticklabels(var_names)
    ax.set_title('Correlation Matrix')
    plt.colorbar(im, ax=ax, label='Correlation')
    save_plot('correlation_matrix.png')

    # 14. Stacked area plot
    x = np.arange(10)
    y1 = np.random.rand(10)
    y2 = np.random.rand(10)
    y3 = np.random.rand(10)
    colors = msu_qual1.as_hex()
    fig, ax = plt.subplots(figsize=FIGSIZE_STANDARD)
    ax.stackplot(x, y1, y2, y3, labels=['Series 1', 'Series 2', 'Series 3'],
                 colors=colors[:3], alpha=0.8)
    ax.set_xlabel('X-axis')
    ax.set_ylabel('Y-axis')
    ax.set_title('Stacked Area Plot')
    ax.legend(loc='upper left')
    save_plot('area_stacked.png')

    # 15. Multiple subplots
    x = np.linspace(0, 10, 100)
    colors = msu_qual1.as_hex()
    fig, axes = plt.subplots(2, 2, figsize=(12, 10))

    # Plot 1: Line
    axes[0, 0].plot(x, np.sin(x), color=MSU_GREEN, linewidth=2)
    axes[0, 0].set_title('Line Plot')

    # Plot 2: Scatter
    axes[0, 1].scatter(np.random.rand(50), np.random.rand(50),
                       color=colors[1], s=50, alpha=0.6)
    axes[0, 1].set_title('Scatter Plot')

    # Plot 3: Bar
    axes[1, 0].bar(['A', 'B', 'C', 'D'], [3, 7, 2, 5], color=colors[:4])
    axes[1, 0].set_title('Bar Chart')

    # Plot 4: Histogram
    axes[1, 1].hist(np.random.randn(1000), bins=30, color=colors[2], alpha=0.7)
    axes[1, 1].set_title('Histogram')

    plt.tight_layout()
    save_plot('subplots.png')


def generate_msu_plots():
    """Generate MSU-themed plot examples."""
    print("\n=== Generating MSU Themed Plots ===")

    # Apply MSU theme with grid
    theme_msu(base_size=11, use_grid=True)

    # 1. Professional line chart
    x = np.linspace(0, 10, 100)
    colors = msu_qual1.as_hex()
    fig, ax = plt.subplots(figsize=FIGSIZE_STANDARD)
    for i, color in enumerate(colors[:3]):
        y = np.exp(-x/5) * np.sin(x + i * 0.5) + i * 0.5
        ax.plot(x, y, color=color, linewidth=2.5,
                label=f'Treatment {i+1}', marker='o',
                markersize=4, markevery=10)
    ax.set_xlabel('Time (hours)')
    ax.set_ylabel('Response (units)')
    ax.set_title('Treatment Response Over Time')
    ax.legend(frameon=False, loc='best')
    ax.set_xlim(0, 10)
    save_plot('professional_line.png', 'msu')

    # 2. Research poster figure
    theme_msu(base_size=14, use_grid=True)
    categories = ['Control', 'Treatment A', 'Treatment B', 'Treatment C', 'Treatment D']
    means = [3.2, 5.8, 4.5, 6.1, 5.3]
    std = [0.5, 0.7, 0.6, 0.8, 0.6]
    colors = msu_qual1.as_hex()
    fig, ax = plt.subplots(figsize=(12, 8))
    x_pos = np.arange(len(categories))
    ax.bar(x_pos, means, yerr=std, color=colors, capsize=10, error_kw={'linewidth': 2})
    ax.set_xticks(x_pos)
    ax.set_xticklabels(categories, rotation=0)
    ax.set_ylabel('Effect Size (units)')
    ax.set_title('Experimental Results Summary', pad=20)
    ax.plot([1, 3], [7.0, 7.0], 'k-', linewidth=2)
    ax.text(2, 7.2, '***', ha='center', fontsize=18)
    save_plot('poster_figure.png', 'msu')

    # 3. Color palette showcase
    theme_msu()
    palettes = [
        ('Sequential (msu_seq)', msu_seq),
        ('Diverging (msu_div)', msu_div),
        ('Qualitative 1 (msu_qual1)', msu_qual1),
        ('Qualitative 2 (msu_qual2)', msu_qual2)
    ]
    fig, axes = plt.subplots(4, 1, figsize=(12, 10))
    for ax, (title, palette) in zip(axes, palettes):
        colors = palette.as_hex()
        n_colors = len(colors)
        for i, color in enumerate(colors):
            ax.add_patch(plt.Rectangle((i, 0), 1, 1,
                                       facecolor=color,
                                       edgecolor='white',
                                       linewidth=2))
            ax.text(i + 0.5, 0.5, color,
                    ha='center', va='center',
                    fontsize=9, rotation=90,
                    color='white' if i < n_colors // 2 else 'black')
        ax.set_xlim(0, n_colors)
        ax.set_ylim(0, 1)
        ax.set_title(title, loc='left', pad=10)
        ax.axis('off')
    plt.tight_layout()
    save_plot('palette_showcase.png', 'msu')

    # 4. Gradient visualization
    x = np.linspace(0, 1, 100)
    y = np.linspace(0, 1, 100)
    X, Y = np.meshgrid(x, y)
    Z = np.sqrt(X**2 + Y**2)
    fig, ax = plt.subplots(figsize=FIGSIZE_STANDARD)
    im = ax.imshow(Z, extent=[0, 1, 0, 1], origin='lower',
                   cmap=msu_seq.as_matplotlib_cmap(), aspect='auto')
    ax.set_xlabel('X Coordinate')
    ax.set_ylabel('Y Coordinate')
    ax.set_title('Sequential Palette Gradient')
    cbar = plt.colorbar(im, ax=ax)
    cbar.set_label('Distance from Origin')
    save_plot('gradient.png', 'msu')

    # 5. Time series with confidence intervals
    theme_msu(use_grid=True)
    np.random.seed(42)
    x = np.linspace(0, 10, 50)
    y1 = np.sin(x) + np.random.randn(50) * 0.2
    y2 = np.cos(x) + np.random.randn(50) * 0.2
    window = 5
    y1_smooth = np.convolve(y1, np.ones(window)/window, mode='same')
    y2_smooth = np.convolve(y2, np.ones(window)/window, mode='same')
    # Calculate rolling standard deviation
    y1_std = np.array([np.std(y1[max(0, i-window):min(len(y1), i+window+1)])
                       for i in range(len(y1))])
    y2_std = np.array([np.std(y2[max(0, i-window):min(len(y2), i+window+1)])
                       for i in range(len(y2))])
    fig, ax = plt.subplots(figsize=(12, 6))
    ax.plot(x, y1_smooth, color=MSU_GREEN, linewidth=2.5, label='Group 1')
    ax.fill_between(x, y1_smooth - y1_std, y1_smooth + y1_std,
                     color=MSU_GREEN, alpha=0.2)
    ax.plot(x, y2_smooth, color=MSU_ORANGE, linewidth=2.5, label='Group 2')
    ax.fill_between(x, y2_smooth - y2_std, y2_smooth + y2_std,
                     color=MSU_ORANGE, alpha=0.2)
    ax.set_xlabel('Time (days)')
    ax.set_ylabel('Measurement')
    ax.set_title('Longitudinal Study Results')
    ax.legend(frameon=False)
    save_plot('timeseries_ci.png', 'msu')

    # 6. Grouped comparison
    theme_msu()
    groups = ['Pre-test', 'Post-test', 'Follow-up']
    data = {
        'Control': [3.2, 3.5, 3.3],
        'Treatment A': [3.1, 5.8, 5.2],
        'Treatment B': [3.3, 4.5, 4.8],
        'Treatment C': [3.0, 6.1, 5.9]
    }
    colors = msu_qual1.as_hex()
    fig, ax = plt.subplots(figsize=(12, 7))
    x = np.arange(len(groups))
    width = 0.2
    conditions = list(data.keys())
    for i, (condition, values) in enumerate(data.items()):
        offset = (i - len(conditions)/2 + 0.5) * width
        ax.bar(x + offset, values, width, label=condition, color=colors[i])
    ax.set_xlabel('Assessment Point')
    ax.set_ylabel('Score')
    ax.set_title('Intervention Effectiveness Across Time')
    ax.set_xticks(x)
    ax.set_xticklabels(groups)
    ax.legend(title='Condition', frameon=False)
    save_plot('grouped_comparison.png', 'msu')

    # 7. Dashboard style
    theme_msu(base_size=10)
    fig = plt.figure(figsize=(14, 10))
    gs = fig.add_gridspec(3, 3, hspace=0.3, wspace=0.3)
    colors = msu_qual1.as_hex()

    # Top: Large time series
    ax1 = fig.add_subplot(gs[0, :])
    x = np.linspace(0, 10, 100)
    for i in range(3):
        y = np.sin(x + i * 0.5) + i * 0.3
        ax1.plot(x, y, color=colors[i], linewidth=2, label=f'Metric {i+1}')
    ax1.set_title('Primary Metrics Over Time', loc='left', fontweight='bold')
    ax1.legend(ncol=3, frameon=False)
    ax1.set_xlabel('Time')

    # Middle left: Bar chart
    ax2 = fig.add_subplot(gs[1, 0])
    categories = ['A', 'B', 'C', 'D']
    values = [23, 45, 32, 38]
    ax2.bar(categories, values, color=colors[:4])
    ax2.set_title('Category Breakdown', loc='left')

    # Middle center: Pie chart
    ax3 = fig.add_subplot(gs[1, 1])
    sizes = [30, 25, 25, 20]
    ax3.pie(sizes, labels=categories, colors=colors[:4],
            autopct='%1.0f%%', startangle=90)
    ax3.set_title('Proportion Analysis', loc='left')

    # Middle right: Scatter
    ax4 = fig.add_subplot(gs[1, 2])
    x_scatter = np.random.rand(50)
    y_scatter = np.random.rand(50)
    ax4.scatter(x_scatter, y_scatter, color=MSU_GREEN, s=50, alpha=0.6)
    ax4.set_title('Correlation View', loc='left')

    # Bottom: Histogram
    ax5 = fig.add_subplot(gs[2, :])
    data = np.random.randn(1000)
    ax5.hist(data, bins=50, color=MSU_GREEN, alpha=0.7)
    ax5.set_title('Distribution Analysis', loc='left', fontweight='bold')
    ax5.set_xlabel('Value')
    ax5.set_ylabel('Frequency')

    fig.suptitle('MSU Data Dashboard', fontsize=16, fontweight='bold', y=0.995)
    save_plot('dashboard.png', 'msu')


def generate_bigten_plots():
    """Generate Big Ten comparison plot examples."""
    print("\n=== Generating Big Ten Plots ===")

    theme_msu()

    # 1. Simple bar comparison (mock data)
    institutions = ['Ohio State', 'Michigan', 'Penn State', 'Michigan State',
                    'Wisconsin', 'Iowa', 'Minnesota', 'Indiana']
    values = [45000, 43000, 42000, 39000, 38000, 35000, 34000, 32000]
    colors = bigten_palette(institutions)
    fig, ax = plt.subplots(figsize=(12, 8))
    ax.barh(range(len(institutions)), values, color=colors)
    ax.set_yticks(range(len(institutions)))
    ax.set_yticklabels(institutions)
    ax.set_xlabel('Enrollment')
    ax.set_title('Big Ten Enrollment Comparison')
    save_plot('enrollment_comparison.png', 'bigten')

    # 2. Time series comparison
    theme_msu(use_grid=True)
    schools = ['Michigan State', 'Michigan', 'Ohio State', 'Wisconsin', 'Penn State']
    colors = bigten_palette(schools)
    fig, ax = plt.subplots(figsize=(12, 7))
    years = np.arange(2010, 2024)
    np.random.seed(42)
    for school, color in zip(schools, colors):
        # Generate realistic-looking admission rate data
        base_rate = 0.5 + np.random.rand() * 0.3
        trend = np.linspace(0, 0.1, len(years))
        noise = np.random.randn(len(years)) * 0.02
        rates = base_rate - trend + noise
        rates = np.clip(rates, 0.2, 0.9) * 100
        ax.plot(years, rates, color=color, linewidth=2.5,
                marker='o', markersize=6, label=school)
    ax.set_xlabel('Year')
    ax.set_ylabel('Admission Rate (%)')
    ax.set_title('Big Ten Admission Rates Over Time')
    ax.legend(frameon=False, loc='best')
    save_plot('admission_trends.png', 'bigten')

    # 3. Grouped bar comparison
    theme_msu()
    schools = ['Michigan State', 'Michigan', 'Ohio State', 'Wisconsin', 'Minnesota']
    colors = bigten_palette(schools)
    # Mock tuition data
    tuition_2015 = [13000, 14000, 10000, 10500, 13500]
    tuition_2023 = [15000, 16000, 11500, 11800, 15000]
    fig, ax = plt.subplots(figsize=(12, 7))
    x = np.arange(len(schools))
    width = 0.35
    ax.bar(x - width/2, tuition_2015, width, label='2015', color=colors, alpha=0.6)
    ax.bar(x + width/2, tuition_2023, width, label='2023', color=colors, alpha=1.0)
    ax.set_xlabel('Institution')
    ax.set_ylabel('In-State Tuition ($)')
    ax.set_title('Tuition Growth Comparison (2015 vs 2023)')
    ax.set_xticks(x)
    ax.set_xticklabels(schools, rotation=45, ha='right')
    ax.legend()
    save_plot('tuition_comparison.png', 'bigten')

    # 4. Scatter comparison
    all_institutions = list_bigten_institutions()[:12]  # Use first 12 for clarity
    colors = bigten_palette(all_institutions)
    np.random.seed(42)
    admission_rates = 20 + np.random.rand(len(all_institutions)) * 60
    completion_rates = 60 + np.random.rand(len(all_institutions)) * 30
    enrollment = 20000 + np.random.rand(len(all_institutions)) * 30000

    fig, ax = plt.subplots(figsize=(10, 10))
    scatter = ax.scatter(admission_rates, completion_rates,
                         s=enrollment/50, c=colors, alpha=0.6)
    ax.set_xlabel('Admission Rate (%)')
    ax.set_ylabel('6-Year Completion Rate (%)')
    ax.set_title('Big Ten: Admissions vs Completion\nBubble size = Enrollment')

    # Add labels for a few interesting points
    for i in [0, 1, 4]:
        ax.annotate(all_institutions[i],
                   (admission_rates[i], completion_rates[i]),
                   xytext=(5, 5), textcoords='offset points',
                   fontsize=9, alpha=0.8)
    save_plot('scatter_comparison.png', 'bigten')

    # 5. Difference from average
    theme_msu()
    all_institutions = list_bigten_institutions()
    np.random.seed(42)
    completion_rates = 70 + np.random.rand(len(all_institutions)) * 20
    mean_rate = np.mean(completion_rates)
    differences = completion_rates - mean_rate
    sorted_idx = np.argsort(differences)
    sorted_institutions = [all_institutions[i] for i in sorted_idx]
    sorted_differences = differences[sorted_idx]

    colors_div = msu_div.as_hex()
    color_array = [colors_div[2] if x < 0 else colors_div[-3] for x in sorted_differences]

    fig, ax = plt.subplots(figsize=(12, 8))
    y_pos = np.arange(len(sorted_institutions))
    ax.barh(y_pos, sorted_differences, color=color_array)
    ax.axvline(x=0, color='black', linestyle='--', linewidth=1.5, alpha=0.7)
    ax.set_yticks(y_pos)
    ax.set_yticklabels(sorted_institutions)
    ax.set_xlabel('Percentage Points from Conference Average')
    ax.set_title('Completion Rate vs Big Ten Average')
    save_plot('difference_from_avg.png', 'bigten')

    # 6. Conference heatmap
    theme_msu()
    institutions = all_institutions[:10]  # Use subset for clarity
    np.random.seed(42)
    metrics = ['Admission\nRate', 'Completion\nRate', 'Pell Grant\n%', 'In-State\nTuition']
    data = np.random.rand(len(metrics), len(institutions))

    fig, ax = plt.subplots(figsize=(14, 6))
    im = ax.imshow(data, cmap=msu_seq.as_matplotlib_cmap(), aspect='auto')
    ax.set_xticks(range(len(institutions)))
    ax.set_xticklabels(institutions, rotation=45, ha='right')
    ax.set_yticks(range(len(metrics)))
    ax.set_yticklabels(metrics)
    ax.set_title('Big Ten Metrics Heatmap (Normalized)')
    plt.colorbar(im, ax=ax, label='Normalized Value')
    save_plot('conference_heatmap.png', 'bigten')

    # 7. Conference overview dashboard
    theme_msu(base_size=9)
    fig = plt.figure(figsize=(16, 10))
    gs = fig.add_gridspec(3, 3, hspace=0.35, wspace=0.35)

    institutions_subset = all_institutions[:8]
    colors = bigten_palette(institutions_subset)

    # Panel 1: Enrollment
    ax1 = fig.add_subplot(gs[0, :])
    enrollment = [45000, 43000, 42000, 39000, 38000, 35000, 34000, 32000]
    ax1.bar(range(len(institutions_subset)), enrollment, color=colors)
    ax1.set_xticks(range(len(institutions_subset)))
    ax1.set_xticklabels(institutions_subset, rotation=45, ha='right')
    ax1.set_ylabel('Enrollment')
    ax1.set_title('A. Undergraduate Enrollment', loc='left', fontweight='bold')

    # Panel 2: Admission Rate Histogram
    ax2 = fig.add_subplot(gs[1, 0])
    admission_rates = 20 + np.random.rand(18) * 60
    ax2.hist(admission_rates, bins=10, color=MSU_GREEN, alpha=0.7)
    ax2.set_xlabel('Admission Rate (%)')
    ax2.set_ylabel('Frequency')
    ax2.set_title('B. Admission Rate\nDistribution', loc='left', fontweight='bold')

    # Panel 3: Completion vs Tuition
    ax3 = fig.add_subplot(gs[1, 1])
    tuition = 10000 + np.random.rand(8) * 8000
    completion = 70 + np.random.rand(8) * 20
    ax3.scatter(tuition, completion, c=colors, s=100, alpha=0.7)
    ax3.set_xlabel('Tuition ($)')
    ax3.set_ylabel('Completion Rate (%)')
    ax3.set_title('C. Tuition vs\nCompletion', loc='left', fontweight='bold')

    # Panel 4: Admission vs Completion
    ax4 = fig.add_subplot(gs[1, 2])
    admission = 20 + np.random.rand(8) * 60
    ax4.scatter(admission, completion, c=colors, s=100, alpha=0.7)
    ax4.set_xlabel('Admission Rate (%)')
    ax4.set_ylabel('Completion Rate (%)')
    ax4.set_title('D. Admission vs\nCompletion', loc='left', fontweight='bold')

    # Panel 5: Tuition comparison
    ax5 = fig.add_subplot(gs[2, :])
    tuition_sorted_idx = np.argsort(tuition)
    sorted_institutions = [institutions_subset[i] for i in tuition_sorted_idx]
    sorted_tuition = tuition[tuition_sorted_idx]
    sorted_colors = [colors[i] for i in tuition_sorted_idx]
    ax5.barh(range(len(sorted_institutions)), sorted_tuition, color=sorted_colors)
    ax5.set_yticks(range(len(sorted_institutions)))
    ax5.set_yticklabels(sorted_institutions)
    ax5.set_xlabel('In-State Tuition ($)')
    ax5.set_title('E. In-State Tuition Comparison', loc='left', fontweight='bold')

    fig.suptitle('Big Ten Conference Overview', fontsize=14, fontweight='bold', y=0.995)
    save_plot('conference_dashboard.png', 'bigten')


def main():
    """Generate all gallery images."""
    print("=" * 60)
    print("Generating Gallery Images for MSUthemes Documentation")
    print("=" * 60)

    try:
        generate_basic_plots()
        generate_msu_plots()
        generate_bigten_plots()

        print("\n" + "=" * 60)
        print("SUCCESS: All gallery images generated!")
        print("=" * 60)
        print(f"\nImages saved to: {OUTPUT_DIR}")
        print("\nNext steps:")
        print("1. Review the generated images")
        print("2. Update gallery markdown files to include images")
        print("3. Rebuild documentation: mkdocs build")

    except Exception as e:
        print(f"\nERROR: Failed to generate images: {e}")
        import traceback
        traceback.print_exc()
        sys.exit(1)


if __name__ == '__main__':
    main()
