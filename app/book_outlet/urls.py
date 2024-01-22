from django.contrib import admin
from django.urls import path, re_path
from django.views.generic import RedirectView

from . import views

urlpatterns = [
    path("", views.index),
    path("<int:id>", views.book_detail, name="book_detail"),
    path("<slug:slug>", views.book_detail, name="book_detail"),
]
