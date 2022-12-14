from django.contrib import admin
from django.template.defaulttags import url
from django.urls import include, path
from django.conf import settings
from django.conf.urls.static import static

# TODO здесь необходимо подклюючит нужные нам urls к проекту

urlpatterns = [
    path("api/admin/", admin.site.urls),
    path("api/redoc-tasks/", include("redoc.urls")),
    path("auth/", include('djoser.urls')),
    path("api/ad/", include("ads.urls")),
    path("", include("users.urls"))
]
urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)