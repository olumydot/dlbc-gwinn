# -*- coding: utf-8 -*-
# Generated by Django 1.10 on 2018-12-19 16:46
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('livestream', '0002_auto_20181219_1137'),
    ]

    operations = [
        migrations.AddField(
            model_name='livestream',
            name='description',
            field=models.CharField(blank=True, max_length=300),
        ),
    ]
