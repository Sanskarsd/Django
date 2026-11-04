from django.urls import path
from . import views
from .views import studentGenericAPIView

urlpatterns = [
    path("post-student/", studentGenericAPIView.as_view(), name="post_student"),
    path("get-student/", studentGenericAPIView.as_view(), name="get_student"),
    path(
        "put-student/<int:roll>/",
        studentGenericAPIView.as_view(),
        name="put_student",
    ),
    path(
        "patch-student/<int:roll>/",
        studentGenericAPIView.as_view(),
        name="patch_student",
    ),
    path(
        "delete-student/<int:roll>/",
        studentGenericAPIView.as_view(),
        name="delete_student",
    ),
]
