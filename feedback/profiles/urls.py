from django.views import static

from . import views
from django.urls import path
from django.conf import settings

urlpatterns = [
    path("", views.CreateProfileView.as_view()),
    path("list/", views.ProfileListView.as_view(), name="profile_list"),
]
