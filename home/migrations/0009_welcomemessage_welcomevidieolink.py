# -*- coding: utf-8 -*-
# Generated by Django 1.10 on 2018-12-17 01:09
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0008_quotableimage_quotablequotes'),
    ]

    operations = [
        migrations.AddField(
            model_name='welcomemessage',
            name='welcomeVidieoLink',
            field=models.CharField(default='www.youtube.com', max_length=200),
            preserve_default=False,
        ),
    ]
