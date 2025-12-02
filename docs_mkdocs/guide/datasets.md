# Datasets

MSUthemes includes a curated dataset of Big Ten Conference institutions from the U.S. Department of Education's College Scorecard. This dataset enables comparative analyses and visualizations across the conference.

## Overview

The Big Ten dataset includes:

- **Time Period**: 1996-2023 (28 years)
- **Institutions**: All 18 Big Ten schools
- **Variables**: 38 metrics including enrollment, admissions, completion rates, tuition, and demographics
- **Total Observations**: 504 rows (18 institutions × 28 years)

## Loading Data

### Basic Loading

```python
from msuthemes import load_bigten_data

# Load complete dataset
df = load_bigten_data()
print(df.shape)  # (504, 38)
print(df.columns)
```

### Filtering by Institution

```python
from msuthemes import load_bigten_data

# Load data for a single institution
msu_data = load_bigten_data(institutions=['Michigan State'])

# Load data for multiple institutions
rivalry_data = load_bigten_data(
    institutions=['Michigan State', 'Michigan', 'Ohio State']
)

# Using abbreviations works too
msu_data = load_bigten_data(institutions=['MSU'])
```

### Filtering by Year

```python
from msuthemes import load_bigten_data

# Load recent years only
recent_data = load_bigten_data(years=[2020, 2021, 2022, 2023])

# Load a specific year range
decade_data = load_bigten_data(years=list(range(2010, 2020)))
```

### Filtering by Columns

```python
from msuthemes import load_bigten_data

# Load only specific columns
focused_data = load_bigten_data(
    columns=['INSTNM', 'YEAR', 'ADM_RATE', 'UGDS', 'TUITIONFEE_IN']
)

# Combine filters
msu_recent = load_bigten_data(
    institutions=['Michigan State'],
    years=list(range(2015, 2024)),
    columns=['YEAR', 'ADM_RATE', 'UGDS']
)
```

## Dataset Variables

### Institution Identifiers

- `UNITID`: Unique institution identifier
- `INSTNM`: Institution name
- `YEAR`: Academic year

### Enrollment Metrics

- `UGDS`: Total undergraduate enrollment
- `UG`: Number of undergraduates
- `GRAD`: Number of graduate students

### Admissions

- `ADM_RATE`: Admission rate (0-1)
- `ADM_RATE_ALL`: Overall admission rate
- `SATVRMID`: SAT verbal midpoint
- `SATMTMID`: SAT math midpoint
- `SATWRMID`: SAT writing midpoint
- `ACTCMMID`: ACT cumulative midpoint
- `ACTENMID`: ACT English midpoint
- `ACTMTMID`: ACT math midpoint
- `ACTWRMID`: ACT writing midpoint

### Completion Rates

- `C150_4`: 150% completion rate (6 years for 4-year programs)
- `C200_4`: 200% completion rate (8 years)

### Tuition and Costs

- `TUITIONFEE_IN`: In-state tuition and fees
- `TUITIONFEE_OUT`: Out-of-state tuition and fees
- `TUITIONFEE_PROG`: Program-specific tuition

### Student Body Demographics

- `UGDS_WHITE`: Percentage of white undergraduates
- `UGDS_BLACK`: Percentage of Black undergraduates
- `UGDS_HISP`: Percentage of Hispanic undergraduates
- `UGDS_ASIAN`: Percentage of Asian undergraduates
- `UGDS_AIAN`: Percentage of American Indian/Alaska Native undergraduates
- `UGDS_NHPI`: Percentage of Native Hawaiian/Pacific Islander undergraduates
- `UGDS_2MOR`: Percentage of two or more races undergraduates
- `UGDS_NRA`: Percentage of non-resident alien undergraduates
- `UGDS_UNKN`: Percentage of race/ethnicity unknown undergraduates

### Financial Aid

- `PCTPELL`: Percentage of students receiving Pell Grants
- `PCTFLOAN`: Percentage of students receiving federal loans

### Institutional Characteristics

