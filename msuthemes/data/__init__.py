"""Data module for MSUthemes.

This module provides access to datasets bundled with the package.

Main Dataset:
    BigTen: Historical data (1996-2023) for all 18 Big Ten Conference institutions
            from the College Scorecard, including enrollment, admission rates,
            completion rates, tuition, and demographic information.

Functions:
    load_bigten_data: Load BigTen institutional dataset
    get_bigten_summary: Get summary statistics
    get_dataset_info: Get dataset information

Examples:
    >>> from msuthemes.data import load_bigten_data
    >>>
    >>> # Load all data
    >>> df = load_bigten_data()
    >>>
    >>> # Filter for MSU
    >>> msu_data = load_bigten_data(institutions=['MSU'])
    >>>
    >>> # Recent years only
    >>> recent = load_bigten_data(years=[2020, 2021, 2022, 2023])
"""

from .data_loader import (
    load_bigten_data,
    get_data_path,
    list_available_datasets,
    get_bigten_summary,
    get_dataset_info,
)

__all__ = [
    "load_bigten_data",
    "get_data_path",
    "list_available_datasets",
    "get_bigten_summary",
    "get_dataset_info",
]
