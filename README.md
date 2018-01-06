# Django Diazo Themes

Example built-in themes for django-diazo.

## Themes

Currently we have these themes included:

    - Open edX Lite (pared down LMS functionality for older browsers like IE<11)

## Installation

### settings.py

    INSTALLED_APPS = (
        ...
        'django_diazo_themes.openedxlite',
        ...
    )

Take a look at the `ExampleView` in `view.py` and implement such a view in your own application.

To synchronize the built-in themes with the database/application run the following command:

    python manage.py syncthemes

Make sure you enable the theme in the Django Admin interface.
