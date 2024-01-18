from django.contrib import admin
from django.urls import path, re_path, include
from django.views.generic import RedirectView

from . import views

urlpatterns = [
    path("", views.index, name="index"),  # index -> /challenges
    path("index-with-template", views.index_with_template),
    path("example-1", views.index_example_1),
    path("<int:month>", views.montly_challenge_by_int),
    path("<str:month>", views.montly_challenge, name="month-challenge-with-arg"),
    path("redirect/<int:month>", views.challenge_redirect),  # learn redirects
    path("named/<int:month>", views.challenge_named, name="named-url"),  # learn named
    path("render-to-string/<str:month>", views.challenge_with_render_to_string),
    path("render-template/<str:month>", views.challenge_with_render_template),
    path("with-404-template/<str:month>", views.montly_challenge_with_404),
]
