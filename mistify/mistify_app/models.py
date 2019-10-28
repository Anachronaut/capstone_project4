from django.db import models
from django.contrib.auth.models import User

class Place(models.Model):
    user = models.ForeignKey('auth.User', null=False, on_delete=models.CASCADE)
    city = models.CharField(max_length=100)
    country = models.CharField(max_length=2)

    def __str__(self):
        return f'{self.city}, {self.country}'

class Weather(models.Model):
    user = models.ForeignKey('auth.User', null=False, on_delete=models.CASCADE)
    w_desc = models.CharField(max_length=100)
    temp = models.CharField(max_length=5)
    cloudy = models.CharField(max_length=100)
    humid = models.CharField(max_length=100)
