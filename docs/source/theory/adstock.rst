Adstock Theory
=============

The adstock transformation is a fundamental concept in Marketing Mix Modeling that captures how marketing effects persist over time.

Mathematical Definition
----------------------

The geometric adstock model is defined as:

.. math::

   \text{Adstock}_t = \text{Media}_t + \alpha \cdot \text{Adstock}_{t-1}

Where:
- :math:`\text{Adstock}_t` is the adstocked value at time :math:`t`
- :math:`\text{Media}_t` is the raw media spend at time :math:`t`
- :math:`\alpha` is the decay parameter (0 < α < 1)
- :math:`\text{Adstock}_{t-1}` is the adstocked value from the previous period

Interpretation
--------------

The adstock parameter :math:`\alpha` controls the persistence of marketing effects:

- **High α (close to 1)**: Marketing effects persist for many periods
- **Low α (close to 0)**: Marketing effects decay quickly

For example, with :math:`\alpha = 0.8`:
- 80% of the previous period's effect carries over
- 20% of the effect decays each period

Half-Life Calculation
--------------------

The half-life of adstock effects can be calculated as:

.. math::

   \text{Half-life} = \frac{\ln(0.5)}{\ln(\alpha)}

This tells us how many periods it takes for half of the marketing effect to decay.

Example
-------

Consider a media campaign with the following spend pattern:

.. code-block:: python

   media_spend = [100, 0, 50, 0, 75]
   alpha = 0.6

The adstocked values would be:

.. math::

   \begin{align}
   \text{Adstock}_1 &= 100 + 0.6 \cdot 0 = 100 \\
   \text{Adstock}_2 &= 0 + 0.6 \cdot 100 = 60 \\
   \text{Adstock}_3 &= 50 + 0.6 \cdot 60 = 86 \\
   \text{Adstock}_4 &= 0 + 0.6 \cdot 86 = 51.6 \\
   \text{Adstock}_5 &= 75 + 0.6 \cdot 51.6 = 105.96
   \end{align}

Implementation
--------------

In our implementation, the adstock transformation is applied using the :func:`geometric_adstock` function:

.. code-block:: python

   from src.utils import geometric_adstock
   
   # Apply adstock transformation
   adstocked_media = geometric_adstock(media_data, alpha=0.6)

See Also
--------

- :func:`geometric_adstock` - Implementation details
- :doc:`saturation` - Next step in the MMM pipeline
- :doc:`regression` - How adstocked data is used in modeling 