# Configuration file for the Sphinx documentation builder.

import os
import sys
from datetime import date

# Stelle sicher, dass Sphinx dein Paket findet
sys.path.insert(0, os.path.abspath("../"))

# Importiere die Version aus deinem Paket
from novacordpy import __version__

# -- Projekt-Informationen -----------------------------------------------------
project = "novacordpy"
copyright = f"{date.today().year}, atpascal07"
author = "atpascal07"
release = __version__
version = __version__

# -- Allgemeine Konfiguration --------------------------------------------------
extensions = [
    "sphinx.ext.autodoc",
    "sphinx.ext.todo",
    "sphinx.ext.viewcode",
    "sphinx.ext.napoleon",
    "sphinx.ext.autosummary",
    "sphinx.ext.intersphinx",
    "sphinx_autodoc_typehints",
    "sphinx_copybutton",
]

simplify_optional_unions = True
autodoc_member_order = "bysource"

# Verknüpfungen zu anderen Projektdokumentationen
intersphinx_mapping = {
    "py": ("https://docs.python.org/3", None),
    "aio": ("https://docs.aiohttp.org/en/stable/", None),
    "req": ("https://requests.readthedocs.io/en/latest/", None),
    "dc": ("https://docs.pycord.dev/en/master/", None),
    "dpy": ("https://discordpy.readthedocs.io/en/stable/", None),
    "sql": ("https://aiosqlite.omnilib.dev/en/stable/", None),
}

templates_path = ["_templates"]
exclude_patterns = ["_build", "Thumbs.db", ".DS_Store"]

# -- HTML-Ausgabe --------------------------------------------------------------
html_theme = "furo"
html_static_path = ["_static"]

html_title = f"<h3 align='center'>{release}</h3>"
html_logo = "_static/novacordpy.png"
html_favicon = "_static/favicon.ico"
