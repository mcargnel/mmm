Adstock Transformation
======================

The adstock transformation models how marketing effects persist over time. This is a fundamental concept in Marketing Mix Modeling.

Mathematical Definition
----------------------

The geometric adstock transformation is defined as:

.. math::

   \text{Adstock}_t = \text{Media}_t + \alpha \cdot \text{Adstock}_{t-1}

Where:
- :math:`\text{Adstock}_t` is the adstocked value at time :math:`t`
- :math:`\text{Media}_t` is the original media spend at time :math:`t`
- :math:`\alpha` is the decay parameter (0 < α < 1)
- :math:`\text{Adstock}_{t-1}` is the adstocked value from the previous period

Interpretation
-------------

- **Higher α values** (closer to 1) mean longer persistence of marketing effects
- **Lower α values** (closer to 0) mean effects decay quickly
- The **half-life** of effects can be calculated as :math:`\ln(0.5) / \ln(\alpha)`

Example
-------

.. code-block:: python

   import numpy as np
   from src.utils import geometric_adstock
   
   # Original media spend
   media_spend = np.array([100, 0, 50, 0, 75])
   
   # Apply adstock with α = 0.6
   adstocked = geometric_adstock(media_spend, alpha=0.6)
   
   print("Original:", media_spend)
   print("Adstocked:", adstocked)
   
   # Output:
   # Original: [100   0  50   0  75]
   # Adstocked: [100.   60.   86.   51.6 105.96]

Implementation
-------------

The adstock transformation is implemented in :func:`src.utils.geometric_adstock`. 