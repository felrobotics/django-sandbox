from django.contrib import admin
from django.urls import path, re_path, include
from django.views.generic import RedirectView

from . import views

urlpatterns = [
    path("", views.starting_page, name="starting-page"),  # starting page
    path("list", views.posts, name="posts-page"),
    path("<slug:slug>", views.single_post, name="single-post"),  # posts/my-first-post
]
