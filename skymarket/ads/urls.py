from django.urls import include, path
from rest_framework.routers import DefaultRouter, SimpleRouter
from ads.views import AdViewSet, CommentViewSet
from rest_framework_nested import routers


# TODO настройка роутов для модели

ads_router = SimpleRouter()
ads_router.register("ads", AdViewSet)
comments_router = routers.NestedSimpleRouter(ads_router, "ads", lookup="ad")
comments_router.register("comments", CommentViewSet)


urlpatterns = [
    path("", include(ads_router.urls)),
    path("", include(comments_router.urls)),
]
