from django.test import TestCase
from django.utils.six import BytesIO
from rest_framework.renderers import JSONRenderer
from rest_framework.parsers import JSONParser
from garden_data.submodel.weather_station import WeatherStation
from garden_data.serializers import WeatherStationSerializer


class GardenDataSerializerTestCase(TestCase):
    #def setUp(self):
    #    weather_station2 = WeatherStation(weather_station='2', description='test 2')
    #    weather_station2.save()

    def test_create_weatherstation(self):
        weather_station1 = WeatherStation(weather_station='1', description='orions garden weather station')
        weather_station1.save()
        self.assertEqual('orions garden weather station', weather_station1.description)

    def test_weather_station_update(self):
        json_string = '{"weather_station": 2, "description": "test_2"}'
        json_bytes = bytes(json_string, encoding='UTF-8')
        stream = BytesIO(json_bytes)
        parser = JSONParser()
        parsed_station = parser.parse(stream)
        new_station_serializer = WeatherStationSerializer(data=parsed_station)
        if new_station_serializer.is_valid():
            new_station = new_station_serializer.save()
        self.assertEqual(2, new_station.weather_station)


#http://www.django-rest-framework.org/api-guide/parsers/#jsonparser
#http://www.django-rest-framework.org/tutorial/1-serialization/