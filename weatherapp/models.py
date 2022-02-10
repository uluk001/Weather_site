from django.db import models

# Create your models here.
class Weather(models.Model):
    city = models.CharField(max_length=1000, verbose_name="Сохраненные города")