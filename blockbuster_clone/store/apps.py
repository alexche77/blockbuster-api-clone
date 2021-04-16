from django.apps import AppConfig


class StoreConfig(AppConfig):
    name = "blockbuster_clone.store"

    def ready(self):
        import blockbuster_clone.store.signals  # noqa F401
