from django.db import models
from django.forms import ModelForm

# Create your models here.
class User(models.Model):
    first_name = models.CharField(default='', max_length=100, name="firstName")
    last_name = models.CharField(default='', max_length=100, name="lastName")
    username = models.CharField(default='', max_length=150, name="username")
    email = models.EmailField(default='', max_length=150, name="email")
    password = models.CharField(default='', max_length=50, name="password")

    def __str__(self):
        return self.username
#
# class UserForm(models.Model):
#     class Meta:
#         model = User
#         exclude = ['user_name']
