# Django
from django.template import Context, Template
from django.test import TestCase

# AA Templates: FI.RE Coalition
from fireauth_templates import __version__


class TestTemplateVariables(TestCase):
    """
    Test FI.RE Auth Template tags
    """

    def test_fireauth_static(self):
        """
        Test fireauth_static
        :return:
        :rtype:
        """

        context = Context({"version": __version__})
        template_to_render = Template(
            "{% load fireauth_template_tags %}"
            "{% fireauth_static 'fireauth_templates/css/fonts.min.css' %}"
        )

        rendered_template = template_to_render.render(context)

        self.assertInHTML(
            f'/static/fireauth_templates/css/fonts.min.css?v={context["version"]}',
            rendered_template,
        )
