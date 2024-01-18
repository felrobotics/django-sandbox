from django.shortcuts import render
from django.http import (
    HttpResponse,
    HttpResponseRedirect,
    HttpResponseNotFound,
    Http404,
)
from django.urls import reverse
from pathlib import Path
from django.template.loader import render_to_string
from django.conf.urls import handler404


# Create your views here.

challenges = {
    "jan": "eat no meat!",
    "feb": "walk 20 min",
    "mar": "learn django",
    "apr": "meditate daily",
}


# Example 0. index
# http://127.0.0.1:8000/challenges
# http://127.0.0.1:8000/challenges/  # this one will be redirected without slash
def index(request):
    list_items = ""
    # months = list(challenges.keys())

    for month in challenges.keys():
        month_path = reverse("index")
        list_items += f'<li><a href="{month_path}{month}">{month.capitalize()}</a></li>'

    response = f"<ul>{list_items}<ul>"
    return HttpResponse(response)


# Example 1. simple function view
# http://127.0.0.1:8000/challenges/example-1
def index_example_1(request):
    return HttpResponse("This Works!")


# Example 2
# http://127.0.0.1:8000/challenges/jan = list(challenges.keys())/jan
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


# Example 6 using template
# http://127.0.0.1:8000/challenges/render-to-string/jan
def challenge_with_render_to_string(request, month):
    text = challenges.get(month, "no valid month")
    response = render_to_string(
        "challenges/challenge.html", context={"month": month, "text": text}
    )
    return HttpResponse(response)


# Example 7 using template
# http://127.0.0.1:8000/challenges/render-template/jan
def challenge_with_render_template(request, month):
    text = challenges.get(month, "no valid month")
    return render(
        request, "challenges/challenge.html", context={"month": month, "text": text}
    )


# Example 8. index with template
# http://127.0.0.1:8000/challenges/index-with-template
def index_with_template(request):
    months = challenges.keys()
    return render(request, "challenges/index.html", {"months": months})


# Example 9 montly challenges with 404 template
# http://127.0.0.1:8000/challenges/with-404-template/febwrong
def montly_challenge_with_404(request, month):
    try:
        text = challenges[month]
        return render(
            request, "challenges/challenge.html", context={"month": month, "text": text}
        )
    except Exception as e:
        response = (
            render_to_string("errors/404.html") + "HELLO we have an e = " + str(e)
        )
        return HttpResponseNotFound(response)  # Important it will send a 404
        # above will work but you can use raise Http404
        # raise Http404()  # standard 404 not found


# Example 10 404 with template using handler404 see: (https://studygyaan.com/django/django-custom-404-error-template-page)
# http://127.0.0.1:8000/non-existing
def custom_404(request, exception):
    return render(request, "errors/404.html", status=404)
