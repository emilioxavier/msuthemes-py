# data

The `data` module provides access to the Big Ten dataset from the College Scorecard.

## Module Overview

This module provides:

- Big Ten College Scorecard data (1996-2023)
- Flexible data loading with filtering
- Dataset summary and metadata functions
- 38 variables covering enrollment, admissions, completion, tuition, and demographics

## Functions

::: msuthemes.data.load_bigten_data

::: msuthemes.data.get_bigten_summary

::: msuthemes.data.get_dataset_info

::: msuthemes.data.list_available_datasets

## Usage Examples

### Basic Data Loading

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

# Load data for single institution
msu_data = load_bigten_data(institutions=['Michigan State'])

# Load data for multiple institutions
rivalry = load_bigten_data(
    institutions=['Michigan State', 'Michigan', 'Ohio State']
)

# Using abbreviations
msu_data = load_bigten_data(institutions=['MSU'])
```

### Filtering by Year

```python
from msuthemes import load_bigten_data

# Load specific years
recent = load_bigten_data(years=[2020, 2021, 2022, 2023])

# Load year range
decade = load_bigten_data(years=list(range(2010, 2020)))

# Load single year
df_2023 = load_bigten_data(years=[2023])
```

### Filtering by Columns

```python
from msuthemes import load_bigten_data

# Load specific columns
df = load_bigten_data(
    columns=['INSTNM', 'YEAR', 'ADM_RATE', 'UGDS']
)

# Combine filters
msu_recent = load_bigten_data(
    institutions=['Michigan State'],
    years=list(range(2015, 2024)),
    columns=['YEAR', 'ADM_RATE', 'C150_4']
)
```

### Getting Dataset Summary

```python
from msuthemes import get_bigten_summary

# Get summary statistics
summary = get_bigten_summary()
print(summary)
```

### Getting Dataset Information

```python
from msuthemes import get_dataset_info

# Get metadata
info = get_dataset_info()
print(info['description'])
print(info['source'])
print(info['years'])
print(info['institutions'])
```

### Listing Available Datasets

```python
from msuthemes import list_available_datasets

# List all datasets
datasets = list_available_datasets()
print(datasets)
```

## Complete Analysis Example

```python
from msuthemes import (
    load_bigten_data,
    bigten_palette,
    theme_msu
)
import matplotlib.pyplot as plt

# Apply theme
theme_msu(grid=True)

# Load and filter data
schools = ['Michigan State', 'Michigan', 'Wisconsin']
df = load_bigten_data(
    institutions=schools,
    years=list(range(2010, 2024)),
    columns=['INSTNM', 'YEAR', 'ADM_RATE']
)

# Get colors
colors = bigten_palette(schools)

# Plot
fig, ax = plt.subplots(figsize=(10, 6))

for school, color in zip(schools, colors):
    school_data = df[df['INSTNM'] == school]
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

plt.tight_layout()
plt.show()
```

## Dataset Variables

### Institution Identifiers
- `UNITID`: Unique institution ID
- `INSTNM`: Institution name
- `YEAR`: Academic year

### Enrollment
- `UGDS`: Total undergraduate enrollment
- `UG`: Number of undergraduates
- `GRAD`: Number of graduates

### Admissions
- `ADM_RATE`: Admission rate (0-1)
- `ADM_RATE_ALL`: Overall admission rate
- `SATVRMID`, `SATMTMID`, `SATWRMID`: SAT score midpoints
- `ACTCMMID`, `ACTENMID`, `ACTMTMID`, `ACTWRMID`: ACT score midpoints

### Completion
- `C150_4`: 6-year completion rate (0-1)
- `C200_4`: 8-year completion rate (0-1)

### Costs
- `TUITIONFEE_IN`: In-state tuition and fees
- `TUITIONFEE_OUT`: Out-of-state tuition and fees
- `TUITIONFEE_PROG`: Program tuition

### Demographics
- `UGDS_WHITE`: % White undergraduates
- `UGDS_BLACK`: % Black undergraduates
- `UGDS_HISP`: % Hispanic undergraduates
- `UGDS_ASIAN`: % Asian undergraduates
- `UGDS_AIAN`: % American Indian/Alaska Native
- `UGDS_NHPI`: % Native Hawaiian/Pacific Islander
- `UGDS_2MOR`: % Two or more races
- `UGDS_NRA`: % Non-resident aliens
- `UGDS_UNKN`: % Race/ethnicity unknown

### Financial Aid
- `PCTPELL`: % receiving Pell Grants
- `PCTFLOAN`: % receiving federal loans

### Institution Characteristics
- `CONTROL`: Public/private control
- `HIGHDEG`: Highest degree awarded
- `REGION`: Geographic region
- `LOCALE`: Urban/rural classification

## Data Quality Notes

- Missing values exist for some variables/years
- Institution names match `list_bigten_institutions()`
- Data sourced from U.S. Department of Education College Scorecard
- Updated through 2023

## Working with Missing Data

```python
from msuthemes import load_bigten_data
import pandas as pd

# Load data
df = load_bigten_data()

# Check missing values
print(df.isnull().sum())

# Drop rows with missing values in specific column
df_clean = df.dropna(subset=['ADM_RATE'])

# Fill missing values with mean
df_filled = df.fillna(df.mean(numeric_only=True))
```

## See Also

- [Dataset Guide](../guide/datasets.md) - Detailed dataset usage guide
- [Big Ten](bigten.md) - Big Ten utilities
- [Gallery](../gallery/bigten.md) - Data visualization examples
