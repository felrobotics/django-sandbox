from django.contrib import admin
from django.urls import path, re_path
from django.views.generic import RedirectView

from . import views

urlpatterns = [
    path("", views.starting_page, name="starting-page"),  # posts (starting page)
    path("with-class", views.StartingPageView.as_view(), name="starting-page-class"),
    path("list", views.posts, name="posts-page"),
    path("<slug:slug>", views.single_post, name="single-post"),
    # using classes
    path("with-class/list", views.AllPostsView.as_view(), name="posts-page-class"),
    path("with-class/read-later", views.ReadLaterView.as_view(), name="read-later"),
    path(
        "with-class/<slug:slug>",
        views.SinglePostView.as_view(),
        name="single-post-view",
    ),
]
