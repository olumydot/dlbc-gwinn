from django.db import models
from django.core.urlresolvers import reverse


class Leadership(models.Model):
    name = models.CharField(max_length=200, db_index=True)  # adding db_index will help optimize lookups on this field
    slug = models.SlugField(max_length=200, db_index=True, unique=True)

    class Meta:
        ordering = ('name',)  # This is to order the database in ascending order of name
        verbose_name = 'leader'  # in the admin site this is what will show in the model and not mangled python name
        verbose_name_plural = 'leaders'

    def __str__(self):
        # this is what is returned whenever a model instance is needed and coerced to be displayed as plain string

        return self.name

    def get_absolute_url(self):
        return reverse('leadership:leadership_list_by_name', args=[self.slug])


class LeaderBio(models.Model):
    leader_name = models.ForeignKey(Leadership, related_name='leaders_bio')
    slug = models.SlugField(max_length=200, db_index=True)
    leader_position = models.CharField(max_length=200, db_index=True)
    Leader_ministry = models.CharField(max_length=200, db_index=True)
    bio = models.TextField(blank=True)
    Leader_facebook = models.CharField(max_length=200, blank=True)
    Leader_twitter = models.CharField(max_length=200, blank=True)
    Leader_instagram= models.CharField(max_length=200, blank=True)
    Leader_email = models.EmailField(max_length=200, blank=True)
    lead_pastor = models.BooleanField(default=False)
    leader_image = models.ImageField(blank=True)

    class Meta:
        ordering = ('leader_name',)
        verbose_name = 'bio'  # in the admin site this is what will show in the model and not mangled python name
        verbose_name_plural = 'bio'
        index_together = (('id', 'slug'),)

    def get_absolute_url(self):
        return reverse('leadership:leader_detail', args=[self.id, self.slug])
