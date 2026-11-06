from django.urls import path, include
from rest_framework.routers import DefaultRouter

from .views import StudentViewSet
from rest_framework_simplejwt.views import (
    TokenObtainPairView,
    TokenRefreshView,
    TokenVerifyView,
)

router = DefaultRouter()
router.register("students", StudentViewSet, basename="student")

urlpatterns = [
    path("login/", TokenObtainPairView.as_view()),
    path("refresh/", TokenRefreshView.as_view()),
    path("verify/", TokenVerifyView.as_view()),
    path("", include(router.urls)),
]
