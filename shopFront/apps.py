from django.apps import AppConfig


class ShopfrontConfig(AppConfig):
    default_auto_field = "django.db.models.BigAutoField"
    name = "shopFront"

    def ready(self):
        import shopFront.signals
