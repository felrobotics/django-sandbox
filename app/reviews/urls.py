from django.urls import path

from . import views

# fmt:off
urlpatterns = [
    path("", views.review),
    path("thank-you", views.thank_you),
    path("better-review", views.better_review)
]
