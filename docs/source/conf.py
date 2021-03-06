# Configuration file for the Sphinx documentation builder.
#
# This file only contains a selection of the most common options. For a full
# list see the documentation:
# https://www.sphinx-doc.org/en/master/usage/configuration.html

# -- Path setup --------------------------------------------------------------

# If extensions (or modules to document with autodoc) are in another directory,
# add these directories to sys.path here. If the directory is relative to the
# documentation root, use os.path.abspath to make it absolute, like shown here.
#
import os
import sys
sys.path.append(os.path.abspath('../../Filtration/src/'))
sys.path.append(os.path.abspath('../../AWS-Utils/src/'))
sys.path.append(os.path.abspath('../../CustomDataset/src/'))
sys.path.append(os.path.abspath('../../ModelManager/src/'))
sys.path.append(os.path.abspath('../../UnifiedImageReader/src/unified_image_reader'))
sys.path.append(os.path.abspath('../../UnifiedImageReader/src/unified_image_reader/adapters/'))
# print(sys.path[-1])

# -- Project information -----------------------------------------------------

project = 'Digital Pathology'
copyright = '2022, Anthony Goncharenko, Saadiya Allahbaksh, Ritik Ghanshani, Adin Solomon, Kevin Karnani, Jesse Rivera, Amanda Warkow'
author = 'Anthony Goncharenko, Saadiya Allahbaksh, Ritik Ghanshani, Adin Solomon, Kevin Karnani, Jesse Rivera, Amanda Warkow'

# The full version, including alpha/beta/rc tags
release = '0.0.1'


# -- General configuration ---------------------------------------------------

autodoc_mock_imports = ["numpy", "boto3", "cloudpickle", "slideio", "vips", "torch", "cv2", "tqdm", "histolab", "pyvips", "sagemaker", "tables"]

# Add any Sphinx extension module names here, as strings. They can be
# extensions coming with Sphinx (named 'sphinx.ext.*') or your custom
# ones.
extensions = ['sphinx.ext.autodoc', 
]

# Add any paths that contain templates here, relative to this directory.
templates_path = ['_templates']

# List of patterns, relative to source directory, that match files and
# directories to ignore when looking for source files.
# This pattern also affects html_static_path and html_extra_path.
exclude_patterns = ["*__pycache__*"]


# -- Options for HTML output -------------------------------------------------

# The theme to use for HTML and HTML Help pages.  See the documentation for
# a list of builtin themes.
#
html_theme = 'sphinx_rtd_theme'

# html_theme_options = {
#     "rightsidebar": "true",
# }
# Add any paths that contain custom static files (such as style sheets) here,
# relative to this directory. They are copied after the builtin static files,
# so a file named "default.css" will overwrite the builtin "default.css".
html_static_path = ['_static']