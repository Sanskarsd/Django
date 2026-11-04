from django.shortcuts import redirect, render
from django.contrib.auth import login, logout
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from django.contrib.auth import update_session_auth_hash
from django.contrib.auth.forms import PasswordChangeForm
from users.forms import LoginForm, RegisterForm

# Create your views here.


def register(request):
    if request.user.is_authenticated:
        return render(request, "user/profile.html")
    if request.method == "POST":
        form = RegisterForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get("username")
            messages.success(request, f"Welcome {username}, Your account is created")
            return redirect("login")

    else:
        form = RegisterForm()

    return render(request, "user/register.html", {"form": form})


def login_view(request):
    if request.user.is_authenticated:
        return render(request, "user/profile.html")
    if request.method == "POST":
        form = LoginForm(request, data=request.POST)
        if form.is_valid():
            username = form.cleaned_data.get("username")
            login(request, form.get_user())
            messages.success(request, f"Welcome {username}, You are logged in")
            return redirect("profile")
    else:
        form = LoginForm()
    return render(request, "user/login.html", {"form": form})


@login_required
def profile(request):
    return render(request, "user/profile.html")


def logout_view(request):
    if request.user.is_authenticated:
        logout(request)
        messages.success(request, "You are logged out")
        return redirect("login")
    else:
        return redirect("login")


@login_required
def change_password(request):

    if request.method == "POST":
        form = PasswordChangeForm(user=request.user, data=request.POST)

        if form.is_valid():
            user = form.save()
            update_session_auth_hash(request, user)
            return redirect("profile")
    else:

        form = PasswordChangeForm(user=request.user)
    return render(request, "user/change_password.html", {"form": form})


def home(request):
    if request.user.is_authenticated:
        return redirect("profile")

    return redirect("login")
