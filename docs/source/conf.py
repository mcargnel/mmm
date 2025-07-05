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

html_theme = 'alabaster'
html_static_path = ['_static']

# Theme options for Alabaster theme
html_theme_options = {
    'logo': 'logo.png',
    'logo_name': True,
    'logo_text_align': 'center',
    'description': 'Marketing Mix Model from Scratch',
    'github_user': 'mcargnel',
    'github_repo': 'mmm',
    'github_button': True,
    'github_type': 'star',
    'github_count': True,
    'travis_button': False,
    'codecov_button': False,
    'analytics_id': '',
    'font_family': "'Roboto', Georgia, serif",
    'head_font_family': "'Roboto', 'Arial', sans-serif",
    'font_size': '16px',
    'page_width': '940px',
    'sidebar_width': '220px',
    'sidebar_collapse': True,
    'sidebar_includehidden': True,
    'navigation_depth': 4,
    'titles_only': False,
    'show_powered_by': False,
    'show_related': True,
    'show_relbars': True,
    'show_sphinx': False,
    'show_source': False,
    'sidebar_header': '#2980B9',
    'sidebar_text': '#333',
    'sidebar_link': '#2980B9',
    'sidebar_link_underscore': '#2980B9',
    'sidebar_list': '#666',
    'sidebar_rss': '#ff6b6b',
    'sidebar_search_button': '#2980B9',
    'sidebar_search_button_text': '#fff',
    'relbar_border': '#2980B9',
    'relbar_link': '#2980B9',
    'relbar_link_underscore': '#2980B9',
    'footer_bg': '#2980B9',
    'footer_text': '#fff',
    'footer_link': '#fff',
    'footer_link_underscore': '#fff'
}

# Additional options for better GitHub Pages compatibility
html_use_index = True
html_split_index = False
html_show_sourcelink = False
html_show_sphinx = False
html_show_copyright = True
