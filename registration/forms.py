from django import forms
from django.forms import ModelForm

from registration.models import User

class UserForm(ModelForm):
    password = forms.CharField(widget=forms.PasswordInput())
    confirm_password=forms.CharField()
    class Meta:
        model = User
        fields = ['First Name', 'Last Name', 'Username', 'Email']

    def clean(self):
        cleaned_data = super(UserForm, self).clean()
        password = cleaned_data.get("password")
        confirm_password = cleaned_data.get("confirm_password")

        if password != confirm_Password:
            raise forms.ValidationError(
                "Passwords do not match"
            )
