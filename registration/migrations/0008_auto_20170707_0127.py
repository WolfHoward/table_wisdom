# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2017-07-07 06:27
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('registration', '0007_auto_20170706_1522'),
    ]

    operations = [
        migrations.RenameField(
            model_name='user',
            old_name='email',
            new_name='Email',
        ),
        migrations.RenameField(
            model_name='user',
            old_name='first_name',
            new_name='First Name',
        ),
        migrations.RenameField(
            model_name='user',
            old_name='last_name',
            new_name='Last Name',
        ),
        migrations.RenameField(
            model_name='user',
            old_name='password',
            new_name='Password',
        ),
        migrations.RenameField(
            model_name='user',
            old_name='user_name',
            new_name='Username',
        ),
    ]
