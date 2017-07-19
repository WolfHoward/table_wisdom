from django.db import models
from django.forms import ModelForm

# Create your models here.
class User(models.Model):
    username = models.CharField(default='', max_length=150, name="username")
    password = models.CharField(default='', max_length=50, name="password")
    email = models.EmailField(default='', max_length=150, name="email")
    first_name = models.CharField(default='', max_length=100, name="firstname")
    last_name = models.CharField(default='', max_length=100, name="lastname")
    is_active = models.BooleanField(default=False)
    discipline = models.CharField(default='', max_length=100, name="discipline")
    hobbies = models.CharField(default='', max_length=200, name="hobbies")


# class UserForm(models.Model):
#     class Meta:
#         model = User
#         exclude = ['user_name']
