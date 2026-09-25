# Configuration file for the Sphinx documentation builder.
#
# For the full list of built-in configuration values, see the documentation:
# https://www.sphinx-doc.org/en/master/usage/configuration.html

import os
import sys
import django

# ---------------------------------------------------------------------------
# CRITICAL FIX: Use ABSOLUTE PATH to project root
# This guarantees Python can find 'sticky_notes' regardless of 
# where Sphinx runs from.
# ---------------------------------------------------------------------------
sys.path.insert(0, r'C:\Users\DiLo\Desktop\capstone-sticky-notes-app')
sys.path.insert(0, r'C:\Users\DiLo\Desktop\capstone-sticky-notes-app\sticky_notes')

# ---------------------------------------------------------------------------
# Django Setup
# ---------------------------------------------------------------------------
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'stickynotes.settings')
django.setup()

# -- Project information -----------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#project-information

project = 'Sticky Notes Application'
copyright = '2026, Faadhil'
author = 'Faadhil'
release = '1.0'

# -- General configuration ---------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#general-configuration

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