from django.db import models
# from django.core.urlresolvers import reverse
# Create your models here.


class AboutUsPix(models.Model):
    header = models.CharField(max_length=200, db_index=True)  # adding db_index will help optimize lookups on this field
    image = models.ImageField()


class AboutUsHeading(models.Model):
    header = models.CharField(max_length=200, db_index=True)  # adding db_index will help optimize lookups on this field
    slug = models.SlugField(max_length=200, db_index=True, unique=True)
    body = models.CharField (max_length=5000, db_index=True)


class Beliefs1(models.Model):
    header = models.CharField (max_length=200, db_index=True)
    body = models.CharField(max_length=5000, db_index=True)


class Beliefs2 (models.Model):
    header = models.CharField (max_length=200, db_index=True)
    body = models.CharField (max_length=5000, db_index=True)


class Beliefs3 (models.Model):
    header = models.CharField (max_length=200, db_index=True)
    body = models.CharField (max_length=5000, db_index=True)




