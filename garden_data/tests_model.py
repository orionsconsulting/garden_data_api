from django.test import TestCase
from garden_data.submodel.garden_data import GardenData
from garden_data.submodel.weather_station import WeatherStation

class WeatherstationTestCase(TestCase):
    def setUp(self):
        weather_station = WeatherStation.objects.create(weather_station=1, description='test station')

    def test_create_weather_station(self):
        weather_station = WeatherStation.objects.create(weather_station=2, description='test station 2')
        self.assertEqual(2, weather_station.id)

    def test_read_weather_station(self):
        weather_station = WeatherStation.objects.filter(id=1)
        self.assertEqual('test station', weather_station[0].description)

    def test_update_weather_stations(self):
        weather_station = WeatherStation.objects.filter(id=1)
        for w in weather_station:
            w.description = 'new description'
            w.save()
        new_weather_station = WeatherStation.objects.filter(id=1)
        self.assertEqual('new description', new_weather_station[0].description)

    def test_delete_weather_staion(self):
        weather_station = WeatherStation.objects.filter(id=1)
        weather_station.delete()
        new_weather_station = WeatherStation.objects.filter(id=1).count()
        self.assertEqual(0, new_weather_station)

class GardenDataTestCase(TestCase):
    def setUp(self):
        weather_station = WeatherStation.objects.create(weather_station=1, description='test station')
        GardenData.objects.create(observation_timestamp='2018-01-01 11:59:00', weather_station=weather_station,
                                  soil_temp=97.8, air_temp=50.0,
                                  soil_moisture=50)

    def test_create_garden_data(self):
        weather_station = WeatherStation.objects.create(weather_station=2, description='test station 2')
        garden_data = GardenData.objects.create(observation_timestamp='2018-01-01 11:59:00', weather_station=weather_station,
                                  soil_temp=50.8, air_temp=50.1,
                                  soil_moisture=50.0)
        self.assertEqual(2, garden_data.id)

    def test_read_garden_data(self):
        garden_data = GardenData.objects.filter(id=1)
        self.assertAlmostEquals(97.8, float(garden_data[0].soil_temp))

    def test_update_garden_data(self):
        garden_data = GardenData.objects.filter(id=1)
        for g in garden_data:
            g.air_temp = 97.8
            g.save()
        new_garden_data = GardenData.objects.filter(id=1)
        self.assertEqual(97.8, float(new_garden_data[0].air_temp))

    def test_delete_garden_data(self):
        garden_data = GardenData.objects.filter(id=1)
        garden_data.delete()
        new_garden_data = GardenData.objects.filter(id=1).count()
        self.assertEqual(0, new_garden_data)
