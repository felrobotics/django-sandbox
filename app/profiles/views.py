from django.http import HttpResponseRedirect
from django.shortcuts import render
from django.views import View
from django.views.generic import ListView
from django.views.generic.edit import CreateView

from .forms import ProfileForm
from .models import UserProfile

# Create your views here.


def store_file(file):
    with open("temp/image.jpg", "wb+") as dest:
        for chunk in file.chunks():
            dest.write(chunk)


class CreateProfileView(View):

    def get(self, request):
        return render(request, "profiles/create_profile.html")

    def post(self, request):
        """Django gives access not only to request.POST but to request.FILES"""
        store_file(request.FILES["image"])
        return HttpResponseRedirect("/profiles")


# Same as above but now using a form
class CreateProfileWithFormView(View):
    def get(self, request):
        form = ProfileForm()
        return render(
            request,
            "profiles/create_profile_with_form.html",
            {"form": form, "action": "/profiles/with-form"},
        )

    def post(self, request):
        """Django gives access not only to request.POST but to request.FILES"""

        submitted_form = ProfileForm(request.POST, request.FILES)

        if submitted_form.is_valid():
            print("@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@form valid!")
            store_file(request.FILES["user_image"])
            return HttpResponseRedirect("/profiles/with-form")

        return render(
            request,
            "profiles/create_profile_with_form.html",
            {"form": submitted_form, "action": "/profiles/with-form"},
        )


# Same as above but now using a model and a form
class CreateProfileWithModelAndFormView(View):
    def get(self, request):
        form = ProfileForm()
        return render(
            request,
            "profiles/create_profile_with_form.html",
            {"form": form, "action": "/profiles/with-model-and-form"},
        )

    def post(self, request):
        """Django gives access not only to request.POST but to request.FILES"""

        submitted_form = ProfileForm(request.POST, request.FILES)
        print(request.FILES)

        if submitted_form.is_valid():
            profile = UserProfile(image=request.FILES["user_image"])
            profile.save()
            # store_file(request.FILES["user_image"])
            return HttpResponseRedirect("/profiles/with-model-and-form")

        return render(
            request,
            "profiles/create_profile_with_form.html",
            {"form": submitted_form, "action": "/profiles/with-model-and-form"},
        )


# Let's use the more specialized CreateView, so we do not need to add get and post
# with CreateView you do not need to create a Form ProfileForm, because django does it
# under the hood
class CreateProfileCreateView(CreateView):
    template_name = "profiles/create_profile_with_form.html"
    model = UserProfile
    fields = "__all__"
    success_url = "/profiles/with-create-view"


class ProfilesView(ListView):
    model = UserProfile
    template_name = "profiles/user_profiles.html"
    context_object_name = "profiles"
