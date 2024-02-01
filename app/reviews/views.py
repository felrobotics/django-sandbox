from django.http import HttpResponseRedirect
from django.shortcuts import render

from .forms import ReviewForm

# Create your views here.


def review(request):
    if request.method == "POST":
        entered_username = request.POST["username"]
        print(entered_username)
        # validate
        if (not entered_username) or (
            len(entered_username) <= 4 or len(entered_username) >= 30
        ):
            return render(request, "reviews/review.html", {"has_error": True})

        return HttpResponseRedirect(redirect_to="thank-you")

    return render(request, "reviews/review.html", {"has_error": False})


# http://127.0.0.1:8000/feedback/better-review
def better_review(request):
    if request.method == "POST":
        form = ReviewForm(request.POST)
        if form.is_valid():
            print(form.cleaned_data)
            return HttpResponseRedirect(redirect_to="thank-you")
        else:
            print("form not valid!")
    form = ReviewForm()
    return render(request, "reviews/better_review.html", {"form": form})


def thank_you(request):
    return render(request, "reviews/thank_you.html")
