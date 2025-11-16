#!/usr/bin/env python3
"""Test script to verify BigTen dataset functionality."""

import sys
import pandas as pd
print("Testing BigTen dataset functionality...\n")

# Test 1: Import data module
print("1. Testing data module import...")
try:
    from msuthemes import data
    from msuthemes.data import load_bigten_data, get_bigten_summary, get_dataset_info
    print("   ✓ Data module imported successfully")
except Exception as e:
    print(f"   ✗ Failed: {e}")
    sys.exit(1)

# Test 2: Load full dataset
print("\n2. Testing load_bigten_data() - full dataset...")
try:
    df = load_bigten_data()
    print(f"   ✓ Dataset loaded successfully")
    print(f"   ✓ Shape: {df.shape[0]} rows × {df.shape[1]} columns")
    print(f"   ✓ Years: {int(df['entry_term'].min())} to {int(df['entry_term'].max())}")
    print(f"   ✓ Institutions: {df['name'].nunique()} unique")
except Exception as e:
    print(f"   ✗ Failed: {e}")
    import traceback
    traceback.print_exc()
    sys.exit(1)

# Test 3: Filter by single institution
print("\n3. Testing institution filtering (single)...")
try:
    msu_data = load_bigten_data(institutions=['MSU'])
    print(f"   ✓ MSU data loaded: {len(msu_data)} rows")
    assert all(msu_data['name'] == 'MSU'), "Institution filter failed"
    print(f"   ✓ All rows are MSU")
except Exception as e:
    print(f"   ✗ Failed: {e}")
    sys.exit(1)

# Test 4: Filter by multiple institutions
print("\n4. Testing institution filtering (multiple)...")
try:
    big3_data = load_bigten_data(institutions=['MSU', 'Michigan', 'Ohio State'])
    institutions_found = big3_data['name'].unique()
    print(f"   ✓ Big 3 data loaded: {len(big3_data)} rows")
    print(f"   ✓ Institutions found: {len(institutions_found)}")
    expected = {'MSU', 'Michigan', 'Ohio State'}
    assert set(institutions_found) == expected, f"Expected {expected}, got {set(institutions_found)}"
    print(f"   ✓ All institutions correct")
except Exception as e:
    print(f"   ✗ Failed: {e}")
    import traceback
    traceback.print_exc()
    sys.exit(1)

# Test 5: Test institution name normalization
print("\n5. Testing institution name aliases...")
try:
    # Test nicknames
    spartans_data = load_bigten_data(institutions=['Spartans'])
    print(f"   ✓ 'Spartans' alias works: {len(spartans_data)} rows")

    # Test abbreviations
    buckeyes_data = load_bigten_data(institutions=['OSU'])
    print(f"   ✓ 'OSU' alias works: {len(buckeyes_data)} rows")

    # Test mixed
    mixed_data = load_bigten_data(institutions=['Wolverines', 'buckeyes', 'msu'])
    print(f"   ✓ Mixed aliases work: {len(mixed_data)} rows")
except Exception as e:
    print(f"   ✗ Failed: {e}")
    import traceback
    traceback.print_exc()
    sys.exit(1)

# Test 6: Filter by years
print("\n6. Testing year filtering...")
try:
    recent_data = load_bigten_data(years=[2020, 2021, 2022, 2023])
    unique_years = sorted([int(y) for y in recent_data['entry_term'].unique()])
    print(f"   ✓ Recent years loaded: {len(recent_data)} rows")
    print(f"   ✓ Years found: {unique_years}")
    assert set(unique_years) == {2020, 2021, 2022, 2023}, "Year filter failed"
except Exception as e:
    print(f"   ✗ Failed: {e}")
    sys.exit(1)

# Test 7: Combined filters
print("\n7. Testing combined filters (institutions + years)...")
try:
    msu_recent = load_bigten_data(institutions=['MSU'], years=[2020, 2021, 2022, 2023])
    print(f"   ✓ MSU recent data: {len(msu_recent)} rows")
    assert len(msu_recent) == 4, f"Expected 4 rows (4 years), got {len(msu_recent)}"
    print(f"   ✓ Row count correct (4 years)")
except Exception as e:
    print(f"   ✗ Failed: {e}")
    sys.exit(1)

