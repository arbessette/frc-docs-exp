"""FRC Docs: local prototype using the WPILib Furo design."""
project = "FIRST Robotics Competition"
author = "FRC Docs contributors"
copyright = "2026, FRC Docs contributors; CC BY 4.0"
release = "0.1"
extensions = ["sphinx_design", "sphinx.ext.intersphinx", "sphinx.ext.autosectionlabel", "sphinx.ext.mathjax", "sphinxcontrib.youtube"]
autosectionlabel_prefix_document = True
nitpicky = True
root_doc = "index"
exclude_patterns = []
html_theme = "furo"
html_title = "FIRST Robotics Competition"
version = "2027"
html_favicon = "_static/images/FIRSTicon_RGB_withTM.ico"
html_logo = "_static/images/FIRST_HorzRGB_reverse.png"
templates_path = ["_templates"]
html_static_path = ["_static"]
html_css_files = ["css/wpilib-rtd.css", "css/sw-components.css", "css/frc-docs.css"]
html_theme_options = {
    "announcement": "<strong>DRAFT</strong> under review",
    "light_css_variables": {
        "color-sidebar-background": "#003974",
        "color-sidebar-brand-text": "#ffffffcc",
        "color-sidebar-link-text": "#acb1b9",
        "color-sidebar-link-text--top-level": "#d9d9d9",
        "color-sidebar-caption-text": "#81868d",
        "color-background-hover": "#023160",
    },
}
intersphinx_mapping = {
    "wpilib": ("https://docs.wpilib.org/en/stable/", None),
}
intersphinx_disabled_reftypes = ["*"]
intersphinx_timeout = 15
linkcheck_timeout = 15
linkcheck_retries = 2
linkcheck_anchors = False
