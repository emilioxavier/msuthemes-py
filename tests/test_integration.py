"""Integration tests for MSUthemes.

These tests verify that components work together correctly in complete workflows.
"""

import pytest
import matplotlib
import matplotlib.pyplot as plt
import numpy as np
from msuthemes import (
    theme_msu,
    set_msu_style,
    colors,
    palettes,
    get_bigten_colors,
    bigten_palette,
    load_bigten_data,
    register_metropolis_fonts,
)


class TestBasicPlottingWorkflow:
    """Test basic plotting workflows."""

    @pytest.mark.integration
    @pytest.mark.mpl
    def test_complete_plot_workflow(self, clean_matplotlib):
        """Test complete workflow: theme + colors + plot."""
        # Apply theme
        theme_msu()

        # Create plot
        fig, ax = plt.subplots()
        x = np.linspace(0, 10, 100)
        y = np.sin(x)

        ax.plot(x, y, color=colors.MSU_GREEN, linewidth=2)
        ax.set_xlabel('X')
        ax.set_ylabel('Y')
        ax.set_title('Test Plot')

        # Verify theme was applied
        assert matplotlib.rcParams['font.family'][0] == 'Metropolis'
        assert matplotlib.rcParams['font.size'] == 11.0

        plt.close(fig)

    @pytest.mark.integration
    @pytest.mark.mpl
    def test_multiple_series_with_palette(self, clean_matplotlib):
        """Test plotting multiple series with MSU palette."""
        theme_msu()

        fig, ax = plt.subplots()
        x = np.linspace(0, 10, 100)

        palette_colors = palettes.msu_qual1.as_hex(n_colors=3)

        for i, color in enumerate(palette_colors):
            y = np.sin(x + i)
            ax.plot(x, y, color=color, label=f'Series {i+1}')

        ax.legend()
        plt.close(fig)


class TestSeabornIntegration:
    """Test seaborn integration workflows."""

    @pytest.mark.integration
    @pytest.mark.mpl
    def test_seaborn_style_application(self, clean_matplotlib, sample_dataframe):
        """Test applying MSU style to seaborn."""
        import seaborn as sns

        set_msu_style(style='whitegrid')

        # Create seaborn plot
        fig, ax = plt.subplots()
        sns.scatterplot(data=sample_dataframe, x='value', y='value', ax=ax)

        # Verify style applied
        assert 'Metropolis' in matplotlib.rcParams['font.family']

        plt.close(fig)


class TestBigTenWorkflows:
    """Test Big Ten data and visualization workflows."""

    @pytest.mark.integration
    @pytest.mark.data
    def test_bigten_data_and_colors_workflow(self, clean_matplotlib):
        """Test loading BigTen data and plotting with institution colors."""
        theme_msu()

        # Load data
        schools = ['MSU', 'Michigan', 'Ohio State']
        data = load_bigten_data(
            institutions=schools,
            columns=['name', 'entry_term', 'UGDS']
        )

        # Get colors
        school_colors = get_bigten_colors(schools)

        # Create plot
        fig, ax = plt.subplots()

        for school in schools:
            school_data = data[data['name'] == school]
            if len(school_data) > 0:
                ax.plot(
                    school_data['entry_term'],
                    school_data['UGDS'],
                    label=school,
                    color=school_colors[school]
                )

        ax.legend()
        plt.close(fig)

    @pytest.mark.integration
    @pytest.mark.data
    def test_bigten_palette_workflow(self):
        """Test creating Big Ten palette and using it."""
        schools = ['MSU', 'Michigan', 'Ohio State', 'Penn State']

        # Get palette
        palette = bigten_palette(schools, as_palette=True)

        # Convert to colormap
        cmap = palette.as_matplotlib_cmap()

        assert cmap is not None
        assert cmap.N > 0

    @pytest.mark.integration
    @pytest.mark.data
    def test_bigten_comparison_plot(self, clean_matplotlib):
        """Test creating Big Ten comparison visualization."""
        theme_msu()

        # Load recent data
        data = load_bigten_data(
            years=[2023],
            columns=['name', 'ADM_RATE']
        )

        # Filter out NaN
        data = data.dropna(subset=['ADM_RATE'])

        # Sort
        data = data.sort_values('ADM_RATE', ascending=False)

        # Get colors
        colors_list = bigten_palette(data['name'].tolist()[:5])

        # Create plot
        fig, ax = plt.subplots()
        ax.barh(range(len(data[:5])), data['ADM_RATE'].values[:5] * 100, color=colors_list[:5])

        plt.close(fig)


class TestPaletteWorkflows:
    """Test palette-related workflows."""

    @pytest.mark.integration
    @pytest.mark.mpl
    def test_sequential_palette_heatmap(self, clean_matplotlib):
        """Test using sequential palette for heatmap."""
        import seaborn as sns

        set_msu_style()

        # Create data
        data = np.random.rand(10, 10)

        # Get colormap
        cmap = palettes.msu_seq.as_matplotlib_cmap()

        # Create heatmap
        fig, ax = plt.subplots()
        sns.heatmap(data, cmap=cmap, ax=ax)

        plt.close(fig)

    @pytest.mark.integration
    @pytest.mark.mpl
    def test_diverging_palette_heatmap(self, clean_matplotlib):
        """Test using diverging palette for heatmap."""
        import seaborn as sns

        set_msu_style()

        # Create data with positive and negative values
        data = np.random.randn(10, 10)

        # Get colormap
        cmap = palettes.msu_div.as_matplotlib_cmap()

        # Create heatmap
        fig, ax = plt.subplots()
        sns.heatmap(data, cmap=cmap, center=0, ax=ax)

        plt.close(fig)

    @pytest.mark.integration
    @pytest.mark.mpl
    def test_qualitative_palette_bar_chart(self, clean_matplotlib):
        """Test using qualitative palette for bar chart."""
        theme_msu()

        categories = ['A', 'B', 'C', 'D', 'E']
        values = [23, 45, 56, 32, 78]

        palette_colors = palettes.msu_qual1.as_hex()

        fig, ax = plt.subplots()
        ax.bar(categories, values, color=palette_colors[:len(categories)])

        plt.close(fig)


