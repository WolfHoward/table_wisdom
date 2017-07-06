from django.db import models

# Create your models here.
class User(models.Model):
    discipline = models.TextField(default='')
    # music = models.TextField(default='')