- `CONTROL`: Institution control (public/private)
- `HIGHDEG`: Highest degree awarded
- `REGION`: Geographic region
- `LOCALE`: Urban/rural classification

## Dataset Information

### Get Summary Statistics

```python
from msuthemes import get_bigten_summary

# Get summary of the dataset
summary = get_bigten_summary()
print(summary)
```

### Get Dataset Metadata

```python
from msuthemes import get_dataset_info

# Get information about the dataset
info = get_dataset_info()
print(info['description'])
print(info['source'])
print(info['years'])
print(info['institutions'])
```

### List Available Datasets

```python
from msuthemes import list_available_datasets

# List all available datasets (currently just BigTen.csv)
datasets = list_available_datasets()
print(datasets)
```

## Analysis Examples

### Admission Rate Trends

```python
from msuthemes import load_bigten_data, bigten_palette, theme_msu
import matplotlib.pyplot as plt

# Setup
theme_msu()

# Load data
df = load_bigten_data(columns=['INSTNM', 'YEAR', 'ADM_RATE'])

# Filter to recent years and select schools
schools = ['Michigan State', 'Michigan', 'Wisconsin']
df_filtered = df[
    (df['INSTNM'].isin(schools)) &
    (df['YEAR'] >= 2010)
]

# Plot
colors = bigten_palette(schools)
fig, ax = plt.subplots(figsize=(10, 6))

for school, color in zip(schools, colors):
    school_data = df_filtered[df_filtered['INSTNM'] == school]
    ax.plot(school_data['YEAR'],
            school_data['ADM_RATE'] * 100,
            color=color,
            linewidth=2.5,
            marker='o',
            label=school)

ax.set_xlabel('Year')
ax.set_ylabel('Admission Rate (%)')
ax.set_title('Admission Rate Trends')
ax.legend()
ax.grid(True, alpha=0.3)

plt.tight_layout()
plt.show()
```

### Enrollment Comparison

```python
from msuthemes import load_bigten_data, bigten_palette, theme_msu
import matplotlib.pyplot as plt

# Setup
theme_msu()

# Load most recent year
df = load_bigten_data(years=[2023], columns=['INSTNM', 'UGDS'])

# Sort by enrollment
df_sorted = df.sort_values('UGDS', ascending=True)

# Get colors
colors = bigten_palette(df_sorted['INSTNM'].tolist())

# Create horizontal bar chart
fig, ax = plt.subplots(figsize=(10, 8))
ax.barh(range(len(df_sorted)),
        df_sorted['UGDS'],
        color=colors)
ax.set_yticks(range(len(df_sorted)))
ax.set_yticklabels(df_sorted['INSTNM'])
ax.set_xlabel('Undergraduate Enrollment')
ax.set_title('Big Ten Enrollment (2023)')

plt.tight_layout()
plt.show()
```

### Tuition Analysis

```python
from msuthemes import load_bigten_data, msu_qual1, theme_msu
import matplotlib.pyplot as plt
import numpy as np

# Setup
theme_msu()

# Load data
df = load_bigten_data(
    years=[2023],
    columns=['INSTNM', 'TUITIONFEE_IN', 'TUITIONFEE_OUT']
)

# Calculate difference
df['DIFF'] = df['TUITIONFEE_OUT'] - df['TUITIONFEE_IN']
df_sorted = df.sort_values('DIFF', ascending=False)

# Plot
fig, ax = plt.subplots(figsize=(10, 8))
colors = msu_qual1.as_hex()

x = np.arange(len(df_sorted))
width = 0.35

ax.barh(x - width/2, df_sorted['TUITIONFEE_IN'],
        width, label='In-State', color=colors[0])
ax.barh(x + width/2, df_sorted['TUITIONFEE_OUT'],
        width, label='Out-of-State', color=colors[1])

ax.set_yticks(x)
ax.set_yticklabels(df_sorted['INSTNM'])
ax.set_xlabel('Tuition and Fees ($)')
ax.set_title('Tuition Comparison (2023)')
ax.legend()

plt.tight_layout()
plt.show()
```

