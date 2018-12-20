from django.db import models

# Create your models here.


class OurContact(models.Model):
    Address = models.TextField()
    PhoneNumber = models.CharField(max_length=12)
    E_mail = models.EmailField()
    location_map = models.TextField(blank=True)


class OtherCloserLocations(models.Model):
    location_Name = models.CharField(max_length=200, db_index=True)
    location_Address = models.CharField(max_length=200, db_index=True)
    location_PhoneNumber = models.CharField(max_length=12)
    location_E_mail = models.EmailField()
    location_map = models.TextField(blank=True)


class GetUserData(models.Model):
    Name = models.CharField(max_length=200, db_index=True)
    Email = models.EmailField()
    Phone = models.CharField(max_length=12)
    Interest = models.CharField(max_length=200)
    Message = models.TextField()

