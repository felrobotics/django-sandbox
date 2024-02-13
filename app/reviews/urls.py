from django.urls import path

from . import views

# fmt:off
urlpatterns = [
    path("", views.review),
    path("thank-you", views.thank_you),
    path("thank-you-view", views.ThankYouView.as_view()),
    path("thank-you-template-view", views.ThankYouTemplateView.as_view()),
    path("better-review", views.better_review),
    path("review-modelform", views.review_with_modelform),
    path("review-class", views.ReviewView.as_view()),
    path("reviews-template-view", views.ReviewListTemplateView.as_view()),
    path("reviews", views.ReviewListView.as_view()),
    path("single-review-template-view/<int:id>", views.SingleReviewTemplateView.as_view()),
    # DetailView needs primary key or slug
    path("review/<int:pk>", views.SingleReviewDetailView.as_view()),
    path("review-form-view", views.ReviewFormView.as_view()),
    path("review-create-view", views.ReviewCreateView.as_view()),

]
