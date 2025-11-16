"""Data loading utilities for MSUthemes.

This module provides functions to load datasets bundled with the package.

Functions:
    load_bigten_data: Load BigTen institutional dataset

Examples:
    >>> from msuthemes.data import load_bigten_data
    >>> import pandas as pd
    >>>
    >>> df = load_bigten_data()
    >>> msu_data = df[df['name'] == 'MSU']
"""

import pandas as pd
from pathlib import Path
from typing import Optional

# TODO: Phase 6 - Implement data loading functions
# - load_bigten_data()
# - Data validation
# - Error handling

__all__ = []
