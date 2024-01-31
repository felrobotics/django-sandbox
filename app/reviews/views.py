from django.http import HttpResponseRedirect
from django.shortcuts import render

# Create your views here.


def review(request):
    print("DEBUG")
    print(request.method)
    if request.method == "POST":
        entered_username = request.POST["username"]
        print(entered_username)
        # validate
        if (not entered_username) or (len(entered_username) <= 10):
            return render(request, "reviews/review.html", {"has_error": True})

        return HttpResponseRedirect(redirect_to="thank-you")

    return render(request, "reviews/review.html", {"has_error": False})


def thank_you(request):
    return render(request, "reviews/thank_you.html")
