from django.contrib import admin
from django.urls import path, include, re_path

urlpatterns = [
    path("api/", include("api.urls")),
    path("docs/", include("docs.urls")),
    path("admin/", admin.site.urls),
    re_path(".*", include('frontend.urls')),
]
