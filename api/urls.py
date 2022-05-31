from django.urls import path, include
from rest_framework.authtoken.views import obtain_auth_token
from rest_framework.routers import SimpleRouter
from . import views as apiViews


router = SimpleRouter()
router.register('habits', apiViews.HabitAPIViewSet.as_view({'get': 'list'}))

urlpatterns = [
        path("", include(router.urls)),
        path("authtoken/", obtain_auth_token),
            ]
