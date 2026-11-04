from django.http import Http404, HttpResponse, HttpResponseNotFound, HttpResponseRedirect
from django.shortcuts import render
from django.urls import reverse
from django.template.loader import render_to_string

# Create your views here.
# def january(request):
#     return HttpResponse("This works for January!")

# def february(request):
#     return HttpResponse("This works for February!")

challenges = {
    "january": "This works for January!",
    "february": "This works for February!",
    "march": "This works for March!",
    "april": "This works for April!",
    "may": "This works for May!",
    "june": "This works for June!",
    "july": "This works for July!",
    "august": "This works for August!",
    "september": "This works for September!",
    "october": "This works for October!",
    "november": "This works for November!",
    "december": None,
}


def index(request):
    return render(request, "challenges/index.html", {"months": list(challenges.keys())})


def challenge_by_month(request, month):

    try:
        # challenge_text = challenges[month]
        # respose_data = render_to_string("challenges/challenge.html")
        # return HttpResponse(respose_data)
        return render(
            request,
            "challenges/challenge.html",
            {"text": challenges[month], "month_name": month},
        )
    except:
        raise Http404(f"This month {month} is not supported!")


def challenge_by_monthnumber(request, month):

    months = list(challenges.keys())[month - 1]
    redirect_path = reverse("month-challenge", args=[months])
    if months in challenges:
        return HttpResponseRedirect(redirect_path)
    else:
        raise Http404("Invalid month number!")
