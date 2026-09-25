# Configuration file for the Sphinx documentation builder.
#
# For the full list of built-in configuration values, see the documentation:
# https://www.sphinx-doc.org/en/master/usage/configuration.html

import os
import sys
import django

# ---------------------------------------------------------------------------
# CRITICAL FIX 1: Add the project root to the Python path
# Since conf.py is inside 'docs/', we need to go up one level ('..') 
# so Python can find the 'sticky_notes' folder.
# ---------------------------------------------------------------------------
sys.path.insert(0, os.path.abspath('..'))

# ---------------------------------------------------------------------------
# CRITICAL FIX 2: Initialize Django properly
# This allows Sphinx to import your models and understand your database schema.
# ---------------------------------------------------------------------------
os.environ['DJANGO_SETTINGS_MODULE'] = 'sticky_notes.settings'
django.setup()

# -- Project information -----------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#project-information

project = 'Sticky Notes Application'
copyright = '2026, Faadhil'
author = 'Faadhil'
release = '1.0'

# -- General configuration ---------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#general-configuration

# ---------------------------------------------------------------------------
# CRITICAL FIX 3: Enable extensions to actually generate docs from code
# autodoc: pulls docstrings from your Python files
# viewcode: adds links to source code
# napoleon: allows Google-style docstrings (easier to read/write)
# ---------------------------------------------------------------------------
extensions = [
    'sphinx.ext.autodoc',
    'sphinx.ext.viewcode',
    'sphinx.ext.napoleon',
]

templates_path = ['_templates']
exclude_patterns = ['_build', 'Thumbs.db', '.DS_Store']

# -- Options for HTML output -------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#options-for-html-output

html_theme = 'alabaster'
html_static_path = ['_static']