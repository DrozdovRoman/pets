from django.contrib import admin
from django.urls import path, include
from django.conf import settings

from .yasg import urlpatterns as doc_urls

urlpatterns = [
    path("admin/", admin.site.urls),
    # path("api/", include('api.urls', namespace='api'))
]

if settings.DEBUG:
    urlpatterns += doc_urls
