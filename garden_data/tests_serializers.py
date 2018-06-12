from django.test import TestCase
from django.http import HttpResponse, JsonResponse
from django.views.decorators.csrf import csrf_exempt
from rest_framework.renderers import JSONRenderer
from rest_framework.parsers import JSONParser
from garden_data.submodel.weather_station import WeatherStation
from garden_data.serializers import WeatherStationSerializer


class GardenDataSerializerTestCase(TestCase):
    #def setUp(self):
    #    weather_station = WeatherStation.objects.create(weather_station=1, description='test station')

    def test_create_weatherstation_serializer(self):
        weather_station1 = WeatherStation(weather_station='1', description='orions garden weather station')
        weather_station1.save()
        self.assertEqual('orions garden weather station', weather_station1.description)

    #def test_update_garden_data(self):
    #    weather_station = WeatherStation.objects.create(weather_station=2, description='test station 2')
    #    garden_data = GardenDataSerializer.update(1,'2018-01-01 11:59:00', weather_station, 97.8, 50.0, 50)
    #    self.assertEqual(100.0, garden_data.air_temp)

#http://www.django-rest-framework.org/api-guide/parsers/#jsonparser
#http://www.django-rest-framework.org/tutorial/1-serialization/