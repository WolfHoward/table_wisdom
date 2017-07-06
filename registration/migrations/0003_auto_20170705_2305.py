# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2017-07-06 04:05
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('registration', '0002_item_text'),
    ]

    operations = [
        migrations.CreateModel(
            name='User',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('discipline', models.TextField(default='')),
                ('music', models.TextField(default='')),
            ],
        ),
        migrations.DeleteModel(
            name='Item',
        ),
    ]
