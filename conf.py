# pylint: disable=invalid-name,redefined-builtin
"""
Configuration file for the Sphinx documentation builder.

For the full list of built-in configuration values, see the documentation:
https://www.sphinx-doc.org/en/master/usage/configuration.html

-- Project information -----------------------------------------------------
https://www.sphinx-doc.org/en/master/usage/configuration.html#project-information

-- General configuration ---------------------------------------------------
https://www.sphinx-doc.org/en/master/usage/configuration.html#general-configuration
"""
import sys
from pathlib import Path
import version_query


def get_version():
    """Get the next expected semantic version for this project."""
    version = version_query.predict_git_repo(Path('.'))
    return version.to_str()

sys.path.append(str(Path("ansible/files").resolve()))
sys.path.append(str(Path("ansible/files/githooks").resolve()))

author = "Xander Harris"
autoyaml_root = "."
copyright = "2024, Xander Harris"
exclude_patterns = [
    "_build",
    "Thumbs.db",
    ".DS_Store",
    ".pytest_cache/*",
    ".tox/*",
    ".venv/*",
]
extensions = [
    "myst_parser",
    "sphinx_copybutton",
    "sphinx_design",
    "sphinx_last_updated_by_git",
    "sphinx_git",
    "sphinx.ext.autodoc",
    "sphinx.ext.coverage",
    "sphinx.ext.duration",
    "sphinx.ext.githubpages",
    "sphinx.ext.graphviz",
    "sphinx.ext.todo",
    'sphinxcontrib.ansibleautodoc',
    "sphinxcontrib.autoyaml",
]
git_untracked_check_dependencies = False
graphviz_output_format = "png"
# -- Options for HTML output -------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#options-for-html-output
html_context = {"full_path": str(Path(".").resolve())}
html_static_path = ["_static"]
html_theme = "sphinx_book_theme"
myst_enable_extensions = [
    "amsmath",
    "attrs_block",
    "attrs_inline",
    "colon_fence",
    "deflist",
    "dollarmath",
    "fieldlist",
    "html_admonition",
    "html_image",
    "linkify",
    "replacements",
    "smartquotes",
    "strikethrough",
    "substitution",
    "tasklist",
]
myst_footnote_transition = True
myst_title_to_header = True
project = "Ansible Kubernetes Control Plane"
release = get_version()
show_authors = True
source_suffix = {
    '.md': 'markdown',
    '.rst': 'restructuredText',
    '.txt': 'markdown'
}
templates_path = ["_templates"]
