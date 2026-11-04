from django.http import HttpResponseRedirect
from django.shortcuts import render
from django.views import View
from django.views.generic import CreateView, ListView
from .forms import ProfileForm
from .models import UserProfile

# Create your views here.


# class CreateProfileView(View):
#     def get(self, request):
#         form = ProfileForm()
#         return render(request, "profiles/create_profile.html", {"form": form})

#     def post(self, request):
#         form = ProfileForm(request.POST, request.FILES)
#         if form.is_valid():
#             profile = UserProfile(user_image=request.FILES["user_image"])
#             profile.save()
#             return HttpResponseRedirect("/profiles/")
#         else:
#             return render(request, "profiles/create_profile.html", {"form": form})


class CreateProfileView(CreateView):
    model = UserProfile
    fields = "__all__"
    template_name = "profiles/create_profile.html"
    success_url = "/profiles/"


class ProfileListView(ListView):
    model = UserProfile
    template_name = "profiles/user_profile.html"
    context_object_name = "profiles"
