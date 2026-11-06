from django.urls import path
from .views import RegisterView

urlpatterns = [path("test3/", RegisterView)]
