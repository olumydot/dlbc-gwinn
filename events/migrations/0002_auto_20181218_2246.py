# -*- coding: utf-8 -*-
# Generated by Django 1.10 on 2018-12-19 03:46
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('ministries', '0002_auto_20181218_1237'),
        ('events', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Event_details',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('slug', models.SlugField(max_length=200)),
                ('image', models.ImageField(blank=True, upload_to='')),
                ('description', models.TextField(blank=True)),
                ('cost', models.CharField(max_length=100)),
                ('start_date', models.DateField()),
                ('end_date', models.DateField()),
                ('start_time', models.TimeField()),
                ('end_time', models.TimeField()),
                ('venue_name', models.CharField(max_length=200)),
                ('venue_address', models.CharField(max_length=200)),
                ('venue_map_address', models.CharField(max_length=200)),
                ('contact_name', models.CharField(max_length=100)),
                ('contact_phone', models.CharField(blank=True, max_length=200)),
                ('contact_email', models.EmailField(blank=True, max_length=254)),
                ('event_website', models.CharField(blank=True, max_length=200)),
                ('date', models.DateTimeField()),
                ('special', models.BooleanField(default=False)),
                ('featured', models.BooleanField(default=False)),
            ],
            options={
                'verbose_name_plural': 'details',
                'ordering': ('event_name',),
                'verbose_name': 'detail',
            },
        ),
        migrations.AlterModelOptions(
            name='event',
            options={'ordering': ('name',), 'verbose_name': 'event', 'verbose_name_plural': 'events'},
        ),
        migrations.RenameField(
            model_name='event',
            old_name='EventName',
            new_name='name',
        ),
        migrations.RemoveField(
            model_name='event',
            name='EventDescription',
        ),
        migrations.RemoveField(
            model_name='event',
            name='EventEndDateTime',
        ),
        migrations.RemoveField(
            model_name='event',
            name='EventFlier',
        ),
        migrations.RemoveField(
            model_name='event',
            name='EventSpeaker',
        ),
        migrations.RemoveField(
            model_name='event',
            name='EventStartDateTime',
        ),
        migrations.RemoveField(
            model_name='event',
            name='EventVenue',
        ),
        migrations.RemoveField(
            model_name='event',
            name='Notes',
        ),
        migrations.AddField(
            model_name='event_details',
            name='event_name',
            field=models.ForeignKey(blank=True, on_delete=django.db.models.deletion.CASCADE, related_name='events_details', to='events.Event'),
        ),
        migrations.AddField(
            model_name='event_details',
            name='ministry_name',
            field=models.ForeignKey(blank=True, on_delete=django.db.models.deletion.CASCADE, related_name='ministrys_details', to='ministries.Ministry'),
        ),
        migrations.AlterIndexTogether(
            name='event_details',
            index_together=set([('id', 'slug')]),
        ),
    ]
