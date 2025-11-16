Working with Datasets
=====================

MSUthemes includes the BigTen dataset with historical institutional data (1996-2023).

For API documentation, see :doc:`api/data`.

Dataset Overview
----------------

The BigTen dataset contains:

* **18 institutions**: All Big Ten Conference schools
* **28 years**: 1996-2023
* **38 variables**: Enrollment, admissions, finances, demographics
* **504 rows**: Complete time series for each institution

Data Source
^^^^^^^^^^^

Data comes from the U.S. Department of Education's College Scorecard:
https://collegescorecard.ed.gov/

Loading Data
------------

Basic Loading
^^^^^^^^^^^^^

.. code-block:: python

   from msuthemes import load_bigten_data

   # Load all data
   df = load_bigten_data()
   print(df.shape)  # (504, 38)

Filter by Institution
^^^^^^^^^^^^^^^^^^^^^

.. code-block:: python

   from msuthemes import load_bigten_data

   # Single institution
   msu_data = load_bigten_data(institutions=['MSU'])

   # Multiple institutions
   rivalry_data = load_bigten_data(
       institutions=['MSU', 'Michigan', 'Ohio State']
   )

Filter by Year
^^^^^^^^^^^^^^

.. code-block:: python

   from msuthemes import load_bigten_data

   # Recent years
   recent = load_bigten_data(years=[2020, 2021, 2022, 2023])

   # Specific time period
   period = load_bigten_data(years=list(range(2010, 2024)))

Combine Filters
^^^^^^^^^^^^^^^

.. code-block:: python

   from msuthemes import load_bigten_data

   # MSU in recent years
   msu_recent = load_bigten_data(
       institutions=['MSU'],
       years=[2020, 2021, 2022, 2023]
   )

Select Columns
^^^^^^^^^^^^^^

.. code-block:: python

   from msuthemes import load_bigten_data

   # Select specific variables
   subset = load_bigten_data(
       columns=['name', 'entry_term', 'UGDS', 'ADM_RATE', 'TUITIONFEE_IN']
   )

Dataset Variables
-----------------

Key Variables
^^^^^^^^^^^^^

* ``name``: Institution name
* ``entry_term``: Year
* ``UGDS``: Total undergraduate enrollment
* ``ADM_RATE``: Admission rate (0-1)
* ``C150_4``: 4-year completion rate
* ``TUITIONFEE_IN``: In-state tuition and fees
* ``TUITIONFEE_OUT``: Out-of-state tuition and fees
* ``PCTPELL``: Percentage receiving Pell grants

Demographic Variables
^^^^^^^^^^^^^^^^^^^^^

* ``UGDS_WHITE``: Percentage white students
* ``UGDS_BLACK``: Percentage Black students
* ``UGDS_HISP``: Percentage Hispanic students
* ``UGDS_ASIAN``: Percentage Asian students
* ``UGDS_MEN``: Percentage male students
* ``UGDS_WOMEN``: Percentage female students

Financial Variables
^^^^^^^^^^^^^^^^^^^

* ``TUITIONFEE_IN``: In-state tuition
* ``TUITIONFEE_OUT``: Out-of-state tuition
* ``ROOMBOARD_ON``: Room and board (on-campus)
* ``BOOKSUPPLY``: Books and supplies
* ``CoA.inState``: Cost of attendance (in-state)
* ``CoA.outState``: Cost of attendance (out-of-state)

Summary Statistics
------------------

Get Summary
^^^^^^^^^^^

.. code-block:: python

   from msuthemes import get_bigten_summary

   # Get summary by institution
   summary = get_bigten_summary()
   print(summary.head())

Dataset Info
^^^^^^^^^^^^

.. code-block:: python

   from msuthemes import get_dataset_info

   # Get metadata
   info = get_dataset_info()
   print(f"Institutions: {info['n_institutions']}")
   print(f"Years: {info['years']}")
   print(f"Variables: {info['n_columns']}")

Visualization Examples
----------------------

Enrollment Trends
^^^^^^^^^^^^^^^^^

