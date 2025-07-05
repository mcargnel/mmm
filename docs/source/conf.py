# Configuration file for the Sphinx documentation builder.
#
# For the full list of built-in configuration values, see the documentation:
# https://www.sphinx-doc.org/en/master/usage/configuration.html

# -- Project information -----------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#project-information

project = 'MMM from Scratch'
copyright = '2025, Martin Cargnel'
author = 'Martin Cargnel'

# -- General configuration ---------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#general-configuration

extensions = [
    'sphinx.ext.autodoc',
    'sphinx.ext.viewcode',
    'sphinx.ext.mathjax',
    'sphinx.ext.napoleon',  # Support for Google/NumPy docstrings
    'sphinx_rtd_theme',     # Read the Docs theme
]

templates_path = ['_templates']
exclude_patterns = []

# Add the src directory to Python path so Sphinx can find your modules
import os
import sys
sys.path.insert(0, os.path.abspath('../..'))



# -- Options for HTML output -------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#options-for-html-output

html_theme = 'classic'
html_static_path = ['_static']

# Theme options for Classic theme
html_theme_options = {
    'rightsidebar': False,
    'stickysidebar': True,
    'collapsiblesidebar': True,
    'externalrefs': True,
    'footerbgcolor': '#2980B9',
    'footertextcolor': '#ffffff',
    'sidebarbgcolor': '#f8f9fa',
    'sidebartextcolor': '#333333',
    'sidebarlinkcolor': '#2980B9',
    'relbarbgcolor': '#2980B9',
    'relbartextcolor': '#ffffff',
    'relbarlinkcolor': '#ffffff',
    'bgcolor': '#ffffff',
    'textcolor': '#333333',
    'linkcolor': '#2980B9',
    'visitedlinkcolor': '#8e44ad',
    'headbgcolor': '#2980B9',
    'headtextcolor': '#ffffff',
    'headlinkcolor': '#ffffff',
    'codebgcolor': '#f8f9fa',
    'codetextcolor': '#333333'
}

# Additional options for better GitHub Pages compatibility
html_use_index = True
html_split_index = False
html_show_sourcelink = False
html_show_sphinx = False
html_show_copyright = True
