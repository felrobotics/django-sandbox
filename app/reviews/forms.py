from django.forms import CharField, Form


class ReviewForm(Form):
    # user_name = CharField(max_length=30) # basic
    # overriding defaults
    user_name = CharField(
        label="Your Name",
        max_length=30,
        required=True,
        error_messages={
            "required": "Your name must not be empty",
            "max_length": "Please enter shorter name!",
        },
    )
