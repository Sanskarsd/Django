from django.urls import path
from . import views
from .views import ProfileAPIView

urlpatterns = [
    path("", views.home, name="home"),
    path("post-profile/", views.post_profile, name="post_profile"),
    path("get-profile/", views.get_profile, name="get_profile"),
    path("put-profile/<str:uname>/", views.put_profile, name="put_profile"),
    path("patch-profile/<str:uname>/", views.patch_profile, name="patch_profile"),
    path("delete-profile/<str:uname>/", views.delete_profile, name="delete_profile"),
    path("classAPIView/", ProfileAPIView.as_view()),
]
