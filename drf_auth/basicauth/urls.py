from django.urls import path, include
from rest_framework.routers import DefaultRouter

from .views import StudentViewSet, RegisterViewSet

router = DefaultRouter()

router.register("students", StudentViewSet, basename="student")

router.register("register", RegisterViewSet, basename="register")

urlpatterns = [
    path("", include(router.urls)),
]
