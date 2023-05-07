from django.apps import AppConfig


class PhonesConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'phones'


class PhonesAppConfig(AppConfig):
    name = 'phones'
    verbose_name = 'Phones Application'

    def ready(self):
        import phones.signals

