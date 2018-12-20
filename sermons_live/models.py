from django.db import models
from django.core.urlresolvers import reverse
from leadership.models import Leadership


class Sermon(models.Model):
    name = models.CharField(max_length=200, db_index=True)  # adding db_index will help optimize lookups on this field
    slug = models.SlugField(max_length=200, db_index=True, unique=True)

    class Meta:
        ordering = ('name',)  # This is to order the database in ascending order of name
        verbose_name = 'sermon'  # in the admin site this is what will show in the model and not mangled python name
        verbose_name_plural = 'sermons'

    def __str__(self):
        # this is what is returned whenever a model instance is needed and coerced to be displayed as plain string

        return self.name

    def get_absolute_url(self):
        return reverse('sermons:sermon_list_by_name', args=[self.slug])


class Sermon_details(models.Model):
    sermon_name = models.ForeignKey(Sermon, related_name='sermons_details', blank=True)
    slug = models.SlugField(max_length=200, db_index=True)
    preacher_name = models.ForeignKey(Leadership, related_name='leaders_details', blank=True)
    image = models.ImageField(blank=True)
    details = models.TextField(blank=True)
    text = models.CharField(max_length=100)
    audio_link = models.CharField(max_length=200, blank=True)
    video_link = models.CharField(max_length=200, blank=True)
    download_link = models.CharField(max_length=200, blank=True)
    date = models.DateTimeField()
    recent = models.BooleanField(default=False)

    class Meta:
        ordering = ('sermon_name',)
        verbose_name = 'detail'  # in the admin site this is what will show in the model and not mangled python name
        verbose_name_plural = 'details'
        index_together = (('id', 'slug'),)

    def get_absolute_url(self):
        return reverse('sermons:sermon_detail', args=[self.id, self.slug])
