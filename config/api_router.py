from django.conf import settings
from rest_framework.routers import DefaultRouter, SimpleRouter

from blockbuster_clone.movies.views import MovieViewSet
from blockbuster_clone.store.views import OrderViewSet
from blockbuster_clone.users.views import UserViewSet

if settings.DEBUG:
    router = DefaultRouter()
else:
    router = SimpleRouter()

router.register("users", UserViewSet)
router.register("movies", MovieViewSet)
router.register("orders", OrderViewSet)


app_name = "api"
urlpatterns = router.urls
