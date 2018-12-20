from django.db import models


class Livestream(models.Model):
    program = models.CharField(max_length=200)
    imaage = models.ImageField()
    livestream_link = models.CharField(max_length=200)
    description = models.CharField(max_length=300, blank=True)
    live = models.BooleanField(default=False)
