from django.db import models

class Place(models.Model):
    city = models.CharField(max_length=100)
    country = models.CharField(max_length=2)

    def __str__(self):
        return f'{self.city}, {self.country}'
