"""
This module defines apps for the todo app.
"""
from django.apps import AppConfig


class TodoConfig(AppConfig):
    """This class defines the config for the todo app"""
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'todo'
