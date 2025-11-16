"""Data loading utilities for MSUthemes.

This module provides functions to load datasets bundled with the package.

Functions:
    load_bigten_data: Load BigTen institutional dataset
    get_data_path: Get path to data directory
    list_available_datasets: List all available datasets

Examples:
    >>> from msuthemes.data import load_bigten_data
    >>> import pandas as pd
    >>>
    >>> # Load complete dataset
    >>> df = load_bigten_data()
    >>>
    >>> # Filter for MSU
    >>> msu_data = df[df['name'] == 'MSU']
    >>>
    >>> # Get specific year
    >>> data_2020 = df[df['entry_term'] == 2020]
"""

import pandas as pd
from pathlib import Path
from typing import Optional, List
import warnings


def get_data_path() -> Path:
    """Get the path to the data directory.

    Returns:
        Path object pointing to the data directory

    Examples:
        >>> data_path = get_data_path()
        >>> print(data_path)
        PosixPath('.../msuthemes/data')
    """
    return Path(__file__).parent


def list_available_datasets() -> List[str]:
    """List all available datasets.

    Returns:
        List of dataset filenames

    Examples:
        >>> datasets = list_available_datasets()
        >>> print(datasets)
        ['BigTen.csv']
    """
    data_dir = get_data_path()
    if not data_dir.exists():
        return []

    return sorted([
        f.name for f in data_dir.glob("*.csv")
    ])


def load_bigten_data(
    institutions: Optional[List[str]] = None,
    years: Optional[List[int]] = None,
    columns: Optional[List[str]] = None
) -> pd.DataFrame:
    """Load BigTen institutional historical dataset (1996-2023).

    This dataset contains historical data from the College Scorecard for
    all 18 Big Ten Conference institutions from 1996 to 2023.

    Args:
        institutions: Filter for specific institutions (default: all 18)
        years: Filter for specific years (default: all years 1996-2023)
        columns: Select specific columns (default: all columns)

    Returns:
        pandas DataFrame with BigTen institutional data

    Raises:
        FileNotFoundError: If BigTen.csv is not found
        ValueError: If invalid institutions or years specified

    Dataset Information:
        - 504 rows (18 institutions × 28 years)
        - 38 columns including:
          * Institutional characteristics (public/private, land-grant, AAU)
          * Enrollment data (total, by gender, by race/ethnicity)
          * Admission rates
          * Completion rates
          * Tuition and fees
          * Cost of attendance
          * Pell grant recipients

    Examples:
        >>> # Load all data
        >>> df = load_bigten_data()
        >>> print(df.shape)
        (504, 38)

        >>> # Filter for specific institutions
        >>> df_msu_um = load_bigten_data(institutions=['MSU', 'Michigan'])
        >>> print(df_msu_um['name'].unique())
        ['MSU', 'Michigan']

        >>> # Filter for specific years
        >>> df_recent = load_bigten_data(years=[2020, 2021, 2022, 2023])
        >>> print(len(df_recent))
        72

        >>> # Select specific columns
        >>> df_small = load_bigten_data(
        ...     institutions=['MSU'],
        ...     columns=['name', 'entry_term', 'UGDS', 'ADM_RATE']
        ... )

        >>> # MSU enrollment over time
        >>> msu_data = load_bigten_data(institutions=['MSU'])
        >>> print(msu_data[['entry_term', 'UGDS']].head())
    """
    # Get data file path
    data_path = get_data_path() / "BigTen.csv"

    if not data_path.exists():
        raise FileNotFoundError(
            f"BigTen dataset not found at {data_path}. "
            "Please ensure the package was installed correctly."
        )

    # Load the dataset
    try:
        df = pd.read_csv(data_path)
    except Exception as e:
        raise IOError(f"Error loading BigTen dataset: {e}")

    # Validate and filter institutions
    if institutions is not None:
        # Normalize institution names
        from msuthemes.bigten import normalize_institution_name

        normalized_institutions = []
        for inst in institutions:
            try:
                normalized = normalize_institution_name(inst)
                # Handle USC/USoCal difference
                if normalized == "USC":
                    normalized = "USoCal"
                normalized_institutions.append(normalized)
            except ValueError as e:
                warnings.warn(f"Skipping invalid institution '{inst}': {e}")

        if normalized_institutions:
            df = df[df['name'].isin(normalized_institutions)]
        else:
            raise ValueError("No valid institutions specified")

    # Filter years
    if years is not None:
        years = [int(y) for y in years]  # Ensure integers
        min_year, max_year = df['entry_term'].min(), df['entry_term'].max()

        # Validate years
        invalid_years = [y for y in years if y < min_year or y > max_year]
        if invalid_years:
            warnings.warn(
                f"Years {invalid_years} are outside the dataset range "
                f"({min_year:.0f}-{max_year:.0f}). These will be ignored."
            )

        df = df[df['entry_term'].isin(years)]

    # Select columns
    if columns is not None:
        # Validate columns
        invalid_cols = [c for c in columns if c not in df.columns]
        if invalid_cols:
            raise ValueError(
                f"Invalid columns: {invalid_cols}. "
                f"Available columns: {list(df.columns)}"
            )
        df = df[columns]

    # Reset index
    df = df.reset_index(drop=True)

    return df


def get_bigten_summary() -> pd.DataFrame:
    """Get summary statistics for the BigTen dataset.

    Returns:
        DataFrame with summary statistics by institution

    Examples:
        >>> summary = get_bigten_summary()
        >>> print(summary.head())
    """
    df = load_bigten_data()

    summary = df.groupby('name').agg({
        'entry_term': ['min', 'max', 'count'],
        'UGDS': ['mean', 'min', 'max'],
        'ADM_RATE': 'mean',
        'C150_4': 'mean',
    }).round(4)

    summary.columns = ['_'.join(col).strip() for col in summary.columns.values]

    return summary.reset_index()


def get_dataset_info() -> dict:
    """Get information about the BigTen dataset.

    Returns:
        Dictionary with dataset information

    Examples:
        >>> info = get_dataset_info()
        >>> print(info['n_institutions'])
        18
        >>> print(info['years'])
        (1996, 2023)
    """
    try:
        df = load_bigten_data()

        return {
            'n_rows': len(df),
            'n_columns': len(df.columns),
            'n_institutions': df['name'].nunique(),
            'institutions': sorted(df['name'].unique().tolist()),
            'years': (int(df['entry_term'].min()), int(df['entry_term'].max())),
            'n_years': df['entry_term'].nunique(),
            'columns': df.columns.tolist(),
        }
    except FileNotFoundError:
        return {
            'error': 'Dataset not found',
            'message': 'BigTen.csv is not available in the data directory'
        }


__all__ = [
    "load_bigten_data",
    "get_data_path",
    "list_available_datasets",
    "get_bigten_summary",
    "get_dataset_info",
]
