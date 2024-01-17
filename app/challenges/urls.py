from django.contrib import admin
from django.urls import path, include

from . import views

urlpatterns = [
    path("example-1", views.index_example_1),
    path("<int:month>", views.montly_challenge_by_int),
    path("<str:month>", views.montly_challenge),
    path("redirect/<int:month>", views.challenge_redirect),  # learn redirects
    path("named/<int:month>", views.challenge_named, name="named-url"),  # learn named
]
