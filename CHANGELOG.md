# Changelog

All notable changes to MSUthemes will be documented in this file.

The format is based on [Keep a Changelog](https://keepachangelog.com/en/1.0.0/),
and this project adheres to [Semantic Versioning](https://semver.org/spec/v2.0.0.html).

## [0.1.0] - 2025-01-16

### Added

#### Core Functionality
- **Colors Module**: MSU official colors and Big Ten institutional colors for all 18 institutions
- **Palettes Module**: 11 professionally designed color palettes (sequential, diverging, qualitative)
- **Fonts Module**: Bundled Metropolis font with 9 weights and italic variants
- **Themes Module**: matplotlib and seaborn theme functions with MSU branding
- **Big Ten Module**: Institutional color utilities with 80+ name aliases
- **Data Module**: BigTen dataset (1996-2023) with comprehensive loading and filtering
- **Utils Module**: Color conversion and manipulation utilities

#### Features
- `theme_msu()` - Apply MSU theme to matplotlib with extensive customization options
- `set_msu_style()` - Seaborn integration with MSU styling
- `get_bigten_colors()` - Get institutional colors with flexible name recognition
- `bigten_palette()` - Create color palettes from Big Ten colors
- `load_bigten_data()` - Load and filter BigTen institutional dataset
- `MSUPalette` class - Advanced palette generation with interpolation
- Metropolis font automatic registration with matplotlib
- Color brightness calculation and manipulation (lighten/darken)
- 18 Big Ten institutions with primary and secondary colors

#### Documentation
- Comprehensive Sphinx documentation with RTD theme
- Installation guide with platform-specific instructions
- Quickstart guide with practical examples
- Complete API reference for all modules
- Gallery of visualization examples
- Migration guide for R package users
- Contributing guidelines
- Changelog and license documentation

#### Testing
- 170+ comprehensive tests across all modules
- Unit tests for colors, palettes, fonts, themes, Big Ten, data, utilities
- Integration tests for complete workflows
- pytest configuration with markers and coverage
- Test coverage reporting (HTML, XML, terminal)
- Shared fixtures for common test scenarios

#### Examples
- 6 comprehensive example scripts covering all features
- Interactive Jupyter notebook tutorial
- Basic usage examples for beginners
- Big Ten institutional comparisons
- Palette showcase and applications
- Seaborn integration examples
- Data visualization dashboard
- Advanced customization techniques
- Comprehensive examples documentation

#### Dataset
- BigTen institutional data (1996-2023)
- 504 rows × 38 columns
- 18 Big Ten institutions
- Enrollment, admission, completion, tuition, demographics
- Source: U.S. Department of Education College Scorecard

### Documentation URLs
- Homepage: https://github.com/emilioxavier/msuthemes-py
- Documentation: https://emilioxavier.github.io/msuthemes-py/
- Repository: https://github.com/emilioxavier/msuthemes-py
- Bug Tracker: https://github.com/emilioxavier/msuthemes-py/issues
- Original R Package: https://cran.r-project.org/package=MSUthemes

### Dependencies
- Python >= 3.8
- matplotlib >= 3.5.0
- numpy >= 1.20.0
- pandas >= 1.3.0
- seaborn >= 0.12.0 (optional)
- plotly >= 5.0.0 (optional, planned)

### License
- Creative Commons Attribution-ShareAlike 4.0 International (CC BY-SA 4.0)
- Metropolis font: SIL Open Font License (OFL)
- BigTen dataset: Public domain (U.S. Department of Education)

---

## [Unreleased]

### Planned
- Plotly theme support
- Additional color palettes
- Interactive palette picker
- More dataset utilities
- Extended documentation
- Community contributions

---

**Note**: This is an alpha release (0.1.0). The API may change in future versions.
For the most up-to-date information, visit the [documentation](https://emilioxavier.github.io/msuthemes-py/).
