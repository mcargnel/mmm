Saturation Functions
===================

Saturation functions model diminishing returns in marketing spend, a key concept in Marketing Mix Modeling.

Mathematical Definition
----------------------

The saturation function transforms adstocked media data to model diminishing returns using the formula:

.. math::

   f(x) = \frac{1 - e^{-\lambda x}}{1 + e^{-\lambda x}}

Where:
- :math:`x` is the input value (typically adstocked media)
- :math:`\lambda` is the saturation parameter controlling curve shape
- :math:`f(x)` is the saturated value between 0 and 1

Interpretation
-------------

- **Higher λ values** create steeper saturation curves
- **Lower λ values** create more gradual saturation
- **Output range** is always between 0 and 1
- **S-shaped curve** models realistic diminishing returns

Example
-------

.. code-block:: python

   import numpy as np
   from src.utils import saturation
   
   # Original adstocked media values
   adstocked_media = np.array([0, 10, 50, 100, 200])
   
   # Apply saturation with different λ values
   saturated_steep = saturation(adstocked_media, lmd=0.1)
   saturated_gradual = saturation(adstocked_media, lmd=0.01)
   
   print("Original:", adstocked_media)
   print("Steep saturation (λ=0.1):", saturated_steep)
   print("Gradual saturation (λ=0.01):", saturated_gradual)

Implementation
-------------

The saturation function is implemented in :func:`src.utils.saturation`.

Business Impact
--------------

Saturation functions are crucial for realistic MMM because:

1. **Realistic Modeling**: Marketing spend has diminishing returns
2. **Budget Optimization**: Helps identify optimal spend levels
3. **ROI Analysis**: More accurate return on investment calculations
4. **Media Mix**: Better understanding of channel effectiveness 