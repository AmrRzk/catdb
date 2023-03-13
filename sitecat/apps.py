from django.apps import AppConfig


class SitecatConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'sitecat'

    def ready(self):
        from . import serializer_decorator
        from . import signals
