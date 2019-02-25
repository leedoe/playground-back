from django.db import models

# Create your models here.
class Workshop(models.Model):
  name = models.CharField(max_length=100)
  address = models.CharField(max_length=200)
  latitude = models.CharField(max_length=5)
  longitude = models.CharField(max_length=5)