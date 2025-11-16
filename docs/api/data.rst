Data Module
===========

.. automodule:: msuthemes.data
   :members:
   :undoc-members:
   :show-inheritance:

Functions
---------

.. autofunction:: msuthemes.data.load_bigten_data

.. autofunction:: msuthemes.data.get_bigten_summary

.. autofunction:: msuthemes.data.get_dataset_info

.. autofunction:: msuthemes.data.get_data_path

.. autofunction:: msuthemes.data.list_available_datasets

Dataset Information
-------------------

BigTen Dataset
^^^^^^^^^^^^^^

The BigTen dataset contains historical data (1996-2023) for all 18 Big Ten Conference
institutions from the U.S. Department of Education's College Scorecard.

**Dimensions:**
  * 504 rows (18 institutions × 28 years)
  * 38 columns

**Key Variables:**
  * ``name``: Institution name
  * ``entry_term``: Year
  * ``UGDS``: Total enrollment
  * ``ADM_RATE``: Admission rate
  * ``C150_4``: 4-year completion rate
  * ``TUITIONFEE_IN``: In-state tuition and fees
  * ``TUITIONFEE_OUT``: Out-of-state tuition and fees
  * ``PCTPELL``: Percentage of Pell grant recipients
  * ``UGDS_*``: Demographic breakdowns

**Data Source:**
  College Scorecard (https://collegescorecard.ed.gov/)

Usage Examples
--------------

Loading Data
^^^^^^^^^^^^

.. code-block:: python

   from msuthemes import load_bigten_data

   # Load all data
   df = load_bigten_data()
   print(df.shape)  # (504, 38)

   # Filter for specific institutions
   msu_data = load_bigten_data(institutions=['MSU'])

   # Filter by years
   recent = load_bigten_data(years=[2020, 2021, 2022, 2023])

   # Combine filters
   comparison = load_bigten_data(
       institutions=['MSU', 'Michigan', 'Ohio State'],
       years=list(range(2015, 2024))
   )

Selecting Columns
^^^^^^^^^^^^^^^^^

.. code-block:: python

   from msuthemes import load_bigten_data

   # Select specific columns
   subset = load_bigten_data(
       columns=['name', 'entry_term', 'UGDS', 'ADM_RATE', 'TUITIONFEE_IN']
   )

   # Combine with filters
   msu_subset = load_bigten_data(
       institutions=['MSU'],
       years=[2020, 2021, 2022, 2023],
       columns=['name', 'entry_term', 'UGDS']
   )

Using Name Aliases
^^^^^^^^^^^^^^^^^^

.. code-block:: python

   from msuthemes import load_bigten_data

   # Works with nicknames
   spartans = load_bigten_data(institutions=['Spartans'])
   wolverines = load_bigten_data(institutions=['Wolverines'])
   buckeyes = load_bigten_data(institutions=['Buckeyes'])

   # Mix of names and aliases
   data = load_bigten_data(
       institutions=['MSU', 'Wolverines', 'buckeyes']
   )

Getting Summaries
^^^^^^^^^^^^^^^^^

.. code-block:: python

   from msuthemes import get_bigten_summary, get_dataset_info

   # Get summary statistics
   summary = get_bigten_summary()
   print(summary.head())

   # Get dataset metadata
   info = get_dataset_info()
   print(f"Institutions: {info['n_institutions']}")
   print(f"Years: {info['years']}")
   print(f"Columns: {info['n_columns']}")

Visualization Example
^^^^^^^^^^^^^^^^^^^^^

.. code-block:: python

   import matplotlib.pyplot as plt
   from msuthemes import theme_msu, get_bigten_colors, load_bigten_data

   # Apply theme
   theme_msu()

   # Load data
   data = load_bigten_data(
       institutions=['MSU', 'Michigan', 'Ohio State'],
       columns=['name', 'entry_term', 'UGDS']
   )

   # Get colors
   colors = get_bigten_colors(['MSU', 'Michigan', 'Ohio State'])

   # Plot
   fig, ax = plt.subplots()
   for school in ['MSU', 'Michigan', 'Ohio State']:
       school_data = data[data['name'] == school]
       ax.plot(
           school_data['entry_term'],
           school_data['UGDS'],
           label=school,
           color=colors[school],
           linewidth=2
       )

   ax.set_xlabel('Year')
   ax.set_ylabel('Enrollment')
   ax.set_title('Big Ten Enrollment Trends')
   ax.legend()
   plt.show()
