from django.db import models
from django.forms import ModelForm

# Create your models here.
class User(models.Model):
    first_name = models.CharField(default='', max_length=100, name="First Name")
    last_name = models.CharField(default='', max_length=100, name="Last Name")
    user_name = models.CharField(default='', max_length=150, name="Username")
    email = models.EmailField(default='', max_length=150, name="Email")
    password = models.CharField(default='', max_length=50, name="Password")

#
# class UserForm(ModelForm):
#     class Meta:
#         model = User
#         fields = ['first_name', 'last_name', 'user_name', 'email', 'password']
