# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2018-11-02 13:59
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('photo', '0002_auto_20181102_1556'),
    ]

    operations = [
        migrations.AddField(
            model_name='image',
            name='image',
            field=models.ImageField(blank=True, upload_to='images/'),
        ),
    ]
