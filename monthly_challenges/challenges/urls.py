from django.urls import path
from challenges import views

urlpatterns = [
    path("", views.index, name="index"),
    path("<int:month>/", views.challenge_by_monthnumber),
    path("<str:month>/", views.challenge_by_month, name="month-challenge"),
]

# <> is place holder so we can use any month name in place of <month> and it will be passed to the function challenge_by_month as an argument.
