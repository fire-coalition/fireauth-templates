"""
TN-NT Templates content processor
"""

# Django
from django.core.handlers.wsgi import WSGIRequest


def fireauth_settings(request: WSGIRequest) -> dict:
    """
    Returning a settings dict
    :param request:
    :return:
    """

    # AA logo
    return_value = {
        "FIREAUTH_TEMPLATE_AA_LOGO": "/static/fireauth_templates/images/fire-coalition-32x32.png"
    }

    return return_value
