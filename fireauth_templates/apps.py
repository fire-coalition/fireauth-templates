"""
TN-NT Templates app config
"""

# Django
from django.apps import AppConfig

from . import __version__


class FireAuthTemplatesConfig(AppConfig):
    name = "fireauth_templates"
    label = "fireauth_templates"
    verbose_name = f"Alliance Auth Templates for FI.RE Coalition v{__version__}"
