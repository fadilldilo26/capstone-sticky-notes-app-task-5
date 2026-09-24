# Configuration file for the Sphinx documentation builder.
#
# For the full list of built-in configuration values, see the documentation:
# https://www.sphinx-doc.org/en/master/usage/configuration.html

import os
import sys

# 1. Add the project root (parent of docs) to the path
project_root = os.path.abspath(os.path.join(os.path.dirname(__file__), '..'))
sys.path.insert(0, project_root)

# DEBUG: Print paths to help us see what's going on
print(f"--- SPHINX DEBUG ---")
print(f"Project Root added to path: {project_root}")
print(f"Current Python Path: {sys.path}")

# List contents of the project root to verify structure
try:
    print(f"Contents of project root: {os.listdir(project_root)}")
except Exception as e:
    print(f"Error listing directory: {e}")

# 2. Set Django settings module
# Try 'sticky_notes.settings' first, but you might need to check your folder name
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'sticky_notes.settings')

# 3. Initialize Django
try:
    import django
    print("Django imported successfully.")
    django.setup()
    print("Django setup completed successfully!")
except Exception as e:
    print(f"ERROR during Django setup: {e}")
    # We don't raise here so Sphinx can still try to build basic docs
    pass

print("--- END DEBUG ---")

# -- Project information -----------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#project-information

project = 'Sticky Notes Application'
copyright = '2026, Faadhil'
author = 'Faadhil'
release = '1.0'

# -- General configuration ---------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#general-configuration

extensions = []

templates_path = ['_templates']
exclude_patterns = ['_build', 'Thumbs.db', '.DS_Store']



# -- Options for HTML output -------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#options-for-html-output

html_theme = 'alabaster'
html_static_path = ['_static']
