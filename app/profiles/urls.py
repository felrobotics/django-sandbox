from django.urls import path

from . import views

urlpatterns = [
    path("", views.CreateProfileView.as_view()),
    path("with-form", views.CreateProfileWithFormView.as_view()),
    path("with-model-and-form", views.CreateProfileWithModelAndFormView.as_view()),
    path("with-create-view", views.CreateProfileCreateView.as_view()),
    path("profiles-list", views.ProfilesView.as_view()),
]
