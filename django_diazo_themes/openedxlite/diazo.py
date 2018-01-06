"""
Register the theme.
"""
from django_diazo.theme import DiazoTheme, registry


class OpenedXLiteTheme(DiazoTheme):
    name = 'Open edX Lite'
    slug = 'openedxlite'
    pattern = '^(?!.*admin)'  # Theme everything but /admin

registry.register(OpenedXLiteTheme)
