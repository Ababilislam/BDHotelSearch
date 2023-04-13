from django.db import models


# Create your models here.
class Freatures(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name


class Hotels(models.Model):
    hotel_name = models.CharField(max_length=100)
    hotel_description = models.TextField()
    hotel_image = models.CharField(max_length=200)
    # price = models.DecimalField(max_digits=6, decimal_places=2
    price = models.IntegerField(default=0)
    features = models.ManyToManyField(Freatures)

    def __str__(self):
        return self.hotel_name
