# Configuration file for Sphinx documentation builder

import os
import sys
sys.path.insert(0, os.path.abspath('../..'))

# -- Project information -----------------------------------------------------
project = 'GPS Tech Doc'
copyright = '2025, GPS Tech Doc'
author = 'Norq Technology Solutions Pvt Ltd'
release = '1.0'

# -- General configuration ---------------------------------------------------
extensions = [
    'sphinx.ext.autodoc',
    'sphinx.ext.napoleon',
    'sphinx.ext.viewcode',
    'sphinx.ext.autosectionlabel',
]

templates_path = ['_templates']
exclude_patterns = ['_build', 'Thumbs.db', '.DS_Store']
source_suffix = '.rst'
master_doc = 'index'
language = 'en'

autodoc_member_order = 'bysource'
autodoc_inherit_docstrings = True
add_module_names = False

# -- Options for HTML output -------------------------------------------------
html_theme = 'sphinx_rtd_theme'
html_static_path = ['_static']
html_sidebars = {
    '**': ['relations.html', 'searchbox.html'],
}
htmlhelp_basename = 'gpsnorqdoc'

def setup(app):
    app.add_css_file('my-theme.css')
