# -*- coding: utf-8 -*-
# Generated by Django 1.10 on 2018-12-17 00:05
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('about_us', '0003_aboutuspix'),
    ]

    operations = [
        migrations.CreateModel(
            name='Beliefs2',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('header', models.CharField(db_index=True, max_length=200)),
                ('body', models.CharField(db_index=True, max_length=5000)),
            ],
        ),
        migrations.CreateModel(
            name='Beliefs3',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('header', models.CharField(db_index=True, max_length=200)),
                ('body', models.CharField(db_index=True, max_length=5000)),
            ],
        ),
        migrations.RenameModel(
            old_name='Beliefs',
            new_name='Beliefs1',
        ),
    ]
