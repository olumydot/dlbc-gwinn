# -*- coding: utf-8 -*-
# Generated by Django 1.10 on 2018-12-14 09:17
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='OtherCloserLocations',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('location_Name', models.CharField(db_index=True, max_length=200)),
                ('location_Address', models.CharField(db_index=True, max_length=200)),
                ('location_PhoneNumber', models.CharField(max_length=12)),
                ('location_E_mail', models.EmailField(max_length=254)),
            ],
        ),
        migrations.CreateModel(
            name='OurContact',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Address', models.CharField(db_index=True, max_length=200)),
                ('PhoneNumber', models.CharField(max_length=12)),
                ('E_mail', models.EmailField(max_length=254)),
            ],
        ),
    ]
