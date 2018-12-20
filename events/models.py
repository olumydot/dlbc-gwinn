from django.db import models
from django.core.urlresolvers import reverse
from ministries.models import Ministry


class Event(models.Model):
    name = models.CharField(max_length=200, db_index=True)  # adding db_index will help optimize lookups on this field
    slug = models.SlugField(max_length=200, db_index=True, unique=True)

    class Meta:
        ordering = ('name',)  # This is to order the database in ascending order of name
        verbose_name = 'event'  # in the admin site this is what will show in the model and not mangled python name
        verbose_name_plural = 'events'

    def __str__(self):
        # this is what is returned whenever a model instance is needed and coerced to be displayed as plain string

        return self.name

    def get_absolute_url(self):
        return reverse('events:event_list_by_name', args=[self.slug])


class Event_details(models.Model):
    event_name = models.ForeignKey(Event, related_name='events_details', blank=True)
    slug = models.SlugField(max_length=200, db_index=True)
    ministry_name = models.ForeignKey(Ministry, related_name='ministrys_details', blank=True)
    image = models.ImageField(blank=True)
    description = models.TextField(blank=True)
    cost = models.CharField(max_length=100)
    start_date = models.DateField()
    end_date = models.DateField()
    start_time = models.TimeField()
    end_time = models.TimeField()
    venue_name = models.CharField(max_length=200)
    venue_address = models.CharField(max_length=200)
    venue_map_address = models.CharField(max_length=200)
    contact_name = models.CharField(max_length=100)
    contact_phone = models.CharField(max_length=200, blank=True)
    contact_email = models.EmailField(blank=True)
    event_website = models.CharField(max_length=200, blank=True)
    special = models.BooleanField(default=False)
    featured = models.BooleanField(default=False)

    class Meta:
        ordering = ('event_name',)
        verbose_name = 'detail'  # in the admin site this is what will show in the model and not mangled python name
        verbose_name_plural = 'details'
        index_together = (('id', 'slug'),)

    def get_absolute_url(self):
        return reverse('events:event_detail', args=[self.id, self.slug])
