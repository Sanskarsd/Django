from django.http import HttpResponseRedirect
from django.shortcuts import render
from django.views import View
from django.views.generic import CreateView, FormView, ListView

from reviews.models import Review
from .forms import ReviewForm
from django.views.generic.base import TemplateView
from django.views.generic.detail import DetailView

# Create your views here.

# def review(request):
#     if request.method == "POST":

#         form=ReviewForm(request.POST)

#         if form.is_valid():
#             print(form.cleaned_data)
#             print(form.data)

#             # Review.objects.create(
#             #     username=form.cleaned_data["username"],
#             #     password=form.cleaned_data["password"],
#             #     review_text=form.cleaned_data["review_text"],
#             #     ratings=form.cleaned_data["rating"]
#             # )


#             form.save()


#             return HttpResponseRedirect("/thank_you")


#     else:
#         form=ReviewForm()


#     return render(request, "reviews/review.html", {"form": form})


# class ReviewView(View):
#     def get(self, request):
#         form=ReviewForm()

#         return render(request, "reviews/review.html", {"form": form})

#     def post(self, request):
#         form=ReviewForm(request.POST)

#         if form.is_valid():
#             print(form.cleaned_data)
#             print(form.data)

#             # Review.objects.create(
#             #     username=form.cleaned_data["username"],
#             #     password=form.cleaned_data["password"],
#             #     review_text=form.cleaned_data["review_text"],
#             #     ratings=form.cleaned_data["rating"]
#             # )


#             form.save()


#             return HttpResponseRedirect("/thank_you")
#         else:
#             return render(request, "reviews/review.html", {"form": form})


# class ReviewView(FormView):
#     template_name = "reviews/review.html"
#     form_class = ReviewForm
#     success_url = "/thank_you"

#     def form_valid(self, form):
#         form.save()
#         return super().form_valid(form)


class ReviewView(CreateView):
    model = Review
    template_name = "reviews/review.html"
    form_class = ReviewForm
    success_url = "/thank_you"


class ThankYouView(TemplateView):
    template_name = "reviews/thank_you.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["message"] = "This works!"
        return context


class ReviewsListView(ListView):
    template_name = "reviews/review_list.html"
    model = Review
    context_object_name = "reviews"


class ReviewDetailView(DetailView):
    model = Review
    template_name = "reviews/review_detail.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        loaded_review = self.object
        request = self.request
        context["is_favourite"] = request.session.get("favourite_review") == str(
            loaded_review.id
        )
        return context


class AddFavoriteView(View):
    def post(self, request):
        review_id = request.POST.get("review_id")
        review = Review.objects.get(pk=review_id)

        request.session["favourite_review"] = review_id
        return HttpResponseRedirect("/reviews/" + review_id)
