from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect, HttpResponseNotFound
from django.urls import reverse
from pathlib import Path


# Create your views here.

challenges = {
    "jan": "eat no meat!",
    "feb": "walk 20 min",
    "mar": "learn django",
    "apr": "meditate daily",
}


# Example 1. simple function view
# http://127.0.0.1:8000/challenges/example-1
def index_example_1(request):
    return HttpResponse("This Works!")


# Example 2
# http://127.0.0.1:8000/challenges/jan
def montly_challenge(request, month):
    return HttpResponse(challenges.get(month, "no valid month"))


# Example 3
# http://127.0.0.1:8000/challenges/1
def montly_challenge_by_int(request, month):
    months = list(challenges.keys())
    if month <= len(months) and month > 0:
        response = challenges[months[month - 1]]
    else:
        response = "invalid month"
    return HttpResponse(response)


# Example 4 (redirects from challenges-redirect/1 to challenges/jan)
# usage: http://127.0.0.1:8000/challenges/redirect/1
def challenge_redirect(request, month):
    months = list(challenges.keys())

    if month > len(months):
        return HttpResponseNotFound("invalid month!!!")

    if month <= len(months) and month > 0:
        month = months[month - 1]
    return HttpResponseRedirect("/challenges/" + str(month))


# Example 5 (named urls, useful for using reverse)
# http://127.0.0.1:8000/challenges/named/1
def challenge_named(request, month):
    months = list(challenges.keys())

    if month > len(months):
        return HttpResponseNotFound("invalid month!!!")

    if month <= len(months) and month > 0:
        redirect_month = months[month - 1]

    named_path = reverse("named-url", args=[month])

    return HttpResponse(
        f"""This path is dymically crated from named url <b>{named_path}</b>
          <br>
          However we could redirect to <b>{Path(named_path).parent.parent}/{redirect_month}</b> if we wish"""
    )
