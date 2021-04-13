from django.apps import AppConfig


class MoviesConfig(AppConfig):
    name = "blockbuster_clone.movies"

    def ready(self):
        import blockbuster_clone.movies.signals