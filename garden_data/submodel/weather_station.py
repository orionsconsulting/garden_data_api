from django.db import models

class WeatherStation(models.Model):
    weather_station = models.IntegerField()
    description = models.CharField(max_length=255)

    class Meta:
        db_table = 'weather_station'
        indexes = [
            models.Index(fields=['weather_station']),
        ]