from django.urls import path
from drf_yasg.views import get_schema_view
from drf_yasg import openapi


schema_view = get_schema_view(
        openapi.Info(
            title="Alprou API",
            default_version="v1",
            ),
        public=False,
        )

urlpatterns = [
        path("swagger/", schema_view.with_ui('swagger'), name="schema-swagger"),
        path("redoc/", schema_view.with_ui('redoc'), name="schema-redoc"),
        ]
