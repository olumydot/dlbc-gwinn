# -*- coding: utf-8 -*-
# Generated by Django 1.10 on 2018-12-19 02:13
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('sermons_live', '0005_sermon_details_text'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='sermon',
            options={'ordering': ('name',), 'verbose_name': 'sermon', 'verbose_name_plural': 'sermons'},
        ),
    ]
