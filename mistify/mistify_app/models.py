from django.db import models
from django.contrib.auth.models import User
from datetime import datetime

class Result(models.Model):
    d=datetime.now()
    d=d.strftime('%I:%M %p, %b %w, %Y')
    user = models.ForeignKey('auth.User', null=False, on_delete=models.CASCADE)
    spot_un = models.CharField('spotify Username', max_length=100)
    city = models.CharField(max_length=100)
    country = models.CharField('2-letter Country Code', max_length=2)
    image = models.URLField(max_length=200, null=True)
    playlist = models.CharField(max_length=200, null=True)
    w_desc = models.CharField(max_length=100)
    temp = models.CharField(max_length=5)
    cloudy = models.CharField(max_length=100)
    humid = models.CharField(max_length=100)
    datetime = models.CharField(default=d, max_length=50)

    def __str__(self):
        return f'{self.city}, {self.country} ({self.datetime})'
