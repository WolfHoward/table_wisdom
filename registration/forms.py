from django import forms
from django.forms import ModelForm

from registration.models import User

class UserForm(ModelForm):
    password = forms.CharField(widget=forms.PasswordInput())
    confirm_password=forms.CharField(widget=forms.PasswordInput())
    class Meta:
        model = User
        fields = ['firstName', 'lastName', 'username', 'email']

    # def clean(self):
    #     cleaned_data = super(UserForm, self).clean()
    #     password = cleaned_data.get("password")
    #     confirm_password = cleaned_data.get("confirm_password")
    #
    #     if password != confirm_password:
    #         raise forms.ValidationError(
    #             "Passwords do not match"
    #         )

# class UserProfileForm(ModelForm):
#     class Meta:
#         model = User
#         exclude = ['username']
