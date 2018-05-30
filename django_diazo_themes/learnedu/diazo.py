"""
Register the theme.
"""
from django_diazo.theme import DiazoTheme, registry


class LearnedUTheme(DiazoTheme):
    name = 'GrayGrids LearnedU Bootstrap4 Theme'
    slug = 'learnedu'
    pattern = '^(?!.*admin)'  # Theme everything but /admin

registry.register(LearnedUTheme)
