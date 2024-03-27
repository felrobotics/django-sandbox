from django.contrib import admin
from django.urls import path, re_path
from django.views.generic import RedirectView

from . import views

urlpatterns = [
    path("", views.starting_page, name="starting-page"),  # posts (starting page)
    path("list", views.posts, name="posts-page"),
    # posts/my-first-post
    # posts/programming-is-fun
    path("<slug:slug>", views.single_post, name="single-post"),
]