### Completion Rate Analysis

```python
from msuthemes import load_bigten_data, bigten_palette, theme_msu
import matplotlib.pyplot as plt

# Setup
theme_msu()

# Load data
df = load_bigten_data(
    years=list(range(2015, 2024)),
    columns=['INSTNM', 'YEAR', 'C150_4']
)

# Calculate average by institution
avg_completion = df.groupby('INSTNM')['C150_4'].mean().sort_values(ascending=False)

# Get colors
colors = bigten_palette(avg_completion.index.tolist())

# Plot
fig, ax = plt.subplots(figsize=(10, 8))
ax.barh(range(len(avg_completion)),
        avg_completion.values * 100,
        color=colors)
ax.set_yticks(range(len(avg_completion)))
ax.set_yticklabels(avg_completion.index)
ax.set_xlabel('6-Year Completion Rate (%)')
ax.set_title('Average Completion Rates (2015-2023)')

plt.tight_layout()
plt.show()
```

### Demographics Visualization

```python
from msuthemes import load_bigten_data, msu_seq, theme_msu
import matplotlib.pyplot as plt

# Setup
theme_msu()

# Load demographics data
df = load_bigten_data(
    institutions=['Michigan State'],
    columns=['YEAR', 'UGDS_WHITE', 'UGDS_BLACK',
             'UGDS_HISP', 'UGDS_ASIAN']
)

# Filter to recent years
df_recent = df[df['YEAR'] >= 2010].sort_values('YEAR')

# Plot stacked area chart
colors = msu_seq.as_hex()
fig, ax = plt.subplots(figsize=(10, 6))

ax.fill_between(df_recent['YEAR'],
                0,
                df_recent['UGDS_WHITE'] * 100,
                label='White',
                color=colors[0],
                alpha=0.8)

ax.fill_between(df_recent['YEAR'],
                df_recent['UGDS_WHITE'] * 100,
                (df_recent['UGDS_WHITE'] + df_recent['UGDS_BLACK']) * 100,
                label='Black',
                color=colors[2],
                alpha=0.8)

ax.set_xlabel('Year')
ax.set_ylabel('Percentage of Undergraduates')
ax.set_title('MSU Undergraduate Demographics Over Time')
ax.legend()

plt.tight_layout()
plt.show()
```

## Data Quality Notes

- **Missing values**: Some variables have missing data for certain years
- **Consistency**: Institution names match those from `list_bigten_institutions()`
- **Updates**: Data reflects College Scorecard releases through 2023
- **Filtering**: Use pandas methods for additional data cleaning

## Working with Missing Data

```python
from msuthemes import load_bigten_data
import pandas as pd

# Load data
df = load_bigten_data()

# Check for missing values
print(df.isnull().sum())

# Drop rows with missing values in specific column
df_clean = df.dropna(subset=['ADM_RATE'])

# Fill missing values
df_filled = df.fillna(df.mean(numeric_only=True))
```

## Combining with External Data

The dataset can be merged with external data sources:

```python
from msuthemes import load_bigten_data
import pandas as pd

# Load Big Ten data
bigten_df = load_bigten_data()

# Your external data
external_df = pd.read_csv('my_data.csv')

# Merge on institution name and year
merged_df = pd.merge(
    bigten_df,
    external_df,
    left_on=['INSTNM', 'YEAR'],
    right_on=['Institution', 'Year'],
    how='inner'
)
```

## Tips and Best Practices

1. **Filter early**: Use function parameters to filter data at load time
2. **Check data types**: Ensure numeric columns are properly typed
3. **Handle missing data**: Check for and handle missing values appropriately
4. **Verify institution names**: Use `list_bigten_institutions()` for consistency
5. **Document sources**: Note that data comes from College Scorecard when publishing

## See Also

- [Big Ten](bigten.md) - Big Ten colors and palettes
- [Gallery](../gallery/bigten.md) - Big Ten visualization examples
- [API Reference](../api/data.md) - Data module documentation
