.. MMM from Scratch documentation master file, created by
   sphinx-quickstart on Fri Jul  4 22:42:16 2025.
   You can adapt this file completely to your liking, but it should at least
   contain the root `toctree` directive.

MMM from Scratch Documentation
==============================

Welcome to the **Marketing Mix Model (MMM) from Scratch** documentation!

This project implements a complete MMM system using only **NumPy and Pandas**, designed for learning and understanding marketing mix modeling from first principles.

What is Marketing Mix Modeling?
-------------------------------

Marketing Mix Modeling is a statistical technique that helps businesses understand how their marketing activities (TV, digital, print, etc.) contribute to sales or other business outcomes. Unlike simple attribution models, MMM accounts for:

- **Adstock Effects**: How marketing impact persists over time
- **Saturation**: Diminishing returns on marketing spend
- **External Factors**: Seasonality, trends, and events
- **Interaction Effects**: How different channels work together

Key Features
------------

* **From First Principles**: Built from scratch to understand the mathematics
* **Educational Focus**: Clear explanations of MMM concepts
* **Mathematical Rigor**: Proper statistical inference and validation
* **Practical Examples**: Real-world scenarios and use cases
* **Docker Support**: Reproducible environments for learning

Quick Start
-----------

.. code-block:: bash

   # Install dependencies
   pip install -r requirements.txt
   
   # Run the model
   python main.py
   
   # Or use Docker
   docker build -t mmm-project .
   docker run --rm mmm-project

Documentation Structure
----------------------

.. toctree::
   :maxdepth: 2
   :caption: Contents:

   theory/index
   api/index
   tutorials/index
   examples/index

Indices and tables
==================

* :ref:`genindex`
* :ref:`modindex`
* :ref:`search`