.. code-block:: python

   import matplotlib.pyplot as plt
   from msuthemes import theme_msu, load_bigten_data, get_bigten_colors

   theme_msu()

   # Load data
   schools = ['MSU', 'Michigan', 'Ohio State']
   data = load_bigten_data(
       institutions=schools,
       columns=['name', 'entry_term', 'UGDS']
   )

   # Get colors
   colors = get_bigten_colors(schools)

   # Plot
   for school in schools:
       school_data = data[data['name'] == school]
       plt.plot(
           school_data['entry_term'],
           school_data['UGDS'],
           label=school,
           color=colors[school],
           linewidth=2
       )

   plt.xlabel('Year')
   plt.ylabel('Total Enrollment')
   plt.title('Big Ten Enrollment Trends')
   plt.legend()
   plt.show()

Admission Rates
^^^^^^^^^^^^^^^

.. code-block:: python

   import matplotlib.pyplot as plt
   from msuthemes import theme_msu, load_bigten_data, bigten_palette

   theme_msu()

   # Load 2023 data
   data = load_bigten_data(
       years=[2023],
       columns=['name', 'ADM_RATE']
   )

   # Sort by admission rate
   data = data.sort_values('ADM_RATE', ascending=False)

   # Get colors
   colors = bigten_palette(data['name'].tolist())

   # Plot
   plt.figure(figsize=(10, 8))
   plt.barh(data['name'], data['ADM_RATE'] * 100, color=colors)
   plt.xlabel('Admission Rate (%)')
   plt.title('Big Ten Admission Rates (2023)')
   plt.tight_layout()
   plt.show()

Demographic Composition
^^^^^^^^^^^^^^^^^^^^^^^

.. code-block:: python

   import matplotlib.pyplot as plt
   from msuthemes import theme_msu, load_bigten_data

   theme_msu()

   # Load MSU demographics over time
   msu = load_bigten_data(
       institutions=['MSU'],
       columns=['entry_term', 'UGDS_WHITE', 'UGDS_BLACK',
                'UGDS_HISP', 'UGDS_ASIAN']
   )

   # Plot stacked area
   plt.stackplot(
       msu['entry_term'],
       msu['UGDS_WHITE'] * 100,
       msu['UGDS_BLACK'] * 100,
       msu['UGDS_HISP'] * 100,
       msu['UGDS_ASIAN'] * 100,
       labels=['White', 'Black', 'Hispanic', 'Asian']
   )

   plt.xlabel('Year')
   plt.ylabel('Percentage of Students')
   plt.title('MSU Student Demographics Over Time')
   plt.legend(loc='upper left')
   plt.show()

Data Analysis Tips
------------------

Handling Missing Data
^^^^^^^^^^^^^^^^^^^^^

Some variables may have missing values for certain years:

.. code-block:: python

   import pandas as pd

   # Check for missing values
   df = load_bigten_data()
   missing = df.isnull().sum()
   print(missing[missing > 0])

   # Drop rows with missing values
   df_clean = df.dropna(subset=['ADM_RATE', 'UGDS'])

Time Series Analysis
^^^^^^^^^^^^^^^^^^^^

.. code-block:: python

   # Calculate year-over-year growth
   msu = load_bigten_data(institutions=['MSU'])
   msu = msu.sort_values('entry_term')
   msu['enrollment_growth'] = msu['UGDS'].pct_change() * 100

Comparative Analysis
^^^^^^^^^^^^^^^^^^^^

.. code-block:: python

   import pandas as pd

   # Compare across institutions
   data = load_bigten_data(years=[2023])

   # Rank by enrollment
   ranked = data.sort_values('UGDS', ascending=False)
   print(ranked[['name', 'UGDS']].head())

   # Calculate percentiles
   data['enrollment_pct'] = data['UGDS'].rank(pct=True) * 100

Next Steps
----------

* :doc:`bigten` - Work with Big Ten colors
* :doc:`quickstart` - More examples
* :doc:`api/data` - Complete data reference
