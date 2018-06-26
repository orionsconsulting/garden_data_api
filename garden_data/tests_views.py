from django.test import TestCase
from django.test import Client
from garden_data.submodel.weather_station import WeatherStation
import json


class GardenDataViewTestCase(TestCase):
    def test_fetch_weather_station_list_get(self):
        client = Client()
        response = client.get('/weather_station/')
        self.assertEqual(200, response.status_code)

    def test_fetch_weather_station_list_post(self):
        client = Client()
        json_data = json.dumps({"weather_station": 1})
        response = client.post('/weather_station/', data=json_data, content_type='json')
        self.assertEqual(400, response.status_code)
        json_data = json.dumps({"weather_station": 1, "description": "orions garden weather station"})
        response = client.post('/weather_station/', data=json_data, content_type='json')
        self.assertEqual(201, response.status_code)

    def test_fetch_single_station_by_id_get(self):
        client = Client()
        response = client.get('/weather_station/1/')
        self.assertEqual(404, response.status_code)
        WeatherStation.objects.create(weather_station=2, description='test station 2')
        client = Client()
        response = client.get('/weather_station/1/')
        self.assertEqual(200, response.status_code)

    def test_put_single_station_by_id(self):
        client = Client()
        json_data = json.dumps({"weather_station": 1})
        response = client.post('/weather_station/', data=json_data, content_type='json')
        self.assertEqual(400, response.status_code)
        json_data = json.dumps({"weather_station": 1, "description": "orions garden weather station"})
        response = client.post('/weather_station/', data=json_data, content_type='json')
        self.assertEqual(201, response.status_code)

    def test_delete_single_station_by_id(self):
        weather_station = WeatherStation.objects.create(weather_station=2, description='test station 2')
        client = Client()
        response = client.delete('/weather_station/1/')
        self.assertEqual(204, response.status_code)