Getting Started with MMM
========================

This tutorial will walk you through creating your first Marketing Mix Model from scratch.

Prerequisites
------------

- Python 3.8+
- Basic understanding of Python and pandas
- Familiarity with linear regression concepts

Installation
-----------

1. Clone the repository and install dependencies:

   .. code-block:: bash

      git clone <your-repo-url>
      cd mmm
      pip install -r requirements.txt

2. Verify the installation:

   .. code-block:: python

      import pandas as pd
      import numpy as np
      from src.utils import geometric_adstock, saturation
      print("✅ All packages installed successfully!")

Understanding the MMM Pipeline
-----------------------------

The MMM process follows these steps:

1. **Data Generation**: Create synthetic marketing data
2. **Adstock Transformation**: Model persistence effects
3. **Saturation**: Model diminishing returns
4. **Regression**: Estimate marketing effects
5. **Contribution Analysis**: Calculate ROI and attribution

Step 1: Generate Data
--------------------

Start by creating synthetic marketing data:

.. code-block:: python

   from src.data_generation import gen_data
   
   # Generate synthetic marketing data
   df = gen_data()
   print(f"Generated {len(df)} observations")
   print(f"Columns: {list(df.columns)}")

Step 2: Apply Adstock Transformation
----------------------------------

Transform raw media spend to account for persistence:

.. code-block:: python

   from src.utils import geometric_adstock
   
   # Apply adstock to media variables
   df['x1_adstock'] = geometric_adstock(df['x1'].values, alpha=0.4)
   df['x2_adstock'] = geometric_adstock(df['x2'].values, alpha=0.6)
   
   print("Adstock transformation complete!")

Step 3: Apply Saturation
-----------------------

Model diminishing returns on marketing spend:

.. code-block:: python

   from src.utils import saturation
   
   # Apply saturation transformation
   df['x1_sat'] = saturation(df['x1_adstock'].values, lmd=2.0)
   df['x2_sat'] = saturation(df['x2_adstock'].values, lmd=1.5)
   
   print("Saturation transformation complete!")

Step 4: Run Linear Regression
----------------------------

Estimate the marketing effects:

.. code-block:: python

   from src.linear_regression import LinearRegression
   
   # Define independent variables
   indep_vars = ['x1_sat', 'x2_sat', 'trend', 'seasonality']
   
   # Create and fit the model
   model = LinearRegression(df, 'y', indep_vars)
   results = model.fit()
   
   # View results
   model.summary()

Step 5: Analyze Contributions
---------------------------

Calculate ROI and attribution:

.. code-block:: python

   from src.contributions import Contributions
   
   # Get coefficients
   coefficients = model.get_coefficients()
   
   # Create contributions object
   contrib = Contributions(df, coefficients)
   
   # Calculate decomposition
   decomposition = contrib.decomposition()
   
   # Calculate ROI
   media_vars = ['x1_sat', 'x2_sat']
   media_costs = {
       'x1_sat': df['x1_sat_media_cost'].sum(),
       'x2_sat': df['x2_sat_media_cost'].sum()
   }
   
   roi = contrib.roi(decomposition, media_vars, media_costs)
   print(f"ROI by channel: {roi}")

Next Steps
----------

- Explore the :doc:`../theory/adstock` page to understand the mathematics
- Check the :doc:`../api/index` for detailed function documentation
- Try different parameters to see how they affect results
- Experiment with your own data

See Also
--------

- :doc:`../theory/index` - Mathematical foundations
- :doc:`../api/index` - API reference
- :doc:`../examples/index` - More examples 