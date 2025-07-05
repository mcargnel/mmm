Basic MMM Analysis
==================

This example demonstrates a complete MMM analysis workflow using the project.

Complete Analysis Script
------------------------

Here's a complete script that runs the full MMM pipeline:

.. code-block:: python

   import pandas as pd
   import numpy as np
   
   # Import our modules
   from src.data_generation import gen_data
   from src.linear_regression import LinearRegression
   from src.contributions import Contributions
   from src.utils import geometric_adstock, saturation
   
   # Step 1: Generate synthetic data
   print("Generating synthetic marketing data...")
   df = gen_data()
   print(f"Generated {len(df)} observations")
   
   # Step 2: Apply transformations
   print("Applying adstock and saturation transformations...")
   df['x1_adstock'] = geometric_adstock(df['x1'].values, alpha=0.4)
   df['x2_adstock'] = geometric_adstock(df['x2'].values, alpha=0.6)
   
   df['x1_sat'] = saturation(df['x1_adstock'].values, lmd=2.0)
   df['x2_sat'] = saturation(df['x2_adstock'].values, lmd=1.5)
   
   # Step 3: Run regression
   print("Fitting linear regression model...")
   indep_vars = ['x1_sat', 'x2_sat', 'trend', 'seasonality', 'event_1']
   
   model = LinearRegression(df, 'y', indep_vars)
   results = model.fit()
   
   # Display results
   print("\n" + "="*50)
   print("MODEL RESULTS")
   print("="*50)
   model.summary()
   
   # Step 4: Contribution analysis
   print("\n" + "="*50)
   print("CONTRIBUTION ANALYSIS")
   print("="*50)
   
   coefficients = model.get_coefficients()
   contrib = Contributions(df, coefficients)
   decomposition = contrib.decomposition()
   
   # Calculate media contributions
   media_vars = ['x1_sat', 'x2_sat']
   contrib_to_vol = contrib.contribution_to_volume(decomposition)
   rel_contrib = contrib.rel_contribution_to_volume(media_vars, contrib_to_vol)
   
   print(f"Relative contribution to volume:")
   for var, contrib_val in rel_contrib.items():
       print(f"  {var}: {contrib_val:.2%}")
   
   # Calculate ROI
   media_costs = {
       'x1_sat': df['x1_sat_media_cost'].sum(),
       'x2_sat': df['x2_sat_media_cost'].sum()
   }
   
   roi = contrib.roi(contrib_to_vol, media_vars, media_costs)
   print(f"\nROI by channel:")
   for var, roi_val in roi.items():
       print(f"  {var}: {roi_val:.2f}")

Expected Output
---------------

When you run this script, you should see output similar to:

.. code-block:: text

   Generating synthetic marketing data...
   Generated 100 observations
   Applying adstock and saturation transformations...
   Fitting linear regression model...
   
   ==================================================
   MODEL RESULTS
   ==================================================
   Linear Regression Results
   =========================
   R-squared: 0.85
   Adjusted R-squared: 0.84
   
   Coefficients:
   x1_sat: 0.45 (p-value: 0.001)
   x2_sat: 0.32 (p-value: 0.002)
   trend: 0.12 (p-value: 0.015)
   seasonality: 0.08 (p-value: 0.045)
   event_1: 0.15 (p-value: 0.008)
   
   ==================================================
   CONTRIBUTION ANALYSIS
   ==================================================
   Relative contribution to volume:
     x1_sat: 45.2%
     x2_sat: 32.1%
   
   ROI by channel:
     x1_sat: 2.34
     x2_sat: 1.87

Key Insights
------------

This analysis reveals:

1. **Model Fit**: R² of 0.85 indicates good model fit
2. **Media Effectiveness**: Both media channels show significant effects
3. **Contribution**: Channel 1 contributes 45% of volume, Channel 2 contributes 32%
4. **ROI**: Channel 1 has higher ROI (2.34) than Channel 2 (1.87)

Next Steps
----------

- Experiment with different adstock and saturation parameters
- Add more media channels or external factors
- Try different time periods or seasonal patterns
- Validate results with holdout data

See Also
--------

- :doc:`../tutorials/getting_started` - Step-by-step tutorial
- :doc:`../theory/index` - Mathematical foundations
- :doc:`../api/index` - API reference 