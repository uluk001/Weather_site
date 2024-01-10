from django.db import models

class WeatherData(models.Model):
    city = models.CharField(max_length=255)
    temperature = models.FloatField()
    pressure = models.FloatField()
    wind_speed = models.FloatField()
    timestamp = models.DateTimeField(auto_now=True)
