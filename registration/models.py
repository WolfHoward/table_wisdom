from django.db import models

# Create your models here.
class User(models.Model):
    first_name = models.TextField(default='')
    last_name = models.TextField(default='')
    user_name = models.CharField(default='', max_length=150)
    email = models.CharField(default='',max_length=150)
    password = models.CharField(default='', max_length=50)
