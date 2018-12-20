from django.db import models
from django.core.urlresolvers import reverse


class Ministry(models.Model):
    name = models.CharField(max_length=200, db_index=True)  # adding db_index will help optimize lookups on this field
    slug = models.SlugField(max_length=200, db_index=True, unique=True)

    class Meta:
        ordering = ('name',)  # This is to order the database in ascending order of name
        verbose_name = 'ministry'  # in the admin site this is what will show in the model and not mangled python name
        verbose_name_plural = 'ministries'

    def __str__(self):
        # this is what is returned whenever a model instance is needed and coerced to be displayed as plain string

        return self.name

    def get_absolute_url(self):
        return reverse('ministries:ministry_list_by_name', args=[self.slug])


class Ministry_details(models.Model):
    ministry_name = models.ForeignKey(Ministry, related_name='ministries_details', blank=True)
    slug = models.SlugField(max_length=200, db_index=True)
    Age = models.CharField(max_length=200, blank=True)
    image = models.ImageField(blank=True)
    details = models.TextField(blank=True)

    class Meta:
        ordering = ('ministry_name',)
        verbose_name = 'detail'  # in the admin site this is what will show in the model and not mangled python name
        verbose_name_plural = 'details'
        index_together = (('id', 'slug'),)

    def get_absolute_url(self):
        return reverse('ministries:ministry_detail', args=[self.id, self.slug])
