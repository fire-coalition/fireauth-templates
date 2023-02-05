"""
Template filter for Terra Nanotech templates
"""

# Django
from django.template.defaulttags import register
from django.templatetags.static import static

# AA Templates: FI.RE Coalition
from fireauth_templates import __version__


@register.simple_tag
def fireauth_static(path: str) -> str:
    """
    Versioned static URL
    :param path:
    :type path:
    :return:
    :rtype:
    """

    static_url = static(path)
    versioned_url = static_url + "?v=" + __version__

    return versioned_url
