# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2018-11-02 12:56
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('photo', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='image',
            name='image_name',
            field=models.CharField(max_length=30),
        ),
    ]
