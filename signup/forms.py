from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User

class SignUpForm(UserCreationForm):
    first_name = forms.CharField(max_length=50, required=True)
    last_name = forms.CharField(max_length=50, required=True)
    email = forms.EmailField(max_length=254)

    class Meta:
        model = User
        fields = ('username', 'first_name', 'last_name', 'email', 'password1', 'password2', )


# from django.forms import ModelForm
#
# from signups.models import User
#
# class UserForm(ModelForm):
#     password = forms.CharField(widget=forms.PasswordInput())
#     confirm_password=forms.CharField(widget=forms.PasswordInput())
#     class Meta:
#         model = User
#         fields = ['firstname', 'lastname', 'username', 'email']

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
