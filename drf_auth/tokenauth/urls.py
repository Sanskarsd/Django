from django.urls import path, include
from rest_framework.routers import DefaultRouter

from .views import RegisterView, LoginView, LogoutView, StudentViewSet

router = DefaultRouter()

router.register("students", StudentViewSet, basename="student")

urlpatterns = [
    path("register/", RegisterView.as_view()),
    path("login/", LoginView.as_view()),
    path("logout/", LogoutView.as_view()),
    path("", include(router.urls)),
]
