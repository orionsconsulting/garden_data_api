from django.db import models
from garden_data.submodel.weather_station import WeatherStation

class GardenData(models.Model):
    observation_timestamp = models.DateTimeField()
    weather_station = models.ForeignKey(WeatherStation, on_delete=models.CASCADE, related_name="weather_station_id")
    soil_temp = models.DecimalField(max_digits=4, decimal_places=1)
    air_temp = models.DecimalField(max_digits=4, decimal_places=1)
    soil_moisture = models.DecimalField(max_digits=4, decimal_places=1)

    class Meta:
        db_table = 'garden_data'
        indexes = [
            models.Index(fields=['weather_station', 'observation_timestamp']),
        ]