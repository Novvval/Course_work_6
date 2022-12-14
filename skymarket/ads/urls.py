from django.urls import include, path
from rest_framework.routers import DefaultRouter

from ads.views import AdViewSet, CommentViewSet

# TODO настройка роутов для модели

router = DefaultRouter()
router.register(r"ads", AdViewSet, basename="ad")
router.register(r"comments", CommentViewSet, basename="ad")


urlpatterns = [
    path('', include(router.urls))
]
