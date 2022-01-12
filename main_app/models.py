from django.db import models

# Create your models here.


class Card(models.Model):
    name = models.CharField(max_length=100)
    position = models.CharField(max_length=100)
    seasons = models.IntegerField()
    brand = models.CharField(max_length=100)
    year = models.IntegerField()
