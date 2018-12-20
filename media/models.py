from django.db import models

# Create your models here.


class MediaUploads(models.Model):
    PictureName = models.CharField (max_length=200, db_index=True)
    MediaImage = models.ImageField(upload_to='mediafolder/%Y/%m/%d', blank=False)
    carouselButtonCharacter = models.CharField(max_length=200, db_index=True)
    slug = models.SlugField(max_length=200, db_index=True, unique=True)