# -*- coding: utf-8 -*-
# Generated by Django 1.10 on 2018-12-14 09:17
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='WelcomeMessage',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(db_index=True, max_length=200)),
                ('welcomeVideoImage', models.ImageField(upload_to='carousel/%Y/%m/%d')),
                ('body', models.TextField()),
            ],
        ),
        migrations.AddField(
            model_name='slidercarousel',
            name='carouselButtonCharacter',
            field=models.CharField(db_index=True, default='Contact us', max_length=200),
            preserve_default=False,
        ),
    ]
