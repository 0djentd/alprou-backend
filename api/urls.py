from django.urls import path, include
from rest_framework.authtoken.views import obtain_auth_token
from rest_framework.routers import SimpleRouter
from . import views

router = SimpleRouter()
router.register('profiles', views.ProfilesViewset, 'profile')
router.register('habits', views.HabitsViewset, 'habit')
router.register('users', views.UsersViewset, 'user')

urlpatterns = [
        path("", include(router.urls)),
        path("", include("rest_framework.urls")),
        path("authtoken/", obtain_auth_token),
            ]
