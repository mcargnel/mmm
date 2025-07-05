Data Generation
==============

.. automodule:: src.data_generation
   :members:
   :undoc-members:
   :show-inheritance:

Functions
---------

.. autofunction:: src.data_generation.gen_data

Examples
--------

Basic data generation:

.. code-block:: python

   from src.data_generation import gen_data
   
   # Generate default data
   df = gen_data()
   print(f"Generated {len(df)} rows of data")
   print(f"Columns: {list(df.columns)}")

Custom parameters:

.. code-block:: python

   # Generate data with custom parameters
   df = gen_data(
       beta_1=2.5,      # Coefficient for x1_sat
       beta_2=1.8,      # Coefficient for x2_sat
       beta_event=2.0,  # Event coefficient
       intercept=1.5    # Model intercept
   ) 