from users import views
from django.contrib.auth import views as auth_views
from django.urls import path, reverse_lazy

urlpatterns = [
    path("", views.home, name="home"),
    path("register/", views.register, name="register"),
    path("login/", views.login_view, name="login"),
    path("logout/", views.logout_view, name="logout"),
    path("profile/", views.profile, name="profile"),
    path("change_password/", views.change_password, name="change_password"),
    path(
        "password/reset/",
        auth_views.PasswordResetView.as_view(
            template_name="user/password_reset.html",
            email_template_name="user/password_reset_email.html",
            subject_template_name="user/password_reset_subject.txt",
            success_url=reverse_lazy("password_reset_done"),
        ),
        name="password_reset",
    ),
    path(
        "password/reset/done/",
        auth_views.PasswordResetDoneView.as_view(
            template_name="user/password_reset_done.html",
        ),
        name="password_reset_done",
    ),
    path(
        "password/reset/<uidb64>/<token>/",
        auth_views.PasswordResetConfirmView.as_view(
            template_name="user/password_reset_confirm.html",
            success_url=reverse_lazy("password_reset_complete"),
        ),
        name="password_reset_confirm",
    ),
    path(
        "password/reset/complete/",
        auth_views.PasswordResetCompleteView.as_view(
            template_name="user/password_reset_complete.html",
        ),
        name="password_reset_complete",
    ),
]
