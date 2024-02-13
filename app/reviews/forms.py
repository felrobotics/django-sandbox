from django import forms

from .models import Review


class ReviewForm(forms.Form):
    # user_name = CharField(max_length=30) # basic
    # overriding defaults
    user_name = forms.CharField(
        label="Your Name",
        max_length=30,
        required=True,
        error_messages={
            "required": "Your name must not be empty",
            "max_length": "Please enter shorter name!",
        },
    )
    # textarea to enter longer texts
    review_text = forms.CharField(
        label="Your Feedback", widget=forms.Textarea, max_length=200
    )
    rating = forms.IntegerField(label="Your Rating", min_value=1, max_value=5)


# above approach is ok, but there is a common use case, which is a form that
# collects data and is connected with a model: ModelForms.
# this has the advantange of reducing code because form fields come from model


class ReviewModelForm(forms.ModelForm):
    """We connect Model Form with a model, and django will automatically create
    the fields."""

    class Meta:
        model = Review
        fields = [
            "user_name",
            "review_text",
            "rating",
        ]  # you can cherry pick some filds
        fields = "__all__"  # if you need all, this is the shortcut
        # alternatively you can render __all__ but exclude one or several with exclude
        # exclude = ["rating"]
        labels = {
            "user_name": "Your Name!",
            "review_text": "Your Feedback!",
            "rating": "Your Rating!",
        }
        widgets = {
            "review_text": forms.Textarea(attrs={"rows": 10}),
        }
        error_messages = {
            "user_name": {
                "required": "Your name must not be empty",
                "max_length": "Please enter shorter name!",
            },
        }
