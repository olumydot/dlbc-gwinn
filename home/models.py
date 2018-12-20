from django.db import models
# from django.core.urlresolvers import reverse
# Create your models here.


# class SliderCarousel(models.Model):
#     name = models.CharField(max_length=200, db_index=True)  # adding db_index will help optimize lookups on this field
#     slug = models.SlugField(max_length=200, db_index=True, unique=True)
#     carouselImage = models.ImageField(upload_to='carousel/%Y/%m/%d', blank=False)
#     carouselButtonCharacter = models.CharField(max_length=200, db_index=True)


class SliderCarousel(models.Model):
    name = models.CharField(max_length=200, db_index=True)  # adding db_index will help optimize lookups on this field
    slug = models.SlugField(max_length=200, db_index=True, unique=True)
    body = models.CharField (max_length=100)
    carouselImage = models.ImageField(upload_to='carousel/%Y/%m/%d', blank=False)
    carouselButtonCharacter = models.CharField(max_length=200, db_index=True)


class WelcomeMessage(models.Model):
    title = models.CharField(max_length=200, db_index=True)
    welcomeVideoImage = models.ImageField(upload_to='welcome/%Y/%m/%d', blank=False)
    welcomeVidieoLink = models.CharField(max_length=200)
    body = models.TextField()


class IconBox(models.Model):
    title = models.CharField(max_length=200, db_index=True)
    body = models.CharField(max_length=100)
    iconImage = models.ImageField(upload_to='icon/%Y/%m/%d', blank=False)
    iconButtonCharacter = models.CharField(max_length=200, db_index=True)

    class Meta:
        verbose_name = 'Icon Box'  # in the admin site this is what will show in the model and not mangled python name
        verbose_name_plural = 'Icon Boxes'


class SpecialEvent(models.Model):
    title = models.CharField(max_length=200, db_index=True)
    datetime = models.CharField(max_length=100)
    address = models.CharField(max_length=200)
    flier = models.ImageField(upload_to='specialevent/%Y/%m/%d', blank=False)


class QuotableQuotes(models.Model):
    quote = models.TextField()
    verse = models.CharField(max_length=50)
    version = models.CharField(max_length=50)


class QuotableImage(models.Model):
    imagename = models.CharField(max_length=200, db_index=True)
    image = models.ImageField(upload_to='quotable/%Y/%m/%d', blank=False)


class Ministries(models.Model):
    ministry = models.CharField(max_length=200, db_index=True)
    age = models.CharField(max_length=200, db_index=True)
    image = models.ImageField(upload_to='ministries/%Y/%m/%d', blank=False)

