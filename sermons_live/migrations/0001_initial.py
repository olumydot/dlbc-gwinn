# -*- coding: utf-8 -*-
# Generated by Django 1.10 on 2018-12-18 19:25
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('leadership', '0006_auto_20181217_0325'),
    ]

    operations = [
        migrations.CreateModel(
            name='Sermon',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(db_index=True, max_length=200)),
                ('slug', models.SlugField(max_length=200, unique=True)),
            ],
            options={
                'ordering': ('name',),
                'verbose_name_plural': 'sermon',
                'verbose_name': 'sermon',
            },
        ),
        migrations.CreateModel(
            name='Sermon_details',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('slug', models.SlugField(max_length=200)),
                ('preacher', models.CharField(blank=True, max_length=200)),
                ('image', models.ImageField(blank=True, upload_to='')),
                ('details', models.TextField(blank=True)),
                ('audio_link', models.CharField(blank=True, max_length=200)),
                ('video_link', models.CharField(blank=True, max_length=200)),
                ('download_link', models.CharField(blank=True, max_length=200)),
                ('date', models.DateTimeField(auto_now=True)),
                ('preacher_name', models.ForeignKey(blank=True, on_delete=django.db.models.deletion.CASCADE, related_name='leaders_details', to='leadership.Leadership')),
                ('sermon_name', models.ForeignKey(blank=True, on_delete=django.db.models.deletion.CASCADE, related_name='sermons_details', to='sermons_live.Sermon')),
            ],
            options={
                'ordering': ('sermon_name',),
                'verbose_name_plural': 'details',
                'verbose_name': 'detail',
            },
        ),
        migrations.AlterIndexTogether(
            name='sermon_details',
            index_together=set([('id', 'slug')]),
        ),
    ]
