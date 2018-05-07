from django.test import TestCase
from garden_data.serializers import GardenDataSerializer
from garden_data.submodel.weather_station import WeatherStation

class GardenDataSerializerTestCase(TestCase):
    def setUp(self):
        weather_station = WeatherStation.objects.create(weather_station=1, description='test station')

    def test_create_garden_data_serializer(self):
        weather_station = WeatherStation.objects.create(weather_station=2, description='test station 2')
        garden_data = GardenDataSerializer.create(observation_timestamp='2018-01-01 11:59:00',
                                                weather_station=weather_station,
                                                soil_temp=50.8, air_temp=50.1,
                                                soil_moisture=50.0)
        self.assertEqual(1, garden_data.id)

    def test_update_garden_data(self):
        weather_station = WeatherStation.objects.create(weather_station=2, description='test station 2')
        garden_data = GardenDataSerializer.update(air_temp =100.0)
        self.assertEqual(100.0, garden_data.air_temp)
