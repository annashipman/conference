from django import forms


class SubmitSessionForm(forms.Form):
    title = forms.CharField()
    first_name = forms.CharField()
    last_name = forms.CharField()
    email = forms.EmailField(required=False)
