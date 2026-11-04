
from django.urls import path

from book_outlet import views


urlpatterns = [
    path("book/",views.book_outlet,name="book_outlet"),
    path("book/<slug:slug>/",views.book_detail,name="book_detail"),
]
