from django import forms


class ProfileForm(forms.Form):
    # user_image = forms.FileField() # the first exercise was with File
    user_image = forms.ImageField()  # we change it to Image which is more specialized
