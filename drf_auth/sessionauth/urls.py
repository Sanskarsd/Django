from django.urls import path, include
from rest_framework.routers import DefaultRouter

from .views import csrf_token_view, LoginView, LogoutView, StudentViewSet

router = DefaultRouter()

router.register("students", StudentViewSet, basename="student")


urlpatterns = [
    path("", include(router.urls)),
    path("csrf/", csrf_token_view),
    path("login/", LoginView.as_view()),
    path("logout/", LogoutView.as_view()),
]
