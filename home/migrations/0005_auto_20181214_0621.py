# -*- coding: utf-8 -*-
# Generated by Django 1.10 on 2018-12-14 11:21
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0004_auto_20181214_0550'),
    ]

    operations = [
        migrations.CreateModel(
            name='SpecialEvent',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(db_index=True, max_length=200)),
                ('address', models.TextField()),
                ('flier', models.ImageField(upload_to='specialevent/%Y/%m/%d')),
            ],
        ),
        migrations.AlterModelOptions(
            name='iconbox',
            options={'verbose_name': 'Icon Box', 'verbose_name_plural': 'Icon Boxes'},
        ),
    ]
