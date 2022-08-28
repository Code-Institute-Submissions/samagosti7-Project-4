"""
        This file contains the configuration for our news app
    """
from django.apps import AppConfig


class NewsConfig(AppConfig):
    """
        First and only configuration
    """
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'news'
