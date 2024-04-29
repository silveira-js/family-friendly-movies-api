from django.conf import settings
from rest_framework.routers import DefaultRouter
from rest_framework.routers import SimpleRouter

from family_friendly_api.core.api.views import MovieViewSet
from family_friendly_api.core.api.views import WatchlistViewSet
from family_friendly_api.users.api.views import UserViewSet

router = DefaultRouter() if settings.DEBUG else SimpleRouter()

router.register(r"users", UserViewSet, basename="user")
router.register(r"movies", MovieViewSet, basename="movies")
router.register(r"watchlists", WatchlistViewSet, basename="watchlists")


app_name = "api"
urlpatterns = router.urls
