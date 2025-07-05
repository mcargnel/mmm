Getting Started
==============

Welcome to the MMM (Marketing Mix Model) project! This guide will help you get up and running quickly.

What is MMM?
-----------

Marketing Mix Modeling (MMM) is a statistical technique used to understand how different marketing activities contribute to business outcomes like sales or revenue. This project implements MMM from scratch using Python, focusing on educational value and understanding the underlying principles.

Quick Installation
------------------

Option 1: Using Virtual Environment (Recommended)
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. code-block:: bash

   # Clone the repository
   git clone <your-repo-url>
   cd mmm

   # Install dependencies
   pip install -r requirements.txt

   # Run the model
   python main.py

Option 2: Using Docker
~~~~~~~~~~~~~~~~~~~~~~

.. code-block:: bash

   # Build the Docker image
   docker build -t mmm-project .

   # Run the model
   docker run --rm mmm-project

Your First MMM Analysis
----------------------

Here's a simple example to get you started:

.. code-block:: python

   import pandas as pd
   from src.data_generation import gen_data
   from src.linear_regression import LinearRegression

   # Generate sample data
   df = gen_data()

   # Fit the model
   model = LinearRegression(df, 'y', ['x1_sat', 'x2_sat', 'trend'])
   results = model.fit()
   model.summary()

This will:
1. Generate synthetic marketing data
2. Fit a linear regression model
3. Display the results

Next Steps
----------

- Read the :doc:`theory/index` section to understand the mathematical foundations
- Explore the :doc:`api/index` for detailed function documentation
- Follow the :doc:`tutorials/index` for step-by-step guides

Need Help?
----------

If you encounter any issues:
1. Check the troubleshooting section
2. Review the API documentation
3. Look at the example notebooks 