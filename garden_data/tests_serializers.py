from django.test import TestCase
from django.utils.six import BytesIO
from rest_framework.renderers import JSONRenderer
from rest_framework.parsers import JSONParser
from garden_data.submodel.weather_station import WeatherStation
from garden_data.serializers import WeatherStationSerializer
from garden_data.submodel.garden_data import GardenData
from garden_data.serializers import GardenDataSerializer


class GardenDataSerializerTestCase(TestCase):
    #def setUp(self):
    #    weather_station2 = WeatherStation(weather_station='2', description='test 2')
    #    weather_station2.save()

    def test_create_weatherstation(self):
        json_string = '{"weather_station":1, "description": "orions garden weather station"}'
        json_bytes = bytes(json_string, encoding='UTF-8')
        stream = BytesIO(json_bytes)
        parser = JSONParser()
        parsed_station = parser.parse(stream)
        new_station_serializer = WeatherStationSerializer(data=parsed_station)
        if new_station_serializer.is_valid():
            new_station = new_station_serializer.save()
            self.assertEqual('orions garden weather station', new_station.description)

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

    def test_create_garden_data(self):
        weather_station1 = WeatherStation(weather_station='1', description='orions garden weather station')
        weather_station1.save()
        json_string = """
            {"observation_timestamp": "2018-01-01 11:59:00", "weather_station": 2,
                      "soil_temp": 97.8, "air_temp":50.0, "soil_moisture":50}
        """
        json_bytes = bytes(json_string, encoding='UTF-8')
        stream = BytesIO(json_bytes)
        parser = JSONParser()
        parsed_station = parser.parse(stream)
        new_data_serializer = GardenDataSerializer(data=parsed_station)
        if new_data_serializer.is_valid():
            new_data = new_data_serializer.save()
            self.assertEqual(97.8, new_data.soil_temp)

    def test_update_garden_data(self):
        weather_station1 = WeatherStation(weather_station='1', description='orions garden weather station')
        weather_station1.save()
        json_string = """
            {"observation_timestamp": "2018-01-01 11:59:00", "weather_station": 2,
                      "soil_temp": 95.8, "air_temp":50.0, "soil_moisture":50}
        """
        json_bytes = bytes(json_string, encoding='UTF-8')
        stream = BytesIO(json_bytes)
        parser = JSONParser()
        parsed_station = parser.parse(stream)
        new_data_serializer = GardenDataSerializer(data=parsed_station)
        if new_data_serializer.is_valid():
            new_data = new_data_serializer.save()
            self.assertEqual(95.8, new_data.soil_temp)