class TestFontWorkflows:
    """Test font-related workflows."""

    @pytest.mark.integration
    @pytest.mark.fonts
    def test_font_registration_and_use(self, clean_matplotlib):
        """Test registering fonts and using them."""
        # Register fonts
        success = register_metropolis_fonts()

        # Apply theme
        theme_msu()

        # Create plot
        fig, ax = plt.subplots()
        ax.text(0.5, 0.5, 'Test Text', fontsize=14, weight='bold')

        # Verify font family is set
        assert 'Metropolis' in matplotlib.rcParams['font.family']

        plt.close(fig)


class TestCompleteWorkflows:
    """Test complete, realistic workflows."""

    @pytest.mark.integration
    @pytest.mark.slow
    def test_complete_data_visualization_workflow(self, clean_matplotlib):
        """Test complete workflow: data + theme + colors + plot + save."""
        # 1. Apply theme
        theme_msu()

        # 2. Load data
        msu_data = load_bigten_data(
            institutions=['MSU'],
            columns=['entry_term', 'UGDS', 'ADM_RATE']
        )

        # 3. Create multi-panel figure
        fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(12, 5))

        # 4. Plot enrollment
        ax1.plot(
            msu_data['entry_term'],
            msu_data['UGDS'],
            color=colors.MSU_GREEN,
            linewidth=2,
            marker='o',
            markersize=4
        )
        ax1.set_xlabel('Year')
        ax1.set_ylabel('Enrollment')
        ax1.set_title('MSU Enrollment Over Time')

        # 5. Plot admission rate
        msu_clean = msu_data.dropna(subset=['ADM_RATE'])
        ax2.plot(
            msu_clean['entry_term'],
            msu_clean['ADM_RATE'] * 100,
            color=colors.MSU_ORANGE,
            linewidth=2,
            marker='s',
            markersize=4
        )
        ax2.set_xlabel('Year')
        ax2.set_ylabel('Admission Rate (%)')
        ax2.set_title('MSU Admission Rate Over Time')

        plt.tight_layout()
        plt.close(fig)

    @pytest.mark.integration
    @pytest.mark.slow
    def test_multi_institution_comparison_workflow(self, clean_matplotlib):
        """Test multi-institution comparison workflow."""
        theme_msu(use_grid=True)

        # Load data for multiple schools
        schools = ['MSU', 'Michigan', 'Ohio State', 'Penn State']
        data = load_bigten_data(
            institutions=schools,
            years=list(range(2015, 2024)),
            columns=['name', 'entry_term', 'UGDS']
        )

        # Get colors
        school_colors = get_bigten_colors(schools)

        # Create plot
        fig, ax = plt.subplots(figsize=(10, 6))

        for school in schools:
            school_data = data[data['name'] == school]
            ax.plot(
                school_data['entry_term'],
                school_data['UGDS'],
                label=school,
                color=school_colors[school],
                linewidth=2.5,
                marker='o'
            )

        ax.set_xlabel('Year')
        ax.set_ylabel('Total Enrollment')
        ax.set_title('Big Ten Enrollment Comparison (2015-2023)')
        ax.legend(loc='best')
        ax.grid(True, alpha=0.3)

        plt.tight_layout()
        plt.close(fig)


class TestErrorHandlingInWorkflows:
    """Test error handling in integrated workflows."""

    @pytest.mark.integration
    def test_invalid_institution_in_workflow(self):
        """Test that invalid institutions raise appropriate errors."""
        with pytest.raises(ValueError):
            data = load_bigten_data(institutions=['Invalid School'])

    @pytest.mark.integration
    def test_invalid_color_name_in_workflow(self):
        """Test that invalid color names raise errors."""
        with pytest.raises((ValueError, KeyError)):
            colors = get_bigten_colors(['NonexistentSchool'])


class TestCrossModuleIntegration:
    """Test integration across multiple modules."""

    @pytest.mark.integration
    def test_colors_palettes_integration(self):
        """Test that colors module integrates with palettes."""
        # MSU Green should be in sequential palette
        seq_colors = palettes.msu_seq.as_hex()

        # At least one should contain MSU Green or similar
        assert any(colors.MSU_GREEN.upper() in c.upper() for c in seq_colors)

    @pytest.mark.integration
    def test_bigten_colors_data_integration(self):
        """Test that Big Ten colors match institutions in dataset."""
        # Get institutions from data
        data = load_bigten_data(columns=['name'])
        data_institutions = set(data['name'].unique())

        # Get institutions from colors
        color_institutions = set(colors.BIGTEN_COLORS_PRIMARY.keys())

        # Should have significant overlap (accounting for name differences)
        assert len(data_institutions.intersection(color_institutions)) > 0

    @pytest.mark.integration
    @pytest.mark.mpl
    def test_theme_palette_integration(self, clean_matplotlib):
        """Test that theme and palettes work together."""
        theme_msu()

        # Get palette
        palette_colors = palettes.msu_qual1.as_hex(n_colors=5)

        # Create plot with palette
        fig, ax = plt.subplots()
        for i, color in enumerate(palette_colors):
            ax.bar(i, i+1, color=color)

        # Theme should still be applied
        assert 'Metropolis' in matplotlib.rcParams['font.family']

        plt.close(fig)
