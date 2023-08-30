"""
FI.RE Auth Templates content processor
"""

# Django
from django.conf import settings
from django.core.handlers.wsgi import WSGIRequest


def fireauth_settings(request: WSGIRequest) -> dict:  # pylint: disable=unused-argument
    """
    Returning a settings dict
    :param request:
    :return:
    """

    # Template Settings
    return_value = {
        "FIREAUTH_TEMPLATE_AA_LOGO": "/static/fireauth_templates/images/fire-coalition-32x32.png",
        "REGISTRATION_VERIFY_EMAIL": getattr(
            settings, "REGISTRATION_VERIFY_EMAIL", True
        ),
    }

    return return_value
