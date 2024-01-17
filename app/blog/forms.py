from django import forms


class PostSearchForm(forms.Form):
    search_field = forms.CharField()

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields["search_field"].widget.attrs.update({"class": "form-control"})
