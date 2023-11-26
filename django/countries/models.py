from django.db import models

class Country(models.Model):
    id = models.AutoField(primary_key=True)
    alpha2 = models.CharField(max_length=3, unique=True)
    alpha3 = models.CharField(max_length=3, unique=True)
    country = models.CharField(max_length=128, unique=True)

