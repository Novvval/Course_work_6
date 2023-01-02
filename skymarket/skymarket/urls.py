from django.contrib import admin
from django.template.defaulttags import url
from django.urls import include, path
from django.conf import settings
from django.conf.urls.static import static
from django.views.generic import RedirectView
from rest_framework_simplejwt.views import TokenObtainPairView, TokenRefreshView

# TODO здесь необходимо подклюючит нужные нам urls к проекту

urlpatterns = [
    path("api/admin/", admin.site.urls),
    path("api/redoc-tasks/", include("redoc.urls")),
    path("auth/", include('djoser.urls')),
    path("auth/", include("djoser.urls.jwt")),
    path("api/token/", TokenObtainPairView.as_view()),
    path("api/refresh/", TokenRefreshView.as_view()),
    path("", include("ads.urls")),
    path("", include("users.urls"))
]
urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)