"""
This module defines settings for the todo app.
"""
EMAIL_BACKEND = 'django.core.mail.backends.console.EmailBackend'
ALLOWED_HOSTS = ['*']

INSTALLED_APPS = [
    # other installed apps
    'crispy_forms',  # Ensure crispy_forms is listed here
    'crispy_bootstrap4',  # Add this if you're using the Bootstrap 4 template pack
]

CRISPY_TEMPLATE_PACK = 'bootstrap4'  # or 'bootstrap5' if you're using Bootstrap 5

DEBUG = True