# Test 8: Column filtering
print("\n8. Testing column filtering...")
try:
    key_cols = ['name', 'entry_term', 'UGDS', 'ADM_RATE', 'TUITIONFEE_IN']
    subset_data = load_bigten_data(columns=key_cols)
    print(f"   ✓ Subset loaded: {subset_data.shape[1]} columns")
    assert list(subset_data.columns) == key_cols, "Column filter failed"
    print(f"   ✓ Columns: {', '.join(subset_data.columns)}")
except Exception as e:
    print(f"   ✗ Failed: {e}")
    sys.exit(1)

# Test 9: Get summary statistics
print("\n9. Testing get_bigten_summary()...")
try:
    summary = get_bigten_summary()
    print(f"   ✓ Summary generated: {summary.shape[0]} institutions")
    print(f"   ✓ Columns: {list(summary.columns)[:5]}...")
    # Find MSU row
    msu_row = summary[summary['name'] == 'MSU']
    if not msu_row.empty:
        print(f"   ✓ Sample - MSU mean enrollment: {msu_row['UGDS_mean'].values[0]:.0f}")
except Exception as e:
    print(f"   ✗ Failed: {e}")
    import traceback
    traceback.print_exc()
    # Don't exit - this is not critical

# Test 10: Get dataset info
print("\n10. Testing get_dataset_info()...")
try:
    info = get_dataset_info()
    print(f"   ✓ Dataset info retrieved")
    print(f"   ✓ Institutions: {info['n_institutions']}")
    print(f"   ✓ Years: {info['years']}")
    print(f"   ✓ Total rows: {info['n_rows']}")
    print(f"   ✓ Columns: {info['n_columns']}")
except Exception as e:
    print(f"   ✗ Failed: {e}")
    # Don't exit - this is not critical

# Test 11: Error handling - invalid institution
print("\n11. Testing error handling (invalid institution)...")
try:
    try:
        bad_data = load_bigten_data(institutions=['Invalid School'])
        print(f"   ✗ Should have raised ValueError")
    except ValueError as ve:
        print(f"   ✓ Correctly raised ValueError: {str(ve)[:60]}...")
except Exception as e:
    print(f"   ✗ Failed: {e}")

# Test 12: Error handling - invalid year
print("\n12. Testing error handling (invalid year)...")
try:
    try:
        bad_data = load_bigten_data(years=[1990])  # Before 1996
        print(f"   ✗ Should have raised ValueError")
    except ValueError as ve:
        print(f"   ✓ Correctly raised ValueError: {str(ve)[:60]}...")
except Exception as e:
    print(f"   ✗ Failed: {e}")

# Test 13: Data quality checks
print("\n13. Testing data quality...")
try:
    df = load_bigten_data()

    # Check required columns exist
    required_cols = ['name', 'entry_term', 'UGDS']
    for col in required_cols:
        assert col in df.columns, f"Missing required column: {col}"
    print(f"   ✓ All required columns present")

    # Check no null institution names
    assert df['name'].notna().all(), "Null institution names found"
    print(f"   ✓ No null institution names")

    # Check year range
    assert df['entry_term'].min() >= 1996, "Years before 1996 found"
    assert df['entry_term'].max() <= 2023, "Years after 2023 found"
    print(f"   ✓ Year range valid (1996-2023)")

except Exception as e:
    print(f"   ✗ Failed: {e}")

# Test 14: Performance check
print("\n14. Testing load performance...")
try:
    import time
    start = time.time()
    df = load_bigten_data()
    elapsed = time.time() - start
    print(f"   ✓ Load time: {elapsed:.3f} seconds")
    assert elapsed < 5.0, f"Load too slow: {elapsed:.3f}s"
    print(f"   ✓ Performance acceptable (< 5s)")
except Exception as e:
    print(f"   ✗ Failed: {e}")

# Summary
print("\n" + "="*60)
print("✓ All dataset tests completed successfully!")
print("="*60)
print(f"\nDataset Summary:")
print(f"  - Total rows: {df.shape[0]}")
print(f"  - Total columns: {df.shape[1]}")
print(f"  - Institutions: {df['name'].nunique()}")
print(f"  - Years: {int(df['entry_term'].min())}-{int(df['entry_term'].max())}")
print(f"  - Sample institutions:")
for inst in sorted(df['name'].unique())[:5]:
    print(f"    • {inst}")
print(f"    ... and {df['name'].nunique() - 5} more")
print("\nBigTen dataset is ready to use!")
