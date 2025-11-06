from django.apps import AppConfig

class TurniejConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'turniej'

    def ready(self):
        import turniej.signals
