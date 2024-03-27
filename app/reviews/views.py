from typing import Any

from django.db.models.query import QuerySet
from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render
from django.views import View
from django.views.generic import DetailView, ListView
from django.views.generic.base import TemplateView
from django.views.generic.edit import CreateView, FormView

from .forms import ReviewForm, ReviewModelForm
from .models import Review


# Create your views here.
def review(request):
    if request.method == "POST":
        entered_username = request.POST["username"]
        print(entered_username)
        # validate
        if (not entered_username) or (
            len(entered_username) <= 4 or len(entered_username) >= 30
        ):
            return render(request, "reviews/review.html", {"has_error": True})

        return HttpResponseRedirect(redirect_to="thank-you")

    return render(request, "reviews/review.html", {"has_error": False})


# http://127.0.0.1:8000/feedback/better-review
def better_review(request):
    if request.method == "POST":
        form = ReviewForm(request.POST)
        if form.is_valid():
            # first steps is to print, but since we created a model, let's store
            # the data in the db
            print(form.cleaned_data)  # only print
            # use the model to store data in db
            review = Review(
                user_name=form.cleaned_data["user_name"],
                review_text=form.cleaned_data["review_text"],
                rating=form.cleaned_data["rating"],
            )
            review.save()
            return HttpResponseRedirect(redirect_to="thank-you")
        else:
            print("Form not valid!")
    form = ReviewForm()
    return render(request, "reviews/better_review.html", {"form": form})


def review_with_modelform(request):
    if request.method == "POST":
        # if we use instance= we update instead of create new entry
        form = ReviewModelForm(request.POST)
        if form.is_valid():
            form.save()  # easier!
            return HttpResponseRedirect(redirect_to="thank-you")
        else:
            print("Form not valid!!!")
    form = ReviewModelForm()
    return render(request, "reviews/better_review.html", {"form": form})

    # in case you want to uptade rather than inser new data, please
    # check "Save Data with a ModelForm (147) t 3:00 "


# All views above are functions, Let's create a class view and see
# some advantages. View is generic view, but there are more specialized
# views such ListView, DetailedView, FormView, etc


class ReviewView(View):
    """This view can be even made simplier using as shown below FormView, we save to write the get and post methods"""

    def get(self, request):
        form = ReviewModelForm()
        return render(request, "reviews/better_review.html", {"form": form})

    def post(self, request):
        form = ReviewModelForm(request.POST)
        if form.is_valid():
            form.save()  # easier!
            return HttpResponseRedirect(redirect_to="thank-you")
        else:
            print("Form not valid!!!")
        return render(request, "reviews/better_review.html", {"form": form})


def thank_you(request):
    return render(request, "reviews/thank_you.html")


# let's rewrite the thank you view function as a class


class ThankYouView(View):
    def get(self, request):
        return render(request, "reviews/thank_you.html")


# This view is specialized
class ThankYouTemplateView(TemplateView):
    template_name = "reviews/thank_you.html"

    def get_context_data(self, **kwargs):
        "this is the method to get context data"
        context = super().get_context_data(**kwargs)
        # we can add e.g a message here
        context["message"] = "This message works!!"
        return context


class ReviewListTemplateView(TemplateView):
    """This is not the most direct way to list with a template.
    This a very common use case, therefore better to use ListView.
    """

    template_name = "reviews/review_list.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        reviews = Review.objects.all()
        context["reviews"] = reviews
        return context


class ReviewListView(ListView):
    """Much simpler than using a TemplateView for list case"""

    template_name = "reviews/review_list.html"
    model = Review
    # to rename default object_list, to review better for the template
    context_object_name = "reviews"

    # if you do not define get_queryset, by default will return all objects
    # here is example to filter some objects by rating. I will comment it
    # to display all objects
    # def get_queryset(self):
    #     base_query = super().get_queryset()
    #     data = base_query.filter(rating__gt=2)
    #     return data


class SingleReviewTemplateView(TemplateView):
    """This is not the most direct way to show a single review
    with a TemplateView. This a very common use case, therefore
    better to use DetailView.
    """

    template_name = "reviews/single_review.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        review_id = context["id"]
        selected_review = Review.objects.get(pk=review_id)
        context["review"] = selected_review
        return context


# http://127.0.0.1:8000/feedback/review/1
class SingleReviewDetailView(DetailView):
    """This saves a lot of code, in the template you can use the model
    in lowercase, in this example review or object (review.name or object.name)
    both work."""

    template_name = "reviews/single_review.html"
    model = Review

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        loaded_review_id = self.object.id
        favorite_id = self.request.session.get["favorite_review"]
        context["is_favorite"] = favorite_id == str(loaded_review_id)
        return context


class ReviewFormView(FormView):
    """More specialized view than above generic View, which handles forms easier.
    With these two following fields, django is able to handle alone the get and post
    methods.

    There are even more specialized views such as CreateView as shown below.
    """

    form_class = ReviewModelForm
    template_name = "reviews/better_review.html"

    # you can customize some methods, e.g form.is_valid ?
    def form_valid(self, form):
        form.save()
        return super().form_valid(form)


class ReviewCreateView(CreateView):
    """This is very specialized, we don't even need a form. It builds up everything
    starting from a model
    The limitation is that you cannot create labels and error messages unless you
    modify the form
    There are also forms for DELETE and UPDATE data"""

    model = Review
    template_name = "reviews/better_review.html"
    fields = "__all__"
    success_url = "/thank-you"

    # Example to modify labels
    def get_form(self, form_class=None):
        form = super().get_form(form_class)
        form.fields["user_name"].label = "Your name (Edited within get_form)"
        return form


# Similar to CreateView there is:
# UpdateView
# DeleteView


class AddFavoriteView(View):
    def post(self, request):
        review_id = request.POST["review_id"]
        # favorite_review = Review.objects.get(pk=review_id)
        request.session["favorite_review"] = review_id
        return HttpResponseRedirect("/feedback/review/" + review_id)
