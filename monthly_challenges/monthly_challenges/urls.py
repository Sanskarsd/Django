from django.contrib import admin
from django.urls import include, path
from django.shortcuts import redirect
from django.urls import re_path

urlpatterns = [
    path("admin/", admin.site.urls),
    path("challenge/", include("challenges.urls")),
 ]
